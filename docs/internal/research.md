# 方法参照与取舍

以下为 2026-11-03 对上游 `main` 分支指令、官方文档与相关论文的核验与设计取舍，不是效果排名或运行基准。借鉴方法，未将第三方 Skill 包或执行流程作为依赖引入。

| 参照 | 吸收 | 不吸收 |
|---|---|---|
| [Matt Pocock grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) | 根据决定依赖按轮推进问题前沿（frontier）；每题附推荐答案；事实由 Agent（或独立上下文）调查 | 必须遍历设计树全部叶节点才算完成；统一要求用户确认后才允许进入下一步行动 |
| [Matt Pocock domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md) | 对照代码检验描述；用具体场景发现概念边界 | 每次明确术语就写词汇表；把讨论默认变成文档维护 |
| [Superpowers brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) | 相关上下文先行（Look Before You Ask）；信息齐全的小任务直接执行；比较方案及代价；Agent 自决的细节标为自身选择（your call）而非用户已同意 | 除非用户主动声明跳过提问，否则非琐碎改动一律强制先发独立方案消息、写并提交 `docs/superpowers/specs/` 设计文档、获批后再固定转调 `writing-plans` |
| [GSD assumptions mode](https://github.com/gsd-build/get-shit-done/blob/main/docs/workflow-discuss-mode.md) | 先分析代码，展示假设的证据、错误后果与不确定性，便于用户纠正 | 固定文件数量、阶段目录与输出文档；将现有实现当成用户期望 |
| [Spec Kit clarify](https://github.com/github/spec-kit/blob/main/templates/commands/clarify.md) | 按影响与不确定性处理覆盖缺口；更新矛盾陈述；问题说明意义并附推荐选项 | 规格文件前置、固定问题与答案长度、将设计方法完全排除在讨论之外 |
| [Requirements Clarity](https://github.com/softaworks/agent-toolkit/blob/main/skills/requirements-clarity/SKILL.md) | 核对价值并寻找更简单的实现 | 主观清晰度分数作为完成标准；默认生成 PRD；出现代码或路径就不触发 |
| [pstack](https://github.com/cursor/plugins/tree/main/pstack)（`cursor/plugins` 仓库中的个人工作流，作者 poteto；访问于 2026-11-04） | 首条回复复述目标与问题且不等待确认；两次同前提修复失败后直接验证前提（Attack the Premise）；能运行观察的分歧用一次性原型判定、不把可运行的检查交给用户；用户先别说出原因猜测以免收窄搜索（转为 Agent 先独立推导）；`/sharpen` 的专业做法、原始材料、方法工具与外部检验四问；`/blast-radius` 的证据等级 | 23 个 playbook 原样抄入 todo 的固定流程；回复中必须点名引用原则；默认多模型 arena/swarm；可逆工作默认不询问直接推进（与用户保留关键拍板权的选择冲突）；不提供可照打回复简写的做法（本项目在说明选项含义后保留附条件推荐项与简短确认） |

## 行业实践与学术依据

以下资料于 2026-11-03 核对一手来源，仅保留在内部维护文档中，不注入运行时 Skill 上下文：

| 议题与来源 | 核心发现与适用边界 | 设计落点 |
|---|---|---|
| **上下文供给、可验证检查与前置流程负担**<br>[Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)（访问于 2026-11-03）；[*Claude Code: Best practices for agentic coding*](https://web.archive.org/web/20250420034405/https://www.anthropic.com/engineering/claude-code-best-practices)（2025-04-18 发布，Wayback 存档）；[Birgitta Böckeler 对 SDD 工具的实测分析](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | 早期实践提倡 Explore → Plan → Code；当前官方文档聚焦补充代码外上下文、提供可运行检查，并指出全大写强调词会让模型机械过度执行。Böckeler 实测指出，重型 SDD 工具会把小修复膨胀为 4 个 user story 与 16 条验收标准（sledgehammer to crack a nut），或生成大量需人工审阅的 Markdown（overkill） | 用平实规则要求实质实现前核对期望结果、边界与成功证据；默认在对话上下文中维护轻量决策状态（`STRUCTURE`），不把重型静态 PRD/Spec 作为必经门禁 |
| **错误前提下的顺从偏见、抗压校准与用户自主权**<br>[EGDP (arXiv:2607.10411)](https://arxiv.org/abs/2607.10411)；[Thinking-in-Bets (arXiv:2610.34654)](https://arxiv.org/abs/2610.34654)；[Big-Big-SycoBench (arXiv:2610.15634)](https://arxiv.org/abs/2610.15634)；[Claude Constitution — Autonomy](https://www.anthropic.com/constitution) | EGDP 在 MLCQ 数据集与 7B–8B 模型上的 code smell 检测实验显示，带错误前提的提示会使判断翻转率（DFR）达 72%、错误顺从率（FAR）超 90%，先提取代码证据可将 DFR 降至 12%、FAR 降至 21%。Thinking-in-Bets 指出单纯要求模型“坚持立场”会导致其忽视真实错误，应在收到反馈前先绑定论断与验证依据；Big-Big-SycoBench 区分了对有效论据的响应率与对无效施压的顺从率；Claude 宪法 Autonomy 条款规定对不赞同的修法应先说明顾虑，但最终尊重用户在自身范围内的决定 | 将用户给定的根因判断与指定改法视为待核验假设：证据支持且边界清晰时直接推进；证据矛盾时说明真实机制并转向；证据不足时标明未核实并给出最小验证步骤；若解释证据后用户仍坚持在自身范围内按原方向修改，保持判断并说明未解决问题与附加风险，请用户确认一次后照办并留痕 |
| **选择性主动澄清与推理悖论**<br>[ClarifyGPT (arXiv:2310.10996)](https://arxiv.org/abs/2310.10996)；[Ask or Assume (arXiv:2603.26233)](https://arxiv.org/abs/2603.26233)；[ClarifyCodeBench (arXiv:2607.00711)](https://arxiv.org/abs/2607.00711)；[CONTRA (arXiv:2610.01769)](https://arxiv.org/abs/2610.01769) | ClarifyCodeBench 发现仅增加推理 token 能提升代码生成准确率，却几乎不提升主动澄清能力（Reasoning Paradox）；Ask or Assume 在欠规范 SWE-bench Verified 上将缺口检测与执行解耦后，解决率从 61.2% 升至 69.4%（完整规范为 70.8%）；CONTRA 通过检查不同候选答案是否导致程序在共享输入上的执行行为差异来筛选问题 | 保留显式的澄清判断规则：可查事实由 Agent 调查，局部可逆细节自行决定；仅当至少存在两个合理答案且会实质改变目标、可观测行为、验收依据或难逆转承诺时才向用户提问，并在证据支持时附条件推荐项供简短确认 |

## 组合后的原则

调查、解释、对话和设计可以交错。先在相关上下文中发现值得讨论的影响，再由事实、知识缺口、用户选择或验证需求决定下一步动作。

需求清楚不是跳过核验的理由；已经核验的前提也不因新消息而重复讨论。分析发现须关联当前目标，独立优化不得自动变成实施要求。

现有 Discover 的多种方向与具体例子、Clarify 的依赖感知提问、Challenge 的有依据判断和 STRUCTURE 的状态保留继续使用。主入口不再要求先识别某种不确定性或可见缺陷才能开始。

上述取舍需要通过真实风格输入和隔离 fixture 验证。热度、指令长度和方法数量不能证明触发可靠或结果更好。
