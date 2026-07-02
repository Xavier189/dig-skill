# dig skill 设计说明

日期：2026-07-02 · 状态：v1 已上线

## 1. 背景与问题定义

作者长期用 superpowers 的 brainstorming skill（历史调用 18 次，个人技能中最高频）加上"新会话直接进 plan mode"的习惯，来补偿同一个问题：**Claude 的提问太浅、细节挖掘太少**。

四种实际经历的失败模式（作者自述，全部命中）：

1. 做完才发现要的是别的——真实意图未被挖出
2. 关键决策被静默代理，且决策错误
3. 问了但问得浅，没问到藏在深处的点 ← **作者自认的病根**
4. 成品与长期规划（"大盘子"）不匹配

诊断：1/2/4 是 3 的下游症状。提问质量 = 深度 × 完备性，两者都不足。若问得够深够细，其余三种失败会在事前暴露。

## 2. 调研：三个参照物的光谱

| 参照物 | 机制 | 结论 |
|---|---|---|
| [superpowers/brainstorming](https://github.com/obra/superpowers) | 一次一问收集信息 → spec → writing-plans 流水线 | 提问是手段非目的、面向设计收敛而非意图挖掘；且在作者环境中终态断链（未装全家桶） |
| [socratic-architect](https://github.com/roy-reshef/socratic-ai-prompt-skill) | 三层提问（澄清/挑战假设/视角转换），永不直接给答案 | 挖得深但纯思辨教练，不落地干活 |
| [requirements-elicitation](https://github.com/andreaswasita/copilot-agents-dojo) | 六维追问 + 铁律"不接受伪装成需求的方案" + user story 产出 | 方法论最完整但仪式过重（个人开发者不需要 user story 与签核） |

dig 取三者交集：比 brainstorming 挖得深，比 socratic-architect 务实（挖完要干活），比 requirements-elicitation 轻。

## 3. 关键决策记录（含被否决项与代价）

### D1 挖掘风格：先拆解后批量精准提问 ｜ 可逆性：高

- **选定**：DECOMPOSE → CHECKLIST 六维扫描 → 批量 ASK（每批 ≤4、带推荐、硬上限两轮）
- **否决**：一次一问对话式（brainstorming 哲学）。作者明确反感挤牙膏；代价是放弃顺藤摸瓜的深钻能力，由 CHECKLIST 六维扫描补盲区
- **否决**：对抗挑战式（socratic-architect 的降魔流）。作者不接受；代价是部分错误前提可能存活到纪要阶段，由"ASK 前先亮拆解图景供当场纠错"补偿

### D2 介入方式：分级自动 + plan mode 联动 + 可手动 ｜ 可逆性：高

- **否决**：强制全量前置（brainstorming 的 HARD-GATE 哲学）。小任务的打断成本 > 失误成本；代价是小型创建任务失去自动保护，兜底为 `/dig` 手动
- **否决**：纯手动。最需要挖的时候恰是用户没意识到自己模糊的时候

### D3 形态：新 skill + CLAUDE.md 纪律条目 ｜ 可逆性：高（删文件即回滚）

- **否决 B**（改造现有 brainstorming）：骨架处处相反（一次一问 vs 批量、强制写 spec vs 可选落盘、转 writing-plans vs 断链），改造量 ≈ 重写还背历史包袱
- **否决 C**（方法论全写进 CLAUDE.md）：常驻 +400~500 token，与作者刚完成的 context 瘦身矛盾；skill 的 progressive disclosure 平时只占 description ~120 token，触发时才加载 5KB 正文

### D4 卸载 brainstorming ｜ 可逆性：中（可重装，但丢失触发惯性）

- 理由：终态断链（writing-plans 未安装）+ 职责被 dig 完全接管 + 省 ~60 token/会话
- 代价：其 "You MUST" 强命令式 description 的高触发可靠性，由 CLAUDE.md 纪律条目继承

### D5 产出：纪要→无缝下游 + memory 沉淀 + 落盘默认关 ｜ 可逆性：高

- 落盘不强制但留固定格式口子：作者有自研 harness 工程，frontmatter 三字段 + 五节固定标题是未来联动的解析契约
- memory 沉淀防泛滥：每次 dig 至多 1-2 条、优先更新旧条目、跨项目事实建议用户手动进全局 CLAUDE.md（skill 不擅改全局配置）

## 4. 失败模式自查

| 失败模式 | 对策 |
|---|---|
| 自动触发失灵 | CLAUDE.md 纪律 + `/dig` 手动，双兜底 |
| 挖掘太烦人 | 分级触发 + 两轮硬上限 + 开放项 >8 先拆任务 |
| 拆解方向跑偏 | ASK 前先亮拆解图景（✅🔍❓ 逐行），用户当场纠 |
| 纪要被略过直接开干 | HARD-RULE：纪要确认前禁止实现/出 plan |

## 5. 演进方向

- **触发观察期**：收集"该触发没触发 / 不该触发触发了"的案例，迭代 description 措辞
- **harness 联动**：落盘参数化（status 字段扩展、按条件自动落盘）
- **门槛调节**：若小任务失误率偏高，删除 description 的 Skip 句回到全量哲学
