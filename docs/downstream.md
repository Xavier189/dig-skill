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

## 日常工作中最常见的入口

```text
一句话需求 / ticket / PRD
            │
            ├─ 先查现有代码、业务规则、文档与惯例
            │
            ├─ 现状已决定全部关键行为 ─────────────→ direct delivery
            ├─ 仍有会改变结果的 owner decision ───→ dig Clarify
            ├─ 已有矛盾、错误假设或危险边界 ───────→ dig Challenge
            └─ 只需整理已知决定 ───────────────────→ STRUCTURE-only
```

例如“订单支持撤回”不应该直接展开成 implementation plan，也不应该因为只有六个字就机械追问。agent 先查当前状态机、取消/退款/库存逻辑、权限与审计惯例；查得到的是事实，自己查。剩下“哪些状态允许撤回”“谁能撤回”“已付款后采用退款还是禁止”“是否通知相关方”这类会改变产品行为的决定，再交给产品 owner 澄清。

一份 PRD 也不因格式完整而自动可信：遗漏真实分叉时用 Clarify；“任何时候可撤回”与“审批后不可变更”同时存在时直接给 Challenge finding；内容已经 decision-complete 时跳过 dig。

## 先分清三件事

`skill`、`subagent` 和文件分别解决能力、执行拓扑与状态延续问题。可以把它们理解成“操作手册/工具箱”“临时增派的同事”“交接单/档案”。它们可以组合，但互不自动触发。

| 当前缺口 | 选择 | 适合的信号 | 不应成为触发条件 |
|---|---|---|---|
| 同类工作反复出现，每次都要重新学习领域规则、schema、工具或稳定步骤 | 窄 skill | 有清楚 trigger、可复用知识/资源、可检验 output contract | 任务大、刚做完 dig、只发生过一次 |
| 一次执行中存在真正独立的 workstream，或高风险事项需要隔离上下文的第二视角 | subagent | 可并行、输入边界清楚、结果能独立验收，或 reviewer independence 有价值 | 文件多、步骤多、为了显得流程完整 |
| 精确状态必须离开当前对话后继续存在 | durable artifact | 跨 session、长时间恢复、审批/审计、多人共享 | 每次 dig、每个 plan、同 session 内可直接传递 |

### 何时才提取窄 skill

业务知识本身通常先是文档、schema、配置或权威数据源，不自动成为 skill。只有下面四项全部成立，才进入 skill 候选：

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

默认从 workspace-local 开始。以下四问全部回答“是”，才适合提升为 global：

1. 去掉仓库名、公司名和内部术语后，能力仍完整成立；
2. 放进两个无关项目也不会给出错误假设或危险命令；
3. 不包含私有 schema、业务政策、环境地址、secret 或团队专属流程；
4. 它的更新节奏不依赖某个项目的代码与 release。

| Scope | 放什么 | 典型例子 |
|---|---|---|
| workspace | 跟随代码版本演进、团队共享、带项目/domain 假设的 instructions、docs、skill、script | `order-change-impact`、本项目 release/runbook、订单领域 reference |
| global | 跨无关项目仍成立的个人偏好、通用方法、格式/工具能力、通用 custom agent role | `dig`、`diagnose`、`humanizer-zh`、通用 `database-optimizer` role |
| hybrid | global 方法 + workspace 事实/adapter | global privacy-review 方法读取当前项目的数据分类与 retention 文档 |

“源码放在工作目录”与“能力全局生效”也不是一回事。当前 `dig` 的 source of truth 在这个 Git 仓库，`~/.agents/skills/dig` 只是 global symlink；这既能版本管理，又避免复制两份。项目专属能力则保留在项目仓库，不做 global activation。

一种清晰的目录布局是：

| Activation scope | Canonical source | Integration |
|---|---|---|
| workspace skill | 当前 repo 的 `.agents/skills/<name>/` 或统一的 `skills/<name>/` | 随 repo 提交，由项目 instructions 或 client 的 workspace discovery 加载；不建立 global symlink |
| global skill | 独立、可版本管理的 source repo | symlink 到当前环境的 `~/.agents/skills/<name>`，避免 source 与 installed copy 分叉 |
| Codex global custom agent | `~/.codex/agents/<name>.toml` | user-level role；不得嵌入单一项目才成立的假设 |

### 何时才用 subagent

subagent 是一次运行中的 worker，不是下一阶段，也不会自动获得 dig 的 shared state。派发时必须把必要的 Handoff Snapshot、文件入口、允许修改的范围和验收证据一起传入。

与用户共同澄清 owner decision 默认留在 primary agent，因为这里最依赖完整对话与即时反馈。subagent 可以在 dig 期间做边界明确的事实核查，也可以在 shared state 稳定后承担独立 implementation/review workstream，但不应代替主会话各自猜需求。

派发前检查四项：

1. 被委托的问题或 contract 已稳定到不同 worker 不会各自猜一套；
2. workstream 能用明确输入、修改边界和 output contract 独立描述；
3. 并行节省的时间，或独立视角降低的风险，明显大于传递与合并成本；
4. 主 agent 能验证结果并负责最终整合。

任一不成立，继续由当前 agent 完成。适合的例子：订单撤回规则确认后，两个 agent 分别盘点 payment 与 inventory 影响；Security reviewer 独立审查 encryption design。不适合的例子：需求还在摇摆时让三个 agent 各自实现，或把一个局部改动机械拆成“设计 agent、编码 agent、审核 agent”。

ad hoc subagent 通常不需要创建配置文件。只有某个独立角色反复出现，并且确实需要稳定的独立 instructions、tools、model 或权限边界时，才创建 custom agent。方法需要被当前 agent 直接应用时做 skill；工作需要交给另一个独立 context 时才考虑 agent。同一领域可以同时有 skill 和 agent，但两者解决的问题不同。

以 Codex 的 user-level custom agent 为例，`~/.codex/agents/*.toml` 属于 global scope，适合 `database-optimizer` 这类跨项目角色。绑定单一业务域的 `order-domain-agent` 默认不应放 global；优先保留在项目 harness/instructions 中，除非当前 client 明确支持并需要 workspace agent definition。

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
| “订单支持撤回” | 查当前状态机与既有规则 → Clarify 状态、角色、补偿和通知等 owner decision | 不为一次需求新建；若状态机影响分析长期重复，再做 workspace skill | 需求稳定后，payment/inventory 影响可并行盘点 | 同 session 不写；需产品确认或跨 session 时写 Brief/issue |
| PRD 同时写“任何时候可撤回”和“审批后不可变更” | Challenge 先指出 contract 矛盾 → Clarify 真正状态边界 → 再决定 design/direct | 不需要 | 矛盾未解决前不派发 | 修订后的 requirement 应回写 PRD/issue |
| “订单列表加导出” | 查已有导出惯例；若字段、权限、范围、数据量都能继承则 direct，否则只 Clarify 剩余分叉 | 已有 export skill 就复用，不临时造 | 通常不需要 | 仅在有新业务决定或跨 session 时记录 |
| “给这个接口多打一条已有格式的日志，字段也确定了” | 直接读代码 → 修改 → targeted test | 不需要 | 不需要 | 不需要 |
| “把 8 个调用点改用已有 `getUserV2`，兼容与测试都已确认” | direct delivery → 针对性验证 | 不需要 | 不需要；8 个调用点本身不是并行理由 | 不写 plan |
| “给生产身份证号做 envelope encryption、在线轮换和零停机迁移” | 查 KMS/现状证据 → technical design → Security/Privacy/DBA review → rollout 复杂时 planning | 已有稳定 domain skill 就复用，不为本任务临时造一个 | 适合独立 security review 或并行盘点 migration 影响 | 通常写 ADR/spec；跨 session rollout 再维护 durable task state |
| “每月都要把三个供应商账单和内部订单对账” | 第一次先完成并验证；规则稳定且重复后提取 `invoice-reconciliation` | 适合，因为 schema、匹配规则和校验可复用 | 供应商输入互相独立且量大时可并行 | skill 保存方法；每次运行报告按审计需要保存，两者不是同一个文件 |
| “这轮 dig 已确认账单导出需求，交给另一个 agent，明天继续” | render Handoff Snapshot；下一位 agent 读取后再选 direct/design/research | 不需要新 skill | 同 session 可把 Snapshot 直接放进派发消息 | 明天新 session 必须使用 durable carrier，例如 `docs/clarity/YYYY-MM-DD-billing-export.md` |
| “我完全不知道业余时间想做什么” | dig Discover → 比较方向；必要时 cheap prototype；也可以 stop | 不急着建 | 通常不需要 | 明确下次继续时才保存 Direction Map |

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
