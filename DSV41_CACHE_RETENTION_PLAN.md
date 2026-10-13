# DS native explicit-cache retention: adaptation plan

Status: implementation in progress, not a serving-support claim. Public routing,
workers, dependencies and cache policy have not been changed by this PR.

## Decision

Unmerged upstream work is usable engineering input. Upstream merge status is
provenance, not a gate requiring upstream approval before xray-infra can adapt,
test, merge and deploy its own implementation. Keep the necessary parts, rather
than importing an old private control platform or a whole incompatible branch.

Implement through the actual DS HTTP/UnifiedRadixCache/HiCache/NIXL path. Keep
ordinary unannotated requests unchanged and retain the current explicit-control
rejection at the public semantic owner until native execution is qualified.

TTL expiry means retention protection ends. It does not require deleting ordinary
cache data, forcing a cache miss, releasing an active transfer, or invalidating
existing I/O owners. The earlier proposal to require a miss at the deadline was
not a sound generic retention test.

## Sources actually inspected

- [Dynamo #6213](https://github.com/ai-dynamo/dynamo/pull/6213), merged
  `f1d5c95a4e646e006422e8c7fd22e22a30fa5972`: nvext TTL extraction and a
  fire-and-forget post-stream pin request through the service mesh.
- [SGLang #18941](https://github.com/sgl-project/sglang/pull/18941), merged
  `f7da379b616ef19676b13a484010906a75681457`: classic HiRadix host pin budget,
  monotonic deadlines, refresh-on-hit, split propagation and lazy expiration.
- [SGLang #21884](https://github.com/sgl-project/sglang/pull/21884), merged
  `1081a25983b5ba9ff28b1a6d227f9aec122a7e06`, removes that implementation;
  [Dynamo #7790](https://github.com/ai-dynamo/dynamo/pull/7790), merged
  `c09ac69702ec9cd2772f5a5a837bee3488723d08`, unwires the associated API. The
  stated direction is a different follow-up approach; do not invent an unproven
  security or corruption explanation for the revert.
- [Dynamo #6629](https://github.com/ai-dynamo/dynamo/pull/6629): useful Anthropic
  compatibility/parser cases, but its last-marker-wins collapse is not a complete
  per-breakpoint implementation.
- [SGLang #30796](https://github.com/sgl-project/sglang/pull/30796), closed without
  merge, head `42ffc312d22422f55938e2ffeacea39951fd237b`: **actual diff inspected**.
  Reuse committed-page resolution, page rounding, bounded TTL/page counts,
  request-local deduplication and metadata operations on the existing storage
  worker queue. Its classic HiRadix/Mooncake retain_groups calls and warning-only
  fallback do not directly satisfy Unified/NIXL or explicit client guarantees.
- [Dynamo #11534](https://github.com/ai-dynamo/dynamo/pull/11534), closed without
  merge, head `530a870878b97a2f0f7c56767c5a641df8fb8175`: **actual diff inspected**.
  Reuse separation of retention intent from sampling and visible rejection when
  an adapter cannot forward a required action. Do not import its unreleased
  frontend-crates Cargo patch or service-mesh-only path into the HTTP bridge.
- [SGLang #38891](https://github.com/sgl-project/sglang/pull/38891), merged
  `7fef014d512e3f61e3a3f8b156a726142952f5be`: versioned KvHintsEnvelope transport,
  not retention execution. Its normalization and IPC shape inform this PR.
- [RFC #36224](https://github.com/sgl-project/sglang/issues/36224) distinguishes
  trusted orchestration metadata from a public application API. It is an issue,
  not a PR. No raw public client action payload is to become a remote control API.
- [Current NVIDIA serving docs](https://docs.nvidia.com/dynamo/v1.5.1/digest/agentic-inference)
  explicitly distinguish supported priority hints from a self-hosted TTL-pinning
  API. Historical blog text alone is not current feature evidence.

Read-only upstream receipts were inspected, not used as shadow serving source.
No upstream unmerged state is itself a reason to reject the useful draft logic.
No ready-made full implementation for this exact DS Unified/NIXL path was found
in the inspected sources; this is a bounded search result, not a universal claim.

## Local execution owners

- `mem_cache/registry.py`: default factory selects UnifiedRadixCache and calls
  `init_hicache`, including FULL/SWA and model-specific components. Applying only
  a legacy HiRadix patch would leave the deployed path unimplemented.
- `managers/io_struct.py`, tokenizer, scheduler and session construction own
  metadata propagation. `CacheInitParams.cache_ttl_seconds` alone has no executor.
- `mem_cache/unified_radix_cache.py` and its components own committed prefix,
  namespace, page identity, node split, matching and eviction eligibility.
- `mem_cache/hybrid_cache/hybrid_cache_controller.py` owns queued storage work;
  `mem_cache/hicache_storage.py` defines per-pool publication/restoration results.
- `mem_cache/storage/nixl/hicache_nixl.py` owns native storage adapter behavior.
  NIXL core remains a transfer/lifetime implementation, not a TTL-policy service.
- Dynamo's merged #18 (`838c18094e6ccc89f06e334960cef2fa3ff50ccc`) is newer than
  the DS public #15-equivalent binary. Preserve that shared work, its namespace
  behavior and its unsupported-control honesty; implement on the correct merged
  base rather than overwriting another task or reintroducing the private layer.

## Small, reviewable implementation sequence

### 1. Transport foundation (this PR)

Port the cache-neutral, versioned envelope into this DS branch. Preserve HTTP
native generate / Engine / tokenizer IPC / scheduler Req / ordinary session
construction; preserve per-item ordering through batch and n>1 expansion.
Append the optional IPC field, reject malformed structure rather than silently
swallowing an empty object, and keep unknown action payloads opaque to transport.
Unhinted requests retain None. This is **not TTL support** and is not deployed.
Native gRPC, PD rebootstrap/encode construction and public Chat/Messages lowering
are follow-up paths, not claimed by this bounded port.

### 2. Native retention execution, adapted from the drafts

Resolve selected prefix ranges against the actual committed Unified tree and
existing page keys. Tokenization/template mapping must prove the selected token
prefix belongs to the complete prompt; do not arbitrarily pin the full prompt or
collapse all breakpoints to the last one. Handle page-aligned FULL/SWA/indexer
and compressed/state pools as a restorable group, not just KV pages.

Use bounded native retention state distinct from transfer/lock ownership. A
shorter request must not shorten another accepted deadline. Node split, shared
prefix and hit refresh must preserve the correct covered range. Budgeting must
account for every required component, with explicit partial/refused outcomes.
Do not resurrect indefinite hard pins, a cross-request HMAC authority, a global
retention ledger, signed receipts, or startup dependencies for ordinary requests.

Adapt draft retention operations to the existing Hybrid controller's storage
queue. Metadata work must not block scheduler execution. Apply acceptance and
request deduplication only after a real successful outcome, not when work is
merely queued. Failed or cancelled publication cannot renew a lease or invent
creation tokens. Expiry never releases in-flight NIXL buffers or callback owners.

L3 retention capability must be owned by the configured native storage adapter.
Qualify a capability and its actual eviction behavior rather than assuming
Mooncake group leases exist on POSIX/NIXL. Under the current non-cleaning native
storage configuration, stored objects may outlive TTL normally; that is not a
TTL violation. Any additional persistent per-object metadata must be native,
bounded and atomic, not a replacement shared authority platform. The exact
storage representation/capability is an implementation decision to prove with
native tests, not an already-qualified mechanism.

### 3. Public semantics and accounting

In Dynamo's existing semantic owners, validate root/block/system/tool controls,
default 5m and optional 1h, invalid TTLs, breakpoint count/order and scopes. Lower
validated annotations to an internal action; do not expose arbitrary trusted
orchestration actions through the public API. Preserve cache namespace and worker
affinity from the merged frontend. An explicit guarantee cannot be a silent
warning-only hint or fire-and-forget pin after the response has claimed success.

Use real match/commit/acceptance outcomes for read, creation and duration-specific
statistics. Ordinary cached-token counts or a synthetic accounting frame cannot
stand in for explicit cache creation. Both streaming and unary final usage must
respect the existing response envelope and terminal identity contracts.

### 4. Tests, own-fork PRs and rollout

- CPU red/green: real request normalization and codecs, batch/n>1, no-hint behavior,
  original IPC layout compatibility, version/schema failures and call-site wiring.
- Native executor: range mapping, actual complete multi-pool pages, splits, shared
  prefixes, deadline refresh/expiry, bounded budget, duplicate/retry outcomes.
- Storage: accepted write before retention, partial/error/queue-full/cancel paths,
  and ownership remaining valid through completion at/after TTL expiry.
- Real DS CUDA/NIXL: protected prefixes survive pressure within the accepted TTL;
  protection becomes reclaimable after expiry. Remaining automatic-cache hits
  after expiry are allowed and must not be mistaken for retention still active.
- Public Chat/Messages: stream/unary, tool use/result/final, n>1 and final usage;
  namespace isolation and multi-worker affinity. No raw metadata leakage.

Open corresponding xray-infra PRs as changes are made. Upstream draft provenance
is disclosed, not a reason to wait for upstream. Only after our normal review,
merge and qualified native/public tests deploy sequentially, preserving TP/EP,
DSPARK/SWA/SPF, write_through, NIXL and wait_complete. Do not claim the first
transport PR or a single-worker functional pass is full-pool TTL delivery.

## Evidence boundaries

This PR's CPU tests use the real envelope codec and real production normalization
and IPC class ASTs, with unrelated scheduler/CUDA collaborators kept opaque.
Forwarding-call checks are structural, not GPU execution tests. Eight local tests,
legacy n>1 retirement (three), SPF (five), and FP4 factory tests pass; the base
1aeb IO source fails all nine hinted normalization combinations and the appended
IPC-field assertion. No physical cache/TTL acceptance is claimed.

LSP is not clean: active probes encountered missing msgspec/torch/zmq dependencies,
three inconclusive checks and the scheduler file-size limit. This is disclosed,
not substituted with an empty diagnostic cache. Project Ruff 0.15.1 selected rules,
format checks, CI-registry validation, compile and diff checks pass. Initial broad Ruff invocation included non-project modernization rules;
project-selected rules are run separately. An initial IPC fixture overwrote its
module name while importing typing globals; it was fixed before reporting green.
