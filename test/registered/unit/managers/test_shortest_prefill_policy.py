"""Stdlib contract regressions for the production shortest-prefill policy."""

import ast
import importlib.util
import unittest
from enum import Enum
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "python/sglang/srt/managers/schedule_policy.py"
_ci_spec = importlib.util.spec_from_file_location(
    "ci_register", ROOT / "python/sglang/test/ci/ci_register.py"
)
_ci = importlib.util.module_from_spec(_ci_spec)
_ci_spec.loader.exec_module(_ci)
register_cpu_ci = _ci.register_cpu_ci
register_cpu_ci(est_time=1, suite="base-a-test-cpu")


def load_policy():
    tree = ast.parse(SOURCE.read_text())
    nodes = [
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef)
        and node.name in ("CacheAwarePolicy", "CacheAgnosticPolicy", "SchedulePolicy")
    ]
    future = ast.ImportFrom(
        module="__future__", names=[ast.alias(name="annotations")], level=0
    )
    namespace = {
        "Enum": Enum,
        "Union": __import__("typing").Union,
        "_ceil_div": lambda a, b: -(-a // b),
    }
    module = ast.fix_missing_locations(
        ast.Module(body=[future, *nodes], type_ignores=[])
    )
    exec(compile(module, str(SOURCE), "exec"), namespace)
    return SimpleNamespace(**namespace)


def request(rid, tokens, matched=0, arrived=0, outputs=0):
    return SimpleNamespace(
        rid=rid,
        origin_input_ids=[0] * tokens,
        output_ids=[0] * outputs,
        num_matched_prefix_tokens=matched,
        time_stats=SimpleNamespace(wait_queue_entry_time=arrived),
        full_untruncated_fill_ids=[0] * tokens,
        prefix_indices=[0] * matched,
    )


class TestShortestPrefillPolicy(unittest.TestCase):
    def test_production_policy_is_recognized(self):
        p = load_policy()
        policy = p.SchedulePolicy.__new__(p.SchedulePolicy)
        self.assertEqual(
            policy._validate_and_adjust_policy(
                "shortest-prefill-first", SimpleNamespace(disable=False)
            ),
            p.CacheAwarePolicy.SHORTEST_PREFILL_FIRST,
        )
        with self.assertRaises(ValueError):
            policy._validate_and_adjust_policy(
                "shortest-prefill-first", SimpleNamespace(disable=True)
            )
        self.assertEqual(
            policy._validate_and_adjust_policy("lpm", SimpleNamespace(disable=True)),
            p.CacheAgnosticPolicy.FCFS,
        )

    def test_uncached_work_ties_and_duplicate_deprioritization(self):
        p = load_policy()
        queue = [
            request("duplicate", 1),
            request("long", 200),
            request("later", 100, 90, 2),
            request("early", 20, 10, 1),
        ]
        p.SchedulePolicy._sort_by_shortest_prefill(queue, {"duplicate"})
        self.assertEqual(
            [r.rid for r in queue], ["early", "later", "long", "duplicate"]
        )
        self.assertEqual(
            p.SchedulePolicy._shortest_prefill_work(request("zero", 4, 100)), 1
        )
        self.assertEqual(
            p.SchedulePolicy._shortest_prefill_work(request("output", 4, 2, outputs=3)),
            5,
        )

    def test_chunk_reserves_page_aligned_capacity_for_shorter_requests(self):
        p = load_policy()
        policy = p.SchedulePolicy.__new__(p.SchedulePolicy)
        policy.policy = p.CacheAwarePolicy.SHORTEST_PREFILL_FIRST
        chunked = request("chunked", 4096)
        cases = [
            (1024, [request("short", 1)], 768),
            (1024, [request("a", 1), request("b", 300)], 256),
            (256, [request("short", 1)], None),
            (1024, [], None),
            (1024, [request("longer", 8192)], None),
        ]
        for budget, queue, expected in cases:
            with self.subTest(budget=budget, expected=expected):
                self.assertEqual(
                    policy.shortest_prefill_chunk_limit(chunked, queue, budget, 256),
                    expected,
                )
        policy.policy = p.CacheAgnosticPolicy.FCFS
        self.assertIsNone(
            policy.shortest_prefill_chunk_limit(
                chunked, [request("short", 1)], 1024, 256
            )
        )

    def test_actual_adder_applies_limit_without_changing_other_policies(self):
        tree = ast.parse(SOURCE.read_text())
        cls = next(
            n
            for n in tree.body
            if isinstance(n, ast.ClassDef) and n.name == "PrefillAdder"
        )
        method = next(
            n
            for n in cls.body
            if isinstance(n, ast.FunctionDef) and n.name == "add_chunked_req"
        )
        namespace = {"CLIP_MAX_NEW_TOKENS": 4096}
        module = ast.fix_missing_locations(ast.Module(body=[method], type_ignores=[]))
        exec(compile(module, str(SOURCE), "exec"), namespace)
        for limit, expected in [(None, 1024), (512, 512)]:
            with self.subTest(limit=limit):
                req = request("chunked", 4096)
                req.sampling_params = SimpleNamespace(max_new_tokens=16)
                req.retracted_stain = False
                req.set_extend_range = lambda start, end: setattr(
                    req, "extend_range", SimpleNamespace(length=end - start)
                )
                budgets = []
                adder = SimpleNamespace(
                    dllm_config=None,
                    rem_chunk_tokens=1024,
                    rem_total_tokens=2048,
                    is_hybrid_swa=False,
                    prefill_delayer_single_pass=None,
                    chunked_req_limit=limit,
                    can_run_list=[],
                    _mamba_gap_budget_for_req=lambda _: 0,
                    _update_prefill_budget=lambda *a, **k: budgets.append((a, k)),
                )
                self.assertIs(namespace["add_chunked_req"](adder, req), req)
                self.assertEqual(req.extend_range.length, expected)
                self.assertEqual(budgets[0][0][1], expected)
                self.assertEqual(adder.can_run_list, [req])

    def test_scheduler_and_adder_wire_reservation_into_existing_continuation(self):
        scheduler = (ROOT / "python/sglang/srt/managers/scheduler.py").read_text()
        policy = SOURCE.read_text()
        self.assertIn(
            "adder.chunked_req_limit = self.policy.shortest_prefill_chunk_limit(",
            scheduler,
        )
        self.assertIn("_rem_tokens = min(_rem_tokens, self.chunked_req_limit)", policy)
        args = (ROOT / "python/sglang/srt/server_args.py").read_text()
        self.assertIn('"shortest-prefill-first",', args)


if __name__ == "__main__":
    unittest.main()
