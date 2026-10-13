"""Unit tests for the NIXL FILE L3 cleaner."""
# ruff: noqa: E402

from sglang.test.ci.ci_register import register_cpu_ci

register_cpu_ci(est_time=5, suite="base-a-test-cpu")

import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from types import SimpleNamespace

from sglang.srt.mem_cache.hicache_storage import PoolName, PoolTransfer
from sglang.srt.mem_cache.storage.nixl.hicache_nixl import HiCacheNixl
from sglang.srt.mem_cache.storage.nixl.nixl_cleaner import (
    HiCacheL3Cleaner,
    _parse_group_key,
    _safe_unlink,
)
from sglang.srt.mem_cache.storage.nixl.nixl_retention import (
    MAX_RETAINED_PHYSICAL_OBJECTS,
    NixlFileRetention,
)
from sglang.srt.mem_cache.storage.nixl.nixl_utils import (
    NixlBackendConfig,
    NixlFileManager,
)
from sglang.test.test_utils import CustomTestCase


class TestNixlFileQuery(CustomTestCase):
    def _cache_with_results(self, results):
        cache = object.__new__(HiCacheNixl)
        cache.backend_selector = SimpleNamespace(backend_name="POSIX", mem_type="FILE")
        cache.file_manager = SimpleNamespace(get_file_path=lambda key: f"/cache/{key}")
        cache.agent = SimpleNamespace(query_memory=lambda *_args, **_kwargs: results)
        return cache

    def test_file_query_rejects_incomplete_cache_objects(self):
        cache = self._cache_with_results(
            [
                {"size": "0"},
                {"size": "149760"},
                None,
                {"size": "224640"},
            ]
        )

        self.assertEqual(
            cache._query_keys_exist(
                ["empty", "complete", "missing", "short"],
                [149760, 149760, 224640, 149760],
            ),
            [False, True, False, False],
        )

    def test_file_query_without_expected_sizes_preserves_existence_semantics(self):
        cache = self._cache_with_results([{"size": "0"}, None])

        self.assertEqual(cache._query_keys_exist(["present", "missing"]), [True, False])

    def test_file_query_requires_one_expected_size_per_key(self):
        cache = self._cache_with_results([])

        with self.assertRaisesRegex(ValueError, "counts must match"):
            cache._query_keys_exist(["one", "two"], [1])

    def test_hybrid_exists_requires_complete_component_sizes(self):
        cache = object.__new__(HiCacheNixl)
        pool_name = PoolName.DEEPSEEK_V4_C1
        host_pool = SimpleNamespace(page_size=1)
        cache.registered_pools = {pool_name: host_pool}
        cache._hybrid_pool_ctx = {
            pool_name: SimpleNamespace(host_pool=host_pool, is_zero_copy=True)
        }
        cache.batch_exists = lambda _keys, _extra_info=None: 2
        cache._prepare_pool_transfer = lambda _transfer, for_write: (
            host_pool,
            ["page-0-c1", "page-1-c1"],
            [(1000, 149760), (2000, 149760)],
            [0, 1],
            1,
        )
        observed = {}

        def query(component_keys, expected_sizes):
            observed["keys"] = component_keys
            observed["sizes"] = expected_sizes
            return [True, False]

        cache._query_keys_exist = query
        result = cache.batch_exists_v2(
            ["page-0", "page-1"],
            [
                PoolTransfer(
                    name=pool_name,
                    host_indices=[0, 1],
                    keys=["page-0", "page-1"],
                )
            ],
        )

        self.assertEqual(result.kv_hit_pages, 1)
        self.assertEqual(result.extra_pool_hit_pages[pool_name], 1)
        self.assertEqual(observed["keys"], ["page-0-c1", "page-1-c1"])
        self.assertEqual(observed["sizes"], [149760, 149760])


class TestHiCacheL3Cleaner(CustomTestCase):
    """Tests for watermark-driven cleanup over bucketed NIXL FILE layout."""

    def setUp(self):
        self.test_dir = tempfile.mkdtemp(prefix="test_nixl_l3_cleaner_")
        self.base_dirs = [os.path.join(self.test_dir, f"disk{i}") for i in range(2)]
        self.file_manager = NixlFileManager(self.base_dirs, use_direct_io=False)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def _write_key(self, key: str, *, mtime: float, size: int = 16) -> str:
        path = self.file_manager.get_file_path(key)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(b"x" * size)
        os.utime(path, (mtime, mtime))
        return path

    def _run_single_group_cleanup(self) -> None:
        cleaner = HiCacheL3Cleaner(
            self.base_dirs,
            tp_rank=0,
            high_watermark=80.0,
            low_watermark=70.0,
            recheck_groups=1,
            unlink_workers=1,
        )
        usage_calls: dict[str, int] = {}

        def fake_usage(path: str) -> float:
            usage_calls[path] = usage_calls.get(path, 0) + 1
            return 90.0 if usage_calls[path] == 1 else 60.0

        cleaner._disk_usage_pct = fake_usage
        self.assertTrue(cleaner._tick())

    def test_parse_group_key_strips_rank_and_kv_suffix(self):
        """Keys for TP ranks and zero-copy K/V files share one cleanup group."""
        self.assertEqual(_parse_group_key("page-a_model_0_8"), "page-a_model")
        self.assertEqual(_parse_group_key("page-a_model_7_8_k"), "page-a_model")
        self.assertEqual(_parse_group_key("page-a_model_7_8_v"), "page-a_model")
        self.assertEqual(_parse_group_key("page-a_model_k"), "page-a_model")

    def test_parse_group_key_strips_hybrid_component_suffix(self):
        """All hybrid component shapes share the logical page's cleanup group."""
        names = [
            "page-a_model_7_8_kv_k",
            "page-a_model_7_8_swa_k",
            "page-a_model_7_8_swa_v",
            "page-a_model_7_8_mamba_temporal",
            "page-a_model_7_8_mamba_conv_0",
            "page-a_model_7_8_indexer_2",
            "page-a_model_7_8_draft_swa",
            "page-a_model_deepseek_v4_c4_indexer_state_2",
        ]

        for name in names:
            with self.subTest(name=name):
                self.assertEqual(_parse_group_key(name), "page-a_model")

    def test_tick_deletes_oldest_group_across_bucketed_dirs(self):
        """A cleaner batch deletes all files in the oldest logical key group."""
        old_keys = ["page-old_model_0_2", "page-old_model_1_2"]
        new_keys = ["page-new_model_0_2", "page-new_model_1_2"]
        old_paths = [self._write_key(key, mtime=100.0) for key in old_keys]
        new_paths = [self._write_key(key, mtime=200.0) for key in new_keys]

        self._run_single_group_cleanup()
        self.assertFalse(any(os.path.exists(path) for path in old_paths))
        self.assertTrue(all(os.path.exists(path) for path in new_paths))

    def test_tick_deletes_hybrid_components_atomically(self):
        """Evict every pool component and TP rank for one logical page."""
        physical_suffixes = [
            "",
            "_k",
            "_v",
            "_kv_k",
            "_kv_v",
            "_swa_k",
            "_swa_v",
            "_mamba_temporal",
            "_mamba_conv_0",
        ]
        old_keys = [
            f"page-old_model_{rank}_2{suffix}"
            for rank in range(2)
            for suffix in physical_suffixes
        ]
        new_keys = [
            f"page-new_model_{rank}_2{suffix}"
            for rank in range(2)
            for suffix in physical_suffixes
        ]
        old_paths = [self._write_key(key, mtime=100.0) for key in old_keys]
        new_paths = [self._write_key(key, mtime=200.0) for key in new_keys]

        self._run_single_group_cleanup()
        self.assertFalse(any(os.path.exists(path) for path in old_paths))
        self.assertTrue(all(os.path.exists(path) for path in new_paths))

    def test_tick_ignores_non_bucket_directories(self):
        """Only hash-bucket directories are treated as NIXL FILE cache entries."""
        non_bucket = os.path.join(self.base_dirs[0], "not-a-bucket")
        os.makedirs(non_bucket, exist_ok=True)
        unrelated = os.path.join(non_bucket, "page-old_model_0_2")
        with open(unrelated, "wb") as f:
            f.write(b"x")

        cleaner = HiCacheL3Cleaner(
            self.base_dirs,
            tp_rank=0,
            high_watermark=80.0,
            low_watermark=70.0,
            unlink_workers=1,
        )
        cleaner._disk_usage_pct = lambda _path: 90.0

        self.assertFalse(cleaner._tick())
        self.assertTrue(os.path.exists(unrelated))

    def test_safe_unlink_tolerates_missing_and_os_errors(self):
        """Cleanup races should not fail the cleaner tick."""
        missing = os.path.join(self.test_dir, "missing")
        existing = os.path.join(self.test_dir, "existing")
        with open(existing, "wb") as f:
            f.write(b"abc")

        self.assertEqual(_safe_unlink(missing), (False, 0))
        self.assertEqual(_safe_unlink(self.test_dir), (False, 0))
        self.assertEqual(_safe_unlink(existing), (True, 3))
        self.assertFalse(os.path.exists(existing))

    def test_start_only_runs_on_tp_rank_zero(self):
        """Only TP rank 0 owns file cleanup for a shared storage directory."""
        cleaner = HiCacheL3Cleaner(self.base_dirs, tp_rank=1, interval_sec=0.01)
        cleaner.start()
        self.assertIsNone(cleaner._thread)

    def test_nixl_config_parses_l3_cleaner_options(self):
        """Cleaner settings are top-level NIXL config, not plugin init params."""
        cfg = NixlBackendConfig(
            {
                "use_uring": "true",
                "l3_cleaner_enabled": False,
                "l3_cleaner_high_watermark": "85",
                "l3_cleaner_low_watermark": 75,
            }
        )

        cleaner_config = cfg.get_l3_cleaner_config()
        self.assertFalse(cleaner_config["enabled"])
        self.assertEqual(cleaner_config["high_watermark"], 85.0)
        self.assertEqual(cleaner_config["low_watermark"], 75.0)
        self.assertEqual(cfg.get_backend_initparams("POSIX"), {"use_uring": "true"})

        default_config = NixlBackendConfig().get_l3_cleaner_config()
        self.assertTrue(default_config["enabled"])

    def test_nixl_config_rejects_non_boolean_l3_cleaner_enabled(self):
        """Cleaner enablement uses native config booleans only."""
        cfg = NixlBackendConfig({"l3_cleaner_enabled": "false"})

        with self.assertRaises(ValueError):
            cfg.get_l3_cleaner_config()


class TestNixlFileRetention(CustomTestCase):
    """CPU/process coverage for bounded FILE retention coordination."""

    def setUp(self):
        self.test_dir = tempfile.mkdtemp(prefix="test_nixl_retention_")
        self.base_dirs = [
            os.path.join(self.test_dir, "disk0"),
            os.path.join(self.test_dir, "disk1"),
        ]
        self.file_manager = NixlFileManager(self.base_dirs, use_direct_io=False)
        self.retention = NixlFileRetention(self.file_manager.iter_all_base_dirs())
        self.file_manager.set_retention(self.retention)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def _write(self, key: str, data: bytes = b"x") -> str:
        path = self.file_manager.get_file_path(key)
        with open(path, "wb") as output:
            output.write(data)
        return path

    def test_concurrent_initialization_uses_one_stable_lock_inode(self):
        fresh_dirs = [
            os.path.join(self.test_dir, "fresh-disk0"),
            os.path.join(self.test_dir, "fresh-disk1"),
        ]
        for path in fresh_dirs:
            os.makedirs(path)
        start = os.path.join(self.test_dir, "start")
        code = """
import os, sys, time
from sglang.srt.mem_cache.storage.nixl.nixl_retention import NixlFileRetention
while not os.path.exists(sys.argv[3]):
    time.sleep(0.001)
retention = NixlFileRetention(sys.argv[1:3])
with open(sys.argv[4], "w") as output:
    output.write(str(os.stat(retention.stripe_paths[0]).st_ino))
"""
        env = os.environ.copy()
        env["PYTHONPATH"] = os.pathsep.join(sys.path)
        results = [os.path.join(self.test_dir, f"init-{index}") for index in range(8)]
        processes = [
            subprocess.Popen(
                [sys.executable, "-c", code, *fresh_dirs, start, result], env=env
            )
            for result in results
        ]
        for process in processes:
            self.addCleanup(
                lambda process=process: process.poll() is None and process.kill()
            )
        open(start, "w").close()
        for process in processes:
            process.wait(timeout=30)
            self.assertEqual(process.returncode, 0)
        inodes = []
        for result in results:
            with open(result) as input_file:
                inodes.append(input_file.read())
        self.assertEqual(len(set(inodes)), 1)

    def test_expiry_reclaims_all_existing_and_new_pool_siblings(self):
        original = self._write("page-a_model_0_2_kv_k")
        with self.retention.transfer_guard([original]):
            self.retention.publish_deadlines([original], 1, now=10)

        # This sibling was absent when retention was first published. Reclaim
        # must rescan every pool and disk while holding the group stripe.
        sibling = self._write("page-a_model_1_2_deepseek_v4_c128_state")
        result = self.retention.reclaim_group("page-a_model", now=12)

        self.assertTrue(result.reclaimed)
        self.assertEqual(result.removed_files, 2)
        self.assertFalse(os.path.exists(original))
        self.assertFalse(os.path.exists(sibling))
        self.assertIsNone(self.retention.deadline_for_group("page-a_model"))

    def test_renewal_keeps_max_deadline(self):
        path = self._write("page-a_model_0_1")
        with self.retention.transfer_guard([path]):
            self.retention.publish_deadlines([path], 100, now=100)
        with self.retention.transfer_guard([path]):
            self.retention.publish_deadlines([path], 10, now=100)
        self.assertEqual(self.retention.deadline_for_group("page-a_model"), 200)

    def test_retained_write_has_no_expiry_gap(self):
        path = self._write("page-a_model_0_1")
        with self.retention.transfer_guard([path]):
            self.retention.publish_deadlines([path], 1, now=1)

        entered = threading.Event()

        def retained_write():
            with self.retention.transfer_guard([path]):
                entered.set()
                time.sleep(0.15)
                self.retention.publish_deadlines([path], 100, now=10)

        writer = threading.Thread(target=retained_write)
        writer.start()
        self.assertTrue(entered.wait(1))
        result = self.retention.reclaim_group("page-a_model", now=10)
        writer.join(1)

        self.assertFalse(result.reclaimed)
        self.assertTrue(os.path.exists(path))
        self.assertEqual(self.retention.deadline_for_group("page-a_model"), 110)

    def test_active_transfer_blocks_reclaim_in_subprocess(self):
        path = self._write("page-a_model_0_1")
        with self.retention.transfer_guard([path]):
            self.retention.publish_deadlines([path], 1, now=1)
        ready = os.path.join(self.test_dir, "ready")
        code = """
import sys, time
from sglang.srt.mem_cache.storage.nixl.nixl_retention import NixlFileRetention
retention = NixlFileRetention(sys.argv[1:3])
with retention.transfer_guard([sys.argv[3]]):
    open(sys.argv[4], 'w').close()
    time.sleep(0.35)
"""
        env = os.environ.copy()
        env["PYTHONPATH"] = os.pathsep.join(sys.path)
        process = subprocess.Popen(
            [sys.executable, "-c", code, *self.base_dirs, path, ready], env=env
        )
        self.addCleanup(lambda: process.poll() is None and process.kill())
        deadline = time.time() + 20
        while not os.path.exists(ready) and time.time() < deadline:
            time.sleep(0.01)
        self.assertTrue(os.path.exists(ready))

        started = time.monotonic()
        result = self.retention.reclaim_group("page-a_model", now=3)
        elapsed = time.monotonic() - started
        process.wait(timeout=3)

        self.assertGreaterEqual(elapsed, 0.2)
        self.assertTrue(result.reclaimed)
        self.assertFalse(os.path.exists(path))

    def test_clear_serializes_and_preserves_lock_inodes(self):
        path = self._write("page-a_model_0_1")
        lock_inodes = [os.stat(item).st_ino for item in self.retention.stripe_paths]
        entered = threading.Event()

        def active_transfer():
            with self.retention.transfer_guard([path]):
                entered.set()
                time.sleep(0.15)

        worker = threading.Thread(target=active_transfer)
        worker.start()
        self.assertTrue(entered.wait(1))
        started = time.monotonic()
        self.file_manager.clear()
        worker.join(1)

        self.assertGreaterEqual(time.monotonic() - started, 0.1)
        self.assertFalse(os.path.exists(path))
        self.assertEqual(
            lock_inodes, [os.stat(item).st_ino for item in self.retention.stripe_paths]
        )

    def test_canonical_paths_and_traversal_and_symlink_rejection(self):
        relative = os.path.relpath(self.base_dirs[0])
        relative_manager = NixlFileManager(relative, use_direct_io=False)
        self.assertTrue(os.path.isabs(relative_manager.base_dirs[0]))
        with self.assertRaises(ValueError):
            relative_manager.get_file_path("../escape")
        with self.assertRaises(ValueError):
            relative_manager.get_file_path("nested/name")

        safe_path = relative_manager.get_file_path("safe-key")
        bucket = os.path.dirname(safe_path)
        shutil.rmtree(bucket)
        os.symlink(self.test_dir, bucket)
        with self.assertRaises(ValueError):
            relative_manager.get_file_path("safe-key")

    def test_limits_are_validated_before_mutation(self):
        paths = [
            f"/root/object-{index}"
            for index in range(MAX_RETAINED_PHYSICAL_OBJECTS + 1)
        ]
        with self.assertRaises(ValueError):
            self.retention.validate_retained_write(paths, 1)
        for invalid in (0, -1, 86401, float("inf"), "10"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.retention.validate_retained_write(["/root/object"], invalid)
        self.assertEqual(os.listdir(self.retention.deadline_dir), [])

    def test_ordinary_fast_path_has_no_retention_metadata_access(self):
        manager = NixlFileManager(
            os.path.join(self.test_dir, "ordinary"), use_direct_io=False
        )
        path = manager.get_file_path("ordinary-key")
        fd = manager.open_file(path, create=True)
        self.assertIsNotNone(fd)
        os.close(fd)
        self.assertIsNone(manager.retention)
        self.assertFalse(
            os.path.exists(os.path.join(manager.base_dirs[0], ".sglang-nixl-retention"))
        )

    def test_external_or_non_posix_retention_is_explicitly_unsupported(self):
        unsupported = NixlFileRetention(
            self.base_dirs,
            retention_supported=False,
            unsupported_reason="external cleaner or non-POSIX backend",
        )
        with self.assertRaisesRegex(RuntimeError, "unsupported"):
            unsupported.validate_retained_write(["object"], 1)


if __name__ == "__main__":
    unittest.main()
