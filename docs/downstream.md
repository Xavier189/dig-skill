# Dig Downstream Contract

## 结论

dig 没有前置流程，也没有强制后继。它负责把未知、分叉或缺陷转成可消费的 shared state；后续动作由当前还缺什么决定，而不是由“任务大不大”决定。

“没有前置”指没有必须先跑的业务 skill 或 workflow；host 的 system/developer/user instructions、权限、安全边界和必要上下文仍然是 ambient constraints。

```text
session / agent work
        │
        ├─ 已清楚且 sound ───────────────────────→ downstream work
        │
        └─ direction / decision / validity uncertainty
                           │
                          dig
                           │
                    shared state ready
                           │
       ┌───────────┬───────┼────────┬─────────┬──────────┐
    evidence    prototype  direct   design   planning  domain review
       │           │       delivery    │         │          │
       └───────────┴─────────── 可在新事实改变决策时回到 dig ─┘
```

## Handoff 只传递状态

短会话无需生成新文档。只有跨 agent、跨 session、存在精确约束或决定被修订时，才输出 Handoff Snapshot：

```markdown
## Ready state
## Carry forward
## Assumptions, deferred items, and accepted risks
## Boundaries
## Success evidence
```

- `Ready state` 描述当前可以做什么，不命令必须进入哪条流程。
- `Carry forward` 只保留下游会用到的 confirmed decision 与 constraint。
- 未决项必须保留真实状态，不能为了“可以开工”伪装成 confirmed。
- 如果对话本身已完成用户目标，直接 stop，不制造 handoff 文件。

## 下游路线

### 1. Evidence / research

当缺的是可核查事实、现状、指标、法规、兼容性或根因时，先 inspect/research。能安全获取的事实不退回给用户回答。

产物是 evidence、诊断结果或 source-backed recommendation。新事实改变方向或约束时，再进入 dig 更新 shared state。

### 2. Cheap prototype / experiment

当用户只有“看到才知道”、可行性未知，或多个方案的差异无法靠讨论可靠判断时，做最小 prototype、spike、mock、sample 或 experiment。

prototype 用于获得决策证据，不静默升级成 production implementation。

### 3. Direct delivery

当需求 decision-complete、没有可见 material defect、改动局部且可逆时直接交付。任务很大不自动排除 direct delivery；关键是是否还存在会改变路线的决定。

产物是用户要的结果与比例适当的 verification，不附加 memo、reviewer 或 plan theater。

### 4. Design

只有实现选择会 materially 改变 external contract、data model、coupling、failure/recovery、security boundary、migration 或长期维护成本时，才先设计。

设计深度按需要选择：

- inline sketch：选择少、可逆、无需长期 handoff；
- durable design / ADR / spec：跨边界、不可逆、需要多人协作、审批或未来追溯。

有效设计应解释 chosen direction、被否决的 material alternative、reversibility、failure/recovery 和为什么当前抽象不是 YAGNI。无需为填模板讨论无关维度。

### 5. Planning

plan 是 coordination state，不是设计完成后的奖章。只在工作多步骤、长时间运行、需要恢复/交接、并行依赖或复杂 rollout 时使用。

默认在当前 task state 中维护；只有用户、团队约定或跨 session handoff 需要时才落盘。不得默认创建 `docs/plans/`。

### 6. Domain review

独立 review 只用于显式要求、高风险、责任隔离或确实需要第二专业视角的场景。按风险选 reviewer：Security、Privacy、Legal、DBA、SRE、Domain Expert 或 Software Architect。

Software Architect 只评实际 software architecture；任务大、文件多或经过 dig 都不是调用理由。产物是 findings、处理结论与 accepted risks，不是风格偏好清单。

### 7. Stop

Discover 得到方向、Clarify 得到决定、Challenge 得到可信审查，可能已经是完整交付。用户没有要求继续时，到此结束。

## 为什么删除 `big-task`

旧 `big-task` 把四个独立问题绑定为固定顺序：

1. 需求是否不清楚；
2. 实现是否需要设计；
3. 风险是否值得独立 review；
4. 执行是否需要 plan。

这四项没有共同触发条件。用 task size 一次性决定会产生四类错误：清晰任务被重复澄清、可逆任务被过度设计、低风险任务被强制 review、短闭环被迫落盘 plan。

因此保留其有效设计原则，删除编排 skill；路由纪律放在全局 instructions，领域深度由相应 skill/agent 按需提供。
