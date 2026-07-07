# dig skill 设计说明

日期：2026-07-02（v1）· 2026-07-03（v2）· 状态：v2 已上线

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

### 2.1 事后对照（2026-07-07，v2.1 输入）

v2 上线后对照的两篇外部文章与一个同类仓库；吸收与否决的决策记录见 D7。

| 参照物 | 机制 | 对照结论 |
|---|---|---|
| [A field guide to Claude Fable: finding your unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns)（Thariq/Anthropic，2026-07-03，X 长文收录进官方博客） | map（prompt/context）≠ territory（真实约束），差值 = unknowns，按 Rumsfeld 四象限拆解；interview / brainstorm-prototype / blind spot pass / references / 实现期 implementation-notes / 事后 quiz 全周期手法 | 独立同源印证：其 interview 例句 "prioritize questions where my answer would change the architecture" 与 dig 提问门槛逐字重合，且立场是模型越强瓶颈越向"人澄清 unknowns 的能力"移——dig 类 skill 价值随模型进步上升。dig 多出假设先行、批量提问、收敛准入、memo 契约；它多出的 show-don't-ask 与实现期 Deviations 被 v2.1 吸收，blind spot pass 转观察项 |
| [Designing Loops](https://x.com/ClaudeDevs/status/2074208949205881033)（Claude Code 官方博文，2026-07-06） | loop = agent 循环工作直到停止条件，按触发/停止/原语/适用任务四维分类（turn-based / goal-based / time-based / proactive）；质量靠可自验证的量化检查 + 把个别修复编码进系统 | 与 dig 是同一工作流的两端：dig 提高人参与的质量（灌入隐性知识），loop 减少人的参与（自主跑更久）——挖得净，loop 才跑得远。v2.1 的 Success criteria 可验证性引导来自"检查越量化越容易自验证"；"把个别修复编码进系统"正是 observations→design 修订循环的既有做法，获官方印证 |
| [mattpocock/skills](https://github.com/mattpocock/skills)：grilling 系（grill-me / grill-with-docs）+ wayfinder | grilling：一次一问的严酷 interview 直到共识，"事实自查、决策必问"，每问带推荐答案，确认前不动工；grill-with-docs 附带产出 ADR 与 glossary；wayfinder（in-progress）：超单 session 的大工作在 issue tracker 建共享决策地图，fog of war 渐进立 ticket，一次 session 只解决一个 | grilling 与 dig 在"一次一问 vs 批量"上正面对立（Matt Pocock 明言 "Asking multiple questions at once is bewildering"）——验证 D1 否决项是真实存在的流派，属用户偏好分歧而非对错；其"事实自查、决策必问"分界线被 v2.1 吸收进提问门槛。wayfinder 恰好是 dig"任务过大转拆分"之后缺失的承接形态，远期联动候选（roadmap §5） |

## 3. 关键决策记录（含被否决项与代价）

### D1 挖掘风格：先拆解后批量精准提问 ｜ 可逆性：高

- **选定**：DECOMPOSE → CHECKLIST 六维扫描 → 批量 ASK（每批 ≤4、带推荐、硬上限两轮）
- **否决**：一次一问对话式（brainstorming 哲学）。作者明确反感挤牙膏；代价是放弃顺藤摸瓜的深钻能力，由 CHECKLIST 六维扫描补盲区
- **否决**：对抗挑战式（socratic-architect 的降魔流）。作者不接受；代价是部分错误前提可能存活到纪要阶段，由"ASK 前先亮拆解图景供当场纠错"补偿

#### D1-R1 修订（2026-07-03，v2）｜ 可逆性：高

- 触发：v1 上线一天的真实使用反馈（observations.md 2026-07-03 三条）——流程被机械执行：提问偏参数没追真实诉求、✅🔍❓ 表与六维清单走过场、澄清后答案带出的新细节不被追问，两轮硬上限制度性砍断深挖。
- 废除："Hard cap: two rounds"；DECOMPOSE 拆解表与 CHECKLIST 六维清单的独立步骤形态。
- 替代：假设先行（三段可证伪陈述：真实目标 / 最易做错处 / 开做草案，✅🔍❓ 附着在草案分叉行上）；六维降为对假设的压力测试探针（禁止逐维填行）；收敛驱动 loop——新问题准入门槛 = 在问题内引用哪句答案 + 指明决定哪个分叉，连续两轮分叉不减 → 转提议拆任务，"开工"随时强制收敛。
- 维持原判：否决"一次一问对话式"不变。loop 是多轮批量（每批 ≤4 带选项推荐），每轮存在的理由是上一轮答案改变了图景；已知问题必须当轮问完，禁止藏问题凑轮次。v1 用 CHECKLIST 补偿被放弃的"顺藤摸瓜"，v2 由 loop 本体承担该能力，补偿机制退役。
- 新代价（有意接受）：单次 dig 变长、轮数不可预测；SKILL.md 77→~110 行，触发加载成本 +~40%；拆解表让位于假设后，当场纠错性依赖"sketch 一行一决策 + ≤15 行"的措辞约束（列为观察项）；frontmatter description 仍写 "Decomposes the request"，与正文 HYPOTHESIZE 存在术语漂移（description 属触发优化线，本轮不动）。
- 回滚开关：恢复 "Hard cap: two rounds" 一句并删除 LOOP 节 = 回到 v1 节奏；假设先行与 loop 相互独立，可只回滚其一。
- 本轮不造 eval：先真实使用观察（用户决策），iteration-2 对比待 loop 行为有观察数据后启动。

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

### D6 跨平台兼容：单文件通用化（2026-07-03）｜ 可逆性：高

- 背景：开源后需支持 Codex/Cursor 等主流 coding agent（用户要求：CC 支持度最高，其余兼容，不支持 skill/斜杠注入的平台不管）。调研发现 SKILL.md 已是 [Agent Skills](https://agentskills.io) 开放标准（Anthropic 发布），Codex、Cursor、Gemini CLI、Copilot/VS Code 等数十家在官方采用名单：格式层兼容免费拿到，真正不可移植的只有正文 4 处 CC 专有引用。
- **选定**：SKILL.md 仍是唯一事实源；4 处专有引用（AskUserQuestion / plan mode / memory / 全局 CLAUDE.md）改能力式措辞——CC 工具名保留置前，各附一句降级做法；语言策略 = 模型消费文本全英文（校准示例任务随之英文化）、用户显示层保留中英双格式（纪要五节标题的中文注释是 harness 解析契约，不动）；README 平台矩阵 CC+Codex+Cursor 详细、其余一句指向 agentskills.io + AGENTS.md 版纪律片段。
- **否决**：adapters/ 平台适配层。N 份同步、漂移风险，破坏"仓库单一事实源"；代价是放弃按平台单独调优措辞的能力。
- **否决**：SKILL.md 纯 CC 语境不动、降级只写 README——非 CC 模型看到的是含陌生工具名的指令，降级行为不可控；代价是 CC 用户也会读到降级从句（正文 +0 行，从句内联）。
- 验收：Codex 实测冒烟**通过**（2026-07-03，codex-cli 0.142.5；模糊日志任务上完整产出三段假设（含两个任务特定 named trap）+ 单消息 4 问带选项/推荐/所测分叉 + 纪要确认前不动代码，~45k tokens）。安装路径实测收敛到跨 agent 共享目录 `~/.agents/skills/dig`（Codex 实测可发现，Cursor 官方文档亦列该目录），README 推荐一条软链服务多家；Cursor 文档级（项目 `.cursor/skills/`、用户 `~/.cursor/skills/` 为平台专属备选）。
- 边界：不承诺非 CC 平台自动触发与行为质量等效，手动调用兜底；非 CC 反馈走 GitHub issue（带平台与版本）。

### D7 v2.1：吸收外部同源实践（2026-07-07）｜ 可逆性：高（四处均为独立句子级改动，删句即回滚）

- 触发：两篇外部文章对照分析（见 §2.1）——trq212《finding your unknowns》与 Claude Code 官方《Designing Loops》，加上从前者评论区顺藤挖出的 mattpocock/skills。
- **选定**（SKILL.md 四处句子级吸收 + 两个观察项，不跑 eval 随 v2 同批观察）：
  1. 提问门槛加"事实/决策"分界线：能自查（代码/文档/git 历史）的事实不问用户，问题只留给决策——来自 grilling，与"答案会改变做法"门槛正交互补（一个滤掉不改变做法的问题，一个滤掉不该由用户回答的问题）
  2. ASK 节加 show-don't-ask 通道：品味类分叉（视觉/交互/措辞/命名）附 2-4 个具体草案让用户挑，不抽象提问——填补四象限中 unknown knowns（"看到才认得"）一格，问答对这类分叉天然低效；CC 上由 AskUserQuestion 的 option preview 承接
  3. SYNTHESIZE 交接附实现期协议：memo 未覆盖的新分叉，低影响选保守默认、记入 Deviations、继续；触及数据模型/对外接口/不可逆时回来问——来自 trq212 核心论点"光提前规划不够，unknowns 会在实现深处冒出来"，是 🔍 delegated 语义向实现期的自然延伸；memo 五节标题契约未动
  4. Success criteria 节加可验证性引导（measurable over sentiment）——来自 loops 文"检查越量化越容易自验证"，memo 是下游输入，可验证的标准让下游能自检
  5. 观察项（不动 SKILL.md）：a) show-don't-ask 该用没用/被滥用；b) 用户一轮内连续答"不知道/你定"（unknown unknowns 密集、用户非需求权威的场景）——攒 3+ 条再决定是否给 LOOP 加教育模式分支（blind spot pass：先解释分叉的后果差异再问）
- **否决**：全盘引入 Rumsfeld 四象限术语——SKILL.md 自有语言（✅🔍❓ + fork）已覆盖，叠第二套术语徒增加载与理解成本；代价是与外部文献的术语映射靠本记录承担
- **否决**：引入完整 implementation-notes.md 流程（trq212 原方案）——dig 定位是前置挖掘，实现期流程超出边界；只取一句话协议作为交接纪律；代价是实现期记录的结构化程度低于原方案
- **否决**：blind spot pass 立即入正文——触发场景（用户在陌生领域）的真实频率未知，先观察再加，避免 v1"清单走过场"教训在新分支上重演
- **维持原判**：D1 否决"一次一问"不变——grilling 的存在恰好证明该流派真实而非稻草人，分歧在用户偏好（作者反挤牙膏）而非对错
- 新代价（有意接受）：SKILL.md 108→110 行，三处原句加长，触发加载成本微增；show-don't-ask 给 ASK 步引入"判断分叉类型"的新自由度，误判（普通分叉滥做草案）列为观察项 5a
- 定位叙事（非 SKILL.md）：README 引入"模型越强，瓶颈越从模型能力移向人澄清 unknowns 的能力"（trq212）与"dig 挖得净、loop 才跑得远"（两文合并图景）

### D8 v2.2：批内独立性约束（2026-07-07）｜ 可逆性：高（一句话，删句即回滚）

- 触发：用户对批量提问的结构性疑虑——一次给 4 问，Q1 的回答可能使 Q2 不该问，或使 Q2 的选项全错，批内表达不了这种依赖。
- 分析：批内依赖三形态——**存在性依赖**（Q1 答案决定 Q2 该不该问）与**选项集依赖**（Q2 该问但选项随 Q1 变）是真问题；**仅推荐依赖**（问题与选项恒成立，只有推荐随 Q1 变）不是，条件式推荐即可解，卡它会把批量削成变相一次一问。现有机制已覆盖大半：loop 的 cite-the-answer 门槛本就是依赖问题的归宿（"born from answers"），假设先行使 ≤15 行草案的分叉行多为同层独立决策，AskUserQuestion 四问同框逐答也让用户能带着 Q1 的选择协调 Q2。缺口只在：SKILL.md 没有一句话禁止依赖问题混入同批，而 v1 教训 = 没写的纪律不被执行。
- **选定 A**：ASK 节加批内独立性约束——存在或选项集依赖本批另一答案的问题不进本批，留给 loop（在那里它恰好满足 cite-the-answer 门槛）；仅推荐变化不算依赖，写条件式推荐留在批内。效果 = 独立问题保持并行（批量的长处）+ 依赖链交给 loop 逐层串行（一次一问的长处，grilling "resolving dependencies one-by-one" 的真正优势被结构性收编）；批量哲学不变。
- **否决 B**（批内条件式问题，"若 Q1 选缓存：TTL？"）：选项组合爆炸、AskUserQuestion 无条件显隐能力、认知负担正是 grilling 指认的 bewildering 本尊。
- **否决 C**（改回一次一问）：D1 既有否决维持——轮次爆炸 + 审讯感 + 丢失四问同框的全局视野（用户能看出这批问题共同勾勒的方向对不对，一次一问给不了）。
- **否决 D**（不动措辞、信任模型自行处理）：v1 已证明没写的纪律靠不住。
- 新代价（有意接受）：深依赖链每层多一轮（但每轮仍并行其余独立问题，且这正是 loop 的本职）；"独立性"判断引入新自由度——过严会把仅推荐依赖也拆批、批量退化为变相一次一问，列为观察项（README 观察清单 11）。

### D9 v2.3：CONTEXT 读取门槛（2026-07-07）｜ 可逆性：高（一段话，删段即回滚）

- 触发：用户对 CONTEXT 步成本的疑虑——session 开头大量读取"是否得不偿失"，以首个真实案例 `case/local-case-1.md`（并发监控改造）为据。
- 案例复盘结论：该案例是深读的**正面样本**而非反例——诊断类任务（用户原话要求"仔细排查"），13 文件 1912 行零重复、顺藤摸瓜式定向排查、结论全部引用到（带行号）；排查推翻了提问的两个前提（bitmap 并非并发计数、"23 点开始不准"在代码中无对应机制），五个提问全部由排查产出。反事实：不读代码则顺着错误前提问出"bitmap 怎么优化"级伪问题，返工成本远超读取成本一个数量级。
- 结构性缺口确认：提问侧有硬门槛（答案改变做法 + cite-the-answer + 收敛判据），读取侧零门槛（仅 "Read what's relevant" 一句）。本案例模型判断对了，但 v1 教训 = 没写的纪律不被执行；真实风险场景是需求类任务被同样深读（读的内容不改变任何问题）、dig 后换 session 读取沉没只剩纪要。
- **选定 A+D**：CONTEXT 节加与提问对称的读取门槛——read only what could change the hypothesis or the questions，停止条件 = 能写出 named trap 与分叉（完全理解是工作阶段的事）；深度随任务类型分档：诊断/改造类挖掘即任务、深读正当且长排查前预告读什么为什么（体感优化）；新功能类读结构/入口/邻近惯例；方向/选型类文档即可。
- **否决 B**（排查委托 Explore subagent、主会话只收摘要）：诊断类的高保真细节会被摘要抹掉（案例中"userData 塞 receivedTime 保证加减落同一 key"这类细节决定方案正确性）；总 token 不省、时间多一跳；仅适合新功能类结构侦察，不做默认。
- **否决 C**（不动、攒反例再修）：A 成本仅一段话且不改变本案例行为（诊断类照样深读），等反例的收益不抵"没写的纪律不被执行"的风险。
- 案例存档：observations.md 记为正面样本（"深读正当"界碑），未来疑似过度读取的反例以它为对照基准；case/ 目录含内部代码细节，不入公开仓库。
- 新代价（有意接受）："任务类型分档"引入判断自由度——误判类型（把诊断类当功能类浅读，假设失去现实根基）列为观察项（README 观察清单 12）。

## 4. 失败模式自查

| 失败模式 | 对策 |
|---|---|
| 自动触发失灵 | CLAUDE.md 纪律 + `/dig` 手动，双兜底 |
| 挖掘太烦人 | 分级触发 + 逐问准入门槛（cite-the-answer）+ 连续冒分叉转拆任务 + "开工"逃生口（v2 起两轮上限废除） |
| 拆解方向跑偏 | ASK 前先亮三段假设（含标记分叉的开做草案），用户当场纠 |
| 纪要被略过直接开干 | HARD-RULE：纪要确认前禁止实现/出 plan |
| loop 不收敛 | 准入门槛两槽硬要求 + "no round quota" + too-big 信号；复发则按 D1-R1 回滚开关恢复上限 |
| 假设先行被填表化 | "换个任务仍成立即是废话"自测句 + named-trap 正反例 + ≤15 行上限；观察分类"假设质量"跟踪 |

## 5. 演进方向

- **触发观察期**：收集"该触发没触发 / 不该触发触发了"的案例，迭代 description 措辞
- **harness 联动**：落盘参数化（status 字段扩展、按条件自动落盘）
- **门槛调节**：若小任务失误率偏高，删除 description 的 Skip 句回到全量哲学
- **v2 观察期**：loop 收敛轮数分布、假设任务特异性（vs 模板化）、"开工"使用频率、校准示例是否被照抄到不相干任务
