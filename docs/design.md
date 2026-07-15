# Sensemaking 产品设计

## North Star

把 uncertainty 转化为明确、可检验、可延续的 shared understanding，同时不把清晰工作拖入流程仪式。

Sensemaking 解决的是 thinking state，不是某一种输入：产品需求、个人想法、重构、部署、资料整理、制度设计或现有文档都只是 starting point。

## 核心模型

不确定性分为三个需要对话协作的类型：

| 类型 | 关键问题 | Mode |
|---|---|---|
| Direction uncertainty | 有哪些值得考虑的方向，依据是什么？ | Discover |
| Decision uncertainty | 哪些现实选择必须由人承担，且会改变结果？ | Clarify |
| Validity uncertainty | 当前 proposal/decision 是否存在实质缺陷？ | Challenge |

另有两种情况不应被吞进来：

- **Fact uncertainty**：缺事实、根因、现状或可行性证据，先 inspect/research/diagnose/prototype。
- **Action-ready**：consequential decisions 已清楚且没有可见 material defect，直接交付。

### Route invariant

route 不由 source、format、domain、lifecycle phase 或 task size 决定。任意 starting point 都使用同一个 gate；具体场景只用于校准这个抽象，不产生专属规则。

## Mode contract

### Discover

Discover 服务于“尚无足够 basis to choose”。它从真实 starting point 出发，识别缺失的是方向、词汇、例子还是判断标准；必要时先 teaching/research，再用 multiple frames 与 recognition-based examples 扩大可见空间。

完成条件是形成 chosen direction、shortlist、待验证 hypothesis，或明确决定暂不继续。不得用首个 hypothesis 锚定用户，也不自动翻译成 PRD。

### Clarify

Clarify 服务于“已有 outcome，但仍有 consequential human-owned choices”。先查证可获得的事实，再提出足够具体、可被否定的 working hypothesis；只追踪答案不同会改变 outcome、scope、validation、risk 或 external commitment 的 material forks。

完成条件是每个 material fork 已 `confirmed`、以可见默认 `assumed`、明确 `deferred`，或转为 evidence/prototype action。agent-owned、局部且可逆的实现选择不升级为用户决策。

### Challenge

Challenge 服务于明确 critique 请求或已经可见的 material defect。它使用少量相关 lens 检验 goal fit、consistency、evidence、boundaries、failure/recovery、stakeholders、testability、reversibility 与 alternatives。

finding 必须说明 defect、basis、consequence 与最小 correction；只有 owner trade-off 未决时才提问。完成条件是 material findings 已修正、驳回、转为决定、暂缓或接受为 risk。

## STRUCTURE

STRUCTURE 保存 shared understanding，而不控制认知过程。它按需记录：

- Intent、Stakeholders、Scenarios
- Scope、Requirements、Constraints
- Decisions、Assumptions & evidence
- Risks & edge cases、Success evidence、Open items

每个 consequential item 使用 `candidate`、`confirmed`、`assumed`、`invalidated`、`deferred` 或 `risk` 状态。修订时 invalidate 旧决定，避免 polished summary 让旧假设重新变成 active requirement。

STRUCTURE-only 只用于保存、对齐或交接已经形成的 shared-decision state，不承担普通改写、摘要、文件整理或数据转换。

## Interaction principles

1. **Evidence before owner question**：能安全查到的事实由 agent 获取。
2. **Teach/show before asking**：用户没有判断基础时先补足 basis。
3. **Consequence over checklist**：只有会改变结果的问题、证据或 finding 才进入对话。
4. **Dependency-aware pacing**：依赖问题逐层追，独立问题可批量展示。
5. **Attackable reasoning**：frame、hypothesis 与 finding 必须具体到可以被反驳。
6. **Honest fog**：暂时无法精确定义的内容保持 open，不制造虚假确定性。
7. **Delta reflection**：后续轮次只说明 shared model 的变化。

## 输出与 persistence

输出是 renderer，不是固定终点。按需要选择 Direction Map、Clarity Memo、Challenge Report、Decision Brief、Requirements Brief、Handoff Snapshot 或不生成 artifact。

默认只维护 conversation state。另一个 agent、后续 session、审批、审计或长期协作会丢失关键信息时，才使用项目既有 carrier 持久化。恢复时保留已接受决定，同时重新验证会漂移的事实与实现状态。

## 下游边界

Sensemaking 完成 thinking job 即归还控制权。剩余工作可以是 evidence gathering、prototype、direct delivery、design、coordination planning、domain review 或 stop；它们没有固定顺序，也不是任何 mode 的自动后继。

独立 reviewer 是 risk-based escalation。Software Architect 只适用于真实 software architecture；非代码任务、文件数量和任务规模都不是调用理由。详细选择规则见 [routing.md](routing.md)。

## 被否决方案

| 方案 | 否决原因 |
|---|---|
| 单一巨型流程 | Discover 需要扩展空间，Clarify 需要收敛，Challenge 需要直接判断，默认动作无法统一 |
| 三个公开 skill | 用户往往不知道当前 uncertainty type；一个入口更利于正确路由 |
| task-size workflow | 规模不能同时决定是否澄清、设计、评审与计划 |
| 固定输出 schema | renderer 反向控制 thinking 会制造 checklist theater |
| 默认独立 reviewer | 跨领域误路由、成本高，且独立视角并非总有增益 |
| 默认自动落盘 | 短会话产生噪音，carrier 与 continuity need 被混为一谈 |

## 验收不变量

1. 缺方向时展示多个可比较 frames，不用单一 hypothesis 锚定。
2. 缺知识时先提供 decision-relevant evidence/examples。
3. solution-disguised-as-requirement 会被追溯到真实问题。
4. critique 先给 evidence-backed findings，不把已知缺陷伪装成问题。
5. 修订过的决定不会在 summary 中复活。
6. 清晰请求不因规模或领域被误触发。
7. 只缺事实或根因时先调查。
8. 任一 mode 完成后不自动进入 design、plan、implementation 或 reviewer。
9. STRUCTURE-only 不吞掉普通内容转换和文件操作。
10. route invariant 在跨领域成对案例中保持成立。
