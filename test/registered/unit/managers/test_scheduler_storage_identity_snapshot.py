import builtins
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import torch

from sglang.test.ci.ci_register import register_cpu_ci
from sglang.test.test_utils import CustomTestCase, maybe_stub_sgl_kernel

maybe_stub_sgl_kernel()

from test.registered.unit.mem_cache.test_mooncake_group_semantics import (
    FakeHostKVCache,
    _make_store,
)
from test.registered.unit.mem_cache.test_mooncake_tenant_config import (
    FakeMooncakeDistributedStore,
    _fake_mooncake_modules,
    _make_storage_config,
)

from sglang.srt.managers.io_struct import GetInternalStateReq
from sglang.srt.managers.scheduler import Scheduler
from sglang.srt.mem_cache.storage.mooncake_store.mooncake_store import MooncakeStore
from sglang.srt.runtime_context import get_context

register_cpu_ci(est_time=12, suite="base-a-test-cpu")

SNAPSHOT_KEY = "hicache_storage_identity_snapshot"


def _make_scheduler(backend=None, *, enabled=True):
    scheduler = Scheduler.__new__(Scheduler)
    scheduler.tree_cache = SimpleNamespace(
        cache_controller=SimpleNamespace(
            enable_storage=enabled, storage_backend=backend
        )
    )
    scheduler.max_total_num_tokens = 100
    scheduler.max_req_input_len = 32
    scheduler.startup_time = 1.0
    scheduler.metrics_reporter = SimpleNamespace(
        last_gen_throughput=1.0,
        spec_total_num_forward_ct=0,
        spec_total_num_accept_tokens=0,
        step_time_dict={},
    )
    scheduler.tp_worker = SimpleNamespace(
        model_runner=SimpleNamespace(weight_load_mem_usage=1.0),
        graph_memory_usage=None,
    )
    scheduler.token_to_kv_pool_allocator = SimpleNamespace(
        get_kvcache=lambda: SimpleNamespace(mem_usage=3.0)
    )
    scheduler.startup_available_gpu_memory_gb = 4.0
    scheduler.swa_tokens_per_layer = None
    scheduler.max_running_requests = 8
    scheduler.spec_algorithm = SimpleNamespace(
        is_none=lambda: True, is_dspark=lambda: False
    )
    scheduler.draft_worker = None
    return scheduler


class TestSchedulerStorageIdentitySnapshot(CustomTestCase):
    def _live_snapshot(self, scheduler):
        with get_context().override_server_args(
            tp_size=1, pp_size=1, dp_size=1, enable_dp_attention=False
        ):
            return scheduler.get_internal_state(GetInternalStateReq()).internal_state[
                SNAPSHOT_KEY
            ]

    def test_absent_controller_or_backend_returns_none(self):
        scheduler = _make_scheduler()
        for tree_cache in (
            None,
            SimpleNamespace(),
            SimpleNamespace(cache_controller=None),
            scheduler.tree_cache,
        ):
            with self.subTest(tree_cache=tree_cache):
                scheduler.tree_cache = tree_cache
                self.assertIsNone(scheduler._get_hicache_storage_identity_snapshot())

    def test_disabled_backend_returns_none_without_importing_store(self):
        store, _ = _make_store(extra_backend_tag="pool", model_name="acme/model")
        scheduler = _make_scheduler(store, enabled=False)
        original_import = builtins.__import__

        def guarded_import(name, *args, **kwargs):
            if name.endswith("storage.mooncake_store.mooncake_store"):
                self.fail("A disabled backend must not import MooncakeStore")
            return original_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=guarded_import):
            self.assertIsNone(scheduler._get_hicache_storage_identity_snapshot())

    def test_dummy_backend_cannot_publish_lookalike_fields(self):
        dummy = SimpleNamespace(
            config_prefix="invented-prefix",
            config=SimpleNamespace(
                tenant_id="invented-tenant", standalone_storage=False
            ),
        )
        scheduler = _make_scheduler(dummy)

        self.assertIsNone(scheduler._get_hicache_storage_identity_snapshot())

    def test_uninitialized_store_returns_none(self):
        scheduler = _make_scheduler(MooncakeStore.__new__(MooncakeStore))

        self.assertIsNone(scheduler._get_hicache_storage_identity_snapshot())

    def test_standalone_store_returns_none(self):
        store, _ = _make_store(extra_backend_tag="pool")
        store.config.standalone_storage = True
        scheduler = _make_scheduler(store)

        self.assertIsNone(scheduler._get_hicache_storage_identity_snapshot())

    def test_real_constructor_snapshot_matches_real_object_keys(self):
        cases = (
            (None, None, None, ["page0_0_k", "page0_0_v"]),
            ("", None, "", ["_page0_0_k", "_page0_0_v"]),
            (
                "pool",
                "acme/model",
                "pool_acme-model",
                ["pool_acme-model_page0_0_k", "pool_acme-model_page0_0_v"],
            ),
        )
        for tag, model, prefix, expected_keys in cases:
            with self.subTest(tag=tag, model=model):
                store, transport = _make_store(extra_backend_tag=tag, model_name=model)
                scheduler = _make_scheduler(store)

                self.assertEqual(
                    scheduler._get_hicache_storage_identity_snapshot(),
                    {"config_prefix": prefix, "store_tenant": "default"},
                )
                store.register_mem_pool_host(FakeHostKVCache(objects_per_page=2))
                self.assertEqual(
                    store.batch_set_v1(["page0"], torch.tensor([0])), [True]
                )
                self.assertEqual(transport.batch_put_calls[0]["keys"], expected_keys)

    def test_nondefault_tenant_comes_from_actual_setup(self):
        with patch.dict(
            "sys.modules", _fake_mooncake_modules(FakeMooncakeDistributedStore)
        ):
            store = MooncakeStore(_make_storage_config("  tenant-a  "))
        transport = FakeMooncakeDistributedStore.instances[-1]

        self.assertEqual(transport.setup_calls[0][1]["tenant_id"], "tenant-a")
        self.assertEqual(
            _make_scheduler(store)._get_hicache_storage_identity_snapshot(),
            {"config_prefix": "test", "store_tenant": "tenant-a"},
        )

    def test_snapshot_is_a_fresh_dict(self):
        store, _ = _make_store(extra_backend_tag="pool", model_name="acme/model")
        scheduler = _make_scheduler(store)
        first = scheduler._get_hicache_storage_identity_snapshot()
        second = scheduler._get_hicache_storage_identity_snapshot()

        self.assertIsNot(first, second)
        first["config_prefix"] = "changed"
        first["store_tenant"] = "changed"
        self.assertEqual(
            scheduler._get_hicache_storage_identity_snapshot(),
            {"config_prefix": "pool_acme-model", "store_tenant": "default"},
        )
        self.assertEqual(store._tag_keys(["page0"]), ["pool_acme-model_page0"])

    def test_both_existing_info_methods_publish_the_snapshot(self):
        store, _ = _make_store(extra_backend_tag="pool", model_name="acme/model")
        scheduler = _make_scheduler(store)
        expected = {"config_prefix": "pool_acme-model", "store_tenant": "default"}

        self.assertEqual(scheduler.get_init_info()[SNAPSHOT_KEY], expected)
        self.assertEqual(self._live_snapshot(scheduler), expected)

    def test_live_snapshot_rereads_backend_after_startup(self):
        first_store, _ = _make_store(extra_backend_tag="first")
        scheduler = _make_scheduler(first_store)
        startup = scheduler.get_init_info()[SNAPSHOT_KEY]
        controller = scheduler.tree_cache.cache_controller

        controller.enable_storage = False
        self.assertIsNone(self._live_snapshot(scheduler))
        controller.storage_backend, _ = _make_store(extra_backend_tag="second")
        controller.enable_storage = True

        self.assertEqual(
            self._live_snapshot(scheduler),
            {"config_prefix": "second", "store_tenant": "default"},
        )
        self.assertEqual(startup, {"config_prefix": "first", "store_tenant": "default"})

    def test_config_mirror_cannot_manufacture_actual_identity(self):
        scheduler = _make_scheduler()
        scheduler.server_args = SimpleNamespace(
            served_model_name="mirror/model",
            hicache_storage_backend="mooncake",
            hicache_storage_backend_extra_config={"extra_backend_tag": "mirror"},
        )

        self.assertIsNone(scheduler._get_hicache_storage_identity_snapshot())
        store, _ = _make_store(extra_backend_tag="actual", model_name="actual/model")
        scheduler.tree_cache.cache_controller.storage_backend = store
        self.assertEqual(
            scheduler._get_hicache_storage_identity_snapshot(),
            {"config_prefix": "actual_actual-model", "store_tenant": "default"},
        )


if __name__ == "__main__":
    unittest.main()
