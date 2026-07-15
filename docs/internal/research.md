# 方法参照与取舍

本页记录当前设计真正吸收的外部思想，不复述产品文档。

| 参照 | 吸收 | 不吸收 |
|---|---|---|
| [Superpowers brainstorming](https://github.com/obra/superpowers) | context-first、alternatives、incremental validation | every-project hard gate、forced spec → plan pipeline |
| [Matt Pocock skills](https://github.com/mattpocock/skills) 的 grilling / wayfinding 方法 | facts 与 decisions 分离、dependency-aware questions、shared understanding、fog of war | relentless tone、全程 one-question doctrine、普通任务默认 issue map |
| [Socratic AI prompt skill](https://github.com/roy-reshef/socratic-ai-prompt-skill) | challenge assumptions、perspective shift | 永不直接给答案的纯教练定位 |
| [Requirements elicitation examples](https://github.com/andreaswasita/copilot-agents-dojo) | 不接受 solution-disguised-as-requirement、关注边界与验收 | 固定维度逐项填表、默认 user story/sign-off ceremony |
| [Finding your unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns) | blind spots、references、show/prototype before asking、unknowns 会在全周期出现 | 把所有 unknowns 强制装进前置 checklist |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | ambiguity、coverage、consistency 与 testability lens | software artifact pipeline 作为跨领域核心 |

## 形成的原则

1. 提问只是获得 decision-relevant information 的工具，不是完成度指标。
2. 能查证的 facts 由 agent 调查；用户只承担 intent、价值取舍与不可逆决定。
3. 用户没有词汇或判断基础时，show/teach/prototype 比更精致的问卷有效。
4. Discover、Clarify 与 Challenge 需要不同默认动作，不能压成单一流程。
5. shared state 需要保存修订语义，但 renderer 不应反向控制 thinking。
6. 后续 design、review、plan 与 execution 是独立维度，不能由 task size 或某个 mode 自动串联。
