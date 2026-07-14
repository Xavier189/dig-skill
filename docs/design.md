# Dig Rebuild v1 设计说明

日期：2026-07-14
状态：implemented on `rewrite/adaptive-dig-v1`

## 1. North Star

Dig 是一个跨领域、可重入的 adaptive thought partner。它没有前置流程，可以是 session 或 agent 工作的第一步。它根据用户当前的不确定性，在 Discover、Clarify、Challenge 三种认知动作之间选择和切换，把模糊、未知或未经检验的想法转化成 shared understanding。

它不拥有下游 design、plan、implementation 或 reviewer。

## 2. 为什么推倒重来

v2.4 把需求清晰度与任务大小解耦，并解决了非代码任务被送往 Software Architect 的 downstream 污染。这一修正继续成立。

但 v2.4 仍把产品定义为“动手前的 requirements excavation”，核心流程固定为：单一 hypothesis → questions → clarity memo。它默认：

1. 用户已经拥有一个可以被追问出来的目标；
2. 用户知道各选项意味着什么；
3. 缺陷最终应转化成澄清问题；
4. 所有 dig 都是另一项工作的前置阶段；
5. 固定五节 memo 足以保存对话结果。

这些前提只适用于“目标存在但有决策分叉”的 Clarify 场景。

用户原始需求更宽：不知道想做什么时需要共同发现；已有 requirement/design 时需要检验缺陷。更深的问题不是“提问还不够好”，而是三种不确定性被压进了同一种提问流程。

## 3. 三类不确定性

| 类型 | 用户状态 | 所需认知动作 | 典型失败 |
|---|---|---|---|
| Direction uncertainty | 不知道目标、缺少语言或判断标准 | 发散、教育、reference/prototype、形成 frames | 过早收敛到 agent 的第一猜测 |
| Decision uncertainty | 目标存在，但多个现实答案导向不同结果 | hypothesis、事实核查、提问、比较、拍板 | 参数题很多，真实分叉没上浮 |
| Validity uncertainty | 设计明确，但可能错误、不完整或不自洽 | evidence、counterexample、failure analysis、alternatives | 把已知缺陷伪装成问题，或直接顺着错方案执行 |

这三类分别映射到 Discover、Clarify、Challenge。它们可以串联，但不是固定阶段。

## 4. 架构

```text
ORIENT
  读取会改变 framing / question / critique 的证据
      ↓
ROUTE
  Discover / Clarify / Challenge
      ↓                         ↘ 必要时切换 mode
WORK  ←─────────────────────────┘
      ↕
STRUCTURE
  维护有状态的 shared model
      ↓
CONVERGE
  使用 mode-specific completion
      ↓
RENDER（可选）
  Direction Map / Clarity Memo / Challenge Report / Brief / Spec
```

`SKILL.md` 只放路由、共同原则、STRUCTURE 摘要与边界；各 mode 通过 `references/` progressive disclosure 加载，避免一个巨型 prompt 同时操纵三套行为。

## 5. Mode 设计

### 5.1 Discover

目标：让 requirement 成为可能，而不是假设 requirement 已存在。

关键机制：

- 从真实 starting point 开始，不先声明唯一“真实目标”；
- 根据场景采用 Facilitator、Creative Partner 或 Advisor stance，但不强制用户先选模式；
- blind-spot pass 区分缺方向、缺语言、缺实例、缺判断依据；
- teach/show-before-ask，避免用户对陌生选项盲选；
- 生成多个后果不同的 plausible frames；
- 使用 examples、counterexamples、references 和 cheap prototype；
- divergence 与 convergence 分离，允许“继续探索”成为合法终点。

### 5.2 Clarify

目标：解决会改变结果的 material decisions。

保留 v2.4 的有效机制：

- facts lookup / decisions ask；
- solution-disguised-as-requirement；
- attackable hypothesis 与 named traps；
- 独立问题 batch、依赖问题逐层；
- question admission gate；
- show-don't-ask；
- delta-only reflection；
- convergence by remaining forks，而不是轮数配额。

调整：旧版 `✅ / 🔍 / ❓` 由跨 mode 的状态语义替换，避免 UI 标记与数据状态混为一体。

### 5.3 Challenge

目标：判断 requirement/design 是否成立，而不只是是否清楚。

关键机制：

- finding-first：已知缺陷直接说，不伪装成用户问题；
- evidence + consequence + minimum correction；
- owner decision 只用于价值冲突、风险承受和不可逆承诺；
- lens 按上下文选择，不机械跑 checklist；
- named methods 是工具，不是固定菜单；
- 保留设计中成立的 strengths，使修订保持约束；
- 非软件任务使用同一逻辑，不接 software reviewer。

## 6. STRUCTURE

STRUCTURE 不是第四个 mode，而是共享状态层。

### 6.1 状态

- `candidate`
- `confirmed`
- `assumed`
- `invalidated`
- `deferred`
- `risk`

状态解决两个根本问题：agent 假设被写成用户需求；后续总结把已推翻决定重新复活。

### 6.2 信息模型

按需记录 Intent、Stakeholders、Scenarios、Scope、Requirements、Constraints、Decisions、Assumptions & evidence、Risks & edge cases、Success evidence、Open items。

这些是可选维度，不是要填满的模板。v1 已证明机械 checklist 会产生“看似完整、没有洞察”的 theater。

### 6.3 Traceability

短会话只在上下文维护。出现多轮、决定修订、精确数值/顺序/negative requirement、跨 session handoff 时启用 decision ledger。

ledger 可保留原始 basis、normalized decision、replaces 和 downstream consequence。只有需要 coverage check 时才分配 stable IDs。

## 7. 触发边界

### 自动触发

- 用户明确缺少方向或判断依据；
- 存在会改变 outcome 的 material ambiguity；
- requirement/design 已出现 concrete material defect，静默执行不成立。

### 显式触发

用户要求 dig、brainstorm、explore、clarify、grill、challenge、stress-test 或审查 requirement/design 时进入相应 mode。

### 跳过

- 清晰执行请求；
- 纯信息问答；
- 明确的一步改写/翻译/格式化；
- 普通 code review、debugging、implementation review，除非目标是底层 requirement/design validity。

关键边界：`decision-complete != decision-sound`，但 material defect gate 不能退化为 every-task review。

## 8. 输出与 persistence

输出是 renderer，不是流程终点：

- Discover → Direction Map
- Clarify → Clarity Memo / Requirements Brief
- Challenge → Challenge Report / revised brief
- 用户明确要求 → PRD / Spec / ADR / user stories

默认不落盘。legacy 五节 clarity memo 保留为 adapter，而非 core contract。

## 9. Handoff 与下游路由

Dig 交付的是可消费的 shared state，不是下一条固定 workflow。需要跨 agent/session 继续时，handoff 只携带：已接受状态、必须保留的边界、`assumed / deferred / risk` 项和 success evidence。

下游还需要区分三个正交机制：

1. `skill` 提供可重复使用的专业能力、workflow、知识与资源；
2. `agent/subagent` 决定本次执行由谁完成、是否并行、是否需要独立视角；
3. conversation message、file、issue 或 task state 决定 shared state 如何跨边界延续。

因此 v1 不预建通用 post-dig skill tree、不建立固定 subagent graph，也不让 dig 默认自动落盘。窄 skill 只从反复出现且边界稳定的真实业务/专业模式中提取；subagent 按本次依赖与风险临时选择；durable artifact 只在跨 session、恢复、审批、审计或明确共享需要时产生。

下游按五个信号独立判断：

1. 缺的是事实、可行性证据还是 owner decision；
2. 用户真正要的 deliverable；
3. 改动的可逆性、耦合与 blast radius；
4. 安全、合规、数据、金钱或公共承诺风险；
5. 是否需要跨步骤、跨人或跨 session 协调。

由此选择 research/prototype、direct delivery、design、planning、domain review 或 stop。它们不是顺序阶段，也不由 task size 单独触发。完整规则见 [downstream.md](downstream.md)。

原 `big-task` skill 被退役，因为它把本应正交的 dig、design、review 与 plan 重新绑成固定链。其 alternatives、failure/recovery、reversibility、YAGNI 等有效原则转入 risk-based design route，不再作为强制 ceremony。

## 10. Reviewer 决策

默认 inline、domain-aware challenge。

Superpowers 曾将 spec/plan 交给 subagent reviewer，后续公开 release notes 记录其回归结果：约增加 25 分钟、没有可测质量提升，因此改为 inline self-review。该结果不能证明所有 reviewer 无效，但足以否决 reviewer-as-ritual。

Dig 的 reviewer policy：

- 只有显式要求、高风险或独立视角确有增益时 escalation；
- reviewer 按 domain 选择；
- Software Architect 只可能服务实际软件架构问题；
- reviewer 不是任何 mode 的 terminal state。

## 11. 外部参照与取舍

| 参照 | 吸收 | 不吸收 |
|---|---|---|
| Matt Pocock grilling | facts/decisions、dependency-aware questions、shared understanding | relentless 与全程 one-question doctrine |
| Matt domain-modeling / wayfinder | precise terms、edge cases、fog-of-war、prototype | 普通会话默认 issue map |
| Superpowers brainstorming | context-first、alternatives、incremental validation、inline self-review | every-project hard gate、forced spec/writing-plans |
| BMAD | divergence 与 advanced elicitation 分离、stance、pre-mortem 等 lens | 100+ ideas、method menu、heavy memlog |
| GSD discuss | specific gray areas、context awareness、batch/assumption pacing | scope-fixed implementation orientation |
| GitHub Spec Kit | ambiguity/coverage/consistency lens、testability | software artifact pipeline 作为 core |
| Anthropic finding-your-unknowns | blind spots、prototype、references、unknowns 可在全周期出现 | 把所有能力限制为 pre-implementation checklist |

## 12. 被否决方案

### 单一巨型流程

否决原因：Discover 需要避免锚定，Clarify 需要收敛，Challenge 需要直接判断；同一默认动作无法同时满足三者。

### 三个公开 skill

否决原因：最需要帮助的用户通常不知道自己处于哪种不确定性。保留一个 `dig` 入口，由内部 router 选择。

### 固定输出 schema 控制流程

否决原因：harness compatibility 属 renderer/adapter；让 schema 控制认知流程会重新制造 checklist theater。

### 默认独立 reviewer

否决原因：跨领域错误、成本高、收益不稳定。改为 inline challenge + risk-based escalation。

### `big-task` 固定编排

否决原因：任务大小不能同时决定是否需要需求挖掘、设计、独立评审和计划；固定链会让清晰的大任务重复澄清、低风险改动产生文档 theater，并把 reviewer 与 plan 变成仪式。保留其中有效的设计 lens，删除编排器。

## 13. 验收标准

1. “我不知道想做什么”不会收到单一 implementation hypothesis。
2. 用户没有知识基础时，agent 先提供 decision-relevant education/examples。
3. Clarify 仍能识别 solution-disguised-as-requirement 和依赖问题。
4. 显式 critique 直接输出 evidence-backed findings，而不是只问问题。
5. 新旧决定在 structured state 中不会同时保持 active。
6. 清晰请求能跳过 dig。
7. 非代码任务不出现 Software Architect 或软件 pipeline。
8. 任一 mode 完成后不自动进入 plan/implementation/reviewer。
9. dig 可以作为 session 第一动作，且不会要求先经过其他 skill。
10. handoff 保存边界与风险，但不会把后继固化成 `big-task` 或任何单一 workflow。

旧版完整决策记录见 [history/v2.4-design.md](history/v2.4-design.md)。
