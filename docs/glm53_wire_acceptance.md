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
