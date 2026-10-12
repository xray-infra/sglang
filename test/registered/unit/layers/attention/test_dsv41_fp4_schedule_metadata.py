"""CPU contract tests for the native low-ratio FP4 metadata selection.

Execute the repository method with external page-table/metadata collaborators
substituted. Real DeepGEMM Tensor creation and GPU warmup need integration tests.
"""

import ast
from pathlib import Path
from types import SimpleNamespace
import unittest


SOURCE = (
    Path(__file__).resolve().parents[5]
    / "python/sglang/srt/layers/attention/deepseek_v4_backend.py"
)


def load_method(sm120):
    tree = ast.parse(SOURCE.read_text())
    cls = next(
        n
        for n in tree.body
        if isinstance(n, ast.ClassDef) and n.name == "DeepseekV4AttnBackend"
    )
    method = next(
        n
        for n in cls.body
        if isinstance(n, ast.FunctionDef) and n.name == "init_forward_metadata_indexer"
    )
    for arg in method.args.args + method.args.kwonlyargs:
        arg.annotation = None
    method.returns = None
    calls = []

    def expand(table, **kwargs):
        calls.append((table, kwargs))
        return "expanded-table"

    namespace = {
        "PagedIndexerMetadata": lambda **kwargs: SimpleNamespace(**kwargs),
        "get_platform": lambda: SimpleNamespace(is_sm120=sm120),
        "_expand_index_page_table": expand,
        "_is_xpu": False,
    }
    module = ast.fix_missing_locations(ast.Module(body=[method], type_ignores=[]))
    exec(compile(module, str(SOURCE), "exec"), namespace)
    return namespace["init_forward_metadata_indexer"], calls


class TestDSV41FP4ScheduleMetadata(unittest.TestCase):
    def test_low_ratio_fp4_is_independent_of_c4_fp4_option(self):
        for sm120 in (False, True):
            for c4_fp4 in (False, True):
                for ratio in (1, 2, 4):
                    with self.subTest(sm120=sm120, c4_fp4=c4_fp4, ratio=ratio):
                        method, calls = load_method(sm120)
                        backend = SimpleNamespace(
                            page_size=256,
                            enable_deepseek_v4_fp4_indexer=c4_fp4,
                            token_to_kv_pool=SimpleNamespace(
                                get_index_k_page_size=lambda _: 64
                            ),
                            dsa_topk_backend=SimpleNamespace(
                                should_use_topk_v2=lambda: False
                            ),
                        )
                        core = SimpleNamespace(
                            page_table="original-table",
                            c1_topk_lengths_clamp1="c1-lengths",
                            c2_topk_lengths_clamp1="c2-lengths",
                            c4_topk_lengths_raw="c4-lengths",
                        )
                        metadata = method(backend, core, compress_ratio=ratio)
                        expected_force = sm120 and (c4_fp4 or ratio in (1, 2))
                        self.assertEqual(
                            metadata.force_deep_gemm_metadata, expected_force
                        )
                        self.assertEqual(metadata.compress_ratio, ratio)
                        self.assertEqual(metadata.page_size, 256)
                        self.assertFalse(metadata.use_topk_v2)
                        if ratio in (1, 2):
                            self.assertEqual(metadata.index_page_size, 64)
                            self.assertEqual(metadata.page_table, "expanded-table")
                            self.assertEqual(metadata.c4_seq_lens, f"c{ratio}-lengths")
                            self.assertEqual(calls[0][1]["compress_ratio"], ratio)
                        else:
                            self.assertEqual(metadata.index_page_size, 0)
                            self.assertEqual(metadata.page_table, "original-table")
                            self.assertEqual(metadata.c4_seq_lens, "c4-lengths")
                            self.assertEqual(calls, [])


if __name__ == "__main__":
    unittest.main()
