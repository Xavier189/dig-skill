# dig（探骊）— 动手之前，先取到需求深处的那颗珠

> 典出《庄子》"探骊得珠"：骊珠藏于九重渊骊龙颔下，潜得够深，才拿得到最值钱的那个点。你说"加个缓存"，它先潜下去问："到底什么慢、慢在哪"——因为 AI 交付最贵的浪费不是做错，而是把不该做的东西漂亮地做完。

面对意图模糊、目标藏在方案背后、或关键决策没有说清的指令，dig 让 agent 开工前先干三件事——无论任务大小，也无论是不是代码任务：

1. **亮出理解假设**——"我理解你真正要的是 X、这事最容易做错在 Y、现在开做我会做 Z"，说错了你当场纠
2. **批量精准提问**——只问"答案会改变做法"的问题，每批 ≤4、带选项和推荐，绝不挤牙膏式一次一问
3. **探到珠再收工**——你的答案引出新分叉就继续追，挖净（或你喊"开工"）才收敛成一份 10 秒可确认的澄清纪要；确认后 dig 结束，把控制权交还下游

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
0. CONTEXT     读相关材料、来源与 memory（先看大盘子）；读取与提问同门槛——只读会改变假设或问题的，能立假设即停，深度随不确定性类型调整
1. HYPOTHESIZE 亮出可证伪假设：真实目标 / 最易做错处 / 开做草案（✅🔍❓ 标注分叉）；六维只做压力测试不填表
2. ASK         批量精准提问（每批≤4、批内相互独立、带选项与推荐、按影响排序），每问指明测试假设的哪一部分；品味类分叉不空问，附 2-4 个草案让你挑
3. LOOP        收敛驱动多轮：新问题须引用你的答案+指明分叉；无新分叉即收敛；持续冒分叉→提议拆任务；随时说"开工"强制收敛
4. SYNTHESIZE  澄清纪要五节；确认后 dig 结束，把 memo 交还下游（新分叉按 Deviations 协议处理，不可逆的回来问）
5. SETTLE      仅在用户或 harness 明确要求时沉淀长期 memory；纪要落盘默认关闭（见 harness 契约）
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

自动触发依赖模型对 description 的语义匹配，非 100% 确定，全局纪律条目是第二条腿。在 `~/.claude/CLAUDE.md` 加入独立的需求清晰度判断，不要塞进小/中/大任务分级：

```markdown
需求清晰度检查（与任务大小、代码/非代码无关）：
- 当用户意图、真实目标、范围、约束、成功标准或隐藏决策存在会改变交付方式的不确定性时，先用 dig skill：亮出理解假设 → 批量精准提问 → 追问到收敛 → 澄清纪要确认。
- 清晰且 decision-complete 的请求直接执行，即使任务很大；模糊请求必须 dig，即使改动很小。
- 用户显式要求使用 dig 或“帮我挖需求”时，无条件执行。
- 纪要确认后 dig 结束；后续 design、reviewer、plan 与 implementation 按任务领域、规模和风险另行决定。
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
Use the dig skill whenever the user's intent, real goal, scope, constraints, success
criteria, or hidden decisions are unclear enough that different answers would change
the deliverable. Task size and domain do not decide whether dig runs: skip it for a
decision-complete request even when large, and use it for an ambiguous request even
when small. Explicit requests to use dig always override the skip. After the clarity
memo is confirmed, end dig and choose design, review, planning, and implementation
independently for the task's domain, size, and risk.
```

## 跨平台降级说明

SKILL.md 单文件即全部方法论，Claude Code 专有能力在正文内置了降级路径，无需适配文件：

| 能力 | Claude Code | 其他平台 |
|---|---|---|
| 结构化提问 | AskUserQuestion（选项卡交互） | 单条消息内编号问题列表，每问带选项与推荐 |
| 长期记忆沉淀（SETTLE） | memory 机制 | 无持久记忆则跳过写入 |
| 全局触发纪律 | CLAUDE.md 条目 | AGENTS.md 或等价全局指令文件 |
| 下游交接 | 纪要确认后结束 dig | 调用方按领域、规模和风险选择后续流程 |
| 自动触发 | description 匹配 + CLAUDE.md 双保险 | 取决于客户端实现，手动调用兜底 |

同一份指令在不同模型、不同客户端上跑出来的质量本来就有差异。遇到问题请带上平台与版本信息提 issue。

## 使用

| 入口 | 说明 |
|---|---|
| 自动触发 | 意图、目标、范围、约束、成功标准或隐藏决策存在会改变交付方式的不确定性时进入；与任务大小和领域无关 |
| `/dig` 手动 | 任何时候显式调用，小任务想挖也可以 |
| 下游交接 | 纪要确认后 dig 结束；是否进入 plan、调用 reviewer 或直接执行由下游独立决定 |

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

## 触发范围：清晰度与任务分级正交

dig 不属于小/中/大任务分级，它只回答一个问题：**用户真正要什么，是否已经清楚到可以开工？**

- 清晰的大任务：跳过 dig，按任务自己的 design/review/plan 流程执行
- 模糊的小任务：先 dig；小不代表不存在不同解释
- 清晰的小任务与纯信息问答：直接执行
- 显式 `/dig`：无条件执行，即使请求看起来已经清楚

这与 [superpowers](https://github.com/obra/superpowers) brainstorming 的“创建类任务全量强制设计”不同：dig 负责 requirements excavation，不负责设计流程，也不绑定 Software Architect 或任何其他 reviewer。

## 局限性备注

- 自动触发是语义匹配，非确定性机制；CLAUDE.md/AGENTS.md 的独立清晰度检查是确定性兜底
- 遵循 Agent Skills 开放标准，任何兼容客户端可用；Claude Code 上功能最全（AskUserQuestion、memory 等），其他平台按「跨平台降级说明」运行，行为质量依赖各客户端与模型的实现
- 交互语言跟随用户全局配置，skill 内只做软引导（match the user's language, keep technical terms in original form）

## 观察期与已知风险

**触发边界的已知风险**（置信度中）：模型可能把“任务复杂”误当成“需求不清”，也可能因改动很小而忽略一句话里的多个现实解释。观察重点不再是任务大小，而是：不同答案是否真的会改变交付方式。

**运行期观察清单**（遇到任一情况，记入 [docs/observations.md](docs/observations.md)）：

1. **漏触发**：需求存在会改变做法的分叉，却未挖直接开干 → 记下当时的指令原文，不论任务大小
2. **误触发**：请求已经 decision-complete，却仅因任务大/复杂被拉进挖掘流程 → 记下指令原文
3. **问题质量**：触发了但问得仍然浅、没打在刀口上 → 记下它问了什么、你期望它问什么
4. **烦人度**：单批问题过多、loop 轮次有被审讯感、说"开工"后仍被追问
5. **纪要质量**：五节纪要漏掉了讨论中已达成的关键共识
6. **显式调用覆盖**：用户明确要求 `/dig` 或“帮我挖需求”后仍被清晰度判断跳过
7. **loop 收敛性**：新问题给不出"由哪句答案引出"、轮数失控、该收敛不收敛
8. **假设质量**：三段假设写成放之四海而皆准的模板，没有任务特异性
9. **show-don't-ask**（v2.1）：品味类分叉（视觉/交互/措辞/命名）仍在空问"想要什么风格"而不给草案；或反过来，普通分叉被滥做草案拖慢节奏
10. **连续"不知道"**（v2.1 观察项）：用户一轮内多次回答"不知道/你定"——用户在陌生领域、连该有观点的决策点都不了解，当前只能靠选项推荐兜底
11. **批内独立性**（v2.2）：依赖问题仍混进同批（答完 Q1 发现 Q2 不该问或选项全错）；或反过来过度拆批——仅推荐会变的弱耦合也被拆去下一轮，批量退化成变相一次一问
12. **读取深度**（v2.3）：需求类任务被深读实现细节（读的内容不改变任何问题）；或反过来诊断类被浅读、假设失去现实根基（正面对照样本见 observations.md 2026-07-07 条）
13. **下游越界**（v2.4）：纪要确认后 dig 继续指定 design、Software Architect、plan 或 implementation；或非代码任务被路由到软件 reviewer

**观察结果 → 对策映射**（调整开关已备好，按症下药）：

| 观察到 | 对策 |
|---|---|
| 含真实分叉的请求频繁漏触发 | description 增补不确定性信号，或在全局纪律中强化“不同答案是否改变交付方式”的判断 |
| 模糊小任务被直接执行 | 明确任务大小不参与 clarity gate，补充小任务正例 |
| 清晰大任务频繁误触发 | 强化 decision-complete 反例，禁止用规模/复杂度替代不确定性判断 |
| 问题仍然浅 | 问题不在触发在执行：检查校准示例是否被读懂、收紧"答案会改变做法"门槛措辞（v2 已引入假设先行，复发则记录具体问题原文） |
| loop 不收敛 | 收紧准入门槛措辞，或按 design.md D1-R1 回滚开关恢复轮数上限 |
| 纪要漏共识 | 在 SYNTHESIZE 步增加"对照全部已回答问题逐条核销"的校验指令 |
| show-don't-ask 用错方向 | 该用没用 → 在校准示例补品味类正反例；滥用 → 收紧"taste call the user will only recognize on sight"的界定措辞（design.md D7） |
| 连续"不知道"高频出现 | 攒 3+ 条 → 考虑给 LOOP 加教育模式分支：先解释该分叉的后果差异再问（blind spot pass，design.md D7 观察项） |
| 批内依赖仍混入 / 过度拆批 | 前者 → 收紧 "existence or option set" 措辞并补批内依赖反例；后者 → 强化"仅推荐变化不算依赖"一句（design.md D8） |
| 读取深度错档 | 需求类被深读 → 收紧 "read only what could change the hypothesis" 措辞；诊断类被浅读 → 强化"诊断类挖掘即任务"一句（design.md D9） |
| dig 指定下游 workflow/reviewer | 收紧 SYNTHESIZE 终点：确认 memo 后立即结束，领域路由交还调用方（design.md D10） |

反馈闭环：观察记录攒够一批、出现高频模式，或暴露能推翻产品定义的结构性问题后，带着 `docs/observations.md` 迭代当前版本。

## 评估

iteration-1（2026-07-02，3 用例 × with/baseline 对照，6 个独立 subagent）：**with-skill 13/13 assertions 全过，baseline 12/13**。量化摘要与 7 条分析师备注（含 baseline 污染因子、量化外质差分析）见 [docs/benchmark-v1.md](docs/benchmark-v1.md)；完整输出与逐条评分证据在 [evals/iteration-1/](evals/iteration-1/)；测试用例定义在 [evals/evals.json](evals/evals.json)。

iteration-2（2026-07-12，v2.4）：6 个新版边界用例全部通过；其中 3 个与 v2.3 snapshot 对照，新版解决了“模糊小任务被跳过”和“清晰大任务被强制 dig”。完整 benchmark、逐条证据和静态 review 页面见 [evals/iteration-2/](evals/iteration-2/)；注意 baseline 只覆盖 eval 0-2，`+0.58` 不是平衡 A/B 的总体提升估计。

## 设计文档与路线

完整的需求挖掘过程、决策记录（含被否决方案与所放弃的代价）见 [docs/design.md](docs/design.md)；迭代计划（description 触发优化、观察期闭环、harness 联动、开源发布待办）见 [docs/roadmap.md](docs/roadmap.md)。

## License

[MIT](LICENSE)
