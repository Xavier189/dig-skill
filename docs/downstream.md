# Dig Downstream Contract

## 结论

dig 没有前置流程，也没有强制后继。它负责把未知、分叉或缺陷转成可消费的 shared state；后续动作由当前还缺什么决定，而不是由“任务大不大”决定。

“没有前置”指没有必须先跑的业务 skill 或 workflow；host 的 system/developer/user instructions、权限、安全边界和必要上下文仍然是 ambient constraints。

dig 与下游不是一棵单选流程树，而是几组正交判断：

| 维度 | 选项 |
|---|---|
| Shared understanding | dig Discover / Clarify / Challenge / narrow STRUCTURE-only / skip |
| Evidence | inspect / research / diagnose / prototype / none |
| Solution shaping | direct / compact design / durable design |
| Execution topology | primary agent / subagent / human or tool reviewer |
| Coordination | inline task state / plan |
| Assurance | proportionate verification / domain review |
| Persistence | conversation / inline Snapshot / durable carrier |

这些维度可以组合。例如一个明确的博客部署可以跳过 dig，同时需要 inspect 当前配置、直接修改、维护简短 plan 并做 smoke test；一个模糊的小重构可能先 Clarify，却完全不需要 subagent、durable design 或落盘。

## 任意 starting point 使用同一个 gate

```text
idea / request / document / repo / folder / existing situation
                              │
             ├─ 只缺事实、根因或可行性 ──→ inspect / research / diagnose / prototype
             ├─ 缺方向或选择依据 ─────────→ dig Discover
             ├─ 缺 human-owned decision ──→ dig Clarify
             ├─ 要检验或已有 material defect → dig Challenge
             ├─ 只需保存 shared decisions ─→ narrow STRUCTURE-only
             └─ action-ready、无已见 material defect → skip dig
```

来源、载体、领域、生命周期阶段和任务大小都不选择路线。查得到的事实由 agent 自己查；局部、可逆且不改变 contract 的实现选择由 agent 自己承担；只有会 materially 改变结果且必须由人负责的选择才进入 Clarify。跨领域成对案例见 [scenarios.md](scenarios.md)。

## 先分清三件事

`skill`、`subagent` 和文件分别解决能力、执行拓扑与状态延续问题。可以把它们理解成“操作手册/工具箱”“临时增派的同事”“交接单/档案”。它们可以组合，但互不自动触发。

| 当前缺口 | 选择 | 适合的信号 | 不应成为触发条件 |
|---|---|---|---|
| 同类工作反复出现，每次都要重新学习领域规则、schema、工具或稳定步骤 | 窄 skill | 有清楚 trigger、可复用知识/资源、可检验 output contract | 任务大、刚做完 dig、只发生过一次 |
| 一次执行中存在真正独立的 workstream，或高风险事项需要隔离上下文的第二视角 | subagent | 可并行、输入边界清楚、结果能独立验收，或 reviewer independence 有价值 | 文件多、步骤多、为了显得流程完整 |
| 精确状态必须离开当前对话后继续存在 | durable artifact | 跨 session、长时间恢复、审批/审计、多人共享 | 每次 dig、每个 plan、同 session 内可直接传递 |

### 何时才提取窄 skill

领域知识本身通常先是文档、schema、配置、分类体系、操作惯例或权威数据源，不自动成为 skill。只有下面四项全部成立，才进入 skill 候选：

1. **Trigger 可识别**：能说清什么请求或情境应加载它；
2. **Reusable payload 存在**：包含通用模型不会稳定掌握的方法、规则、schema、脚本、模板或工具集成；
3. **Boundary 可验收**：能说清输入、输出和何时完成；
4. **应该按需加载**：不是 scope 内每次任务都必须遵守的短规则。

并且至少满足一个价值信号：真实任务中反复重新发现；同类错误反复发生；操作虽不频繁但高风险、脆弱或验证成本高。

先判断内容真正属于什么：

| 内容 | 更合适的载体 | 例子 |
|---|---|---|
| scope 内始终生效的短规则 | `AGENTS.md` / host instructions | Java 项目统一构建命令、禁止修改生成文件 |
| 项目事实、领域术语、业务规则 | 普通文档、schema、配置、权威系统 | 订单状态含义、退款期限、内部 API contract |
| 某一次需求的决定与未决项 | issue、Requirements Brief、Handoff Snapshot | 本次“订单撤回”的状态边界与 accepted risk |
| 可重复、按需触发的方法与资源 | skill | 状态机变更影响分析、隐私影响评估、对账 workflow |
| 必须确定执行的重复机械操作 | script/tool；必要时由 skill 调用 | schema 校验、报表转换、固定格式打包 |

优先按稳定的业务能力或专业能力拆，而不是按“dig 之后的第几步”拆。例如：

- `invoice-reconciliation` 可以封装固定的账单 schema、匹配规则、异常分类和校验脚本；
- `privacy-impact-review` 可以封装稳定的 privacy lens、证据要求和报告 contract；
- `after-dig`、`big-task`、`do-design-then-plan` 只是编排名称，没有稳定领域能力，不应成为 skill。

当前版本不新增通用 `technical-design`、`rollout-planning` 或业务 umbrella skill。先观察真实任务中是否反复出现“agent 每次都重新发明同一套方法、遗漏同一类检查、重复拼同一段工具代码”；有稳定重复后再提取，比先画完整 skill tree 更可靠。

### 工作区还是全局

选择能够容纳全部假设的最窄 activation scope。下面四问全部回答“是”时，能力适合 global；如果一开始就明确跨无关项目成立，可以直接 global，不必先经历 workspace-local 的“晋升流程”：

1. 去掉仓库名、公司名和内部术语后，能力仍完整成立；
2. 放进两个无关项目也不会给出错误假设或危险命令；
3. 不包含私有 schema、业务政策、环境地址、secret 或团队专属流程；
4. 它的更新节奏不依赖某个项目的代码与 release。

| Scope | 放什么 | 典型例子 |
|---|---|---|
| workspace | 跟随当前工作对象演进、带项目/domain/资料集假设的 instructions、docs、skill、script | `order-change-impact`、博客 runbook、笔记库分类约定、订单领域 reference |
| global | 跨无关项目仍成立的个人偏好、通用方法、格式/工具能力、通用 custom agent role | `dig`、`diagnose`、`humanizer-zh`、通用 `database-optimizer` role |
| hybrid | global 方法 + workspace 事实/adapter | global privacy-review 方法读取当前项目的数据分类与 retention 文档 |

“源码放在哪里”与“能力在哪些任务中激活”也不是一回事。canonical source 可以位于可版本管理的独立仓库，installed entry 使用 symlink；workspace-specific source 则跟随对应 workspace，不做 global activation。具体 discovery 路径属于 host integration detail，不属于 dig contract；本项目的安装方式见 [README](../README.md#安装)。

workspace 也不等于代码仓库：它可以是博客、notes vault、资料目录、运维环境或个人项目。判断依据始终是这些假设在哪个边界内成立，而不是目录里有没有源码。

### 何时才用 subagent

subagent 是一次运行中的 worker，不是下一阶段，也不会自动获得 dig 的 shared state。派发时必须把必要的 Handoff Snapshot、文件入口、允许修改的范围和验收证据一起传入。

与用户共同澄清 owner decision 默认留在 primary agent，因为这里最依赖完整对话与即时反馈。subagent 可以在 dig 期间做边界明确的事实核查，也可以在 shared state 稳定后承担独立 implementation/review workstream，但不应代替主会话各自猜需求。

派发前检查四项：

1. 被委托的问题或 contract 已稳定到不同 worker 不会各自猜一套；
2. workstream 能用明确输入、修改边界和 output contract 独立描述；
3. 并行节省的时间，或独立视角降低的风险，明显大于传递与合并成本；
4. 主 agent 能验证结果并负责最终整合。

任一不成立，继续由当前 agent 完成。适合的例子：订单撤回规则确认后，两个 agent 分别盘点 payment 与 inventory 影响；Security reviewer 独立审查 encryption design。不适合的例子：需求还在摇摆时让三个 agent 各自实现，或把一个局部改动机械拆成“设计 agent、编码 agent、审核 agent”。

ad hoc subagent 通常不需要创建配置文件。只有某个独立角色反复出现，并且确实需要稳定的独立 instructions、tools、model 或权限边界时，才创建 custom agent。方法需要被当前 agent 直接应用时做 skill；工作需要交给另一个独立 context 时才考虑 agent。同一领域可以同时有 skill 和 agent，但两者解决的问题不同。custom agent 的 scope 同样遵循“容纳全部假设的最窄边界”，具体配置位置由 host 决定。

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

plan 是 coordination state，不是设计完成后的奖章。只在多步骤工作确实需要依赖/进度协调，或工作长时间运行、需要恢复/交接、存在并行依赖或复杂 rollout 时使用。

默认在当前 task state 中维护；只有用户、团队约定或跨 session handoff 需要时才落盘。不得默认创建 `docs/plans/`。

### 6. Domain review

独立 review 只用于显式要求、高风险、责任隔离或确实需要第二专业视角的场景。按风险选 reviewer：Security、Privacy、Legal、DBA、SRE、Domain Expert 或 Software Architect。

Software Architect 只评实际 software architecture；任务大、文件多或经过 dig 都不是调用理由。产物是 findings、处理结论与 accepted risks，不是风格偏好清单。

### 7. Stop

Discover 得到方向、Clarify 得到决定、Challenge 得到可信审查，可能已经是完整交付。用户没有要求继续时，到此结束。

## 通俗路由示例

完整的 product、refactor、optimization、upgrade、mini app、blog、folder organization 与非代码对照见 [场景校准矩阵](scenarios.md)。它刻意使用成对案例验证两件事：同一表面任务可因思考状态不同而走不同路线；相同思考状态跨领域仍走同一路线。案例不定义 trigger。

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
