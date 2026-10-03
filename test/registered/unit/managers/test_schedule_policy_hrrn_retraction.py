import unittest
from array import array
from unittest.mock import MagicMock

import torch

from sglang.srt.managers.schedule_batch import Req
from sglang.srt.managers.schedule_policy import PrefillAdder, SchedulePolicy
from sglang.srt.mem_cache.base_prefix_cache import InsertParams
from sglang.srt.mem_cache.radix_cache import RadixCache, RadixKey
from sglang.srt.sampling.sampling_params import SamplingParams
from sglang.srt.server_args import ServerArgs, set_global_server_args_for_scheduler
from sglang.test.ci.ci_register import register_cpu_ci
from sglang.test.test_utils import CustomTestCase

register_cpu_ci(est_time=5, suite="base-a-test-cpu")


class TestSchedulePolicyHRRNRetraction(CustomTestCase):
    def setUp(self):
        set_global_server_args_for_scheduler(ServerArgs(model_path="dummy"))

    def make_retracted_req(self, cached_tokens=100):
        req = Req(
            "resume",
            "",
            array("q", range(100)),
            SamplingParams(max_new_tokens=512),
        )
        req.output_ids = array("q", [500] * 300)
        tree = RadixCache.create_simulated()
        # Another request can keep this prefix cached after this req releases KV.
        tokens = req.origin_input_ids + req.output_ids
        tree.insert(
            InsertParams(
                key=RadixKey(token_ids=tokens[:cached_tokens]),
                value=torch.arange(cached_tokens, dtype=torch.int64),
            )
        )
        req.reset_for_retract()
        return req, tree

    def make_policy(self, tree):
        return SchedulePolicy("hrrn", tree, False, False, False)

    def make_adder(self, tree, chunk_tokens=2048):
        allocator = MagicMock()
        allocator.available_size.return_value = 1_000_000
        running_batch = MagicMock()
        running_batch.reqs = []
        running_batch.batch_size.return_value = 0
        return PrefillAdder(
            page_size=1,
            tree_cache=tree,
            token_to_kv_pool_allocator=allocator,
            running_batch=running_batch,
            new_token_ratio=1.0,
            rem_input_tokens=2048,
            rem_chunk_tokens=chunk_tokens,
        )

    def test_retracted_cost_matches_native_prefill_debit(self):
        req, tree = self.make_retracted_req()
        self.assertTrue(req.is_retracted)
        self.assertEqual(len(req.output_ids), 300)
        self.assertEqual(req.num_matched_prefix_tokens, 0)
        policy = self.make_policy(tree)
        policy.calc_priority([req], processed_tokens=100_000)
        estimated_tokens = policy._uncached_len(req)
        req.init_next_round_input(tree)
        adder = self.make_adder(tree)
        adder.add_one_req(req, False, None)

        self.assertIn(req, adder.can_run_list)
        self.assertEqual(req.extend_range.length, 300)
        self.assertEqual(2048 - adder.rem_input_tokens, 300)
        self.assertEqual(estimated_tokens, req.extend_range.length)

    def test_requeued_request_does_not_bypass_aged_cold_request(self):
        resume, tree = self.make_retracted_req()
        # Mirror the scheduler's arrival snapshot when a req is requeued.
        resume.arrival_processed_tokens = 100_000
        cold = Req(
            "cold",
            "",
            array("q", range(10_000, 11_000)),
            SamplingParams(max_new_tokens=10),
        )
        cold.arrival_processed_tokens = 0
        queue = [resume, cold]
        self.make_policy(tree).calc_priority(queue, processed_tokens=100_000)

        self.assertEqual([req.rid for req in queue], ["cold", "resume"])

    def test_generated_prefix_hits_preserve_last_token_prefill(self):
        for cached_tokens, expected_tokens in [(250, 150), (400, 1)]:
            with self.subTest(cached_tokens=cached_tokens):
                req, tree = self.make_retracted_req(cached_tokens)
                policy = self.make_policy(tree)
                policy.calc_priority([req], processed_tokens=100_000)
                estimated_tokens = policy._uncached_len(req)
                req.init_next_round_input(tree)
                adder = self.make_adder(tree)
                adder.add_one_req(req, False, None)

                self.assertEqual(req.extend_range.length, expected_tokens)
                self.assertEqual(estimated_tokens, expected_tokens)

    def test_chunking_keeps_total_remaining_cost(self):
        req, tree = self.make_retracted_req()
        policy = self.make_policy(tree)
        policy.calc_priority([req], processed_tokens=100_000)
        estimated_tokens = policy._uncached_len(req)
        req.init_next_round_input(tree)
        adder = self.make_adder(tree, chunk_tokens=64)
        adder.add_one_req(req, False, None)

        self.assertIs(adder.new_chunked_req, req)
        self.assertEqual(req.extend_range.length, 64)
        self.assertEqual(2048 - adder.rem_input_tokens, 64)
        self.assertEqual(estimated_tokens, 300)

    def test_fresh_cached_request_still_prefills_last_token(self):
        _, tree = self.make_retracted_req()
        req = Req(
            "fresh",
            "",
            array("q", range(100)),
            SamplingParams(max_new_tokens=512),
        )
        policy = self.make_policy(tree)
        policy.calc_priority([req], processed_tokens=100_000)
        estimated_tokens = policy._uncached_len(req)
        req.init_next_round_input(tree)
        adder = self.make_adder(tree)
        adder.add_one_req(req, False, None)

        self.assertEqual(estimated_tokens, 1)
        self.assertEqual(req.extend_range.length, 1)
        self.assertEqual(2048 - adder.rem_input_tokens, 1)


if __name__ == "__main__":
    unittest.main()
