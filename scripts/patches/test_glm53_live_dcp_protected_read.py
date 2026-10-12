"""CPU regression on the trusted live overlay, not a native transport proof.

Runs the real DCP scratch/locking methods with real CPU Torch allocations.
The SDK is a strict signature double: no client setup, grant, receipt or IO.
"""

import ctypes
import threading
from types import SimpleNamespace
from unittest.mock import MagicMock, create_autospec

import pytest
from sglang.srt.mem_cache.storage.dcp_hicache_storage import DCPHiCacheStorage


class ScratchSDK:
    """Shape of the independently inspected native Python binding."""

    def get_into(self, key: str, pointer: int, size: int) -> int:
        raise AssertionError("signature double only")

    def unregister_buffer(self, pointer: int) -> int:
        raise AssertionError("signature double only")


def descriptor() -> dict:
    return {
        "version": 1,
        "tp_size": 8,
        "pp_size": 1,
        "dcp_size": 4,
        "physical_page": 64,
        "logical_page": 256,
        "model_manifest_sha256": "a" * 64,
        "config_sha256": "b" * 64,
        "tokenizer_sha256": "c" * 64,
        "position_sha256": "d" * 64,
        "mla_page_nbytes": 16,
        "indexer_page_nbytes": 16,
        "layout": "page_first",
        "kv_format": "fp8",
        "indexer_format": "fp8",
        "layer_bitmap": [0],
    }


@pytest.fixture
def adapter():
    store = create_autospec(ScratchSDK, instance=True, spec_set=True)
    store.unregister_buffer.return_value = 0
    legacy = MagicMock(side_effect=RuntimeError("ordinary READ rejected"))
    backend = SimpleNamespace(
        store=store,
        _get_batch_zero_copy_impl=legacy,
        _durability=object(),
        config=SimpleNamespace(standalone_storage=False),
        register_buffer=MagicMock(),
        close=MagicMock(),
    )
    storage = DCPHiCacheStorage(backend, descriptor(), 0, 0, 2)
    try:
        yield storage, store, legacy
    finally:
        if not storage.closed:
            storage.close()


def test_real_blob_uses_protected_scalar_entry_and_copies_bytes(adapter):
    storage, store, legacy = adapter
    data = b"ack-data"
    scratch = storage.scratch
    assert scratch is not None

    def read(key, pointer, size):
        assert key == "root_ack2_1"
        assert pointer == scratch.data_ptr()
        assert size == len(data)
        ctypes.memmove(pointer, data, size)
        return size

    store.get_into.side_effect = read
    result = storage._blob("root_ack2_1", len(data))
    assert result == data
    scratch.zero_()
    assert result == data
    store.get_into.assert_called_once_with("root_ack2_1", scratch.data_ptr(), len(data))
    legacy.assert_not_called()


@pytest.mark.parametrize("returned", [-800, -703, None, 0, 3, 9, True, 8.0])
def test_wrong_or_partial_result_remains_unknown_without_legacy_retry(
    adapter, returned
):
    storage, store, legacy = adapter
    store.get_into.return_value = returned
    assert storage._blob("root_ack2_1", 8) is None
    store.get_into.assert_called_once()
    legacy.assert_not_called()


@pytest.mark.parametrize(
    "error", [OSError("io"), ValueError("proof"), RuntimeError("grant")]
)
def test_native_read_failure_is_not_retried_via_plain_batch(adapter, error):
    storage, store, legacy = adapter
    store.get_into.side_effect = error
    assert storage._blob("root_ack2_1", 8) is None
    store.get_into.assert_called_once()
    legacy.assert_not_called()


@pytest.mark.parametrize("size", [0, -1, None, True, 8.0, 10000000])
def test_invalid_or_unowned_span_does_not_enter_sdk(adapter, size):
    storage, store, legacy = adapter
    assert storage._blob("root_ack2_1", size) is None
    store.get_into.assert_not_called()
    legacy.assert_not_called()


@pytest.mark.parametrize("state", ["closed", "closing", "cancelled"])
def test_lifecycle_guard_never_reads(adapter, state):
    storage, store, legacy = adapter
    if state == "cancelled":
        storage.cancelled = lambda: True
    else:
        setattr(storage, state, True)
    assert storage._blob("root_ack2_1", 8) is None
    store.get_into.assert_not_called()
    legacy.assert_not_called()
    storage.closed = False
    storage.closing = False


def test_missing_native_entry_fails_before_buffer_registration():
    backend = SimpleNamespace(
        _get_batch_zero_copy_impl=MagicMock(),
        _durability=object(),
        store=SimpleNamespace(unregister_buffer=lambda pointer: 0),
        config=SimpleNamespace(standalone_storage=False),
        register_buffer=MagicMock(),
    )
    with pytest.raises(ValueError, match="protected scalar reads"):
        DCPHiCacheStorage(backend, descriptor(), 0, 0, 2)
    backend.register_buffer.assert_not_called()


def test_close_cannot_unregister_scratch_during_native_read(adapter):
    storage, store, legacy = adapter
    entered = threading.Event()
    release = threading.Event()
    closing = threading.Event()
    results = []
    failures = []
    data = b"ack-data"

    def read(key, pointer, size):
        entered.set()
        if not release.wait(5):
            raise RuntimeError("test release deadline")
        ctypes.memmove(pointer, data, size)
        return size

    def blob():
        try:
            results.append(storage._blob("root_ack2_1", len(data)))
        except (
            OSError,
            ValueError,
            RuntimeError,
            AssertionError,
            TypeError,
            AttributeError,
        ) as error:
            failures.append(error)

    def close():
        closing.set()
        try:
            storage.close()
        except (
            OSError,
            ValueError,
            RuntimeError,
            AssertionError,
            TypeError,
            AttributeError,
        ) as error:
            failures.append(error)

    store.get_into.side_effect = read
    reader = threading.Thread(target=blob, daemon=True)
    closer = threading.Thread(target=close, daemon=True)
    reader.start()
    try:
        assert entered.wait(1), "real blob never called the scalar protected entry"
        closer.start()
        assert closing.wait(1)
        store.unregister_buffer.assert_not_called()
    finally:
        release.set()
        reader.join(6)
        if closer.ident is not None:
            closer.join(6)
    assert not reader.is_alive()
    assert not closer.is_alive()
    assert failures == []
    assert results == [data]
    assert storage.closed
    assert storage.scratch is None
    store.unregister_buffer.assert_called_once()
    legacy.assert_not_called()
