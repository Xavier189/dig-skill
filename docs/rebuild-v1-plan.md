# Dig Rebuild v1 落地计划

状态：已完成，待用户决定是否合并
分支：`rewrite/adaptive-dig-v1`
基线：`aca1ed53700da3ee9cb505724966540406d45d08`（main / dig v2.4）

## 目标

把 dig 从“动手前的需求澄清流程”重建为跨领域、可重入的 adaptive thought partner：

- 用户不知道想要什么时，帮助发现方向；
- 用户有粗略目标但存在真实分叉时，帮助澄清决策；
- 用户已有需求或设计时，检验缺陷、盲区、矛盾和未决点；
- 全程维护结构化 shared understanding，但不绑定 design、plan、implementation 或 reviewer。

## 已确认的产品边界

1. 保留一个公开入口 `dig`，不要求用户先判断自己需要哪种能力。
2. 内部按 `Discover / Clarify / Challenge` 三种 mode 路由，可切换但不强制全走。
3. `STRUCTURE` 是横切层，不是第四种 mode；短会话只在上下文中维护，长会话或显式要求时才渲染或落盘。
4. 对话或 critique 本身是交付物时直接完成，不设置“先确认 clarity memo 才能 review”的循环门槛。
5. 明确请求只有在用户显式要求 dig/challenge，或已发现实质缺陷时才进入；复杂度和任务大小不是触发条件。
6. 默认 inline、domain-aware challenge；任何 subagent reviewer 都是按领域和风险选择的 escalation，不是终态。
7. 事实由 agent 调研，价值取舍与不可逆决策交给用户。
8. 结构化输出区分 `candidate / confirmed / assumed / invalidated / deferred / risk`，防止把推测伪装成需求。

## 文件改造

- `skills/dig/SKILL.md`：缩成路由、共同原则、横切状态和退出边界。
- `skills/dig/references/discover.md`：blind-spot pass、多个 frame、teach/show-before-ask、prototype/reference、发散与收敛。
- `skills/dig/references/clarify.md`：继承并收紧 v2.4 的 hypothesis、问题门槛、batch/依赖 loop、solution-disguised-as-requirement。
- `skills/dig/references/challenge.md`：直接给 finding、反例、pre-mortem、边界/失败场景、替代方案和 accepted risk。
- `skills/dig/references/structure.md`：共享需求模型、状态语义、decision ledger 与按需 renderer。
- `README.md`：以新 North Star、三 mode、STRUCTURE 和使用边界重写。
- `docs/design.md`：记录新架构、关键权衡和外部调研结论；旧版设计移入 `docs/history/`。
- `docs/roadmap.md`：切换为 rebuild v1 的验证与未来合并路线；旧版 roadmap 归档。
- `evals/evals.json`：重建 behavior 与 trigger 边界用例。

## 验证矩阵

| 场景 | 必须看到 | 必须避免 |
|---|---|---|
| 用户完全不知道方向 | 多个 plausible frames、blind spots、必要的解释/示例 | 单一“真实目标”锚定、直接 plan |
| 方案伪装成需求 | 追溯真实问题、核查事实、澄清决策 | 只问方案参数 |
| 明确要求审查非代码设计 | 直接给 evidence-backed findings 与修订建议 | 只提问、Software Architect |
| 对话中决定被修改 | confirmed/invalidated/assumed 等状态清楚 | 新旧决定并存、猜测冒充确认 |
| 清晰的一步请求 | 直接执行 | 因“可能还有盲区”而自动进入 dig |
| 显式 dig 但请求已清楚 | 零问题也可形成轻量 shared-understanding snapshot | 制造问题或强制下游流程 |

## 执行与验收

1. 保存旧版 skill snapshot，作为 existing-skill baseline。
2. 完成 skill、references 和文档重写。
3. 对 JSON、Markdown 链接、frontmatter 和目录结构做静态检查。
4. 选取覆盖三 mode、STRUCTURE 与 skip 边界的代表用例，分别运行 rebuild v1 与 v2.4 baseline。
5. 按 assertion 评分，生成 benchmark 与 `review.html`。
6. 分析误触发、锚定、提问代替 critique、状态丢失和 reviewer 污染；必要时迭代一次。
7. 最终确认所有修改只存在于 `rewrite/adaptive-dig-v1`，main 未被改写。

## 验收结果

- rebuild v1：9/9 eval、34/34 assertions 通过；
- v2.4 baseline：27/34 assertions 通过；
- 新版相对旧版的 mean per-eval pass rate：100.00% vs 80.56%；
- 两套 `quick_validate.py` 均通过；
- JSON、Markdown 本地链接、frontmatter、目录结构与 `git diff --check` 均通过；
- 静态结果见 [benchmark](../evals/rebuild-v1/benchmark.md) 与 [review viewer](../evals/rebuild-v1/review.html)；
- `main` 仍停留在基线 commit，合并说明见 [merge notes](merge-notes.md)。

## Downstream 收口

rebuild 完成后的追加审计确认原 `big-task` 固定编排无保留必要：

- installed `big-task` 与 Claude symlink 已删除；
- Codex / Claude 全局 instructions 已改为 risk-based downstream routing；
- dig 明确为无业务 skill 前置、无强制后继；
- Handoff Snapshot 只传递 ready state、边界、假设、暂缓项、风险与 success evidence；
- targeted handoff eval 最终 4/4、14/14 assertions 通过，详见 [benchmark](../evals/handoff-v1/benchmark.md)。
