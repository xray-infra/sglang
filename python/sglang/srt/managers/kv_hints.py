# SPDX-License-Identifier: Apache-2.0
"""Versioned, cache-neutral request metadata; this module does not execute hints.

Adapted from upstream SGLang PR #38891 (7fef014d512e3f61e3a3f8b156a726142952f5be).
Execution and payload validation belong to the implementing cache component.
"""

from __future__ import annotations

from typing import Any, Optional

import msgspec

KV_HINT_PROTOCOL_VERSION = "0.1"
CACHE_RETENTION_ACTION_TYPE = "kv.retain_prefix"
CACHE_RETENTION_ACTION_VERSION = "1.0"
MAX_CACHE_RETENTION_DURATION_SECONDS = 86_400
MAX_CACHE_RETENTION_ACTIONS = 8_192


class KvHintAction(msgspec.Struct, frozen=True, kw_only=True):
    action_id: str
    action_type: str
    action_version: str
    payload: dict[str, Any] = {}

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        from sglang.srt.utils.msgspec_utils import (
            msgspec_struct_pydantic_core_schema,
        )

        return msgspec_struct_pydantic_core_schema(cls, handler)


class KvHintsEnvelope(msgspec.Struct, frozen=True, kw_only=True):
    protocol_version: str
    message_id: str
    actions: list[KvHintAction] = []

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        from sglang.srt.utils.msgspec_utils import (
            msgspec_struct_pydantic_core_schema,
        )

        return msgspec_struct_pydantic_core_schema(cls, handler)


class CacheRetentionIntent(msgspec.Struct, frozen=True, kw_only=True):
    """A validated request for retention, not evidence that it was applied."""

    action_id: str
    prefix_token_count: int
    duration_seconds: int


def _required_positive_int(payload: dict[str, Any], field: str) -> int:
    value = payload.get(field)
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field} must be a positive integer")
    return value


def parse_cache_retention_intents(
    envelope: Optional[KvHintsEnvelope], *, prompt_token_count: int
) -> tuple[CacheRetentionIntent, ...]:
    """Validate supported retain-prefix actions without executing them.

    Unknown action types remain opaque transport metadata. A recognized action
    must use the exact supported envelope/action versions and worker-token
    boundary contract; otherwise the request must fail instead of silently
    degrading explicit cache control into ordinary best-effort caching.
    """
    if envelope is None:
        return ()

    retention_actions = [
        action
        for action in envelope.actions
        if action.action_type == CACHE_RETENTION_ACTION_TYPE
    ]
    if not retention_actions:
        return ()
    if envelope.protocol_version != KV_HINT_PROTOCOL_VERSION:
        raise ValueError(
            "kv.retain_prefix requires kv_hints protocol_version "
            f'"{KV_HINT_PROTOCOL_VERSION}"'
        )
    if len(retention_actions) > MAX_CACHE_RETENTION_ACTIONS:
        raise ValueError(
            "kv.retain_prefix action count exceeds the worker limit of "
            f"{MAX_CACHE_RETENTION_ACTIONS}"
        )

    intents = []
    action_ids = set()
    previous_prefix = 0
    for action in retention_actions:
        if not action.action_id or action.action_id in action_ids:
            raise ValueError("kv.retain_prefix action_id must be non-empty and unique")
        action_ids.add(action.action_id)
        if action.action_version != CACHE_RETENTION_ACTION_VERSION:
            raise ValueError(
                "kv.retain_prefix requires action_version "
                f'"{CACHE_RETENTION_ACTION_VERSION}"'
            )

        prefix_token_count = _required_positive_int(
            action.payload, "prefix_token_count"
        )
        duration_seconds = _required_positive_int(
            action.payload, "duration_seconds"
        )
        if prefix_token_count > prompt_token_count:
            raise ValueError(
                "kv.retain_prefix prefix_token_count exceeds the worker prompt "
                f"length ({prefix_token_count} > {prompt_token_count})"
            )
        if prefix_token_count <= previous_prefix:
            raise ValueError(
                "kv.retain_prefix prefix_token_count values must be strictly increasing"
            )
        if duration_seconds > MAX_CACHE_RETENTION_DURATION_SECONDS:
            raise ValueError(
                "kv.retain_prefix duration_seconds exceeds the worker limit of "
                f"{MAX_CACHE_RETENTION_DURATION_SECONDS}"
            )
        previous_prefix = prefix_token_count
        intents.append(
            CacheRetentionIntent(
                action_id=action.action_id,
                prefix_token_count=prefix_token_count,
                duration_seconds=duration_seconds,
            )
        )
    return tuple(intents)


def decode_kv_hints_envelope(value: Any) -> KvHintsEnvelope:
    """Decode structural metadata, not an assertion that an action is supported."""
    if isinstance(value, KvHintsEnvelope):
        return value
    try:
        return msgspec.convert(value, KvHintsEnvelope)
    except (msgspec.ValidationError, TypeError) as exc:
        raise ValueError(f"Malformed kv_hints envelope: {exc}") from exc
