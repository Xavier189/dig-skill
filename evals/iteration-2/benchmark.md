# Skill Benchmark: dig

**Model**: gpt-5 Codex
**Date**: 2026-07-12T03:15:30Z
**Evals**: v2.4 = 0-5；v2.3 baseline = 0-2；每个已执行配置 1 run

## Summary

| Metric | With Skill | Without Skill | Delta |
|--------|------------|---------------|-------|
| Pass Rate | 100% ± 0% | 42% ± 52% | +0.58 |
| Time | 0.0s ± 0.0s | 0.0s ± 0.0s | +0.0s |
| Tokens | 0 ± 0 | 0 ± 0 | +0 |

> 这不是平衡 A/B：新版跑 6 个边界用例，v2.3 baseline 只跑其中 3 个。`+0.58` 仅描述本次已执行记录，不能外推成总体提升幅度。

## 分析备注

- eval-0 有区分力：v2.3 因“小任务”直接跳过；v2.4 因“更专业”存在真实 taste fork 而进入 dig，并展示 3 个具体方向。
- eval-1 有区分力：v2.3 对 decision-complete 的大型迁移请求仍强制 memo；v2.4 直接交付执行清单。
- eval-2 新旧双过。Software Architect 污染的根因是全局 `AGENTS.md` 未限定领域，不是 v2.3 `SKILL.md`；该全局规则已单独修复。
- eval-0 前两次运行暴露 escape hatch 与 show-don't-ask 冲突；v2.4 明确“停止提问不等于省略 taste sketches”后，最终回归通过。
- subagent 通知未提供 timing/token，相关指标保持 0，不用于效率结论。
