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

## Phase 3：收敛与合并准备

- [x] 根据 eval 输出修正一次（无 material behavior regression；validator 发现并修正 description 长度）
- [x] 检查 frontmatter、Markdown links、JSON 与目录结构
- [x] 确认 main 未被修改、所有新工作只在 rewrite branch
- [x] 形成 merge/migration notes
- [ ] 用户审核后再决定是否覆盖 main

## 后续观察项

这些不阻塞 rebuild v1：

1. Discover 是否因过度发散而迟迟不收敛。
2. “material defect” 自动 Challenge gate 是否误触发普通清晰请求。
3. stance 自动切换是否需要显式用户控制。
4. decision ledger 的启用门槛是否过早或过晚。
5. renderer 是否需要独立 skill/harness adapter。
6. description 是否需要 20-query trigger optimization；先积累真实误判再做，避免合成样本过拟合。

旧版路线保存在 [history/v2.4-roadmap.md](history/v2.4-roadmap.md)。
