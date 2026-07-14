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

这些分支不是必须六选一的终态。每次只解决当前最靠前的缺口：例如先 research 得到事实，事实改变方向时回到 dig；方向稳定后再判断是否需要 design；只有 rollout 真的需要协调时才增加 planning。

## 先分清三件事

`skill`、`subagent` 和文件分别解决能力、执行拓扑与状态延续问题。可以把它们理解成“操作手册/工具箱”“临时增派的同事”“交接单/档案”。它们可以组合，但互不自动触发。

| 当前缺口 | 选择 | 适合的信号 | 不应成为触发条件 |
|---|---|---|---|
| 同类工作反复出现，每次都要重新学习领域规则、schema、工具或稳定步骤 | 窄 skill | 有清楚 trigger、可复用知识/资源、可检验 output contract | 任务大、刚做完 dig、只发生过一次 |
| 一次执行中存在真正独立的 workstream，或高风险事项需要隔离上下文的第二视角 | subagent | 可并行、输入边界清楚、结果能独立验收，或 reviewer independence 有价值 | 文件多、步骤多、为了显得流程完整 |
| 精确状态必须离开当前对话后继续存在 | durable artifact | 跨 session、长时间恢复、审批/审计、多人共享 | 每次 dig、每个 plan、同 session 内可直接传递 |

### 何时才提取窄 skill

优先按稳定的业务能力或专业能力拆，而不是按“dig 之后的第几步”拆。例如：

- `invoice-reconciliation` 可以封装固定的账单 schema、匹配规则、异常分类和校验脚本；
- `privacy-impact-review` 可以封装稳定的 privacy lens、证据要求和报告 contract；
- `after-dig`、`big-task`、`do-design-then-plan` 只是编排名称，没有稳定领域能力，不应成为 skill。

当前版本不新增通用 `technical-design`、`rollout-planning` 或业务 umbrella skill。先观察真实任务中是否反复出现“agent 每次都重新发明同一套方法、遗漏同一类检查、重复拼同一段工具代码”；有稳定重复后再提取，比先画完整 skill tree 更可靠。

### 何时才用 subagent

subagent 是一次运行中的 worker，不是下一阶段，也不会自动获得 dig 的 shared state。派发时必须把必要的 Handoff Snapshot、文件入口、允许修改的范围和验收证据一起传入。

适合的例子：两个 agent 分别核查 API compatibility 和 database migration 影响；Security reviewer 独立审查 encryption design。不适合的例子：需求还在摇摆时让三个 agent 各自实现，或把一个局部改动机械拆成“设计 agent、编码 agent、审核 agent”。

## Handoff 与落盘

dig 默认不自动写文件。短会话无需生成新文档；需要跨 agent、跨 session、保留精确约束或追踪修订时，才 render Handoff Snapshot：

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

Snapshot 放在哪里由延续方式决定：

| 延续方式 | 推荐 carrier | dig 行为 |
|---|---|---|
| 同一 agent、同一 session | 当前 conversation context | 维护 shared state；通常不展示完整 Snapshot，不写文件 |
| 同一 session、换 agent/subagent | dispatch message 中的 inline Snapshot | 只传对方完成任务所需状态；通常不写文件 |
| 新 session、隔天继续、长任务恢复 | 项目约定的 file / issue / task state | 用户或授权 harness 要求持久化时写入；新 session 先读它 |
| 审批、审计、多人长期共享 | spec / ADR / issue / decision record | 按组织 contract 落盘，而不是强行使用 dig 专属格式 |

跨 session 时不能假定新 session 仍拥有旧对话。恢复者应先读取 durable snapshot，再核对 git state、代码、外部事实等会漂移的现状；Snapshot 保存的是当时已接受的决定，不保证所有事实永久有效。

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

## 通俗路由示例

| 用户场景 | 最小合理路线 | 窄 skill | subagent | 是否落盘 |
|---|---|---|---|---|
| “给这个接口多打一条已有格式的日志，字段也确定了” | 直接读代码 → 修改 → targeted test | 不需要 | 不需要 | 不需要 |
| “我想做个能长期积累的个人项目，但完全不知道做什么” | dig Discover → 比较方向；选不出时做 cheap prototype；也可以直接 stop | 不急着建 | 通常不需要 | 当天聊完不写；明确下次继续时可保存 Direction Map |
| “这三个页面我说不清喜欢哪种风格，看到才知道” | dig → 2–3 个 mock/sample → 根据反馈更新 shared state | 只有反复生成同类品牌稿且有稳定规范时才考虑 | 可并行做视觉参考，但不是默认 | 同 session 不写；品牌决策要复用时写 brief |
| “把 8 个调用点改用已有 `getUserV2`，兼容与测试都已确认” | direct delivery → 针对性验证 | 不需要 | 不需要；8 个调用点本身不是并行理由 | 不写 plan |
| “设计一份匿名员工调研，匿名边界和结果使用方式还没定” | dig Clarify → 必要的 policy research → 高风险时做 Privacy/HR/Legal review | 反复执行同类评估时可提取 domain skill | 只有独立专业判断有价值时使用 | 若需审批或下个 session 继续，写 Brief；绝不找 Software Architect |
| “给生产身份证号做 envelope encryption、在线轮换和零停机迁移” | 查 KMS/现状证据 → technical design → Security/Privacy/DBA review → rollout 复杂时 planning | 已有稳定 domain skill 就复用，不为本任务临时造一个 | 适合独立 security review 或并行盘点 migration 影响 | 通常写 ADR/spec；跨 session rollout 再维护 durable task state |
| “每月都要把三个供应商账单和内部订单对账” | 第一次先完成并验证；规则稳定且重复后提取 `invoice-reconciliation` | 适合，因为 schema、匹配规则和校验可复用 | 供应商输入互相独立且量大时可并行 | skill 保存方法；每次运行报告按审计需要保存，两者不是同一个文件 |
| “这轮 dig 已确认账单导出需求，交给另一个 agent，明天继续” | render Handoff Snapshot；下一位 agent 读取后再选 direct/design/research | 不需要新 skill | 同 session 可把 Snapshot 直接放进派发消息 | 明天新 session 必须使用 durable carrier，例如 `docs/clarity/YYYY-MM-DD-billing-export.md` |

三个容易混淆的对照：

1. **Design 决定怎么做，planning 决定怎么协调执行。** 一个跨服务迁移可能两者都需要；一个单人当天完成的高风险算法选择可能需要 design，但不需要 plan。
2. **Domain review 决定是否值得第二专业视角，subagent 只是承载这个视角的一种方式。** reviewer 也可以是人、工具或当前 agent 的 evidence-backed self-review。
3. **Handoff Snapshot 是状态内容，file 只是 carrier。** 同 session 可以直接随消息传递；跨 session 才需要可靠的 durable carrier。

## 为什么删除 `big-task`

旧 `big-task` 把四个独立问题绑定为固定顺序：

1. 需求是否不清楚；
2. 实现是否需要设计；
3. 风险是否值得独立 review；
4. 执行是否需要 plan。

这四项没有共同触发条件。用 task size 一次性决定会产生四类错误：清晰任务被重复澄清、可逆任务被过度设计、低风险任务被强制 review、短闭环被迫落盘 plan。

因此保留其有效设计原则，删除编排 skill；路由纪律放在全局 instructions，领域深度由相应 skill/agent 按需提供。
