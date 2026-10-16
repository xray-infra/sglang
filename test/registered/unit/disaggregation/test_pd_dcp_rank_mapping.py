import unittest
from types import SimpleNamespace

from sglang.srt.disaggregation.common.conn import CommonKVManager
from sglang.test.ci.ci_register import register_cpu_ci
from sglang.test.test_utils import CustomTestCase

register_cpu_ci(est_time=2, suite="base-a-test-cpu")


def _target(*, decode_tp, decode_dcp, prefill_tp, engine_rank, hybrid=False):
    mgr = SimpleNamespace(
        attn_tp_size=decode_tp,
        kv_args=SimpleNamespace(engine_rank=engine_rank),
        is_mla_backend=not hybrid,
        is_hybrid_mla_backend=hybrid,
        dcp_size=decode_dcp,
        dcp_rank=engine_rank % decode_dcp,
        attn_cp_size=1,
        attn_cp_rank=0,
        enable_all_cp_ranks_for_transfer=False,
        pp_size=1,
        pp_rank=0,
    )
    info = SimpleNamespace(
        attn_tp_size=prefill_tp,
        attn_cp_size=1,
        pp_size=1,
        enable_dsa_cache_layer_split=False,
    )
    CommonKVManager._resolve_rank_mapping(mgr, info)
    return info


class TestDecodeDcpRankMapping(CustomTestCase):
    def test_decode_dcp_picks_prefill_rank_with_same_shard(self):
        # decode TP8/DCP4 <- prefill TP4/DCP4 (e.g. PP2 x TP4 prefill).
        targets = [
            _target(decode_tp=8, decode_dcp=4, prefill_tp=4, engine_rank=r)
            for r in range(8)
        ]
        self.assertEqual([t.target_tp_rank for t in targets], [0, 1, 2, 3] * 2)
        self.assertTrue(all(t.required_dst_info_num == 2 for t in targets))

    def test_decode_dcp_spans_multiple_prefill_dcp_groups(self):
        # decode TP16/DCP4 <- prefill TP8/DCP4: groups {0..3},{4..7} on prefill.
        got = [
            _target(
                decode_tp=16, decode_dcp=4, prefill_tp=8, engine_rank=r
            ).target_tp_rank
            for r in range(16)
        ]
        self.assertEqual(got, [0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 4, 5, 6, 7])

    def test_prefill_tp_below_dcp_keeps_block_mapping(self):
        # Prefill TP2 or TP1 cannot hold DCP4 shards; it runs DCP1 and the
        # sender relayouts 1 -> 4, so keep the original block mapping.
        for prefill_tp in (1, 2):
            ratio = 8 // prefill_tp
            got = [
                _target(
                    decode_tp=8, decode_dcp=4, prefill_tp=prefill_tp, engine_rank=r
                ).target_tp_rank
                for r in range(8)
            ]
            self.assertEqual(got, [r // ratio for r in range(8)])

    def test_hybrid_mla_keeps_block_mapping(self):
        # Hybrid-MLA state and draft head slicing derive source offsets from
        # the block mapping, so the shard-matching mapping is pure MLA only.
        got = [
            _target(
                decode_tp=8, decode_dcp=4, prefill_tp=4, engine_rank=r, hybrid=True
            ).target_tp_rank
            for r in range(8)
        ]
        self.assertEqual(got, [r // 2 for r in range(8)])

    def test_without_decode_dcp_mapping_is_unchanged(self):
        got = [
            _target(
                decode_tp=8, decode_dcp=1, prefill_tp=4, engine_rank=r
            ).target_tp_rank
            for r in range(8)
        ]
        self.assertEqual(got, [r // 2 for r in range(8)])

    def test_non_contiguous_dcp_group_fails_closed(self):
        # TP rank 1 claiming DCP rank 2 means DCP groups are not contiguous.
        mgr = SimpleNamespace(
            attn_tp_size=8,
            kv_args=SimpleNamespace(engine_rank=1),
            is_mla_backend=True,
            is_hybrid_mla_backend=False,
            dcp_size=4,
            dcp_rank=2,
            attn_cp_size=1,
            attn_cp_rank=0,
            enable_all_cp_ranks_for_transfer=False,
            pp_size=1,
            pp_rank=0,
        )
        info = SimpleNamespace(
            attn_tp_size=4,
            attn_cp_size=1,
            pp_size=1,
            enable_dsa_cache_layer_split=False,
        )
        with self.assertRaisesRegex(RuntimeError, "contiguous DCP groups"):
            CommonKVManager._resolve_rank_mapping(mgr, info)


if __name__ == "__main__":
    unittest.main()
