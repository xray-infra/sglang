# Comprehensive DAG publication package map

Status: DRAFT_FOR_J_NO_REMOTE_MUTATION
Source SHA256: `862cb6f949400c336069bbfe93c8b7d2ed83c88142aa48bc1580e354a82e48af`

The sole live task authority remains [SG1](https://github.com/xray-infra/sglang/issues/1). This file is a proposed mapping, not a publication or implementation receipt.
Original hard parents and their existing native blockers remain OPEN. Candidate closure does not authorize activation/deployment.
Every conditional capability has its own real checklist anchor, exact selector, owner, consumer AC and unique candidate binding slot; no direction-wide acceptance activates all children.
An accepted capability must bind a real independently closeable candidate child before execution/support. Unselected/unknown checklists are not claimed implementations and do not create unconditional native AND blockers.

Counts: {'fine_nodes': 112, 'packages': 59, 'reuse': 19, 'proposed_new': 40, 'conditional_checklists': 32, 'authority_checklists': 4}. Package cycles: [].

## Independently closeable packages

| Key | Fine nodes | Existing authority / proposed repository | Parent | Close boundary |
|---|---|---|---|---|
| PROFILE | V01 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| FRAMEWORK_CONTRACT | V02,V03,V04 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| INTEGRATION | I01 | https://github.com/xray-infra/sglang/issues/16 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| OWNER_CONTRACT | E01 | https://github.com/xray-infra/sglang/issues/17 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| TRUSTED_GATEWAY | A01 | https://github.com/xray-infra/sglang/issues/5 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| ECONOMIC_INPUT | A02 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| GENERATION_CONTRACT | A03 | https://github.com/xray-infra/sglang/issues/18 | https://github.com/xray-infra/sglang/issues/8 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| STORE_OPERATION | S01 | NEW xray-infra/Mooncake | https://github.com/xray-infra/sglang/issues/19 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| STORE_VARIANT | S02 | https://github.com/xray-infra/Mooncake/issues/10 | https://github.com/xray-infra/Mooncake/issues/3 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| ENGINE_OPERATION | E02 | https://github.com/xray-infra/sglang/issues/19 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| RESTORE_ADMISSION | E03,E04 | https://github.com/xray-infra/sglang/issues/20 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| ROUTER_BOUNDARY | Q01 | NEW xray-infra/dynamo | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| TRUSTED_RECEIPT | Q02,E05 | https://github.com/xray-infra/sglang/issues/21 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| IMMUTABLE_IDENTITY | S05 | https://github.com/xray-infra/sglang/issues/22 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| TENANT_MODE | S10 | NEW xray-infra/Mooncake | https://github.com/xray-infra/sglang/issues/22 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| GENERATION_DELIVERY | E06 | https://github.com/xray-infra/sglang/issues/23 | https://github.com/xray-infra/sglang/issues/8 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| CANONICAL_DIRECTORY | Q03,Q04,Q05 | https://github.com/xray-infra/dynamo/issues/2 | https://github.com/xray-infra/dynamo/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| WORKER_ADMISSION_BOOKING | Q06 | https://github.com/xray-infra/dynamo/issues/3 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| RESTORE_PREDICTION | Q07 | https://github.com/xray-infra/dynamo/issues/4 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| MIXED_FAIRNESS | Q08 | https://github.com/xray-infra/dynamo/issues/5 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| L2_PHYSICAL_OWNER | S07 | https://github.com/xray-infra/Mooncake/issues/11 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| IO_PROGRESS | S08 | https://github.com/xray-infra/sglang/issues/24 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| L3_ABI | L01 | https://github.com/xray-infra/Mooncake/issues/12 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| L3_CANDIDATE | L02,L03,L04 | https://github.com/xray-infra/Mooncake/issues/13 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| ACTUAL_SERVICE | E07 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/21 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| ENVIRONMENT_LOCK | V05 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| VLLM_COMPARISON | VV1,V06,BV,VV2 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| BATCH_FREEZE | B00 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/25 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| ACCEPTANCE_A | BA | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/25 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| PHYSICAL_PERMISSION | BS | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/25 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| ACCEPTANCE_B | BB | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/25 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| ACCEPTANCE_C | BC | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/25 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| ACCEPTANCE_AGENT | BE | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/25 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| ACCEPTANCE_EXTENSIONS | BX | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/25 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| RELEASE_A | RA | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/26 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| RELEASE_FULL | RB | https://github.com/xray-infra/sglang/issues/26 | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| AGENT_DECISION | AG01,R02 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/27 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| SHARING_DECISION | AG04,R04 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/28 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_R01 | R01 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_R03 | R03 | NEW xray-infra/Mooncake | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_R05 | R05 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_R06 | R06 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_R07 | R07 | NEW xray-infra/dynamo | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_R08 | R08 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_R09 | R09 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_R10 | R10 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_R11 | R11 | NEW xray-infra/Mooncake | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_R12 | R12 | NEW xray-infra/Mooncake | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_RX01 | RX01 | NEW xray-infra/dynamo | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_RX02 | RX02 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_RX03 | RX03 | NEW xray-infra/dynamo | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_RX04 | RX04 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_RX05 | RX05 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_RX06 | RX06 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_RX07 | RX07 | NEW xray-infra/Mooncake | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_RX08 | RX08 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_RX09 | RX09 | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| DECISION_S09 | S09 | NEW xray-infra/Mooncake | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |
| RESEARCH_SCOPE | F01,F02,F03,F04,RD | NEW xray-infra/sglang | https://github.com/xray-infra/sglang/issues/1 | Full listed decision/candidate/batch receipt; no partial-parent substitution |

## Exact node anchors and selected-scope candidates

| Fine node | Mapping | Authority and anchor | Binding / completion rule |
|---|---|---|---|
| V01 | NEW_PACKAGE | proposed:PROFILE#coverage-v01 | Full independently closeable PROFILE |
| V02 | NEW_PACKAGE | proposed:FRAMEWORK_CONTRACT#coverage-v02 | Full independently closeable FRAMEWORK_CONTRACT |
| V03 | NEW_PACKAGE | proposed:FRAMEWORK_CONTRACT#coverage-v03 | Full independently closeable FRAMEWORK_CONTRACT |
| V04 | NEW_PACKAGE | proposed:FRAMEWORK_CONTRACT#coverage-v04 | Full independently closeable FRAMEWORK_CONTRACT |
| I01 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/16#coverage-i01 | Full independently closeable INTEGRATION |
| E01 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/17#coverage-e01 | Full independently closeable OWNER_CONTRACT |
| A01 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/5#coverage-a01 | Full independently closeable TRUSTED_GATEWAY |
| A02 | NEW_PACKAGE | proposed:ECONOMIC_INPUT#coverage-a02 | Full independently closeable ECONOMIC_INPUT |
| A03 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/18#coverage-a03 | Full independently closeable GENERATION_CONTRACT |
| S01 | NEW_PACKAGE | proposed:STORE_OPERATION#coverage-s01 | Full independently closeable STORE_OPERATION |
| S02 | EXISTING_ISSUE | https://github.com/xray-infra/Mooncake/issues/10#coverage-s02 | Full independently closeable STORE_VARIANT |
| E02 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/19#coverage-e02 | Full independently closeable ENGINE_OPERATION |
| E03 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/20#coverage-e03 | Full independently closeable RESTORE_ADMISSION |
| E04 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/20#coverage-e04 | Full independently closeable RESTORE_ADMISSION |
| Q01 | NEW_PACKAGE | proposed:ROUTER_BOUNDARY#coverage-q01 | Full independently closeable ROUTER_BOUNDARY |
| Q02 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/21#coverage-q02 | Full independently closeable TRUSTED_RECEIPT |
| E05 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/21#coverage-e05 | Full independently closeable TRUSTED_RECEIPT |
| S05 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/22#coverage-s05 | Full independently closeable IMMUTABLE_IDENTITY |
| S10 | NEW_PACKAGE | proposed:TENANT_MODE#coverage-s10 | Full independently closeable TENANT_MODE |
| E06 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/23#coverage-e06 | Full independently closeable GENERATION_DELIVERY |
| Q03 | EXISTING_ISSUE | https://github.com/xray-infra/dynamo/issues/2#coverage-q03 | Full independently closeable CANONICAL_DIRECTORY |
| Q04 | EXISTING_ISSUE | https://github.com/xray-infra/dynamo/issues/2#coverage-q04 | Full independently closeable CANONICAL_DIRECTORY |
| Q05 | EXISTING_ISSUE | https://github.com/xray-infra/dynamo/issues/2#coverage-q05 | Full independently closeable CANONICAL_DIRECTORY |
| Q06 | EXISTING_ISSUE | https://github.com/xray-infra/dynamo/issues/3#coverage-q06 | Full independently closeable WORKER_ADMISSION_BOOKING |
| Q07 | EXISTING_ISSUE | https://github.com/xray-infra/dynamo/issues/4#coverage-q07 | Full independently closeable RESTORE_PREDICTION |
| Q08 | EXISTING_ISSUE | https://github.com/xray-infra/dynamo/issues/5#coverage-q08 | Full independently closeable MIXED_FAIRNESS |
| S07 | EXISTING_ISSUE | https://github.com/xray-infra/Mooncake/issues/11#coverage-s07 | Full independently closeable L2_PHYSICAL_OWNER |
| S08 | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/24#coverage-s08 | Full independently closeable IO_PROGRESS |
| L01 | EXISTING_ISSUE | https://github.com/xray-infra/Mooncake/issues/12#coverage-l01 | Full independently closeable L3_ABI |
| L02 | EXISTING_ISSUE | https://github.com/xray-infra/Mooncake/issues/13#coverage-l02 | Full independently closeable L3_CANDIDATE |
| L03 | EXISTING_ISSUE | https://github.com/xray-infra/Mooncake/issues/13#coverage-l03 | Full independently closeable L3_CANDIDATE |
| L04 | EXISTING_ISSUE | https://github.com/xray-infra/Mooncake/issues/13#coverage-l04 | Full independently closeable L3_CANDIDATE |
| E07 | NEW_PACKAGE | proposed:ACTUAL_SERVICE#coverage-e07 | Full independently closeable ACTUAL_SERVICE |
| V05 | NEW_PACKAGE | proposed:ENVIRONMENT_LOCK#coverage-v05 | Full independently closeable ENVIRONMENT_LOCK |
| VV1 | NEW_PACKAGE | proposed:VLLM_COMPARISON#coverage-vv1 | Full independently closeable VLLM_COMPARISON |
| V06 | NEW_PACKAGE | proposed:VLLM_COMPARISON#coverage-v06 | Full independently closeable VLLM_COMPARISON |
| BV | NEW_PACKAGE | proposed:VLLM_COMPARISON#coverage-bv | Full independently closeable VLLM_COMPARISON |
| VV2 | NEW_PACKAGE | proposed:VLLM_COMPARISON#coverage-vv2 | Full independently closeable VLLM_COMPARISON |
| B00 | NEW_PACKAGE | proposed:BATCH_FREEZE#coverage-b00 | Full independently closeable BATCH_FREEZE |
| BA | NEW_PACKAGE | proposed:ACCEPTANCE_A#coverage-ba | Full independently closeable ACCEPTANCE_A |
| BS | NEW_PACKAGE | proposed:PHYSICAL_PERMISSION#coverage-bs | Full independently closeable PHYSICAL_PERMISSION |
| BB | NEW_PACKAGE | proposed:ACCEPTANCE_B#coverage-bb | Full independently closeable ACCEPTANCE_B |
| BC | NEW_PACKAGE | proposed:ACCEPTANCE_C#coverage-bc | Full independently closeable ACCEPTANCE_C |
| BE | NEW_PACKAGE | proposed:ACCEPTANCE_AGENT#coverage-be | Full independently closeable ACCEPTANCE_AGENT |
| BX | NEW_PACKAGE | proposed:ACCEPTANCE_EXTENSIONS#coverage-bx | Full independently closeable ACCEPTANCE_EXTENSIONS |
| RA | NEW_PACKAGE | proposed:RELEASE_A#coverage-ra | Full independently closeable RELEASE_A |
| RB | EXISTING_ISSUE | https://github.com/xray-infra/sglang/issues/26#coverage-rb | Full independently closeable RELEASE_FULL |
| AG01 | NEW_PACKAGE | proposed:AGENT_DECISION#coverage-ag01 | Full independently closeable AGENT_DECISION |
| R02 | NEW_PACKAGE | proposed:AGENT_DECISION#coverage-r02 | Full independently closeable AGENT_DECISION |
| AG04 | NEW_PACKAGE | proposed:SHARING_DECISION#coverage-ag04 | Full independently closeable SHARING_DECISION |
| R04 | NEW_PACKAGE | proposed:SHARING_DECISION#coverage-r04 | Full independently closeable SHARING_DECISION |
| R01 | NEW_PACKAGE | proposed:DECISION_R01#coverage-r01 | Full independently closeable DECISION_R01 |
| R03 | NEW_PACKAGE | proposed:DECISION_R03#coverage-r03 | Full independently closeable DECISION_R03 |
| R05 | NEW_PACKAGE | proposed:DECISION_R05#coverage-r05 | Full independently closeable DECISION_R05 |
| R06 | NEW_PACKAGE | proposed:DECISION_R06#coverage-r06 | Full independently closeable DECISION_R06 |
| R07 | NEW_PACKAGE | proposed:DECISION_R07#coverage-r07 | Full independently closeable DECISION_R07 |
| R08 | NEW_PACKAGE | proposed:DECISION_R08#coverage-r08 | Full independently closeable DECISION_R08 |
| R09 | NEW_PACKAGE | proposed:DECISION_R09#coverage-r09 | Full independently closeable DECISION_R09 |
| R10 | NEW_PACKAGE | proposed:DECISION_R10#coverage-r10 | Full independently closeable DECISION_R10 |
| R11 | NEW_PACKAGE | proposed:DECISION_R11#coverage-r11 | Full independently closeable DECISION_R11 |
| R12 | NEW_PACKAGE | proposed:DECISION_R12#coverage-r12 | Full independently closeable DECISION_R12 |
| RX01 | NEW_PACKAGE | proposed:DECISION_RX01#coverage-rx01 | Full independently closeable DECISION_RX01 |
| RX02 | NEW_PACKAGE | proposed:DECISION_RX02#coverage-rx02 | Full independently closeable DECISION_RX02 |
| RX03 | NEW_PACKAGE | proposed:DECISION_RX03#coverage-rx03 | Full independently closeable DECISION_RX03 |
| RX04 | NEW_PACKAGE | proposed:DECISION_RX04#coverage-rx04 | Full independently closeable DECISION_RX04 |
| RX05 | NEW_PACKAGE | proposed:DECISION_RX05#coverage-rx05 | Full independently closeable DECISION_RX05 |
| RX06 | NEW_PACKAGE | proposed:DECISION_RX06#coverage-rx06 | Full independently closeable DECISION_RX06 |
| RX07 | NEW_PACKAGE | proposed:DECISION_RX07#coverage-rx07 | Full independently closeable DECISION_RX07 |
| RX08 | NEW_PACKAGE | proposed:DECISION_RX08#coverage-rx08 | Full independently closeable DECISION_RX08 |
| RX09 | NEW_PACKAGE | proposed:DECISION_RX09#coverage-rx09 | Full independently closeable DECISION_RX09 |
| S09 | NEW_PACKAGE | proposed:DECISION_S09#coverage-s09 | Full independently closeable DECISION_S09 |
| F01 | NEW_PACKAGE | proposed:RESEARCH_SCOPE#coverage-f01 | Full independently closeable RESEARCH_SCOPE |
| F02 | NEW_PACKAGE | proposed:RESEARCH_SCOPE#coverage-f02 | Full independently closeable RESEARCH_SCOPE |
| F03 | NEW_PACKAGE | proposed:RESEARCH_SCOPE#coverage-f03 | Full independently closeable RESEARCH_SCOPE |
| F04 | NEW_PACKAGE | proposed:RESEARCH_SCOPE#coverage-f04 | Full independently closeable RESEARCH_SCOPE |
| RD | NEW_PACKAGE | proposed:RESEARCH_SCOPE#coverage-rd | Full independently closeable RESEARCH_SCOPE |
| S06 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/22#coverage-s06 | Unique SELECTED_S06 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| AG02 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/27#coverage-ag02 | Unique SELECTED_AG02 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| AG03 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/27#coverage-ag03 | Unique SELECTED_AG03 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| AG05 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/28#coverage-ag05 | Unique SELECTED_AG05 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP01 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp01 | Unique SELECTED_CP01 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP02 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp02 | Unique SELECTED_CP02 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP03 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp03 | Unique SELECTED_CP03 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP04 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp04 | Unique SELECTED_CP04 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP05 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp05 | Unique SELECTED_CP05 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP06 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp06 | Unique SELECTED_CP06 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP07 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp07 | Unique SELECTED_CP07 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP08 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp08 | Unique SELECTED_CP08 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP09 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp09 | Unique SELECTED_CP09 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP10 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp10 | Unique SELECTED_CP10 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP11 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp11 | Unique SELECTED_CP11 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP12 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp12 | Unique SELECTED_CP12 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP13 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp13 | Unique SELECTED_CP13 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP14 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp14 | Unique SELECTED_CP14 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP15 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp15 | Unique SELECTED_CP15 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP16 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp16 | Unique SELECTED_CP16 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP17 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp17 | Unique SELECTED_CP17 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP18 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp18 | Unique SELECTED_CP18 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP19 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp19 | Unique SELECTED_CP19 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP20 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp20 | Unique SELECTED_CP20 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP21 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp21 | Unique SELECTED_CP21 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP22 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp22 | Unique SELECTED_CP22 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP23 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp23 | Unique SELECTED_CP23 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP24 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp24 | Unique SELECTED_CP24 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP25 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp25 | Unique SELECTED_CP25 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP26 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp26 | Unique SELECTED_CP26 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP27 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp27 | Unique SELECTED_CP27 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| CP28 | REAL_CONDITIONAL_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-cp28 | Unique SELECTED_CP28 child required when exact selector accepted; currently NOT_IMPLEMENTED |
| S00 | REAL_AUTHORITY_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-s00 | Explicit audit/whole-parent receipt; no implementation credit |
| SJ | REAL_AUTHORITY_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-sj | Explicit audit/whole-parent receipt; no implementation credit |
| SP | REAL_AUTHORITY_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-sp | Explicit audit/whole-parent receipt; no implementation credit |
| PH | REAL_AUTHORITY_CHECKLIST | https://github.com/xray-infra/sglang/issues/1#coverage-ph | Explicit audit/whole-parent receipt; no implementation credit |

## Native development package dependencies

These are candidate/decision closure edges only. Intra-package order remains the complete fine DAG. Conditional/checklist receipts stay explicit and must not be converted into parent-closure assumptions.

- PROFILE → FRAMEWORK_CONTRACT: V01→V02, V01→V03, V01→V04
- FRAMEWORK_CONTRACT → INTEGRATION: V03→I01
- INTEGRATION → OWNER_CONTRACT: I01→E01
- OWNER_CONTRACT → GENERATION_CONTRACT: E01→A03
- PROFILE → GENERATION_CONTRACT: V01→A03
- OWNER_CONTRACT → STORE_OPERATION: E01→S01
- STORE_OPERATION → STORE_VARIANT: S01→S02
- STORE_OPERATION → ENGINE_OPERATION: S01→E02
- OWNER_CONTRACT → RESTORE_ADMISSION: E01→E03
- ENGINE_OPERATION → RESTORE_ADMISSION: E02→E03
- FRAMEWORK_CONTRACT → ROUTER_BOUNDARY: V03→Q01
- TRUSTED_GATEWAY → TRUSTED_RECEIPT: A01→Q02
- OWNER_CONTRACT → TRUSTED_RECEIPT: E01→Q02
- ROUTER_BOUNDARY → TRUSTED_RECEIPT: Q01→Q02
- RESTORE_ADMISSION → TRUSTED_RECEIPT: E04→Q02, E04→E05
- ENGINE_OPERATION → IMMUTABLE_IDENTITY: E02→S05
- GENERATION_CONTRACT → IMMUTABLE_IDENTITY: A03→S05
- GENERATION_CONTRACT → GENERATION_DELIVERY: A03→E06
- ENGINE_OPERATION → GENERATION_DELIVERY: E02→E06
- RESTORE_ADMISSION → GENERATION_DELIVERY: E04→E06
- TRUSTED_RECEIPT → GENERATION_DELIVERY: E05→E06
- IMMUTABLE_IDENTITY → GENERATION_DELIVERY: S05→E06
- TRUSTED_RECEIPT → CANONICAL_DIRECTORY: Q02→Q03
- IMMUTABLE_IDENTITY → CANONICAL_DIRECTORY: S05→Q03
- GENERATION_DELIVERY → CANONICAL_DIRECTORY: E06→Q03
- CANONICAL_DIRECTORY → WORKER_ADMISSION_BOOKING: Q04→Q06, Q05→Q06
- TRUSTED_RECEIPT → WORKER_ADMISSION_BOOKING: E05→Q06
- GENERATION_DELIVERY → WORKER_ADMISSION_BOOKING: E06→Q06
- WORKER_ADMISSION_BOOKING → RESTORE_PREDICTION: Q06→Q07
- TRUSTED_GATEWAY → MIXED_FAIRNESS: A01→Q08
- TRUSTED_RECEIPT → MIXED_FAIRNESS: E05→Q08
- WORKER_ADMISSION_BOOKING → MIXED_FAIRNESS: Q06→Q08
- RESTORE_PREDICTION → MIXED_FAIRNESS: Q07→Q08
- ACTUAL_SERVICE → MIXED_FAIRNESS: E07→Q08
- ENGINE_OPERATION → L2_PHYSICAL_OWNER: E02→S07
- IMMUTABLE_IDENTITY → L2_PHYSICAL_OWNER: S05→S07
- RESTORE_ADMISSION → IO_PROGRESS: E03→S08, E04→S08
- L2_PHYSICAL_OWNER → IO_PROGRESS: S07→S08
- L3_ABI → L3_CANDIDATE: L01→L02
- ENGINE_OPERATION → L3_CANDIDATE: E02→L02
- IMMUTABLE_IDENTITY → L3_CANDIDATE: S05→L02
- L2_PHYSICAL_OWNER → L3_CANDIDATE: S07→L02
- IO_PROGRESS → L3_CANDIDATE: S08→L02
- MIXED_FAIRNESS → AGENT_DECISION: Q08→AG01
- IO_PROGRESS → AGENT_DECISION: S08→AG01
- RESTORE_ADMISSION → SHARING_DECISION: E04→AG04
- TRUSTED_RECEIPT → SHARING_DECISION: E05→AG04
- IO_PROGRESS → SHARING_DECISION: S08→AG04
- INTEGRATION → BATCH_FREEZE: I01→B00
- PROFILE → BATCH_FREEZE: V01→B00
- OWNER_CONTRACT → BATCH_FREEZE: E01→B00
- BATCH_FREEZE → ACCEPTANCE_A: B00→BA
- ENGINE_OPERATION → ACCEPTANCE_A: E02→BA
- RESTORE_ADMISSION → ACCEPTANCE_A: E04→BA
- STORE_VARIANT → ACCEPTANCE_A: S02→BA
- ENVIRONMENT_LOCK → ACCEPTANCE_A: V05→BA
- FRAMEWORK_CONTRACT → ACCEPTANCE_A: V04→BA
- STORE_VARIANT → PHYSICAL_PERMISSION: S02→BS
- GENERATION_DELIVERY → PHYSICAL_PERMISSION: E06→BS
- CANONICAL_DIRECTORY → PHYSICAL_PERMISSION: Q04→BS, Q05→BS
- ACCEPTANCE_A → PHYSICAL_PERMISSION: BA→BS
- ACCEPTANCE_A → ACCEPTANCE_B: BA→BB
- BATCH_FREEZE → ACCEPTANCE_B: B00→BB
- MIXED_FAIRNESS → ACCEPTANCE_B: Q08→BB
- IO_PROGRESS → ACCEPTANCE_B: S08→BB
- PHYSICAL_PERMISSION → ACCEPTANCE_B: BS→BB
- ACTUAL_SERVICE → ACCEPTANCE_B: E07→BB
- ACCEPTANCE_B → ACCEPTANCE_C: BB→BC
- L3_CANDIDATE → ACCEPTANCE_C: L04→BC
- BATCH_FREEZE → ACCEPTANCE_C: B00→BC
- BATCH_FREEZE → ACCEPTANCE_AGENT: B00→BE
- AGENT_DECISION → ACCEPTANCE_AGENT: AG01→BE
- SHARING_DECISION → ACCEPTANCE_AGENT: AG04→BE
- FRAMEWORK_CONTRACT → VLLM_COMPARISON: V02→BV, V02→VV1, V04→V06
- BATCH_FREEZE → VLLM_COMPARISON: B00→BV
- ACCEPTANCE_A → VLLM_COMPARISON: BA→BV
- ACCEPTANCE_A → RELEASE_A: BA→RA
- ACCEPTANCE_C → RELEASE_FULL: BC→RB
- PHYSICAL_PERMISSION → RELEASE_FULL: BS→RB
- ACCEPTANCE_AGENT → RELEASE_FULL: BE→RB
- FRAMEWORK_CONTRACT → RELEASE_FULL: V02→RB
- RESEARCH_SCOPE → RELEASE_FULL: RD→RB
- ACCEPTANCE_B → RELEASE_FULL: BB→RB
- VLLM_COMPARISON → RELEASE_FULL: VV2→RB
- ACCEPTANCE_EXTENSIONS → RELEASE_FULL: BX→RB
- DECISION_S09 → RELEASE_FULL: S09→RB
- RESTORE_PREDICTION → DECISION_R01: Q07→R01
- ECONOMIC_INPUT → DECISION_R01: A02→R01
- L2_PHYSICAL_OWNER → DECISION_R03: S07→R03
- ECONOMIC_INPUT → DECISION_R03: A02→R03
- IMMUTABLE_IDENTITY → DECISION_R05: S05→R05
- GENERATION_CONTRACT → DECISION_R05: A03→R05
- GENERATION_DELIVERY → DECISION_R06: E06→R06
- CANONICAL_DIRECTORY → DECISION_R06: Q03→R06
- CANONICAL_DIRECTORY → DECISION_R07: Q05→R07
- PROFILE → DECISION_R08: V01→R08
- IMMUTABLE_IDENTITY → DECISION_R08: S05→R08
- PROFILE → DECISION_R09: V01→R09
- IMMUTABLE_IDENTITY → DECISION_R09: S05→R09
- PROFILE → DECISION_R10: V01→R10
- FRAMEWORK_CONTRACT → DECISION_R10: V02→R10
- IMMUTABLE_IDENTITY → DECISION_R10: S05→R10
- L3_ABI → DECISION_R11: L01→R11
- IO_PROGRESS → DECISION_R11: S08→R11
- L3_ABI → DECISION_R12: L01→R12
- DECISION_R08 → DECISION_R12: R08→R12
- DECISION_R01 → RESEARCH_SCOPE: R01→F01, R01→RD
- AGENT_DECISION → RESEARCH_SCOPE: R02→F01, AG01→F01, R02→RD
- ACCEPTANCE_B → RESEARCH_SCOPE: BB→F01
- SHARING_DECISION → RESEARCH_SCOPE: R04→F02, R04→RD
- DECISION_R03 → RESEARCH_SCOPE: R03→F03, R03→RD
- DECISION_R08 → RESEARCH_SCOPE: R08→F03, R08→RD
- DECISION_R11 → RESEARCH_SCOPE: R11→F03, R11→RD
- DECISION_R05 → RESEARCH_SCOPE: R05→F04, R05→RD
- DECISION_R06 → RESEARCH_SCOPE: R06→F04, R06→RD
- DECISION_R07 → RESEARCH_SCOPE: R07→F04, R07→RD
- DECISION_R10 → RESEARCH_SCOPE: R10→F04, R10→RD
- MIXED_FAIRNESS → DECISION_RX01: Q08→RX01
- SHARING_DECISION → DECISION_RX01: AG04→RX01
- MIXED_FAIRNESS → DECISION_RX02: Q08→RX02
- RESTORE_PREDICTION → DECISION_RX02: Q07→RX02
- RESTORE_PREDICTION → DECISION_RX03: Q07→RX03
- L2_PHYSICAL_OWNER → DECISION_RX03: S07→RX03
- FRAMEWORK_CONTRACT → DECISION_RX04: V02→RX04
- RESTORE_PREDICTION → DECISION_RX04: Q07→RX04
- DECISION_R10 → DECISION_RX04: R10→RX04
- DECISION_R09 → RESEARCH_SCOPE: R09→RD
- DECISION_R12 → RESEARCH_SCOPE: R12→RD
- DECISION_RX01 → RESEARCH_SCOPE: RX01→RD
- DECISION_RX02 → RESEARCH_SCOPE: RX02→RD
- DECISION_RX03 → RESEARCH_SCOPE: RX03→RD
- DECISION_RX04 → RESEARCH_SCOPE: RX04→RD
- VLLM_COMPARISON → RESEARCH_SCOPE: VV2→RD
- DECISION_RX05 → RESEARCH_SCOPE: RX05→RD
- DECISION_RX06 → RESEARCH_SCOPE: RX06→RD
- DECISION_RX07 → RESEARCH_SCOPE: RX07→RD
- DECISION_RX08 → RESEARCH_SCOPE: RX08→RD
- DECISION_RX09 → RESEARCH_SCOPE: RX09→RD
- INTEGRATION → ENVIRONMENT_LOCK: I01→V05
- FRAMEWORK_CONTRACT → ENVIRONMENT_LOCK: V04→V05
- PROFILE → ENVIRONMENT_LOCK: V01→V05
- ENVIRONMENT_LOCK → VLLM_COMPARISON: V05→VV1
- OWNER_CONTRACT → VLLM_COMPARISON: E01→VV1
- ENGINE_OPERATION → VLLM_COMPARISON: E02→VV1
- INTEGRATION → VLLM_COMPARISON: I01→V06
- ECONOMIC_INPUT → VLLM_COMPARISON: A02→VV2
- BATCH_FREEZE → ACCEPTANCE_EXTENSIONS: B00→BX
- RESEARCH_SCOPE → ACCEPTANCE_EXTENSIONS: RD→BX
- GENERATION_CONTRACT → DECISION_RX05: A03→RX05
- TRUSTED_RECEIPT → DECISION_RX05: E05→RX05
- IO_PROGRESS → DECISION_RX05: S08→RX05
- TRUSTED_GATEWAY → DECISION_RX06: A01→RX06
- AGENT_DECISION → DECISION_RX06: AG01→RX06
- DECISION_R07 → DECISION_RX06: R07→RX06
- DECISION_R06 → DECISION_RX07: R06→RX07
- L2_PHYSICAL_OWNER → DECISION_RX07: S07→RX07
- CANONICAL_DIRECTORY → DECISION_RX07: Q05→RX07
- OWNER_CONTRACT → ACTUAL_SERVICE: E01→E07
- TRUSTED_RECEIPT → ACTUAL_SERVICE: E05→E07
- DECISION_R08 → DECISION_RX08: R08→RX08
- ECONOMIC_INPUT → DECISION_RX08: A02→RX08
- PROFILE → DECISION_RX09: V01→RX09
- DECISION_R10 → DECISION_RX09: R10→RX09
- DECISION_R11 → DECISION_RX09: R11→RX09
- L2_PHYSICAL_OWNER → DECISION_S09: S07→S09
- DECISION_RX07 → DECISION_S09: RX07→S09
- TRUSTED_GATEWAY → TENANT_MODE: A01→S10
- OWNER_CONTRACT → TENANT_MODE: E01→S10

## Preserved whole-feature hard gates

- MC3 ← MC1/MC2; Dynamo1 ← SG7/SG8/SG4. Existing publication facts and old whole-parent AC are unchanged.
- PH maps the actual full roll-up to those original authorities; BS permits only its stated scoped experiment, not parent closure.
- SG25 retains full A/B/C/selected-extension acceptance. Independent batch children permit A progress without waiting for all future B/C work.
- SG27/28 retain full selected-session/single-flight hardware value AC. New decision child closure does not close them.

## Entry and resources

- Source-only PROFILE/FRAMEWORK_CONTRACT decisions feed existing SG16 integration; no second vLLM runtime or production business fixture is a first SG vertical prerequisite.
- SG16 must produce actual candidate/provenance/joint entry build before SG17→Store/Engine lifecycle→SG20 restore-admission→A.
- Gateway/SLO/economics inputs, L3 ABI, current absent GPU and selected advanced capabilities each block only their stated axes; no invented tenant, device ABI or performance result.
- Native package graph and fine receipt graph are distinct. Full fine DAG/requirement ledger are frozen via R1 documentation-only draft, exact blob/raw references, with no second status platform.

## J review focus

1. Verify package folding acyclic and preserved hard authorities; audit all contract versus candidate versus hardware receipt boundaries.
2. Verify REAL_CONDITIONAL_CHECKLIST selection/binding policy is an acceptable remote backlog representation; if not, promote only specific independently closeable selected candidates, without changing fine coverage.
3. Verify mixed-control actual service, cost-aware victim/retract, tenant mode, replica/fault domains and distinct shared-page/compute producer/cohort/attention AC are not swallowed by umbrella titles.
