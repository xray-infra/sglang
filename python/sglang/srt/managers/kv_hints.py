# SPDX-License-Identifier: Apache-2.0
"""Versioned, cache-neutral request metadata; this module does not execute hints.

Adapted from upstream SGLang PR #38891 (7fef014d512e3f61e3a3f8b156a726142952f5be).
Execution and payload validation belong to the implementing cache component.
"""

from __future__ import annotations

from typing import Any

import msgspec


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


def decode_kv_hints_envelope(value: Any) -> KvHintsEnvelope:
    """Decode structural metadata, not an assertion that an action is supported."""
    if isinstance(value, KvHintsEnvelope):
        return value
    try:
        return msgspec.convert(value, KvHintsEnvelope)
    except (msgspec.ValidationError, TypeError) as exc:
        raise ValueError(f"Malformed kv_hints envelope: {exc}") from exc
