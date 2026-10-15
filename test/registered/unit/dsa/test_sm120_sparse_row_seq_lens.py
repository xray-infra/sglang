"""SM120 sparse MLA needs one index bound per query row.

FlashInfer's SM120 sparse MLA v32/GLM entry point derives its batch from the
query rows and rejects any ``seq_lens`` whose length is neither the row count nor
a (batch, q_len) pair. SGLang metadata supplies it per request, so extend batches
carry a tensor padded to the captured batch size and target verify keeps one entry
per request while the query holds one row per draft token. Both shapes must be
converted before the kernel sees them.
"""

import unittest

import torch

from sglang.srt.layers.attention.dsa_backend import _sm120_row_seq_lens
from sglang.test.ci.ci_register import register_cpu_ci

register_cpu_ci(est_time=2, suite="base-a-test-cpu")


def _page_table(valid_counts, width=8):
    """Page table whose first ``valid_counts[i]`` slots per row are real pages."""
    table = torch.full((len(valid_counts), width), -1, dtype=torch.int32)
    for row, count in enumerate(valid_counts):
        table[row, :count] = torch.arange(count, dtype=torch.int32)
    return table


class TestSm120RowSeqLens(unittest.TestCase):
    def test_exact_row_count_is_passed_through(self):
        # Plain decode: one request per query row, already row-indexed.
        seq_lens = torch.tensor([1, 2, 3, 4], dtype=torch.int32)
        table = _page_table([1, 2, 3, 4])
        out = _sm120_row_seq_lens(seq_lens, table, num_rows=4)
        self.assertIs(out, seq_lens)

    def test_extend_batch_padded_to_capture_size_is_trimmed(self):
        # A four-row extend batch whose per-request tensor was padded to the
        # captured batch size of eight.
        seq_lens = torch.tensor([1, 2, 3, 4, 0, 0, 0, 0], dtype=torch.int32)
        table = _page_table([1, 2, 3, 4])
        out = _sm120_row_seq_lens(seq_lens, table, num_rows=4)
        self.assertEqual(out.tolist(), [1, 2, 3, 4])

    def test_target_verify_expands_to_one_entry_per_draft_row(self):
        # One request, four draft rows: metadata holds a single request-bound
        # entry while the query has four rows.
        seq_lens = torch.tensor([4], dtype=torch.int32)
        table = _page_table([4, 5, 6, 7])
        out = _sm120_row_seq_lens(seq_lens, table, num_rows=4)
        self.assertEqual(out.tolist(), [4, 5, 6, 7])
        self.assertEqual(out.dtype, torch.int32)

    def test_row_without_a_valid_slot_keeps_length_one(self):
        # Zero-length bounds would make the kernel read nothing at all; a length
        # of one lets it consume masked padding instead.
        seq_lens = torch.tensor([1, 2, 3, 4], dtype=torch.int32)
        table = _page_table([1, 0, 3, 4])
        out = _sm120_row_seq_lens(seq_lens, table, num_rows=8)
        self.assertEqual(out.tolist(), [1, 1, 3, 4])

    def test_counts_ignore_interior_holes(self):
        # Only the number of real slots matters; -1 padding is masked by the
        # kernel either way.
        seq_lens = torch.tensor([9], dtype=torch.int32)
        table = torch.tensor([[5, -1, 6, -1], [-1, -1, -1, -1]], dtype=torch.int32)
        out = _sm120_row_seq_lens(seq_lens, table, num_rows=2)
        self.assertEqual(out.tolist(), [2, 1])


if __name__ == "__main__":
    unittest.main()
