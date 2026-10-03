"""Real loopback HTTP/SDK protocol tests, without an inference engine."""

import asyncio
import json
import unittest
from contextlib import asynccontextmanager
from pathlib import Path

from aiohttp import web

from sglang.benchmark.mixed_replay import replay_trace
from sglang.test.ci.ci_register import register_cpu_ci
from sglang.test.test_utils import CustomTestCase

register_cpu_ci(est_time=8, suite="base-a-test-cpu")


def _trace(*episodes):
    return {"synthetic": True, "episodes": list(episodes)}


def _episode(name, arrival_ms=0, turns=1):
    return {
        "id": name,
        "label": "synthetic",
        "arrival_ms": arrival_ms,
        "turns": [
            {
                "messages": [{"role": "user", "content": name}],
                "max_output_tokens": 8,
                "wait_before_ms": 0,
            }
            for _ in range(turns)
        ],
    }


class _ProtocolServer:
    def __init__(self):
        self.receipts = {}
        self.release = asyncio.Event()
        self.finish_sent = asyncio.Event()
        self.active = set()

    async def _chunk(self, response, rid, *, delta=None, finish=None, usage=None):
        chunk = {
            "id": f"server-{rid}",
            "object": "chat.completion.chunk",
            "created": 1,
            "model": "synthetic-model",
            "choices": (
                []
                if usage is not None
                else [{"index": 0, "delta": delta or {}, "finish_reason": finish}]
            ),
        }
        if usage is not None:
            chunk["usage"] = usage
        packet = b"data: " + json.dumps(chunk).encode() + b"\n\n"
        # Actual socket writes split a JSON frame; the SDK owns SSE parsing.
        await response.write(packet[: len(packet) // 2])
        await asyncio.sleep(0)
        await response.write(packet[len(packet) // 2 :])

    async def handle(self, request):
        task = asyncio.current_task()
        self.active.add(task)
        rid = request.headers["X-Replay-Request-ID"]
        self.receipts[rid] = await request.json()
        response = web.StreamResponse(headers={"Content-Type": "text/event-stream"})
        try:
            if rid == "http_error:0":
                return web.json_response(
                    {"error": {"message": "synthetic HTTP failure"}}, status=500
                )
            await response.prepare(request)
            await self._chunk(response, rid, delta={"role": "assistant"})
            await self._chunk(response, rid, delta={"reasoning_content": "reasoning"})
            if rid != "contentless:0":
                await self._chunk(response, rid, delta={"content": f"reply-{rid}"})
            if rid in ("active_cancel:0", "blocked:0"):
                await self.release.wait()
            if rid == "eof:0":
                await response.write_eof()
                return response
            await self._chunk(response, rid, finish="stop")
            if rid == "finish_usage:0":
                self.finish_sent.set()
                await self.release.wait()
            await self._chunk(
                response,
                rid,
                usage={
                    "prompt_tokens": 3,
                    "completion_tokens": 2,
                    "total_tokens": 5,
                    "prompt_tokens_details": {},
                },
            )
            await response.write(b"data: [DONE]\n\n")
            await response.write_eof()
        except (ConnectionResetError, asyncio.CancelledError):
            # Client cancellation need not immediately become a failed write.
            pass
        finally:
            self.active.remove(task)
        return response

    @asynccontextmanager
    async def serve(self):
        app = web.Application()
        app.router.add_post("/v1/chat/completions", self.handle)
        runner = web.AppRunner(app, shutdown_timeout=1)
        await runner.setup()
        site = web.TCPSite(runner, "127.0.0.1", 0)
        await site.start()
        port = site._server.sockets[0].getsockname()[1]
        try:
            yield f"http://127.0.0.1:{port}/v1"
        finally:
            self.release.set()
            await asyncio.wait_for(runner.cleanup(), timeout=5)
            if self.active:
                raise AssertionError("protocol handlers did not terminate")


class TestMixedReplay(CustomTestCase):
    def test_mixed_turn_permits_and_cancellation(self):
        async def run():
            trace = json.loads(
                (Path(__file__).parent / "fixtures" / "mixed_replay.json").read_text()
            )
            server = _ProtocolServer()
            async with server.serve() as base_url:
                output = await asyncio.wait_for(
                    replay_trace(
                        trace,
                        base_url=base_url,
                        model="synthetic-model",
                        total_timeout_s=3,
                    ),
                    timeout=5,
                )
            records = {record["id"]: record for record in output}
            self.assertEqual(len(records), 9)
            for rid in (
                "agent:0",
                "agent:1",
                "short:0",
                "long:0",
                "burst_a:0",
                "burst_b:0",
            ):
                self.assertEqual(
                    records[rid]["status"], "completed", records[rid]["error"]
                )
            self.assertEqual(
                {record["label"] for record in output},
                {"agent", "short", "long", "cancel", "burst"},
            )
            queued = records["queued_cancel:0"]
            self.assertEqual(queued["status"], "cancelled")
            self.assertIsNone(queued["dispatch_s"])
            self.assertNotIn(queued["id"], server.receipts)
            active = records["active_cancel:0"]
            self.assertEqual(active["status"], "cancelled")
            self.assertEqual(active["generated_text"], "reply-active_cancel:0")
            self.assertIsNone(active["completion_s"])
            self.assertEqual(records["active_cancel:1"]["status"], "suppressed")
            self.assertNotIn("active_cancel:1", server.receipts)
            self.assertLess(
                records["short:0"]["dispatch_s"], records["agent:1"]["eligible_s"]
            )
            self.assertEqual(
                server.receipts["agent:1"]["messages"][1],
                {"role": "assistant", "content": "reply-agent:0"},
            )
            self.assertEqual(server.receipts["long:0"]["max_completion_tokens"], 1024)
            for record in output:
                self.assertIsNotNone(record["terminal_s"])
                self.assertIsNone(record["server_queue_s"])
                self.assertIsNone(record["cached_tokens"])
                if record["status"] == "completed":
                    self.assertEqual(record["generated_text"], f"reply-{record['id']}")
                    self.assertLessEqual(record["eligible_s"], record["dispatch_s"])
                    self.assertLessEqual(
                        record["dispatch_s"], record["first_content_s"]
                    )
                    self.assertLessEqual(
                        record["first_content_s"], record["completion_s"]
                    )
                    self.assertEqual(record["raw_usage"]["prompt_tokens_details"], {})

        asyncio.run(run())

    def test_eof_and_finish_before_final_usage(self):
        async def run():
            server = _ProtocolServer()
            async with server.serve() as base_url:
                task = asyncio.create_task(
                    replay_trace(
                        _trace(
                            _episode("eof"),
                            _episode("finish_usage"),
                            _episode("http_error"),
                            _episode("contentless"),
                        ),
                        base_url=base_url,
                        model="synthetic-model",
                        total_timeout_s=3,
                    )
                )
                try:
                    await asyncio.wait_for(server.finish_sent.wait(), timeout=2)
                    self.assertFalse(task.done())
                    server.release.set()
                    records = {
                        record["id"]: record
                        for record in await asyncio.wait_for(task, timeout=3)
                    }
                finally:
                    server.release.set()
                    task.cancel()
                    await asyncio.gather(task, return_exceptions=True)
            self.assertEqual(records["eof:0"]["status"], "incomplete")
            self.assertIsNone(records["eof:0"]["completion_s"])
            self.assertEqual(records["finish_usage:0"]["status"], "completed")
            self.assertEqual(records["finish_usage:0"]["raw_usage"]["total_tokens"], 5)
            self.assertEqual(records["http_error:0"]["status"], "error")
            self.assertIsNone(records["http_error:0"]["completion_s"])
            self.assertIsNotNone(records["http_error:0"]["terminal_s"])
            self.assertIsNone(records["http_error:0"]["cached_tokens"])
            self.assertIsNone(records["http_error:0"]["server_queue_s"])
            self.assertEqual(records["contentless:0"]["status"], "completed")
            self.assertIsNone(records["contentless:0"]["first_content_s"])
            self.assertEqual(records["contentless:0"]["generated_text"], "")

        asyncio.run(run())

    def test_global_deadline_includes_future_turns(self):
        async def run():
            server = _ProtocolServer()
            async with server.serve() as base_url:
                output = await asyncio.wait_for(
                    replay_trace(
                        _trace(_episode("blocked"), _episode("future", 1000, 2)),
                        base_url=base_url,
                        model="synthetic-model",
                        total_timeout_s=0.2,
                    ),
                    timeout=3,
                )
            records = {record["id"]: record for record in output}
            self.assertEqual(records["blocked:0"]["status"], "cancelled")
            self.assertEqual(records["future:0"]["status"], "cancelled")
            self.assertEqual(records["future:1"]["status"], "suppressed")
            self.assertIsNone(records["future:0"]["eligible_s"])
            self.assertIsNone(records["future:0"]["dispatch_s"])
            self.assertNotIn("future:0", server.receipts)
            self.assertTrue(all(record["terminal_s"] is not None for record in output))

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
