"""CPU call-site regression on the trusted captured worker package.

Uses the real native hash, real DCP prepare and real shared-read key builder.
Only admission voting/storage reservation are doubles; no GPU/receipt proof.
"""

import threading
from array import array
from types import SimpleNamespace
from unittest.mock import create_autospec

import pytest
from sglang.srt.mem_cache.radix_cache import RadixKey
from sglang.srt.mem_cache.unified_cache.prompt_cache_dcp_retention import (
    DCPRetentionBridge,
)
from sglang.srt.mem_cache.unified_cache.prompt_cache_shared_read import native_page_keys
from sglang.srt.mem_cache.utils import (
    compute_node_hash_values,
    get_hash_str,
    get_storage_hash_str,
)


@pytest.mark.parametrize(
    "extra_key,salt",
    [
        (None, None),
        (None, "tenant-a"),
        ("adapter-a", None),
        ("", ""),
        ("适配器", "租户"),
    ],
)
def test_actual_prepare_and_shared_read_use_storage_namespace(extra_key, salt):
    tokens = array("q", range(768))
    key = RadixKey(tokens, extra_key, cache_salt=salt)
    node = SimpleNamespace(parent=None, key=key)
    expected = compute_node_hash_values(node, 256)
    assert expected == get_storage_hash_str(key, page_size=256)
    if extra_key is not None or salt is not None:
        assert expected != get_hash_str(list(tokens), page_size=256)

    captured_pages = []

    def reserve(operation, pages, duration):
        captured_pages.append(list(pages))
        return {"acknowledged_retain_for_ms": duration}

    lease = SimpleNamespace(
        prefix_tokens=768,
        tiers=("L1", "L3"),
        plan=SimpleNamespace(retain_for_ms=300000),
        expiration_deadline=300000000000,
    )
    manager = SimpleNamespace(
        leases={("reservation", "endpoint"): lease}, clock=lambda: 0
    )
    cache = SimpleNamespace(page_size=256, _all_reduce=lambda tensor, op: None)
    producer = SimpleNamespace(
        cache=cache, _vote=lambda ok: ok, _gather=lambda row: [row], _rank_id=lambda: 0
    )
    bridge = create_autospec(DCPRetentionBridge, instance=True)
    bridge.manager = manager
    bridge.producer = producer
    bridge.dcp = SimpleNamespace(prepare_cache_retention=reserve)
    bridge.groups = {}
    bridge.endpoints = {}
    bridge.io_scopes = {}
    bridge.io_lock = threading.RLock()
    body = {"token_ids": tokens, "extra_key": extra_key, "cache_salt": salt}
    claims = {
        "reservation_id": "reservation",
        "native_incarnation": "native",
        "authority_revision": "revision",
        "native_request_id": "request",
        "request_started_at_ms": 1,
    }
    DCPRetentionBridge.prepare(bridge, body, claims)
    assert captured_pages == [expected]
    req = SimpleNamespace(origin_input_ids=tokens, extra_key=extra_key, cache_salt=salt)
    assert native_page_keys(req, 768, 256) == expected


@pytest.mark.parametrize("salt", [None, "tenant-a", "租户"])
def test_storage_namespace_survives_radix_split(salt):
    tokens = array("q", range(768))
    whole = RadixKey(tokens, "adapter", cache_salt=salt)
    first = SimpleNamespace(parent=None, key=whole[:256])
    first.hash_value = compute_node_hash_values(first, 256)
    child = SimpleNamespace(parent=first, key=whole[256:])
    assert first.hash_value + compute_node_hash_values(
        child, 256
    ) == get_storage_hash_str(whole, page_size=256)
