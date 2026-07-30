# Sensemaking（探骊）

> Turn uncertainty into shared understanding. —— 把不确定性转化为共同理解。

Sensemaking 是一个跨领域的 **adaptive thought-partner skill**。它不替你写实现，也不接管 design / plan / review 流水线——只在真正卡住时，把不确定性变成可讨论、可拍板、可交接的 shared understanding：

- **缺方向** → 找到可比较的方向与判断依据（Discover）
- **有会改变结果的人责选择** → 把决策上浮并收敛（Clarify）
- **已有方案可能不成立** → 用证据挑战硬伤（Challenge）
- **thinking 已完成** → 必要时保存带状态的 shared decisions（STRUCTURE）

它不按任务大小、代码/非代码、输入格式或工作阶段触发。完成当前 thinking job 后立即结束，把控制权交还下游。

![Sensemaking routing](docs/assets/sensemaking-routing.svg)

---

## 解决什么问题

AI 辅助工作里最贵的浪费，往往不是执行力不够，而是在错误理解上漂亮地做完：

| 失败模式 | 真正缺的是 |
|---|---|
| 做完才发现要的是别的 | 方向或真实目标尚未形成 |
| 关键选择被默默替你定了 | 会改变结果的 human-owned decision 没有上浮 |
| 方案看起来完整，落地才发现自相矛盾 | 已有 proposal 里的 material defect 没被挑战 |
| 谈过一轮，换 session / 换 agent 又丢 | shared decisions 缺少可延续的状态 |

Sensemaking 只处理这几类 **thinking-state** 问题。产品需求、个人想法、重构、部署、资料整理、制度设计——都只是 starting point，不是专属领域。

---

## 什么场景下使用

判断标准只有一条：**当前真正缺的是方向、会改变结果的人责决策，还是对已有方案的有效性检验？**

### 该用

| 场景 | 缺什么 | 路线 | 得到什么 |
|---|---|---|---|
| “想做个小程序，但不知道解决什么问题” | 方向与判断标准 | **Discover** | 2–4 个后果不同的方向，能比较后再选 |
| “订单支持撤回”——谁可撤、何时可撤、补偿怎么做都未拍板 | material forks | **Clarify** | 关键决策被确认、委托默认或明确暂缓 |
| “接口慢了，帮我优化”——查完发现有 SLO / 成本 / 一致性取舍 | 先事实，后 owner trade-off | diagnose → **Clarify** | 不靠猜根因；取舍上浮给人 |
| “改业务总碰很多地方，重划模块还是先改最痛链路？” | 选择依据未稳定 | inspect → **Discover / Clarify** | 可见的改造策略与边界 |
| PRD 同时要求“任何时候可撤回”和“审批后不可变更” | 方案自相矛盾 | **Challenge** | findings、最小修正或 accepted risk |
| 制度既要求公开自我归责，又希望大家主动暴露问题 | 目标与激励冲突 | **Challenge** | 把冲突说清，再决定修还是接受 |
| 讨论已收敛，要把 confirmed / assumed / deferred / risk 交给下一轮 | 只需保存状态 | **STRUCTURE-only** | 可交接的 shared-decision snapshot |
| 显式要求 brainstorm / 挖清楚 / grill 这个方案 | 点名要 thinking partnership | 对应 mode | 最小必要 mode，做完即停 |

### 不该用（或先别用）

| 场景 | 原因 | 该做什么 |
|---|---|---|
| 撤回规则、补偿、通知、验收都已确认 | action-ready | 直接交付 + 比例适当的 verification |
| 局部、可逆的 helper 抽取，public contract 不变 | agent-owned 实现选择 | 直接改 + 针对性测试 |
| “接口慢了”，日志 / 画像还没看 | 缺事实，不是缺决策 | inspect / diagnose；证据暴露 trade-off 再进入 |
| 压缩邮件、按规则整理文件夹、对齐 CSV | 普通改写 / 文件 / 数据操作 | 直接执行；规则冲突变成 owner decision 时再 Clarify |
| 没有可见缺陷，也没有人要求 review，只是想“再稳一点” | 仪式性 Challenge | 跳过 |

同一种表面任务可以走完全不同的路：一句话需求可能已经够清楚，也可能藏着会改 outcome 的分叉；大型迁移可能 decision-complete，也可能只缺事实证据。**route 只由当前 thinking state 决定。**

更多成对案例：[docs/examples.md](docs/examples.md)。

---

## 愿景与设计思想

### North Star

把 uncertainty 转化为**明确、可检验、可延续**的 shared understanding，同时不把本来已经清楚的工作拖进流程仪式。

### 一个入口，三种 mode

| 不确定性 | 关键问题 | Mode |
|---|---|---|
| Direction | 有哪些值得考虑的方向，依据是什么？ | Discover |
| Decision | 哪些现实选择必须由人承担，且会改变结果？ | Clarify |
| Validity | 当前 proposal / decision 是否存在实质缺陷？ | Challenge |

另两类故意不吞进来：

- **Fact uncertainty** → 先 inspect / research / diagnose / prototype
- **Action-ready** → 直接交付，不为“证明想过”而走流程

使用者往往说不清自己缺的是哪一种。拆成三个公开 skill 会逼人选对工具；**一个入口**让 agent 按信号路由，需要时再切换 mode，且绝不把三个当仪式全跑一遍。

### 设计原则

1. **Facts 归 agent，intent / 价值 / 风险 / 不可逆承诺归人**
2. **Consequence over checklist** — 答案不会改变结果的问题不配问
3. **Teach / show before ask** — 没有判断基础时，先补知识或给具体草案
4. **Attackable reasoning** — 假设与 finding 必须具体到能被当场否定
5. **Honest fog** — 暂时说不清就标 `not yet specified`，不制造假精确
6. **完成 thinking job 即停** — 不自动进入 design、plan、implementation 或 reviewer
7. **Task size 不是 workflow selector** — 清晰的大任务可跳过；模糊的小任务可进入

被否决方案及理由见 [docs/design.md](docs/design.md)。

---

## 三种 thinking mode

### Discover — 还没有方向

不假设用户心里藏着完整目标。先补 blind spots 与 decision-relevant knowledge，再展示 2–4 个**后果真正不同**的 frames，让人有能力比较后再收敛。

**完成：** chosen direction / shortlist / 待验证 hypothesis，或明确决定暂不继续。

### Clarify — 有 outcome，但仍有人责分叉

先读上下文、核查事实，只把会 materially 改变 outcome、scope、risk、success evidence 或 external commitment 的选择交给用户。品味类分叉给具体草案，不要求凭空描述。

**完成：** 每个 material fork 已确认、以可见默认委托，或明确暂缓。

### Challenge — 已有方案，需要检验

对已看见的矛盾、错误假设、失败路径或不安全边界，直接给 finding、依据、后果和最小修正。只在修正涉及价值取舍、风险承担或不可逆承诺时提问。

**完成：** material findings 被接受、修正、驳回并留理由，或记为 accepted risk。

---

## 与其他 skill / 能力如何协作

Sensemaking 负责 shared understanding；其他能力负责各自的缺口。它们**可组合，互不自动触发**。

| 当前缺口 | 最小动作 |
|---|---|
| 方向 / 人责决策 / 方案有效性 | Sensemaking |
| 事实、根因、兼容性、可行性 | inspect / research / diagnose / prototype |
| 可识别、可复用的领域方法 | 窄业务 skill（如隐私审查、对账、发版 checklist） |
| 已 action-ready，改动局部可逆 | 直接交付 + 比例适当的 verification |
| 会改 contract / data / failure / security / migration | compact design（需要追溯时再写 durable design） |
| 高风险或确需独立专业视角 | 按 domain 选 reviewer——不是 Sensemaking 的自动后继 |

典型组合：

1. **先 Sensemaking，再领域 skill** — 需求还在晃时先收敛，再用实现或审查 skill 执行。
2. **领域工作中途回到 Sensemaking** — 执行中发现选择会改对外承诺，停下来 Clarify / Challenge，再继续。
3. **不要因为刚做完 Sensemaking 就新建 skill** — 只有 trigger 可识别、方法可复用、边界可检验时，才值得抽取窄 skill。细则见 [docs/routing.md](docs/routing.md)。

Sensemaking 不是 reviewer 的替代品，也**不自动召唤** reviewer。Software Architect 只评 software architecture，绝不因为经过 Sensemaking 而出现。

---

## Shared state

STRUCTURE 是贯穿各 mode 的轻量状态层，不是固定表单。按需记录 intent、scope、requirements、constraints、decisions、assumptions、risks、success evidence、open items，并区分：

| 状态 | 含义 |
|---|---|
| `candidate` | 仍在探索的方向 |
| `confirmed` | 用户或权威来源已确认 |
| `assumed` | agent 的显式临时默认 |
| `invalidated` | 已被推翻，不可悄悄复活 |
| `deferred` | 有意暂缓，并保留默认或后果 |
| `risk` | 已知问题或接受的 trade-off |

短对话只需活在当前 context。多轮修订、跨 agent / session、审批或追溯确实需要时，才渲染 Direction Map、Clarity Memo、Challenge Report、Decision Brief、Requirements Brief 或 Handoff Snapshot。**默认不写文件。**

交接只描述“现在可以做什么”和仍未决项——不命令下游进入固定 workflow。

---

## 边界

- 可以是 session 或 agent 工作的第一步，没有其他 skill 前置。
- 完成当前 thinking job 后立即结束，不指定固定 successor。
- facts 由 agent 调查；intent、价值取舍、风险承担和 hard-to-reverse decisions 由用户决定。
- 独立 reviewer 仅在显式要求、高风险或确需第二专业视角时按 domain 选择。

---

## 安装

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

复制目录同样可用；symlink 更利于跟随仓库更新。自动触发取决于 host 对 description 的语义匹配；显式调用 `$sensemaking` 是可靠兜底。

---

## 文档

| 文档 | 何时阅读 |
|---|---|
| [产品设计](docs/design.md) | 核心模型、边界与被否决方案 |
| [下游路由](docs/routing.md) | skill / subagent / design / plan / review / 落盘如何选择 |
| [跨领域示例](docs/examples.md) | 用成对案例校准 route invariant |
| [维护资料入口](docs/internal/README.md) | 研究依据、eval 与图源 |

Skill 本体在 [`skills/sensemaking/`](skills/sensemaking/)，只保留 agent 执行指令与按需加载的 references。

---

## 验证

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/sensemaking
python3 -m json.tool evals/evals.json >/dev/null
```

行为校准覆盖 Discover、Clarify、Challenge、STRUCTURE-only、skip、fact-only investigation、跨领域不变量和下游边界。用例见 [`evals/evals.json`](evals/evals.json)。

---

## License

[MIT](LICENSE)
