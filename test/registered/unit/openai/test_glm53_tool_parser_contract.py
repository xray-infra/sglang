"""CPU call-site coverage; optionally replay captured serving source, never a server.

GLM53_REPLAY_SERVING_SOURCE=/path/to/captured-serving-chat.py.txt enables a
negative control: the captured methods execute against the real repository
parser/protocol classes. No GPU, HTTP requests, or patched live process is used.
"""

import ast
import json
import os
import types
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import create_autospec

from sglang.srt.entrypoints.openai import serving_chat
from sglang.srt.entrypoints.openai.protocol import ChatCompletionRequest, ToolChoice
from sglang.test.ci.ci_register import register_cpu_ci

register_cpu_ci(est_time=3, suite="base-a-test-cpu")

TEXT = "<tool_call>get_weather<arg_key>location</arg_key><arg_value>Paris</arg_value></tool_call>"
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "parameters": {
                "type": "object",
                "properties": {"location": {"type": "string"}},
                "required": ["location"],
            },
        },
    }
]
CHOICES = [
    "auto",
    "required",
    ToolChoice.model_validate({"function": {"name": "get_weather"}}),
]


def serving_instance():
    server = object.__new__(serving_chat.OpenAIServingChat)
    server.tool_call_parser = "glm47"
    # Avoid initializing GPU workers; only this manager dependency is a double.
    # The serving methods, protocol models and FunctionCallParser remain real.
    server.tokenizer_manager = create_autospec(SimpleNamespace(tokenizer=None))
    server.tokenizer_manager.tokenizer = None
    replay = os.environ.get("GLM53_REPLAY_SERVING_SOURCE")
    if replay:
        tree = ast.parse(Path(replay).read_text())
        cls = next(
            node
            for node in tree.body
            if isinstance(node, ast.ClassDef) and node.name == "OpenAIServingChat"
        )
        names = {"_process_tool_calls", "_process_tool_call_stream"}
        methods = [
            node
            for node in cls.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name in names
        ]
        if {node.name for node in methods} != names:
            raise ValueError(
                "Captured source must contain both real tool call-site methods"
            )
        namespace = vars(serving_chat).copy()
        # Preserve all real dependencies; replace only the captured call-site bodies.
        module = ast.Module(body=list[ast.stmt](methods), type_ignores=[])
        # Operator-selected trusted local capture only; never a live process.
        exec(compile(module, replay, "exec"), namespace)  # noqa: S102
        for name in names:
            setattr(server, name, types.MethodType(namespace[name], server))
    return server


def request(choice):
    return ChatCompletionRequest.model_validate(
        {
            "model": "zai-org/GLM-5.3",
            "messages": [{"role": "user", "content": "Call get_weather for Paris."}],
            "tools": TOOLS,
            "tool_choice": choice,
        }
    )


class TestGlm53NonstreamContract(unittest.TestCase):
    def test_auto_required_named_call_real_parser(self):
        for choice in CHOICES:
            with self.subTest(choice=choice):
                server = serving_instance()
                req = request(choice)
                result = server._process_tool_calls(
                    TEXT,
                    server._effective_tools(req),
                    {"type": "stop", "matched": None},
                    tool_choice=req.tool_choice,
                )
                calls = result.tool_calls
                if calls is None:
                    self.fail("Native tool call was not parsed")
                self.assertEqual(len(calls), 1)
                call = calls[0]
                self.assertEqual(call.function.name, "get_weather")
                self.assertEqual(
                    json.loads(call.function.arguments), {"location": "Paris"}
                )
                self.assertTrue(call.id)
                self.assertEqual(result.finish_reason["type"], "tool_calls")


class TestGlm53StreamContract(unittest.IsolatedAsyncioTestCase):
    async def test_auto_required_named_call_real_parser(self):
        for choice in CHOICES:
            for size in (1, 7, len(TEXT)):
                with self.subTest(choice=choice, chunk_size=size):
                    server = serving_instance()
                    req = request(choice)
                    parser_dict, has_calls = {}, {}
                    calls = []
                    for offset in range(0, len(TEXT), size):
                        async for event in server._process_tool_call_stream(
                            0,
                            TEXT[offset : offset + size],
                            parser_dict,
                            {"meta_info": {"id": "cpu-tool-contract"}},
                            req,
                            has_calls,
                        ):
                            chunk = json.loads(event.removeprefix("data: ").strip())
                            calls.extend(
                                chunk["choices"][0]["delta"].get("tool_calls") or []
                            )
                    self.assertTrue(has_calls.get(0))
                    self.assertEqual(
                        [c["function"]["name"] for c in calls if c["function"]["name"]],
                        ["get_weather"],
                    )
                    self.assertEqual({c["index"] for c in calls}, {0})
                    args = "".join(c["function"]["arguments"] or "" for c in calls)
                    self.assertEqual(json.loads(args), {"location": "Paris"})
                    self.assertEqual(len([c for c in calls if c["id"]]), 1)


if __name__ == "__main__":
    unittest.main()
