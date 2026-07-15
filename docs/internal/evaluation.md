# 行为校准

[`evals/evals.json`](../../evals/evals.json) 是当前唯一保留的 eval manifest。逐次模型输出、评分页面和阶段 benchmark 不属于产品事实，也不应占据文档导航；运行结果应进入 CI artifact、release evidence 或外部实验记录，而不是长期堆在仓库。

## 覆盖面

- Discover：无方向、缺判断基础、避免单一 hypothesis 锚定；
- Clarify：solution-disguised-as-requirement、evidence gate、owner decisions；
- Challenge：非代码方案、material defect、finding-first；
- STRUCTURE-only：修订状态、handoff 与普通转换的边界；
- Skip：清晰一步任务、局部 refactor、decision-complete 大任务；
- Fact uncertainty：性能根因与外部事实先调查；
- Invariance：相同 thinking state 跨代码/非代码、个人/工作、greenfield/maintenance 保持同一路由；
- Handoff：不自动选择 design、plan、reviewer 或 implementation。

## 静态校验

```bash
python3 -m json.tool evals/evals.json >/dev/null
python3 /path/to/skill-creator/scripts/quick_validate.py skills/sensemaking
```

行为 benchmark 必须记录 model、host instructions、skill path、run count、grader 与原始 evidence。被全局 instructions 或 memory 污染的 baseline 不能解读为裸模型对照；缺失的 timing/token 数据不得填零后用于效率结论。
