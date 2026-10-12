# GLM-5.3 wire regression and source-coherence gates

Tracking: [xray-infra/sglang#68](https://github.com/xray-infra/sglang/issues/68).
Scope: `zai-org/GLM-5.3`, **not Flash**. No production service/configuration
changes, dependency upgrades or other-model deployment changes are included.

## Finding and source boundary

The 2026-10-12 read-only audit found:

- Public Dynamo native HTTP nonstreaming tool requests returned 503, while nearby
  ordinary-text controls returned 200.
- Native worker58 nonstreaming tool requests returned 500 with
  `FunctionCallParser.__init__() got an unexpected keyword argument 'tool_choice'`.
  Its captured serving methods pass that keyword and call `owns_tool_format`,
  while the parser interface is incompatible. Required/named streaming shares
  this call site. **Native auto-streaming succeeded**; not all streaming is broken.
- The reviewed source base is
  `cache-foundation-2026-10-01@94602c9c2b7cbdb8efd5c52802dac6a1c180089e`.
  Its real serving/parser pair handles the GLM native format coherently.
- The live worker image prefix is `15f14455ebca`, with embedded Git HEAD
  `07c8f7294daa12087e969c89a11f773d36b9d42d` and numerous tracked overlays.
  **An image label or embedded HEAD does not identify the running source.**
  The attempted full parser capture was not usable; the runtime exception and
  serving stack are evidence, not a claimed complete worker-source snapshot.
- Applicable Dynamo native code is `qwen38-native-port` at
  `13c50272d53f1d22e9ae91df4e07d301f038815d`, PR
  [xray-infra/dynamo#11](https://github.com/xray-infra/dynamo/pull/11), not Dynamo main.
  The frontend binary/image/lockfile correspondence is not yet completely proven.

This change does **not** add ignored kwargs, parser shims or fake tool results.
It fixes a genuine native usage-reporting bug and adds executable tool/source
checks. The public frontend's remaining streaming error path is not declared fixed.

## Native cache-read contract

When cache reporting is enabled:

| Raw native count | Wire `prompt_tokens_details.cached_tokens` |
| --- | --- |
| Known 0 | `0` |
| Known positive integer | Exact native count |
| Missing, null or invalid negative | Absent (unknown), not fabricated `0` |
| Any contributing prompt unknown | Total remains unknown, not a partial sum |

Prompt/cache counts are deduplicated across choices. Empty inputs do not imply a
measured zero. Streaming collectors retain null/missing as unknown; continuous
usage and final usage use the same distinction. Multimodal counts still serialize,
but they no longer fabricate a cache zero merely by creating a details object.
Reporting disabled does not expose a cache-read count.

These are shared OpenAI usage/protocol helpers, not a model-name special case.
Known-positive accounting, total token arithmetic, choice deduplication and
multimodal counts have regression controls. No inference or runtime configuration
for another model is changed. This is **not** full cross-model GPU qualification.

A native read counter is not a verified billing receipt: Radix hits do not prove
paid cache writes, TTL guarantees, write-token accounting or invoice correctness.
Dynamo may intentionally withhold accounting when its verified envelope is unknown.
That downstream projection is a separate gate; missing public fields must not be
filled with invented zeros.

## CPU regressions

```bash
PYTHONPATH=python python -m pytest -p no:cacheprovider \
  test/registered/unit/openai/test_glm53_wire_usage.py \
  test/registered/unit/openai/test_glm53_tool_parser_contract.py \
  test/registered/unit/openai/test_glm53_source_coherence.py \
  test/registered/unit/function_call/test_glm47_schema_types.py -q
```

Use the release image's actual dependencies. The tool tests execute real serving
call-site methods with the real `glm47` parser and protocol classes, not an HTTP
stub. Only the tokenizer-manager dependency is doubled to avoid GPU startup.
They assert auto/required/named names, valid JSON arguments, IDs/indexes, final
nonstreaming `tool_calls` finish reason, and streaming chunks of 1/7/full length.
They do not exercise a complete GPU generation or public frontend.

For an operator-selected **trusted local** serving capture, negative control:

```bash
GLM53_REPLAY_SERVING_SOURCE=/path/to/deployed-serving-chat.py.txt \
  PYTHONPATH=python python -m pytest \
  test/registered/unit/openai/test_glm53_tool_parser_contract.py -q
```

This executes only the two captured call-site bodies against the real repository
parser/protocol dependencies. It is not a full deployed-parser replay; never run
it with an untrusted capture or against a live process.

Observed isolated CPU evidence, 2026-10-12:

- Baseline: 4 cache assertion failures, 18 passes, 676 passing subtests.
- Captured-call-site replay: **9 exact `tool_choice` TypeErrors**, corresponding to
  all 3 nonstreaming choices and the 6 required/named streaming chunk cases;
  native auto-streaming controls still pass. Cache baseline failures are separate.
- Candidate, including source-gate tests: **28 passes / 693 passing subtests**.
  Dependency warnings (20) remain; they are not rewritten as errors or hidden
  success signals. Runtime ~19 seconds in the isolated image sandbox.
- Sandbox: `--read-only --network none --cpus 2 --memory 4g --pids-limit 256`,
  writable temporary cache only, candidate/capture mounted read-only, no GPU or
  model/production volume mounts. No live service was changed or restarted.

## Source gate: Git objects, not image self-attestation

Generate an approved manifest from an externally reviewed release commit:

```bash
python scripts/ci/check_python_source_coherence.py generate \
  --repo . --revision <reviewed-release-commit> --output /tmp/approved-source.json
```

The generator hashes **committed/archived Python source under `python/sglang`**,
not the working tree. Dirty overlays cannot bless themselves into the manifest.
Use the manifest from the authoritative checkout/CI artifact, not an untrusted
copy regenerated inside the candidate image. The manifest itself is not signed;
its approval, transport and artifact integrity remain release responsibilities.

Inside the finished candidate image/canary, with its normal runtime interpreter
and environment (after all mounts/install/entrypoint modifications), resolve the
actual import directory without starting a model:

```bash
python -c 'import importlib.util; print(importlib.util.find_spec("sglang").submodule_search_locations[0])'
python /path/to/check_python_source_coherence.py verify \
  --manifest /approved/approved-source.json --source-root <actual-import-directory>
```

Any modified/missing/unexpected Python module, source symlink/outside-root path,
or hidden symlink directory fails the gate. Regular bytecode caches are ignored.
Empty/malformed manifests fail closed. Tests mutate every carried fixture module
and prove that generation uses committed objects despite a dirty serving overlay.

This is a **Python-source gate**, not binary/wheel/CUDA-kernel attestation or proof
of live health. Dependency versions/digests, compiled extensions, launch flags,
mounts and image/binary provenance require separate review. Recheck the running
canary after startup; no mutable source overlays are permitted in the release.
The script is provided for release integration; this PR does not secretly change
the production launcher or enable an automatic rollout.

**Do not replace the running package with this older baseline checkout.** The
GLM NVFP4/DCP/pre-KV/prefill patches must first be inventoried, reviewed and
integrated into the release commit. Only then generate its manifest and construct
a replacement image. Other workers have not been per-file verified. Shared nodes
and their non-GLM services are outside this rollout's ownership.

## Static-check evidence and limitations

New tests, source-gate script and usage helper: Ruff/format checks and configured
Pyright return zero findings. For the four existing OpenAI modules, using the same
configuration and dependency typing sources as the Git baseline:

- Pyright: baseline **218 errors / 1 warning**, candidate **218 / 1**, **0 new**
  diagnostic fingerprints (file/rule/message, counted with multiplicity).
- Ruff: baseline **726 findings**, candidate **718**, **0 new** fingerprints.

Those whole-file baseline problems are **not fixed by this PR** and whole-file
lint/type checks are **not green**. Active LSP also retains source-root/dependency
environment failures; an empty/suppressed cache is not clean evidence. Known import
and Pydantic-version misresolutions were classified with configured-check and CPU
proof, not inline ignores. No bulk modernizations, casts, rule disabling or
unrelated fixes are used to manufacture a green result. Require the repository's
supported CI environment and review its remaining findings before release.

Raw audit/check artifacts are retained locally in
`/private/tmp/glm53-current-audit-20261012/` (`cpu-red.txt`,
`cpu-tool-replay-red.txt`, `cpu-green-full.txt`,
`pyright-baseline-comparison.json`, `ruff-baseline-comparison.json`). These paths
are evidence references, **not remotely accessible artifacts promised to reviewers**;
the PR/issue includes the reproducible commands and result summary.

## Production acceptance remains blocked

No full public matrix or rollout is claimed. For **each** OpenAI/Anthropic wire
protocol, run the following low-concurrency canary matrix through the actual public
native frontend, followed by native-worker controls:

| Request | Nonstreaming | Streaming |
| --- | --- | --- |
| Ordinary | Expected text + exact final usage | Expected text, no error, correct final usage |
| Tool | auto / required / named | auto / required / named; arbitrary SSE chunk boundaries |

For every tool response, assert exactly the declared tool name, nonempty tool-call
ID, valid JSON arguments matching schema and task, and a tool completion stop
reason. Assemble streamed tool arguments by index/ID; do not accept partial JSON,
SSE error events, a bare HTTP 200 or a trailing `[DONE]` as success. Do not execute
the weather tool during these probes.

For every cell verify known-zero, repeated-prefix positive-hit and unknown
accounting behavior, including continuous/final usage, choice deduplication and
absence of internal accounting keys on the public wire. Confirm that every actual
routed GLM worker is qualified, not just worker58.

Then separately validate verified cache-read/cache-write receipts, TTL classes,
expiry/restart behavior, billable totals and signed-envelope failure/unknown paths.
Do not promote native read counts to paid write counts. Preserve diagnostics and
rollback/canary boundaries. Source checks, GPU patch qualification, public-matrix
qualification and explicit production-change authorization are all required before
rollout; none is replaced by the CPU result above.

## Verified single-worker wire acceptance (2026-10-12)

The bounded four-file worker backport was deployed to node58. Native OpenAI
12/12, same-image single-worker frontend OpenAI 12/12 and Anthropic 12/12
passed: ordinary and auto/required-or-any/named tools, JSON/SSE, valid tool
IDs/names/arguments and completion reasons, no stream error, and final usage.
Both frontend protocols reported real cold-cache zero and repeated-prefix
4608-token hits. No external weather tool was executed. These 36 cases prove
the single-worker interface matrix, not public full-pool acceptance.

Only the validated wire/backport/test changes belong to this PR's merge scope.
The storage-namespace candidate and its CPU tests are retained on the separate
`fix/glm53-retention-storage-hash-68` branch/PR: CPU passed, actual GPU probe
failed. Cache writes, TTL/expiry/restart, L3 receipts and billing remain open
under issue68. Merging wire changes does not authorize rollout or claim those
cache gates passed. No further automatic live rollback is authorized.

## L3 namespace follow-up (2026-10-12; not accepted for rollout)

The captured worker's DCP retention and shared-read callers used `get_hash_str`,
while actual HiCache writes use `get_storage_hash_str`, including the
`extra_key`/`cache_salt` namespace seed. A correlated fresh 5m request showed
identical DCP namespaces but different reserved/storage page roots on all eight
ranks, `retained_owners=0`, absent ACKs and master commit error `-703`.

The minimal live-overlay delta is
`scripts/patches/glm53-native-retention-storage-hash-worker.patch`; its adjacent
hash manifest pins the original and candidate bytes of both overlay modules.
Those modules are absent from this repository baseline: this is a bounded
worker backport, not a wholesale import or approval of its existing overlay.

`scripts/patches/test_glm53_live_retention_storage_hash.py` exercises the real
native hash, DCP prepare and shared-read key builder against the trusted worker
package. Admission voting/storage reservation are doubles; it is not a real
storage/receipt or TP8 integration gate. Run with that captured package on
`PYTHONPATH`, in a Linux CPU-only container, using
`python -m pytest -p no:cacheprovider --disable-warnings /path/to/test_glm53_live_retention_storage_hash.py -q`.
The native C++ extension needs an executable container-private build tmpfs;
read-only root, no network/GPU, and CPU/memory/PID limits remain enabled.
Original source: 4 failed / 4 passed; candidate: 8 passed (20 dependency warnings).
Identical package paths/configuration: Pyright 31 errors to 29, zero new
fingerprints, **not whole-file green**. A detached two-file baseline comparison
had different import topology and was rejected rather than used for approval.

The real node58 candidate probe subsequently returned HTTP500 after 101.459s;
worker ACK reads reported TCP EOF and `TRANSFER_FAIL(-800)`. The transport
root cause is not established. At the user's interruption the remote rollback
had already restored the two original overlay files and restarted the worker;
readback showed health200. No further automatic rollback is authorized.
Backend/producer diagnostic logs have been removed. The four prior interface
fixes remain; no other worker, Flash service or public route was changed.
Cache-write, TTL/expiry/restart, receipts/billing and public-fleet gates remain
unpassed. This candidate and its CPU evidence must not be described as deployed
or accepted.

## Protected singleton scratch read follow-up

Actual current native binding inspection proves ordinary `batch_get_into`
uses READ0x80 for the allocated-memory/TCP branch, incompatible with the
receiver's protected READ0xc0 plus proof requirement. SDK `get_into(key, ptr,
size)` directly reaches `GetMemoryReplicaHeld` on the host-memory branch and
obtains its real grant through native master callbacks. Missing Python proof
arguments are not evidence that the SDK cannot obtain a grant.

The new bounded DCP-only patch
`scripts/patches/glm53-native-dcp-protected-read-worker.patch` switches `_blob`
to that existing scalar entry, checks capability before registering scratch,
validates the span and exact integer byte count, and retains `io_lock` through
copy-out. Native failure/partial/unknown stays `None`; there is no ordinary
batch fallback, forged grant or guessed Python Finish/End call. Native owns
its Claim/Finish/Abort lifecycle. General multi-key/nested reads are not changed.

The adjacent test runs real DCP methods and CPU Torch allocations with a strict
SDK signature double, not real transport/grant/receipt IO. Original source:
19 failed / 4 passed; candidate: 23 passed. Together with real native-hash cases:
31 passed, 20 dependency warnings. Same source path/package/configuration
Pyright 18 errors to 15, zero new; baseline findings remain, not full-file green.

The separately authorized 30s observation attempt failed during bpftrace live
attach (address/interior-offset support unavailable). No valid event records
were collected: not verified zero traffic or a successful transport gate.
Owned probe processes/definitions and scratch directories were removed;
service identity/lifetime unchanged. This candidate still needs actual node58
storage/receipt/TTL acceptance; merging source does not authorize fleet rollout.
