import hashlib
import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

from sglang.test.ci.ci_register import register_cpu_ci

register_cpu_ci(est_time=2, suite="base-a-test-cpu")

SCRIPT = (
    Path(__file__).resolve().parents[4] / "scripts/ci/check_python_source_coherence.py"
)
spec = importlib.util.spec_from_file_location("source_gate", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("Source gate module is missing")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class TestPythonSourceCoherence(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.repo = Path(self.directory.name)
        self.root = self.repo / "python/sglang"
        (self.root / "function_call").mkdir(parents=True)
        self.content = {
            "serving_chat.py": b"parser(tools=tools)\n",
            "function_call/parser.py": b"def parser(tools): return tools\n",
        }
        for name, value in self.content.items():
            (self.root / name).write_bytes(value)
        self.manifest = {
            "version": 1,
            "revision": "reviewed-fixture",
            "files": {
                name: hashlib.sha256(value).hexdigest()
                for name, value in self.content.items()
            },
        }

    def test_clean_and_every_modified_module(self):
        self.assertEqual(gate.verify_source(self.manifest, self.root), [])
        for name, content in self.content.items():
            with self.subTest(name=name):
                (self.root / name).write_bytes(content + b"# overlaid source\n")
                self.assertEqual(
                    gate.verify_source(self.manifest, self.root), [f"modified: {name}"]
                )
                (self.root / name).write_bytes(content)

    def test_missing_and_unexpected_modules_fail_closed(self):
        (self.root / "serving_chat.py").unlink()
        (self.root / "overlay.py").write_text("# unreviewed module\n")
        self.assertEqual(
            gate.verify_source(self.manifest, self.root),
            ["missing: serving_chat.py", "unexpected: overlay.py"],
        )

    def test_empty_and_outside_root_manifests_are_rejected(self):
        for files in ({}, {"../outside.py": "0" * 64}, {"/outside.py": "0" * 64}):
            with self.subTest(files=files), self.assertRaises(ValueError):
                gate.verify_source({"version": 1, "files": files}, self.root)

    def test_symlink_cannot_hide_a_source_overlay(self):
        outside = self.repo / "outside.py"
        outside.write_bytes(self.content["serving_chat.py"])
        (self.root / "serving_chat.py").unlink()
        (self.root / "serving_chat.py").symlink_to(outside)
        self.assertEqual(
            gate.verify_source(self.manifest, self.root),
            ["symlink/outside-root: serving_chat.py"],
        )

    def test_untracked_symlink_directory_cannot_hide_extra_modules(self):
        outside = self.repo / "external-package"
        outside.mkdir()
        (outside / "__init__.py").write_text("# unreviewed package\n")
        (self.root / "extra").symlink_to(outside, target_is_directory=True)
        self.assertEqual(
            gate.verify_source(self.manifest, self.root), ["symlink-directory: extra"]
        )

    def git(self, *args):
        return subprocess.run(
            ["git", *args], cwd=self.repo, check=True, capture_output=True, text=True
        ).stdout.strip()

    def test_generation_uses_committed_objects_not_dirty_source(self):
        self.git("init", "-q")
        self.git("add", "python")
        self.git(
            "-c",
            "user.name=Source Gate Test",
            "-c",
            "user.email=gate@example.invalid",
            "commit",
            "-qm",
            "fixture",
        )
        revision = self.git("rev-parse", "HEAD")
        (self.root / "serving_chat.py").write_text("parser(tool_choice='required')\n")
        manifest = gate.generate_manifest(self.repo, revision)
        self.assertEqual(manifest["revision"], revision)
        self.assertEqual(manifest["files"], self.manifest["files"])
        self.assertEqual(
            gate.verify_source(manifest, self.root), ["modified: serving_chat.py"]
        )


if __name__ == "__main__":
    unittest.main()
