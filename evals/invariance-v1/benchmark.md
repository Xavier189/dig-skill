# Invariance v1 Benchmark

日期：2026-07-14

## 目的

验证 dig 的 route 只取决于 thinking state，不取决于 source、carrier、domain、lifecycle phase 或 task size；同时验证 STRUCTURE-only 不接管普通文件整理与数据转换。

## 方法

- 用例：`evals/evals.json` ID 13–21。
- 每个用例使用独立 `codex exec --ephemeral --sandbox read-only` fresh session。
- 被测 session 只收到 raw prompt，不收到 case name、assertions、预期 route 或本轮缺陷说明。
- model：`gpt-5.6-sol`；Codex CLI：`0.144.3`；每个用例 1 次运行。
- 评分严格依据可见 final response，不把未写出的意图算作 evidence。

## 结果

| ID | 场景 | Route | Assertions |
|---:|---|---:|---:|
| 13 | 自发 refactor 的 material choice | PASS | 4/4 |
| 14 | 非代码审批流程的 material choice | PASS | 3/4 |
| 15 | 清晰局部 refactor | PASS | 4/4 |
| 16 | 清晰个人博客部署 | PASS | 4/4 |
| 17 | 纯根因不确定的性能回归 | PASS | 4/4 |
| 18 | 无方向的个人 mini app | PASS | 4/4 |
| 19 | 无整理目标与判断依据的资料目录 | PASS | 4/4 |
| 20 | 规则明确的资料目录 dry-run | PASS | 4/4 |
| 21 | 规则明确的 CSV join | PASS | 3/3 |
| **合计** |  | **9/9** | **34/35（97.14%）** |

route-level invariance 全部通过：同为 Clarify 的 code/non-code pair、同为 action-ready 的 refactor/blog pair、同为 Discover 的 mini app/folder pair，以及同一 folder domain 的 Discover/direct 对照均符合 state gate。CSV 用例直接输出转换结果，没有进入 STRUCTURE-only。

唯一失败来自 ID 14：response 正确进入 Clarify 并识别风险分级的 owner decision，但未先请求当前等待节点、失败率或现有流程等 evidence source，过早提出 target frame。该失败不属于 router 错误，属于 Clarify evidence discipline。

评分后已在 `references/clarify.md` 增加 `Evidence gate before a working hypothesis`：current-state evidence 可能改变诊断或 option set 时必须先 inspect；不可访问时先请求最小 source pointer，不能把 symptom 直接当 cause 或 target design。尝试对 ID 14 做最终 fresh-session rerun 时，本机 Codex 额度耗尽，命令被拒绝；因此本报告不声称该最后修正已经行为复验。

## 评分口径调整记录

初次 assertions 对 ID 15、16、20 同时要求“只给下一步最小动作”和“复述完整后续动作/全部边界”，严格评分会把输出粒度冲突误记成 route failure。调整后，skip cases 只验证：直接进入最小执行/evidence 动作、不重开既定决定、不进入 dig/STRUCTURE ceremony、不强制 reviewer 或 plan。Clarify 的 evidence assertions 没有放宽。

逐项 final response 见 [responses.md](responses.md)，机器可读汇总见 [benchmark.json](benchmark.json)。
