"""Characterize native cache IO ownership on CPU, without device transfers."""

import threading
import unittest
from contextlib import contextmanager
from queue import Queue
from types import SimpleNamespace
from unittest.mock import Mock

from sglang.test.ci.ci_register import register_cpu_ci
from sglang.test.test_utils import CustomTestCase, maybe_stub_sgl_kernel

maybe_stub_sgl_kernel()

from test.registered.unit.mem_cache.test_storage_prefetch_lifecycle import (
    _staged_fixture,
)

from sglang.srt.mem_cache.base_prefix_cache import CacheRequestHandle
from sglang.srt.mem_cache.hicache_storage import STORAGE_BATCH_SIZE
from sglang.srt.mem_cache.hybrid_cache.hybrid_cache_controller import PrefetchOperation
from sglang.srt.mem_cache.pool_host.mha import MHATokenToKVPoolHost
from sglang.srt.mem_cache.unified_radix_cache import _OngoingPrefetch

register_cpu_ci(est_time=10, suite="base-a-test-cpu")

_WAIT_SECONDS = 5
_PAGE_SIZE = 2


def _make_host_pool(size):
    pool = MHATokenToKVPoolHost.__new__(MHATokenToKVPoolHost)
    pool.device = "cpu"
    pool.size = size
    pool.page_size = _PAGE_SIZE
    pool.lock = threading.RLock()
    pool.clear()
    return pool


def _make_cache(size=160):
    cache, _, _ = _staged_fixture()
    cache.disable = False
    cache.host_memory_mode = "cache"
    cache.buffer_pipeline = None
    cache.prefetch_loaded_tokens_by_reqid.clear()
    cache.prefetch_loaded_storage_start_by_reqid.clear()
    cache.tree_core.inc_host_lock_ref = Mock(
        return_value=SimpleNamespace(to_dec_params=lambda: None)
    )
    cc = cache.cache_controller
    cc.host_memory_mode = "cache"
    del cc.prefetch_rate_limited
    cc.prefetch_capacity_limit = size // 2
    cc.prefetch_tokens_occupied = 0
    cc.mem_pool_host = _make_host_pool(size)
    cc.storage_host_pool = cc.mem_pool_host
    cc.storage_stop_event = threading.Event()
    cc.prefetch_buffer = Queue()
    cc.prefetch_sync_queue = Queue()
    cc.prefetch_hit_queue = Queue()
    cc.ack_prefetch_queue = Queue()
    cc.ack_backup_queue = Queue()
    cc.host_mem_release_queue = Queue()
    cc.extra_host_mem_release_queues = {}
    cc.prefetch_completion_sync_groups = []
    cc.page_get_func = cc._page_get_zero_copy
    return cache


class _BlockingBackend:
    """A synchronous Python IO boundary; it does not model DMA completion."""

    def __init__(self, blocked_call, *, blocked_success=True):
        self.blocked_call = blocked_call
        self.blocked_success = blocked_success
        self.started = [threading.Event(), threading.Event()]
        self.release = threading.Event()
        self.calls = []

    def batch_get_v1(self, hashes, host_indices, extra_info):
        call = len(self.calls)
        self.calls.append(list(hashes))
        self.started[call].set()
        if call == self.blocked_call:
            if not self.release.wait(_WAIT_SECONDS):
                raise TimeoutError("The test did not release its backend IO boundary")
            return [self.blocked_success] * len(hashes)
        return [True] * len(hashes)


@contextmanager
def _storage_workers(controller, backend, *, sync=False):
    errors = Queue()

    def run(target):
        try:
            target()
        except BaseException as error:
            errors.put((error, error.__traceback__))

    targets = [controller.prefetch_io_aux_func]
    if sync:
        targets.append(controller.prefetch_sync_thread_func)
    threads = [threading.Thread(target=run, args=(target,)) for target in targets]
    for thread in threads:
        thread.start()
    try:
        yield
    finally:
        backend.release.set()
        controller.storage_stop_event.set()
        controller.prefetch_buffer.put(None)
        controller.prefetch_sync_queue.put(None)
        for thread in threads:
            thread.join(_WAIT_SECONDS)
        if any(thread.is_alive() for thread in threads):
            raise AssertionError("A cache IO test worker did not stop")
        if not errors.empty():
            error, traceback = errors.get_nowait()
            raise error.with_traceback(traceback)


def _operation(controller, handle, pages, prefix):
    operation = PrefetchOperation(handle, list(range(pages * _PAGE_SIZE)))
    operation.hash_value = [f"{prefix}{page}" for page in range(pages)]
    operation.host_indices = controller.mem_pool_host.alloc(pages * _PAGE_SIZE)
    assert operation.host_indices is not None
    return operation


def _drain(cache, *, acks=0, releases=0):
    cache._drain_storage_control_queues_impl(
        n_storage_hit=0,
        n_ack_prefetch=acks,
        n_backup=0,
        n_release=releases,
        extra_release_counts={},
        log_metrics=False,
    )


class TestCacheIOBackpressureCharacterization(CustomTestCase):
    def test_cache_mode_threshold_checks_current_intent_before_enqueue(self):
        cache = _make_cache()
        cc = cache.cache_controller
        cc.prefetch_tokens_occupied = 64
        available = cc.mem_pool_host.available_size()
        handle = CacheRequestHandle("soft-limit", 0)

        self.assertEqual(cc.prefetch_capacity_limit, 80)
        self.assertFalse(cc.prefetch_rate_limited())
        cache.prefetch_from_storage(handle, 0, list(range(32)))

        self.assertEqual(cc.prefetch_tokens_occupied, 96)
        self.assertTrue(cc.prefetch_rate_limited())
        self.assertIn(handle, cache.ongoing_prefetch)
        self.assertIs(
            cc.prefetch_queue.get_nowait(), cache.ongoing_prefetch[handle].operation
        )
        self.assertEqual(cc.mem_pool_host.available_size(), available)

    def test_active_read_is_not_counted_in_prefetch_queue(self):
        cache = _make_cache()
        cc = cache.cache_controller
        backend = _BlockingBackend(0)
        cc.storage_backend = backend
        first = _operation(cc, CacheRequestHandle("first", 0), 1, "a")
        second = _operation(cc, CacheRequestHandle("second", 0), 1, "b")
        cc.prefetch_buffer.put(first)

        with _storage_workers(cc, backend):
            self.assertTrue(backend.started[0].wait(_WAIT_SECONDS))
            cc.prefetch_buffer.put(second)
            self.assertEqual(cc.prefetch_buffer.qsize(), 1)
            self.assertEqual(backend.calls, [first.hash_value])
            self.assertFalse(backend.started[1].is_set())

            backend.release.set()
            self.assertTrue(backend.started[1].wait(_WAIT_SECONDS))
            acks = [cc.prefetch_sync_queue.get(timeout=_WAIT_SECONDS) for _ in range(4)]
            self.assertEqual(backend.calls, [first.hash_value, second.hash_value])
            self.assertEqual(
                [ack.operation for ack in acks], [first, first, second, second]
            )
            self.assertEqual(
                [bool(ack.completed_req) for ack in acks], [False, True, False, True]
            )

    def test_cancel_releases_completed_prefix_before_inflight_tail(self):
        pages = STORAGE_BATCH_SIZE + 1
        cache = _make_cache(pages * _PAGE_SIZE)
        cc = cache.cache_controller
        pool = cc.mem_pool_host
        backend = _BlockingBackend(1, blocked_success=False)
        cc.storage_backend = backend
        handle = CacheRequestHandle("cancel-tail", 0)
        operation = _operation(cc, handle, pages, "page")
        cc.prefetch_tokens_occupied = len(operation.token_ids)
        cache.ongoing_prefetch[handle] = _OngoingPrefetch(
            0, operation.token_ids, operation.host_indices, operation, None, {}
        )
        cc.prefetch_buffer.put(operation)
        completed = STORAGE_BATCH_SIZE * _PAGE_SIZE

        with _storage_workers(cc, backend, sync=True):
            self.assertTrue(backend.started[1].wait(_WAIT_SECONDS))
            progress = cc.ack_prefetch_queue.get(timeout=_WAIT_SECONDS)
            self.assertEqual(progress.completed_tokens, completed)
            cc.ack_prefetch_queue.put(progress)
            _drain(cache, acks=1)
            self.assertEqual(operation.completed_tokens, completed)

            cache.release_aborted_request(handle)
            self.assertNotIn(handle, cache.ongoing_prefetch)
            self.assertEqual(cc.prefetch_tokens_occupied, 0)
            self.assertEqual(pool.available_size(), 0)
            self.assertTrue(pool.slot_used[operation.host_indices].all())

            _drain(cache, releases=cc.host_mem_release_queue.qsize())
            self.assertEqual(pool.available_size(), completed)
            self.assertTrue(pool.slot_used[operation.host_indices[completed:]].all())
            self.assertFalse(pool.slot_used[operation.host_indices[:completed]].any())

            backend.release.set()
            acks = [cc.ack_prefetch_queue.get(timeout=_WAIT_SECONDS) for _ in range(2)]
            self.assertEqual(acks[0].completed_tokens, completed)
            self.assertTrue(acks[1].completed_req)
            for ack in acks:
                cc.ack_prefetch_queue.put(ack)
            _drain(cache, acks=2)
            self.assertEqual(pool.available_size(), completed)
            self.assertTrue(pool.slot_used[operation.host_indices[completed:]].all())
            self.assertEqual(cc.host_mem_release_queue.qsize(), 1)

            _drain(cache, releases=1)
            self.assertEqual(pool.available_size(), pages * _PAGE_SIZE)
            self.assertFalse(pool.slot_used.any())


if __name__ == "__main__":
    unittest.main()
