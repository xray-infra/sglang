"""CPU-only tests for UnifiedRadixCache request lock lifecycle."""

import unittest
from array import array
from types import SimpleNamespace
from unittest.mock import MagicMock

import torch

from sglang.srt.managers.kv_hints import KvHintAction, KvHintsEnvelope
from sglang.srt.mem_cache.base_prefix_cache import InsertResult
from sglang.srt.mem_cache.unified_cache.components import BASE_COMPONENT_TYPE
from sglang.srt.mem_cache.unified_radix_cache import UnifiedRadixCache
from sglang.test.ci.ci_register import register_cpu_ci

register_cpu_ci(est_time=2, suite="base-a-test-cpu")


class TestUnifiedRadixLockRefScenarios(unittest.TestCase):
    @staticmethod
    def _retained_req(prompt_len):
        return SimpleNamespace(
            origin_input_ids=array("q", range(prompt_len)),
            cache_write_tokens=None,
            cache_write_tokens_by_ttl=None,
            cached_tokens=0,
            cache_write_candidate_ranges=[],
            cache_retention_applied_prefix_lens={},
            kv_hints=KvHintsEnvelope(
                protocol_version="0.1",
                message_id="test",
                actions=[
                    KvHintAction(
                        action_id="retain",
                        action_type="kv.retain_prefix",
                        action_version="1.0",
                        payload={
                            "duration_seconds": 300,
                            "prefix_token_count": prompt_len,
                        },
                    )
                ],
            ),
        )

    def test_cache_write_counts_adopted_prompt_ranges_once(self):
        req = self._retained_req(10)
        result = InsertResult(
            prefix_len=8,
            adopted_ranges={
                BASE_COMPONENT_TYPE: [(0, 4), (4, 12)],
            },
        )

        UnifiedRadixCache._record_prompt_cache_write(req, result, inserted_len=12)
        self.assertIsNone(req.cache_write_tokens)
        UnifiedRadixCache.finalize_cache_retention_usage(req, {300: 10})

        self.assertEqual(req.cache_write_tokens, 10)
        self.assertEqual(req.cache_write_tokens_by_ttl, {300: 10})

    def test_cache_write_excludes_generated_tokens_and_accumulates(self):
        req = self._retained_req(8)
        first = InsertResult(
            prefix_len=0,
            adopted_ranges={BASE_COMPONENT_TYPE: [(0, 4)]},
        )
        second = InsertResult(
            prefix_len=4,
            adopted_ranges={BASE_COMPONENT_TYPE: [(4, 12)]},
        )

        UnifiedRadixCache._record_prompt_cache_write(req, first, inserted_len=4)
        UnifiedRadixCache._record_prompt_cache_write(req, second, inserted_len=12)
        self.assertIsNone(req.cache_write_tokens)
        UnifiedRadixCache.finalize_cache_retention_usage(req, {300: 8})

        self.assertEqual(req.cache_write_tokens, 8)
        self.assertEqual(req.cache_write_tokens_by_ttl, {300: 8})

    def test_cache_write_splits_applied_one_hour_and_five_minute_ranges(self):
        req = self._retained_req(12)
        req.cached_tokens = 2
        result = InsertResult(
            prefix_len=2,
            adopted_ranges={BASE_COMPONENT_TYPE: [(2, 12)]},
        )

        UnifiedRadixCache._record_prompt_cache_write(req, result, inserted_len=12)
        UnifiedRadixCache.finalize_cache_retention_usage(req, {3600: 8, 300: 12})

        self.assertEqual(req.cache_write_tokens, 10)
        self.assertEqual(req.cache_write_tokens_by_ttl, {300: 4, 3600: 6})

        UnifiedRadixCache.finalize_cache_retention_usage(req, {3600: 8, 300: 12})
        self.assertEqual(req.cache_write_tokens, 10)
        self.assertEqual(req.cache_write_tokens_by_ttl, {300: 4, 3600: 6})

    def test_failed_retention_publishes_explicit_zero_not_candidates(self):
        req = self._retained_req(8)
        result = InsertResult(
            prefix_len=0,
            adopted_ranges={BASE_COMPONENT_TYPE: [(0, 8)]},
        )

        UnifiedRadixCache._record_prompt_cache_write(req, result, inserted_len=8)
        UnifiedRadixCache.finalize_cache_retention_usage(req, {})

        self.assertEqual(req.cache_write_tokens, 0)
        self.assertEqual(req.cache_write_tokens_by_ttl, {})
        self.assertEqual(req.cache_retention_applied_prefix_lens, {})

    def test_automatic_cache_write_is_not_reported_as_billable_creation(self):
        req = SimpleNamespace(
            origin_input_ids=array("q", range(8)),
            cache_write_tokens=None,
            cache_write_tokens_by_ttl=None,
            cached_tokens=0,
            cache_retention_applied_prefix_lens={},
            kv_hints=None,
        )
        result = InsertResult(
            prefix_len=0,
            adopted_ranges={BASE_COMPONENT_TYPE: [(0, 8)]},
        )

        UnifiedRadixCache._record_prompt_cache_write(req, result, inserted_len=8)

        self.assertIsNone(req.cache_write_tokens)

    def test_no_insert_without_last_node_skips_lock_release(self):
        cache = object.__new__(UnifiedRadixCache)
        cache.session = MagicMock()
        cache.session.try_cache_finished_req.return_value = False
        cache.disable = False
        cache.req_to_token_pool = MagicMock()
        cache.req_to_token_pool.req_to_token = torch.arange(8).reshape(1, 8)
        cache.free_kv_row = MagicMock()
        cache._dec_req_lock = MagicMock()
        cache._components_tuple = ()
        cache.enable_session_radix_cache = False

        kv = SimpleNamespace(req_pool_idx=0, cache_protected_len=0)
        req = SimpleNamespace(
            origin_input_ids=array("q", [1, 2, 3]),
            output_ids=array("q"),
            kv=kv,
            last_node=None,
            swa_prefix_lock_released=False,
        )

        cache.cache_finished_req(req, is_insert=False, kv_len_to_handle=3)

        cache.free_kv_row.assert_called_once_with(kv, [(0, 3)])
        cache._dec_req_lock.assert_not_called()


if __name__ == "__main__":
    unittest.main()
