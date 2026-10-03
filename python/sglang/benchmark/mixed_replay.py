"""Small causal trace replay through the public OpenAI streaming API.

Times describe this client, not the engine queue, KV transfers, or cache hits.
The SDK parses SSE; completion requires a finish reason and normal iteration.
"""

import asyncio
import math
import time

from openai import AsyncOpenAI

from sglang.benchmark.datasets.common import DatasetRow
from sglang.benchmark.serving import get_request


async def replay_trace(
    trace: dict,
    *,
    base_url: str,
    model: str,
    max_in_flight: int = 1,
    total_timeout_s: float = 30.0,
    request_timeout_s: float = 10.0,
    api_key: str = "unused",
) -> list[dict]:
    """Replay synthetic episodes; each turn separately acquires a client permit.

    Episode arrivals are milliseconds from the trace origin (minimum zero).
    Later turns depend on actual replies and wait_before_ms after completion.
    cancel_after_ms runs from eligibility, including time waiting for a permit.
    dispatch_s is SDK invocation, not socket dispatch or server receipt.
    Missing server observations remain None; raw_usage preserves field presence.
    """
    episodes = trace["episodes"]
    if not episodes or min(e["arrival_ms"] for e in episodes) != 0:
        raise ValueError("episode arrivals must start at zero")
    if not isinstance(max_in_flight, int) or max_in_flight < 1:
        raise ValueError("max_in_flight must be a positive integer")
    for value in (total_timeout_s, request_timeout_s):
        if not math.isfinite(value) or value <= 0:
            raise ValueError("timeouts must be finite and positive")
    if len({e["id"] for e in episodes}) != len(episodes):
        raise ValueError("episode ids must be unique")
    for episode in episodes:
        if not episode["turns"] or episode["turns"][0]["wait_before_ms"] != 0:
            raise ValueError("episodes need turns, with no first-turn wait")
        for value in [episode["arrival_ms"]] + [
            turn.get(name, 0)
            for turn in episode["turns"]
            for name in ("wait_before_ms", "cancel_after_ms")
        ]:
            if not math.isfinite(value) or value < 0:
                raise ValueError("trace times must be finite and nonnegative")

    results = {}
    for episode in episodes:
        for index, _ in enumerate(episode["turns"]):
            results[episode["id"], index] = {
                "id": f"{episode['id']}:{index}",
                "label": episode["label"],
                "turn_index": index,
                "scheduled_arrival_s": None,
                "eligible_s": None,
                "dispatch_s": None,
                "first_content_s": None,
                "completion_s": None,
                "cancel_requested_s": None,
                "terminal_s": None,
                "status": "pending",
                "generated_text": "",
                "server_response_id": None,
                "raw_usage": None,
                "raw_sglext": None,
                "server_queue_s": None,
                "cached_tokens": None,
                "error": None,
            }
    permit = asyncio.Semaphore(max_in_flight)
    client = AsyncOpenAI(
        base_url=base_url,
        api_key=api_key,
        timeout=request_timeout_s,
        max_retries=0,
    )

    async def send_turn(turn, history, record):
        stream = None
        saw_finish = False
        try:
            async with permit:
                record["dispatch_s"] = time.perf_counter()
                stream = await client.chat.completions.create(
                    model=model,
                    messages=history,
                    max_completion_tokens=turn["max_output_tokens"],
                    stream=True,
                    stream_options={"include_usage": True},
                    extra_headers={"X-Replay-Request-ID": record["id"]},
                )
                try:
                    async for chunk in stream:
                        record["server_response_id"] = chunk.id
                        if chunk.usage is not None:
                            record["raw_usage"] = chunk.usage.model_dump(
                                exclude_unset=True
                            )
                            details = record["raw_usage"].get("prompt_tokens_details")
                            if details is not None:
                                record["cached_tokens"] = details.get("cached_tokens")
                        if "sglext" in (chunk.model_extra or {}):
                            record["raw_sglext"] = chunk.model_extra["sglext"]
                        for choice in chunk.choices:
                            content = choice.delta.content
                            if content:
                                if record["first_content_s"] is None:
                                    record["first_content_s"] = time.perf_counter()
                                record["generated_text"] += content
                            if choice.finish_reason is not None:
                                saw_finish = True
                finally:
                    await asyncio.wait_for(stream.close(), timeout=request_timeout_s)
            if saw_finish:
                record["status"] = "completed"
                record["completion_s"] = time.perf_counter()
            else:
                record["status"] = "incomplete"
                record["error"] = "stream ended without a finish reason"
        except asyncio.CancelledError:
            record["status"] = "cancelled"
            if record["cancel_requested_s"] is None:
                record["cancel_requested_s"] = time.perf_counter()
            raise
        except Exception as exc:
            record["status"] = "error"
            record["error"] = f"{type(exc).__name__}: {exc}"
        finally:
            record["terminal_s"] = time.perf_counter()

    async def cancel_turn(task, record, delay_ms):
        await asyncio.sleep(delay_ms / 1000)
        if not task.done():
            record["cancel_requested_s"] = time.perf_counter()
            task.cancel()

    async def run_episode(episode):
        history = []
        try:
            for index, turn in enumerate(episode["turns"]):
                record = results[episode["id"], index]
                if index:
                    previous = results[episode["id"], index - 1]
                    record["scheduled_arrival_s"] = (
                        previous["completion_s"] + turn["wait_before_ms"] / 1000
                    )
                    await asyncio.sleep(
                        max(0, record["scheduled_arrival_s"] - time.perf_counter())
                    )
                history.extend(turn["messages"])
                record["eligible_s"] = time.perf_counter()
                task = asyncio.create_task(send_turn(turn, list(history), record))
                timer = (
                    asyncio.create_task(
                        cancel_turn(task, record, turn["cancel_after_ms"])
                    )
                    if "cancel_after_ms" in turn
                    else None
                )
                try:
                    await task
                finally:
                    if timer is not None:
                        timer.cancel()
                        await asyncio.gather(timer, return_exceptions=True)
                if record["status"] != "completed":
                    return
                history.append(
                    {"role": "assistant", "content": record["generated_text"]}
                )
        except asyncio.CancelledError:
            pass
        finally:
            for index in range(len(episode["turns"])):
                record = results[episode["id"], index]
                if record["status"] == "pending":
                    record["status"] = "suppressed"
                    record["terminal_s"] = time.perf_counter()

    tasks = []
    rows = [
        DatasetRow(
            prompt=episode,
            prompt_len=0,
            output_len=episode["turns"][0]["max_output_tokens"],
            timestamp=episode["arrival_ms"],
        )
        for episode in episodes
    ]
    # Start planned arrivals after SDK setup, immediately before native replay.
    epoch = time.perf_counter()
    for episode in episodes:
        results[episode["id"], 0]["scheduled_arrival_s"] = (
            epoch + episode["arrival_ms"] / 1000
        )

    async def replay_arrivals():
        async for row in get_request(rows, float("inf"), use_trace_timestamps=True):
            tasks.append(asyncio.create_task(run_episode(row.prompt)))
        await asyncio.gather(*tasks)

    try:
        await asyncio.wait_for(replay_arrivals(), timeout=total_timeout_s)
    except asyncio.TimeoutError:
        for record in results.values():
            if record["status"] == "pending":
                record["status"] = (
                    "cancelled" if record["turn_index"] == 0 else "suppressed"
                )
                record["terminal_s"] = time.perf_counter()
                if record["status"] == "cancelled":
                    record["cancel_requested_s"] = record["terminal_s"]
                record["error"] = "global deadline"
    finally:
        for task in tasks:
            if not task.done():
                task.cancel()
        try:
            await asyncio.wait_for(
                asyncio.gather(*tasks, return_exceptions=True),
                timeout=request_timeout_s,
            )
        finally:
            await asyncio.wait_for(client.close(), timeout=request_timeout_s)
    return list(results.values())
