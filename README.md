# dig（探骊）— 动手之前，先取到需求深处的那颗珠

> 典出《庄子》"探骊得珠"：骊珠藏于九重渊骊龙颔下，潜得够深，才拿得到最值钱的那个点。你说"加个缓存"，它先潜下去问："到底什么慢、慢在哪"——因为 AI 编码最贵的浪费不是写错代码，而是把不该做的东西漂亮地做完。

面对大任务或模糊指令，dig 让 agent 开工前先干三件事：

1. **亮出理解假设**——"我理解你真正要的是 X、这事最容易做错在 Y、现在开做我会做 Z"，说错了你当场纠
2. **批量精准提问**——只问"答案会改变做法"的问题，每批 ≤4、带选项和推荐，绝不挤牙膏式一次一问
3. **探到珠再收工**——你的答案引出新分叉就继续追，挖净（或你喊"开工"）才收敛成一份 10 秒可确认的澄清纪要，确认后才进 plan/实现

遵循 [Agent Skills](https://agentskills.io) 开放标准。Claude Code 支持最完整，Codex / Cursor / Gemini CLI 等数十家兼容客户端也能用。

## 它解决什么问题

AI 交付不符预期的四种常见失败模式：

| 失败模式 | 根因 |
|---|---|
| 做完才发现要的是别的 | 真实意图没被挖出来 |
| 关键决策被替你拍板 | 隐含决策没有上浮 |
| 问了但问得太浅 | 问题没过"答案会改变做法"这道门槛，只碰表面参数 |
| 成品与长期规划不搭 | 会话不知道你的"大盘子" |

病根是第三条：提问质量不够（深度 × 完备性），其余都是它的下游症状。v1 的解法是先拆解、后批量提问。用了一天发现拆解本身也会被走过场：表格填了，清单扫了，问出来的还是参数题。所以 v2 换成**假设先行 + 收敛循环**——先亮出可证伪的理解假设（你真正要什么 / 这事最易做错在哪 / 现在开做我会怎么做），问题只能从假设最不稳的地方长出来，且必须过"答案会改变做法"这道门槛。答案引出新分叉就继续追问，每个新问题都要说得出由哪句答案引出、决定哪个分叉。挖净，或者你喊"开工"，才收敛。

这个赌注有外部印证。Anthropic 官方博客《[finding your unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns)》的论断是：模型越强，交付质量的瓶颈越从模型能力移向"你把自己的 unknowns 澄清到什么程度"——需求挖掘的价值随模型进步上升，而不是被淘汰。Claude Code 官方的《Designing Loops》讲另一端：agent 要自主跑得久，前提是"完成"可验证、方向不含糊。dig 站在两端的交点上：开工前把 unknowns 挖净，后面的 loop 才自主跑得远（对照分析见 [design.md §2.1](docs/design.md)）。

## 核心机制

```
0. CONTEXT     读上下文与 memory（先看大盘子）；读取与提问同门槛——只读会改变假设或问题的，能立假设即停，深度随任务类型（诊断深读/功能读结构/选型读文档）
1. HYPOTHESIZE 亮出可证伪假设：真实目标 / 最易做错处 / 开做草案（✅🔍❓ 标注分叉）；六维只做压力测试不填表
2. ASK         批量精准提问（每批≤4、批内相互独立、带选项与推荐、按影响排序），每问指明测试假设的哪一部分；品味类分叉不空问，附 2-4 个草案让你挑
3. LOOP        收敛驱动多轮：新问题须引用你的答案+指明分叉；无新分叉即收敛；持续冒分叉→提议拆任务；随时说"开工"强制收敛
4. SYNTHESIZE  澄清纪要五节，确认后进 plan/实现（交接附 Deviations 协议：实现中冒出纪要没盖住的分叉，低影响选保守默认记录后继续，不可逆的回来问）
5. SETTLE      长期信息沉淀 memory；纪要落盘默认关闭（见 harness 契约）
```

提问铁律：答案会改变做法的问题才配问，两个现实答案若导向同一做法就不值得问；能靠读代码/文档/git 历史自查的事实不拿去问用户，问题只留给决策；同批问题必须相互独立——某问题的存在或选项集随本批另一问题的答案而变，就留给下一轮（那正是 loop 的本职），只有推荐会变的写条件式推荐留在批内；每个问题必须指明测试假设的哪一部分，禁止无锚点的"还有什么要补充"；不接受伪装成需求的方案（"要个按钮"先追溯到它解决什么问题）；关键决策带推荐上浮，不默默拍板；开放项超过 ~8 个视为任务过大，先建议分解而不是审讯，loop 中连续两轮新分叉不减也同样转拆分。

## 安装

dig 遵循 [Agent Skills](https://agentskills.io) 开放标准（SKILL.md 格式），可在任何兼容客户端使用。Claude Code 支持最完整，其余平台按「跨平台降级说明」运行。本仓库是唯一维护处，各平台都推荐 symlink 跟随仓库更新（不想跟随可改用 `cp -r`）。

```bash
git clone https://github.com/Xavier189/dig-skill.git
```

### Claude Code

**1. skill 本体**

```bash
ln -s "$(pwd)/dig-skill/skills/dig" ~/.claude/skills/dig
```

**2. CLAUDE.md 触发纪律**

自动触发依赖模型对 description 的语义匹配，非 100% 确定，全局纪律条目是第二条腿。在 `~/.claude/CLAUDE.md` 的任务分级段落加入：

```markdown
大任务（新功能、架构变更、重构、复杂配置/选型）：
- 动手或进 plan mode 前，先用 dig skill 挖掘需求：拆解模糊点与隐含决策 → 批量精准提问 → 澄清纪要确认后才继续
```

### Codex / Cursor（共用 `~/.agents/skills/`，一条软链服务多家）

两家都读取跨 agent 共享的用户级 skills 目录 `~/.agents/skills/`：

```bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)/dig-skill/skills/dig" ~/.agents/skills/dig
```

- **Codex**：启动时按 description 发现，任务匹配即激活（早期版本需 `codex --enable skills` 手动开启）；平台专属目录 `~/.codex/skills/` 亦可。已在 codex-cli 0.142.5 实测：从 `~/.agents/skills/` 正常发现，且模糊任务上完整走出"三段假设（含任务特定风险点）→ 单条消息 4 问（带选项、推荐、注明所测分叉）→ 纪要确认前不动代码"的降级形态。
- **Cursor**：`/dig` 手动调用，Agent 亦会按 description 自动选用（官方文档：[Agent Skills | Cursor Docs](https://cursor.com/docs/skills)）；平台专属目录为项目级 `.cursor/skills/`、用户级 `~/.cursor/skills/`。注：Cursor 侧为文档级支持，未实测，问题请提 issue。
- 触发第二条腿：在 `AGENTS.md` 或项目 AGENTS.md 加入下方纪律片段。

### AGENTS.md 纪律片段（非 Claude Code 平台的第二条腿）

```markdown
For substantial tasks (new features, architecture or technology decisions, refactors,
complex configuration), run the dig skill BEFORE starting work or writing a plan:
hypothesize → batched precise questions → loop until nothing new surfaces → clarity
memo confirmed by the user.
```

## 跨平台降级说明

SKILL.md 单文件即全部方法论，Claude Code 专有能力在正文内置了降级路径，无需适配文件：

| 能力 | Claude Code | 其他平台 |
|---|---|---|
| 结构化提问 | AskUserQuestion（选项卡交互） | 单条消息内编号问题列表，每问带选项与推荐 |
| 长期记忆沉淀（SETTLE） | memory 机制 | 无持久记忆则跳过写入 |
| 全局触发纪律 | CLAUDE.md 条目 | AGENTS.md 或等价全局指令文件 |
| plan mode 联动 | 纪要作为 plan 的输入 | 各平台等价 planning 流程同理 |
| 自动触发 | description 匹配 + CLAUDE.md 双保险 | 取决于客户端实现，手动调用兜底 |

同一份指令在不同模型、不同客户端上跑出来的质量本来就有差异。遇到问题请带上平台与版本信息提 issue。

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

- brainstorming：全量强制，任何创建类工作（含小改动）都必须先过设计流程
- dig：分级触发，大任务与模糊指令自动进入；小 bug fix、单点修改、纯信息问答不触发（随时可 `/dig` 手动补）

这是有意的取舍：小任务全量强制的打断成本高于其失误成本。若使用中发现小任务失误率偏高，删掉 description 末尾的 "Skip for small fixes..." 一句即可回到全量哲学（完全可逆）。

## 局限性备注

- 自动触发是语义匹配，非确定性机制；CLAUDE.md 纪律条目不可省略
- 遵循 Agent Skills 开放标准，任何兼容客户端可用；Claude Code 上功能最全（AskUserQuestion、memory、plan mode 联动都可用），其他平台按「跨平台降级说明」运行，行为质量依赖各客户端与模型的实现
- 交互语言跟随用户全局配置，skill 内只做软引导（match the user's language, keep technical terms in original form）

## 观察期与已知风险（v1 上线备注）

**触发力度的已知风险**（置信度中）：被替代的 brainstorming 使用 "You MUST … any creative work" 命令式措辞，触发力极强；dig 的 description 是条件式（"Use BEFORE substantial tasks…" / "Skip for…"），语义匹配柔性更大。预期影响分布：

- 大任务：不担心，description + CLAUDE.md 纪律双保险
- 小任务：设计上就不触发（`/dig` 手动兜底）
- **中等大小任务：存在犹豫带**。"中型功能改动"算不算 substantial 由模型现场判断，这是最可能漏触发的区间

**运行期观察清单**（遇到任一情况，记入 [docs/observations.md](docs/observations.md)）：

1. **漏触发**：该挖没挖直接开干 → 记下当时的指令原文
2. **误触发**：小任务/纯问答被拉进挖掘流程 → 记下指令原文
3. **问题质量**：触发了但问得仍然浅、没打在刀口上 → 记下它问了什么、你期望它问什么
4. **烦人度**：单批问题过多、loop 轮次有被审讯感、说"开工"后仍被追问
5. **纪要质量**：五节纪要漏掉了讨论中已达成的关键共识
6. **plan mode 联动**：大任务进 plan 前没有先跑 dig
7. **loop 收敛性**：新问题给不出"由哪句答案引出"、轮数失控、该收敛不收敛
8. **假设质量**：三段假设写成放之四海而皆准的模板，没有任务特异性
9. **show-don't-ask**（v2.1）：品味类分叉（视觉/交互/措辞/命名）仍在空问"想要什么风格"而不给草案；或反过来，普通分叉被滥做草案拖慢节奏
10. **连续"不知道"**（v2.1 观察项）：用户一轮内多次回答"不知道/你定"——用户在陌生领域、连该有观点的决策点都不了解，当前只能靠选项推荐兜底
11. **批内独立性**（v2.2）：依赖问题仍混进同批（答完 Q1 发现 Q2 不该问或选项全错）；或反过来过度拆批——仅推荐会变的弱耦合也被拆去下一轮，批量退化成变相一次一问
12. **读取深度**（v2.3）：需求类任务被深读实现细节（读的内容不改变任何问题）；或反过来诊断类被浅读、假设失去现实根基（正面对照样本见 observations.md 2026-07-07 条）

**观察结果 → 对策映射**（调整开关已备好，按症下药）：

| 观察到 | 对策 |
|---|---|
| 中型任务频繁漏触发 | description 增补命令式措辞（"You MUST use…"），或在 CLAUDE.md 纪律条目里细化任务分级线 |
| 小任务失误率偏高 | 删除 description 末尾 Skip 句，回到全量哲学 |
| 误触发频繁 | 收紧 substantial 的定义、显式扩充 Skip 列表 |
| 问题仍然浅 | 问题不在触发在执行：检查校准示例是否被读懂、收紧"答案会改变做法"门槛措辞（v2 已引入假设先行，复发则记录具体问题原文） |
| loop 不收敛 | 收紧准入门槛措辞，或按 design.md D1-R1 回滚开关恢复轮数上限 |
| 纪要漏共识 | 在 SYNTHESIZE 步增加"对照全部已回答问题逐条核销"的校验指令 |
| show-don't-ask 用错方向 | 该用没用 → 在校准示例补品味类正反例；滥用 → 收紧"taste call the user will only recognize on sight"的界定措辞（design.md D7） |
| 连续"不知道"高频出现 | 攒 3+ 条 → 考虑给 LOOP 加教育模式分支：先解释该分叉的后果差异再问（blind spot pass，design.md D7 观察项） |
| 批内依赖仍混入 / 过度拆批 | 前者 → 收紧 "existence or option set" 措辞并补批内依赖反例；后者 → 强化"仅推荐变化不算依赖"一句（design.md D8） |
| 读取深度错档 | 需求类被深读 → 收紧 "read only what could change the hypothesis" 措辞；诊断类被浅读 → 强化"诊断类挖掘即任务"一句（design.md D9） |

反馈闭环：观察记录攒够一批（或出现高频模式）后，带着 `docs/observations.md` 迭代 v2。

## 评估

iteration-1（2026-07-02，3 用例 × with/baseline 对照，6 个独立 subagent）：**with-skill 13/13 assertions 全过，baseline 12/13**。量化摘要与 7 条分析师备注（含 baseline 污染因子、量化外质差分析）见 [docs/benchmark-v1.md](docs/benchmark-v1.md)；完整输出与逐条评分证据在 [evals/iteration-1/](evals/iteration-1/)；测试用例定义在 [evals/evals.json](evals/evals.json)。

v2（2026-07-03）按决策未跑新 eval，先真实使用观察（见 [docs/roadmap.md](docs/roadmap.md) §2）；iteration-1 数据反映的是 v1 行为。

## 设计文档与路线

完整的需求挖掘过程、决策记录（含被否决方案与所放弃的代价）见 [docs/design.md](docs/design.md)；迭代计划（description 触发优化、观察期闭环、harness 联动、开源发布待办）见 [docs/roadmap.md](docs/roadmap.md)。

## License

[MIT](LICENSE)
