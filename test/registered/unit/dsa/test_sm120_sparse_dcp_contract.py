"""The SM120 sparse MLA backend must speak the DCP decode contract.

Under decode context parallelism each rank owns a disjoint shard of the KV cache,
so the model's attention forward calls the DCP query path and expects a partial
output plus its log-sum-exp, which it then combines across ranks with
``dcp_a2a_lse_reduce``. That means ``_forward_flashinfer_sparse_mla`` has to

* filter the shared top-k slots down to this rank's own rows and pack them,
* bound each row by the number of entries that survived, and
* ask FlashInfer for the LSE, returning ``(out, lse)``.

Without DCP the kernel returns a single tensor, and plain decode must stay
byte-identical to the non-DCP path.
"""

import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import torch

from sglang.srt.layers.attention.dsa_backend import DeepseekSparseAttnBackend
from sglang.test.ci.ci_register import register_cpu_ci

register_cpu_ci(est_time=3, suite="base-a-test-cpu")

KERNEL = "sglang.kernels.ops.attention.flash_mla_sm120.flashinfer_sparse_mla_forward"
LOCALIZE = "sglang.srt.layers.attention.dsa_backend.localize_dcp_page_table"
FIXUP = "sglang.srt.layers.attention.dsa_backend.fixup_zero_kv_rows"


def _backend(dcp_size):
    backend = DeepseekSparseAttnBackend.__new__(DeepseekSparseAttnBackend)
    backend.workspace_buffer = torch.zeros(8, dtype=torch.uint8)
    backend.dcp_size = dcp_size
    backend.dcp_rank = 0 if dcp_size == 1 else 2
    backend._dcp_page_table_cache = SimpleNamespace()
    backend.kv_cache_dim = 576
    backend.qk_nope_head_dim = 512
    backend.kv_lora_rank = 512
    backend.qk_rope_head_dim = 64
    backend.physical_page_size = 64
    backend.get_device_int32_arange = (
        lambda length: torch.arange(length, dtype=torch.int32)
    )
    return backend


def _call(backend, page_table, seq_lens, q_rows=4):
    return backend._forward_flashinfer_sparse_mla(
        q_all=torch.zeros(q_rows, 32, 576, dtype=torch.bfloat16),
        kv_cache=torch.zeros(16, 64, 576, dtype=torch.uint8),
        page_table_1=page_table,
        seq_lens=seq_lens,
        sm_scale=0.1,
        skip_softmax_threshold_scale_factor=None,
        metadata=SimpleNamespace(),
        layer=SimpleNamespace(layer_id=7),
        topk_indices=torch.zeros(q_rows, 8, dtype=torch.int32),
    )


class TestSm120SparseDcpContract(unittest.TestCase):
    def test_non_dcp_returns_the_kernel_result_unchanged(self):
        backend = _backend(dcp_size=1)
        page_table = torch.arange(32, dtype=torch.int32).view(4, 8)
        sentinel = torch.ones(4, 32, 512)
        with patch(KERNEL, return_value=sentinel) as kernel:
            out = _call(backend, page_table, torch.tensor([1, 2, 3, 4]))
        self.assertIs(out, sentinel)
        self.assertFalse(kernel.call_args.kwargs["return_lse"])
        # Plain decode keeps its own per-row lengths, not a page-table count.
        self.assertEqual(kernel.call_args.kwargs["seq_lens"].tolist(), [1, 2, 3, 4])

    def test_dcp_returns_output_and_lse(self):
        backend = _backend(dcp_size=4)
        page_table = torch.arange(32, dtype=torch.int32).view(4, 8)
        counts = torch.tensor([3, 0, 5, 1], dtype=torch.int32)
        localized = page_table.clone()
        out = torch.ones(4, 32, 512)
        lse = torch.zeros(4, 32)
        with patch(LOCALIZE, return_value=(localized, counts)) as localize, patch(
            KERNEL, return_value=(out, lse)
        ) as kernel, patch(FIXUP) as fixup:
            result = _call(backend, page_table, torch.tensor([9], dtype=torch.int32))

        self.assertIsInstance(result, tuple)
        self.assertIs(result[0], out)
        self.assertIs(result[1], lse)

        # The shared table is localized for this rank.
        self.assertEqual(localize.call_args.kwargs["dcp_size"], 4)
        self.assertEqual(localize.call_args.kwargs["dcp_rank"], 2)
        self.assertEqual(localize.call_args.kwargs["layer_id"], 7)

        # The kernel is bounded by the surviving entries, and never by zero.
        self.assertTrue(kernel.call_args.kwargs["return_lse"])
        self.assertEqual(
            kernel.call_args.kwargs["seq_lens"].tolist(), [3, 1, 5, 1]
        )
        # A row that lost every slot still points at a real page, so the kernel
        # has something to read before fixup blanks it.
        self.assertEqual(localized[1, 0].item(), 0)

        # fixup sees the true counts, not the clamped ones.
        self.assertEqual(fixup.call_args.args[2].tolist(), [3, 0, 5, 1])
        self.assertEqual(fixup.call_args.kwargs["max_seq_len"], 1)

    def test_dcp_is_skipped_when_only_one_rank(self):
        backend = _backend(dcp_size=1)
        page_table = torch.arange(32, dtype=torch.int32).view(4, 8)
        with patch(LOCALIZE) as localize, patch(
            KERNEL, return_value=torch.ones(4, 32, 512)
        ), patch(FIXUP) as fixup:
            _call(backend, page_table, torch.tensor([1, 2, 3, 4]))
        localize.assert_not_called()
        fixup.assert_not_called()


if __name__ == "__main__":
    unittest.main()
