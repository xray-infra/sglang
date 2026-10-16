"""Bookkeeping for bootstrap rendezvous before decode has reserved KV.

The transfer backend still owns the destination-pointer handshake and abort
draining. This table only joins a completed optimistic prefill with decode's
control endpoints. It performs no I/O, including while holding its lock.

One request reaches a prefill rank from every decode rank that maps onto it
(decode attention TP above the prefill's: one receiver per decode TP rank), so
a room holds up to ``expected`` endpoints. The first registration fixes that
count; it is the decode side's ``required_dst_info_num``.
"""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field

Endpoint = tuple[str, int]
# (endpoint, failed) pairs to send; empty when there is nothing to send.
BootstrapNotification = list[tuple[Endpoint, bool]]


@dataclass
class BootstrapRoom:
    owner: object | None = None
    endpoints: list[Endpoint] = field(default_factory=list)
    expected_endpoints: int | None = None
    ready: bool = False
    ready_notified: set[Endpoint] = field(default_factory=set)
    failed: bool = False
    expires_at: float = 0.0


class DeferredBootstrap:
    def __init__(self, timeout: float):
        self.timeout = timeout
        self.rooms: dict[int, BootstrapRoom] = {}
        self.lock = threading.Lock()
        self._next_cleanup = 0.0

    def _room(self, room: int) -> BootstrapRoom:
        now = time.monotonic()
        if now >= self._next_cleanup:
            # Active senders own their lifetime. Unmatched endpoints and closed
            # rooms expire, including cancellation before the sender exists.
            self.rooms = {
                key: state
                for key, state in self.rooms.items()
                if state.owner is not None or state.expires_at > now
            }
            self._next_cleanup = now + min(1.0, self.timeout)
        return self.rooms.setdefault(room, BootstrapRoom(expires_at=now + self.timeout))

    @staticmethod
    def _notification(
        state: BootstrapRoom, endpoints: list[Endpoint] | None = None
    ) -> BootstrapNotification:
        out: BootstrapNotification = []
        for endpoint in state.endpoints if endpoints is None else endpoints:
            if state.failed:
                out.append((endpoint, True))
            elif state.ready and endpoint not in state.ready_notified:
                # One readiness message per endpoint and transfer. Decode must
                # consume it before publishing destinations, so none can trail
                # Success and accidentally admit the next transfer using this room.
                state.ready_notified.add(endpoint)
                out.append((endpoint, False))
        return out

    def open(self, room: int, owner: object) -> BootstrapRoom | None:
        with self.lock:
            state = self._room(room)
            if state.owner is not None:
                return None
            state.owner = owner
            return state

    def register(
        self, room: int, endpoint: Endpoint, expected: int = 1
    ) -> BootstrapNotification:
        with self.lock:
            state = self._room(room)
            if endpoint in state.endpoints:
                return self._notification(state, [endpoint])
            if state.expected_endpoints is None:
                state.expected_endpoints = max(1, expected)
            if (
                expected != state.expected_endpoints
                or len(state.endpoints) >= state.expected_endpoints
            ):
                # A room identifies one request, not a reusable allocation slot.
                # Reject a receiver beyond that request's decode ranks without
                # replacing the registered ones.
                return [(endpoint, True)]
            state.endpoints.append(endpoint)
            return self._notification(state, [endpoint])

    def complete(self, room: int, owner: object) -> BootstrapNotification:
        with self.lock:
            state = self.rooms.get(room)
            if state is None or state.owner is not owner or state.failed:
                return []
            state.ready = True
            return self._notification(state)

    def fail(self, room: int) -> BootstrapNotification:
        with self.lock:
            state = self._room(room)
            if state.failed:
                return []
            state.failed = True
            return self._notification(state)

    def close(
        self, room: int, owner: object, *, success: bool = False
    ) -> BootstrapNotification:
        with self.lock:
            state = self.rooms.get(room)
            if state is None or state.owner is not owner:
                return []
            if success and not state.failed:
                # The caller clears transport state before sending Success.
                # Only then can decode reuse this room for recomputation.
                del self.rooms[room]
                return [(endpoint, False) for endpoint in state.endpoints]
            state.owner = None
            already_failed = state.failed
            state.failed = True
            state.expires_at = time.monotonic() + self.timeout
            # Retain a bounded tombstone: a late endpoint must not wait forever
            # or attach to a second request using the same bootstrap room.
            return [] if already_failed else self._notification(state)
