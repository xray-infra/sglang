import unittest
from types import SimpleNamespace
from unittest.mock import patch

from sglang.srt.arg_groups.overrides import resolution_result
from sglang.srt.arg_groups.speculative_hook import _handle_eagle_family
from sglang.srt.server_args import ServerArgs
from sglang.test.ci.ci_register import register_cpu_ci
from sglang.test.test_utils import CustomTestCase

register_cpu_ci(est_time=10, suite="base-a-test-cpu")

_MODEL_PATH = "zai-org/GLM-5.3"


class TestGlm5NativeNextnDraftPath(CustomTestCase):
    def test_nextn_defaults_to_the_target_checkpoint_as_draft(self):
        server_args = ServerArgs(model_path=_MODEL_PATH)
        server_args.speculative_algorithm = "NEXTN"
        server_args.speculative_draft_model_path = None
        server_args._model_config = SimpleNamespace(
            hf_config=SimpleNamespace(
                architectures=["Glm5NextForConditionalGeneration"]
            )
        )

        # Exercise the existing EAGLE/NEXTN resolver without entering unrelated
        # model-specific validation or choosing runtime speculative parameters.
        with (
            patch(
                "sglang.srt.arg_groups.speculative_hook._disable_overlap_schedule_for_cpu"
            ),
            patch(
                "sglang.srt.arg_groups.speculative_hook._handle_iquest_q1_mtp_draft"
            ),
            patch(
                "sglang.srt.arg_groups.speculative_hook._auto_choose_speculative_params",
                return_value=(2, 1, 3),
            ),
        ):
            _handle_eagle_family(server_args)

        self.assertEqual(
            resolution_result(server_args, "speculative_draft_model_path"),
            _MODEL_PATH,
        )


if __name__ == "__main__":
    unittest.main()
