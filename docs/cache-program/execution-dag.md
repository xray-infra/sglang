# 全面来源覆盖与固定执行 DAG

REVIEWED_PLANNING_SNAPSHOT；2026-10-03。J已PASS可用来源/已知需求覆盖、fine DAG与native package规划；执行实时状态唯一以canonical Map为准。112是独立产物与关闭条件的逻辑包，不要求111张新票，不以节点计数证明完整。

唯一状态权威：[canonical Map](https://github.com/xray-infra/sglang/issues/1)。JSON定义候选前置/条件guard，coverage-matrix定义逐source概念/原分类/disposition/nativeblock refs；G发布后补exactSHAblob。

## 读取与执行边界

144本地canonical都有actual named-reader FULL回执，0pending/0unowned，source-inventory/read-coverage-ledger逐路径/范围/reader留证。8Lark1404unique block IDs全semanticread、88源先概念/180source refs；GitHub37issues/9draftPR/40comments实际读完，108native关系核对。6domain final+GitHub/Lark报告由assembler全文回读。不是所有引用论文/源码或原始聊天均全文。

微信正文MISSING（验证码归档）、4API空turn/2compaction Chatraw不可用、5Lark附件PDFmetadata-only、P01–21primaryselected、GPU两raw点数组尾部未重读。所有缺口有sourcegate，取得原文/primary/code后追加source→concept→disposition；不得用另一论文或旧CPU PASS替全文。

公共API普通/cold/short/longprompt/longdecode/newtenant进展、trusted权益、物理安全是主线。Agent为首试点，生命周期hint可选；给定网络前提不建立拓扑优化分支，实际传输正确性/争用仍计量。首FULL/non-PD固定域逐层成为working产品，再共享L2公平/authority，再一套实际L3。每探索固定签accepted/measured-no-change/deferred/rejected/unknown；accepted绑定完整consumer实现与验收，unknown不得silent skip，deferred/rejected有理由与reopen trigger。

九PR全部draft OPEN/unmerged，没有jointcandidate。Store19PASS/2SKIP、TE same8 RED→GREEN、SG metadata/diagnostic/HRRN窄CPU、R7slots/control、R8三real socket、standaloneSM120 CUDA各自limited事实复用。SG3/4/12/14与MC8 closed历史保留supporting，不授完整功能/device/positivecredit/SLO/economics/deploy。

实现包关闭必须真实代码或有据native足够、producer→owner→consumer集成、fixedSHA/config、必要CPU与故障receipt。完整feature消费者freeze后集中约定batch，failure/相关变化才affectedclosure复测。工具为配套；schema/图表/目录存在不能替功能。CPUcandidate关闭只解开发blocker；BS物理启用receipt先于BB，PH全parent AC在batch后。Parent仅containment，不当child开始前置；MC3←MC1/MC2、Dyn1←SG7/SG8保留nativehardblockers。

## 总览

~~~mermaid
flowchart TD
 V01["真实profile"] --> I01["joint candidate"] --> E01["唯一owner合同"]
 E01 --> S01["Store/TE lifetime"] --> E02["真实IO"] --> E03["host grant"] --> E04["HBM/layer消费"] --> BA["A完整固定域"]
 A01["trusted入口"] --> Q02["context"] --> E05["worker兑现"] --> E07["actual-result累计"]
 E04 --> E06["acquire/revoke/drain"] --> Q03["authority桥"] --> Q04["N/K"] --> Q05["G/repair"] --> Q06["票/feedback"] --> Q07["成本"] --> Q08["原queue公平"]
 E06 --> BS["physical启用gate"]
 Q05 --> BS
 BA --> BS --> BB["B sharedL2混流"]
 Q08 --> BB
 S08["必要writeback/IO份额"] --> BB
 L01["actualL3ABI"] --> L02["单adapter"] --> L03["双粒度IO"] --> L04["finite prefetch"] --> BC["C actualL3"]
 BB --> BC --> PH["原hardparent全部AC"]
 BB --> PH
 R01["12方向/4融合/额外decision"] --> RD["fixeddisposition"] --> BX["accepted扩展完整freeze"]
 CP01["条件consumer包"] -. accepted .-> BX
 VV1["独立vLLMadapter"] --> BV["同资源比较"] --> VV2["最终框架receipt"]
 PH --> RB["所选完整scope发布"]
 BX --> RB
 VV2 --> RB
 BA --> RA["仅A有限出口"]
~~~

## 节点导航

| ID | 执行包 / 性质 | owner | deps | 原锚 | scope / batch |
|---|---|---|---|---|---|
| [S00](#s00) | 全文覆盖与不可访问来源复核 / audit_gate | coverage/J | 独立根输入 | G package/checklist | audit / explicit_decision_or_audit_receipt |
| [V01](#v01) | 固定首路径运行组合与真实主模型 / decision | A/H/产品 | 独立根输入 | T00 | input / explicit_decision_or_audit_receipt |
| [A01](#a01) | 可信入口与租户/共享域身份 / input_gate | gateway人类owner/E | 独立根输入 | T03 | input / explicit_decision_or_audit_receipt |
| [A02](#a02) | 业务trace/SLO/成本输入一次冻结 / input_gate | 产品/H/成本owner | 独立根输入 | T03 | input / explicit_decision_or_audit_receipt |
| [L01](#l01) | 真实专用L3设备合同 / input_gate | 设备人类owner/D/B | 独立根输入 | T16 | input / explicit_decision_or_audit_receipt |
| [SJ](#sj) | J整源覆盖/图/边界独立审查 / audit_review_gate | J | [S00](#s00) | G package/checklist | audit / explicit_decision_or_audit_receipt |
| [V02](#v02) | vLLM独立接口和维护范围对照 / decision | F/A | [V01](#v01) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [SP](#sp) | G唯一Map映射与I知识同步 / audit_publication | G/I | [SJ](#sj) | Map | audit / explicit_decision_or_audit_receipt |
| [V03](#v03) | 锁首vertical主引擎与Router初始接入范围 / decision | A/B/E/F | [V01](#v01)、[V02](#v02) | G package/checklist | input / explicit_decision_or_audit_receipt |
| [V04](#v04) | 固定release能力/拒绝组合矩阵 / decision | A/B/F | [V01](#v01)、[V02](#v02) | G package/checklist | core / formal_receipt |
| [I01](#i01) | 整合既有九draft为真实统一候选 / integration | 集成owner/H | [V03](#v03) | T00 | core / BA/BB/BC_by_selected_scope |
| [Q01](#q01) | Routerhost原生队列/booking与职责确认 / decision | E | [V03](#v03) | G package/checklist | core / BA/BB/BC_by_selected_scope |
| [E01](#e01) | 恢复owner/consumer与退账合同 / decision | B/D/C | [I01](#i01) | T01 | core / BA/BB/BC_by_selected_scope |
| [V05](#v05) | 首 SGLang 环境/transitive artifact 与实际库锁 / integration | 打包owner/H/A | [I01](#i01)、[V04](#v04)、[V01](#v01) | G package/checklist | core / formal_receipt |
| [A03](#a03) | 模型语义generation与全mutation初合同 / decision | B/E/D/部署owner | [E01](#e01)、[V01](#v01) | T02 | core / BA/BB/BC_by_selected_scope |
| [B00](#b00) | 一次批前freeze与实际观测consumer / acceptance_prepare | H/组件/J | [I01](#i01)、[V01](#v01)、[E01](#e01) | T18 | support / T18 |
| [S01](#s01) | Store/TE操作owner与逻辑/物理终态贯通 / implementation | D | [E01](#e01) | T04 | core / BA/BB/BC_by_selected_scope |
| [S10](#s10) | Store tenantmode 与强 per-API 容量隔离一次需求决定 / decision | 产品/gateway/D/B | [A01](#a01)、[E01](#e01) | T03/HITL5+T08/SR06 tenant-mode decision child | core_decision_conditional_mode / decision_registry; selected S06 in BB |
| [E02](#e02) | SG pooled读/写worker异常与rank终态 / implementation | B/D | [S01](#s01) | T04 | core / BA/BB/BC_by_selected_scope |
| [S02](#s02) | TE完成发布与variant拒绝接入 / implementation | D/集成owner | [S01](#s01) | T05 | core / BA/BB/BC_by_selected_scope |
| [E03](#e03) | host恢复grant与active占用硬门控 / implementation | B/C | [E01](#e01)、[E02](#e02) | T06 | core / BA/BB/BC_by_selected_scope |
| [S05](#s05) | immutable对象key与producer旧binding / implementation | B/D | [E02](#e02)、[A03](#a03) | T08 | core / BA/BB/BC_by_selected_scope |
| [VV1](#vv1) | vLLM等价Store适配/事件实际消费者 / implementation | F/vLLM adapterowner | [V05](#v05)、[V02](#v02)、[E01](#e01)、[E02](#e02) | G package/checklist | core / formal_receipt |
| [E04](#e04) | HBM准入与逐层消费/释放闭环 / implementation | B/C | [E03](#e03) | T06 | core / BA/BB/BC_by_selected_scope |
| [R05](#r05) | 公共prefix预计算与版本发布取舍 / research_decision | B/D/产品 | [S05](#s05)、[A03](#a03) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [R08](#r08) | 无损codec/低bitKV/MLA独立表示取舍 / research_decision | B/表示owner/H | [V01](#v01)、[S05](#s05) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [R09](#r09) | 非prefixRAG与上下文变体取舍 / research_decision | 表示/应用owner/H | [V01](#v01)、[S05](#s05) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [R10](#r10) | 跨TP/layout与hybrid合法状态恢复 / research_decision | B/F/表示owner/H | [V01](#v01)、[V02](#v02)、[S05](#s05) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [S07](#s07) | L2 placement/replica/lease/pin实际容量回收 / implementation | D/B | [E02](#e02)、[S05](#s05) | T14 | core / BA/BB/BC_by_selected_scope |
| [V06](#v06) | 实际补丁维护面积与upgrade门槛 / decision | A/B/E/F/D | [I01](#i01)、[V04](#v04)、[VV1](#vv1) | G package/checklist | research / formal_receipt |
| [BA](#ba) | A fixed-domain无信用vertical批 / acceptance | H/J | [B00](#b00)、[E02](#e02)、[E04](#e04)、[S02](#s02)、[V05](#v05)、[V04](#v04) | T18.A | hardware / T18.A |
| [Q02](#q02) | 可信context逐turn传播到真实Req / implementation | E/B | [A01](#a01)、[E01](#e01)、[Q01](#q01)、[E04](#e04) | T07 | core / BA/BB/BC_by_selected_scope |
| [CP07](#cp07) | 表示对象data/scale/codec ABI实际consumer / conditional_implementation | A/B/D | [R08](#r08)、[V04](#v04)、[S05](#s05) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [R12](#r12) | 设备attention与active-decode下层流式读 / research_decision | 表示/设备owner/H | [L01](#l01)、[R08](#r08) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [RX08](#rx08) | pruning/compaction 独立质量与表示决策 / research_decision | representation/kernel | [R08](#r08)、[A02](#a02) | G package/checklist | exploratory / decision_registry |
| [R03](#r03) | 价值收录/淘汰/副本取舍 / research_decision | D/B/H | [S07](#s07)、[A02](#a02) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [S08](#s08) | demand/writeback/prefetch三类有界IO份额 / implementation | B/D/E | [E03](#e03)、[E04](#e04)、[S07](#s07) | T15 | core / BA/BB/BC_by_selected_scope |
| [BV](#bv) | vLLM固定模型/trace/预算对照批 / acceptance | F/H/J | [V02](#v02)、[B00](#b00)、[VV1](#vv1)、[BA](#ba) | G package/checklist | hardware / explicit_decision_or_audit_receipt |
| [CP14](#cp14) | host-cache/buffer/direct/nativeoffload独立路径 / conditional_implementation | B/F | [V04](#v04)、[BA](#ba)、[R08](#r08) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [RA](#ra) | 有限A发布出口 / release | 发布owner/H/J/G | [BA](#ba) | T19.A | release / explicit_decision_or_audit_receipt |
| [E05](#e05) | worker typed兑现/拒绝与实际服务结算 / implementation | B/C | [Q02](#q02)、[E04](#e04) | T07 | core / BA/BB/BC_by_selected_scope |
| [S06](#s06) | 所选强 per-API Store 隔离的 per-batch tenant consumer / conditional_implementation | D/B/E | [A01](#a01)、[Q02](#q02)、[S05](#s05)、[S10](#s10) | T08 | conditional / BA/BB/BC_by_selected_scope |
| [CP09](#cp09) | 原生量化/MLA被选表示端到端 / conditional_implementation | B/D/model | [CP07](#cp07)、[E04](#e04)、[R08](#r08) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [CP10](#cp10) | 一个layout/TP转换及有限物化副本 / conditional_implementation | B/F/D | [R10](#r10)、[CP07](#cp07)、[S05](#s05) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [CP11](#cp11) | hybrid合法stop集合/完整checkpoint消费者 / conditional_implementation | B/F/D | [R10](#r10)、[CP07](#cp07)、[E04](#e04) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [CP18](#cp18) | 真实冷attentionpartition/merge消费者 / conditional_implementation | device/B/model | [R12](#r12)、[CP07](#cp07)、[E04](#e04)、[L01](#l01) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [CP26](#cp26) | 所选 KV pruning 与 ragged compaction 消费 / conditional_implementation | representation/kernel | [RX08](#rx08)、[CP07](#cp07)、[E04](#e04) | G package/checklist | conditional / BX |
| [CP08](#cp08) | 冷层一个codec encode→decode→kernel闭环 / conditional_implementation | D/B/device | [CP07](#cp07)、[S08](#s08)、[R08](#r08) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [L02](#l02) | 一个真实L3 adapter与发布/迁移 / implementation | D/B | [L01](#l01)、[E02](#e02)、[S05](#s05)、[S07](#s07)、[S08](#s08) | T17 | core / BA/BB/BC_by_selected_scope |
| [R11](#r11) | L3 CPU/DPU/GPU发起与KVIO取舍 / research_decision | D/设备owner/B/H | [L01](#l01)、[S08](#s08) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [VV2](#vv2) | 同合同机器证据后的最终框架选择 / decision | 框架/产品owner/H | [BV](#bv)、[V06](#v06)、[A02](#a02) | G package/checklist | research / formal_receipt |
| [AG04](#ag04) | 真实重复IO与single-flight取舍 / decision | B/H | [E04](#e04)、[E05](#e05)、[S08](#s08) | X02 | research / explicit_decision_or_audit_receipt |
| [E06](#e06) | 唯一worker acquire/revoke authority / implementation | B/E/D | [A03](#a03)、[E02](#e02)、[E04](#e04)、[E05](#e05)、[S05](#s05) | T09 | core / BA/BB/BC_by_selected_scope |
| [E07](#e07) | 实际结果累计服务账与去重消费 / implementation | B | [E01](#e01)、[E05](#e05) | T07/SG21 EC11 independent child | core / BB |
| [RX05](#rx05) | RL policy/训练推理共用资源合同取舍 / research_decision | 训练/平台/B/E | [A03](#a03)、[E05](#e05)、[S08](#s08) | G package/checklist | research / decision_scope_receipt |
| [CP15](#cp15) | RAG非prefixfusion/contextvariants实际consumer / conditional_implementation | retrieval/B/D/model | [R09](#r09)、[CP07](#cp07)、[E04](#e04)、[S08](#s08) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [L03](#l03) | L3 deadline队列与双粒度IO / implementation | D/B/设备owner | [L02](#l02) | T17 | core / BA/BB/BC_by_selected_scope |
| [F03](#f03) | 融合3紧凑表示×价值收录×L3IO / fusion_decision | B/D/设备/H | [R03](#r03)、[R08](#r08)、[R11](#r11) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [RX09](#rx09) | 模型原生跨层 KV/persistent replay 范围裁决 / research_decision | model/representation/kernel | [V01](#v01)、[R10](#r10)、[R11](#r11) | G package/checklist | exploratory / decision_registry |
| [R04](#r04) | prefixDAG/分组/sharedpage/Cascade取舍 / research_decision | B/E/H | [AG04](#ag04) | X02 | research / explicit_decision_or_audit_receipt |
| [AG05](#ag05) | 所选 bounded restore 单 leader/waiter consumer / conditional_implementation | B/SG actual restore IO/ref owner (reuse SG28); Router E demand summary only | [AG04](#ag04)、[E06](#e06) | X02 | conditional / BE |
| [CP05](#cp05) | 公共prefix版本manifest与实际预计算发布 / conditional_implementation | 产品/B/D | [R05](#r05)、[E06](#e06)、[S08](#s08) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [Q03](#q03) | canonical身份登记与generation通知桥 / implementation | E/B | [Q02](#q02)、[S05](#s05)、[E06](#e06) | T10 | core / BA/BB/BC_by_selected_scope |
| [CP24](#cp24) | 所选RL/训练资源跨step执行接入 / conditional_implementation | 训练/平台/B | [RX05](#rx05)、[E06](#e06)、[E05](#e05)、[S08](#s08) | G package/checklist | conditional / BX |
| [CP16](#cp16) | L3逐层deadline及时恢复/format融合 / conditional_implementation | B/D/devicekernel | [R11](#r11)、[L03](#l03)、[E04](#e04) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [L04](#l04) | L3分层预取/有限保留与write admission / implementation | B/D | [L03](#l03) | T17 | core / BA/BB/BC_by_selected_scope |
| [CP27](#cp27) | 所选模型原生跨层 persistent replay / conditional_implementation | model/representation/kernel | [RX09](#rx09)、[CP11](#cp11)、[L02](#l02) | G package/checklist | conditional / BX |
| [CP01](#cp01) | 祖先DAG/共享页可消费合同 / conditional_implementation | B/D | [R04](#r04)、[S05](#s05)、[E04](#e04) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [F02](#f02) | 融合2DAG×分组×sharedpage×Cascade / fusion_decision | B/E/H | [R04](#r04) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [Q04](#q04) | namespace与完整object query/event parity / implementation | E/B/D | [Q03](#q03) | T10 | core / BA/BB/BC_by_selected_scope |
| [R06](#r06) | 弹性扩缩容与会话连续性取舍 / research_decision | B/D/E | [E06](#e06)、[Q03](#q03) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [Q05](#q05) | group验证与bounded目录恢复 / implementation | E/D | [Q04](#q04) | T10 | core / BA/BB/BC_by_selected_scope |
| [CP06](#cp06) | 弹性退役/新实例有限预热 / conditional_implementation | 部署/B/D/E | [R06](#r06)、[E06](#e06)、[Q03](#q03)、[S07](#s07) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [BS](#bs) | MC3/SG8/Dynamo1物理activation必需轴 / hard_gate | H/J/原owner | [S02](#s02)、[E06](#e06)、[Q04](#q04)、[Q05](#q05)、[BA](#ba) | parents | hardware / explicit_decision_or_audit_receipt |
| [Q06](#q06) | Router预测ticket与attempt反馈校正 / implementation | E/B | [Q04](#q04)、[Q05](#q05)、[E05](#e05)、[E06](#e06) | T11 | core / BA/BB/BC_by_selected_scope |
| [R07](#r07) | 全局索引/批量匹配/多租户运营扩展 / research_decision | E/D/H | [Q05](#q05) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [RX07](#rx07) | Master HA/metadata OpLog与故障运营scope / research_decision | D/部署/H | [R06](#r06)、[S07](#s07)、[Q05](#q05) | G package/checklist | research / decision_scope_receipt |
| [Q07](#q07) | 恢复vs重算预测与负反馈consumer / implementation | E/B/D | [Q06](#q06) | T12 | core / BA/BB/BC_by_selected_scope |
| [F04](#f04) | 融合4身份×预热×索引×弹性 / fusion_decision | B/E/D/H | [R05](#r05)、[R06](#r06)、[R07](#r07)、[R10](#r10) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [CP19](#cp19) | 所选HA/OpLog实际部署与恢复消费者 / conditional_implementation | D/部署 | [RX07](#rx07)、[S07](#s07)、[Q05](#q05) | G package/checklist | conditional / BX |
| [S09](#s09) | 部署 actual replica/故障域与 cache-loss 合同 / decision | D/部署 | [S07](#s07)、[RX07](#rx07) | G package/checklist | core / BX |
| [CP20](#cp20) | 所选价值收录/晋升/副本最小policy / conditional_implementation | D/B | [R03](#r03)、[S07](#s07)、[S08](#s08)、[Q07](#q07) | G package/checklist | conditional / BX |
| [Q08](#q08) | 原生队列租户公平/aging与有界亲和 / implementation | E/B/C | [A01](#a01)、[E05](#e05)、[Q06](#q06)、[Q07](#q07)、[E07](#e07) | T13 | core / BA/BB/BC_by_selected_scope |
| [R01](#r01) | 投入价值与恢复/计算联合调度取舍 / research_decision | E/B/H/产品 | [Q07](#q07)、[A02](#a02) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [RX03](#rx03) | 快路由/慢replica双反馈稳定性 / research_decision | E/D/H | [Q07](#q07)、[S07](#s07) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [RX04](#rx04) | cache-awarePD/CP与pool→decode完整状态 / research_decision | B/F/E/H | [V02](#v02)、[Q07](#q07)、[R10](#r10) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [CP28](#cp28) | 所选故障域副本与实际读降级 / conditional_implementation | D/Mooncake/部署 | [S09](#s09)、[S07](#s07)、[E02](#e02) | G package/checklist | conditional / BX |
| [AG01](#ag01) | Agent原生保留/前缀机会与承诺边界 / decision | B/试点产品/H | [Q08](#q08)、[S08](#s08) | X01 | research / explicit_decision_or_audit_receipt |
| [BB](#bb) | B共享目录/公共混流/调度/L2完整批 / acceptance | H/J | [BA](#ba)、[B00](#b00)、[Q08](#q08)、[S08](#s08)、[BS](#bs)、[E07](#e07) | T18.B | hardware / T18.B |
| [CP02](#cp02) | 有界cold公共prefill producer / conditional_implementation | B/selected engine common-prefill producer; Router E supplies bounded queued demand | [CP01](#cp01)、[Q08](#q08)、[AG04](#ag04) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [RX01](#rx01) | pending需求图/producer优先取舍 / research_decision | E/B/H | [Q08](#q08)、[AG04](#ag04) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [RX02](#rx02) | 服务计量/有限hedging/成本感知retraction独立子能力决策 / research_decision | E/B/H | [Q08](#q08)、[Q07](#q07) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [CP22](#cp22) | 所选慢replica与快路由稳定反馈 / conditional_implementation | E/D/B | [RX03](#rx03)、[S07](#s07)、[Q07](#q07) | G package/checklist | conditional / BX |
| [CP12](#cp12) | 实际PD pool→D/首token/增长写回 / conditional_implementation | B/F/PDowner | [RX04](#rx04)、[V04](#v04)、[E02](#e02)、[S05](#s05) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [CP17](#cp17) | 固定CPworker策略及被选split/merge / conditional_implementation | E/B/parallelowner | [RX04](#rx04)、[Q07](#q07)、[Q08](#q08)、[R10](#r10) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [AG02](#ag02) | pause/return/final与有限retention / conditional_implementation | B/产品 | [AG01](#ag01)、[Q02](#q02)、[E05](#e05)、[S08](#s08) | X01 | conditional / BE |
| [R02](#r02) | 生命周期预测与及时提升取舍 / research_decision | B/产品/H | [AG01](#ag01) | X01 | research / explicit_decision_or_audit_receipt |
| [RX06](#rx06) | 公共ContextCache API/权益承诺取舍 / research_decision | 产品/gateway/B/D | [A01](#a01)、[AG01](#ag01)、[R07](#r07) | G package/checklist | research / decision_scope_receipt |
| [BC](#bc) | C真实专用L3完整批 / acceptance | H/J/设备owner | [BB](#bb)、[L04](#l04)、[B00](#b00) | T18.C | hardware / T18.C |
| [CP03](#cp03) | cohort放置/一次预取/sharedHBM消费者 / conditional_implementation | E/B | [CP01](#cp01)、[S08](#s08)、[Q08](#q08) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [CP21](#cp21) | queued-prefix需求树实际enqueue/dequeue消费者 / conditional_implementation | E/B | [RX01](#rx01)、[Q08](#q08)、[S05](#s05) | G package/checklist | conditional / BX |
| [CP23](#cp23) | 所选工作计量/有限hedging/成本感知victim的窄consumer / conditional_implementation | E/B/D | [RX02](#rx02)、[Q08](#q08)、[Q07](#q07)、[E05](#e05) | G package/checklist | conditional / BX |
| [CP13](#cp13) | cache-onlyP bypass被选完整协议 / conditional_implementation | B/F/PDowner | [RX04](#rx04) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [AG03](#ag03) | program/branch fork-join预算与返回语义 / conditional_implementation | B/E/产品 | [AG02](#ag02)、[E07](#e07) | G package/checklist | conditional / BE |
| [F01](#f01) | 融合1共享L2×Agent信号×恢复调度 / fusion_decision | B/E/D/H | [R01](#r01)、[R02](#r02)、[AG01](#ag01)、[BB](#bb) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [CP25](#cp25) | 所选ContextCache用户API完整服务 / conditional_implementation | gateway/产品/B/D | [RX06](#rx06)、[S05](#s05)、[E06](#e06) | G package/checklist | conditional / BX |
| [PH](#ph) | 原完整feature父票AC回填并真正关闭 / hard_parent_rollup | G/H/J/原owner | [BS](#bs)、[BB](#bb)、[BC](#bc) | MC3/SG8/Dynamo1 | release / scope registry/audit only |
| [CP04](#cp04) | Cascade/Hydragen真实batch/kernel接入 / conditional_implementation | B/kernelowner | [CP03](#cp03)、[V04](#v04) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [BE](#be) | 被接受Agent/分支条件扩展批 / acceptance | H/J | [B00](#b00)、[AG01](#ag01)、[AG04](#ag04) | G package/checklist | hardware / explicit_decision_or_audit_receipt |
| [RD](#rd) | 全研究方向explicit disposition与扩展scope registry / scope_decision | 领域owner/产品/J | [R01](#r01)、[R02](#r02)、[R03](#r03)、[R04](#r04)、[R05](#r05)、[R06](#r06)、[R07](#r07)、[R08](#r08)、[R09](#r09)、[R10](#r10)、[R11](#r11)、[R12](#r12)、[F01](#f01)、[F02](#f02)、[F03](#f03)、[F04](#f04)、[RX01](#rx01)、[RX02](#rx02)、[RX03](#rx03)、[RX04](#rx04)、[VV2](#vv2)、[RX05](#rx05)、[RX06](#rx06)、[RX07](#rx07)、[RX08](#rx08)、[RX09](#rx09) | G package/checklist | research / explicit_decision_or_audit_receipt |
| [BX](#bx) | 所选扩展统一完整freeze验收receipt / conditional_acceptance | H/J/产品/领域owner | [B00](#b00)、[RD](#rd) | G package/checklist | conditional / BX selected_scope_extension_of_T18 |
| [RB](#rb) | 最终scope冻结与完整产品发布 / release | 发布owner/H/J/G | [BC](#bc)、[BS](#bs)、[BE](#be)、[V02](#v02)、[RD](#rd)、[BB](#bb)、[PH](#ph)、[VV2](#vv2)、[BX](#bx)、[S09](#s09) | T19 | release / explicit_decision_or_audit_receipt |

## 完整执行包

每包source对应已读domain原子或native源先概念，原primaryselected不变FULL。可验证consumer同时含实际生产接口和后继执行包；关闭只授所列scope。

<a id="s00"></a>
### S00 — 全文覆盖与不可访问来源复核

Owner：coverage/J；audit_gate；status：DRAFT_PENDING_INPUTS；scope：audit。

前置：独立输入；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/storage-article-requirements.md#U01; no product implementation in this decision。

固定产物：source coverage ledger、hash/range、missing/exclude理由。

完整DoD：读过的source逐项有receipt；微信与4空turn/2compaction不可用边界显式保留；G/I全文分页实际回读；不以inventory作fullread

可验证consumer：全部节点事实来源。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/storage-article-requirements.md#U01。

domain原子：storage:U01；Lark source-first：LARK-082、LARK-088。

<a id="v01"></a>
### V01 — 固定首路径运行组合与真实主模型

Owner：A/H/产品；decision；status：DECISION_REQUIRED；scope：input。

前置：独立输入；原锚：T00。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; work/coverage/framework-version-requirements.md#FW02; work/coverage/representation-hardware-requirements.md#RH01; work/coverage/storage-article-requirements.md#U03; work/coverage/router-control-requirements.md#R02; work/coverage/engine-requirements.md#EC01; no product implementation in this decision。

固定产物：engine/store/router/runtime/model/layout支持manifest。

完整DoD：固定实际source、package/library/image ABI与模型/tokenizer/template；FULL/TP1/default-domain首路径与PD/direct/buffer-only/hybrid/TP扩展分开；未知不猜 correctness fixture与production主模型分别锁；已有Qwen0.5B fixedsnapshot可作FULL/BF16/TP1设备正确性fixture，真实runtime/attention/extensions仍须验。业务主模型未给不阻fixture路径，fixture结果不授业务质量/收益。

可验证consumer：I01、E01、L01、B00。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/framework-version-requirements.md#FW02；work/coverage/representation-hardware-requirements.md#RH01；work/coverage/storage-article-requirements.md#U03；work/coverage/router-control-requirements.md#R02；work/coverage/engine-requirements.md#EC01。

domain原子：framework:FW02、representation:RH01、storage:U03、router:R02、engine:EC01；Lark source-first：LARK-003、LARK-004、LARK-006、LARK-087。

<a id="a01"></a>
### A01 — 可信入口与租户/共享域身份

Owner：gateway人类owner/E；input_gate；status：DECISION_REQUIRED；scope：input。

前置：独立输入；原锚：T03。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; work/coverage/storage-article-requirements.md#SR06; work/coverage/storage-article-requirements.md#U04; work/coverage/storage-article-requirements.md#R04; work/coverage/router-control-requirements.md#R01; no product implementation in this decision。

固定产物：HITL5鉴权入口事实与strip/overwrite合同。

完整DoD：实际gateway repo/权威tenant/class/domain/session/model来源、可绕过入口、公共protected字段处理锁定；缺真实身份不授权益

可验证consumer：Q02、S06、E05。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR06；work/coverage/storage-article-requirements.md#U04；work/coverage/storage-article-requirements.md#R04；work/coverage/router-control-requirements.md#R01。

domain原子：storage:SR06、storage:U04、storage:R04、router:R01；Lark source-first：LARK-011、LARK-014。

<a id="a02"></a>
### A02 — 业务trace/SLO/成本输入一次冻结

Owner：产品/H/成本owner；input_gate；status：DECISION_REQUIRED；scope：input。

前置：独立输入；原锚：T03。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; work/coverage/framework-version-requirements.md#FW02; work/coverage/storage-article-requirements.md#SR11; work/coverage/storage-article-requirements.md#EX13; work/coverage/storage-article-requirements.md#U04; work/coverage/acceptance-evidence-requirements.md#economics_denominators; no product implementation in this decision。

固定产物：真实混比/arrival/toolgap/output、SLO与价格/机会成本合同。

完整DoD：责任人及来源、单位、成本边界和分母预签；未知为UNKNOWN；价格不阻auth或保守code，只阻SLO/经济裁决

可验证consumer：BA、BB、BC、BV、R01。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/framework-version-requirements.md#FW02；work/coverage/storage-article-requirements.md#SR11；work/coverage/storage-article-requirements.md#EX13；work/coverage/storage-article-requirements.md#U04；work/coverage/acceptance-evidence-requirements.md#economics_denominators。

domain原子：framework:FW02、storage:SR11、storage:EX13、storage:U04、acceptance:economics_denominators；Lark source-first：LARK-002、LARK-070、LARK-087。

<a id="l01"></a>
### L01 — 真实专用L3设备合同

Owner：设备人类owner/D/B；input_gate；status：DECISION_REQUIRED；scope：input。

前置：独立输入；原锚：T16。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; work/coverage/representation-hardware-requirements.md#RH25; work/coverage/storage-article-requirements.md#SR12; work/coverage/storage-article-requirements.md#SR16; work/coverage/storage-article-requirements.md#U02; work/coverage/storage-article-requirements.md#R06; work/coverage/router-control-requirements.md#R34; work/coverage/engine-requirements.md#XR12; no product implementation in this decision。

固定产物：driver/ABI/object/layout/queue/fence/fault合同。

完整DoD：范围/deadline/read-write-prefetch/partial/cancel/drained/release/shutdown/alignment/容量/介质耐久；directGPU实际支持，不猜GPUDirect/带宽/持久性；无设备只锁missing输入 若 actual flash：GC/满盘 steady state、physical writes/unique KV/retry-replica bytes、WAF/wear/QD/read-write混合tail真实 telemetry；非flash wear轴 NA，能耗只用有来源 sensor与idle/dynamic boundary，不用 TDP充实测。

可验证consumer：L02、L03、L04。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/representation-hardware-requirements.md#RH25；work/coverage/storage-article-requirements.md#SR12；work/coverage/storage-article-requirements.md#SR16；work/coverage/storage-article-requirements.md#U02；work/coverage/storage-article-requirements.md#R06；work/coverage/router-control-requirements.md#R34；work/coverage/engine-requirements.md#XR12。

domain原子：representation:RH25、storage:SR12、storage:SR16、storage:U02、storage:R06、router:R34、engine:XR12；Lark source-first：LARK-003、LARK-059、LARK-062。

<a id="sj"></a>
### SJ — J整源覆盖/图/边界独立审查

Owner：J；audit_review_gate；status：DRAFT_PENDING_INPUTS；scope：audit。

前置：S00；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; no product implementation in this decision。

固定产物：正式J coverage/DAG审查及纠偏receipt。

完整DoD：domain/G/I/context所有receipt和52R、12+4+6+新范围；机器graph无cycle/dangling及条件边显式；本次只能graph检查非产品test；旧Map冻结至PASS

可验证consumer：SP。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md。

domain原子：；Lark source-first：。

<a id="v02"></a>
### V02 — vLLM独立接口和维护范围对照

Owner：F/A；decision；status：DECISION_REQUIRED；scope：research。

前置：V01；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; no product implementation in this decision。

固定产物：vLLM connector→core→worker五场景及维护差异表。

完整DoD：bulk load/failed/frontier/eligible/scheduled分开；decode save job refs/ACK、PD、TP/LCM、hybrid、salt/tenant、priority明确；逐层hook no-op不冒称pipeline

可验证consumer：V03、BV。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md。

domain原子：；Lark source-first：LARK-005。

<a id="sp"></a>
### SP — G唯一Map映射与I知识同步

Owner：G/I；audit_publication；status：DRAFT_PENDING_INPUTS；scope：audit。

前置：SJ；原锚：Map。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; no product implementation in this decision。

固定产物：同canonicalMap实际nativeedges/历史复用+LarkObservePatchVerify。

完整DoD：不重开closed窄history、不duplicateauthority/featurecandidate；新细任务选择native子票或已票checklist保持close边界；G solewriter、I solewriter，全文回读链接/正文/层级；不另tracker

可验证consumer：审计交付。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md。

domain原子：；Lark source-first：。

<a id="v03"></a>
### V03 — 锁首vertical主引擎与Router初始接入范围

Owner：A/B/E/F；decision；status：DECISION_REQUIRED；scope：input。

前置：V01、V02；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; no product implementation in this decision。

固定产物：一次性选型decision与改选触发。

完整DoD：真实模型必要组合与维护成本决定；SG主线、vLLM对照保留；Dynamo按真实入口consumer决定，不默认首vertical必选；不双深fork 这是开工首scope裁决，不宣SG性能胜；最终生产框架selection由VV2消费真实对照。

可验证consumer：I01、Q01。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md。

domain原子：；Lark source-first：LARK-005。

<a id="v04"></a>
### V04 — 固定release能力/拒绝组合矩阵

Owner：A/B/F；decision；status：DECISION_REQUIRED；scope：core。

前置：V01、V02；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/framework-version-requirements.md; work/coverage/framework-version-requirements.md#FW03; work/coverage/representation-hardware-requirements.md#RH19; work/coverage/storage-article-requirements.md#SR10; work/coverage/storage-article-requirements.md#R06; work/coverage/engine-requirements.md#EC01; no product implementation in this decision。

固定产物：config/path/state/quant/parallelism/kernel claim ledger。

完整DoD：FW03完整能力matrix，FC01–08纠偏：SG946已有tp_lcm/page_head代码、MLAreplicated另路；SGFP4SM100/SM120validator不等HiCache/PD支持；VL MC>=0.3.12且CUDA13distribution与SG/Dynamo floor不同；main/doc访问时scope与release分开；每组合actualvalidator/consumer/unknown拒绝。

可验证consumer：V05、V06、CP01、CP07。关闭边界：Complete sourced decision/environment/candidate receipt, no implicit hardware authorization。

batch：formal_receipt；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/framework-version-requirements.md；work/coverage/framework-version-requirements.md#FW03；work/coverage/representation-hardware-requirements.md#RH19；work/coverage/storage-article-requirements.md#SR10；work/coverage/storage-article-requirements.md#R06；work/coverage/engine-requirements.md#EC01。

domain原子：framework:FW03、representation:RH19、storage:SR10、storage:R06、engine:EC01；Lark source-first：LARK-006、LARK-028、LARK-055。

<a id="i01"></a>
### I01 — 整合既有九draft为真实统一候选

Owner：集成owner/H；integration；status：NOT_STARTED；scope：core。

前置：V03；原锚：T00。

实际模块/责任：existing 9 candidate SHA manifests; chosen production build/import/vertical entry receipt。

固定产物：selected/rejected draft、实际candidate ref、完整commit与provenance。

完整DoD：SG PR6/9/11/13/15，MC PR4→7、CI6、CUDA9逐项选用/不用理由；冲突实解；实际joint build/入口/接口smoke与H/J receipt，不靠清单关票

可验证consumer：E01、S01、B00。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/framework-version-requirements.md#FW01；work/coverage/acceptance-evidence-requirements.md#evidence_scope。

domain原子：framework:FW01、acceptance:evidence_scope；Lark source-first：LARK-006、LARK-074、LARK-077、LARK-078、LARK-079、LARK-082。

<a id="q01"></a>
### Q01 — Routerhost原生队列/booking与职责确认

Owner：E；decision；status：DECISION_REQUIRED；scope：core。

前置：V03；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: Router host/native-queue ownership choice resolution; work/coverage/router-control-requirements.md §8 host/framework handoff; no Router implementation in this decision。

固定产物：actual gateway/handler/queue adapter contract。

完整DoD：复用eligibility/filter/scorer/picker/DRR/lane/pending rollback与cleanup；同步热path只本地view；不另建authorityqueue或重booking；Dynamo替代trigger有证据

可验证consumer：Q02、Q04、Q06。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/storage-article-requirements.md#R07。

domain原子：storage:R07；Lark source-first：LARK-015、LARK-032。

<a id="e01"></a>
### E01 — 恢复owner/consumer与退账合同

Owner：B/D/C；decision；status：DECISION_REQUIRED；scope：core。

前置：I01；原锚：T01。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; work/coverage/storage-article-requirements.md#R07; work/coverage/router-control-requirements.md#R11; work/coverage/router-control-requirements.md#R37; work/coverage/engine-requirements.md#EC02; work/coverage/engine-requirements.md#EC16; no product implementation in this decision。

固定产物：acquire→commit/rollback→physical release/unknown合同。

完整DoD：queued/active/source pin/host/HBM/cancel-tail分账；唯一owner与真实caller；取消/失败typed receipt；不重复原生booking/charge，无consumer字段删除

可验证consumer：S01、E02、Q02。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#R07；work/coverage/router-control-requirements.md#R11；work/coverage/router-control-requirements.md#R37；work/coverage/engine-requirements.md#EC02；work/coverage/engine-requirements.md#EC16。

domain原子：storage:R07、router:R11、router:R37、engine:EC02、engine:EC16；Lark source-first：LARK-009、LARK-073。

<a id="v05"></a>
### V05 — 首 SGLang 环境/transitive artifact 与实际库锁

Owner：打包owner/H/A；integration；status：NOT_STARTED；scope：core。

前置：I01、V04、V01；原锚：G package映射。

实际模块/责任：REUSE_SUPPORTING_ASSETS: actual production consumer integration/freeze defined in this package + H existing acceptance contract; no tool-only platform。

固定产物：SG与vLLM各image/wheel/native-library完整lock。

完整DoD：FW04各source/overlay/distribution/transitive依赖hash、CUDA/driver目标、symbols/importpath与MC补丁provenance；Dynamo仅选用时锁；不安装同namespace互盖MC包；无浮动latest/删依赖/关versioncheck制造PASS。CPU候选与GPU模块/kernel能力分开。 本包仅首 SG946 ordinary FULL 运行环境；vLLM 独立环境属于 VV1，不作为 BA 的第二engine前置。production主模型未知可先用已明确 correctness fixture，fixture不授真实业务quality/吞吐。

可验证consumer：BA、VV1、BV。关闭边界：Complete sourced decision/environment/candidate receipt, no implicit hardware authorization。

batch：formal_receipt；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/framework-version-requirements.md；work/coverage/framework-version-requirements.md#FW04；work/coverage/engine-requirements.md#EC01。

domain原子：framework:FW04、engine:EC01；Lark source-first：LARK-006、LARK-081。

<a id="a03"></a>
### A03 — 模型语义generation与全mutation初合同

Owner：B/E/D/部署owner；decision；status：DECISION_REQUIRED；scope：core。

前置：E01、V01；原锚：T02。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; work/coverage/framework-version-requirements.md#FW02; work/coverage/storage-article-requirements.md#SR06; work/coverage/storage-article-requirements.md#U03; work/coverage/router-control-requirements.md#R02; work/coverage/engine-requirements.md#EC18; no product implementation in this decision。

固定产物：实际artifact/layout/所有mutation owner表。

完整DoD：single-controller coarse retire；weight/backend/tenant/generic RPC/SetInternalState/LoRA/elastic/release-resume入口与失败分支逐项锁；缺artifact仍gate

可验证consumer：S05、E06、Q03。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/framework-version-requirements.md#FW02；work/coverage/storage-article-requirements.md#SR06；work/coverage/storage-article-requirements.md#U03；work/coverage/router-control-requirements.md#R02；work/coverage/engine-requirements.md#EC18。

domain原子：framework:FW02、storage:SR06、storage:U03、router:R02、engine:EC18；Lark source-first：LARK-028、LARK-029。

<a id="b00"></a>
### B00 — 一次批前freeze与实际观测consumer

Owner：H/组件/J；acceptance_prepare；status：NOT_STARTED；scope：support。

前置：I01、V01、E01；原锚：T18。

实际模块/责任：work/implementation/validation/acceptance evidence；selected framework/backend real consumer and existing replay assets。

固定产物：fixedhead/config/ABI/oracle/trace/病例/skip/预算manifest。

完整DoD：复用已有trace/replay/CI assets；实际部署SHA非计划值；request-attempt-op-gene映射/ownerclock/causality；actual/reported/inferred与null分开；仅必要开发回归，不tool-onlymilestone

可验证consumer：BA、BB、BC、BE、BV。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：T18；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/framework-version-requirements.md#FW15；work/coverage/storage-article-requirements.md#SR11；work/coverage/router-control-requirements.md#R35；work/coverage/engine-requirements.md#EC17；work/coverage/acceptance-evidence-requirements.md#freeze_batch；work/coverage/acceptance-evidence-requirements.md#causal_trace_presence。

domain原子：framework:FW15、storage:SR11、router:R35、engine:EC17、acceptance:freeze_batch、acceptance:causal_trace_presence；Lark source-first：LARK-008、LARK-069、LARK-073、LARK-074、LARK-075、LARK-076、LARK-077、LARK-078、LARK-079、LARK-080、LARK-084、LARK-087。

<a id="s01"></a>
### S01 — Store/TE操作owner与逻辑/物理终态贯通

Owner：D；implementation；status：NOT_STARTED；scope：core。

前置：E01；原锚：T04。

实际模块/责任：MC719 mooncake-store/src/transfer_task.cpp::TransferEngineOperationState/TransferFuture wait/query/free (storage S6)；MC719 mooncake-store/src/client_service.cpp::Put/Query/Get/BatchGet; master_service.cpp::Allocate/PutEnd/PutRevoke/GrantReadLease (storage S2/S3)；MC719 transfer-engine/src/transport/transport.cpp::freeBatchID Busy owner (storage S6)。

固定产物：Client OperationState/TransferSubmitter完整scope候选。

完整DoD：真实GET/PUT同步返回、partial-submit/query/free/error/timeout永久hold策略、描述vector借用buffer寿命；逻辑失败sticky、query/free唯一串行owner；成功free后不再访问；unknown不得强free

可验证consumer：S02、E02。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR01；work/coverage/storage-article-requirements.md#SR02；work/coverage/storage-article-requirements.md#SR03；work/coverage/storage-article-requirements.md#SR04；work/coverage/storage-article-requirements.md#R03；work/coverage/engine-requirements.md#EC03；work/coverage/engine-requirements.md#EC04；work/coverage/acceptance-evidence-requirements.md#evidence_scope。

domain原子：storage:SR01、storage:SR02、storage:SR03、storage:SR04、storage:R03、engine:EC03、engine:EC04、acceptance:evidence_scope；Lark source-first：LARK-023。

<a id="e02"></a>
### E02 — SG pooled读/写worker异常与rank终态

Owner：B/D；implementation；status：NOT_STARTED；scope：core。

前置：S01；原锚：T04。

实际模块/责任：SG946 python/sglang/srt/managers/cache_controller.py::_storage_load_thread/load/progress/ACK (engine P4)；SG946 hybrid_cache/hybrid_cache_controller.py::backup worker (engine P11)；mooncake_store.py actual batch_get/batch_put (storage S1)。

固定产物：backend→controller worker→URC真实读写failure候选。

完整DoD：GET正常/partial/False/抛异常与PUT异常均有一致rank终态；payload结果与release_safe分开；late/重复ACK按handle/op；unknown隔离且保留owner，不能fake成功ACK

可验证consumer：E03、E04、E06、BA。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/framework-version-requirements.md#FW05；work/coverage/storage-article-requirements.md#SR01；work/coverage/storage-article-requirements.md#SR04；work/coverage/router-control-requirements.md#R14；work/coverage/engine-requirements.md#EC03；work/coverage/engine-requirements.md#EC04；work/coverage/engine-requirements.md#EC19；work/coverage/engine-requirements.md#AG08。

domain原子：framework:FW05、storage:SR01、storage:SR04、router:R14、engine:EC03、engine:EC04、engine:EC19、engine:AG08；Lark source-first：LARK-021、LARK-022、LARK-023。

<a id="s02"></a>
### S02 — TE完成发布与variant拒绝接入

Owner：D/集成owner；implementation；status：NOT_STARTED；scope：core。

前置：S01；原锚：T05。

实际模块/责任：MC719 OperationState/StoreSubmitter variant guard; transfer-engine event BatchDesc/Slice submit/seal/query/free (storage P02/P03/S6)；PROPOSED: Store event lifetime integration only selected variant; current event/TENT reject retained。

固定产物：Store+TE同state query/free consumer及variant支持表。

完整DoD：classic/event/TENT allocate/submit前真实拒绝/放行；TE PR7 source和同8CPU只为历史窄证据；event放行仍需Store整条consumer和设备硬gate；直接transport/NVMe/MP/TENT未验profile拒绝

可验证consumer：E02、BA、BS。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR05；work/coverage/storage-article-requirements.md#SR10；work/coverage/storage-article-requirements.md#R06；work/coverage/acceptance-evidence-requirements.md#evidence_scope。

domain原子：storage:SR05、storage:SR10、storage:R06、acceptance:evidence_scope；Lark source-first：。

<a id="e03"></a>
### E03 — host恢复grant与active占用硬门控

Owner：B/C；implementation；status：NOT_STARTED；scope：core。

前置：E01、E02；原锚：T06。

实际模块/责任：SG946 unified_radix_cache.py::_try_alloc_storage_hit/_handle_prefetch_result/release_aborted_request (engine P2/P3/P5)；cache_controller.py enqueue/active op/progress/final ACK (engine P4)。

固定产物：host allocate/enqueue/source acquire前真实grant。

完整DoD：意图limiter/qsize不作物理账；queued/active/cancel-tail真实bytes/ops；所有rank确定顺序，拒绝/shorten/revoke/recompute可取消；host承诺完整兑现或0重算

可验证consumer：E04、S08。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR04；work/coverage/storage-article-requirements.md#SR08；work/coverage/router-control-requirements.md#R17；work/coverage/router-control-requirements.md#R38；work/coverage/engine-requirements.md#EC05；work/coverage/engine-requirements.md#EC16。

domain原子：storage:SR04、storage:SR08、router:R17、router:R38、engine:EC05、engine:EC16；Lark source-first：LARK-012、LARK-013、LARK-078。

<a id="s05"></a>
### S05 — immutable对象key与producer旧binding

Owner：B/D；implementation；status：NOT_STARTED；scope：core。

前置：E02、A03；原锚：T08。

实际模块/责任：SG946 mem_cache/storage/mooncake_store/mooncake_store.py::config_prefix/_tag_keys/batch_put; utils.py storage_namespace_seed (engine P14/router R06)；MC719 client_service.cpp::Put/BatchPut; master_service.cpp::PutEnd/Upsert (storage S2/S8)；PROPOSED: immutable epoch/write binding checks; original key no compatibility fallback。

固定产物：backend/prefetch/backup key/generation真实接入。

完整DoD：None/empty/UTF8实际prefix、完整storage seed/hash/KV/rank/PP suffix；仅sealed对象、禁同keyUpsert、同key写重试串行；晚PUT保旧key/backend；partial attach失败closed

可验证consumer：S06、E06、Q03、S07。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR02；work/coverage/storage-article-requirements.md#SR06；work/coverage/storage-article-requirements.md#R05；work/coverage/router-control-requirements.md#R02；work/coverage/engine-requirements.md#EC14；work/coverage/engine-requirements.md#AG01。

domain原子：storage:SR02、storage:SR06、storage:R05、router:R02、engine:EC14、engine:AG01；Lark source-first：LARK-024、LARK-027、LARK-028、LARK-030。

<a id="vv1"></a>
### VV1 — vLLM等价Store适配/事件实际消费者

Owner：F/vLLM adapterowner；implementation；status：NOT_STARTED；scope：core。

前置：V05、V02、E01、E02；原锚：G package映射。

实际模块/责任：vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py；vllm Mooncake scheduler/offload worker/admission/result callbacks。

固定产物：出树adapter及必要窄core/worker hooks。

完整DoD：FW06+FW15：实际context/attempt→lookup/load/invalidfrontier→coreeligible/scheduled；save_jobrefs/generation/allrank/idlepoll与readattempt差异；Storelogicalfailed不free；事件真实producer→controller/Hconsumer/ownerclock因果，缺rank/late/cancel/source-loss/unknown拒绝；保nativeblockallocator和bulk/no-oplayer语义，不开第二deepfork。trusted权益仅A01完成才启。 独立 vLLM v0.30.0 环境/package/CUDA/artifact/import/library lock 在本包完成；不与SGenv强行同一个锁，不阻首SG运行。

可验证consumer：BV、VV2。关闭边界：Complete sourced decision/environment/candidate receipt, no implicit hardware authorization。

batch：formal_receipt；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/framework-version-requirements.md；work/coverage/framework-version-requirements.md#FW06；work/coverage/framework-version-requirements.md#FW15。

domain原子：framework:FW06、framework:FW15；Lark source-first：LARK-073。

<a id="e04"></a>
### E04 — HBM准入与逐层消费/释放闭环

Owner：B/C；implementation；status：NOT_STARTED；scope：core。

前置：E03；原锚：T06。

实际模块/责任：SG946 schedule_policy.py::PrefillAdder select/commit (engine P8)；unified_radix_cache.py::init_load_back/wholefinish reaper (engine P6/P7)；l2_transfer.py layer copy events; memory_pool.py actual per-layer consumer (engine P7)；schedule_batch.py next-step/retract; scheduler.py native waiting candidate (engine P8/P9)。

固定产物：PrefillAdder/select→loadback→commit→layer fence→whole reaper接入。

完整DoD：复用原生adder/allocator，足够则源码实证no-change；缺口只加物化前gate；保持page/chunk/nextdecode/未来增长，不加全层barrier；blocked未commit跳过边界与commit结束batch边界明确 worker 每步冷/短/singleton机会与已接纳长 decode physical headroom 兑现，复用 next-step/retract 原生门；candidate blocked 与 committed-stop 分开，不机械 break→continue，长期到达进展由 BB验。

可验证consumer：E05、E06、BA。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/framework-version-requirements.md#FW05；work/coverage/storage-article-requirements.md#SR01；work/coverage/storage-article-requirements.md#SR04；work/coverage/storage-article-requirements.md#SR09；work/coverage/storage-article-requirements.md#R02；work/coverage/router-control-requirements.md#R17；work/coverage/router-control-requirements.md#R38；work/coverage/engine-requirements.md#EC03；work/coverage/engine-requirements.md#EC06；work/coverage/engine-requirements.md#EC07；work/coverage/engine-requirements.md#EC09；work/coverage/engine-requirements.md#EC13；work/coverage/engine-requirements.md#EC19。

domain原子：framework:FW05、storage:SR01、storage:SR04、storage:SR09、storage:R02、router:R17、router:R38、engine:EC03、engine:EC06、engine:EC07、engine:EC09、engine:EC13、engine:EC19；Lark source-first：LARK-003、LARK-012、LARK-013、LARK-015、LARK-021、LARK-022。

<a id="r05"></a>
### R05 — 公共prefix预计算与版本发布取舍

Owner：B/D/产品；research_decision；status：DECISION_REQUIRED；scope：research。

前置：S05、A03；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/representation-hardware-requirements.md#RH07; work/coverage/storage-article-requirements.md#EX04; work/coverage/router-control-requirements.md#R29; work/coverage/engine-requirements.md#XR09; no product implementation in this decision。

固定产物：12方向#5对象版本预热/按需对照decision。

完整DoD：真实渲染token而非template相似；model/tokenizer/position/toolpromptrevision绑定；每对象寿命内避免GPU秒减precompute/staging/retention成本，版本快变/不用否证

可验证consumer：RD、F04。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/representation-hardware-requirements.md#RH07；work/coverage/storage-article-requirements.md#EX04；work/coverage/router-control-requirements.md#R29；work/coverage/engine-requirements.md#XR09。

domain原子：representation:RH07、storage:EX04、router:R29、engine:XR09；Lark source-first：LARK-047。

<a id="r08"></a>
### R08 — 无损codec/低bitKV/MLA独立表示取舍

Owner：B/表示owner/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：V01、S05；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/storage-article-requirements.md#EX08; work/coverage/engine-requirements.md#XR03; no product implementation in this decision。

固定产物：12方向#8三表示路线model/rank字节与质量decision。

完整DoD：无损逐byte；KVquant scale/error/kernellayout与任务质量；MLA原生latent/RoPE/rank复制与rank0broadcast实际成本；权重量化不证明KV；CPU/DPU/GPU编码resource及临时HBM

可验证consumer：RD、F03。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/storage-article-requirements.md#EX08；work/coverage/engine-requirements.md#XR03。

domain原子：storage:EX08、engine:XR03；Lark source-first：LARK-052、LARK-053、LARK-054。

<a id="r09"></a>
### R09 — 非prefixRAG与上下文变体取舍

Owner：表示/应用owner/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：V01、S05；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/representation-hardware-requirements.md#RH15; work/coverage/storage-article-requirements.md#EX09; work/coverage/engine-requirements.md#XR04; no product implementation in this decision。

固定产物：12方向#9 exactprefix vs selectedrecompute/variant decision。

完整DoD：同text不同位置/前文不直接exactKV；CacheBlend/PromptCache/CacheCraft条件与新负载；多跳/跨文档/长检索质量oracle、位置/顺序/插入变量；误差叠加单独验收、变体容量失控退出

可验证consumer：RD。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/representation-hardware-requirements.md#RH15；work/coverage/storage-article-requirements.md#EX09；work/coverage/engine-requirements.md#XR04。

domain原子：representation:RH15、storage:EX09、engine:XR04；Lark source-first：LARK-057。

<a id="r10"></a>
### R10 — 跨TP/layout与hybrid合法状态恢复

Owner：B/F/表示owner/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：V01、V02、S05；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/framework-version-requirements.md#FW10; work/coverage/representation-hardware-requirements.md#RH19; work/coverage/representation-hardware-requirements.md#RH22; work/coverage/storage-article-requirements.md#EX07; work/coverage/engine-requirements.md#XR01; work/coverage/engine-requirements.md#XR02; no product implementation in this decision。

固定产物：12方向#10真实组合矩阵与legal-boundary decision。

完整DoD：FULL/SWA/Mamba/recurrent必要组件合法集合交集、checkpointdensity/replay；scalarMIN现状不冒setintersection；TP/LCM/page/block/kernel/PP/CP转换成本，DCP/backends/FP4不支持显式拒绝；跨engine不预建tensorABI

可验证consumer：RD、F04。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/framework-version-requirements.md#FW10；work/coverage/representation-hardware-requirements.md#RH19；work/coverage/representation-hardware-requirements.md#RH22；work/coverage/storage-article-requirements.md#EX07；work/coverage/engine-requirements.md#XR01；work/coverage/engine-requirements.md#XR02。

domain原子：framework:FW10、representation:RH19、representation:RH22、storage:EX07、engine:XR01、engine:XR02；Lark source-first：LARK-055、LARK-056。

<a id="s07"></a>
### S07 — L2 placement/replica/lease/pin实际容量回收

Owner：D/B；implementation；status：NOT_STARTED；scope：core。

前置：E02、S05；原锚：T14。

实际模块/责任：MC719 master_service.cpp placement/lease/eviction/pin/quota/actual replica consumers; replica.h::ReplicateConfig (storage S3/S4/S5/S7)；MC719 tenant_quota_ledger.cpp actual allocation/settle; SG host/HBM source references。

固定产物：原生Master/object/group/quota hooks候选。

完整DoD：仅补实际missinghook；requested/actual replica分开，physical副本去重；source lease不能保force remove/ownerloss；release后allocator真实再用；reader/writer在飞驱逐/复制/失败出口完整

可验证consumer：S08、L02、R03、BB。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR03；work/coverage/storage-article-requirements.md#SR08；work/coverage/storage-article-requirements.md#R01；work/coverage/router-control-requirements.md#R37；work/coverage/engine-requirements.md#EC16。

domain原子：storage:SR03、storage:SR08、storage:R01、router:R37、engine:EC16；Lark source-first：LARK-007、LARK-019、LARK-025、LARK-043。

<a id="v06"></a>
### V06 — 实际补丁维护面积与upgrade门槛

Owner：A/B/E/F/D；decision；status：DECISION_REQUIRED；scope：research。

前置：I01、V04、VV1；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/framework-version-requirements.md; work/coverage/framework-version-requirements.md#FW16; no product implementation in this decision。

固定产物：files/hooks/privateAPI/ABI upstream差异receipt。

完整DoD：FW16固定SHA实际patch及invariants/graph-async行为、对象ABI、受影响consumer与所需回归；不用LOC/latest宣维护小；改source/binary/profile重适用gate，不造migration/backcompat层或自动upgrade。

可验证consumer：VV2。关闭边界：Complete sourced decision/environment/candidate receipt, no implicit hardware authorization。

batch：formal_receipt；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/framework-version-requirements.md；work/coverage/framework-version-requirements.md#FW16。

domain原子：framework:FW16；Lark source-first：。

<a id="ba"></a>
### BA — A fixed-domain无信用vertical批

Owner：H/J；acceptance；status：NOT_STARTED；scope：hardware。

前置：B00、E02、E04、S02、V05、V04；原锚：T18.A。

实际模块/责任：REUSE_SUPPORTING_ASSETS: actual production consumer integration/freeze defined in this package + H existing acceptance contract; no tool-only platform。

固定产物：cold/L2hit/取消/PUT/GET/fault与设备数据receipt。

完整DoD：真实storage→host→GPU，强native同总DRAM对照、objectpayload/output oracle、device-onlyevict保host、localempty后storage恢复；lateACK/rank/tail/sourcepin再分配、shutdown/DMA硬验；所有必需轴，不CPU冒设备

可验证consumer：RA、BB、R01。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：T18.A；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/framework-version-requirements.md#FW05；work/coverage/storage-article-requirements.md#SR01；work/coverage/storage-article-requirements.md#SR11；work/coverage/router-control-requirements.md#R36；work/coverage/engine-requirements.md#EC03；work/coverage/engine-requirements.md#EC20；work/coverage/acceptance-evidence-requirements.md#evidence_scope；work/coverage/acceptance-evidence-requirements.md#freeze_batch；work/coverage/acceptance-evidence-requirements.md#six_path_oracles。

domain原子：framework:FW05、storage:SR01、storage:SR11、router:R36、engine:EC03、engine:EC20、acceptance:evidence_scope、acceptance:freeze_batch、acceptance:six_path_oracles；Lark source-first：LARK-007、LARK-021、LARK-069、LARK-080、LARK-081、LARK-084。

<a id="q02"></a>
### Q02 — 可信context逐turn传播到真实Req

Owner：E/B；implementation；status：NOT_STARTED；scope：core。

前置：A01、E01、Q01、E04；原锚：T07。

实际模块/责任：Dynamo b83 http/service/metadata.rs::extract_metadata_from_http；extensions.rs::apply_frontend_nvext_policy → metadata/preprocessor/routing_host；SG946 request_handlers/handler_base.py→Tokenizer request broadcast→Req internal consumer；PROPOSED: trusted context/attempt mapping bridge; actual gateway repo remains input。

固定产物：入口metadata→handler→Tokenizer→Req内部context候选。

完整DoD：public自报字段清除/覆盖；ordinary默认完整路径；每turn新admission；toolwait不持activebooking；request/attempt/handle映射及retry/stream/cancel/retract明确

可验证consumer：E05、S06、Q03、Q06。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/router-control-requirements.md#R03；work/coverage/engine-requirements.md#EC10；work/coverage/engine-requirements.md#AG03。

domain原子：router:R03、engine:EC10、engine:AG03；Lark source-first：LARK-001、LARK-011、LARK-014、LARK-026。

<a id="cp07"></a>
### CP07 — 表示对象data/scale/codec ABI实际consumer

Owner：A/B/D；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：R08、V04、S05；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: selected representation storage object ABI (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: mooncake_store.py key/manifest (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：native/codec/quant/MLA分profile objectmanifest。

完整DoD：RH10data+scale/zero/layout/codecversion/padding/shard/epoch完整；modelnative状态权威consumer，BF16baseline与低bitquality不同；已支持/unknown/拒profile explicit。

可验证consumer：CP08、CP09、CP10、CP11、BX。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R08", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "representation_object_abi"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/framework-version-requirements.md#FW14；work/coverage/representation-hardware-requirements.md#RH10；work/coverage/storage-article-requirements.md#EX08；work/coverage/engine-requirements.md#XR03。

domain原子：framework:FW14、representation:RH10、storage:EX08、engine:XR03；Lark source-first：LARK-028、LARK-052。

<a id="r12"></a>
### R12 — 设备attention与active-decode下层流式读

Owner：表示/设备owner/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：L01、R08；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/representation-hardware-requirements.md#RH30; work/coverage/storage-article-requirements.md#EX11; work/coverage/engine-requirements.md#XR13; no product implementation in this decision。

固定产物：12方向#12长期近数据attention可行性decision。

完整DoD：exactpartialoutput/LSE正确query/mask/scaling与数值误差；每层往返、内部扫描/算力/带宽/能耗；搬KV/设备算/稀疏近似三路，近似质量另验；普通DPU/SSD/CMX不预设tensor算力

可验证consumer：RD。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/representation-hardware-requirements.md#RH30；work/coverage/storage-article-requirements.md#EX11；work/coverage/engine-requirements.md#XR13。

domain原子：representation:RH30、storage:EX11、engine:XR13；Lark source-first：LARK-063、LARK-064。

<a id="rx08"></a>
### RX08 — pruning/compaction 独立质量与表示决策

Owner：representation/kernel；research_decision；status：NOT_STARTED；scope：exploratory。

前置：R08、A02；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/representation-hardware-requirements.md; work/coverage/representation-hardware-requirements.md#RH34; no product implementation in this decision。

固定产物：pruning/compaction 独立质量与表示决策：固定 scope 与可审 receipt。

完整DoD：锁 LeanKV v1 或 DiffKV v3，不融合版本数字；dense/heterogeneous K/V/per-head/token sparse 对比一次决定；逐 sample 质量、output length、完成 latency、长尾、总成本与 temporary HBM/SM；accepted 绑定 CP26，未读 primary 全文 gate 保留。

可验证consumer：RD。关闭边界：一次 signed resolution：accepted/measured-no-change/deferred/rejected/unknown；accepted 必绑定实现与验收，unknown 不得关闭。

batch：decision_registry；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH34。

domain原子：representation:RH34；Lark source-first：。

<a id="r03"></a>
### R03 — 价值收录/淘汰/副本取舍

Owner：D/B/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：S07、A02；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/storage-article-requirements.md#EX01; work/coverage/router-control-requirements.md#R25; no product implementation in this decision。

固定产物：12方向#3 LRU强基线与FLOPs-byte增量decision。

完整DoD：录入/层/提升/副本分开；连续prefix依赖、replica/pinbyte-time、newworkload适应；大池LRU足够可明确reject复杂评分；不把hitcount当省费

可验证consumer：RD、F03。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/storage-article-requirements.md#EX01；work/coverage/router-control-requirements.md#R25。

domain原子：storage:EX01、router:R25；Lark source-first：LARK-041、LARK-042、LARK-086。

<a id="s08"></a>
### S08 — demand/writeback/prefetch三类有界IO份额

Owner：B/D/E；implementation；status：NOT_STARTED；scope：core。

前置：E03、E04、S07；原锚：T15。

实际模块/责任：SG946 managers/cache_controller.py actual read/write/prefetch/backup worker queues (engine P4/P11)；SG946 mem_cache/unified_radix_cache.py::D2H backup reserve/host→Store pin/write finish (engine P11)；SG946 hybrid_cache/hybrid_cache_controller.py::backup worker (engine P11)；PROPOSED: demand/necessary writeback/prefetch finite grants at actual submissions; no new TE platform。

固定产物：engine grants/controller/Store队列完整consumer。

完整DoD：ordinary份额不依A01；trustedpolicy扩展另须Q02/Q08；activebytes/ops与rank一致；prefetch剩余额度可撤销、demand保证、必要writeback排空防sourcepin堵塞；高水位/backpressure不造qsize账 新 sealed page incremental writeback/D2H/PUT actual producer 至 completion source pin，partialtail/重复写/backpressure 与结束后台tail归旧owner；必要 eviction writeback 有进展，有限优先级继承不永久升 class。

可验证consumer：AG01、L02、R11、BB。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR09；work/coverage/router-control-requirements.md#R28；work/coverage/router-control-requirements.md#R38；work/coverage/engine-requirements.md#EC08；work/coverage/engine-requirements.md#EC19；work/coverage/engine-requirements.md#AG07。

domain原子：storage:SR09、router:R28、router:R38、engine:EC08、engine:EC19、engine:AG07；Lark source-first：LARK-009、LARK-013、LARK-017、LARK-018、LARK-026、LARK-042。

<a id="bv"></a>
### BV — vLLM固定模型/trace/预算对照批

Owner：F/H/J；acceptance；status：NOT_STARTED；scope：hardware。

前置：V02、B00、VV1、BA；原锚：G package映射。

实际模块/责任：REUSE_SUPPORTING_ASSETS: actual production consumer integration/freeze defined in this package + H existing acceptance contract; no tool-only platform。

固定产物：独立环境同模型/tokenizer/layout/arrival预算connector对照。

完整DoD：native强基线与Store bulkfailed/jobpin物理scope；共Storedrain缺口不能换框架消失；维护面积/SLO与主线同口径，无machine保持blocked不强第二fork

可验证consumer：R01、RB。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：explicit_decision_or_audit_receipt；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/framework-version-requirements.md#FW07；work/coverage/acceptance-evidence-requirements.md#economics_denominators。

domain原子：framework:FW07、acceptance:economics_denominators；Lark source-first：LARK-005、LARK-068、LARK-071。

<a id="cp14"></a>
### CP14 — host-cache/buffer/direct/nativeoffload独立路径

Owner：B/F；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：V04、BA、R08；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: hicache_hook.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: unified cache registry/DirectLinker/host offload (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：一个selectedpath registry/keys/loader/copy候选。

完整DoD：FW09初始化互斥和拒配置保留；同trace总DRAM、近端副本/IO/H2D/layerstall/graph/cancelrelease；dynamic共存若选才做hook，不能旧profile透明sharedABI；设备visibility单验。

可验证consumer：BX。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R08", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "selected_host_buffer_direct_path"}。

source refs：work/coverage/framework-version-requirements.md；work/coverage/framework-version-requirements.md#FW09。

domain原子：framework:FW09；Lark source-first：。

<a id="ra"></a>
### RA — 有限A发布出口

Owner：发布owner/H/J/G；release；status：NOT_STARTED；scope：release。

前置：BA；原锚：T19.A。

实际模块/责任：REUSE_SUPPORTING_ASSETS: actual production consumer integration/freeze defined in this package + H existing acceptance contract; no tool-only platform。

固定产物：只A scope支持/拒绝profiles与release receipt。

完整DoD：A全部必需轴及该scope适用hardparent真正close；merge/deploy沿授权；明确不关闭B/C/X/研究；draft/CI不授deployment

可验证consumer：RB。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/router-control-requirements.md#R36；work/coverage/acceptance-evidence-requirements.md#operations_recovery_shutdown。

domain原子：router:R36、acceptance:operations_recovery_shutdown；Lark source-first：。

<a id="e05"></a>
### E05 — worker typed兑现/拒绝与实际服务结算

Owner：B/C；implementation；status：NOT_STARTED；scope：core。

前置：Q02、E04；原锚：T07。

实际模块/责任：SG946 request_handlers/handler_base.py→Req→PrefillAdder commit；scheduler.py::run_batch; scheduler_components/batch_result_processor.py actual forward/stream/result receipt consumer (engine P10/EC10)。

固定产物：Req/result processor typed receipt与实际consumer。

完整DoD：ADMISSION_COMMITTED/REJECTED、forward/stream/retry-safe、actual prefill/decode/current+future HBM与restore区分；old/duplicate不双结算；长decode反馈滚动修正；不重造无消费者chargeledger

可验证consumer：Q06、Q08、S08、BB。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/framework-version-requirements.md#FW15；work/coverage/router-control-requirements.md#R11；work/coverage/router-control-requirements.md#R13；work/coverage/engine-requirements.md#EC07；work/coverage/engine-requirements.md#EC09；work/coverage/engine-requirements.md#EC10；work/coverage/engine-requirements.md#EC17；work/coverage/engine-requirements.md#AG03；work/coverage/acceptance-evidence-requirements.md#causal_trace_presence。

domain原子：framework:FW15、router:R11、router:R13、engine:EC07、engine:EC09、engine:EC10、engine:EC17、engine:AG03、acceptance:causal_trace_presence；Lark source-first：LARK-009、LARK-012、LARK-019、LARK-033、LARK-038、LARK-073。

<a id="s06"></a>
### S06 — 所选强 per-API Store 隔离的 per-batch tenant consumer

Owner：D/B/E；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：A01、Q02、S05、S10；原锚：T08。

实际模块/责任：MC719 mooncake-integration/store/store_py.cpp::setup + Python batch_get/batch_put (storage S13)；MC719 client_service.cpp::BatchQuery tenant overload→master_service.cpp quota consumer (storage S7/S13)；PROPOSED ONLY_IF_S10: per-batch tenant binding/RPC consumer; no TE lifetime files。

固定产物：binding→Client→Master tenant-aware RPC完整consumer。

完整DoD：setup-domain不冒perAPI tenant；分batch可信tenant复用buffer，拒globaltenant并发mutation；share域授权/physicalquota/retention受益与IO服务账分开；default与nondefault实际PUT/GET/event/query 仅S10显式选择强perAPI Store隔离才启用；setupdomain/namespace/Engine service-retention额度核心模式先复用，不用强Store模式阻塞普通路径。

可验证consumer：Q04、S07、BB。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR06；work/coverage/storage-article-requirements.md#R04；work/coverage/router-control-requirements.md#R07。

domain原子：storage:SR06、storage:R04、router:R07；Lark source-first：LARK-026。

执行guard：{"decision": "S10", "selector": "strong_per_api_store_quota", "accepted": "只有真实产品要求强perAPI Store物理quota时实施per-batch Client→Master consumer", "unknown": "BLOCKED", "deferred_rejected": "signed setup-domain/native namespace + Engine权益模式；该强Store隔离明确unsupported/reopen"}。

<a id="cp09"></a>
### CP09 — 原生量化/MLA被选表示端到端

Owner：B/D/model；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：CP07、E04、R08；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: selected native attention/KV quant or MLA backend (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: memory_pool.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: rank broadcast (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：data+scale原生attention、MLAlatent/RoPE rank分发候选。

完整DoD：RH12/13分别profiles：量化generation完整scale、transformbuffers与错epoch拒、避免无意BF16中转；MLAowner/rankbroadcast与各rank读强对照；FP4/PD/hierarchicalunsupported明确拒，MLA非GQA无损codec；各quality与多rankfailure独验。 native KV quant与native MLA分别选subprofile、分别oracle与关闭receipt；选择其中一项不自动要求另一项，若皆选均须对应真实kernel/quality。

可验证consumer：BX、F03。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R08", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "selected_native_kv_quant_or_mla"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/framework-version-requirements.md#FW14；work/coverage/representation-hardware-requirements.md#RH12；work/coverage/representation-hardware-requirements.md#RH13；work/coverage/storage-article-requirements.md#EX08；work/coverage/engine-requirements.md#XR03。

domain原子：framework:FW14、representation:RH12、representation:RH13、storage:EX08、engine:XR03；Lark source-first：LARK-053、LARK-054。

<a id="cp10"></a>
### CP10 — 一个layout/TP转换及有限物化副本

Owner：B/F/D；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：R10、CP07、S05；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: mooncake_store.py TP/page_head (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: selected host pool PoolTransfer (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: selected attention target (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：sourcepair→Store→gather/scatter/scale→targetallocator/kernel。

完整DoD：RH19/20+FW10真实TP/PP/CP/page/heads/replicatedmatrix；sameTPcontrol/partialrank/namespace拒、numericoracle；online重排vsnativecopies成本/scratch/复制预算；DCP/hybrid跨TPunsupported不扩称，crossengineuniversalABI拒。

可验证consumer：BX、CP06、F04。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R10", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "cross_tp_layout_conversion"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/framework-version-requirements.md#FW10；work/coverage/representation-hardware-requirements.md#RH20；work/coverage/storage-article-requirements.md#EX07；work/coverage/engine-requirements.md#XR02。

domain原子：framework:FW10、representation:RH20、storage:EX07、engine:XR02；Lark source-first：LARK-055。

<a id="cp11"></a>
### CP11 — hybrid合法stop集合/完整checkpoint消费者

Owner：B/F/D；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：R10、CP07、E04；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: unified_cache/components/full.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: components/swa.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: components/mamba.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: hybrid_cache_controller.py (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：FULL+SWAwindow+recurrentcheckpoint write/read/evict/recover。

完整DoD：RH22–24/FW13actualcaller使用合法集合交集，含长合法/中间hole/不同rank/缺sidecar；alignedcheckpoint/COW/rollback/cancel/重放；uniform vs tool/fork边界、buffer_only/backendblock限制；全部必要statefence/allocator回收，FULLpass不扩hybrid。

可验证consumer：BX、F04。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R10", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "hybrid_legal_restore"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/framework-version-requirements.md#FW13；work/coverage/representation-hardware-requirements.md#RH22；work/coverage/representation-hardware-requirements.md#RH23；work/coverage/storage-article-requirements.md#EX07；work/coverage/storage-article-requirements.md#R02；work/coverage/engine-requirements.md#XR01。

domain原子：framework:FW13、representation:RH22、representation:RH23、storage:EX07、storage:R02、engine:XR01；Lark source-first：LARK-056。

<a id="cp18"></a>
### CP18 — 真实冷attentionpartition/merge消费者

Owner：device/B/model；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：R12、CP07、E04、L01；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: actual L3 compute executor UNKNOWN_INPUT (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: selected partial attention/output-LSE merge kernel (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：query→devicecold output+LSE→GPUhot→merge→nextlayer。

完整DoD：RH30–32accepted真实computeABI才启；samequery/disjointKV/mask/scaling/LSElogbase/precision、epoch/fault/partial/cancelrefs；exactmerge vs sparse/criticalentry质量独立；每tokenbytes/scan/roundtrip/energy对restore对照，模拟不关feature。

可验证consumer：BX。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R12", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "near_data_attention"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH31；work/coverage/representation-hardware-requirements.md#RH32；work/coverage/storage-article-requirements.md#EX11；work/coverage/engine-requirements.md#XR13。

domain原子：representation:RH31、representation:RH32、storage:EX11、engine:XR13；Lark source-first：LARK-063、LARK-064。

<a id="cp26"></a>
### CP26 — 所选 KV pruning 与 ragged compaction 消费

Owner：representation/kernel；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX08、CP07、E04；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: selected-model attention kernel (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: sglang/python/sglang/srt/mem_cache/memory_pool.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: selected representation storage codec (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：所选 KV pruning 与 ragged compaction 消费：固定 scope 与可审 receipt。

完整DoD：importance→prune/quant→ragged page publish→GPU compaction→restore→实际 attention；deleted token identity/RoPE/mask 明确，cancel/temporary bytes/SM owner 归账；同 dense/native baseline 的逐 sample/outputlength/完成 latency/longtail 与质量阈值冻结，故障不能读取已删状态。

可验证consumer：BX。关闭边界：真实实现与 consumer 集成 + 固定 source/config + 必要 CPU receipt；设备/收益在对应批次另验。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX08", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "kv_pruning_compaction"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH34。

domain原子：representation:RH34；Lark source-first：。

<a id="cp08"></a>
### CP08 — 冷层一个codec encode→decode→kernel闭环

Owner：D/B/device；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：CP07、S08、R08；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: selected cold codec/backend (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: l2_transfer.py staging/decoder (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：authoritative tensor→encode→commit→selectiveread→decode真实候选。

完整DoD：RH11lossless逐byte与CacheGen有损quality分别，page/chunk/scratch生命周期；L3所选另L01/L02；不能bitstream假直接attention，SM/HBM/IObudget真消费。

可验证consumer：BX、F03。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R08", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "lossless_cold_codec"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH11；work/coverage/storage-article-requirements.md#EX08；work/coverage/engine-requirements.md#XR03。

domain原子：representation:RH11、storage:EX08、engine:XR03；Lark source-first：LARK-052。

<a id="l02"></a>
### L02 — 一个真实L3 adapter与发布/迁移

Owner：D/B；implementation；status：NOT_STARTED；scope：core。

前置：L01、E02、S05、S07、S08；原锚：T17。

实际模块/责任：MC719 mooncake-store/src/nvme_kv_backend.cpp::OffloadOne/root publish + real_client.cpp memory/disk/DFS read owner (storage S11/S12)；PROPOSED: one selected actual-device backend adapter on existing op/client contract; device ABI input L01。

固定产物：selectedbackend adapter/controller迁移候选。

完整DoD：真正targetcopy→commit/publish→source退，失败取消幂等保合法副本；partial恢复连续prefix/合法组件；有界staging与physicalcredits；不建tier平台

可验证consumer：L03、BC。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/representation-hardware-requirements.md#RH26；work/coverage/storage-article-requirements.md#SR12；work/coverage/router-control-requirements.md#R34；work/coverage/engine-requirements.md#XR12。

domain原子：representation:RH26、storage:SR12、router:R34、engine:XR12；Lark source-first：LARK-003、LARK-059。

<a id="r11"></a>
### R11 — L3 CPU/DPU/GPU发起与KVIO取舍

Owner：D/设备owner/B/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：L01、S08；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/representation-hardware-requirements.md#RH25; work/coverage/storage-article-requirements.md#EX10; work/coverage/storage-article-requirements.md#EX13; work/coverage/router-control-requirements.md#R27; no product implementation in this decision。

固定产物：12方向#11介质/queue/page聚合与发起路线decision。

完整DoD：CPUbatchbaseline、DPU命令内存、GPUIOkernelSM竞争；page共享粒度与physicalIO聚合扫描；end-to-endP99/CPUcycles-page/能耗/写放大，directDMA不免CPUcontrol成本；硬件无ABI保持unknown

可验证consumer：RD、F03。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/representation-hardware-requirements.md#RH25；work/coverage/storage-article-requirements.md#EX10；work/coverage/storage-article-requirements.md#EX13；work/coverage/router-control-requirements.md#R27。

domain原子：representation:RH25、storage:EX10、storage:EX13、router:R27；Lark source-first：LARK-060、LARK-061、LARK-062。

<a id="vv2"></a>
### VV2 — 同合同机器证据后的最终框架选择

Owner：框架/产品owner/H；decision；status：DECISION_REQUIRED；scope：research。

前置：BV、V06、A02；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/framework-version-requirements.md; work/coverage/framework-version-requirements.md#FW08; no product implementation in this decision。

固定产物：维持SG/切VL/收窄scope一次selection receipt。

完整DoD：FW08逐目标必需组合PASS/FAIL/UNKNOWN；bulkTTFT/ITL与radix/session/layer需求、同SLO成本和维护面积客观；sharedMCdrain缺口不能换框架假修；缺事实不裁胜负；选后唯一deepfork，Dynamo独立hostgate。

可验证consumer：RB、RD。关闭边界：Complete sourced decision/environment/candidate receipt, no implicit hardware authorization。

batch：formal_receipt；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/framework-version-requirements.md；work/coverage/framework-version-requirements.md#FW08。

domain原子：framework:FW08；Lark source-first：LARK-005。

<a id="ag04"></a>
### AG04 — 真实重复IO与single-flight取舍

Owner：B/H；decision；status：DECISION_REQUIRED；scope：research。

前置：E04、E05、S08；原锚：X02。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; work/coverage/representation-hardware-requirements.md#RH03; work/coverage/storage-article-requirements.md#EX03; work/coverage/router-control-requirements.md#R22; work/coverage/engine-requirements.md#XR05; no product implementation in this decision。

固定产物：sameprefix重复sourceIO measurement与decision。

完整DoD：native读后去重不冒singleflight；以deadline/hot争用/短prefix反例决定native足够no-change或实施；不凭逻辑key给physical折扣，未知保deferred

可验证consumer：AG05、R04。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/representation-hardware-requirements.md#RH03；work/coverage/storage-article-requirements.md#EX03；work/coverage/router-control-requirements.md#R22；work/coverage/engine-requirements.md#XR05。

domain原子：representation:RH03、storage:EX03、router:R22、engine:XR05；Lark source-first：LARK-036、LARK-085。

<a id="e06"></a>
### E06 — 唯一worker acquire/revoke authority

Owner：B/E/D；implementation；status：NOT_STARTED；scope：core。

前置：A03、E02、E04、E05、S05；原锚：T09。

实际模块/责任：SG946 unified_cache/storage_attachment.py::attach/detach/apply_runtime_config; cache_controller.py::stop (engine P12)；scheduler.py::is_fully_idle + real weight mutation/request/batch consumer (engine P12/EC18)；PROPOSED: same owner acquire/revoke/generation bridge; Gate A/B not ready。

固定产物：SG8唯一candidate acquire/begin-revoke/retire。

完整DoD：sameowner互斥；先禁新信用与真实pool读写/H2D/D2H，再drain oldproducer+consumer；host→H2D→request/batch/forward静默，oldwriteback保持binding；join/timeout/unknown拒reset/rebind；新generation仅全retire后commit

可验证consumer：Q03、Q04、BS。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR05；work/coverage/storage-article-requirements.md#SR07；work/coverage/storage-article-requirements.md#R03；work/coverage/router-control-requirements.md#R04；work/coverage/engine-requirements.md#EC15；work/coverage/engine-requirements.md#EC18；work/coverage/acceptance-evidence-requirements.md#operations_recovery_shutdown。

domain原子：storage:SR05、storage:SR07、storage:R03、router:R04、engine:EC15、engine:EC18、acceptance:operations_recovery_shutdown；Lark source-first：LARK-023、LARK-029、LARK-030、LARK-079。

<a id="e07"></a>
### E07 — 实际结果累计服务账与去重消费

Owner：B；implementation；status：NOT_STARTED；scope：core。

前置：E01、E05；原锚：T07/SG21 EC11 independent child。

实际模块/责任：SG946 managers/scheduler.py::run_batch；SG946 managers/scheduler_components/batch_result_processor.py::decode result/finish (engine P10/EC11)；PROPOSED: consumed actual-result dedup/cumulative charge hook at those real callers; no new unconsumed ledger。

固定产物：实际结果累计服务账与去重消费：固定 scope 与可审 receipt。

完整DoD：run_batch/batch_result_processor 实际 launched/committed/accepted decode/uncached prefill/retract recompute/abort waste 分开；重试不清历史、重复 result callback 不双计、overlap 两 iteration refs 独立、逻辑 cancel 不退已执行工作；原生 charge 优先，shared prefix 不计 uncached compute；token work 不冒精确 GPU-ns。实际反馈用于 worker/service 与 Router 预算，经济在冻结批校准。

可验证consumer：Q08、S08、AG03、BB、B00。关闭边界：真实实现与 consumer 集成 + 固定 source/config + 必要 CPU receipt；设备/收益在对应批次另验。

batch：BB；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/engine-requirements.md；work/coverage/storage-article-requirements.md#SR09；work/coverage/router-control-requirements.md#R35；work/coverage/router-control-requirements.md#R37；work/coverage/engine-requirements.md#EC07；work/coverage/engine-requirements.md#EC11；work/coverage/engine-requirements.md#EC17；work/coverage/acceptance-evidence-requirements.md#causal_trace_presence。

domain原子：storage:SR09、router:R35、router:R37、engine:EC07、engine:EC11、engine:EC17、acceptance:causal_trace_presence；Lark source-first：。

<a id="rx05"></a>
### RX05 — RL policy/训练推理共用资源合同取舍

Owner：训练/平台/B/E；research_decision；status：DECISION_REQUIRED；scope：research。

前置：A03、E05、S08；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/lark-requirements.md; work/coverage/representation-hardware-requirements.md#RH37; work/coverage/storage-article-requirements.md#EX12; work/coverage/router-control-requirements.md#R33; work/coverage/engine-requirements.md#XR11; no product implementation in this decision。

固定产物：RL policy/训练推理共用资源合同取舍的一次性完整receipt。

完整DoD：LARK039/040：相同policyrevision祖先共享，trajectorytail/环境state独立；weight更新新namespace、oldinflight按训练一致性drain/continue/cut决策；trainingstep HBM/IO非稳定可用L1，推理active/futuredecode/pin预算需资源管理层实际owner；optimizer/activation不归KV；真实业务是否需要共用先one-time决议，不假设已部署。

可验证consumer：RD、CP24。关闭边界：Source-backed disposition and explicit profile/owner/input/reopen/exit; unknown does not grant support。

batch：decision_scope_receipt；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/lark-requirements.md；work/coverage/representation-hardware-requirements.md#RH37；work/coverage/storage-article-requirements.md#EX12；work/coverage/router-control-requirements.md#R33；work/coverage/engine-requirements.md#XR11。

domain原子：representation:RH37、storage:EX12、router:R33、engine:XR11；Lark source-first：LARK-038、LARK-039、LARK-040。

<a id="cp15"></a>
### CP15 — RAG非prefixfusion/contextvariants实际consumer

Owner：retrieval/B/D/model；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：R09、CP07、E04、S08；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: selected RAG/model quality pipeline UNKNOWN_INPUT (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: selected selective recompute/attention adapter (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：retrievalchunk→positiontransform→selectiverecompute→attention→output。

完整DoD：RH15–18真实quality/原始顺序指令/位置合同；fullprefill/exactprefix强oracle；textsame非exact；有限contextvariant身份/dependency/cap/eviction、取消不误publish、合法fullrecompute拒路径；不得暗改retrievalorder或万能15%比例。quant联合误差仅选CP09后guard。

可验证consumer：BX。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R09", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "nonprefix_rag_selective_recompute"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH15；work/coverage/representation-hardware-requirements.md#RH16；work/coverage/representation-hardware-requirements.md#RH17；work/coverage/representation-hardware-requirements.md#RH18；work/coverage/storage-article-requirements.md#EX09；work/coverage/storage-article-requirements.md#R05；work/coverage/engine-requirements.md#XR04。

domain原子：representation:RH15、representation:RH16、representation:RH17、representation:RH18、storage:EX09、storage:R05、engine:XR04；Lark source-first：LARK-057、LARK-058。

<a id="l03"></a>
### L03 — L3 deadline队列与双粒度IO

Owner：D/B/设备owner；implementation；status：NOT_STARTED；scope：core。

前置：L02；原锚：T17。

实际模块/责任：MC719 nvme_kv_executor_io_uring.cpp queue/drain; nvme_kv_backend.cpp IndexQueue (storage S10)；PROPOSED: selected device executor physical aggregation/deadline consumer; GPUDirect only proven profile。

固定产物：逻辑page共享/淘汰+physicalpage/layer聚合consumer。

完整DoD：保持子集读和取消粒度；read/write/prefetch预算/queue-depth/priorityinherit限于依赖；CPU batching先基线，endpoint/NUMA/H2D争用与deviceGC/写放大计入 若 actual flash：GC/满盘 steady state、physical writes/unique KV/retry-replica bytes、WAF/wear/QD/read-write混合tail真实 telemetry；非flash wear轴 NA，能耗只用有来源 sensor与idle/dynamic boundary，不用 TDP充实测。

可验证consumer：L04、R11、BC。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/representation-hardware-requirements.md#RH26；work/coverage/storage-article-requirements.md#SR12；work/coverage/storage-article-requirements.md#SR16；work/coverage/storage-article-requirements.md#EX10；work/coverage/router-control-requirements.md#R34；work/coverage/engine-requirements.md#XR12。

domain原子：representation:RH26、storage:SR12、storage:SR16、storage:EX10、router:R34、engine:XR12；Lark source-first：LARK-004、LARK-017、LARK-018、LARK-060。

<a id="f03"></a>
### F03 — 融合3紧凑表示×价值收录×L3IO

Owner：B/D/设备/H；fusion_decision；status：DECISION_REQUIRED；scope：research。

前置：R03、R08、R11；原锚：G package映射。

实际模块/责任：component source scopes of referenced research decisions。

固定产物：codec/admission/IO聚合2×2交互disposition。

完整DoD：每路线恢复deadline内有效hit、quality、SM/HBM/controlCPU及flash成本；本机装下/解码贵反例；没有设备不可宣益，组合质量误差不相加

可验证consumer：RD。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/representation-hardware-requirements.md#RH14；work/coverage/representation-hardware-requirements.md#RH33。

domain原子：representation:RH14、representation:RH33；Lark source-first：LARK-069。

<a id="rx09"></a>
### RX09 — 模型原生跨层 KV/persistent replay 范围裁决

Owner：model/representation/kernel；research_decision；status：NOT_STARTED；scope：exploratory。

前置：V01、R10、R11；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/representation-hardware-requirements.md; work/coverage/representation-hardware-requirements.md#RH35; no product implementation in this decision。

固定产物：模型原生跨层 KV/persistent replay 范围裁决：固定 scope 与可审 receipt。

完整DoD：默认长期 deferred；DeepSeek V4/V4.1 native CSA/HCA/CSA2/global HBM/persistent host/SSD 与 generic cross-transformer operator fusion UNKNOWN 分开。选中真实模型后先全文 primary/code 核证，锁 layer alias lifecycle 与 SWA replay 合法 checkpoint，再决定 CP27。不能借 abstract 授实现支持。

可验证consumer：RD。关闭边界：一次 signed resolution：accepted/measured-no-change/deferred/rejected/unknown；accepted 必绑定实现与验收，unknown 不得关闭。

batch：decision_registry；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH35。

domain原子：representation:RH35；Lark source-first：。

<a id="r04"></a>
### R04 — prefixDAG/分组/sharedpage/Cascade取舍

Owner：B/E/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：AG04；原锚：X02。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; work/coverage/router-control-requirements.md#R24; no product implementation in this decision。

固定产物：12方向#4三种收益与kernel独立decision。

完整DoD：global祖先identity/COW/冷producer有界；存储副本、HBM页共享、attention读取计算分开；cohortdeadline/singleton、branch错位/短prefix反例；路由×kernel2×2

可验证consumer：RD、F02。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/router-control-requirements.md#R24。

domain原子：router:R24；Lark source-first：LARK-045。

<a id="ag05"></a>
### AG05 — 所选 bounded restore 单 leader/waiter consumer

Owner：B/SG actual restore IO/ref owner (reuse SG28); Router E demand summary only；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：AG04、E06；原锚：X02。

实际模块/责任：SG946 unified_radix_cache.py::prefetch_from_storage/_handle_prefetch_result/release_aborted_request (router R22/engine P2/P3/P5)；cache_controller.py actual read worker/ACK + host allocator；PROPOSED: existing-object restore leader/waiter physicalop/ref consumer only。

固定产物：一次源restore physicalop→合法hostresult→独立waiter恢复consumer；不含cold共同prefill计算生产。

完整DoD：仅accepted触发；每waiter独立cancel/服务/targetH2D/decode；最后waiter取消仍drain；producer失败/期限可重算不复活；sourceIO可共享但目标GPU物理分开 仅已存在compatible object的restore singleflight；不声称一次compute，cold prefill production归CP02。

可验证consumer：F01、F02、BE。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BE；hardware/input：candidate_close_does_not_authorize_device_or_activation。

执行guard：{"decision": "AG04", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "restore_singleflight"}。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/representation-hardware-requirements.md#RH03；work/coverage/storage-article-requirements.md#EX03；work/coverage/router-control-requirements.md#R22；work/coverage/engine-requirements.md#XR05。

domain原子：representation:RH03、storage:EX03、router:R22、engine:XR05；Lark source-first：LARK-036。

<a id="cp05"></a>
### CP05 — 公共prefix版本manifest与实际预计算发布

Owner：产品/B/D；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：R05、E06、S08；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: actual template/model publication repo UNKNOWN_INPUT (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: chosen engine native prefill/backend immutable PUT (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：renderedtokens→compute→sealedcommit→poolpublish→newworker恢复。

完整DoD：RH07–09权重/tokenizer/位置/template/tools/权限/生命周期manifest；新namespace失效drain、有界IO/byte-time预热、unused回收；no-prewarm/on-demand对照回本，跨租户明确允许。

可验证consumer：CP06、BX、F04。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R05", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "public_prefix_precompute"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH07；work/coverage/representation-hardware-requirements.md#RH08；work/coverage/storage-article-requirements.md#EX04；work/coverage/router-control-requirements.md#R29；work/coverage/engine-requirements.md#XR09。

domain原子：representation:RH07、representation:RH08、storage:EX04、router:R29、engine:XR09；Lark source-first：LARK-047。

<a id="q03"></a>
### Q03 — canonical身份登记与generation通知桥

Owner：E/B；implementation；status：NOT_STARTED；scope：core。

前置：Q02、S05、E06；原锚：T10。

实际模块/责任：Dynamo b83 SGLang registration/handler→DiscoverySpec::EventSource/list-watch→shared_cache；PROPOSED: SG authority notification producer, withdraw bridge (router R05)。

固定产物：register/EventSource/withdraw consumer。

完整DoD：actualmodel/layout/artifact/tenant/prefix/ABI与epoch；旧event source撤回后注册新source；diagnostic snapshot不能发credit；同pinned authority/present/group/view才能query

可验证consumer：Q04、Q05。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR07；work/coverage/router-control-requirements.md#R05。

domain原子：storage:SR07、router:R05；Lark source-first：LARK-031。

<a id="cp24"></a>
### CP24 — 所选RL/训练资源跨step执行接入

Owner：训练/平台/B；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX05、E06、E05、S08；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: actual RL rollout/training resource owner UNKNOWN_INPUT (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: SG mutation/quiescence (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: Dynamo context (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：所选RL/训练资源跨step执行接入的一次性完整receipt。

完整DoD：真实trainstep boundary→资源window→推理active/decode/io grant consumer；policyversion变更revoke/retire/newnamespace，forkprefix sealed/tail与环境state独立；training机会IO不能挤demand，暂停保留受控，越界typedreject；不接管optimizer或宣cache保存训练语义。

可验证consumer：BX。关闭边界：Accepted scope + real implementation/consumer integrated + necessary CPU H/J receipt; final support requires BX。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX05", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "selected_rl_rollout_or_training_colocation"}。

source refs：work/coverage/lark-requirements.md；work/coverage/representation-hardware-requirements.md#RH37；work/coverage/storage-article-requirements.md#EX12；work/coverage/router-control-requirements.md#R33；work/coverage/engine-requirements.md#XR11。

domain原子：representation:RH37、storage:EX12、router:R33、engine:XR11；Lark source-first：LARK-040。

<a id="cp16"></a>
### CP16 — L3逐层deadline及时恢复/format融合

Owner：B/D/devicekernel；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：R11、L03、E04；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: selected L3 executor/backend (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: l2_transfer.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: actual layer attention consumer (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：deadline→range/layerplan→IO/codec/H2D→fence→attention。

完整DoD：RH27/28整批立即/有界JIT/逐层对照；乱序不提前消费，wholefinish退source；criticalpath不doublecountoverlap；unpack/layout/scale融合仅已测瓶颈、实际scratchowner和质量oracle，非跨transformer层operatorfusion。codec/layout所选依CP08/CP10。

可验证consumer：BX、F03。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R11", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "l3_jit_layer_io"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH27；work/coverage/representation-hardware-requirements.md#RH28；work/coverage/storage-article-requirements.md#EX10；work/coverage/router-control-requirements.md#R27；work/coverage/engine-requirements.md#XR12。

domain原子：representation:RH27、representation:RH28、storage:EX10、router:R27、engine:XR12；Lark source-first：LARK-065。

<a id="l04"></a>
### L04 — L3分层预取/有限保留与write admission

Owner：B/D；implementation；status：NOT_STARTED；scope：core。

前置：L03；原锚：T17。

实际模块/责任：existing SG controller prefetch/backup and native Store offload/promotion consumer (storage S10/engine P11)；PROPOSED: finite deadline/prefetch/writeadmission consumer after selected device facts。

固定产物：L3→host→GPU需求/预测提示consumer。

完整DoD：预测返回先L3→L2，临近执行进L1；不全预热HBM；cancel未提交停止，submitted到drain；不写所有KV或每token扫全context；低价值可拒入L3 若 actual flash：GC/满盘 steady state、physical writes/unique KV/retry-replica bytes、WAF/wear/QD/read-write混合tail真实 telemetry；非flash wear轴 NA，能耗只用有来源 sensor与idle/dynamic boundary，不用 TDP充实测。

可验证consumer：R02、F01、F03、BC。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR12；work/coverage/storage-article-requirements.md#SR16；work/coverage/router-control-requirements.md#R31；work/coverage/router-control-requirements.md#R34；work/coverage/engine-requirements.md#AG06；work/coverage/engine-requirements.md#XR12。

domain原子：storage:SR12、storage:SR16、router:R31、router:R34、engine:AG06、engine:XR12；Lark source-first：LARK-042、LARK-061。

<a id="cp27"></a>
### CP27 — 所选模型原生跨层 persistent replay

Owner：model/representation/kernel；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX09、CP11、L02；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: selected-model native persistent/global/SWA cache (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: selected L3 adapter (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：所选模型原生跨层 persistent replay：固定 scope 与可审 receipt。

完整DoD：checkpoint→tier→bounded replay→实际模型 output；layer alias/lifetime、global/persistent state ABI、SWA legalboundary/缺 state/version 真实 oracle；GPU质量与实际设备成本；generic operator fusion 不在此包自动 accepted。

可验证consumer：BX。关闭边界：真实实现与 consumer 集成 + 固定 source/config + 必要 CPU receipt；设备/收益在对应批次另验。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX09", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "model_native_persistent_crosslayer_replay"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH35。

domain原子：representation:RH35；Lark source-first：。

<a id="cp01"></a>
### CP01 — 祖先DAG/共享页可消费合同

Owner：B/D；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：R04、S05、E04；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: sglang/srt/mem_cache/unified_cache/components/full.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: sglang/srt/mem_cache/unified_radix_cache.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: memory_pool.py native allocator (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：globalancestor/sealedpage/COW/ref/pin真实consumer。

完整DoD：RH02同suffix异历史拒；实际物理共享bytes与独立tail/targetH2D/decode分开；source与consumerfence不合并。

可验证consumer：CP02、CP03。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R04", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "prefix_dag_shared_page"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH02；work/coverage/engine-requirements.md#AG05。

domain原子：representation:RH02、engine:AG05；Lark source-first：LARK-039。

<a id="f02"></a>
### F02 — 融合2DAG×分组×sharedpage×Cascade

Owner：B/E/H；fusion_decision；status：DECISION_REQUIRED；scope：research。

前置：R04；原锚：G package映射。

实际模块/责任：component source scopes of referenced research decisions。

固定产物：路由×kernel及三capacity收益disposition。

完整DoD：有界cohort与singleton保护；branch数/共享比/到达错位扫描；存储/HBM/kernel贡献分开、groupwait和hotspot代价；最优化pagedkernel强对照

可验证consumer：RD。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/representation-hardware-requirements.md#RH06；work/coverage/representation-hardware-requirements.md#RH33。

domain原子：representation:RH06、representation:RH33；Lark source-first：LARK-046、LARK-069。

<a id="q04"></a>
### Q04 — namespace与完整object query/event parity

Owner：E/B/D；implementation；status：NOT_STARTED；scope：core。

前置：Q03；原锚：T10。

实际模块/责任：Dynamo b83 shared_cache.rs::expand_actual_query_keys/check_blocks；SG946 mooncake_store.py::_tag_keys/config_prefix/storage_namespace_seed actual key oracle (engine P14/router R06/R07)；PROPOSED: exact N/K producer→index→query binding; namespace never grants Store quota。

固定产物：N/K真实producer→index→query候选。

完整DoD：SG实际PUT/GET完整K/V/TP/PP components向量被Rust生产apply/query消费；N合法同域正例/跨域拒；K逐bytes一致；删除/expiry/gap/revoke先失credit；不去salt

可验证consumer：Q05、Q06、BS。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/framework-version-requirements.md#FW15；work/coverage/storage-article-requirements.md#SR07；work/coverage/router-control-requirements.md#R06；work/coverage/router-control-requirements.md#R07。

domain原子：framework:FW15、storage:SR07、router:R06、router:R07；Lark source-first：LARK-027。

<a id="r06"></a>
### R06 — 弹性扩缩容与会话连续性取舍

Owner：B/D/E；research_decision；status：DECISION_REQUIRED；scope：research。

前置：E06、Q03；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/storage-article-requirements.md#EX05; work/coverage/router-control-requirements.md#R32; work/coverage/engine-requirements.md#XR10; no product implementation in this decision。

固定产物：12方向#6独立Store/scale-out/in/upgrade恢复decision。

完整DoD：停新admission→drain→poolcommitted保留→旧epoch撤；热点预热有界且无需全迁移；非KV业务/RNG/output状态不能仅KV宣恢复；突发/元数据HA/OpLog成熟度与故障范围

可验证consumer：RD、F04。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/storage-article-requirements.md#EX05；work/coverage/router-control-requirements.md#R32；work/coverage/engine-requirements.md#XR10。

domain原子：storage:EX05、router:R32、engine:XR10；Lark source-first：LARK-048。

<a id="q05"></a>
### Q05 — group验证与bounded目录恢复

Owner：E/D；implementation；status：NOT_STARTED；scope：core。

前置：Q04；原锚：T10。

实际模块/责任：Dynamo b83 shared_cache.rs::check_blocks/apply_batch/subscriber；Store group_id verification + all-object path; actual snapshot/watermark contract input (router R08/R09)；PROPOSED: bounded shared-index repair only once real source API is fixed。

固定产物：独立G fastpath与source reconcile。

完整DoD：首scope group shortcut关，allobject可用；G启用须真实taggedlogicalkey/tenant/group完整性等于fallback，groupmiss仅失fastpath；sharedset无snapshot/cursor保持uncertain，不伪造workerindex能力；真实后端cursor/限额reconcileconsumer 实际 snapshot/cursor repair 支持边界固定，scale envelope 超出显式 unsupported；测 event repair 与 lookup CPU/tail/lease占用，不自行编 replay。

可验证consumer：Q06、BB、BS。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR07；work/coverage/storage-article-requirements.md#SR15；work/coverage/storage-article-requirements.md#EX06；work/coverage/router-control-requirements.md#R08；work/coverage/router-control-requirements.md#R09。

domain原子：storage:SR07、storage:SR15、storage:EX06、router:R08、router:R09；Lark source-first：LARK-027、LARK-031、LARK-049。

<a id="cp06"></a>
### CP06 — 弹性退役/新实例有限预热

Owner：部署/B/D/E；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：R06、E06、Q03、S07；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: actual deployment/autoscale hooks UNKNOWN_INPUT (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: sglang storage_attachment.py/scheduler.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: Dynamo discovery (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: Mooncake segment lifecycle (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：scaleout/in/upgrade真实consumer。

完整DoD：RH21+R06停admit/drain/撤epoch/poolcommitted，贡献nodeowner失效/HA-oplog合同；适用prewarm另依CP05，layout变更另依CP10；不全迁移、不仅KV承诺RNG/tool/live-stream连续性，恢复突发budget。

可验证consumer：BX、F04。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R06", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "elastic_cache_continuity"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH21；work/coverage/storage-article-requirements.md#EX05；work/coverage/router-control-requirements.md#R32；work/coverage/engine-requirements.md#XR10。

domain原子：representation:RH21、storage:EX05、router:R32、engine:XR10；Lark source-first：LARK-048。

<a id="bs"></a>
### BS — MC3/SG8/Dynamo1物理activation必需轴

Owner：H/J/原owner；hard_gate；status：NOT_STARTED；scope：hardware。

前置：S02、E06、Q04、Q05、BA；原锚：parents。

实际模块/责任：work/implementation/validation/acceptance evidence；selected framework/backend real consumer and existing replay assets。

固定产物：physical Gate A/B / event / identity / consumer device receipt。

完整DoD：保留原MC3←MC1/MC2、Dynamo1←SG7/SG8 native关系；候选CLOSED不授ACTIVE/event/positivecredit。先验证本批启用所需真实physical acquire/退役/Store+TE最后访问、N/K/G多rank/worker/gap gate；receipt仅放行批准scope实验，不称原parent全部AC已关闭。原parent最终AC由PH依据完整功能批结果roll-up。

可验证consumer：BB、RB。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：explicit_decision_or_audit_receipt；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR07；work/coverage/router-control-requirements.md#R04。

domain原子：storage:SR07、router:R04；Lark source-first：LARK-029、LARK-083。

<a id="q06"></a>
### Q06 — Router预测ticket与attempt反馈校正

Owner：E/B；implementation；status：NOT_STARTED；scope：core。

前置：Q04、Q05、E05、E06；原锚：T11。

实际模块/责任：Dynamo b83 routing_host/kv.rs::dispatch_selection/request_guard.rs；Actor::book_and_respond/free_if_booking, cancellation.rs/migration (router R13/R14)；PROPOSED: worker typed receipt→unique AttemptId booking consumer。

固定产物：dispatch/guard/Actor/lease boundedticket候选。

完整DoD：engine最后admissionauthority；只退对应attempt booking；miss/partial/revoke/cancel/old或乱序receipt幂等；placement不减硬IO/HBM/decode；503不默认retry，stream后不重采样

可验证consumer：Q07、Q08、BB。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/router-control-requirements.md#R13；work/coverage/router-control-requirements.md#R14；work/coverage/router-control-requirements.md#R15。

domain原子：router:R13、router:R14、router:R15；Lark source-first：LARK-009、LARK-019、LARK-020、LARK-032、LARK-033。

<a id="r07"></a>
### R07 — 全局索引/批量匹配/多租户运营扩展

Owner：E/D/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：Q05；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/storage-article-requirements.md#SR15; work/coverage/storage-article-requirements.md#EX06; work/coverage/router-control-requirements.md#R10; no product implementation in this decision。

固定产物：12方向#7对象数/控制CPU/租户cacheSLO decision。

完整DoD：batchLPM/摘要/分片/前端hash减重复rank工作；查询授lease与actualread/consumed分开；小对象元数据CPU、quota/pin/TTL/服务公平、gap/restart/deletion故障；不以更多微服务代替需求 锁 metadata bounded scale envelope：真实 page/object/tenant/fanout/eventrate，query/put/event CPU/memory/tail/lease占用；1024 in-memory shards 非1024 distributed Master；gap/reconnect/source restart 零信用到可证恢复，hotroute不阻塞跨集群lookup。

可验证consumer：RD、F04。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/storage-article-requirements.md#SR15；work/coverage/storage-article-requirements.md#EX06；work/coverage/router-control-requirements.md#R10。

domain原子：storage:SR15、storage:EX06、router:R10；Lark source-first：LARK-025、LARK-049。

<a id="rx07"></a>
### RX07 — Master HA/metadata OpLog与故障运营scope

Owner：D/部署/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：R06、S07、Q05；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/lark-requirements.md; work/coverage/representation-hardware-requirements.md#RH36; work/coverage/storage-article-requirements.md#SR13; work/coverage/storage-article-requirements.md#U04; work/coverage/acceptance-evidence-requirements.md#operations_recovery_shutdown; no product implementation in this decision。

固定产物：Master HA/metadata OpLog与故障运营scope的一次性完整receipt。

完整DoD：LARK050：固定部署HA/OpLog/元数据恢复/存储owner寿命成熟度；source tokens/weights权威持久性和best-effortcache分开；failover/lease失效/indexgap/fault正确失败或可恢复；承诺的恢复SLO未知保持gate；独立failurematrixconsumer，不把多副本当数据永不失。 明确 single-master safe-miss/recompute 或 native HA，RTO/RPO 来源未给保持 unknown；选举不等 durable metadata restore，DFS allocator 未证继续 reject；old lease/softpin/endpoint 不授持续保护。

可验证consumer：RD、CP19。关闭边界：Source-backed disposition and explicit profile/owner/input/reopen/exit; unknown does not grant support。

batch：decision_scope_receipt；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/lark-requirements.md；work/coverage/representation-hardware-requirements.md#RH36；work/coverage/storage-article-requirements.md#SR13；work/coverage/storage-article-requirements.md#U04；work/coverage/acceptance-evidence-requirements.md#operations_recovery_shutdown。

domain原子：representation:RH36、storage:SR13、storage:U04、acceptance:operations_recovery_shutdown；Lark source-first：LARK-050。

<a id="q07"></a>
### Q07 — 恢复vs重算预测与负反馈consumer

Owner：E/B/D；implementation；status：NOT_STARTED；scope：core。

前置：Q06；原锚：T12。

实际模块/责任：Dynamo b83 native local filter/scorer/picker + replica_sync.rs/ActiveSequenceEvents feedback；PROPOSED: unit/profile/age/confidence cost calibration consumer and bounded correction (router R15/R18/R19)。

固定产物：scorer本地cost/profile+actualinterval校准候选。

完整DoD：明确单位/version/profile/generation/age/置信度；UNKNOWN保守；关键路径含queue/lookup/IO/H2D/transform/residualcompute，boundedhysteresis；无跨集群热lookup；prediction不是经济PASS

可验证consumer：Q08、R01、BB。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/router-control-requirements.md#R15；work/coverage/router-control-requirements.md#R18；work/coverage/router-control-requirements.md#R19；work/coverage/engine-requirements.md#EC13。

domain原子：router:R15、router:R18、router:R19、engine:EC13；Lark source-first：LARK-010、LARK-012、LARK-034、LARK-068。

<a id="f04"></a>
### F04 — 融合4身份×预热×索引×弹性

Owner：B/E/D/H；fusion_decision；status：DECISION_REQUIRED；scope：research。

前置：R05、R06、R07、R10；原锚：G package映射。

实际模块/责任：component source scopes of referenced research decisions。

固定产物：缓存运营成本/版本失效/弹性恢复disposition。

完整DoD：模型权威身份→newnamespace→有限prewarm→directoryready→scaleevent；pin/capacity/restore预算、versionchurn/warm-unused/indexCPU；原生足够、accept或defer均附触发

可验证consumer：RD。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/representation-hardware-requirements.md#RH09；work/coverage/representation-hardware-requirements.md#RH33。

domain原子：representation:RH09、representation:RH33；Lark source-first：LARK-069。

<a id="cp19"></a>
### CP19 — 所选HA/OpLog实际部署与恢复消费者

Owner：D/部署；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX07、S07、Q05；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: Mooncake native HA/OpLog/segment registry (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: Client leader discovery (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: Dynamo event recovery (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：所选HA/OpLog实际部署与恢复消费者的一次性完整receipt。

完整DoD：按RX07接受scope配置真实Master HA/OpLog/存量snapshot与boundedreconcile；leader失效/恢复、metadata一致性、旧owner停止/lease边界、目录credit恢复、payload正确或typedmiss重算；部署时budget/shutdown/容量再用；不建第二元数据authority/强事务框架。 failover/catchup/durableprefix→实际 query/GET→目录撤信用/冷 recompute→GPU消费；metadata/data owner分别故障，actual quota/capacity 与 old producer 不误读；无 HA 时真实 cold rebuild/recompute 路径也需 receipt。

可验证consumer：BX。关闭边界：Accepted scope + real implementation/consumer integrated + necessary CPU H/J receipt; final support requires BX。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX07", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "selected_ha_or_safe_miss_recovery"}。

source refs：work/coverage/lark-requirements.md；work/coverage/representation-hardware-requirements.md#RH36；work/coverage/storage-article-requirements.md#SR13。

domain原子：representation:RH36、storage:SR13；Lark source-first：LARK-050。

<a id="s09"></a>
### S09 — 部署 actual replica/故障域与 cache-loss 合同

Owner：D/部署；decision；status：NOT_STARTED；scope：core。

前置：S07、RX07；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/storage-article-requirements.md; work/coverage/storage-article-requirements.md#SR14; work/coverage/storage-article-requirements.md#U04; work/coverage/acceptance-evidence-requirements.md#operations_recovery_shutdown; no product implementation in this decision。

固定产物：部署 actual replica/故障域与 cache-loss 合同：固定 scope 与可审 receipt。

完整DoD：一次锁每 profile 最低 actual copies、best-effort 降级/cold fallback、segment-to-host failure-domain、吞吐 vs 容灾副本目标。原生 replica 能力先复用，未给拓扑/可用性不填假值；硬 continuity 才绑定 CP28；不把网络充足视为故障域已知。

可验证consumer：S07、CP28、RB。关闭边界：真实实现与 consumer 集成 + 固定 source/config + 必要 CPU receipt；设备/收益在对应批次另验。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/storage-article-requirements.md；work/coverage/storage-article-requirements.md#SR14；work/coverage/storage-article-requirements.md#U04；work/coverage/acceptance-evidence-requirements.md#operations_recovery_shutdown。

domain原子：storage:SR14、storage:U04、acceptance:operations_recovery_shutdown；Lark source-first：。

<a id="cp20"></a>
### CP20 — 所选价值收录/晋升/副本最小policy

Owner：D/B；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：R03、S07、S08、Q07；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: Mooncake native placement/admission/eviction (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: SG bounded retention policy (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：所选价值收录/晋升/副本最小policy的一次性完整receipt。

完整DoD：R03真测LRU不足才选：是否录入/层/提升/replica四个实际hook，value单位/ancestor依赖与canonicalobject；no-use/失败/取消仍计成本；有界统计/scoreCPU和pinbyte-time、LRU强baseline；物理副本去重与各GPUtarget独立；不足则有据reject复杂算法。

可验证consumer：BX、F03。关闭边界：Accepted scope + real implementation/consumer integrated + necessary CPU H/J receipt; final support requires BX。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R03", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "value_admission_eviction"}。

source refs：work/coverage/lark-requirements.md；work/coverage/storage-article-requirements.md#EX01；work/coverage/router-control-requirements.md#R25。

domain原子：storage:EX01、router:R25；Lark source-first：LARK-041。

<a id="q08"></a>
### Q08 — 原生队列租户公平/aging与有界亲和

Owner：E/B/C；implementation；status：NOT_STARTED；scope：core。

前置：A01、E05、Q06、Q07、E07；原锚：T13。

实际模块/责任：Dynamo b83 policy_queue.rs/queue.rs Actor/DRR frozen charge + worker lanes；SG946 schedule_policy.py/PrefillAdder; batch_result_processor actual service (engine P8/P10/router R16/R37)；PROPOSED: bounded tenant/class/cold progress policy at original consumers。

固定产物：DRR/Actor/selector真实policyconsumer。

完整DoD：approved权益与热度分开；cold正服务/可运行容量份额、longdecode进展、hot burst/affinity cap/aging/deadline/超载typed拒绝；ordinary无hint完整；requeue/cancel不重复charge

可验证consumer：S08、AG01、BB。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BA/BB/BC_by_selected_scope；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR09；work/coverage/router-control-requirements.md#R11；work/coverage/router-control-requirements.md#R16；work/coverage/router-control-requirements.md#R19；work/coverage/engine-requirements.md#EC09。

domain原子：storage:SR09、router:R11、router:R16、router:R19、engine:EC09；Lark source-first：LARK-001、LARK-011、LARK-016、LARK-020、LARK-032。

<a id="r01"></a>
### R01 — 投入价值与恢复/计算联合调度取舍

Owner：E/B/H/产品；research_decision；status：DECISION_REQUIRED；scope：research。

前置：Q07、A02；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/router-control-requirements.md#R19; no product implementation in this decision。

固定产物：12方向#1 evidence/strongbaseline/否证决策。

完整DoD：同SLO成本/完成任务、decode主成本/无重复/本机已覆盖反例；pool+route+admission增量，网络保障仍量endpoint争用；选simpleheuristic，复杂learner后置

可验证consumer：RD、F01。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/router-control-requirements.md#R19。

domain原子：router:R19；Lark source-first：LARK-002、LARK-004、LARK-007、LARK-008、LARK-010、LARK-034、LARK-070、LARK-086。

<a id="rx03"></a>
### RX03 — 快路由/慢replica双反馈稳定性

Owner：E/D/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：Q07、S07；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/router-control-requirements.md#R15; work/coverage/router-control-requirements.md#R26; work/coverage/engine-requirements.md#XR14; no product implementation in this decision。

固定产物：EWMA/hysteresis/minresidence/migrationcap决策。

完整DoD：新replica真实complete才ready；preble/cacheroutechurn/rewarmdip；breakstickiness后不被下游score再绑；offsticky/oscillation/迁移bytes完整consumer与同资源对照

可验证consumer：RD。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/router-control-requirements.md#R15；work/coverage/router-control-requirements.md#R26；work/coverage/engine-requirements.md#XR14。

domain原子：router:R15、router:R26、engine:XR14；Lark source-first：LARK-043、LARK-066。

<a id="rx04"></a>
### RX04 — cache-awarePD/CP与pool→decode完整状态

Owner：B/F/E/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：V02、Q07、R10；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/representation-hardware-requirements.md#RH29; work/coverage/engine-requirements.md#XR08; no product implementation in this decision。

固定产物：nativePD/固定CP池及动态splitmerge边界决策。

完整DoD：残余suffix仍attention历史；PDbootstrap/metadata/firsttokenlogits/sampling不因KV全hit消失；VertumnusRTP-LLMprefill限定、decode独立；固定CPpool先，转换/GPUtime/goodput计价，不首vertical强依赖

可验证consumer：RD。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/representation-hardware-requirements.md#RH29；work/coverage/engine-requirements.md#XR08。

domain原子：representation:RH29、engine:XR08；Lark source-first：LARK-067。

<a id="cp28"></a>
### CP28 — 所选故障域副本与实际读降级

Owner：D/Mooncake/部署；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：S09、S07、E02；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: Mooncake Master allocator/replica/placement (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: Mooncake Client GET replica selection (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：所选故障域副本与实际读降级：固定 scope 与可审 receipt。

完整DoD：仅硬可用性要求时实现 native domain-aware placement 缺口；partial allocation/actual report/quota、COPY/MOVE target publish 后退 source、owner lost + hot reader/writer 竞争正确数据或 typed miss；unique capacity/copy bytes 实测，actual target output 消费完整。

可验证consumer：BX。关闭边界：真实实现与 consumer 集成 + 固定 source/config + 必要 CPU receipt；设备/收益在对应批次另验。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "S09", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "hard_failure_domain_replica"}。

source refs：work/coverage/storage-article-requirements.md；work/coverage/storage-article-requirements.md#SR14。

domain原子：storage:SR14；Lark source-first：。

<a id="ag01"></a>
### AG01 — Agent原生保留/前缀机会与承诺边界

Owner：B/试点产品/H；decision；status：DECISION_REQUIRED；scope：research。

前置：Q08、S08；原锚：X01。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; work/coverage/storage-article-requirements.md#EX02; work/coverage/router-control-requirements.md#R30; work/coverage/engine-requirements.md#AG01; no product implementation in this decision。

固定产物：真实toolgap/tokenrewrite/branch保留机会与promise decision。

完整DoD：跨轮/子agent祖先/公共prefix分开；append/rewrite/compact失效；best-effort与有预算恢复承诺选定；原生足够须measuredno-change，未知TTL留gate；不随C通过自动完成

可验证consumer：AG02、R02、R04。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#EX02；work/coverage/router-control-requirements.md#R30；work/coverage/engine-requirements.md#AG01。

domain原子：storage:EX02、router:R30、engine:AG01；Lark source-first：LARK-001、LARK-037、LARK-072、LARK-085。

<a id="bb"></a>
### BB — B共享目录/公共混流/调度/L2完整批

Owner：H/J；acceptance；status：NOT_STARTED；scope：hardware。

前置：BA、B00、Q08、S08、BS、E07；原锚：T18.B。

实际模块/责任：REUSE_SUPPORTING_ASSETS: actual production consumer integration/freeze defined in this package + H existing acceptance contract; no tool-only platform。

固定产物：真实tenant×class×cold/hot/context/output性能/故障receipt。

完整DoD：普通/Agent独跑+代表混比+突发；cold长decode/slowtenant P95/P99/oldest-age/offered拒绝timeout；pool/local同DRAM/route/admission/IO消融、actualrestoredconsumed、pin/replica/waste成本；A02不齐经济NOT_EVALUATED

可验证consumer：BC、RB、R01、F01、F04。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：T18.B；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR11；work/coverage/storage-article-requirements.md#R01；work/coverage/router-control-requirements.md#R36；work/coverage/engine-requirements.md#EC20；work/coverage/acceptance-evidence-requirements.md#freeze_batch；work/coverage/acceptance-evidence-requirements.md#six_path_oracles；work/coverage/acceptance-evidence-requirements.md#economics_denominators。

domain原子：storage:SR11、storage:R01、router:R36、engine:EC20、acceptance:freeze_batch、acceptance:six_path_oracles、acceptance:economics_denominators；Lark source-first：LARK-001、LARK-002、LARK-008、LARK-016、LARK-021、LARK-068、LARK-069、LARK-070、LARK-071、LARK-072、LARK-075、LARK-076、LARK-084。

<a id="cp02"></a>
### CP02 — 有界cold公共prefill producer

Owner：B/selected engine common-prefill producer; Router E supplies bounded queued demand；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：CP01、Q08、AG04；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: sglang/srt/managers/scheduler.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: unified_radix_cache.py prefix commit (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：一个有期限cold common-prefix prefill compute producer→sealedprefix commit→siblings合法复用。

完整DoD：RH03真实原队列producer/waiterdeadline、failure/retry/取消/drain，独立计算强对照；source单次与每GPUtarget预算分开；globalproducer仅accepted需。 本包只去重cold共同prefill计算；已存在对象的once-restore/GET聚合属AG05，不能用restore leader覆盖compute producer。

可验证consumer：CP03。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R04", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "cold_common_prefill_pioneer"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH03；work/coverage/router-control-requirements.md#R21。

domain原子：representation:RH03、router:R21；Lark source-first：LARK-036。

<a id="rx01"></a>
### RX01 — pending需求图/producer优先取舍

Owner：E/B/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：Q08、AG04；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/router-control-requirements.md#R20; work/coverage/engine-requirements.md#XR06; no product implementation in this decision。

固定产物：pendingprefix→count/deadline/cohort/eviction决策。

完整DoD：PEEKqueued-demand与FCFS/LPM/仅eviction强对照；cancel/dequeue即减计数；低共享短queue保持native，不人为delay低负载；producer/ancestor计算价值只计一次

可验证consumer：RD、F02。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/router-control-requirements.md#R20；work/coverage/engine-requirements.md#XR06。

domain原子：router:R20、engine:XR06；Lark source-first：LARK-044。

<a id="rx02"></a>
### RX02 — 服务计量/有限hedging/成本感知retraction独立子能力决策

Owner：E/B/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：Q08、Q07；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/engine-requirements.md#EC12; work/coverage/engine-requirements.md#XR14; no product implementation in this decision。

固定产物：token/GPUwork/restoreservice/byte-time与hedging决策。

完整DoD：先少量权益/硬额度；DRF/learner非首must；满载双跑否证，只有independentspare+deadline风险触发私有target/op；输家drain且计失败取消工作；live流重采样拒绝 EC12独立cost_aware_victim_retraction selector：已有native length/ratio/cadence/retract机制先复用，针对真实OOM/prioritypreempt一次判现有victim足够、measured-no-change/deferred或窄selected修改；不是HRRN估价修复就算victim决策实现。victim恢复状态、已执行服务/re-prefill、copy/延期成本及longdecode ITL/goodput/totalwaste统一同shape native comparator；NULL retract不是便宜KV pause；input_embeds/beam/lastrequest/backup耗尽安全失败。没数据签defer+触发，不每decode token引入新公平抢占；accepted仅绑定CP23该子consumer。

可验证consumer：RD。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/engine-requirements.md#EC12；work/coverage/engine-requirements.md#XR14。

domain原子：engine:EC12、engine:XR14；Lark source-first：LARK-035、LARK-086。

<a id="cp22"></a>
### CP22 — 所选慢replica与快路由稳定反馈

Owner：E/D/B；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX03、S07、Q07；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: Mooncake copy/move/placement (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: Dynamo local scoring/negative feedback (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：所选慢replica与快路由稳定反馈的一次性完整receipt。

完整DoD：EWMA/hysteresis/minresidence/periodmigrationbytes批准后实际placement/scoreconsumer；newcopycomplete才ready、oldnewoverlap有额度；过载破亲和唯一裁决，不多环各纠同request；churn/rewarmdip/offsticky/oscillation取消/失败计价。

可验证consumer：BX、F04。关闭边界：Accepted scope + real implementation/consumer integrated + necessary CPU H/J receipt; final support requires BX。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX03", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "slow_replica_fast_route_control"}。

source refs：work/coverage/lark-requirements.md；work/coverage/router-control-requirements.md#R26；work/coverage/engine-requirements.md#XR14。

domain原子：router:R26、engine:XR14；Lark source-first：LARK-043、LARK-066。

<a id="cp12"></a>
### CP12 — 实际PD pool→D/首token/增长写回

Owner：B/F/PDowner；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX04、V04、E02、S05；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: disaggregation/decode_hicache_mixin.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: disaggregation/decode.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: decode_kvcache_offload_manager.py (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：nativePDdelta/receiver/offload首token完整consumer。

完整DoD：FW11确认生产PD必需则必须执行而非强改非PD：bootstrap/metadata/logits/sampling/params、prefix+delta、decodegrowth/tail下一轮消费、retract/cancel/late/rank释放；activeoffload不冒GPU页free，queue+jobpin计入。

可验证consumer：CP13、BX。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX04", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "native_pd_cache_path"}。

source refs：work/coverage/framework-version-requirements.md；work/coverage/framework-version-requirements.md#FW11；work/coverage/engine-requirements.md#AG07；work/coverage/engine-requirements.md#XR08。

domain原子：framework:FW11、engine:AG07、engine:XR08；Lark source-first：LARK-067。

<a id="cp17"></a>
### CP17 — 固定CPworker策略及被选split/merge

Owner：E/B/parallelowner；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX04、Q07、Q08、R10；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: actual parallel placement/control owner UNKNOWN_INPUT (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: selected TP/layout handoff (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：residualqueue/cache/GPUtime-awareCP实际consumer。

完整DoD：RH29先fixedCPselection，再decision接受动态才epoch/rankACK/drain/replica splitmerge；layout变化依CP10；cold/高hit短suffix/TPOT/GPUcost，不搬RTP-LLM参数或64GPU收益，decode独立。 route×reconfigure×cache 三因子完整消融；全适应时间含 observe/decision/drain/switch/cachefill/TTFT recovery；out-of-time regret/βλwindow sensitivity/hotshift/shortburst；source pin/partial replica/old epoch faults；request 与 token weighted SLO、length bucket公平均报。

可验证consumer：BX、F04。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX04", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "cache_aware_cp_reconfiguration"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH29；work/coverage/engine-requirements.md#XR08。

domain原子：representation:RH29、engine:XR08；Lark source-first：LARK-067。

<a id="ag02"></a>
### AG02 — pause/return/final与有限retention

Owner：B/产品；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：AG01、Q02、E05、S08；原锚：X01。

实际模块/责任：SG946 unified_cache/components/full.py session_ref/match/finish (engine P1)；SG actual request pause/return/final producer input; URC backup/retention consumer；PROPOSED conditional: finite chosen retention policy; active permit released between turns。

固定产物：session_ref/match/finish/eviction真实consumer。

完整DoD：仅AG01 accepted触发；toolwait无executionpermit；L1soft/L2lease/L3retention不同；final/cancel主动解除hint；短wait两搬运否证；program服务+IO+byte-time不因newrequest重置

可验证consumer：AG03、F01、BE。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BE；hardware/input：candidate_close_does_not_authorize_device_or_activation。

执行guard：{"decision": "AG01", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "finite_session_retention"}。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#EX02；work/coverage/router-control-requirements.md#R30；work/coverage/engine-requirements.md#AG02；work/coverage/engine-requirements.md#AG03；work/coverage/engine-requirements.md#AG08。

domain原子：storage:EX02、router:R30、engine:AG02、engine:AG03、engine:AG08；Lark source-first：LARK-037。

<a id="r02"></a>
### R02 — 生命周期预测与及时提升取舍

Owner：B/产品/H；research_decision；status：DECISION_REQUIRED；scope：research。

前置：AG01；原锚：X01。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/cache-execution-program.md; work/coverage/router-control-requirements.md#R31; no product implementation in this decision。

固定产物：12方向#2无信号/固定TTL/业务事件/预测事件对照decision。

完整DoD：预计return/slack、短wait往返、误预取和同步resume突发；承诺与best-effort分开；缺真实trace保持decisionrequired，不造TTL

可验证consumer：RD、F01。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/router-control-requirements.md#R31。

domain原子：router:R31；Lark source-first：LARK-037、LARK-065。

<a id="rx06"></a>
### RX06 — 公共ContextCache API/权益承诺取舍

Owner：产品/gateway/B/D；research_decision；status：DECISION_REQUIRED；scope：research。

前置：A01、AG01、R07；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/lark-requirements.md; no product implementation in this decision。

固定产物：公共ContextCache API/权益承诺取舍的一次性完整receipt。

完整DoD：LARK051：public/private share domain、contexthandle/TTL/pinquota、源tokens权威记录与cacheloss重算、计费单位与用户受益/physical副本两账；best-effort/预算恢复承诺明确；产品入口新API仅实际需求接受后，hash存在不授权，续租/删除/expired/撤权完整scope，不自动暴露privilegedtenant。

可验证consumer：RD、CP25。关闭边界：Source-backed disposition and explicit profile/owner/input/reopen/exit; unknown does not grant support。

batch：decision_scope_receipt；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/lark-requirements.md。

domain原子：；Lark source-first：LARK-051。

<a id="bc"></a>
### BC — C真实专用L3完整批

Owner：H/J/设备owner；acceptance；status：NOT_STARTED；scope：hardware。

前置：BB、L04、B00；原锚：T18.C。

实际模块/责任：REUSE_SUPPORTING_ASSETS: actual production consumer integration/freeze defined in this package + H existing acceptance contract; no tool-only platform。

固定产物：devicefault/reset/shutdown/迁移/读写预取消融receipt。

完整DoD：ABI真实driver，L3→host→GPU、source-target容量与再用、介质写放大/寿命、P99mixed读写/同步恢复；fake不授support；A02不齐只资源单位比较 若 actual flash：GC/满盘 steady state、physical writes/unique KV/retry-replica bytes、WAF/wear/QD/read-write混合tail真实 telemetry；非flash wear轴 NA，能耗只用有来源 sensor与idle/dynamic boundary，不用 TDP充实测。

可验证consumer：RB、F03。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：T18.C；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/storage-article-requirements.md#SR11；work/coverage/storage-article-requirements.md#SR16；work/coverage/storage-article-requirements.md#EX13；work/coverage/router-control-requirements.md#R36；work/coverage/engine-requirements.md#EC20；work/coverage/acceptance-evidence-requirements.md#freeze_batch；work/coverage/acceptance-evidence-requirements.md#six_path_oracles；work/coverage/acceptance-evidence-requirements.md#economics_denominators。

domain原子：storage:SR11、storage:SR16、storage:EX13、router:R36、engine:EC20、acceptance:freeze_batch、acceptance:six_path_oracles、acceptance:economics_denominators；Lark source-first：LARK-003、LARK-061、LARK-069、LARK-070、LARK-084。

<a id="cp03"></a>
### CP03 — cohort放置/一次预取/sharedHBM消费者

Owner：E/B；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：CP01、S08、Q08；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: sglang/srt/managers/schedule_policy.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: schedule_batch.py (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: unified_radix_cache.py refs (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：pending→boundedcohort→restore→sharedpage候选。

完整DoD：RH04原queue deadline/burstcap/singleton保进展；不凑batch拖低负载；取消/出队ref清理；每请求decode/tail独立预算。

可验证consumer：CP04、BX。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R04", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "bounded_cohort"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH04；work/coverage/router-control-requirements.md#R23；work/coverage/engine-requirements.md#XR07。

domain原子：representation:RH04、router:R23、engine:XR07；Lark source-first：LARK-045。

<a id="cp21"></a>
### CP21 — queued-prefix需求树实际enqueue/dequeue消费者

Owner：E/B；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX01、Q08、S05；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: Dynamo SchedulerQueue/policy_queue.rs (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: SG queued Req/URC retention consumer (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：queued-prefix需求树实际enqueue/dequeue消费者的一次性完整receipt。

完整DoD：原pendingqueue真实prefix→祖先count/earliestdeadline/候选/累计受益；取消和dispatch即减不留幽灵count；用于有限retention/restore/coldproducer/replica的指定consumer，不额造queue；pioneer/FCFS/LPM/仅eviction强对照，shortqueue/lowshare退原native，cold进展。

可验证consumer：BX、F02。关闭边界：Accepted scope + real implementation/consumer integrated + necessary CPU H/J receipt; final support requires BX。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX01", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "queued_prefix_demand_consumer"}。

source refs：work/coverage/lark-requirements.md；work/coverage/router-control-requirements.md#R20；work/coverage/engine-requirements.md#XR06。

domain原子：router:R20、engine:XR06；Lark source-first：LARK-044。

<a id="cp23"></a>
### CP23 — 所选工作计量/有限hedging/成本感知victim的窄consumer

Owner：E/B/D；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX02、Q08、Q07、E05；原锚：G package映射。

实际模块/责任：SG946 managers/schedule_batch.py native next-step/retraction/victim path (engine P8/EC12)；SG946 unified_radix_cache.py legal state/restore source refs; scheduler.py run_batch + batch_result_processor actual service (engine P6/P10)；PROPOSED_SELECTED_SUBCAPABILITY: only charge / bounded hedge / cost-aware victim hook explicitly chosen; exact modification callsite locked in RX02 receipt。

固定产物：所选真实charge或有界hedging候选的一次性完整receipt。

完整DoD：先fixedbudget强base；只有所选multi-resourcecharge实际policyconsumer才加账，预计/actual增量releaseonce；hedging仅independentspare/slack批准触发，两个私有target/op，合法winner/loserdrain且计重复work；满载拒双跑、stream不重采样；两独立scope可分别关闭。 独立selected_capabilities.cost_aware_victim_retraction：只在RX02明确选此项才把恢复成本/已有actualservice历史接固定SG schedule_batch.py nativevictim/retraction path及URC合法restore/recompute consumer（engine P8/EC12），exact victim hook由decision receipt锁定，不能虚构函数。真实retract选择→合法保留/弃用→重新admit/re-prefill→result累计，先维持nativecapacity/next-step safety。对比同shape native length/ratio/cadence，报告victim解释、总abort/re-prefill/copy/defer work、ITL/goodput与收益；cancel/最后request/beam/input_embeds/backup不足反例。仅charge或hedge accepted不自动要求修改victim；costvictim accepted也不自动要求hedge。

可验证consumer：BX。关闭边界：Accepted scope + real implementation/consumer integrated + necessary CPU H/J receipt; final support requires BX。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX02", "accepted": "Execute only selected subcapability consumer; none implies others", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "any_explicitly_selected_of(work_charge,bounded_restore_compute_hedge,cost_aware_victim_retraction)"}。

source refs：work/coverage/lark-requirements.md；work/coverage/engine-requirements.md#EC12；work/coverage/engine-requirements.md#XR14。

domain原子：engine:EC12、engine:XR14；Lark source-first：LARK-035。

<a id="cp13"></a>
### CP13 — cache-onlyP bypass被选完整协议

Owner：B/F/PDowner；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX04；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: selected disaggregation scheduler/bootstrap/logits transfer (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：cache-only decode首token/metadata/采样consumer。

完整DoD：FW12完整hit亦有首token/logprob/version/params真实owner；miss/expiry正确拒或重新引P；取消drain/rank再用；先benefit/侵入decision接受，再候选与GPUbatch，模拟不关feature。

可验证consumer：BX。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX04", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "pd_prefill_bypass"}。

source refs：work/coverage/framework-version-requirements.md；work/coverage/framework-version-requirements.md#FW12；work/coverage/engine-requirements.md#XR08。

domain原子：framework:FW12、engine:XR08；Lark source-first：。

<a id="ag03"></a>
### AG03 — program/branch fork-join预算与返回语义

Owner：B/E/产品；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：AG02、E07；原锚：G package映射。

实际模块/责任：actual workflow program/branch/join producer repo INPUT_REQUIRED；SG946 Req/result_processor + existing Router context/queue service budget consumer；PROPOSED selected program/branch budget inheritance/join lifecycle; not generic global ledger。

固定产物：全部/任一/分阶段join真实hintconsumer。

完整DoD：关键路径hint受控额度、未采用branch取消；共享祖先sealed、mutabletail独立；业务工具副作用/权威source记录非KV职责；branch不各自无限优先

可验证consumer：F01、BE。关闭边界：Complete selected production implementation + actual producer/consumer integration + fixed SHA/config + necessary unit/smoke/negative-path H/J receipt; candidate close only。

batch：BE；hardware/input：candidate_close_does_not_authorize_device_or_activation。

执行guard：{"decision": "AG01", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "program_branch_forkjoin_budget"}。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/router-control-requirements.md#R12；work/coverage/engine-requirements.md#AG04；work/coverage/engine-requirements.md#AG05；work/coverage/engine-requirements.md#AG06。

domain原子：router:R12、engine:AG04、engine:AG05、engine:AG06；Lark source-first：LARK-038、LARK-039。

<a id="f01"></a>
### F01 — 融合1共享L2×Agent信号×恢复调度

Owner：B/E/D/H；fusion_decision；status：DECISION_REQUIRED；scope：research。

前置：R01、R02、AG01、BB；原锚：G package映射。

实际模块/责任：component source scopes of referenced research decisions。

固定产物：A/B/AB交互收益与部署disposition。

完整DoD：同资源SLO，workflow完成、cold等待、toolgap/错误预取/两搬运/同时return；正交消融非峰值相乘；accepted明确implementation/验收范围，unknown留gate

可验证consumer：RD。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/representation-hardware-requirements.md#RH33。

domain原子：representation:RH33；Lark source-first：LARK-069。

<a id="cp25"></a>
### CP25 — 所选ContextCache用户API完整服务

Owner：gateway/产品/B/D；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：RX06、S05、E06；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: actual gateway ContextCache API repo UNKNOWN_INPUT (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: Mooncake immutable objects (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: SG context handle consumer (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：所选ContextCache用户API完整服务的一次性完整receipt。

完整DoD：一个actualcontexthandle create/use/renew/release API真实producer→授权→opaqueobject→engine消费；same-domain/撤权/epoch/expiry/掉cache错误与重算，有限TTL/pin/perbeneficiarybilling；多租户public/private明确；读lease/GPUready/服务permit不混保留承诺；不建兼容fallback产品。

可验证consumer：BX。关闭边界：Accepted scope + real implementation/consumer integrated + necessary CPU H/J receipt; final support requires BX。

batch：BX；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "RX06", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "context_cache_public_api"}。

source refs：work/coverage/lark-requirements.md。

domain原子：；Lark source-first：LARK-051。

<a id="ph"></a>
### PH — 原完整feature父票AC回填并真正关闭

Owner：G/H/J/原owner；hard_parent_rollup；status：NOT_STARTED；scope：release。

前置：BS、BB、BC；原锚：MC3/SG8/Dynamo1。

实际模块/责任：existing GitHub native feature parents/receipt; G sole mutation owner。

固定产物：原feature完整AC/实际适用scope native close receipt。

完整DoD：每父票原完整AC含consumer、设备、失败/取消、服务活性及适用scope验收逐项真实回填；既有native硬关系保留，不降AC、不将candidate receipt作parent close；仅适用scope全PASS才真正close。验收批不反依等待自己结果的openparent。

可验证consumer：RB。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：scope registry/audit only；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：outputs/cache-execution-program.md；work/coverage/github-coverage.md；work/coverage/acceptance-evidence-requirements.md#operations_recovery_shutdown。

domain原子：acceptance:operations_recovery_shutdown；Lark source-first：LARK-083。

<a id="cp04"></a>
### CP04 — Cascade/Hydragen真实batch/kernel接入

Owner：B/kernelowner；conditional_implementation；status：NOT_STARTED；scope：conditional。

前置：CP03、V04；原锚：G package映射。

实际模块/责任：PROPOSED_SELECTED_SCOPE: selected engine attention backend (actual file/hook resolution required at decision; not claimed existing function)；PROPOSED_SELECTED_SCOPE: FlashInfer Cascade/Hydragen API actual batch/page metadata (actual file/hook resolution required at decision; not claimed existing function)。

固定产物：sharedprefix+uniquesuffix pagetable/mask/RoPE kernel候选。

完整DoD：RH05调用真实supportedkernel，workspace/scratch预算、rank一致性/引用fence、取消；存储去重与HBM共享不作kernel性能证据。

可验证consumer：BX、F02。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

执行guard：{"decision": "R04", "accepted": "Execute only this explicitly selected subcapability (or required production profile); parent direction accepted is insufficient", "unknown": "BLOCKED", "deferred_rejected": "signed subcapability disposition/reopen; unselected/deferred profile explicitly unsupported", "unknown_detail": "No silent skip; chosen scope can't complete until disposition is explicit.", "selector": "shared_attention_kernel"}。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH05；work/coverage/router-control-requirements.md#R24；work/coverage/engine-requirements.md#XR07。

domain原子：representation:RH05、router:R24、engine:XR07；Lark source-first：LARK-046。

<a id="be"></a>
### BE — 被接受Agent/分支条件扩展批

Owner：H/J；acceptance；status：NOT_STARTED；scope：hardware。

前置：B00、AG01、AG04；原锚：G package映射。

实际模块/责任：REUSE_SUPPORTING_ASSETS: actual production consumer integration/freeze defined in this package + H existing acceptance contract; no tool-only platform。

固定产物：各decision明确选scope的consumer+device+workflow receipt。

完整DoD：只有acceptedbranch实施/集成后才执行；no-change须真实测量并签resolution；workflow时间/质量/toolwait分离，ordinary公平仍通过；无数据不能defaultno-change

可验证consumer：F01、F02、RB。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：explicit_decision_or_audit_receipt；hardware/input：candidate_close_does_not_authorize_device_or_activation。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/acceptance-evidence-requirements.md#six_path_oracles。

domain原子：acceptance:six_path_oracles；Lark source-first：LARK-071、LARK-072、LARK-085。

<a id="rd"></a>
### RD — 全研究方向explicit disposition与扩展scope registry

Owner：领域owner/产品/J；scope_decision；status：DECISION_REQUIRED；scope：research。

前置：R01、R02、R03、R04、R05、R06、R07、R08、R09、R10、R11、R12、F01、F02、F03、F04、RX01、RX02、RX03、RX04、VV2、RX05、RX06、RX07、RX08、RX09；原锚：G package映射。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/context-requirements.md; outputs/inference-cache-architecture.md; work/coverage/representation-hardware-requirements.md#RH01; work/coverage/representation-hardware-requirements.md#RH33; work/coverage/storage-article-requirements.md#R07; no product implementation in this decision。

固定产物：accepted/exploratory/deferred/rejected/unknown一次性scope冻结。

完整DoD：每方向来源/现成能力/新增价值/冲突/owner/输入/触发/DoD；accepted需附完整implementation→consumer→集成→适用验收closed边界，deferred有恢复触发而非隐式skip；未知保gate。此节点不自动选择任何算法 已接受研究分支必须在scope registry绑定新增完整执行包；执行包未绑定时RB BLOCKED，不以本decision关闭自动完成实验实现。 每个方向逐subcapability签选择，例如R08 lossless/quant/MLA、RX04 nativePD/P-bypass/CP分别；一项accepted不得把同族其它能力默认AND。决策族的范围可签有据defer，不要求全部探索当前实现。

可验证consumer：RB。关闭边界：Signed one-time source-backed decision/input; UNKNOWN keeps dependent axis BLOCKED。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/inference-cache-architecture.md；work/coverage/representation-hardware-requirements.md#RH01；work/coverage/representation-hardware-requirements.md#RH33；work/coverage/storage-article-requirements.md#R07。

domain原子：representation:RH01、representation:RH33、storage:R07；Lark source-first：LARK-086。

<a id="bx"></a>
### BX — 所选扩展统一完整freeze验收receipt

Owner：H/J/产品/领域owner；conditional_acceptance；status：NOT_STARTED；scope：conditional。

前置：B00、RD；原锚：G package映射。

实际模块/责任：REUSE_SUPPORTING_ASSETS: actual production consumer integration/freeze defined in this package + H existing acceptance contract; no tool-only platform。

固定产物：各accepted扩展真实consumer/集成/设备/quality/收益批receipt。

完整DoD：RH06/09/14/18/24/32/33与FW09–14按scope合并T18已有batch，不各建benchmark资产。所有selectedcandidate完整freeze后一次适用batch；同native强baseline/model/trace/resource/quality/SLO、2×2交互+否证；reported/actual/inferred与环境失败/skip分开。缺输入BLOCKED，不吞accepted分支；deferred/reject须signed理由与reopen触发。 所有表示评估统一逐sample质量/outputlength/完成latency/longtail；扣precompute、migration、codec、failure/cancel/unused-prefetch成本。

可验证consumer：RB。关闭边界：Accepted decision + complete real production candidate/consumer + dependency integration + necessary CPU receipt; support/quality/device/performance via BX。

batch：BX selected_scope_extension_of_T18；hardware/input：CPU candidate may close independently; applicable runtime/GPU/RNIC/L3/quality/SLO gates remain required before support。

source refs：work/coverage/representation-hardware-requirements.md；work/coverage/representation-hardware-requirements.md#RH06；work/coverage/representation-hardware-requirements.md#RH09；work/coverage/representation-hardware-requirements.md#RH14；work/coverage/representation-hardware-requirements.md#RH18；work/coverage/representation-hardware-requirements.md#RH24；work/coverage/representation-hardware-requirements.md#RH32；work/coverage/representation-hardware-requirements.md#RH33；work/coverage/router-control-requirements.md#R36；work/coverage/acceptance-evidence-requirements.md#freeze_batch；work/coverage/acceptance-evidence-requirements.md#economics_denominators。

domain原子：representation:RH06、representation:RH09、representation:RH14、representation:RH18、representation:RH24、representation:RH32、representation:RH33、router:R36、acceptance:freeze_batch、acceptance:economics_denominators；Lark source-first：LARK-046、LARK-058、LARK-064、LARK-069、LARK-084。

<a id="rb"></a>
### RB — 最终scope冻结与完整产品发布

Owner：发布owner/H/J/G；release；status：NOT_STARTED；scope：release。

前置：BC、BS、BE、V02、RD、BB、PH、VV2、BX、S09；原锚：T19。

实际模块/责任：REUSE_SUPPORTING_ASSETS: actual production consumer integration/freeze defined in this package + H existing acceptance contract; no tool-only platform。

固定产物：scope registry、适用hardparents、upgrade/stop/observe与release receipt。

完整DoD：所选scope全部consumer+code/CPU/integration/device/性能/可deploy轴pass；X01/X02明确resolution；rejected/deferred研究不强实施但理由/触发/期限明确；未验组合启动拒绝

可验证consumer：产品运营。关闭边界：Full stated receipt, with original hardware/parent/publication guards preserved。

batch：explicit_decision_or_audit_receipt；hardware/input：not_applicable_to_document_decision。

source refs：work/coverage/context-requirements.md；outputs/cache-execution-program.md；work/coverage/router-control-requirements.md#R36；work/coverage/engine-requirements.md#EC20；work/coverage/acceptance-evidence-requirements.md#operations_recovery_shutdown。

domain原子：router:R36、engine:EC20、acceptance:operations_recovery_shutdown；Lark source-first：LARK-083。

<a id="s10"></a>
### S10 — Store tenantmode 与强 per-API 容量隔离一次需求决定

Owner：产品/gateway/D/B；decision；NOT_STARTED。

前置：A01、E01。

实际模块/责任：DOCUMENT_ONLY: fixed resolution/scope receipt from work/coverage/storage-article-requirements.md#SR06; work/coverage/router-control-requirements.md#R07; work/source-audit/mooncake-store-lifecycle.md#S13; no product implementation in this decision。

固定产物：所选 setup-domain/namespace + Engine service/retention权益，或强 per-API Store容量隔离 resolution。

完整DoD：先复用setup-domain、不可变namespace和Engine服务/驻留额度，不能将Store setup tenant称API tenant；一次确认是否必须每APItenant强Store物理容量隔离、授权/成本承诺/最低quota与缺失RPC。若非必需签native setup模式/unsupported强隔离；只有明确所需才selected_capabilities.strong_per_api_store_quota=accepted，绑定S06完整per-batchconsumer；未知BLOCKED该强隔离scope，不阻setup普通/核心公共API权益路径。

可验证consumer：S06、Q04、S07、BB。关闭边界：实际产品/tenantmode来源 + 三owner签定字段/consumer/支持拒绝；不授实现/容量设备验收。

batch：decision_registry; selected S06 in BB；hardware/input：需求决策不需GPU；所选强模式完整支持须BB。

source refs：work/coverage/storage-article-requirements.md#SR06；work/coverage/router-control-requirements.md#R07；work/source-audit/mooncake-store-lifecycle.md#S13。

## 52R逐项覆盖

| R / 原分类 | concept / scope | tasks | disposition |
|---|---|---|---|
| R-001 / must | 池化L2：容量聚合、跨实例复用、命中成本/延迟/命中率；查清收益机制和适用负载 | [S01](#s01)、[E02](#e02)、[S07](#s07)、[BA](#ba)、[BB](#bb) | accepted_requirement; implementation_and_input_gates_still_open |
| R-002 / must | 成本效率/研究：证据边界、投入价值、扩展机会与否证；不是无条件采用所有技术 | [A02](#a02)、[R01](#r01)、[VV2](#vv2) | accepted_requirement; implementation_and_input_gates_still_open |
| R-003 / must | 给定网络能力前提；不能把网络建设作为全图首个假定阻塞，但仍核算传输争用与时间 | [V01](#v01)、[L03](#l03)、[R01](#r01) | accepted_requirement; implementation_and_input_gates_still_open |
| R-004 / must | 专用L3：设备合同、容量/恢复/I/O/取消/完成接口；未知ABI不能假装已具备 | [L01](#l01)、[L02](#l02)、[BC](#bc) | accepted_requirement; implementation_and_input_gates_still_open |
| R-005 / must | 跨L1/L2/L3放置、预取、迁层、恢复、写回、有效容量与资源利用；统一用户层级名称和框架映射 | [E03](#e03)、[E04](#e04)、[S07](#s07)、[S08](#s08)、[L02](#l02)、[L04](#l04)、[BB](#bb)、[BC](#bc)、[RB](#rb)、[CP14](#cp14) | accepted_requirement; implementation_and_input_gates_still_open |
| R-006 / must | 原文与一手证据实际读取；访问不可用须明示，不能以其他论文冒充原文已读 | [S00](#s00)、[SJ](#sj) | accepted_requirement; implementation_and_input_gates_still_open |
| R-007 / must | 全方向研究覆盖、组合/冲突/已有能力/增量价值；每方向必须有 explicit disposition | [RD](#rd)、[BX](#bx) | accepted_requirement; implementation_and_input_gates_still_open |
| R-008 / must | 版本依赖+框架对照：按锁定版本比较调用链、表示、PD/恢复、调度与改造成本；保留独立vLLM工作线 | [V01](#v01)、[V02](#v02)、[V03](#v03)、[BV](#bv)、[RX04](#rx04)、[VV1](#vv1)、[VV2](#vv2)、[CP12](#cp12) | accepted_requirement; implementation_and_input_gates_still_open |
| R-009 / must | 设备验收依赖；后续可用CPU证据不等于GPU正确性/收益；本次只读审计，不新跑机器实验 | [B00](#b00)、[BA](#ba)、[BB](#bb)、[BC](#bc) | accepted_requirement; implementation_and_input_gates_still_open |
| R-010 / must | 完整研究与固定执行规范同步；本审计 agent 不执行远端写，主任务负责具体落地 | [SJ](#sj)、[SP](#sp) | accepted_requirement; implementation_and_input_gates_still_open |
| R-011 / 探索 | 优先研究系统缓存/调度收益；这是投资判断待证据支撑，不能宣布所有算子已无价值 | [R01](#r01) | explicit_research_decision_required |
| R-012 / must | Router/queue分类、亲和、绿色通道、预算及缓存共同调度；不仅目录查找 | [E03](#e03)、[Q01](#q01)、[E05](#e05)、[Q08](#q08)、[S08](#s08)、[BB](#bb)、[RX01](#rx01) | accepted_requirement; implementation_and_input_gates_still_open |
| R-013 / must | 跨层合同与真实消费者；目录命中→可恢复→GPU就绪→引擎准入→执行释放端到端 | [E01](#e01)、[S01](#s01)、[S02](#s02)、[E02](#e02)、[E03](#e03)、[E04](#e04)、[E05](#e05)、[E06](#e06)、[BA](#ba)、[BS](#bs)、[VV1](#vv1) | accepted_requirement; implementation_and_input_gates_still_open |
| R-014 / must | Agent首试点：跨轮上下文、工具等待/返回、分支、结束/取消；任务完成成本与时间 | [A02](#a02)、[Q02](#q02)、[AG01](#ag01)、[AG02](#ag02)、[AG03](#ag03)、[BB](#bb)、[BE](#be)、[BX](#bx) | accepted_requirement; implementation_and_input_gates_still_open |
| R-015 / must | 通用API混流：普通短请求、长输入、长输出、冷请求、新租户与Agent共同公平；Agent能力须可选 | [A01](#a01)、[A02](#a02)、[Q02](#q02)、[E05](#e05)、[S06](#s06)、[Q08](#q08)、[S08](#s08)、[BA](#ba)、[BB](#bb)、[VV1](#vv1)、[RX06](#rx06)、[CP25](#cp25)、[S10](#s10) | accepted_requirement; implementation_and_input_gates_still_open |
| R-016 / must | 真实功能实现工作为主；研发候选、接入消费者、CPU证据、设备验收和上线分别记账 | [I01](#i01)、[RA](#ra)、[RB](#rb) | accepted_requirement; implementation_and_input_gates_still_open |
| R-017 / 被否定 | 禁止把全览继续写成临时建议或反复选下一方向；固定可执行任务、触发/交付/依赖/DoD | [RD](#rd)、[SJ](#sj) | rejected; fixed_function_delivery_and_batch_acceptance_enforced |
| R-018 / must | 事实来源与执行任务映射；未知事实先锁决策；GitHub既有任务状态/依赖须实际回读 | [S00](#s00)、[I01](#i01)、[A01](#a01)、[RD](#rd)、[SJ](#sj)、[SP](#sp)、[PH](#ph) | accepted_requirement; implementation_and_input_gates_still_open |
| R-019 / 被否定 | 不让验证/回放工具代替真实功能；完整切片集成冻结后批次验收，失败或相关改动才局部复测 | [B00](#b00)、[BA](#ba)、[BB](#bb)、[BC](#bc)、[RA](#ra)、[RB](#rb)、[BX](#bx) | rejected; fixed_function_delivery_and_batch_acceptance_enforced |
| R-020 / must | 本次覆盖审计：来源→需求→任务→依赖→验收；六工作线不是仅六目录，也不能从近期20节点拼概览 | [S00](#s00)、[RD](#rd)、[SJ](#sj)、[SP](#sp) | accepted_requirement; implementation_and_input_gates_still_open |
| R-021 / 探索 | 恢复时间、GPU选择、缓存层、副本、当前负载/未来decode容量联合决策 | [Q06](#q06)、[Q07](#q07)、[R01](#r01)、[RX02](#rx02)、[RX03](#rx03)、[RX04](#rx04)、[CP12](#cp12)、[CP13](#cp13)、[CP17](#cp17)、[CP22](#cp22)、[CP23](#cp23) | explicit_research_decision_required |
| R-022 / 探索 | 明确事件、有限TTL、暂停保留/下沉、返回恢复与主动解除pin；短等待多搬运反例 | [L04](#l04)、[AG01](#ag01)、[AG02](#ag02)、[BE](#be)、[R02](#r02) | explicit_research_decision_required |
| R-023 / 探索 | FLOPs/byte、重算成本、层间恢复、驻留时长、副本成本；简单收录和LRU强基线 | [Q07](#q07)、[S07](#s07)、[R03](#r03)、[RX03](#rx03)、[CP20](#cp20)、[CP22](#cp22) | explicit_research_decision_required |
| R-024 / 探索 | 全局祖先身份、共享页、分组恢复、producer选择、同前缀kernel；decode共享收益单独证明 | [Q05](#q05)、[AG04](#ag04)、[AG05](#ag05)、[BE](#be)、[R04](#r04)、[RX01](#rx01)、[CP01](#cp01)、[CP02](#cp02)、[CP03](#cp03)、[CP04](#cp04)、[CP21](#cp21) | explicit_research_decision_required |
| R-025 / 探索 | 固定system/tool定义随版本预计算发布；收益回本与版本失效 | [S05](#s05)、[R05](#r05)、[CP05](#cp05) | explicit_research_decision_required |
| R-026 / 探索 | 独立Store、扩缩容预热、升级转存、请求换机恢复、恢复突发限额 | [E06](#e06)、[Q03](#q03)、[R06](#r06)、[RX03](#rx03)、[CP06](#cp06)、[RX07](#rx07)、[CP19](#cp19)、[CP22](#cp22) | explicit_research_decision_required |
| R-027 / 探索 | 批量匹配、事件索引、ready状态、lease/pin/对象完成、配额与身份隔离 | [A01](#a01)、[A03](#a03)、[Q02](#q02)、[S05](#s05)、[S06](#s06)、[E06](#e06)、[Q03](#q03)、[Q04](#q04)、[Q05](#q05)、[S07](#s07)、[BS](#bs)、[R07](#r07)、[RX06](#rx06)、[RX07](#rx07)、[CP19](#cp19)、[CP25](#cp25)、[S10](#s10) | explicit_research_decision_required |
| R-028 / 探索 | 冷层编码、L2消费格式、L1原生格式、MLA不同表示；质量与兼容边界独立验收 | [R08](#r08)、[V04](#v04)、[CP07](#cp07)、[CP08](#cp08)、[CP09](#cp09)、[CP14](#cp14)、[BX](#bx) | explicit_research_decision_required |
| R-029 / 探索 | CacheBlend类非前缀块/上下文变体/选择性重算；单独质量验收和退出条件 | [R09](#r09)、[CP15](#cp15)、[BX](#bx) | explicit_research_decision_required |
| R-030 / 探索 | 跨TP/布局/块尺寸；完整KV、滑窗、递归检查点；降低表示和部署分割 | [A03](#a03)、[S05](#s05)、[R10](#r10)、[RX04](#rx04)、[V04](#v04)、[CP07](#cp07)、[CP10](#cp10)、[CP11](#cp11)、[CP12](#cp12)、[CP17](#cp17)、[BX](#bx)、[RX05](#rx05)、[CP24](#cp24) | explicit_research_decision_required |
| R-031 / 探索 | 批量恢复、逻辑page与物理I/O双粒度、deadline、read/write/prefetch预算、取消、解压DMA | [S08](#s08)、[L01](#l01)、[L02](#l02)、[L03](#l03)、[L04](#l04)、[BC](#bc)、[R11](#r11)、[CP16](#cp16)、[BX](#bx) | explicit_research_decision_required |
| R-032 / 探索 | 冷KV近数据计算、partial output/logsumexp合并；独立长期课题，设备算力/带宽先决 | [R12](#r12)、[CP18](#cp18)、[BX](#bx) | explicit_research_decision_required |
| R-033 / 探索 | 共享L2＋Agent阶段信号＋恢复调度：完整任务时间、冷请求等待、无效预取、搬运成本 | [F01](#f01) | explicit_research_decision_required |
| R-034 / 探索 | 前缀DAG＋分组＋共享页＋Cascade：存储副本/HBM副本/kernel收益分开核算，分组等待及热点争用 | [F02](#f02)、[CP01](#cp01)、[CP03](#cp03)、[CP04](#cp04) | explicit_research_decision_required |
| R-035 / 探索 | 原生紧凑格式＋价值收录＋L3 I/O：CPU/DPU/GPU发起路径对照；不默认DMA无控制成本 | [L01](#l01)、[L03](#l03)、[R11](#r11)、[F03](#f03)、[CP07](#cp07)、[CP08](#cp08)、[CP09](#cp09)、[CP16](#cp16) | explicit_research_decision_required |
| R-036 / 探索 | 兼容身份＋版本预热＋全局索引＋弹性；版本作废、成本解释、容量/pin/恢复预算 | [F04](#f04)、[CP05](#cp05)、[CP06](#cp06)、[CP10](#cp10) | explicit_research_decision_required |
| R-037 / 探索 | Agent真实前缀机会：跨轮、子Agent祖先、跨任务公共前缀分开；追加/改写/压缩导致的失效 | [AG01](#ag01)、[AG02](#ag02)、[AG04](#ag04)、[AG05](#ag05)、[BE](#be)、[R02](#r02)、[R04](#r04)、[CP01](#cp01)、[CP02](#cp02)、[RX05](#rx05)、[CP24](#cp24) | explicit_research_decision_required |
| R-038 / 探索 | 连续完成与新任务公平：GPU服务、恢复I/O、缓存驻留三资源；热度不等于服务等级；续跑额度/aging | [Q02](#q02)、[E05](#e05)、[Q06](#q06)、[Q08](#q08)、[S08](#s08)、[AG01](#ag01)、[AG02](#ag02)、[AG03](#ag03)、[BE](#be)、[RX02](#rx02)、[RX05](#rx05)、[CP23](#cp23)、[CP24](#cp24) | explicit_research_decision_required |
| R-039 / 探索 | 并行工具/子Agent fork-join依赖感知；全部/任一/分阶段返回语义；避免过早占HBM | [AG01](#ag01)、[AG03](#ag03)、[AG04](#ag04)、[AG05](#ag05)、[BE](#be)、[R04](#r04)、[CP02](#cp02)、[RX05](#rx05)、[CP24](#cp24) | explicit_research_decision_required |
| R-040 / 探索 | 增量块写回、源GPU页所有权、异步积压/背压、结束后尾部占用、哪些数据不入L3 | [S08](#s08)、[L04](#l04)、[R03](#r03)、[CP20](#cp20) | explicit_research_decision_required |
| R-041 / 待决策 | 尽力缓存 vs 有预算恢复承诺；对象lease/pin/完成不能合并成未经定义的会话保证 | [AG01](#ag01)、[AG02](#ag02)、[BE](#be)、[R02](#r02)、[RX06](#rx06)、[CP25](#cp25) | explicit_research_decision_required |
| R-042 / 探索 | 本机强基线、同总DRAM共享池、联合路由、L3、生命周期预取；A/B/AB消融，不能相乘单项收益 | [A02](#a02)、[B00](#b00)、[BA](#ba)、[BB](#bb)、[BC](#bc)、[R01](#r01)、[BX](#bx) | explicit_research_decision_required |
| R-043 / 探索 | 版本/依赖：引擎+Mooncake client/Store+Router锁定、模型支持边界、配置/ABI、组合矩阵 | [V01](#v01)、[V03](#v03)、[I01](#i01)、[A03](#a03)、[E06](#e06)、[V04](#v04)、[V05](#v05)、[V06](#v06)、[CP14](#cp14) | explicit_research_decision_required |
| R-044 / 探索 | SGLang KV lifecycle：冷/L2命中/tool-return/共享前缀突发/传输中取消；allocate/pin/load/ready/release实链 | [E01](#e01)、[E02](#e02)、[E03](#e03)、[E04](#e04)、[E06](#e06) | explicit_research_decision_required |
| R-045 / 探索 | 引擎准入与混流公平：恢复或重算、排队/在途账、HBM与未来decode、冷请求/长输出/租户保护 | [E01](#e01)、[E03](#e03)、[E04](#e04)、[Q02](#q02)、[E05](#e05)、[Q07](#q07)、[Q08](#q08)、[RX02](#rx02)、[CP23](#cp23) | explicit_research_decision_required |
| R-046 / 探索 | Store lifecycle：数据与元数据就绪、身份、lease/pin/错误、TE完成/取消/资源回收，部署启用门槛 | [E01](#e01)、[S01](#s01)、[S02](#s02)、[E02](#e02)、[S05](#s05)、[S06](#s06)、[S07](#s07)、[BS](#bs)、[RX07](#rx07)、[CP19](#cp19) | explicit_research_decision_required |
| R-047 / 探索 | Router/queue：目录来源、新鲜度、路由/排序/准入职责、亲和/绿色通道分类、deadline/预算/aging | [A01](#a01)、[Q01](#q01)、[Q02](#q02)、[Q03](#q03)、[Q04](#q04)、[Q05](#q05)、[Q06](#q06)、[Q08](#q08)、[RX01](#rx01)、[RX03](#rx03)、[CP21](#cp21)、[CP22](#cp22) | explicit_research_decision_required |
| R-048 / must | vLLM独立对照：固定版本的connector/PD/decode写回/跨TP/混合状态/调度契约，不是只在结论中点名 | [V02](#v02)、[V03](#v03)、[BV](#bv)、[RX04](#rx04)、[V04](#v04)、[V05](#v05)、[VV1](#vv1)、[V06](#v06)、[VV2](#vv2)、[CP10](#cp10)、[CP12](#cp12)、[CP13](#cp13)、[CP14](#cp14) | accepted_requirement; implementation_and_input_gates_still_open |
| R-049 / 待决策 | 主模型/真实trace、SLO/流量比例/恢复阈值/TTL/队列参数/价格数据；建立决策合同而非填假值 | [V01](#v01)、[A02](#a02)、[B00](#b00)、[RD](#rd) | explicit_research_decision_required |
| R-050 / 探索 | 跨仓所有权/消费者、身份、信用、资源预算/启用和事件部署：已建工单属历史执行基准，本次重新验证覆盖，不能自证完整 | [E01](#e01)、[A03](#a03)、[Q01](#q01)、[S05](#s05)、[E06](#e06)、[Q03](#q03)、[Q04](#q04)、[Q06](#q06)、[BS](#bs)、[RD](#rd)、[PH](#ph)、[VV1](#vv1)、[V06](#v06) | explicit_research_decision_required |
| R-051 / must | 功能交付和验收分层：候选代码、真实消费者接入、CPU控制、GPU/设备数据正确性、实测收益、部署各有状态 | [I01](#i01)、[S02](#s02)、[B00](#b00)、[BA](#ba)、[BS](#bs)、[BB](#bb)、[BC](#bc)、[RA](#ra)、[RB](#rb)、[SJ](#sj)、[PH](#ph)、[V05](#v05)、[BX](#bx) | accepted_requirement; implementation_and_input_gates_still_open |
| R-052 / 探索 | 成本效率合同：同SLO完成成本/GPU秒/P99 TTFT/TPOT/有效连续前缀；失败、取消、复制、pin驻留计入；无价格仅资源对照 | [A02](#a02)、[Q07](#q07)、[B00](#b00)、[BB](#bb)、[BC](#bc)、[R01](#r01) | explicit_research_decision_required |

12研究：1→R01；2→R02；3→R03；4→R04；5→R05；6→R06；7→R07；8→R08；9→R09；10→R10；11→R11；12→R12。四融合：F01、F02、F03、F04。六源码工作线：版本依赖→V01,V04,V05,I01,V06；SGLang生命周期→E01,E02,E03,E04,E06,E07；引擎准入公平→E03,E04,E05,Q08,E07；Store/TE→S01,S02,S05,S06,S07,S08,L01,L02,L03,L04；Router队列→Q01,Q02,Q03,Q04,Q05,Q06,Q07,Q08；vLLM独立→V02,VV1,BV,VV2,V06。

## Domain原子去重映射

| source atom | 固定execution/decision |
|---|---|
| framework:FW01 | [I01](#i01) |
| framework:FW02 | [V01](#v01)、[A02](#a02)、[A03](#a03) |
| framework:FW03 | [V04](#v04) |
| framework:FW04 | [V05](#v05) |
| framework:FW05 | [E02](#e02)、[E04](#e04)、[BA](#ba) |
| framework:FW06 | [VV1](#vv1) |
| framework:FW07 | [BV](#bv) |
| framework:FW08 | [VV2](#vv2) |
| framework:FW09 | [CP14](#cp14) |
| framework:FW10 | [R10](#r10)、[CP10](#cp10) |
| framework:FW11 | [CP12](#cp12) |
| framework:FW12 | [CP13](#cp13) |
| framework:FW13 | [CP11](#cp11) |
| framework:FW14 | [CP07](#cp07)、[CP09](#cp09) |
| framework:FW15 | [E05](#e05)、[Q04](#q04)、[VV1](#vv1)、[B00](#b00) |
| framework:FW16 | [V06](#v06) |
| representation:RH01 | [RD](#rd)、[V01](#v01) |
| representation:RH02 | [CP01](#cp01) |
| representation:RH03 | [AG04](#ag04)、[AG05](#ag05)、[CP02](#cp02) |
| representation:RH04 | [CP03](#cp03) |
| representation:RH05 | [CP04](#cp04) |
| representation:RH06 | [BX](#bx)、[F02](#f02) |
| representation:RH07 | [R05](#r05)、[CP05](#cp05) |
| representation:RH08 | [CP05](#cp05) |
| representation:RH09 | [BX](#bx)、[F04](#f04) |
| representation:RH10 | [CP07](#cp07) |
| representation:RH11 | [CP08](#cp08) |
| representation:RH12 | [CP09](#cp09) |
| representation:RH13 | [CP09](#cp09) |
| representation:RH14 | [BX](#bx)、[F03](#f03) |
| representation:RH15 | [R09](#r09)、[CP15](#cp15) |
| representation:RH16 | [CP15](#cp15) |
| representation:RH17 | [CP15](#cp15) |
| representation:RH18 | [BX](#bx)、[CP15](#cp15) |
| representation:RH19 | [R10](#r10)、[V04](#v04) |
| representation:RH20 | [CP10](#cp10) |
| representation:RH21 | [CP06](#cp06) |
| representation:RH22 | [R10](#r10)、[CP11](#cp11) |
| representation:RH23 | [CP11](#cp11) |
| representation:RH24 | [BX](#bx) |
| representation:RH25 | [L01](#l01)、[R11](#r11) |
| representation:RH26 | [L02](#l02)、[L03](#l03) |
| representation:RH27 | [CP16](#cp16) |
| representation:RH28 | [CP16](#cp16) |
| representation:RH29 | [RX04](#rx04)、[CP17](#cp17) |
| representation:RH30 | [R12](#r12) |
| representation:RH31 | [CP18](#cp18) |
| representation:RH32 | [BX](#bx)、[CP18](#cp18) |
| representation:RH33 | [F01](#f01)、[F02](#f02)、[F03](#f03)、[F04](#f04)、[BX](#bx)、[RD](#rd) |
| representation:RH34 | [RX08](#rx08)、[CP26](#cp26) |
| representation:RH35 | [RX09](#rx09)、[CP27](#cp27) |
| representation:RH36 | [RX07](#rx07)、[CP19](#cp19) |
| representation:RH37 | [RX05](#rx05)、[CP24](#cp24) |
| storage:SR01 | [S01](#s01)、[E02](#e02)、[E04](#e04)、[BA](#ba) |
| storage:SR02 | [S01](#s01)、[S05](#s05) |
| storage:SR03 | [S01](#s01)、[S07](#s07) |
| storage:SR04 | [S01](#s01)、[E02](#e02)、[E03](#e03)、[E04](#e04) |
| storage:SR05 | [E06](#e06)、[S02](#s02) |
| storage:SR06 | [A01](#a01)、[A03](#a03)、[S05](#s05)、[S06](#s06)、[S10](#s10) |
| storage:SR07 | [E06](#e06)、[Q03](#q03)、[Q04](#q04)、[Q05](#q05)、[BS](#bs) |
| storage:SR08 | [S07](#s07)、[E03](#e03) |
| storage:SR09 | [Q08](#q08)、[S08](#s08)、[E04](#e04)、[E07](#e07) |
| storage:SR10 | [S02](#s02)、[V04](#v04) |
| storage:SR11 | [B00](#b00)、[BA](#ba)、[BB](#bb)、[BC](#bc)、[A02](#a02) |
| storage:SR12 | [L01](#l01)、[L02](#l02)、[L03](#l03)、[L04](#l04) |
| storage:SR13 | [RX07](#rx07)、[CP19](#cp19) |
| storage:SR14 | [S09](#s09)、[CP28](#cp28) |
| storage:SR15 | [R07](#r07)、[Q05](#q05) |
| storage:SR16 | [L01](#l01)、[L03](#l03)、[L04](#l04)、[BC](#bc) |
| storage:EX01 | [R03](#r03)、[CP20](#cp20) |
| storage:EX02 | [AG01](#ag01)、[AG02](#ag02) |
| storage:EX03 | [AG04](#ag04)、[AG05](#ag05) |
| storage:EX04 | [R05](#r05)、[CP05](#cp05) |
| storage:EX05 | [R06](#r06)、[CP06](#cp06) |
| storage:EX06 | [R07](#r07)、[Q05](#q05) |
| storage:EX07 | [R10](#r10)、[CP10](#cp10)、[CP11](#cp11) |
| storage:EX08 | [R08](#r08)、[CP07](#cp07)、[CP08](#cp08)、[CP09](#cp09) |
| storage:EX09 | [R09](#r09)、[CP15](#cp15) |
| storage:EX10 | [R11](#r11)、[L03](#l03)、[CP16](#cp16) |
| storage:EX11 | [R12](#r12)、[CP18](#cp18) |
| storage:EX12 | [RX05](#rx05)、[CP24](#cp24) |
| storage:EX13 | [A02](#a02)、[BC](#bc)、[R11](#r11) |
| storage:U01 | [S00](#s00) |
| storage:U02 | [L01](#l01) |
| storage:U03 | [V01](#v01)、[A03](#a03) |
| storage:U04 | [A01](#a01)、[A02](#a02)、[RX07](#rx07)、[S09](#s09) |
| storage:R01 | [S07](#s07)、[BB](#bb) |
| storage:R02 | [E04](#e04)、[CP11](#cp11) |
| storage:R03 | [S01](#s01)、[E06](#e06) |
| storage:R04 | [A01](#a01)、[S06](#s06) |
| storage:R05 | [S05](#s05)、[CP15](#cp15) |
| storage:R06 | [V04](#v04)、[L01](#l01)、[S02](#s02) |
| storage:R07 | [E01](#e01)、[Q01](#q01)、[RD](#rd) |
| router:R01 | [A01](#a01) |
| router:R02 | [V01](#v01)、[A03](#a03)、[S05](#s05) |
| router:R03 | [Q02](#q02) |
| router:R04 | [E06](#e06)、[BS](#bs) |
| router:R05 | [Q03](#q03) |
| router:R06 | [Q04](#q04) |
| router:R07 | [S06](#s06)、[Q04](#q04)、[S10](#s10) |
| router:R08 | [Q05](#q05) |
| router:R09 | [Q05](#q05) |
| router:R10 | [R07](#r07) |
| router:R11 | [E01](#e01)、[E05](#e05)、[Q08](#q08) |
| router:R12 | [AG03](#ag03) |
| router:R13 | [Q06](#q06)、[E05](#e05) |
| router:R14 | [Q06](#q06)、[E02](#e02) |
| router:R15 | [Q06](#q06)、[Q07](#q07)、[RX03](#rx03) |
| router:R16 | [Q08](#q08) |
| router:R17 | [E03](#e03)、[E04](#e04) |
| router:R18 | [Q07](#q07) |
| router:R19 | [R01](#r01)、[Q07](#q07)、[Q08](#q08) |
| router:R20 | [RX01](#rx01)、[CP21](#cp21) |
| router:R21 | [CP02](#cp02) |
| router:R22 | [AG04](#ag04)、[AG05](#ag05) |
| router:R23 | [CP03](#cp03) |
| router:R24 | [R04](#r04)、[CP04](#cp04) |
| router:R25 | [R03](#r03)、[CP20](#cp20) |
| router:R26 | [RX03](#rx03)、[CP22](#cp22) |
| router:R27 | [R11](#r11)、[CP16](#cp16) |
| router:R28 | [S08](#s08) |
| router:R29 | [R05](#r05)、[CP05](#cp05) |
| router:R30 | [AG01](#ag01)、[AG02](#ag02) |
| router:R31 | [R02](#r02)、[L04](#l04) |
| router:R32 | [R06](#r06)、[CP06](#cp06) |
| router:R33 | [RX05](#rx05)、[CP24](#cp24) |
| router:R34 | [L01](#l01)、[L02](#l02)、[L03](#l03)、[L04](#l04) |
| router:R35 | [B00](#b00)、[E07](#e07) |
| router:R36 | [BA](#ba)、[BB](#bb)、[BC](#bc)、[BX](#bx)、[RA](#ra)、[RB](#rb) |
| router:R37 | [E01](#e01)、[E07](#e07)、[S07](#s07) |
| router:R38 | [E03](#e03)、[E04](#e04)、[S08](#s08) |
| engine:EC01 | [V01](#v01)、[V04](#v04)、[V05](#v05) |
| engine:EC02 | [E01](#e01) |
| engine:EC03 | [S01](#s01)、[E02](#e02)、[E04](#e04)、[BA](#ba) |
| engine:EC04 | [E02](#e02)、[S01](#s01) |
| engine:EC05 | [E03](#e03) |
| engine:EC06 | [E04](#e04) |
| engine:EC07 | [E04](#e04)、[E05](#e05)、[E07](#e07) |
| engine:EC08 | [S08](#s08) |
| engine:EC09 | [E04](#e04)、[E05](#e05)、[Q08](#q08) |
| engine:EC10 | [Q02](#q02)、[E05](#e05) |
| engine:EC11 | [E07](#e07) |
| engine:EC12 | [RX02](#rx02)、[CP23](#cp23) |
| engine:EC13 | [Q07](#q07)、[E04](#e04) |
| engine:EC14 | [S05](#s05) |
| engine:EC15 | [E06](#e06) |
| engine:EC16 | [E01](#e01)、[E03](#e03)、[S07](#s07) |
| engine:EC17 | [E05](#e05)、[E07](#e07)、[B00](#b00) |
| engine:EC18 | [E06](#e06)、[A03](#a03) |
| engine:EC19 | [E02](#e02)、[E04](#e04)、[S08](#s08) |
| engine:EC20 | [BA](#ba)、[BB](#bb)、[BC](#bc)、[RB](#rb) |
| engine:AG01 | [AG01](#ag01)、[S05](#s05) |
| engine:AG02 | [AG02](#ag02) |
| engine:AG03 | [Q02](#q02)、[E05](#e05)、[AG02](#ag02) |
| engine:AG04 | [AG03](#ag03) |
| engine:AG05 | [AG03](#ag03)、[CP01](#cp01) |
| engine:AG06 | [AG03](#ag03)、[L04](#l04) |
| engine:AG07 | [S08](#s08)、[CP12](#cp12) |
| engine:AG08 | [AG02](#ag02)、[E02](#e02) |
| engine:XR01 | [R10](#r10)、[CP11](#cp11) |
| engine:XR02 | [R10](#r10)、[CP10](#cp10) |
| engine:XR03 | [R08](#r08)、[CP07](#cp07)、[CP08](#cp08)、[CP09](#cp09) |
| engine:XR04 | [R09](#r09)、[CP15](#cp15) |
| engine:XR05 | [AG04](#ag04)、[AG05](#ag05) |
| engine:XR06 | [RX01](#rx01)、[CP21](#cp21) |
| engine:XR07 | [CP03](#cp03)、[CP04](#cp04) |
| engine:XR08 | [RX04](#rx04)、[CP12](#cp12)、[CP13](#cp13)、[CP17](#cp17) |
| engine:XR09 | [R05](#r05)、[CP05](#cp05) |
| engine:XR10 | [R06](#r06)、[CP06](#cp06) |
| engine:XR11 | [RX05](#rx05)、[CP24](#cp24) |
| engine:XR12 | [L01](#l01)、[L02](#l02)、[L03](#l03)、[L04](#l04)、[CP16](#cp16) |
| engine:XR13 | [R12](#r12)、[CP18](#cp18) |
| engine:XR14 | [RX02](#rx02)、[RX03](#rx03)、[CP22](#cp22)、[CP23](#cp23) |
| acceptance:evidence_scope | [I01](#i01)、[BA](#ba)、[S01](#s01)、[S02](#s02) |
| acceptance:freeze_batch | [B00](#b00)、[BA](#ba)、[BB](#bb)、[BC](#bc)、[BX](#bx) |
| acceptance:six_path_oracles | [BA](#ba)、[BB](#bb)、[BC](#bc)、[BE](#be) |
| acceptance:causal_trace_presence | [B00](#b00)、[E05](#e05)、[E07](#e07) |
| acceptance:economics_denominators | [A02](#a02)、[BB](#bb)、[BC](#bc)、[BV](#bv)、[BX](#bx) |
| acceptance:operations_recovery_shutdown | [RA](#ra)、[RB](#rb)、[PH](#ph)、[E06](#e06)、[RX07](#rx07)、[S09](#s09) |

## 88 Lark source-first概念

180native source refs（block/revision/chapter/snapshotline/URL）保存在coverage-matrix；这些概念独立从8页抽取，没有由DAG反推。

| ID / 原分类 | concept / boundary | tasks |
|---|---|---|
| LARK-001 / 范围依据，待上下文reader核显式用户归因 | 通用公共API混流，Agent首试且生命周期提示可选；不能只验Agent或要求专用SDK才能正常服务 | [Q02](#q02)、[Q08](#q08)、[BB](#bb)、[AG01](#ag01) |
| LARK-002 / 目标依据，非已证收益 | 降低实际命中成本和延迟，提升可用命中率与总资源利用；价格折扣与物理成本分开；不追100%容量利用 | [A02](#a02)、[R01](#r01)、[BB](#bb) |
| LARK-003 / 产品架构范围 | L1 GPU、共享DRAM L2、未来专属L3联合控制；rank私有host staging仍是实际独立物理层 | [V01](#v01)、[E04](#e04)、[L01](#l01)、[L02](#l02)、[BC](#bc) |
| LARK-004 / 设计约束 | 网络连通/带宽假设不免除endpoint PCIe/NUMA/DMA/队列成本；不重复优化用户已排除的网络拓扑，但不能忽略搬运关键路径 | [V01](#v01)、[R01](#r01)、[L03](#l03) |
| LARK-005 / 比较决定，需实际模型/SLO维护面积验证 | SGLang主研究线、vLLM条件替代与公平对照；不是SGLang性能已胜；不同时深改两个引擎 | [V02](#v02)、[V03](#v03)、[BV](#bv)、[VV2](#vv2) |
| LARK-006 / 固定事实与验收规范 | 源码组合/官方容器recipe/实际fork运行provenance独立；固定tag或archive不证明联合安装/ABI兼容 | [V01](#v01)、[I01](#i01)、[V04](#v04)、[V05](#v05) |
| LARK-007 / 探索与收益假设 | 容量去重/统计池化/独立实例恢复/释放路由选择；不把不同GPU上的活跃HBM副本都自动去掉 | [S07](#s07)、[BA](#ba)、[R01](#r01) |
| LARK-008 / 经济与观测规范 | token hit、避免prefill工作、最终消费hit分开；存在性/query hit不等可用消费hit或attention时间比例 | [B00](#b00)、[BB](#bb)、[R01](#r01) |
| LARK-009 / 设计不变量 | Router预测、engine服务与HBM、cache/TE物理占用独立；booking不硬reserve；实际占用/未来credit/费用不重复叠加 | [E01](#e01)、[E05](#e05)、[Q06](#q06)、[S08](#s08) |
| LARK-010 / 研究方案 | 最小预计完成时间联合排队/恢复/计算/输出；保守误差/校准；P95段相加不是请求P95保证 | [Q07](#q07)、[R01](#r01) |
| LARK-011 / 研究方案，公共混流核心 | interactive/compound/session/batch权益与资源代价分离；客户priority/class/fixture标签不能自授权 | [A01](#a01)、[Q02](#q02)、[Q08](#q08) |
| LARK-012 / 设计方案与待实现功能 | deadline/未来decode/恢复bytes/staging byte-time/retention多维准入；max_tokens不等实际成本；未知输出滚动估计 | [E03](#e03)、[E04](#e04)、[E05](#e05)、[Q07](#q07) |
| LARK-013 / 固定事实加新增gate | select-before-materialize、真实IO grant与GPU fence共同准入；绿色通道不能绕容量或把qsize当资源 | [E03](#e03)、[E04](#e04)、[S08](#s08) |
| LARK-014 / 待业务事实与实施要求 | gateway认证tenant/share-domain/内部service_context传播；公开字段直通现状不能作为可信tenant授权 | [A01](#a01)、[Q02](#q02) |
| LARK-015 / 设计约束 | 单authoritative waiting容器、恢复等待状态视图；不另复制生命周期队列，不能任意跳过native资源阻塞 | [E04](#e04)、[Q01](#q01) |
| LARK-016 / 待真实policy与混流验收 | tenant份额→组内命中/SLO/aging，hot burst有界且cold有可运行份额；只给cold排队份额而无容量不构成进展 | [Q08](#q08)、[BB](#bb) |
| LARK-017 / 待实现功能 | demand/prefetch/writeback/eviction至少保留必要进展与实际credit；分页不是抢占，intent阈值不是hard grant | [S08](#s08)、[L03](#l03) |
| LARK-018 / 探索方案 | 只对必需依赖继承有限优先级、pin byte-time计量；不能强制夺回仍被fence保护的内存 | [S08](#s08)、[L03](#l03) |
| LARK-019 / 设计方案 | 预计工作先扣、actual prefill/decode/IO已耗修正；共享物理容量一次计量；高命中长decode仍占服务；public受益账不等物理副本账 | [E05](#e05)、[S07](#s07)、[Q06](#q06) |
| LARK-020 / 待实现功能 | 有限队列/早拒绝/retry-after/取消与deadline；不可无限重试放大恢复IO，不把已stream重试成新答案 | [Q08](#q08)、[Q06](#q06) |
| LARK-021 / 固定caller事实与验收场景 | 冷miss/pooled hit/Agent返回/突发共享/取消尾部；FULL普通host路径；DirectLinker/P-D独立，不拼接现成功能 | [E02](#e02)、[E04](#e04)、[BA](#ba)、[BB](#bb) |
| LARK-022 / 固定事实+契约要求 | placement/HOST_COMMIT/HBM_ALLOC/逐层read-safe/whole release_safe各有owner；保留H2D与forward逐层重叠，不能加全层barrier | [E04](#e04)、[E02](#e02) |
| LARK-023 / 固定事实与设计约束 | logical abort≠physical reclaim，late ACK只结算旧op/generation refs；未知DMA/drain不提前free/退款，不令旧attempt复活 | [E02](#e02)、[S01](#s01)、[E06](#e06) |
| LARK-024 / 上层协议要求，非Store自动保证 | 不可变content key、禁same-key Upsert、写/重试串行；PutEnd无generation；read lease不保护原地Upsert | [S05](#s05) |
| LARK-025 / 固定事实 | read time lease/soft硬pin/group/Exist授lease分别计量；group非事务；pin不证明DMA停止；query无consume也延长lease | [S07](#s07)、[R07](#r07) |
| LARK-026 / 固定事实与条件扩展要求 | setup/client域≠同worker每APItenant，MEMORY quota≠IO/GPU公平；强Store域隔离需可信per-batch参数，不mutable globaltenant | [S06](#s06)、[Q02](#q02)、[S08](#s08)、[S10](#s10) |
| LARK-027 / 固定源码纠偏后的合同 | namespace授权、完整对象key、verified-group三个独立gate；两marker均sglang-hicache；group失败不等所有object命中失败 | [Q04](#q04)、[Q05](#q05)、[S05](#s05) |
| LARK-028 / 设计要求 | 真实weights/tokenizer/positions/LoRA/dtype/layout/shard/多模态身份；served name/统计version不能代替实际artifact或physical epoch | [A03](#a03)、[S05](#s05)、[V04](#v04)、[CP07](#cp07) |
| LARK-029 / 研究方向，NOT_READY | engine-owned generation与单controller coarse exclusive retire；必须真实stop/join/fence/旧缓存失效；diag/startup不是lease | [A03](#a03)、[E06](#e06)、[BS](#bs) |
| LARK-030 / 硬owner契约需求 | 旧backup/D2H/PUT携带不可变旧key/backend或drain后rebind；只挡读不挡旧producer会污染新generation | [S05](#s05)、[E06](#e06) |
| LARK-031 / 待实现功能 | gap/disconnect先撤credit，后台有界reconcile与epoch隔离；worker index snapshot不能泛化独立sharedset | [Q03](#q03)、[Q05](#q05) |
| LARK-032 / 固定底座及边界 | host eligibility/sync filter-score-picker与原生booking/rollback；不得逐候选阻塞RPC或建第二allocator/queue；cached DRR只local | [Q01](#q01)、[Q06](#q06)、[Q08](#q08) |
| LARK-033 / 拟定新增合同 | attempt-aware ADMISSION_COMMITTED/REJECTED/stale/revoked/partial/fail；普通503不足决定retry-safe；已开始输出不能透明重试 | [E05](#e05)、[Q06](#q06) |
| LARK-034 / 探索方案 | 按完整关键路径、合法prefix、保留后驻留成本选读/部分读/重算；目录hit不总恢复；保留重算对照 | [Q07](#q07)、[R01](#r01) |
| LARK-035 / 条件性探索 | 仅有独立资源和slack才有限恢复/重算竞速；独立buffer；满负载通常恶化，不默认双跑 | [RX02](#rx02)、[CP23](#cp23) |
| LARK-036 / 探索与后续测量决议 | leader/waiter去重source IO，目标H2D/decode仍独立；原生tree读后去重不是端到端single-flight；最后waiter等drain | [AG04](#ag04)、[AG05](#ag05)、[CP02](#cp02) |
| LARK-037 / 用户试点下探索功能 | pause/tool interval/return/final、softTTL分层retention与hint预取；可选提示，不等read lease；错误预取/驻留挤占普通流量计量 | [AG01](#ag01)、[AG02](#ag02)、[R02](#r02) |
| LARK-038 / 探索方案 | 跨API轮次/program/branch服务、IO、retention及关键路径预算；新请求不能重置公平账；不得对所有Agent默认优待 | [AG03](#ag03)、[E05](#e05)、[RX05](#rx05) |
| LARK-039 / 探索方案 | COW共享不可变prefix、beam/fork/RLtrajectory及policy revision；旧权重inflight静默和namespace，环境/tool状态不随KV自动恢复 | [CP01](#cp01)、[AG03](#ag03)、[RX05](#rx05) |
| LARK-040 / 探索候选 | 训练step HBM/IO与推理cache residency协调；optimizer状态不是L1，GPU资源边界先明确，非既有部署事实 | [RX05](#rx05)、[CP24](#cp24) |
| LARK-041 / 探索候选，需对照LRU | 价值/bytes/FLOPs/重用概率与deadline共同决定存入/保留/晋升；FancyEviction反证复杂算法必胜；容量大时LRU可强 | [R03](#r03)、[CP20](#cp20) |
| LARK-042 / 探索设计 | L1活跃、L2近期价值、L3长尾，非每访问逐层promote；copy/evict/write/retain成本和prefetch precision实测 | [L04](#l04)、[R03](#r03)、[S08](#s08) |
| LARK-043 / 探索设计 | 热点少量replica消尾部，cold少副本，unique vsphysical bytes区别；全局复本与私有active HBM不同，共享quota记真实副本 | [S07](#s07)、[RX03](#rx03)、[CP22](#cp22) |
| LARK-044 / 探索候选 | queue prefix ancestor deadline/累计受益引导保留和restore；PEEK等paper候选不等本引擎可用功能；冷producer收益需测 | [RX01](#rx01)、[CP21](#cp21) |
| LARK-045 / 探索候选 | 有限cohort等待与吞吐/尾延迟交互，singleton保留lane；真实token identity；大cohort不能饿死普通请求 | [CP03](#cp03)、[R04](#r04) |
| LARK-046 / 探索候选 | Hydragen/Cascade共享注意力计算与容量/IO去重分别比较；kernel×router二乘二，不因存了相同KV自动有算子收益 | [CP04](#cp04)、[F02](#f02)、[BX](#bx) |
| LARK-047 / 探索候选 | 高价值public prompt真实token化后预填充、版本化发布与撤销；weights/tokenizer/RoPE/template/namespace版本一致；预存价值抵费用 | [R05](#r05)、[CP05](#cp05) |
| LARK-048 / 探索候选 | scaleout预热、rolling upgrade、scalein drain/selective transfer；不全量迁移；恢复KV≠恢复RNG/output/tool业务状态 | [R06](#r06)、[CP06](#cp06) |
| LARK-049 / 探索设计 | 热digest/batch longest-prefix/shard/global object count/主控CPU；approx snapshot过期保守撤credit；不是全局同步大事务 | [R07](#r07)、[Q05](#q05) |
| LARK-050 / 探索运维门槛 | Master HA、metadata OpLog、故障后cache rebuild/eviction保护；best-effort replica不同于源tokens/权重持久性，需部署故障验证 | [RX07](#rx07)、[CP19](#cp19) |
| LARK-051 / 探索产品候选 | 公共/私有share domain、TTL/pin配额、context handle与计费；不能用hash存在证明授权；同physical共享账与用户受益账分离 | [RX06](#rx06)、[CP25](#cp25) |
| LARK-052 / 探索候选 | lossless codec/hot可消费cold紧凑/多表示边际容量；解压CPU/GPU/SM/HBM临时成本，不只测压缩比 | [R08](#r08)、[CP07](#cp07)、[CP08](#cp08) |
| LARK-053 / 探索候选 | KIVI类非对称量化bits+scale+position与误差预算；KV与weight NVFP4严格分开；质量/布局/数值兼容独立验收 | [R08](#r08)、[CP09](#cp09) |
| LARK-054 / 探索与框架支持审计候选 | latent cache native表示、rank replication/广播和重复读成本；rank-replicated不是容量÷TP，DirectLinker/main能力不能泛化 | [R08](#r08)、[CP09](#cp09) |
| LARK-055 / 受约束release入口事实，组合待验 | head/rank重组、两端LCM/page_head与完整模型布局矩阵；release有tp_lcm入口；不是任意TP/attention互操作 | [V04](#v04)、[R10](#r10)、[CP10](#cp10) |
| LARK-056 / 未来扩展要求，现成字段不等实现 | FULL/SWA/Mamba状态合法checkpoint边界/连续prefix集合；当前caller scalar MIN；sidepool完整性不等合法集合求交 | [R10](#r10)、[CP11](#cp11) |
| LARK-057 / 探索候选 | CacheBlend/CacheCraft融合/位置相关重算与质量；相同文档不等上下文KV相同；完整prefix vs suffix不同 | [R09](#r09)、[CP15](#cp15) |
| LARK-058 / 探索验收 | 量化×RAG融合/多表示联合质量与任务成功；多个单独质量通过不保证组合误差可相加 | [CP15](#cp15)、[BX](#bx) |
| LARK-059 / 未来设备产品范围与接口要求 | range/layer/priority/deadline/physical credit、completed/drained/fault；DMA alignment/真实cancel/reset/shutdown必须设备receipt | [L01](#l01)、[L02](#l02) |
| LARK-060 / 探索方案 | page-layer-head聚合、批量metadata/object query、chunk上限；逻辑小页/物理大块折中，partial/cancel/out-of-order精确处理 | [L03](#l03)、[R11](#r11) |
| LARK-061 / 探索方案 | write admission/write-evict/write-through、闪存GC/endurance/writeamp；长期read复用得抵写与寿命成本，不默认全写 | [L04](#l04)、[R11](#r11)、[BC](#bc) |
| LARK-062 / 探索候选 | CPU/NIC-DPU/GPU IO prepare/codec/index执行位置比较；Tutti等不是Mooncake验证结果；GPU SM干扰计量 | [R11](#r11)、[L01](#l01) |
| LARK-063 / 高风险远期研究候选 | InstInfer类输出+LSE归并、query/mask/scale和能耗带宽；不把CMX IO称SSD attention；float非bitexact；先硬件实证 | [R12](#r12)、[CP18](#cp18) |
| LARK-064 / 高风险独立候选 | 主动decode offload/稀疏检索频率与质量代价；300GiB/s示例非目标机器结果，reuse收益不消除decode bandwidth | [R12](#r12)、[CP18](#cp18)、[BX](#bx) |
| LARK-065 / 探索候选 | slack预算下早L3晚L2/L1逐层deadline pipeline；目标关键层stall/resident byte-time，不追峰值带宽 | [CP16](#cp16)、[R02](#r02) |
| LARK-066 / 探索方案 | 快准入与慢副本/retention反馈分开，hysteresis/min residency/迁移上限；非多个调度器独立发冲突决定；counterexample突发/漂移 | [RX03](#rx03)、[CP22](#cp22) |
| LARK-067 / 探索候选 | 剩余miss/attention work决定CP/prefill placement并计转换成本；固定CP候选先验后动态；prefill论文不自动端到端赢家 | [RX04](#rx04)、[CP12](#cp12)、[CP17](#cp17) |
| LARK-068 / 探索验收 | 恢复/队列/计算校准、ordering regret、model/length变化及controller开销；查询hit比不是predictor效用，校准不等公平/SLO | [Q07](#q07)、[BV](#bv)、[BB](#bb) |
| LARK-069 / 验收设计 | baseline→pool→readiness/fairness→Agent→L3，含2×2交互；同DRAM/HBM/model/quality/trace/output，资源/收益分母固定 | [B00](#b00)、[BA](#ba)、[BB](#bb)、[BC](#bc)、[BX](#bx)、[F01](#f01)、[F02](#f02)、[F03](#f03)、[F04](#f04) |
| LARK-070 / 验收规范 | request/token/hit/restored token成本、总或增量资源、pin byte-seconds；价格/SLO/真实混比缺失不裁经济PASS，账不换分母 | [A02](#a02)、[BB](#bb)、[BC](#bc)、[R01](#r01) |
| LARK-071 / 验收规范 | 按tenant×class×冷热×输入输出报告尾部/拒绝/cancel/oldest age；hot改善不能掩盖cold、长decode或Agent慢类，offered保留 | [BB](#bb)、[BV](#bv)、[BE](#be) |
| LARK-072 / 验收设计 | task/turn/episode completion、tool等待、质量与成功；小模型smoke不代表Agent代码质量，外部工具计时独立 | [BE](#be)、[AG01](#ag01)、[BB](#bb) |
| LARK-073 / 契约/观测规范 | attempt/op/generation/allocation、单owner seq/clock与cause链接；跨机monotonic不能直接相减，模拟事件不physical proof | [B00](#b00)、[E01](#e01)、[E05](#e05)、[VV1](#vv1) |
| LARK-074 / 实际CPU supporting成果 | 逐turn permit/真实history/toolwait释放/cancel/deadline；synthetic labels非权益；SDK invocation不是wire/server dispatch | [I01](#i01)、[B00](#b00) |
| LARK-075 / 固定观测合同 | actual server cached_tokens缺失null、SDK default0不observed；cachedtokens无法区分tier、READY、lease和IO，不填虚构serverqueue | [B00](#b00)、[BB](#bb) |
| LARK-076 / 固定观测合同 | query hit→host prefetch→request reuse三计数，窗口不能摊RID；多个P99不能相减；storage requested-page bandwidth不是wire或restore latency | [B00](#b00)、[BB](#bb) |
| LARK-077 / 已核窄历史supporting evidence | metadata小修/diag/HRRN/Store与TE有界CPU/CUDA各保留范围；draft非merge/部署；缺依赖/fixture/139不是产品RED | [I01](#i01)、[B00](#b00) |
| LARK-078 / 已核CPU characterization | soft limit/FIFO activequeue/host tail ACK排free后实际drain；无生产修改；不证明KV bytes/source pin/DMA/GPU安全 | [I01](#i01)、[E03](#e03)、[B00](#b00) |
| LARK-079 / 已核CPU控制边界与纠偏 | is_fully_idle检查ongoing，stop失败保留owner/异常worker无ACK拒detach；direct bypass不是普通可达bug；noop drain/人工ongoing不测实际acquire | [E06](#e06)、[I01](#i01)、[B00](#b00) |
| LARK-080 / 历史有界CUDA supporting result | 单卡normal copy/kernel/event/4MiB byteverify+later资源观察；首budget abort和wrapperFAIL保留；当前无机器、不SG/TE/RDMA/shutdown | [B00](#b00)、[BA](#ba) |
| LARK-081 / 未执行的静态验收计划 | pins/ABI/import/kernel→device-only evict host restore→TCP存储恢复；flush_cache也清host，不能冒称host命中；无真实endpoint/perf | [V05](#v05)、[BA](#ba) |
| LARK-082 / 上一版局部执行基线事实 | 20逻辑core/2deferred、9draft/0统一candidate、T00 receipt；不得反向宣称所有早期探索已coverage；本轮待comprehensive ledger/J | [I01](#i01)、[S00](#s00) |
| LARK-083 / 验收规范 | child receipt解除开发依赖，hard物理gate/ACTIVE/credit/部署独立；unknown与拒绝实现、完整consumer；不通过依赖环自授权 | [BS](#bs)、[PH](#ph)、[RB](#rb) |
| LARK-084 / 用户近期执行规范的文档依据 | 完整featurefreeze后统一批，变更/失败影响closure才复测；上下文reader核显式要求；不是不写必要unit/反例 | [B00](#b00)、[BA](#ba)、[BB](#bb)、[BC](#bc)、[BX](#bx) |
| LARK-085 / 上一版范围决定，非用户取消研究 | session retention/singleflight测分布后实施或measured no-change；无数据不能自动no-change，不将deferred当完成或必永久排除 | [AG01](#ag01)、[AG04](#ag04)、[BE](#be) |
| LARK-086 / 研究决策候选 | 低复用、本地足够、decode主导/大LRU/满负载hedging的负收益；不能仅列支持论文；20-30%例子不是业务验收门槛 | [R01](#r01)、[R03](#r03)、[RX02](#rx02)、[RD](#rd) |
| LARK-087 / 来源边界 | 320卡与8卡smoke环境是文章历史，不是现有可用部署；内部地址脱敏，当前无GPU，不新增SSH/probe | [V01](#v01)、[A02](#a02)、[B00](#b00) |
| LARK-088 / 明确来源MISSING | 微信参考原文未读；captcha不能代正文，不能用论文补读receipt；需求覆盖与第三方收益主张均标未可核，不推已验证 | [S00](#s00) |

## 输入与未决gate

| gate | consumer / axis | UNKNOWN effects |
|---|---|---|
| A02 | BB,BC,BV / performance_slo_economics | NOT_EVALUATED/BLOCKED; resource-unit comparison may run |
| L01 | L02,L03,L04,BC / device_correctness,integration | BLOCKED; no fake device support |
| V01 | B00,BA,BB,BC,BV / actual_runtime_model_profile | BLOCKED for relevant batch |
| SRC-WECHAT | S00 / MISSING_BODY | URL cannot open; HTML captcha only; article title/claims/denominators unknown |
| SRC-CHAT | S00 / PARTIAL_UNAVAILABLE | 4 API empty turns + 2 compactions; available messages only; no raw transcript full claim |
| SRC-PDF | RD / METADATA_ONLY_OR_SELECTED | 5 Lark attachments enumerated only; primary papers P01–21 selective; accepted research implementation must obtain applicable complete primary/code |
| SRC-GPU-RAW | B00 / PARTIAL_TAIL | raw historical run1/run2 point-array tails not reread this audit; limited conclusion uses full adjudication/postcheck, not recomputed peak |

静态结构：112nodes/355unionedges（含44guards），cycle0/dangling0/all112从5roots可达；52R/88concept无unmapped。Unknown条件包BLOCKED；仅graph结构检查，不是产品测试/J PASS。

## J/G/I 发布交接

J已实际审全部receipt/R/88concept/domainatom/consumer/依赖/guard/原硬父及59独立包的native mapping并整体PASS。GsoleGithubwriter固定SG946独立docsbranch/draftPR存3sanitized资产；Map唯一状态权威exactSHAblob/raw导航。G按现票扩scope/checklist与新独立package收敛，不为112逻辑包机械建票；shared producer、singleflight、cohort、actual attention 保持独立AC。IsoleLarkwriter保完整解释/研究disposition与JSONblob导航，不建第二状态表。本轮未产品实现/测试/GPU/SSH/remote mutation。

## 子能力 selector 的固定解释

方向accepted不等全部子能力accepted：R08 codec/quant/MLA、RX04 nativePD/P-bypass/CP、V04 host/cache/buffer/direct分别签selector；unknown阻对应选择分支，无选择不授支持。首BA仅SG环境与correctness fixture，不等vLLM第二环境或生产主模型输入；所选生产profile确需某能力时升入其freeze必需scope。详细selected_capabilities guard在JSON。

## 集中修订 receipt

S10单独tenantmode需求decision，setupdomain/namespace/Engine service-retention额度先reuse；只有明确强perAPI Store物理quota才S06 perbatch consumer，Q04/BB无此无条件前置。code_scope按固定报告真实caller，decision/audit为DOCUMENT_ONLY，新增hook显式PROPOSED；S08controller/URC/backup、E05/E07actualresult、Q02metadata/handlerchain分别归属。AG05仅once-restore，CP02仅cold共同prefill生产。所有9report actualread receipts已统一清除旧pending字段。

EC12集中补齐：RX02/CP23中cost-aware victim/retraction独立子selector，native机制可据same-shape work/ITL/goodput/waste comparator签no-change/defer；只有明确selected才窄接nativevictim→合法恢复/重算→actualresultconsumer，不将hedging或HRRN修复冒称已覆盖抢占选择。

## 冻结审阅回执

J overall PASS 仅授可用来源/已知需求规划、112fine节点与59独立包native映射（19existing/40proposed）。已批准proof固定为 work/coverage/completeness-review-approved.md；SHA256 ea0ea421e30aaa17e195c168ee4807e4e6d8370b3bfb3e0296be53ebe92aae13。9draft仍unmerged、设备/physical safety/sharedcredit/SLO/economics/deploy轴没有升级，所有unavailable/selected source gates保留。G/I按已授权发布并observe/readback，selected checklist能力执行前须绑定唯一真实candidate child及适用deps/batch；执行实时状态只在 [canonical Map](https://github.com/xray-infra/sglang/issues/1)。metadata-only更新不改112/355/44结构。
