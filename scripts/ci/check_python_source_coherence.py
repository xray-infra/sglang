"""Compare installed SGLang Python source with an externally approved Git manifest.

Generate from Git objects, never from a dirty worktree or an image's labels.
This is a source gate, not a GPU/binary/dependency or live-service acceptance test.
"""

import argparse
import hashlib
import io
import json
import subprocess
import tarfile
from pathlib import Path, PurePosixPath

PACKAGE_PREFIX = "python/sglang/"


def generate_manifest(repo: Path, revision: str) -> dict:
    commit = subprocess.run(
        ["git", "rev-parse", "--verify", "--end-of-options", f"{revision}^{{commit}}"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    archive = subprocess.run(
        ["git", "archive", "--format=tar", commit, "python/sglang"],
        cwd=repo,
        check=True,
        capture_output=True,
    ).stdout
    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive)) as tree:
        for member in tree:
            if not member.name.startswith(PACKAGE_PREFIX) or not member.name.endswith(
                ".py"
            ):
                continue
            if not member.isfile():
                raise ValueError(f"Non-regular Python source: {member.name}")
            content = tree.extractfile(member)
            if content is None:
                raise ValueError(f"Unreadable Git source: {member.name}")
            name = member.name.removeprefix(PACKAGE_PREFIX)
            files[name] = hashlib.sha256(content.read()).hexdigest()
    if not files:
        raise ValueError("Revision has no SGLang Python source")
    return {"version": 1, "revision": commit, "files": files}


def verify_source(manifest: dict, source_root: Path) -> list[str]:
    files = manifest.get("files")
    if manifest.get("version") != 1 or not isinstance(files, dict) or not files:
        raise ValueError("Unsupported or empty source manifest")
    if not source_root.is_dir():
        raise ValueError("Source root must be the installed sglang package directory")
    errors = []
    root = source_root.resolve()
    for name, expected in files.items():
        path = PurePosixPath(name)
        if (
            path.is_absolute()
            or ".." in path.parts
            or path.as_posix() != name
            or path.suffix != ".py"
            or not isinstance(expected, str)
            or len(expected) != 64
            or any(char not in "0123456789abcdef" for char in expected)
        ):
            raise ValueError(f"Invalid manifest entry: {name}")
        actual = root / name
        if not actual.resolve().is_relative_to(root) or actual.is_symlink():
            errors.append(f"symlink/outside-root: {name}")
        elif not actual.is_file():
            errors.append(f"missing: {name}")
        elif hashlib.sha256(actual.read_bytes()).hexdigest() != expected:
            errors.append(f"modified: {name}")
    # rglob does not descend symlink directories: reject them rather than
    # allowing an untracked Python package to hide outside the checked tree.
    for actual in root.rglob("*"):
        name = actual.relative_to(root).as_posix()
        if actual.is_symlink() and actual.is_dir():
            errors.append(f"symlink-directory: {name}")
        elif actual.suffix == ".py" and name not in files:
            errors.append(f"unexpected: {name}")
    return sorted(errors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    generate = commands.add_parser("generate")
    generate.add_argument("--repo", type=Path, required=True)
    generate.add_argument("--revision", required=True)
    generate.add_argument("--output", type=Path, required=True)
    verify = commands.add_parser("verify")
    verify.add_argument("--manifest", type=Path, required=True)
    verify.add_argument("--source-root", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "generate":
            manifest = generate_manifest(args.repo, args.revision)
            args.output.write_text(
                json.dumps(manifest, sort_keys=True, indent=2) + "\n"
            )
            print(
                f"Manifest: {manifest['revision']}, {len(manifest['files'])} Python files"
            )
            return 0
        manifest = json.loads(args.manifest.read_text())
        errors = verify_source(manifest, args.source_root)
        if errors:
            print("\n".join(errors))
            return 1
        print(f"Source matches approved manifest {manifest['revision']}")
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Source gate failed: {error}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
