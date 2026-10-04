# 方法参照与取舍

以下为 2026-10-04 对上游 main 分支指令的阅读与设计取舍，不是效果排名或运行基准。借鉴方法，未将第三方 Skill 包或执行流程作为依赖引入。

| 参照 | 吸收 | 不吸收 |
|---|---|---|
| [Matt Pocock grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) | 根据决定依赖展开后续问题；事实由 Agent 调查；答案改变问题集合 | 穷尽所有分支、所有决定都交给用户、统一要求结束批准 |
| [Matt Pocock domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md) | 对照代码检验描述；用具体场景发现概念边界 | 每次明确术语就写词汇表；把讨论默认变成文档维护 |
| [Superpowers brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) | 功能与行为变更也开展探索；相关上下文先行；比较设计及代价 | 所有路径强制批准；复杂度只升不降；架构路径固定衔接 spec 和 plan |
| [GSD assumptions mode](https://github.com/gsd-build/get-shit-done/blob/main/docs/workflow-discuss-mode.md) | 先分析代码，展示假设的证据、错误后果与不确定性，便于用户纠正 | 固定文件数量、阶段目录与输出文档；将现有实现当成用户期望 |
| [Spec Kit clarify](https://github.com/github/spec-kit/blob/main/templates/commands/clarify.md) | 按影响与不确定性处理覆盖缺口；更新矛盾陈述；问题说明意义 | 规格文件前置、固定问题与答案长度、将设计方法完全排除在讨论之外 |
| [Requirements Clarity](https://github.com/softaworks/agent-toolkit/blob/main/skills/requirements-clarity/SKILL.md) | 核对价值并寻找更简单的实现 | 主观清晰度分数作为完成标准；默认生成 PRD；出现代码或路径就不触发 |

## 组合后的原则

调查、解释、对话和设计可以交错。先在相关上下文中发现值得讨论的影响，再由事实、知识缺口、用户选择或验证需求决定下一步动作。

需求清楚不是跳过核验的理由；已经核验的前提也不因新消息而重复讨论。分析发现须关联当前目标，独立优化不得自动变成实施要求。

现有 Discover 的多种方向与具体例子、Clarify 的依赖感知提问、Challenge 的有依据判断和 STRUCTURE 的状态保留继续使用。主入口不再要求先识别某种不确定性或可见缺陷才能开始。

上述取舍需要通过真实风格输入和隔离 fixture 验证。热度、指令长度和方法数量不能证明触发可靠或结果更好。
