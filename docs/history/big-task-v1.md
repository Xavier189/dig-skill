# Retired big-task v1

状态：2026-07-14 退役，不再作为 installed skill。

原 skill 以任务大小为触发条件，固定编排：

1. dig 需求挖掘并确认 clarity memo；
2. 分段设计并逐段确认；
3. Software Architect 独立评审；
4. 默认写入 `docs/plans/` 并跟踪执行。

退役原因：四个阶段分别由需求不确定性、设计耦合与可逆性、风险/领域、协调复杂度决定，没有统一的“big task”触发条件。固定编排与新版 dig 的正交边界冲突，并制造 reviewer 与 plan theater。

保留内容：alternatives、trade-off、reversibility、failure/recovery、YAGNI 与 domain-aware review。它们已迁移到 [downstream contract](../downstream.md) 的 risk-based route。
