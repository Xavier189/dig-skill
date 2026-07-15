# Invariance v1 Benchmark

首次运行：2026-07-14

ID 14 final rerun：2026-07-15

## 目的

验证 dig 的 route 只取决于 thinking state，不取决于 source、carrier、domain、lifecycle phase 或 task size；同时验证 STRUCTURE-only 不接管普通文件整理与数据转换。

## 方法

- 用例：`evals/evals.json` ID 13–21。
- 每个用例使用独立 `codex exec --ephemeral --sandbox read-only` fresh session。
- 被测 session 只收到 raw task prompt；需要显式定位隔离 skill 时仅附 skill path，不收到 case name、assertions、预期 route 或本轮缺陷说明。
- model：`gpt-5.6-sol`；Codex CLI：`0.144.3`；最终记分每个用例取 1 次运行。
- 评分严格依据可见 final response，不把未写出的意图算作 evidence。
- ID 14 final rerun 使用独立 `/tmp` fixture，仅包含 `skills/dig/`，并启用 `--ephemeral --ignore-user-config --ignore-rules --sandbox read-only`。
- 表中每个 case 只统计最终采用的一次 fresh run；ID 14 修正前的失败运行保留为迭代证据，不计入最终分数。

## 结果

| ID | 场景 | Route | Assertions |
|---:|---|---:|---:|
| 13 | 自发 refactor 的 material choice | PASS | 4/4 |
| 14 | 非代码审批流程的 material choice | PASS | 4/4 |
| 15 | 清晰局部 refactor | PASS | 4/4 |
| 16 | 清晰个人博客部署 | PASS | 4/4 |
| 17 | 纯根因不确定的性能回归 | PASS | 4/4 |
| 18 | 无方向的个人 mini app | PASS | 4/4 |
| 19 | 无整理目标与判断依据的资料目录 | PASS | 4/4 |
| 20 | 规则明确的资料目录 dry-run | PASS | 4/4 |
| 21 | 规则明确的 CSV join | PASS | 3/3 |
| **合计** |  | **9/9** | **35/35（100%）** |

route-level invariance 全部通过：同为 Clarify 的 code/non-code pair、同为 action-ready 的 refactor/blog pair、同为 Discover 的 mini app/folder pair，以及同一 folder domain 的 Discover/direct 对照均符合 state gate。CSV 用例直接输出转换结果，没有进入 STRUCTURE-only。

ID 14 初次 response 正确进入 Clarify，但未先请求当前等待节点、失败率或现有流程等 evidence source，过早提出 target frame。随后在 `references/clarify.md` 增加 `Evidence gate before a working hypothesis`：current-state evidence 可能改变诊断或 option set 时必须先 inspect；不可访问时先请求最小 source pointer，不能把 symptom 直接当 cause 或 target design。

final rerun 中，response 将方案标记为 `candidate`，主动请求当前审批流程或 checklist 的最小来源指针，并明确“没有现状证据前，不判断两三天卡在检查、排队还是责任不清”。ID 14 的 4 项 assertions 全部通过。

| ID 14 assertion | 结果 | 可见 evidence |
|---|---|---|
| 识别速度、控制、责任与风险承担的真实分叉 | PASS | 区分等待时间、自动/人工边界、风险接受者与流程 Owner |
| 区分可调查事实与 owner decision | PASS | 请求流程/checklist source pointer；明确未获证据前不判断 bottleneck |
| 使用 Clarify 而非跳过 shared-understanding work | PASS | 所有方案均标为 `candidate`，提出会改变后续方案的父决策 |
| 不进入 software/big-task pipeline | PASS | 未推荐 Software Architect、代码实现或固定下游流程 |

## 评分口径调整记录

初次 assertions 对 ID 15、16、20 同时要求“只给下一步最小动作”和“复述完整后续动作/全部边界”，严格评分会把输出粒度冲突误记成 route failure。调整后，skip cases 只验证：直接进入最小执行/evidence 动作、不重开既定决定、不进入 dig/STRUCTURE ceremony、不强制 reviewer 或 plan。Clarify 的 evidence assertions 没有放宽。

逐项 final response 见 [responses.md](responses.md)，机器可读汇总见 [benchmark.json](benchmark.json)。
