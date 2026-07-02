# dig — Socratic Requirements Excavation for Claude Code

在动手之前，先把你真正想要的东西挖出来。

dig 是一个 Claude Code skill：面对大任务或模糊指令时，它让 Claude 先拆解任务、识别所有模糊点与被静默代理的关键决策，把问题**批量、精准**地抛给你，形成一份 10 秒可确认的澄清纪要，然后才允许进入 plan 或实现。

## 它解决什么问题

AI 交付不符预期的四种常见失败模式：

| 失败模式 | 根因 |
|---|---|
| 做完才发现要的是别的 | 真实意图没被挖出来 |
| 关键决策被替你拍板 | 隐含决策没有上浮 |
| 问了但问得太浅 | 提问发生在拆解之前，只碰到表面参数 |
| 成品与长期规划不搭 | 会话不知道你的"大盘子" |

病根是第三条：**提问质量不够（深度 × 完备性）**，其余都是它的下游症状。dig 的解法是**先拆解、后提问**——未完成拆解与清单校验之前禁止提问，保证每个问题都打在刀口上。

## 核心机制

```
0. CONTEXT    读上下文与 memory（先看大盘子，再拆任务）
1. DECOMPOSE  拆解为子决策，标记 ✅已明确 / 🔍被代理的关键决策 / ❓模糊
2. CHECKLIST  六维清单防漏项（真实目标/边界/成功标准/失败场景/依赖约束/长期匹配）
3. ASK        先亮拆解图景供当场纠错，再批量精准提问（每批≤4、带选项与推荐、硬上限两轮）
4. SYNTHESIZE 澄清纪要五节，确认后无缝进 plan/实现
5. SETTLE     长期信息沉淀 memory；纪要落盘默认关闭（见 harness 契约）
```

提问铁律：每个问题必须锚定具体决策点，禁止无锚点的"还有什么要补充"；不接受伪装成需求的方案（"要个按钮"先追溯到它解决什么问题）；关键决策带推荐上浮而非默默拍板；开放项超过 ~8 个视为任务过大，先建议分解而不是审讯。

## 安装（两条腿，缺一不可）

**1. skill 本体**

```bash
cp -r skills/dig ~/.claude/skills/dig
```

**2. CLAUDE.md 触发纪律**

自动触发依赖模型对 description 的语义匹配，非 100% 确定，全局纪律条目是第二条腿。在 `~/.claude/CLAUDE.md` 的任务分级段落加入：

```markdown
大任务（新功能、架构变更、重构、复杂配置/选型）：
- 动手或进 plan mode 前，先用 dig skill 挖掘需求：拆解模糊点与隐含决策 → 批量精准提问 → 澄清纪要确认后才继续
```

## 使用

| 入口 | 说明 |
|---|---|
| 自动触发 | 大任务（新功能/新项目/架构或选型/重构/复杂配置）与含模糊目标的指令自动进入 |
| `/dig` 手动 | 任何时候显式调用，小任务想挖也可以 |
| plan mode 联动 | 大任务进 plan 前先完成 dig，纪要作为 plan 的输入 |

## 澄清纪要落盘（harness 接口契约）

默认不落盘。当用户要求保存（或外部 harness 请求）时，写入项目内 `docs/clarity/YYYY-MM-DD-<slug>.md`：

```markdown
---
task: <slug>
date: YYYY-MM-DD
status: confirmed   # confirmed | draft
---
## Goal（真实目标）
## Decisions（已拍板）
## Boundaries（明确不做）
## Success criteria（成功标准）
## Open items（开放项）
```

frontmatter 三字段 + 五个固定标题是机器可解析的稳定契约，消费端按标题锚点解析即可。**不要改动标题文案——它是接口。**

## 触发范围备注（与 superpowers/brainstorming 的差异）

dig 在作者的工作流中替代了 [superpowers](https://github.com/obra/superpowers) 的 brainstorming skill，但触发哲学不同：

- brainstorming：**全量强制**——任何创建类工作（含小改动）都必须先过设计流程
- dig：**分级触发**——大任务与模糊指令自动进入；小 bug fix、单点修改、纯信息问答不触发（随时可 `/dig` 手动补）

这是有意的取舍：小任务全量强制的打断成本高于其失误成本。若使用中发现小任务失误率偏高，删掉 description 末尾的 "Skip for small fixes..." 一句即可回到全量哲学（完全可逆）。

## 局限性备注

- 自动触发是语义匹配，非确定性机制；CLAUDE.md 纪律条目不可省略
- 为 Claude Code 设计，依赖其 AskUserQuestion 工具与 memory 机制；移植到其他 agent 框架需替换这两处
- 交互语言跟随用户全局配置，skill 内只做软引导（match the user's language, keep technical terms in original form）

## 设计文档

完整的需求挖掘过程、决策记录（含被否决方案与所放弃的代价）见 [docs/design.md](docs/design.md)。
