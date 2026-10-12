"""CPU contracts: real normalization/dispatch methods, fake scheduler collaborators.

These tests do not exercise CUDA or prove NIXL physical retirement.
"""

from __future__ import annotations

import ast
import asyncio
import copy
import importlib.util
import logging
import sys
import types
import unittest
import uuid
from collections import Counter
from contextlib import nullcontext
from dataclasses import dataclass, field
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "python/sglang/srt/managers/tokenizer_manager.py"
REGISTRY = ROOT / "python/sglang/test/ci/ci_register.py"
spec = importlib.util.spec_from_file_location("parallel_state_ci_register", REGISTRY)
assert spec is not None and spec.loader is not None
registry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(registry)
register_cpu_ci = registry.register_cpu_ci
register_cpu_ci(est_time=1, suite="base-a-test-cpu")


class TimeStats:
    def __init__(self, **kwargs):
        pass

    def set_created_time(self, value):
        pass

    def set_finished_time(self):
        pass


def req_state(outputs, finished, event, obj, time_stats):
    return SimpleNamespace(
        out_list=outputs,
        finished=finished,
        event=event,
        obj=obj,
        time_stats=time_stats,
        dispatched=False,
    )


def load_methods():
    module = types.ModuleType("parallel_state_contract")
    sys.modules[module.__name__] = module
    module.__dict__.update(
        ast=ast,
        asyncio=asyncio,
        copy=copy,
        uuid=uuid,
        Counter=Counter,
        dataclass=dataclass,
        field=field,
        get_return_hidden_states_mode=lambda v: v,
        logger=logging.getLogger(__name__),
        nullcontext=nullcontext,
        get_bool_env_var=lambda _: False,
        ReqState=req_state,
        APIServerReqTimeStats=TimeStats,
    )
    future = ast.ImportFrom("__future__", [ast.alias("annotations")], 0)
    io_tree = ast.parse(SOURCE.with_name("io_struct.py").read_text())
    generate = next(
        n
        for n in io_tree.body
        if isinstance(n, ast.ClassDef) and n.name == "GenerateReqInput"
    )
    exec(
        compile(
            ast.fix_missing_locations(ast.Module([future, generate], [])),
            str(SOURCE.with_name("io_struct.py")),
            "exec",
        ),
        module.__dict__,
    )
    tree = ast.parse(SOURCE.read_text())
    cls = next(
        n
        for n in tree.body
        if isinstance(n, ast.ClassDef) and n.name == "TokenizerManager"
    )
    names = {
        "_init_req_state",
        "_handle_batch_request",
        "_release_req_states_on_failure",
    }
    methods: list[ast.stmt] = [
        n
        for n in cls.body
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name in names
    ]
    container = ast.ClassDef("Manager", [], [], methods, [])
    exec(
        compile(
            ast.fix_missing_locations(ast.Module([future, container], [])),
            str(SOURCE),
            "exec",
        ),
        module.__dict__,
    )
    return module


class ParallelSampleStateRetirement(unittest.IsolatedAsyncioTestCase):
    def manager(self):
        module = load_methods()
        manager = module.Manager()
        manager.enable_trace = False
        manager.disaggregation_mode = "none"
        manager.rid_to_state = {}
        manager._should_use_batch_tokenization = lambda *_: False
        manager._dispatch_to_scheduler = lambda *_: None
        manager.abort_request = lambda rid: self.fail(f"unexpected abort: {rid}")
        return module, manager

    async def test_actual_normalization_allocates_only_original_batch_states(self):
        for batch in (1, 2, 4):
            for n in (1, 2, 3):
                with self.subTest(batch=batch, n=n):
                    module, manager = self.manager()
                    obj = module.GenerateReqInput(
                        text="test"
                        if batch == 1
                        else [f"test-{i}" for i in range(batch)],
                        sampling_params={"n": n},
                    )
                    obj.normalize_batch_and_arguments()
                    manager._init_req_state(obj)
                    original = (
                        {obj.rid} if obj.is_single else set(obj.rid[: obj.batch_size])
                    )
                    self.assertEqual(set(manager.rid_to_state), original)

    async def test_parallel_batch_completion_leaves_no_undispatched_states(self):
        for batch in (1, 2):
            for n in (2, 3):
                with self.subTest(batch=batch, n=n):
                    module, manager = self.manager()
                    obj = module.GenerateReqInput(
                        text=[f"test-{i}" for i in range(batch)],
                        sampling_params={"n": n},
                    )
                    obj.normalize_batch_and_arguments()
                    manager._init_req_state(obj)
                    dispatched = []

                    async def tokenize(sub):
                        return SimpleNamespace(
                            rid=sub.rid,
                            sampling_params=SimpleNamespace(max_new_tokens=2),
                        )

                    async def send(tokenized):
                        state = manager.rid_to_state[tokenized.rid]
                        state.dispatched = True
                        dispatched.append(tokenized.rid)

                    async def wait(sub, request):
                        # Stand-in for a terminal scheduler response, not a physical-I/O claim.
                        manager.rid_to_state.pop(sub.rid)
                        yield {"meta_info": {"id": sub.rid}}

                    async def collect(generators):
                        return [await generator.__anext__() for generator in generators]

                    manager._tokenize_one_request = tokenize
                    manager._send_one_request = send
                    manager._wait_one_response = wait
                    manager._collect_batch_responses = collect
                    outputs = [
                        value async for value in manager._handle_batch_request(obj)
                    ]
                    self.assertEqual(len(outputs[0]), batch * n)
                    self.assertEqual(len(dispatched), batch * (n + 1))
                    self.assertEqual(manager.rid_to_state, {})

    async def test_failure_cleanup_retains_dispatched_owners(self):
        _, manager = self.manager()
        manager.rid_to_state = {
            "local": SimpleNamespace(dispatched=False),
            "owner": SimpleNamespace(dispatched=True),
        }
        aborted = []
        manager.abort_request = aborted.append
        manager._release_req_states_on_failure({"local", "owner", "missing"})
        self.assertEqual(set(manager.rid_to_state), {"owner"})
        self.assertEqual(aborted, ["owner"])


if __name__ == "__main__":
    unittest.main()
