# Sensemaking（探骊）

> Turn uncertainty into shared understanding.

Sensemaking 是一个跨领域的 adaptive thought-partner skill：当方向尚未形成时帮助探索，当现实选择仍会改变结果时帮助澄清，当已有方案需要检验时帮助挑战，并在必要时保存已经形成的 shared decisions。

它不按任务大小、代码/非代码、输入格式或工作阶段触发，也不接管后续 design、plan、implementation 或 reviewer 路由。

![Sensemaking routing](docs/assets/sensemaking-routing.svg)

## 一个入口，四种最小动作

| 当前真正缺什么 | 路线 | 结果 |
|---|---|---|
| 没有方向、词汇、例子或选择依据 | **Discover** | 可比较的方向、判断标准或待验证 hypothesis |
| outcome 已存在，但仍有 consequential human-owned choice | **Clarify** | 已确认、委托或暂缓的 material decisions |
| proposal/decision 需要检验，或已有 material defect | **Challenge** | findings、修订建议与 accepted risks |
| thinking 已完成，只需保存、对齐或交接 | **STRUCTURE-only** | 带状态的 shared understanding |
| 只缺事实、根因或可行性证据 | inspect / research / diagnose / prototype | evidence；必要时再进入 Sensemaking |
| 已 action-ready，且没有可见 material defect | skip | 直接交付并做比例适当的 verification |

同一种表面任务可能走不同路线：一句话需求可能已经足够清楚，也可能藏着会改变 outcome 的分叉；大型迁移可能 decision-complete，也可能只缺事实证据。route 只由当前 thinking state 决定。

## 三种 thinking mode

### Discover

用户缺少方向或判断基础时，不假设其心里藏着一个完整目标。先补充 blind spots、examples 和 decision-relevant knowledge，再展示 2–4 个后果真正不同的 frames，让用户有能力比较后再收敛。

### Clarify

先读取可获得的上下文并核查事实，只把会 materially 改变 outcome、scope、risk、success evidence 或 external commitment 的选择交给用户。问题按依赖关系组织；taste call 用具体草案帮助识别，不要求用户凭空描述。

### Challenge

对已经看见的矛盾、错误假设、失败路径或不安全边界直接给 finding、依据、后果和最小修正。只在修正涉及价值取舍、风险承担或不可逆承诺时提问。

## Shared state

STRUCTURE 是贯穿各 mode 的轻量状态层，不是固定表单。它按需记录 intent、scope、requirements、constraints、decisions、assumptions、risks、success evidence 和 open items，并区分：

| 状态 | 含义 |
|---|---|
| `candidate` | 仍在探索的方向 |
| `confirmed` | 用户或权威来源已确认 |
| `assumed` | agent 的显式临时默认 |
| `invalidated` | 已被推翻，不可悄悄复活 |
| `deferred` | 有意暂缓，并保留默认或后果 |
| `risk` | 已知问题或接受的 trade-off |

短对话只需在当前 context 中维护。多轮修订、跨 agent/session、审批或追溯确实需要时，才输出 Direction Map、Clarity Memo、Challenge Report、Decision Brief、Requirements Brief 或 Handoff Snapshot。默认不写文件。

## 边界

- 可以是 session 或 agent 工作的第一步，没有业务 skill 前置。
- 完成当前 thinking job 后立即结束，不指定固定 successor。
- task size 不是 workflow selector；清晰的大任务可以跳过，模糊的小任务可以进入。
- facts 由 agent 调查；intent、价值取舍、风险承担和 hard-to-reverse decisions 由用户决定。
- reviewer 只在显式要求、高风险或独立专业视角确有价值时使用，并按实际 domain 选择。
- Software Architect 只评 software architecture，绝不因为经过 Sensemaking 而自动出现。

## 安装

在仓库根目录执行：

```bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)/skills/sensemaking" ~/.agents/skills/sensemaking
```

Claude Code 也可以使用专属目录：

```bash
ln -s "$(pwd)/skills/sensemaking" ~/.claude/skills/sensemaking
```

复制目录同样可用；symlink 更便于让仓库版本作为 single source of truth。自动触发能力取决于 host，显式调用 `$sensemaking` 是可靠兜底。

## 文档

| 文档 | 何时阅读 |
|---|---|
| [产品设计](docs/design.md) | 理解核心模型、边界和被否决方案 |
| [下游路由](docs/routing.md) | 判断 skill、subagent、design、plan、review 与落盘边界 |
| [跨领域示例](docs/examples.md) | 用成对案例校准 route invariant |
| [维护资料入口](docs/internal/README.md) | 维护或演进 skill 时查研究依据、eval 与图源 |

Skill 本体位于 [`skills/sensemaking/`](skills/sensemaking/)，只保留 agent 执行所需的指令与按需加载 references；仓库说明与维护材料不会注入每次调用的 context。

## 验证

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/sensemaking
python3 -m json.tool evals/evals.json >/dev/null
```

行为校准覆盖 Discover、Clarify、Challenge、STRUCTURE-only、skip、fact-only investigation、跨领域不变量和下游边界。用例定义见 [`evals/evals.json`](evals/evals.json)，维护说明见 [evaluation.md](docs/internal/evaluation.md)。

## License

[MIT](LICENSE)
