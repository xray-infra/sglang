"""SGLANG_NVFP4_CKPT_FP8_NEXTN_MOE on non-DeepGEMM MoE runners -- CPU-only.

An NVFP4 checkpoint keeps its NextN layer in bf16. With the flag on, the triton
runner (and flashinfer_cutlass / flashinfer_cutedsl, which Fp8MoEMethod runs on
triton) casts that layer's expert and shared-expert projections to 128x128
block FP8 while the weights stream past, so nothing else in the checkpoint is
materialized. DeepGEMM keeps the UE8M0 path.
"""

import contextlib
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import torch

from sglang.srt.environ import envs
from sglang.srt.layers.moe.utils import MoeRunnerBackend
from sglang.srt.layers.quantization.fp8_utils import block_quant_dequant
from sglang.srt.models.deepseek_common.deepseek_weight_loader import (
    DeepseekV2WeightLoaderMixin,
    NextNDisabledConfig,
    NextNEnabledConfig,
)
from sglang.srt.models.deepseek_common.utils import enable_nextn_moe_bf16_cast_to_fp8
from sglang.test.ci.ci_register import register_cpu_ci
from sglang.test.test_utils import CustomTestCase

register_cpu_ci(est_time=5, suite="base-a-test-cpu")

LAYER = 78
_UTILS_BACKEND = "sglang.srt.models.deepseek_common.utils.get_moe_runner_backend"
_LOADER_BACKEND = (
    "sglang.srt.models.deepseek_common.deepseek_weight_loader.get_moe_runner_backend"
)
_FP4 = SimpleNamespace(get_name=lambda: "modelopt_fp4")
_NEXTN = NextNEnabledConfig(
    num_nextn_layers=1,
    nextn_layer_id=LAYER,
    nextn_layer_prefix=f"model.layers.{LAYER}",
    nextn_spec_weight_names=["shared_head.norm", "eh_proj", "enorm", "hnorm"],
)


@contextlib.contextmanager
def _backend(backend):
    with (
        patch(_UTILS_BACKEND, return_value=backend),
        patch(_LOADER_BACKEND, return_value=backend),
    ):
        yield


def _flag(on):
    return patch.object(envs.SGLANG_NVFP4_CKPT_FP8_NEXTN_MOE, "get", return_value=on)


def _loader(n_routed_experts=2):
    loader = DeepseekV2WeightLoaderMixin.__new__(DeepseekV2WeightLoaderMixin)
    loader.quant_config = _FP4
    loader.config = SimpleNamespace(n_routed_experts=n_routed_experts)
    return loader


def _weights():
    torch.manual_seed(0)
    p = f"model.layers.{LAYER}"
    # 300 x 200 is deliberately not a multiple of the 128 block.
    return [
        (f"{p}.mlp.experts.0.gate_proj.weight", torch.randn(300, 200).bfloat16()),
        (f"{p}.mlp.experts.0.up_proj.weight", torch.randn(300, 200).bfloat16()),
        (f"{p}.mlp.experts.0.down_proj.weight", torch.randn(200, 300).bfloat16()),
        (f"{p}.mlp.experts.1.gate_proj.weight", torch.randn(300, 200).bfloat16()),
        (f"{p}.mlp.experts.1.up_proj.weight", torch.randn(300, 200).bfloat16()),
        (f"{p}.mlp.experts.1.down_proj.weight", torch.randn(200, 300).bfloat16()),
        (f"{p}.mlp.shared_experts.gate_proj.weight", torch.randn(256, 128).bfloat16()),
        (f"{p}.mlp.shared_experts.up_proj.weight", torch.randn(256, 128).bfloat16()),
        (f"{p}.mlp.shared_experts.down_proj.weight", torch.randn(128, 256).bfloat16()),
        (f"{p}.mlp.gate.weight", torch.randn(2, 128).bfloat16()),
        (f"{p}.mlp.gate.e_score_correction_bias", torch.randn(2)),
        (f"{p}.self_attn.o_proj.weight", torch.randn(128, 128).bfloat16()),
        (f"{p}.eh_proj.weight", torch.randn(128, 256).bfloat16()),
        ("model.layers.77.mlp.experts.0.gate_proj.weight", torch.randn(8, 8)),
    ]


def _is_cast(name):
    return name.startswith(f"model.layers.{LAYER}.mlp.") and (
        ".experts." in name or ".shared_experts." in name
    )


class TestGate(CustomTestCase):
    def test_off_by_default(self):
        with _backend(MoeRunnerBackend.TRITON):
            self.assertFalse(enable_nextn_moe_bf16_cast_to_fp8(_FP4))

    def test_runner_backends(self):
        with _flag(True):
            for backend, expected in [
                (MoeRunnerBackend.DEEP_GEMM, True),
                (MoeRunnerBackend.TRITON, True),
                (MoeRunnerBackend.FLASHINFER_CUTLASS, True),
                (MoeRunnerBackend.FLASHINFER_CUTEDSL, True),
                (MoeRunnerBackend.FLASHINFER_TRTLLM, False),
                (MoeRunnerBackend.AUTO, False),
            ]:
                with self.subTest(backend=backend), _backend(backend):
                    self.assertEqual(enable_nextn_moe_bf16_cast_to_fp8(_FP4), expected)

    def test_requires_modelopt_fp4(self):
        with _flag(True), _backend(MoeRunnerBackend.TRITON):
            self.assertFalse(enable_nextn_moe_bf16_cast_to_fp8(None))
            self.assertFalse(
                enable_nextn_moe_bf16_cast_to_fp8(
                    SimpleNamespace(get_name=lambda: "fp8")
                )
            )


class TestStreamingCast(CustomTestCase):
    def test_flag_off_returns_input_untouched(self):
        weights = iter(_weights())
        with _flag(False), _backend(MoeRunnerBackend.TRITON):
            out = _loader()._maybe_quant_weights_to_fp8_ue8m0(weights, [], _NEXTN)
        self.assertIs(out, weights)

    def test_target_model_untouched(self):
        weights = iter(_weights())
        with _flag(True), _backend(MoeRunnerBackend.TRITON):
            out = _loader()._maybe_quant_weights_to_fp8_ue8m0(
                weights, [], NextNDisabledConfig()
            )
        self.assertIs(out, weights)

    def test_triton_casts_nextn_mlp_lazily(self):
        src = _weights()
        consumed = []

        def gen():
            for item in src:
                consumed.append(item[0])
                yield item

        with _flag(True), _backend(MoeRunnerBackend.FLASHINFER_CUTLASS):
            out = _loader()._maybe_quant_weights_to_fp8_ue8m0(gen(), [], _NEXTN)
            # Streaming: nothing is read before the loader pulls.
            self.assertEqual(consumed, [])
            got = list(out)

        names = [n for n, _ in got]
        by_name = dict(got)
        for name, orig in src:
            if not _is_cast(name):
                self.assertIs(by_name[name], orig, name)
                continue
            w = by_name[name]
            s = by_name[name[: -len("weight")] + "weight_scale_inv"]
            self.assertEqual(w.dtype, torch.float8_e4m3fn, name)
            self.assertEqual(s.dtype, torch.float32, name)
            n, k = orig.shape
            self.assertEqual(tuple(w.shape), (n, k))
            self.assertEqual(tuple(s.shape), (-(-n // 128), -(-k // 128)))
            deq = block_quant_dequant(w, s, [128, 128], torch.float32)
            ref = orig.float()
            # e4m3 keeps 3 mantissa bits: <= 1/16 of the block amax per element,
            # plus the up-to-2x headroom of a power-of-two scale.
            self.assertLessEqual(
                (deq - ref).abs().max().item(), ref.abs().max().item() / 8, name
            )
            self.assertLess((deq - ref).abs().mean().item(), 0.05, name)
        # One scale per cast weight, emitted right after it.
        n_cast = sum(_is_cast(n) for n, _ in src)
        self.assertEqual(len(names), len(src) + n_cast)
        for i, name in enumerate(names):
            if name.endswith("weight_scale_inv"):
                self.assertEqual(
                    names[i - 1], name.replace("weight_scale_inv", "weight")
                )

    def test_deep_gemm_keeps_ue8m0_path(self):
        loader = _loader()
        with (
            _flag(True),
            _backend(MoeRunnerBackend.DEEP_GEMM),
            patch.object(
                DeepseekV2WeightLoaderMixin, "_mark_nextn_moe_weights_as_ue8m0"
            ) as mark,
        ):
            out = loader._maybe_quant_weights_to_fp8_ue8m0(iter(_weights()), [], _NEXTN)
        self.assertIsInstance(out, list)
        mark.assert_called_once()
        by_name = dict(out)
        self.assertEqual(
            by_name[f"model.layers.{LAYER}.mlp.experts.1.down_proj.weight"].dtype,
            torch.float8_e4m3fn,
        )


if __name__ == "__main__":
    unittest.main()
