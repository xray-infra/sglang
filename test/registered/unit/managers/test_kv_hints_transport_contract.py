"""Real envelope codec and request normalization; no CUDA/cache execution claim."""

from __future__ import annotations

import ast
import copy
import importlib.util
import sys
import types
import typing
import unittest
from array import array
from pathlib import Path

import msgspec

ROOT = Path(__file__).resolve().parents[4]
IO_SOURCE = ROOT / "python/sglang/srt/managers/io_struct.py"


def load_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


registry = load_file("kv_hint_registry", ROOT / "python/sglang/test/ci/ci_register.py")
register_cpu_ci = registry.register_cpu_ci
register_cpu_ci(est_time=1, suite="base-a-test-cpu")
hints = load_file("kv_hint_contract_types", IO_SOURCE.with_name("kv_hints.py"))


def load_generate():
    # Existing AST harness uses real GenerateReqInput and fake unrelated manager
    # collaborators; inject the actual msgspec-backed envelope implementation.
    harness = load_file(
        "kv_hint_normalization_harness",
        Path(__file__).with_name("test_parallel_sample_state_retirement.py"),
    )
    module = harness.load_methods()
    module.KvHintsEnvelope = hints.KvHintsEnvelope
    module.decode_kv_hints_envelope = hints.decode_kv_hints_envelope
    if IO_SOURCE != harness.SOURCE.with_name("io_struct.py"):
        tree = ast.parse(IO_SOURCE.read_text())
        cls = next(
            n
            for n in tree.body
            if isinstance(n, ast.ClassDef) and n.name == "GenerateReqInput"
        )
        exec(
            compile(
                ast.fix_missing_locations(
                    ast.Module(
                        [
                            ast.ImportFrom("__future__", [ast.alias("annotations")], 0),
                            cls,
                        ],
                        [],
                    )
                ),
                str(IO_SOURCE),
                "exec",
            ),
            module.__dict__,
        )  # noqa: S102 -- production AST, never user input
    return module.GenerateReqInput


def envelope(name="one"):
    return {
        "protocol_version": "0.1",
        "message_id": name,
        "actions": [
            {
                "action_id": name,
                "action_type": "kv.retain_prefix",
                "action_version": "1.0",
                "payload": {"duration_seconds": 300, "prefix_token_count": 256},
            }
        ],
    }


class KvHintsTransportContract(unittest.TestCase):
    def test_real_codec_roundtrip_and_opaque_action(self):
        decoded = hints.decode_kv_hints_envelope(envelope())
        self.assertIs(hints.decode_kv_hints_envelope(decoded), decoded)
        self.assertEqual(msgspec.json.decode(msgspec.json.encode(decoded)), envelope())
        self.assertEqual(
            msgspec.msgpack.decode(
                msgspec.msgpack.encode(decoded), type=hints.KvHintsEnvelope
            ),
            decoded,
        )
        # Transport does not invent a supported action/capability set.
        other = envelope()
        other["actions"][0]["action_type"] = "future.example"
        self.assertEqual(
            hints.decode_kv_hints_envelope(other).actions[0].action_type,
            "future.example",
        )

    def test_malformed_envelopes_raise_instead_of_silent_drop(self):
        bad = [
            {},
            [],
            "bad",
            {"protocol_version": 1, "message_id": "one"},
            {**envelope(), "actions": [{"action_id": "one"}]},
        ]
        for value in bad:
            with (
                self.subTest(value=value),
                self.assertRaisesRegex(ValueError, "Malformed kv_hints"),
            ):
                hints.decode_kv_hints_envelope(value)
        Generate = load_generate()
        for value in bad:
            with self.subTest(ingress=value), self.assertRaises(ValueError):
                Generate(text="test", kv_hints=value).normalize_batch_and_arguments()

    def test_retention_intents_require_exact_worker_boundaries(self):
        decoded = hints.decode_kv_hints_envelope(envelope())
        self.assertEqual(
            hints.parse_cache_retention_intents(decoded, prompt_token_count=512),
            (
                hints.CacheRetentionIntent(
                    action_id="one",
                    prefix_token_count=256,
                    duration_seconds=300,
                ),
            ),
        )

        opaque_value = envelope()
        opaque_value["actions"][0]["action_type"] = "future.example"
        opaque = hints.decode_kv_hints_envelope(opaque_value)
        self.assertEqual(
            hints.parse_cache_retention_intents(opaque, prompt_token_count=512), ()
        )

        cases = {
            "protocol_version": (
                {**envelope(), "protocol_version": "9.0"},
                "protocol_version",
            ),
            "action_version": (
                {
                    **envelope(),
                    "actions": [{**envelope()["actions"][0], "action_version": "2.0"}],
                },
                "action_version",
            ),
            "missing_prefix": (
                {
                    **envelope(),
                    "actions": [
                        {
                            **envelope()["actions"][0],
                            "payload": {"duration_seconds": 300},
                        }
                    ],
                },
                "prefix_token_count",
            ),
            "boolean_duration": (
                {
                    **envelope(),
                    "actions": [
                        {
                            **envelope()["actions"][0],
                            "payload": {
                                "duration_seconds": True,
                                "prefix_token_count": 256,
                            },
                        }
                    ],
                },
                "duration_seconds",
            ),
            "duration_limit": (
                {
                    **envelope(),
                    "actions": [
                        {
                            **envelope()["actions"][0],
                            "payload": {
                                "duration_seconds": 86_401,
                                "prefix_token_count": 256,
                            },
                        }
                    ],
                },
                "worker limit",
            ),
            "prompt_limit": (envelope(), "worker prompt length"),
        }
        for name, (value, error) in cases.items():
            prompt_token_count = 128 if name == "prompt_limit" else 512
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, error):
                hints.parse_cache_retention_intents(
                    hints.decode_kv_hints_envelope(value),
                    prompt_token_count=prompt_token_count,
                )

        out_of_order = envelope()
        out_of_order["actions"].append(
            {
                "action_id": "two",
                "action_type": "kv.retain_prefix",
                "action_version": "1.0",
                "payload": {"duration_seconds": 300, "prefix_token_count": 128},
            }
        )
        with self.assertRaisesRegex(ValueError, "strictly increasing"):
            hints.parse_cache_retention_intents(
                hints.decode_kv_hints_envelope(out_of_order), prompt_token_count=512
            )

    def test_single_and_broadcast_batch_parallel_sample_order(self):
        Generate = load_generate()
        for batch in (1, 2, 4):
            for n in (1, 2, 3):
                with self.subTest(batch=batch, n=n):
                    obj = Generate(
                        text="test" if batch == 1 else ["test"] * batch,
                        sampling_params={"n": n},
                        kv_hints=envelope(),
                    )
                    obj.normalize_batch_and_arguments()
                    if obj.is_single:
                        self.assertEqual(obj.kv_hints.message_id, "one")
                    else:
                        self.assertEqual(len(obj.kv_hints), batch * n)
                        for i in range(batch * n):
                            self.assertEqual(obj[i].kv_hints.message_id, "one")
                            self.assertIs(obj[i], obj[i])
                        # Already-expanded metadata is safe to normalize again.
                        obj._normalize_kv_hints()
                        self.assertEqual(len(obj.kv_hints), batch * n)

    def test_per_item_and_none_expand_like_actual_inputs(self):
        Generate = load_generate()
        original = [envelope("first"), None, envelope("third")]
        before = copy.deepcopy(original)
        for n in (1, 2, 3):
            obj = Generate(
                text=["first", "absent", "third"],
                sampling_params={"n": n},
                kv_hints=original,
            )
            obj.normalize_batch_and_arguments()
            names = [
                None if obj[i].kv_hints is None else obj[i].kv_hints.message_id
                for i in range(3 * n)
            ]
            self.assertEqual(names, ["first", None, "third"] * n)
        self.assertEqual(original, before)
        with self.assertRaisesRegex(ValueError, "length of kv_hints"):
            Generate(
                text=["one", "two"], kv_hints=[envelope()]
            ).normalize_batch_and_arguments()

    def test_unhinted_requests_remain_unhinted(self):
        Generate = load_generate()
        for batch in (1, 3):
            obj = Generate(
                text="test" if batch == 1 else ["test"] * batch,
                sampling_params={"n": 2},
            )
            obj.normalize_batch_and_arguments()
            self.assertIsNone(obj.kv_hints)
            for i in range(batch * 2):
                self.assertIsNone(obj[i].kv_hints)

    def test_real_ipc_field_is_append_only_and_optional(self):
        tree = ast.parse(IO_SOURCE.read_text())
        cls = next(
            n
            for n in tree.body
            if isinstance(n, ast.ClassDef) and n.name == "TokenizedGenerateReqInput"
        )
        fields = [n for n in cls.body if isinstance(n, ast.AnnAssign)]
        self.assertEqual(fields[-1].target.id, "kv_hints")
        self.assertIsNone(fields[-1].value.value)

    def test_real_ipc_layout_roundtrip_and_previous_short_message(self):
        tree = ast.parse(IO_SOURCE.read_text())
        classes = [
            next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == name)
            for name in ("BaseReq", "TokenizedGenerateReqInput")
        ]
        module = types.ModuleType("kv_hint_real_ipc_layout")
        sys.modules[module.__name__] = module
        module.__dict__.update(vars(typing))
        module.__dict__["__name__"] = "kv_hint_real_ipc_layout"
        module.__dict__.update(
            msgspec=msgspec, array=array, KvHintsEnvelope=hints.KvHintsEnvelope
        )
        # Unrelated collaborators stay opaque, while the actual production field
        # order, base tag, optional envelope and msgpack decoder are exercised.
        for name in (
            "SamplingParams",
            "MultimodalProcessorOutput",
            "ReturnHiddenStatesMode",
            "SessionParams",
            "PositionalEmbeds",
            "Modality",
            "PickleWrapper",
        ):
            module.__dict__[name] = typing.Any
        exec(
            compile(
                ast.fix_missing_locations(
                    ast.Module(
                        [
                            ast.ImportFrom("__future__", [ast.alias("annotations")], 0),
                            *classes,
                        ],
                        [],
                    )
                ),
                str(IO_SOURCE),
                "exec",
            ),
            module.__dict__,
        )  # noqa: S102 -- production AST only
        Req = module.TokenizedGenerateReqInput
        req = Req(
            input_text="test",
            input_ids=None,
            input_embeds=None,
            mm_inputs=None,
            token_type_ids=None,
            sampling_params={},
            return_logprob=False,
            logprob_start_len=-1,
            top_logprobs_num=0,
            token_ids_logprob=None,
            stream=False,
            rid="wire",
            cache_salt="namespace-A",
            kv_hints=hints.decode_kv_hints_envelope(envelope()),
        )
        wire = msgspec.msgpack.encode(req)
        restored = msgspec.msgpack.decode(wire, type=Req)
        self.assertEqual(restored.kv_hints, req.kv_hints)
        self.assertEqual(restored.cache_salt, "namespace-A")
        fields = msgspec.msgpack.decode(wire)
        # Removing the final appended field reproduces the previous wire layout.
        short = msgspec.msgpack.decode(msgspec.msgpack.encode(fields[:-1]), type=Req)
        self.assertIsNone(short.kv_hints)
        self.assertEqual(short.rid, "wire")
        self.assertEqual(short.cache_salt, "namespace-A")

    def test_actual_forwarding_call_sites(self):
        for relative, owner in (
            ("entrypoints/engine.py", "kv_hints"),
            ("managers/tokenizer_manager.py", "obj.kv_hints"),
            ("managers/scheduler.py", "recv_req.kv_hints"),
            ("session/session_controller.py", "req.kv_hints"),
        ):
            with self.subTest(path=relative):
                tree = ast.parse((ROOT / "python/sglang/srt" / relative).read_text())
                values = [
                    ast.unparse(k.value)
                    for node in ast.walk(tree)
                    if isinstance(node, ast.Call)
                    for k in node.keywords
                    if k.arg == "kv_hints"
                ]
                self.assertIn(owner, values)
        tree = ast.parse(
            (ROOT / "python/sglang/srt/managers/schedule_batch.py").read_text()
        )
        assignments = [
            ast.unparse(node) for node in ast.walk(tree) if isinstance(node, ast.Assign)
        ]
        self.assertIn("self.kv_hints = kv_hints", assignments)


if __name__ == "__main__":
    unittest.main()
