# 下游路由与能力边界

Sensemaking 只解决 shared understanding。完成后不要问“固定下一步是什么”，而要问“现在还缺什么”。

## 六个独立维度

| 维度 | 可选路线 |
|---|---|
| Thinking | Discover / Clarify / Challenge / STRUCTURE-only / skip |
| Evidence | inspect / research / diagnose / prototype / none |
| Solution shaping | direct / compact design / durable design |
| Execution topology | primary agent / subagent / human or tool reviewer |
| Coordination | inline task state / plan |
| Persistence | conversation / inline Snapshot / durable carrier |

它们可以组合，但互不自动触发。明确的博客部署可以 `skip + inspect + direct delivery + smoke test`；模糊的小重构可以 `inspect + Clarify + direct delivery`；高风险 encryption 需求可以 `skip + technical design + Security review + rollout plan`。

## 下游动作

| 当前缺口 | 最小动作 | 何时升级 |
|---|---|---|
| 事实、根因、兼容性或可行性未知 | inspect / research / diagnose / cheap prototype | evidence 暴露新的 owner decision 或 validity problem |
| 状态清楚、改动局部且可逆 | direct delivery + proportionate verification | 实现选择改变重要边界 |
| contract、data、coupling、failure/recovery、security 或 migration 会被改变 | compact design | 需要审批、长期追溯或多人 handoff 时写 durable design/ADR/spec |
| 多步骤存在依赖、并行、长时间恢复或复杂 rollout | plan | 默认维护 task state；只有 continuity need 才落盘 |
| 高风险或需要独立专业判断 | domain review | 按 Security、Privacy、Legal、DBA、SRE、Domain Expert 或 Software Architect 选择 |
| 当前 thinking 本身就是交付 | stop | 不制造 implementation handoff |

## Skill、subagent 与文件不是同一层

| 机制 | 解决什么 | 例子 |
|---|---|---|
| `AGENTS.md` / host instructions | scope 内几乎每次都必须遵守的短规则 | 构建命令、禁止修改生成文件 |
| 文档 / schema / authoritative source | 项目事实、术语、业务规则和当前 contract | 订单状态、退款期限、内部 API |
| 窄 skill | 可识别触发、按需加载的稳定方法与资源 | privacy impact review、对账 workflow |
| subagent / custom agent | 本次独立 workstream 或隔离的第二视角 | 分别盘点 payment 与 inventory 影响 |
| durable artifact | 让状态跨时间、session、审批或审计继续存在 | issue、ADR、Handoff Snapshot |

### 何时提取窄 skill

同时满足以下条件才值得提取：

1. trigger 可识别；
2. 存在通用模型不会稳定掌握的 reusable method、rule、schema、script、template 或 tool integration；
3. input、output 与完成边界可检验；
4. 应按需加载，而不是 scope 内始终生效；
5. 已反复重新发现、反复出错，或虽低频但高风险且脆弱。

项目事实通常先进入文档或权威系统；确定的机械操作优先做 script/tool。不要因为一次任务很大或刚完成 shared-understanding work 就创建 skill。

### Workspace 还是 global

选择能容纳全部假设的最窄 activation scope。满足以下四项时才适合 global：

1. 去掉仓库名、公司名和内部术语后仍完整成立；
2. 放进无关项目不会给出错误假设或危险命令；
3. 不含私有 schema、政策、环境地址、secret 或团队专属流程；
4. 更新节奏不依赖某个项目的代码和 release。

带项目/domain/资料集假设的能力留在 workspace。通用方法可以 global，并读取 workspace 的 facts/adapter，形成 hybrid。workspace 可以是代码库、博客、notes vault、资料目录或运维环境。

### 何时用 subagent

subagent 是 execution topology，不是下一阶段。只有以下条件成立时才派发：

1. contract 已稳定到不同 worker 不会各猜一套；
2. workstream 有明确输入、修改边界和独立验收证据；
3. 并行收益或独立视角的风险收益高于传递与整合成本；
4. primary agent 能验证并负责最终整合。

与用户共同处理 owner decision 默认留在 primary agent。需要重复的独立 role、tools、model 或 permission boundary 时才创建 custom agent；方法需要当前 agent 直接应用时使用 skill。

## Handoff 与落盘

默认不写文件。continuity need 决定 carrier：

| 延续方式 | Carrier |
|---|---|
| 同一 agent、同一 session | conversation context |
| 同 session、换 agent/subagent | dispatch message 中的 inline Handoff Snapshot |
| 新 session、隔天继续或长任务恢复 | 项目约定的 file / issue / task state |
| 审批、审计或多人长期共享 | spec / ADR / issue / decision record |

Snapshot 只保留下游需要的 ready state、confirmed decisions、boundaries、success evidence，以及仍为 `assumed`、`deferred`、`risk` 的项目。它描述“现在可以做什么”，不命令消费者进入固定 workflow。
