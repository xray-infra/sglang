"""Hardware-gated skeleton for non-Flash GLM-5.3 built-in NEXTN PD+DCP4.

This is an integration launch contract, not CPU-contract coverage or proof of
correctness. It intentionally mirrors the GLM-5.2 DSA PD/MTP layer-split
fixture: prefill owns source KV pages and decode owns DCP rank-local target
pages plus replicated NEXTN state.
"""

import unittest

import torch

from sglang.test.ci.ci_register import register_cuda_ci
from sglang.test.kits.eval_accuracy_kit import GSM8KMixin
from sglang.test.server_fixtures.disaggregation_fixture import (
    PDDisaggregationServerBase,
)

register_cuda_ci(est_time=900, stage="extra-b", runner_config="8-gpu-b300")


@unittest.skipUnless(
    torch.cuda.is_available() and torch.cuda.device_count() >= 8,
    "hardware-gated: GLM-5.3 PD+DCP4 NEXTN requires eight GPUs; not proof",
)
class TestGLM53DSAPDNextNDCP4(PDDisaggregationServerBase, GSM8KMixin):
    """Combined DSA, PD, DCP4, and built-in NEXTN smoke/accuracy skeleton."""

    model = "zai-org/GLM-5.3"
    gsm8k_accuracy_thres = 0.80
    gsm8k_num_questions = 32
    gsm8k_num_threads = 8
    gsm8k_num_shots = 5

    extra_prefill_args = [
        "--tp",
        "4",
        "--dsa-prefill-backend",
        "trtllm",
        "--kv-cache-dtype",
        "fp8_e4m3",
        "--mem-fraction-static",
        "0.85",
        "--speculative-algorithm",
        "NEXTN",
        "--speculative-num-steps",
        "5",
        "--speculative-eagle-topk",
        "1",
        "--speculative-num-draft-tokens",
        "6",
    ]
    extra_decode_args = [
        "--tp",
        "4",
        "--dcp-size",
        "4",
        "--dcp-comm-backend",
        "a2a",
        "--dcp-replicate-q-proj",
        "--dsa-decode-backend",
        "trtllm",
        "--kv-cache-dtype",
        "fp8_e4m3",
        "--mem-fraction-static",
        "0.85",
        "--speculative-algorithm",
        "NEXTN",
        "--speculative-num-steps",
        "5",
        "--speculative-eagle-topk",
        "1",
        "--speculative-num-draft-tokens",
        "6",
        "--base-gpu-id",
        "4",
    ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.launch_all()


if __name__ == "__main__":
    unittest.main()
