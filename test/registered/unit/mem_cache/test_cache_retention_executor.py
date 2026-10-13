"""Focused CPU tests for the native Unified/NIXL retention executor."""
# ruff: noqa: E402

from sglang.test.ci.ci_register import register_cpu_ci

register_cpu_ci(est_time=5, suite="base-a-test-cpu")

import unittest
from array import array
from types import SimpleNamespace
from unittest import TestCase, mock

import torch

from sglang.srt.managers.cache_controller import HiCacheController
from sglang.srt.mem_cache.hicache_storage import PoolName, PoolTransfer
from sglang.srt.mem_cache.hybrid_cache.hybrid_cache_controller import (
    HybridCacheController,
    StorageOperation,
)
from sglang.srt.mem_cache.unified_radix_cache import (
    UnifiedRadixCache,
    _RetentionTransaction,
)


class _Node:
    def __init__(self, node_id, key, parent=None):
        self.id = node_id
        self.key = key
        self.parent = parent


class TestCacheRetentionExecutor(TestCase):
    def _path_cache(self):
        root = _Node(0, [])
        first = _Node(1, [1, 2, 3, 4], root)
        second = _Node(2, [5, 6, 7, 8], first)
        nodes = {0: root, 1: first, 2: second}
        cache = UnifiedRadixCache.__new__(UnifiedRadixCache)
        cache.tree_core = SimpleNamespace(
            is_eagle=False,
            page_size=4,
            node_by_id=lambda node_id: nodes[node_id],
        )
        cache.match_prefix = lambda params: SimpleNamespace(
            full_kv_hit_length=len(params.key),
            best_match_node=nodes[len(params.key) // 4],
        )
        req = SimpleNamespace(
            origin_input_ids=array("q", range(8)),
            extra_key=None,
            cache_salt=None,
        )
        return cache, req

    def test_exact_aligned_path_success(self):
        cache, req = self._path_cache()
        self.assertEqual(cache._retention_path(req, 8), [1, 2])

    def test_unaligned_boundary_rejected_without_rounding(self):
        cache, req = self._path_cache()
        with self.assertRaisesRegex(ValueError, "not exactly representable"):
            cache._retention_path(req, 6)

    def test_multi_ttl_queues_max_covering_policy(self):
        cache = UnifiedRadixCache.__new__(UnifiedRadixCache)
        req = SimpleNamespace(rid="r")
        tx = _RetentionTransaction(req, {30: 8, 120: 4}, 2, mock.Mock(), set())
        cache._retention_transactions = {"r": tx}
        cache._retention_operation_rids = {}
        cache._retention_path = lambda _req, boundary: [1, 2] if boundary == 8 else [1]
        cache.ongoing_write_through = {}
        cache.hicache_storage_pass_prefix_keys = False
        cache.tree_core = SimpleNamespace(build_storage_backup_spec=lambda *_: object())
        writes = []

        def write(node_id, *, retention_duration_seconds, retention_rid):
            writes.append((node_id, retention_duration_seconds, retention_rid))
            return len(writes)

        cache.write_backup_storage = write
        cache._poll_cache_retention_transactions()
        self.assertEqual(writes, [(1, 30, "r"), (2, 30, "r"), (1, 120, "r")])

    def test_existing_page_renewal_counts_zero_creation(self):
        req = SimpleNamespace(
            origin_input_ids=array("q", range(8)),
            cached_tokens=8,
            cache_write_candidate_ranges=[],
        )
        UnifiedRadixCache.finalize_cache_retention_usage(req, {60: 8})
        self.assertEqual(req.cache_write_tokens, 0)
        self.assertEqual(req.cache_write_tokens_by_ttl, {60: 0})

    def _controller_operation(self, sidecar_results):
        controller = HybridCacheController.__new__(HybridCacheController)
        controller.page_size = 4
        controller.backup_skip = False
        controller.storage_backend = SimpleNamespace(
            batch_set_v2=lambda transfers, extra: sidecar_results
        )
        controller.should_backup = lambda transfer: True
        controller._resolve_sidecar_kv_derived_pool_transfers = lambda operation: None
        controller._resolve_sidecar_nonkv_derived_pool_transfers = lambda operation: (
            None
        )
        transfer = PoolTransfer(name=PoolName.SWA, keys=["page"])
        operation = StorageOperation(
            torch.tensor([0, 1, 2, 3]),
            [1, 2, 3, 4],
            hash_value=["page"],
            pool_transfers=[transfer],
            retention_duration_seconds=60,
        )
        return controller, operation

    def test_one_pool_failure_fails_operation(self):
        controller, operation = self._controller_operation({PoolName.SWA: [False]})
        with mock.patch.object(
            HiCacheController,
            "_page_backup",
            side_effect=lambda op: setattr(op, "completed_tokens", 4),
        ):
            controller._page_backup(operation)
        self.assertFalse(operation.success)

    def test_all_pools_success_and_duration_propagates(self):
        seen = []
        controller, operation = self._controller_operation({PoolName.SWA: [True]})
        controller.storage_backend.batch_set_v2 = lambda transfers, extra: (
            seen.append(extra.retention_duration_seconds) or {PoolName.SWA: [True]}
        )
        with mock.patch.object(
            HiCacheController,
            "_page_backup",
            side_effect=lambda op: setattr(op, "completed_tokens", 4),
        ):
            controller._page_backup(operation)
        self.assertTrue(operation.success)
        self.assertEqual(seen, [60])

    def test_one_rank_failure_reduces_to_failure(self):
        cache = UnifiedRadixCache.__new__(UnifiedRadixCache)
        cache._all_reduce = lambda tensor, op: tensor.fill_(0)
        self.assertFalse(cache._reduce_cache_retention_success(True))

    def test_terminal_not_ready_before_ack(self):
        cache = UnifiedRadixCache.__new__(UnifiedRadixCache)
        cache._retention_ready_outputs = []
        self.assertEqual(cache.take_cache_retention_ready_outputs(), [])

    def test_terminal_ready_only_after_finalize(self):
        cache = UnifiedRadixCache.__new__(UnifiedRadixCache)
        req = SimpleNamespace(
            rid="r",
            origin_input_ids=array("q", range(4)),
            cached_tokens=0,
            cache_write_candidate_ranges=[(0, 4)],
            cache_retention_output_deferred=True,
        )
        tx = _RetentionTransaction(req, {60: 4}, 1, mock.Mock(), set())
        cache._retention_transactions = {"r": tx}
        cache._retention_operation_rids = {}
        cache._retention_ready_outputs = []
        cache.dec_lock_ref = mock.Mock()
        cache._finish_cache_retention_transaction(tx, success=True)
        self.assertEqual(req.cache_write_tokens, 4)
        self.assertTrue(req.cache_retention_output_deferred)
        self.assertEqual(cache.take_cache_retention_ready_outputs(), [req])
        self.assertFalse(req.cache_retention_output_deferred)

    def test_abort_releases_unqueued_transaction_lock(self):
        cache = UnifiedRadixCache.__new__(UnifiedRadixCache)
        req = SimpleNamespace(rid="r")
        tx = _RetentionTransaction(req, {60: 4}, 1, mock.Mock(), set())
        cache._retention_transactions = {"r": tx}
        cache._retention_operation_rids = {}
        cache._retention_ready_outputs = []
        cache.dec_lock_ref = mock.Mock()
        cache.abort_cache_retention("r")
        cache.dec_lock_ref.assert_called_once()
        self.assertNotIn("r", cache._retention_transactions)

    def test_ordinary_request_has_no_retention_state_transition(self):
        cache = UnifiedRadixCache.__new__(UnifiedRadixCache)
        req = SimpleNamespace(cache_retention_intents=())
        cache.begin_cache_retention(req)
        self.assertFalse(hasattr(req, "cache_retention_output_deferred"))


if __name__ == "__main__":
    unittest.main()
