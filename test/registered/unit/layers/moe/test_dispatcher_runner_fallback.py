"""Expert-id mapping follows the runner a quant method actually built.

On sm120 --moe-runner-backend is pinned to flashinfer_cutlass for the NVFP4
experts, which handles EP with global expert ids, so the standard dispatcher
skips the global->local mapping. Fp8MoEMethod has no flashinfer_cutlass path
and runs triton instead (e.g. an FP8-cast NextN draft layer). Triton indexes
its local experts, so under EP a global id past num_local_experts read out of
bounds (illegal memory access in the first fused-MoE GEMM).
"""

from types import SimpleNamespace
from unittest.mock import patch

import pytest
import torch

from sglang.srt.layers.moe.moe_runner.base import MoeRunnerConfig
from sglang.srt.layers.moe.token_dispatcher import standard
from sglang.srt.layers.moe.topk import StandardTopKOutput
from sglang.srt.layers.moe.utils import MoeA2ABackend, MoeRunnerBackend
from sglang.srt.runtime_context import get_flags
from sglang.test.ci.ci_register import register_cpu_ci

register_cpu_ci(est_time=4, suite="stage-b-test-cpu-intel")

NUM_EXPERTS, EP_SIZE, EP_RANK = 256, 8, 3
NUM_LOCAL = NUM_EXPERTS // EP_SIZE


@pytest.fixture
def _moe_flags():
    moe = get_flags().moe
    saved = (moe.runner_backend, moe.a2a_backend)
    moe.runner_backend = MoeRunnerBackend.FLASHINFER_CUTLASS
    moe.a2a_backend = MoeA2ABackend.NONE
    yield moe
    moe.runner_backend, moe.a2a_backend = saved


@pytest.fixture
def _ep():
    parallel = SimpleNamespace(moe_ep_size=EP_SIZE, moe_ep_rank=EP_RANK)
    with (
        patch.object(standard, "get_parallel", return_value=parallel),
        patch.object(standard, "get_device", return_value="cpu"),
        patch.object(
            standard,
            "should_use_flashinfer_cutlass_moe_fp4_allgather",
            return_value=False,
        ),
    ):
        yield


def _config():
    return MoeRunnerConfig(
        num_experts=NUM_EXPERTS,
        num_local_experts=NUM_LOCAL,
        num_fused_shared_experts=0,
    )


def _topk():
    ids = torch.tensor(
        [[0, EP_RANK * NUM_LOCAL, EP_RANK * NUM_LOCAL + 5, NUM_EXPERTS - 1]],
        dtype=torch.int32,
    )
    return StandardTopKOutput(
        topk_weights=torch.full(ids.shape, 0.25),
        topk_ids=ids,
        router_logits=torch.zeros(1, NUM_EXPERTS),
    )


def test_fp8_method_declares_its_triton_fallback(_moe_flags):
    from sglang.srt.layers.quantization.fp8 import Fp8MoEMethod

    method = object.__new__(Fp8MoEMethod)
    method.is_fp4_expert = False
    method.create_moe_runner(SimpleNamespace(), _config())
    assert method.runner.runner_backend.is_triton()
    assert method.dispatch_runner_backend == MoeRunnerBackend.TRITON


def test_pinned_backend_alone_keeps_global_ids(_moe_flags, _ep):
    dispatcher = standard.StandardDispatcher(_config())
    assert dispatcher.skip_local_expert_mapping
    out = dispatcher.dispatch(torch.zeros(1, 8), _topk())
    assert out.topk_output.topk_ids.tolist() == _topk().topk_ids.tolist()


def test_triton_fallback_maps_ids_to_local(_moe_flags, _ep):
    from sglang.srt.layers.moe.fused_moe_triton.layer import create_moe_dispatcher

    method = SimpleNamespace(dispatch_runner_backend=MoeRunnerBackend.TRITON)
    with patch(
        "sglang.srt.layers.moe.fused_moe_triton.layer.is_npu", return_value=False
    ):
        dispatcher = create_moe_dispatcher(_config(), quant_method=method)
    assert isinstance(dispatcher, standard.StandardDispatcher)
    assert not dispatcher.skip_local_expert_mapping
    out = dispatcher.dispatch(torch.zeros(1, 8), _topk())
    # Only this rank's 32 experts survive, renumbered from 0; the rest drop.
    assert out.topk_output.topk_ids.tolist() == [[-1, 0, 5, -1]]


def test_quant_method_without_override_follows_the_flag(_moe_flags, _ep):
    from sglang.srt.layers.moe.fused_moe_triton.layer import create_moe_dispatcher

    with patch(
        "sglang.srt.layers.moe.fused_moe_triton.layer.is_npu", return_value=False
    ):
        dispatcher = create_moe_dispatcher(_config(), quant_method=SimpleNamespace())
    assert dispatcher.skip_local_expert_mapping
