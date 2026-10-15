"""CPU contracts for DSA DCP page ownership and PD configuration."""

from types import SimpleNamespace

import numpy as np
import pytest
import torch

from sglang.srt.arg_groups.model_overrides.deepseek_v2 import _dsa_dcp_overrides
from sglang.srt.disaggregation.common.conn import CommonKVManager
from sglang.srt.disaggregation.common.utils import build_dcp_token_transfer_plan
from sglang.srt.disaggregation.utils import is_elided_entry
from sglang.srt.layers.attention.dsa.dsa_dcp import (
    chunk_cu_seqlens,
    dcp_token_seq_lens,
)
from sglang.test.ci.ci_register import register_cpu_ci

register_cpu_ci(est_time=5, suite="base-a-test-cpu")


def test_pd_dcp4_nextn_contract_keeps_dcp_defaults():
    cfg = SimpleNamespace(
        dcp_size=4,
        enable_hisparse=False,
        enable_hierarchical_cache=False,
        disaggregation_mode="decode",
        speculative_eagle_topk=1,
        dsa_prefill_backend=None,
        dsa_decode_backend=None,
        dcp_replicate_q_proj=None,
        dcp_comm_backend="a2a",
    )

    overrides = _dsa_dcp_overrides(cfg)

    assert overrides["dsa_prefill_backend"] == "trtllm"
    assert overrides["dsa_decode_backend"] == "trtllm"
    assert overrides["dcp_replicate_q_proj"] is True


def test_pd_dcp_rejects_hicache_layout():
    cfg = SimpleNamespace(
        dcp_size=4,
        enable_hisparse=False,
        enable_hierarchical_cache=True,
        disaggregation_mode="decode",
        speculative_eagle_topk=1,
        dsa_prefill_backend=None,
        dsa_decode_backend=None,
        dcp_replicate_q_proj=None,
        dcp_comm_backend="a2a",
    )

    with pytest.raises(ValueError, match="HiCache"):
        _dsa_dcp_overrides(cfg)


def test_pd_dcp_page_mapping_is_rank_local_and_draft_replicated():
    plans = [
        build_dcp_token_transfer_plan(
            np.array([10, 11, 12], dtype=np.int32),
            np.array([20, 21, 22], dtype=np.int32),
            physical_page_size=4,
            dcp_size=4,
            dcp_rank=rank,
            decode_prefix_len=0,
            num_kv_tokens=12,
        )
        for rank in range(4)
    ]

    # Target MLA pages are partitioned by DCP rank, while the built-in NEXTN
    # entry remains replicated in a virtual page of physical_page_size * DCP.
    assert [p.target_src_token_indices.tolist() for p in plans] == [
        [0, 4, 8],
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
    ]
    assert plans[0].draft_src_token_indices.tolist() == list(range(12))
    assert all(
        np.array_equal(p.draft_src_token_indices, plans[0].draft_src_token_indices)
        for p in plans
    )
    assert all(
        np.array_equal(p.draft_dst_token_indices, plans[0].draft_dst_token_indices)
        for p in plans
    )


def test_dcp_page_counts_never_become_token_seq_lens():
    # Four-token pages with a five-token request leave a partial final page.
    physical_page_size = 4
    cache_seqlens = torch.tensor([5, 8], dtype=torch.int32)
    localized_page_counts = (cache_seqlens + physical_page_size - 1) // physical_page_size
    assert torch.equal(
        dcp_token_seq_lens(cache_seqlens, localized_page_counts), cache_seqlens
    )
    assert not torch.equal(cache_seqlens, localized_page_counts)


def test_dcp_chunk_fixup_uses_chunk_base_for_nonuniform_cu_seqlens():
    cu_seqlens_q = torch.tensor([0, 2, 5, 6], dtype=torch.int32)
    assert torch.equal(
        chunk_cu_seqlens(cu_seqlens_q, 1, 3), torch.tensor([0, 3, 4])
    )


def test_zero_destination_elision_is_dsa_only():
    assert is_elided_entry(4, [0], 0, state_type="dsa")
    assert not is_elided_entry(4, [0], 0, state_type="swa")


def test_pd_dcp_rejects_dcp_to_dcp_relayout():
    manager = CommonKVManager.__new__(CommonKVManager)
    manager.dcp_size = 2
    manager.dcp_rank = 0
    manager.is_mla_backend = True
    manager.is_hybrid_mla_backend = False

    with pytest.raises(RuntimeError, match="Unsupported PD DCP topology"):
        manager.requires_dcp_relayout(dst_dcp_size=4, dst_dcp_rank=0)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
