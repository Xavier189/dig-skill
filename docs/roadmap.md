# Rebuild v1 Roadmap

当前开发分支：`rewrite/adaptive-dig-v1`

## Phase 1：产品模型与 skill 重写

- [x] 确认 North Star：adaptive thought partner，而非单一 requirements elicitation
- [x] 明确 Discover / Clarify / Challenge
- [x] 明确 STRUCTURE 横切层与 renderer 边界
- [x] reviewer 与 downstream workflow 解耦
- [x] 保存 v2.4 baseline snapshot
- [x] 重写 `SKILL.md`
- [x] 拆分四个 reference playbook
- [x] 重写 README 与 design

## Phase 2：Behavior eval

- [x] 重建 `evals/evals.json`
- [x] Discover：无方向时多 frame、无单一锚定
- [x] Discover：缺少知识时 teach/show-before-ask
- [x] Clarify：solution-disguised-as-requirement 回归
- [x] Challenge：非代码设计 finding-first
- [x] STRUCTURE：修订决定正确 invalidated
- [x] Skip：清晰请求直接执行
- [x] Boundary：无 Software Architect、无自动 plan/implementation
- [x] candidate 与 v2.4 baseline 对照
- [x] 生成 benchmark 与 static review viewer
- [x] input-agnostic metamorphic eval：route 9/9，assertions 34/35
- [ ] Clarify final evidence-gate rerun：已修正文案，2026-07-14 因 Codex 额度耗尽未能复验

## Phase 3：收敛与合并准备

- [x] 根据 eval 输出修正一次（无 material behavior regression；validator 发现并修正 description 长度）
- [x] 检查 frontmatter、Markdown links、JSON 与目录结构
- [x] 确认 main 未被修改、所有新工作只在 rewrite branch
- [x] 形成 merge/migration notes
- [ ] 用户审核后再决定是否覆盖 main

## Phase 4：Downstream 解耦

- [x] 审计并退役 `big-task` 固定编排
- [x] 明确 dig 无业务 skill 前置、无强制后继
- [x] 增加 Handoff Snapshot renderer
- [x] 将全局 task-size 分级改为 risk-based downstream routing
- [x] 保留 alternatives、reversibility、failure/recovery、YAGNI 与 domain-aware review
- [x] targeted handoff eval：4/4、14/14 assertions
- [x] 生成 [handoff benchmark](../evals/handoff-v1/benchmark.md) 与 [static viewer](../evals/handoff-v1/review.html)

## 后续观察项

这些不阻塞 rebuild v1：

1. Discover 是否因过度发散而迟迟不收敛。
2. “material defect” 自动 Challenge gate 是否误触发普通清晰请求。
3. stance 自动切换是否需要显式用户控制。
4. decision ledger 的启用门槛是否过早或过晚。
5. renderer 是否需要独立 skill/harness adapter。
6. description 是否需要 20-query trigger optimization；先积累真实误判再做，避免合成样本过拟合。
7. 哪些真实业务/专业任务稳定重复，足以提取窄 skill；不预先建立通用 post-dig skill tree。
8. 跨 agent 的 inline Snapshot 是否足够，还是反复出现状态丢失，值得增加 dispatch adapter。
9. 跨 session 使用是否足够频繁且摩擦稳定，值得增加 persistence/resume adapter；在此之前不让 dig 默认自动落盘。
10. 跨 source、carrier、domain、lifecycle phase 与 task size 的真实样本中，same thinking state 是否保持 same gate；重点观察局部反馈是否再次被错误提升为核心 trigger。
11. STRUCTURE-only 是否误吞普通改写、文件整理、数据转换或摘要任务。
12. Clarify 的 evidence gate 是否稳定阻止“没有现状证据就先处方化”；额度恢复后优先重跑 invariance ID 14。

旧版路线保存在 [history/v2.4-roadmap.md](history/v2.4-roadmap.md)。
