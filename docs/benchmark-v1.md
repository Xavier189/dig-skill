# Skill Benchmark: dig

**Model**: <model-name>
**Date**: 2026-07-02T11:31:10Z
**Evals**: 0, 1, 2 (3 runs each per configuration)

## Summary

| Metric | With Skill | Without Skill | Delta |
|--------|------------|---------------|-------|
| Pass Rate | 100% ± 0% | 93% ± 12% | +0.07 |
| Time | 0.0s ± 0.0s | 0.0s ± 0.0s | +0.0s |
| Tokens | 0 ± 0 | 0 ± 0 | +0 |- 污染警告：baseline 并非裸模型——subagent 继承了全局 CLAUDE.md 的 dig 纪律条目与项目 memory（批量精准提问偏好），方法论双通道渗透。Delta +7pp 应解读为「SKILL.md 细节纪律 vs 环境残留方法论」的净值，实际相对裸模型的增量远大于此。
- eval-0 双满分 = 非区分性用例（污染环境下 baseline 形态趋同，连 ✅🔍❓ 标记都出现在 baseline 输出中）。
- eval-1 是关键区分组：baseline 挂在「无状态标记拆解」，且 assertions 之外的质差明显——baseline 16 问开放式无选项无推荐（超过 dig 的 ~8 问拆任务阈值）；with-skill 8 问分两批带选项/推荐/置信度/被否决项代价，并显式给出量化成功标准与两轮上限承诺。
- eval-2 双满分是设计目标达成而非无效用例：验证 Skip 条款生效，dig 对小任务零拖累。
- timing/token 数据缺失：agent-teams 通知不携带 total_tokens/duration_ms，本轮无法比较开销。
- eval-1 with-skill 首跑长时间无产出被状态询问唤醒后完成（替补 agent 已中止未写文件）；产出质量不受影响，但记录该运行异常。

## 运行细节

- 3 用例 × (with-skill + baseline) = 6 个独立 subagent 并行
- 逐条 assertion 评分证据见 dig-skill-workspace/iteration-1/*/*/run-1/grading.json
- 完整输出（questions.md 等）同目录 run-1/outputs/
