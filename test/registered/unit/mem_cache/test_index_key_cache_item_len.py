"""PD state stride of the DSA index-K cache -- CPU-only.

PD pages the DSA state with the device pool's 64-token kernel page and sends
target and draft entries with one index list, so every entry must report the
kernel page as its transfer stride, including a DCP-replicated draft pool whose
rows pack dcp_size kernel pages.
"""

import unittest
from types import SimpleNamespace

import torch

from sglang.srt.mem_cache.index_key_cache import IndexKeyCache
from sglang.test.ci.ci_register import register_cpu_ci
from sglang.test.test_utils import CustomTestCase

register_cpu_ci(est_time=2, suite="base-a-test-cpu")

INDEX_HEAD_DIM = 128
KERNEL_PAGE = 64
# 128 B of fp8 keys plus one 4 B scale per token.
KERNEL_PAGE_BYTES = KERNEL_PAGE * (INDEX_HEAD_DIM + 4)


def _cache(*, page_size, index_page_size, skip_topk_layers, num_pages=3):
    pool = SimpleNamespace(
        page_size=page_size,
        index_kpool=1,
        index_page_size=index_page_size,
        index_head_dim=INDEX_HEAD_DIM,
        quant_block_size=128,
        layer_num=len(skip_topk_layers),
        skip_topk_layers=list(skip_topk_layers),
    )
    cache = IndexKeyCache.__new__(IndexKeyCache)
    cache.pool = pool
    cache.buffer = [
        torch.zeros(
            cache._buffer_shape(cache._layer_num_pages(i, num_pages)),
            dtype=torch.uint8,
        )
        for i in range(pool.layer_num)
    ]
    return cache


class TestIndexKeyCacheItemLen(CustomTestCase):
    def test_dcp_replicated_draft_reports_kernel_page(self):
        # Decode draft under DCP4: rows span page_size * dcp = 256 virtual
        # tokens, i.e. four 64-token kernel pages.
        cache = _cache(
            page_size=KERNEL_PAGE * 4,
            index_page_size=KERNEL_PAGE,
            skip_topk_layers=[False],
        )
        self.assertEqual(cache.buffer[0][0].nbytes, 4 * KERNEL_PAGE_BYTES)
        _, _, item_lens = cache.state_buf_infos()
        self.assertEqual(item_lens, [KERNEL_PAGE_BYTES])

    def test_kernel_page_k_starts_at_k_times_item_len(self):
        # The transfer writes page k at base + k * item_len; that must be the
        # kernel view's page k, which the indexer reads for locs [64k, 64k+64).
        cache = _cache(
            page_size=KERNEL_PAGE * 4,
            index_page_size=KERNEL_PAGE,
            skip_topk_layers=[False],
        )
        buf = cache.buffer[0]
        kernel = cache._kernel_view(buf)
        _, _, (item_len,) = cache.state_buf_infos()
        for k in (0, 1, 5, kernel.shape[0] - 1):
            self.assertEqual(
                kernel[k].data_ptr() - buf.data_ptr(), k * item_len, msg=f"page {k}"
            )

    def test_unreplicated_pool_unchanged(self):
        cache = _cache(
            page_size=KERNEL_PAGE,
            index_page_size=KERNEL_PAGE,
            skip_topk_layers=[False, True, False],
        )
        _, data_lens, item_lens = cache.state_buf_infos()
        self.assertEqual(item_lens, [KERNEL_PAGE_BYTES, 0, KERNEL_PAGE_BYTES])
        self.assertEqual(data_lens[1], 0)

    def test_skip_topk_layer_reports_zero(self):
        cache = _cache(
            page_size=KERNEL_PAGE * 4,
            index_page_size=KERNEL_PAGE,
            skip_topk_layers=[True, False],
        )
        _, _, item_lens = cache.state_buf_infos()
        self.assertEqual(item_lens, [0, KERNEL_PAGE_BYTES])


if __name__ == "__main__":
    unittest.main()
