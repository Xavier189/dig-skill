# Roadmap

仓库是 dig 的单一事实源（`~/.claude/skills/dig` 是指向 `skills/dig` 的 symlink），所有迭代在此维护。

## 1. Description 触发优化（v1.x，观察期后启动）

针对已知的「中型任务犹豫带」风险（见 [benchmark-v1.md](benchmark-v1.md) 分析师备注与 README 观察期一节）。

做法（skill-creator 的自动化优化环节）：

1. 生成 20 条真实风格的触发评估查询（8-10 条应触发 + 8-10 条不应触发的近似干扰项），用户审核签字
2. 跑优化循环（后台，约 5 轮迭代）：
   ```bash
   cd ~/.claude/skills/skill-creator && python3 -m scripts.run_loop \
     --eval-set <trigger-eval.json> --skill-path <repo>/skills/dig \
     --model <当前会话模型> --max-iterations 5 --verbose
   ```
   脚本自动 60/40 切分训练/保留集，每条查询跑 3 次取触发率，按保留集分数选 `best_description` 防过拟合
3. 用 `best_description` 更新 SKILL.md frontmatter，前后对比入库

启动时机：`docs/observations.md` 攒到 3+ 条「漏触发」记录后（用真实失败案例替换部分合成查询，优化更对症）。

## 2. 观察期反馈闭环（进行中）

- 2026-07-03：首批真实反馈到达（机械化执行 / 提问偏参数 / 澄清后不追问，详见 [observations.md](observations.md) 三条）→ **v2 已发布**：假设先行 + 收敛驱动 loop + 深浅问校准示例，决策记录见 [design.md](design.md) D1-R1。
- 2026-07-07：外部对照吸收（trq212《finding your unknowns》官方博客文 + Claude Code 官方《Designing Loops》+ 顺藤挖出的 mattpocock/skills）→ **v2.1 已发布**：提问门槛加"事实自查、决策必问"分界线、ASK 加 show-don't-ask 通道（品味类分叉附草案）、纪要交接附实现期 Deviations 协议、Success criteria 加可验证性引导。四处均句子级、删句即回滚，决策记录 [design.md](design.md) D7 + §2.1。不跑 eval，随 v2 同批观察；观察重点追加：show-don't-ask 该用没用/被滥用、用户连续答"不知道"的频率（blind spot pass 候选场景，README 观察清单 9/10）。
- 2026-07-07：用户疑虑驱动（批量提问的批内依赖：Q1 的回答可能使 Q2 作废或选项全错）→ **v2.2 已发布**：ASK 加批内独立性约束——存在或选项集依赖本批另一答案的问题留给 loop（在那里恰好满足 cite-the-answer 门槛），仅推荐变化写条件式推荐留批内。独立问题并行 + 依赖链 loop 逐层串行，一次一问流派的依赖感知被结构性收编而批量哲学不变。决策记录 [design.md](design.md) D8；观察重点：依赖仍混批 / 过度拆批（README 观察清单 11）。
- 2026-07-07：用户疑虑驱动（CONTEXT 步 session 开头大量读取是否得不偿失，首个真实案例复盘：本地 case/local-case-1.md，诊断类深读 1912 行被判定为正面样本）→ **v2.3 已发布**：CONTEXT 加与提问对称的读取门槛——read only what could change the hypothesis or the questions，能写出 named trap 与分叉即停；深度随任务类型分档（诊断/改造类挖掘即任务且长排查前预告、新功能类读结构/入口/惯例、方向/选型类读文档）。案例已脱敏存档 [observations.md](observations.md) 作"深读正当"界碑。决策记录 [design.md](design.md) D9；观察重点：任务类型误判（README 观察清单 12）。
- 本轮按用户决策**不跑 evals/iteration-2**，先真实使用观察。v2 观察重点：loop 收敛轮数分布、假设是否任务特定（vs 模板化）、"开工"逃生口触发情况、校准示例是否被照抄到不相干任务。
- 运行中按 [README 观察清单](../README.md#观察期与已知风险) 记录到 [observations.md](observations.md)。
- iteration-2 启动条件：v2 观察攒 3+ 条或出现高频模式；届时与 iteration-1 对照（评分基建已就位），并考虑把 loop 收敛性写成新 assertion。

## 3. Harness 联动（远期）

澄清纪要落盘参数化：`status` 字段扩展、按条件自动落盘、外部 harness 通过固定五节标题锚点消费（接口契约见 README「澄清纪要落盘」一节，不可破坏性变更）。

## 4. 开源发布待办

- [x] 跨平台兼容（2026-07-03）：对齐 Agent Skills 开放标准，SKILL.md 单文件通用化（CC 一等 + 内置降级措辞），README 平台安装矩阵（Claude Code / Codex / Cursor 详细，其余指向 agentskills.io）——决策记录 design.md D6
- [ ] 确认 LICENSE（当前 MIT，可换）
- [x] GitHub 仓库已建并公开：[Xavier189/dig-skill](https://github.com/Xavier189/dig-skill)
- [x] 仓库描述与 topics（claude-code, claude-skill, agent-skills, requirements-engineering, socratic-method, ai-agents, codex, cursor）

## 5. 同类项目联动（远期候选）

[mattpocock/skills](https://github.com/mattpocock/skills) 的 wayfinder（in-progress 状态）与 dig 天然衔接：dig 判定"任务过大转拆分"后，拆出的子任务目前只是一段建议文本；wayfinder 把这类超 session 的模糊工作变成 issue tracker 上的共享决策地图（fog of war 渐进立 ticket，一次 session 只解决一个）。若其毕业出 in-progress，评估"dig 拆分 → wayfinder 式地图"的交接形态。对照记录见 [design.md](design.md) §2.1。
