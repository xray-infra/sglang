"""Real owner policy against SDK/HTTP doubles, not a native receipt proof."""

import threading
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from sglang.srt.mem_cache.storage.mooncake_store.replica_policy import (
    TwoOwnerReplicaPolicy,
)

SIZE = 274877906944


def segment(host, alias, port, base, identity):
    return {
        "segment_name": f"{host}:{alias}",
        "segment_id": f"{identity}-1",
        "client_id": f"{identity}-2",
        "te_endpoint": f"{host}:{port}",
        "base_address": hex(base),
        "size_bytes": SIZE,
        "protocol": "tcp",
        "status": "OK",
    }


def memory(endpoint, address, size, complete):
    descriptor = SimpleNamespace(
        transport_endpoint=endpoint, buffer_address=address, size=size
    )
    return SimpleNamespace(
        status=complete,
        is_memory_replica=lambda: True,
        get_memory_descriptor=lambda: SimpleNamespace(buffer_descriptor=descriptor),
    )


@pytest.fixture
def policy():
    # No SDK constructor, client setup, grant, physical IO or registration.
    p = TwoOwnerReplicaPolicy.__new__(TwoOwnerReplicaPolicy)
    p.store = MagicMock()
    p.url = "http://master.invalid/get_segments_detail"
    p.hosts = ("10.90.1.43", "10.90.1.44")
    p.segment_bytes = SIZE
    p.complete = object()
    p.local = threading.local()
    p.config_cls = SimpleNamespace
    p.http = MagicMock()
    segments = [
        segment("10.90.1.43", 13288, 16696, 0x760563000000, 1),
        segment("10.90.1.44", 12301, 15199, 0x7F9F60000000, 2),
    ]
    p.http.get.return_value.json.return_value = {"segments": segments}
    replicas = [
        memory(s["te_endpoint"], int(s["base_address"], 16) + 4096, 8192, p.complete)
        for s in segments
    ]
    p.store.batch_get_replica_desc.return_value = {"key": replicas}
    return p, segments, replicas


def test_segment_alias_is_not_transport_endpoint(policy):
    p, _, _ = policy
    assert p.ready({"key": 8192})


def test_copy_configuration_still_uses_segment_names(policy):
    p, _, _ = policy
    config = p.configuration(p.owners())
    assert config.replica_num == 2
    assert config.preferred_segments == ["10.90.1.43:13288", "10.90.1.44:12301"]


@pytest.mark.parametrize(
    "field", ["segment_id", "client_id", "te_endpoint", "base_address"]
)
def test_owner_epoch_or_mapping_change_is_rejected_by_fence(policy, field):
    p, segments, _ = policy
    replacement = [dict(s) for s in segments]
    replacement[0][field] = {
        "segment_id": "3-1",
        "client_id": "3-2",
        "te_endpoint": "10.90.1.43:16697",
        "base_address": hex(0x760563001000),
    }[field]
    p.http.get.return_value.json.side_effect = [
        {"segments": segments},
        {"segments": replacement},
    ]
    assert not p.ready({"key": 8192})


@pytest.mark.parametrize(
    "fault",
    ["one_owner", "duplicate", "status", "size", "endpoint", "range_low", "range_high"],
)
def test_host_only_or_partial_replica_never_passes(policy, fault):
    p, segments, replicas = policy
    target = replicas[1]
    descriptor = target.get_memory_descriptor().buffer_descriptor
    if fault == "one_owner":
        p.store.batch_get_replica_desc.return_value = {"key": replicas[:1]}
    elif fault == "duplicate":
        p.store.batch_get_replica_desc.return_value = {
            "key": [replicas[0], replicas[0]]
        }
    elif fault == "status":
        target.status = object()
    elif fault == "size":
        descriptor.size += 1
    elif fault == "endpoint":
        descriptor.transport_endpoint = "10.90.1.44:9999"
    elif fault == "range_low":
        descriptor.buffer_address = int(segments[1]["base_address"], 16) - 1
    else:
        descriptor.buffer_address = int(segments[1]["base_address"], 16) + SIZE - 4096
    assert not p.ready({"key": 8192})


@pytest.mark.parametrize("field", ["te_endpoint", "base_address"])
def test_unknown_owner_mapping_does_not_fall_back_to_ip(policy, field):
    p, segments, _ = policy
    del segments[0][field]
    with pytest.raises((ValueError, RuntimeError)):
        p.ready({"key": 8192})


def test_same_host_wrong_native_segment_range_is_rejected(policy):
    p, segments, replicas = policy
    replicas[0].get_memory_descriptor().buffer_descriptor.buffer_address = (
        int(segments[0]["base_address"], 16) + SIZE
    )
    assert not p.ready({"key": 8192})
