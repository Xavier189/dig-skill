# Skill Benchmark: dig handoff

**Baseline**: commit `6c482c6`
**Model**: Codex (GPT-5)
**Date**: 2026-07-14
**Evals**: 9–12，共 4 组，每个最终 configuration 1 次隔离运行

## Summary

| Metric | With skill | Old skill | Delta |
|---|---:|---:|---:|
| Mean per-eval pass rate | 100.00% | 87.50% | +12.50 pp |
| Assertion total | 14/14 | 12/14 | +14.29 pp |
| Time | unavailable | unavailable | — |
| Tokens | unavailable | unavailable | — |

## Observations

- 新版能在高风险 encryption 场景选择 Security/Cryptography design review，而旧版只抽象地“交还所属领域”。
- no-prerequisite、state-preserving handoff 与 clear reversible direct-delivery 新旧版本均通过，说明新增 handoff contract 没破坏原边界。
- eval 11 的首次 candidate 输出漏掉 targeted verification；SKILL 补充 `direct delivery with proportionate verification` 后 rerun 通过，pre-fix 输出保留在 viewer。
- 当前每个最终 configuration 只有一次运行，适合做 boundary regression，不用于估计随机方差。
