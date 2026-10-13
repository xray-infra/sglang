"""Bounded filesystem retention coordination for the NIXL FILE backend.

This module deliberately coordinates only the built-in FILE cleaner.  It uses a
small, stable set of advisory ``flock`` files; cache objects never get their own
lock inode or open lock descriptor.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import logging
import math
import os
import re
import stat
import tempfile
import time
from collections.abc import Iterable, Iterator
from contextlib import contextmanager, suppress
from dataclasses import dataclass

from sglang.srt.mem_cache.hicache_storage import PoolName
from sglang.srt.mem_cache.storage.nixl.nixl_routing import BUCKET_HEX_CHARS

logger = logging.getLogger(__name__)

MAX_RETAINED_PHYSICAL_OBJECTS = 8192
MAX_RETENTION_DURATION_SECONDS = 86400
_RETENTION_DIR_NAME = ".sglang-nixl-retention"
_STRIPE_COUNT = 64
_RANK_SUFFIX_RE = re.compile(r"_(\d+)_(\d+)$")
_KV_SUFFIXES = ("_k", "_v")
_POOL_NAME_PATTERN = "|".join(
    sorted((re.escape(pool.value) for pool in PoolName), key=len, reverse=True)
)
_HYBRID_COMPONENT_SUFFIX_RE = re.compile(
    rf"_(?:{_POOL_NAME_PATTERN})(?:_(?:temporal|conv_\d+|[kv]|\d+))?$"
)
_BUCKET_NAME_RE = re.compile(rf"^[0-9a-f]{{{BUCKET_HEX_CHARS}}}$")


def parse_group_key(name: str) -> str:
    """Return the logical identity shared by all physical siblings of a page."""
    stem = os.path.basename(name)
    stem = _HYBRID_COMPONENT_SUFFIX_RE.sub("", stem)
    for suffix in _KV_SUFFIXES:
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
            break
    match = _RANK_SUFFIX_RE.search(stem)
    if match is not None:
        stem = stem[: match.start()]
    return stem


@dataclass(frozen=True)
class ReclaimResult:
    reclaimed: bool
    removed_files: int = 0
    removed_bytes: int = 0


class NixlFileRetention:
    """Coordinate transfers, the built-in cleaner, and clear with POSIX flock."""

    def __init__(
        self,
        storage_dirs: Iterable[str],
        *,
        retention_supported: bool = True,
        unsupported_reason: str = "",
        stripe_count: int = _STRIPE_COUNT,
    ) -> None:
        dirs = [
            os.path.realpath(os.path.abspath(path)) for path in storage_dirs if path
        ]
        if not dirs:
            raise ValueError("NIXL FILE retention requires a storage directory")
        if not hasattr(fcntl, "flock"):
            raise RuntimeError("NIXL FILE retention requires POSIX flock semantics")
        self.storage_dirs = list(dict.fromkeys(dirs))
        self.retention_supported = retention_supported
        self.unsupported_reason = unsupported_reason
        self.stripe_count = stripe_count

        # One coordinator root is sufficient because every process using these
        # storage dirs resolves the same canonical first root.
        self.metadata_dir = os.path.join(self.storage_dirs[0], _RETENTION_DIR_NAME)
        self.deadline_dir = os.path.join(self.metadata_dir, "deadlines")
        self._mkdir_without_symlink(self.metadata_dir)
        self._mkdir_without_symlink(self.deadline_dir)
        self.global_lock_path = os.path.join(self.metadata_dir, "global.lock")
        self.stripe_paths = [
            os.path.join(self.metadata_dir, f"stripe-{index:02d}.lock")
            for index in range(stripe_count)
        ]
        # Publication locks serialize read-max-replace while transfers retain
        # shared ownership of the corresponding cleaner stripe.
        self.publish_lock_paths = [
            os.path.join(self.metadata_dir, f"publish-{index:02d}.lock")
            for index in range(stripe_count)
        ]
        for path in [
            self.global_lock_path,
            *self.stripe_paths,
            *self.publish_lock_paths,
        ]:
            fd = os.open(
                path, os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0), 0o600
            )
            os.close(fd)

    @staticmethod
    def _mkdir_without_symlink(path: str) -> None:
        try:
            os.mkdir(path, mode=0o700)
        except FileExistsError:
            # Every TP/rank process may initialize the same fresh cache root at
            # once. The winner creates the directory; all losers must validate
            # that the existing inode is a real directory, not follow a link.
            pass
        path_stat = os.stat(path, follow_symlinks=False)
        if not stat.S_ISDIR(path_stat.st_mode):
            raise ValueError(
                f"NIXL retention metadata path must be a real directory: {path}"
            )

    @staticmethod
    def _open_lock(path: str) -> int:
        return os.open(path, os.O_RDWR | getattr(os, "O_NOFOLLOW", 0))

    @staticmethod
    def _lock(fd: int, exclusive: bool) -> None:
        fcntl.flock(fd, fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)

    @staticmethod
    def _unlock_close(fd: int) -> None:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)

    def _stripe_index(self, group_key: str) -> int:
        digest = hashlib.blake2b(group_key.encode("utf-8"), digest_size=8).digest()
        return int.from_bytes(digest, "big") % self.stripe_count

    def _deadline_path(self, group_key: str) -> str:
        digest = hashlib.sha256(group_key.encode("utf-8")).hexdigest()
        return os.path.join(self.deadline_dir, f"{digest}.deadline")

    def validate_retained_write(
        self, physical_paths: Iterable[str], duration_seconds: object
    ) -> int:
        """Validate a complete retained write before it can mutate storage."""
        if not self.retention_supported:
            detail = f": {self.unsupported_reason}" if self.unsupported_reason else ""
            raise RuntimeError(
                "NIXL FILE retention is unsupported without the built-in cleaner "
                f"and POSIX flock semantics{detail}"
            )
        if (
            isinstance(duration_seconds, bool)
            or not isinstance(duration_seconds, int)
            or duration_seconds <= 0
            or duration_seconds > MAX_RETENTION_DURATION_SECONDS
        ):
            raise ValueError(
                "retention_duration_seconds must be greater than 0 and at most "
                f"{MAX_RETENTION_DURATION_SECONDS}"
            )
        unique_paths = {
            os.path.realpath(os.path.abspath(path)) for path in physical_paths
        }
        if len(unique_paths) > MAX_RETAINED_PHYSICAL_OBJECTS:
            raise ValueError(
                "retained NIXL FILE write exceeds the limit of "
                f"{MAX_RETAINED_PHYSICAL_OBJECTS} unique physical objects"
            )
        return duration_seconds

    @contextmanager
    def transfer_guard(self, physical_paths: Iterable[str]) -> Iterator[None]:
        """Hold global and group shared ownership through a synchronous transfer."""
        groups = {parse_group_key(path) for path in physical_paths}
        stripes = sorted({self._stripe_index(group) for group in groups})
        global_fd = self._open_lock(self.global_lock_path)
        stripe_fds: list[int] = []
        try:
            self._lock(global_fd, exclusive=False)
            for index in stripes:
                fd = self._open_lock(self.stripe_paths[index])
                self._lock(fd, exclusive=False)
                stripe_fds.append(fd)
            yield
        finally:
            for fd in reversed(stripe_fds):
                self._unlock_close(fd)
            self._unlock_close(global_fd)

    @contextmanager
    def clear_guard(self) -> Iterator[None]:
        """Serialize clear against all transfers without replacing lock inodes."""
        fd = self._open_lock(self.global_lock_path)
        try:
            self._lock(fd, exclusive=True)
            yield
        finally:
            self._unlock_close(fd)

    def publish_deadlines(
        self,
        physical_paths: Iterable[str],
        duration_seconds: float,
        *,
        now: float | None = None,
    ) -> None:
        """Atomically publish max(existing, new) while transfer locks are held."""
        deadline = (time.time() if now is None else now) + duration_seconds
        groups = sorted({parse_group_key(path) for path in physical_paths})
        publish_fds: list[int] = []
        try:
            for index in sorted({self._stripe_index(group) for group in groups}):
                fd = self._open_lock(self.publish_lock_paths[index])
                self._lock(fd, exclusive=True)
                publish_fds.append(fd)
            for group_key in groups:
                old_deadline = self._read_deadline(group_key)
                self._write_deadline(group_key, max(deadline, old_deadline or 0.0))
        finally:
            for fd in reversed(publish_fds):
                self._unlock_close(fd)

    def _read_deadline(self, group_key: str) -> float | None:
        path = self._deadline_path(group_key)
        try:
            fd = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
            with os.fdopen(fd, encoding="utf-8") as deadline_file:
                payload = json.load(deadline_file)
            if payload.get("group") != group_key:
                raise ValueError("retention sidecar identity mismatch")
            deadline = float(payload["deadline"])
            if not math.isfinite(deadline):
                raise ValueError("non-finite retention deadline")
            return deadline
        except FileNotFoundError:
            return None
        except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError):
            # Corrupt metadata must fail closed rather than violating retention.
            logger.warning("Invalid NIXL retention sidecar %s", path, exc_info=True)
            return math.inf

    def _write_deadline(self, group_key: str, deadline: float) -> None:
        path = self._deadline_path(group_key)
        fd, temporary = tempfile.mkstemp(prefix=".deadline-", dir=self.deadline_dir)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as deadline_file:
                json.dump({"group": group_key, "deadline": deadline}, deadline_file)
                deadline_file.write("\n")
                deadline_file.flush()
                os.fsync(deadline_file.fileno())
            os.replace(temporary, path)
        finally:
            with suppress(FileNotFoundError):
                os.unlink(temporary)

    def deadline_for_group(self, group_key: str) -> float | None:
        """Test/diagnostic accessor. Cleaner paths use it only under a stripe lock."""
        return self._read_deadline(group_key)

    def _scan_group(self, group_key: str) -> list[str]:
        paths: list[str] = []
        for base_dir in self.storage_dirs:
            try:
                buckets = list(os.scandir(base_dir))
            except OSError:
                continue
            for bucket in buckets:
                try:
                    if _BUCKET_NAME_RE.fullmatch(
                        bucket.name
                    ) is None or not bucket.is_dir(follow_symlinks=False):
                        continue
                    entries = list(os.scandir(bucket.path))
                except OSError:
                    continue
                for entry in entries:
                    try:
                        if (
                            entry.is_file(follow_symlinks=False)
                            and parse_group_key(entry.name) == group_key
                        ):
                            paths.append(entry.path)
                    except OSError:
                        continue
        return paths

    def reclaim_group(
        self, group_key: str, *, now: float | None = None
    ) -> ReclaimResult:
        """Exclusively rescan and reclaim one group if its deadline has expired."""
        global_fd = self._open_lock(self.global_lock_path)
        stripe_fd: int | None = None
        try:
            self._lock(global_fd, exclusive=False)
            stripe_fd = self._open_lock(
                self.stripe_paths[self._stripe_index(group_key)]
            )
            self._lock(stripe_fd, exclusive=True)
            deadline = self._read_deadline(group_key)
            if deadline is not None and deadline > (
                time.time() if now is None else now
            ):
                return ReclaimResult(False)

            removed_files = 0
            removed_bytes = 0
            all_removed = True
            for path in self._scan_group(group_key):
                try:
                    size = os.stat(path, follow_symlinks=False).st_size
                    os.unlink(path)
                    removed_files += 1
                    removed_bytes += size
                except FileNotFoundError:
                    continue
                except OSError:
                    all_removed = False
                    logger.debug(
                        "Failed to unlink NIXL L3 file %s", path, exc_info=True
                    )
            if all_removed:
                try:
                    os.unlink(self._deadline_path(group_key))
                except FileNotFoundError:
                    pass
                except OSError:
                    all_removed = False
                    logger.warning(
                        "Failed to remove NIXL retention sidecar for %s",
                        group_key,
                        exc_info=True,
                    )
            return ReclaimResult(all_removed, removed_files, removed_bytes)
        finally:
            if stripe_fd is not None:
                self._unlock_close(stripe_fd)
            self._unlock_close(global_fd)

    def clear_deadlines(self) -> None:
        """Remove sidecars while the caller holds the global exclusive lock."""
        try:
            entries = list(os.scandir(self.deadline_dir))
        except OSError:
            return
        for entry in entries:
            try:
                if entry.is_file(follow_symlinks=False):
                    os.unlink(entry.path)
            except OSError:
                logger.warning(
                    "Failed to remove NIXL retention sidecar %s",
                    entry.path,
                    exc_info=True,
                )
