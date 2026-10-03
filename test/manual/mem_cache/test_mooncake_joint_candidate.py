"""Explicit Linux integration entry; requires a freshly built native Mooncake.

Run this file with MOONCAKE_JOINT_MASTER_BIN and MOONCAKE_JOINT_EVIDENCE set.
There are no dependency stubs or skips. The Qwen geometry is a byte fixture,
not a model, GPU transfer, scheduler startup, or deployment correctness test.
"""

import hashlib
import json
import os
import socket
import subprocess
import sys
import time
import unittest
import uuid
from pathlib import Path
from types import SimpleNamespace

import requests
import torch

from sglang.srt.managers.scheduler import Scheduler
from sglang.srt.mem_cache.hicache_storage import HiCacheStorageConfig
from sglang.srt.mem_cache.memory_pool import MHATokenToKVPool
from sglang.srt.mem_cache.pool_host.mha import MHATokenToKVPoolHost
from sglang.srt.mem_cache.storage.mooncake_store import mooncake_store
from sglang.srt.mem_cache.storage.mooncake_store.mooncake_store import MooncakeStore


def _sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _free_ports(count):
    sockets = [socket.socket() for _ in range(count)]
    try:
        for sock in sockets:
            sock.bind(("127.0.0.1", 0))
        return [sock.getsockname()[1] for sock in sockets]
    finally:
        for sock in sockets:
            sock.close()


class MooncakeJointCandidateTest(unittest.TestCase):
    def test_full_page_host_tcp_roundtrip(self):
        self.assertEqual(sys.platform, "linux", "This entry requires Linux native TCP")
        master_bin = Path(os.environ["MOONCAKE_JOINT_MASTER_BIN"]).resolve(strict=True)
        evidence_path = Path(os.environ["MOONCAKE_JOINT_EVIDENCE"]).resolve()
        evidence_path.parent.mkdir(parents=True, exist_ok=True)
        import mooncake.store as native_store

        native_path = Path(native_store.__file__).resolve(strict=True)
        self.assertIn(".so", native_path.name)
        evidence = {
            "status": "STARTED",
            "scope": "CPU FULL/page64/page_first/BF16 host TCP; no inference or GPU",
            "sg_source_sha": os.environ["JOINT_SG_SOURCE_SHA"],
            "mc_source_sha": os.environ["JOINT_MC_SOURCE_SHA"],
            "python": sys.version,
            "torch": torch.__version__,
            "native_binding": {"path": str(native_path), "sha256": _sha256(native_path)},
            "master": {"path": str(master_bin), "sha256": _sha256(master_bin)},
            "entry_sha256": _sha256(__file__),
            "sg_backend": {
                "path": str(Path(mooncake_store.__file__).resolve()),
                "sha256": _sha256(mooncake_store.__file__),
            },
            "geometry": {"layers": 24, "kv_heads": 2, "head_dim": 64, "page_size": 64},
            "segment_bytes": 64 << 20,
            "cleanup": {},
        }
        rpc_port, metrics_port, metadata_port, client_port = _free_ports(4)
        backend = host = None
        registered = False
        allocations = []
        master = None
        log_path = evidence_path.with_suffix(".master.log")
        log = log_path.open("wb")
        try:
            master = subprocess.Popen(
                [
                    str(master_bin),
                    f"--port={rpc_port}",
                    "--rpc_address=127.0.0.1",
                    "--enable_metric_reporting=true",
                    f"--metrics_port={metrics_port}",
                    "--metrics_host=127.0.0.1",
                    "--enable_http_metadata_server=true",
                    f"--http_metadata_server_port={metadata_port}",
                    "--http_metadata_server_host=127.0.0.1",
                    "--logtostderr=true",
                ],
                stdout=log,
                stderr=subprocess.STDOUT,
            )
            # HTTP response readiness, followed by normal setup/warmup below.
            deadline = time.monotonic() + 30
            with requests.Session() as session:
                session.trust_env = False
                while True:
                    self.assertIsNone(master.poll(), f"Master exited; see {log_path}")
                    try:
                        response = session.get(
                            f"http://127.0.0.1:{metrics_port}/health", timeout=1
                        )
                        response.raise_for_status()
                        health = response.json()
                        evidence["master_health"] = health
                        if (
                            isinstance(health, dict)
                            and health.get("status") == "ok"
                            and health.get("service_ready") is True
                        ):
                            break
                    except (requests.RequestException, ValueError):
                        pass
                    if time.monotonic() >= deadline:
                        self.fail(f"Master HTTP readiness timed out; see {log_path}")
                    time.sleep(0.05)

            device_pool = MHATokenToKVPool(
                size=64,
                page_size=64,
                dtype=torch.bfloat16,
                head_num=2,
                head_dim=64,
                layer_num=24,
                device="cpu",
                enable_memory_saver=False,
                enable_alt_stream=False,
            )
            host = MHATokenToKVPoolHost(
                device_pool,
                host_to_device_ratio=7,
                host_size=0,
                page_size=64,
                layout="page_first",
                pin_memory=False,
                device="cpu",
            )
            self.assertIsNotNone(host.kv_buffer)
            self.assertEqual(host.kv_buffer.device.type, "cpu")
            evidence["host_tensor_bytes"] = host.kv_buffer.numel() * host.kv_buffer.element_size()
            evidence["device_fixture_bytes"] = sum(
                buf.numel() * buf.element_size()
                for buf in (*device_pool.k_buffer, *device_pool.v_buffer)
            )
            for size in (128, 128, 128, 64):
                indices = host.alloc(size)
                self.assertIsNotNone(indices)
                allocations.append(indices)
            source, target, native_target, missing_target = allocations
            pattern = torch.arange(128 * 24 * 2 * 64).reshape(128, 24, 2, 64) % 251
            host.k_buffer[source] = pattern.to(torch.bfloat16)
            host.v_buffer[source] = (pattern + 1).to(torch.bfloat16)
            for indices in (target, native_target, missing_target):
                host.k_buffer[indices] = -123
                host.v_buffer[indices] = -124
            missing_before = (
                host.k_buffer[missing_target].clone(), host.v_buffer[missing_target].clone()
            )
            config = HiCacheStorageConfig(
                tp_rank=0, tp_size=1, pp_rank=0, pp_size=1,
                attn_cp_rank=0, attn_cp_size=1, is_mla_model=False,
                enable_storage_metrics=False, is_page_first_layout=True,
                model_name="Qwen/Qwen2.5-0.5B-Instruct",
                extra_config={
                    "local_hostname": f"127.0.0.1:{client_port}",
                    "metadata_server": f"http://127.0.0.1:{metadata_port}/metadata",
                    "global_segment_size": 64 << 20,
                    "protocol": "tcp", "device_name": "",
                    "master_server_address": f"127.0.0.1:{rpc_port}",
                    # Fresh master has no segments until normal setup below.
                    # Strict native /health above is the startup readiness gate.
                    "master_metrics_port": metrics_port, "check_server": False,
                    "standalone_storage": False,
                    "extra_backend_tag": f"joint-{uuid.uuid4().hex}",
                },
            )
            backend = MooncakeStore(config, mem_pool=host)
            self.assertIsInstance(backend.store, native_store.MooncakeDistributedStore)
            backend.register_mem_pool_host(host)
            registered = True
            keys = ["page-a", "page-b"]
            put_result = backend.batch_set_v1(keys, source)
            self.assertEqual(put_result, [True, True])
            self.assertEqual(backend.batch_exists(keys), 2)
            get_result = backend.batch_get_v1(keys, target)
            self.assertEqual(get_result, [True, True])
            for src, dst in ((source, target), (source, native_target)):
                if dst is native_target:
                    native_keys, pointers, sizes = backend._batch_preprocess(
                        backend._tag_keys(keys), dst
                    )
                    native_result = backend.store.batch_get_into(native_keys, pointers, sizes)
                    self.assertEqual(native_result, sizes)
                    evidence["native_get_bytes"] = native_result
                for buffer in (host.k_buffer, host.v_buffer):
                    self.assertTrue(torch.equal(
                        buffer[src].contiguous().view(torch.uint8),
                        buffer[dst].contiguous().view(torch.uint8),
                    ), "Complete K/V page byte mismatch")
            self.assertEqual(backend.batch_set_v1(keys, source), [True, True])
            self.assertEqual(backend.batch_get_v1(keys, target), [True, True])
            self.assertEqual(backend.batch_exists(["cold-page"]), 0)
            self.assertEqual(backend.batch_get_v1(["cold-page"], missing_target), [False])
            missing_keys, pointers, sizes = backend._batch_preprocess(
                backend._tag_keys(["cold-page"]), missing_target
            )
            native_miss = backend.store.batch_get_into(missing_keys, pointers, sizes)
            self.assertEqual(len(native_miss), 2)
            self.assertTrue(all(code < 0 for code in native_miss))
            for buffer, before in zip((host.k_buffer, host.v_buffer), missing_before):
                self.assertTrue(torch.equal(
                    buffer[missing_target].contiguous().view(torch.uint8),
                    before.contiguous().view(torch.uint8),
                ))

            # Only the diagnostic receiver is constructed without model startup.
            # The production getter reads the very same normal backend instance.
            scheduler = Scheduler.__new__(Scheduler)
            scheduler.tree_cache = SimpleNamespace(cache_controller=SimpleNamespace(
                enable_storage=True, storage_backend=backend
            ))
            identity = scheduler._get_hicache_storage_identity_snapshot()
            self.assertEqual(identity, {
                "config_prefix": backend.config_prefix, "store_tenant": "default"
            })
            mapped = sorted({
                line.split()[-1] for line in Path("/proc/self/maps").read_text().splitlines()
                if len(line.split()) >= 6 and ".so" in line.split()[-1]
                and ("mooncake" in line.split()[-1] or "transfer_engine" in line.split()[-1])
            })
            evidence["mapped_native_libraries"] = [
                {"path": path, "sha256": _sha256(path)} for path in mapped
            ]
            self.assertIn(str(native_path), mapped)
            evidence.update({
                "sg_put_pages": put_result, "sg_get_pages": get_result,
                "native_missing_errors": native_miss, "identity": identity,
                "full_page_bytes_equal": True, "missing_target_unchanged": True,
                "all_synchronous_io_returned": True,
            })
        finally:
            # Keep real backing tensors alive through native unregister/close.
            # This is ordinary synchronous cleanup, not an arbitrary DMA-drain proof.
            try:
                if backend is not None:
                    try:
                        backend.clear()  # The master is private to this test.
                        if registered:
                            rc = backend.store.unregister_buffer(host.kv_buffer.data_ptr())
                            evidence["cleanup"]["unregister_code"] = rc
                            self.assertEqual(rc, 0)
                    finally:
                        rc = backend.store.close()
                        evidence["cleanup"]["native_close_code"] = rc
                        self.assertEqual(rc, 0)
                if host is not None:
                    for indices in allocations:
                        self.assertEqual(host.free(indices), len(indices))
                    host.destroy()
                    evidence["cleanup"]["host_destroyed"] = host.kv_buffer is None
            finally:
                if master is not None:
                    if master.poll() is None:
                        master.terminate()
                        try:
                            master.wait(timeout=10)
                        except subprocess.TimeoutExpired:
                            master.kill()
                            master.wait(timeout=10)
                            evidence["cleanup"]["forced_master_kill"] = True
                            self.fail("Owned master did not terminate normally")
                    evidence["cleanup"]["master_reaped"] = master.poll() is not None
                log.close()
                evidence["status"] = "IO_COMPLETE" if evidence.get("all_synchronous_io_returned") else "FAILED"
                evidence_path.write_text(json.dumps(evidence, indent=2) + "\n")


if __name__ == "__main__":
    unittest.main()
