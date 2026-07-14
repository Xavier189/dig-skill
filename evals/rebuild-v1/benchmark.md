# Skill Benchmark: dig rebuild v1

**Model**: Codex (GPT-5)
**Date**: 2026-07-14
**Evals**: 0–8，共 9 组，每个 configuration 1 次隔离运行

## Summary

| Metric | With skill | Old skill | Delta |
|---|---:|---:|---:|
| Mean per-eval pass rate | 100.00% | 80.56% | +19.44 pp |
| Assertion total | 34/34 | 27/34 | +20.59 pp |
| Time | unavailable | unavailable | — |
| Tokens | unavailable | unavailable | — |

## Observations

- 新版 9/9 组全部通过，旧版主要失分于 Discover 过早让用户选择、Challenge 不做 finding-first，以及面对明确但有重大缺陷的要求时直接照做。
- eval 1、2、4、5、8 新旧版本都全通过，说明旧版在普通 Clarify、状态语义和清晰请求跳过上已有强基线。
- eval 4 没有量化出新版 exact state label 与修订轨迹的全部优势；现有 assertions 只检查语义正确性。
- 当前每个 configuration 只有一次运行，适合做 deterministic boundary regression，不用于估计随机方差。
- 隔离 subagent 没有返回 timing/token 指标；JSON 中的 `0` 表示 unavailable。
