# Sensemaking（探骊）

> Turn uncertainty into shared understanding. —— 把不确定性转化为共同理解。

Sensemaking 不是“又一个需求澄清 checklist”，也不是设计/计划/实现流水线。它是一个 **adaptive thought-partner skill**：在动手之前（或动手中途卡住时），帮你把真正卡住的东西变成可讨论、可拍板、可交接的 shared understanding。

一句话：**缺方向时找方向，有分叉时把决策上浮，有硬伤时把风险说穿——然后把控制权交还你的业务 skill 或下游执行。**

![Sensemaking routing](docs/assets/sensemaking-routing.svg)

---

## 这是干什么的

团队推广时最常被问的两句是：

1. **这东西到底解决什么？**
2. **我平时什么业务场景该用它？**

答案不是“怎么装 skill / 怎么敲 slash command”，而是：**什么 thinking state 下，继续往下做会浪费、做错或替人拍板。**

AI 交付里最贵的浪费，往往不是代码写错，而是：

| 常见惨剧 | 真正缺的是 |
|---|---|
| 做完才发现要的是别的 | 方向或真实目标没形成 |
| 关键选择被 agent 默默替你定了 | 会改变结果的 human-owned decision 没上浮 |
| 方案看起来完整，落地才发现自相矛盾 | 已有 proposal 里的 material defect 没被挑战 |
| 澄清过一轮，隔天/换人又丢 | shared decisions 的状态没有可交接载体 |

Sensemaking 只吃这四类问题。它不替你写业务实现，也不规定后面一定要 design、plan 或请 Software Architect。

---

## 什么时候用：业务与实践场景

判断标准只有一条：**当前真正缺的是方向、会改变结果的人责决策，还是对已有方案的有效性检验？**  
任务大小、是不是代码、来自谁、处在哪个生命周期阶段——都不决定要不要进。

### 该用

| 你听到的话 / 面对的局面 | 真正缺什么 | 走哪条路 | 期望结果 |
|---|---|---|---|
| “想做个小程序 / 内部工具，但还不知道解决什么问题” | 没方向、没判断标准 | **Discover** | 2–4 个后果不同的方向，能比较后再选 |
| “订单支持撤回” —— 谁可撤、何时可撤、补偿怎么做都没拍板 | 有 outcome，但 material forks 未决 | **Clarify** | 关键决策被确认、委托默认或明确暂缓 |
| “接口最近慢了，帮我优化一下” 后面发现有 SLO / 成本 / 一致性取舍 | 先缺事实，证据出来后出现 owner trade-off | diagnose → **Clarify** | 不靠猜根因；trade-off 上浮给人 |
| “改业务总要碰很多地方，不知道重划模块还是先改最痛链路” | 选择依据未稳定 | inspect → **Discover / Clarify** | 可见的改造策略与边界 |
| PRD 同时写“任何时候可撤回”和“审批后不可变更” | 已有方案自相矛盾 | **Challenge** | findings + 最小修正 / 接受的 risk |
| 复盘制度要求公开自我归责，又希望大家主动暴露问题 | 目标与激励冲突 | **Challenge** | 把冲突说清楚，再决定修制度还是接受 |
| 讨论已经收敛，要把 confirmed / assumed / deferred / risk 交给下一个 agent 或明天的自己 | thinking 完成，只需保存状态 | **STRUCTURE-only** | 可交接的 shared-decision snapshot |
| 显式说“帮我 brainstorm / 挖清楚 / grill 一下这个方案” | 用户点名要 thinking partnership | 对应 mode | 按最小必要 mode 做完即停 |

### 不该用（或先别用）

| 局面 | 原因 | 该做什么 |
|---|---|---|
| “仅待支付订单可由下单人撤回；补偿、通知、验收都已确认” | 已经 action-ready | 直接交付 + 比例适当的 verification |
| “只把现有校验抽到 helper，public contract 不变” | 局部、可逆、agent-owned | 直接改 + 针对性测试 |
| “接口慢了”且还没查过日志 / 画像 / 回归点 | 缺的是事实，不是决策 | inspect / diagnose；证据暴露 trade-off 再进 Sensemaking |
| “把邮件压到 150 字 / 按规则整理文件夹 / 对齐两个 CSV” | 普通改写、文件操作、数据转换 | 直接执行；只有规则冲突变成 owner decision 时才 Clarify |
| 只是想证明“方案够不够稳”而没有可见缺陷、也没人要求 review | 不要为仪式而 Challenge | 跳过 |

同一种表面任务可以走完全不同的路：一句话需求可能已经够清楚，也可能藏着会改 outcome 的分叉；大型迁移可能 decision-complete，也可能只缺事实证据。**route 只由当前 thinking state 决定。**

更多成对案例见 [docs/examples.md](docs/examples.md)。

---

## 愿景与设计思想

### North Star

把 uncertainty 转化为**明确、可检验、可延续**的 shared understanding，同时不把本来已经清楚的工作拖进流程仪式。

Sensemaking 解决的是 **thinking state**，不是某一种输入格式。产品需求、个人想法、重构、部署、资料整理、制度设计、现有文档——都只是 starting point。

### 为什么是一个入口，而不是三个 skill

不确定性需要对话协作的主要有三类：

| 不确定性 | 关键问题 | Mode |
|---|---|---|
| Direction | 有哪些值得考虑的方向，依据是什么？ | Discover |
| Decision | 哪些现实选择必须由人承担，且会改变结果？ | Clarify |
| Validity | 当前 proposal / decision 是否存在实质缺陷？ | Challenge |

用户往往**不知道**自己缺的是哪一种。拆成三个公开 skill，会逼人先选对工具；一个入口让 agent 按信号路由，需要时再切换 mode。

另两类故意不吞进来：

- **Fact uncertainty** → 先 inspect / research / diagnose / prototype
- **Action-ready** → 直接交付，不为“证明自己想过”而走流程

### 几条硬原则（设计取舍）

1. **Facts 归 agent，intent / 价值 / 风险 / 不可逆承诺归人** —— 能安全查到的别问；会改变结果的别替人定。
2. **Consequence over checklist** —— 只有答案不同会改变 frame、decision 或评价的问题才配问。
3. **Teach / show before ask** —— 用户没有判断基础时，先补知识、给例子或廉价草案，再问选择。
4. **Attackable reasoning** —— 假设、方向、finding 必须具体到能被用户当场否定。
5. **Honest fog** —— 暂时说不清就标 `not yet specified`，不制造假精确。
6. **完成 thinking job 即停** —— 不自动进入 design、plan、implementation 或 reviewer；下游按“现在还缺什么”另选。
7. **Task size 不是 workflow selector** —— 清晰的大任务可以跳过；模糊的小任务可以进入。

被否决的方案（以及为什么否）见 [docs/design.md](docs/design.md)：单一巨型流程、三个公开 skill、按任务大小选流程、固定输出 schema、默认独立 reviewer、默认自动落盘。

---

## 三种 thinking mode（最小必要）

### Discover — 还没有方向

用户缺的是目标、词汇、例子或选择依据，而不是“心里藏着一个完整需求等你挖”。先补 blind spots 与 decision-relevant knowledge，再展示 2–4 个**后果真正不同**的 frames，让人有能力比较后再收敛。

**完成：** 有了 chosen direction / shortlist / 待验证 hypothesis，或明确决定暂不继续。

### Clarify — 有 outcome，但仍有人责分叉

先读上下文、核查事实，只把会 materially 改变 outcome、scope、risk、success evidence 或 external commitment 的选择交给用户。品味类分叉给具体草案，不要求凭空描述。

**完成：** 每个 material fork 已确认、以可见默认委托、或明确暂缓。

### Challenge — 已有方案，需要检验

对已看见的矛盾、错误假设、失败路径或不安全边界，直接给 finding、依据、后果和最小修正。只在修正涉及价值取舍、风险承担或不可逆承诺时提问。

**完成：** material findings 被接受、修正、驳回并留理由，或记为 accepted risk。

Mode 可以随对话切换，但**绝不把三个当仪式全跑一遍**。只做当前缺口需要的最小动作。

---

## 怎么和业务 skill / 其他能力一起用

Sensemaking 解决的是 shared understanding；业务 skill、脚本、subagent、设计与评审解决的是另一层问题。它们**可组合，互不自动触发**。

```
你的请求
   │
   ├─ 缺方向 / 人责决策 / 方案有效性？ ──► Sensemaking（Discover / Clarify / Challenge）
   │                                         │
   │                                         ▼  thinking job 完成，交出 shared state
   │
   ├─ 只缺事实 / 根因 / 可行性？ ─────────► inspect / research / diagnose / prototype
   │
   ├─ 已有可识别的业务方法？ ─────────────► 窄业务 skill（对账、隐私审查、发布 checklist…）
   │
   └─ 已 action-ready？ ──────────────────► 直接交付 + 比例适当的 verification
                                              （必要时再 compact design / plan / domain review）
```

### 和团队里其他 skill 的分工

| 机制 | 解决什么 | 例子 |
|---|---|---|
| **Sensemaking** | 方向、consequential choice、validity | “要不要做 / 做成什么样才算对 / 这方案有没有硬伤” |
| **窄业务 skill** | 可识别触发 + 可复用方法/规则/模板 | privacy impact review、对账 workflow、发版 checklist |
| **文档 / schema / 权威源** | 项目事实与合同式规则 | 订单状态机、退款期限、内部 API |
| **AGENTS.md / 全局纪律** | 几乎每次都必须遵守的短规则 | 构建命令、禁止改生成文件 |
| **subagent** | 独立 workstream 或隔离第二视角 | 并行盘点 payment 与 inventory 影响 |
| **design / plan / reviewer** | 实现塑形、协调、高风险专业判断 | 改 contract 前的 compact design；Security review |

推荐用法：

1. **先 Sensemaking，再业务 skill** —— 当需求本身还在晃：先 Clarified / Challenged，再用你们的实现/审查 skill 干活。
2. **业务 skill 中途挂起，回来 Sensemaking** —— 执行中发现“这个选择会改对外承诺”，停下来 Clarify / Challenge，再恢复。
3. **不要因为刚做完 Sensemaking 就新建 skill** —— 只有 trigger 可识别、方法可复用、边界可检验、且反复踩坑或高风险时，才值得抽窄 skill（细则见 [docs/routing.md](docs/routing.md)）。
4. **Sensemaking 不是 reviewer 的替代品，也不自动召唤 reviewer** —— 默认 inline challenge；独立 reviewer 只在显式要求、高风险或确需第二专业视角时按 **domain** 选择。Software Architect 只评 software architecture。

### 显式调用

自动触发取决于 host 对 description 的语义匹配，不是 100% 确定。推广到团队时，建议同时告诉同事：

- 不确定要不要用时，直接 `$sensemaking` / 显式说“用 sensemaking 帮我看看”
- 已经想清楚、只是想执行时，**不要**为了“走流程”而调用
- 调用后如果本身已 action-ready，agent 应直接说明并停止，而不是硬造问题

---

## Shared state：谈完之后留下什么

STRUCTURE 是贯穿各 mode 的轻量状态层，**不是固定表单**。按需记录 intent、scope、requirements、constraints、decisions、assumptions、risks、success evidence、open items，并区分：

| 状态 | 含义 |
|---|---|
| `candidate` | 仍在探索的方向 |
| `confirmed` | 用户或权威来源已确认 |
| `assumed` | agent 的显式临时默认 |
| `invalidated` | 已被推翻，不可悄悄复活 |
| `deferred` | 有意暂缓，并保留默认或后果 |
| `risk` | 已知问题或接受的 trade-off |

短对话只需活在当前 context。多轮修订、跨 agent / session、审批或追溯确实需要时，才渲染 Direction Map、Clarity Memo、Challenge Report、Decision Brief、Requirements Brief 或 Handoff Snapshot。**默认不写文件。**

交接时只传“现在可以做什么”和仍未决的 `assumed` / `deferred` / `risk`——不命令下游进入固定 workflow。

---

## 边界（推广时一并讲清）

- 可以是 session 或 agent 工作的**第一步**，没有业务 skill 前置。
- 完成当前 thinking job 后**立即结束**，不指定固定 successor。
- facts 由 agent 调查；intent、价值取舍、风险承担和 hard-to-reverse decisions 由用户决定。
- reviewer 只在显式要求、高风险或独立专业视角确有价值时使用，并按实际 domain 选择。
- Software Architect 只评 software architecture，**绝不因为经过 Sensemaking 而自动出现**。

---

## 安装

仓库根目录：

```bash
git clone https://github.com/Xavier189/dig-skill.git
cd dig-skill
mkdir -p ~/.agents/skills
ln -s "$(pwd)/skills/sensemaking" ~/.agents/skills/sensemaking
```

Claude Code 也可挂到专属目录：

```bash
ln -s "$(pwd)/skills/sensemaking" ~/.claude/skills/sensemaking
```

`cp -r` 同样可用；symlink 更利于让本仓库作为 single source of truth。自动触发能力取决于 host；显式调用 `$sensemaking` 是可靠兜底。

可选：在 `AGENTS.md` / `CLAUDE.md` 加一条清晰度纪律，作为 description 匹配之外的第二条腿——**有会改变交付方式的方向/决策/有效性不确定性时先 Sensemaking；decision-complete 且无可见缺陷则跳过；显式点名则无条件进入。**

---

## 文档

| 文档 | 何时阅读 |
|---|---|
| [产品设计](docs/design.md) | 理解核心模型、边界和被否决方案 |
| [下游路由](docs/routing.md) | skill / subagent / design / plan / review / 落盘怎么选 |
| [跨领域示例](docs/examples.md) | 用成对案例校准“同表面任务、不同 thinking state” |
| [维护资料入口](docs/internal/README.md) | 维护或演进时查研究依据、eval 与图源 |

Skill 本体在 [`skills/sensemaking/`](skills/sensemaking/)，只保留 agent 执行指令与按需加载的 references；仓库说明与维护材料不会注入每次调用的 context。

---

## 验证

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/sensemaking
python3 -m json.tool evals/evals.json >/dev/null
```

行为校准覆盖 Discover、Clarify、Challenge、STRUCTURE-only、skip、fact-only investigation、跨领域不变量和下游边界。用例见 [`evals/evals.json`](evals/evals.json)，说明见 [evaluation.md](docs/internal/evaluation.md)。

---

## License

[MIT](LICENSE)
