# dig（探骊）— 把还没想清楚的事，想深、说清、经得起质疑

dig 是一个跨领域的 adaptive thought-partner skill。

它不只在“需求模糊”时追问：当你不知道自己想做什么，它帮助发现方向；当你已有粗略目标，它帮助澄清真实分叉；当你已经给出需求或设计，它帮助找出缺陷、盲区、矛盾和未决点。

```text
                   ┌─ Discover：发现方向
原始想法与上下文 ──┼─ Clarify：澄清决策 ──→ STRUCTURE ──→ 可选输出
                   └─ Challenge：检验设计
```

STRUCTURE 贯穿三种 mode，持续区分哪些是候选方向、已确认决定、agent 假设、已推翻内容、暂缓项和已知风险。它防止一份看起来完整的总结把对话里的精确约束重新抹平。

遵循 [Agent Skills](https://agentskills.io) 开放格式，可安装到 Claude Code、Codex、Cursor 及其他兼容客户端。

## 它解决的不是一种问题

| 用户状态 | 真正需要的动作 | dig mode |
|---|---|---|
| “我也不知道想做什么” | 补认知、展示可能性、发现判断标准 | Discover |
| “大方向有了，但很多细节没想清” | 找出会改变结果的分叉并拍板 | Clarify |
| “方案已经写好了，帮我看看有没有问题” | 用证据、反例、失败场景和替代方案检验 | Challenge |

三种 mode 可以切换，但不会为了“流程完整”强制全走一遍。任务大小也不决定是否触发：清晰的大任务可以跳过 dig，模糊的小任务可以进入 Clarify，一句“我不知道自己想做什么”可以直接进入 Discover。

## Discover：需求还不存在时，先让它成为可能

Discover 不假设用户心里藏着一个等待被问出来的完整需求。

它会先判断用户缺的是方向、词汇、参考物，还是选择依据，然后使用：

- blind-spot pass：解释用户还不知道该问什么；
- multiple frames：给出 2–4 个后果真正不同的方向，不用单一“真实目标”锚定；
- teach/show-before-ask：用户没有判断基础时先解释、调研或展示；
- recognition over recall：用样例、对照、场景或 cheap prototype 让用户“看到才知道”；
- deliberate convergence：只有当用户能比较方向时才收敛。

Discover 可以结束于一个方向、一个 shortlist、一项待验证的 hypothesis，或“现在不值得继续”的明确判断，不强制生成 PRD。

## Clarify：只问真的会改变结果的问题

Clarify 保留了 dig v2.4 中验证最充分的能力：

- 先读相关上下文；能查到的事实不问用户；
- 把方案追溯回它试图解决的问题，不接受 solution-disguised-as-requirement；
- 提出可证伪的 outcome、task-specific traps 和 current sketch；
- 独立问题每批 2–4 个，依赖问题逐层追；
- 每问都必须能说明不同答案会怎样改变结果；
- taste call 不空问，给具体草案或示例；
- 回答只更新 delta，旧假设被推翻后明确标为 invalidated。

Clarify 的终点不是“问够若干轮”，而是所有 material fork 已确认、以显式默认委托、暂缓，或转化为 research/prototype 行动。

## Challenge：已有设计时，直接挑出问题

Challenge 不把已经看见的缺陷伪装成问题让用户重新回答。它先给 finding，再说明依据、后果和最小修正；只有价值取舍、风险承受或不可逆承诺仍需用户决定时才提问。

会按任务选择少数有效 lens：

- goal fit 与 proxy optimization；
- internal consistency；
- assumptions 与 evidence；
- boundaries、negative cases、failure/recovery；
- stakeholders 与 incentives；
- terminology 与 domain model；
- success/testability；
- reversibility 与 cheaper experiment；
- materially different alternatives。

pre-mortem、inversion、counterexample、first principles 等是按需工具，不是固定菜单。

Challenge 适用于软件设计，也适用于会议方案、制度、内容结构、运营流程、产品方向等非代码任务。

## STRUCTURE：需求结构化，而不是机械填表

dig 在对话中维护一份轻量 shared model，可能包含：

- Intent
- Stakeholders
- Scenarios
- Scope
- Requirements
- Constraints
- Decisions
- Assumptions & evidence
- Risks & edge cases
- Success evidence
- Open items

只记录当前任务真正需要的部分。每个 consequential item 使用明确状态：

| 状态 | 含义 |
|---|---|
| `candidate` | 仍在探索的方向 |
| `confirmed` | 用户或权威来源已确认 |
| `assumed` | agent 的显式临时默认 |
| `invalidated` | 已被推翻或替代，不可悄悄复活 |
| `deferred` | 有意暂缓，并记录默认或后果 |
| `risk` | 已知问题或接受的 trade-off |

短对话不展示内部标签。多轮讨论、决定被修改、精确数字/顺序/negative requirement 很重要，或需要跨 session handoff 时，才启用轻量 decision ledger。

## 输出不是固定流水线

按用户需要选择最轻的 renderer：

- Direction Map
- Clarity Memo
- Challenge Report
- Requirements Brief
- PRD / Spec（仅在明确需要时）
- 不落盘，只在对话中形成 shared understanding

默认不写文件。用户或授权 harness 要求持久化时，默认目录为：

```text
docs/discovery/YYYY-MM-DD-<slug>.md
docs/clarity/YYYY-MM-DD-<slug>.md
docs/challenges/YYYY-MM-DD-<slug>.md
```

旧 harness 需要 `Goal / Decisions / Boundaries / Success criteria / Open items` 五节契约时，可以把它作为 renderer adapter；这个兼容格式不再控制内部思考流程。

## 触发与跳过

应该触发：

- 用户明确说“不知道想做什么”、想 brainstorm/explore；
- intent、scope、constraint、success criteria、术语或 hidden decision 存在会改变结果的真实分叉；
- 用户显式要求 dig、clarify、grill、challenge、stress-test 或审查 requirement/design；
- 用户要求把散落讨论、修订决定或 requirements 结构化、对齐或转换为可靠摘要；
- 请求虽清晰，但已经看到会让静默执行不成立的 material contradiction/defect。

应该跳过：

- decision-complete、没有可见实质缺陷的执行请求；
- 纯信息问答；
- 简单改写、翻译、格式化等明确的一步任务；
- 普通 code review、debugging 或 implementation review——除非用户要审查的是其底层 intent/requirement/design。

`decision-complete` 不等于 `decision-sound`，但这也不授权 dig 把所有清晰任务变成强制 review。

## 与下游流程的边界

dig 只负责 discovery、clarity、challenge 和 shared-state structure。

- 对话或 critique 本身是交付物时，直接完成，不先设置 memo gate。
- dig 作为前置工作时，在 shared understanding 被接受前不开始依赖这些决定的下游交付。
- 完成后立即归还控制权，不指定 plan mode、implementation、architecture review 或 task-size workflow。
- 默认 inline、domain-aware challenge；独立 reviewer 是高风险或显式要求时的 escalation。
- 非软件任务永远不会因为 dig 被路由到 Software Architect。

## 安装

```bash
git clone https://github.com/Xavier189/dig-skill.git
```

### Claude Code

```bash
ln -s "$(pwd)/dig-skill/skills/dig" ~/.claude/skills/dig
```

### Codex / Cursor 共享目录

```bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)/dig-skill/skills/dig" ~/.agents/skills/dig
```

也可以复制目录而不使用 symlink。自动触发能力取决于具体客户端；显式调用始终是可靠兜底。

建议在全局 instructions 中只放简短路由纪律，不复制完整流程：

```markdown
Use dig when the user lacks a direction, when materially different interpretations
would change the outcome, or when the user asks to challenge a requirement/design.
Skip clear execution requests unless a concrete material defect is already visible.
Dig never selects downstream planning, implementation, or reviewers.
```

## 项目结构

```text
skills/dig/
├── SKILL.md
└── references/
    ├── discover.md
    ├── clarify.md
    ├── challenge.md
    └── structure.md
```

完整产品决策见 [docs/design.md](docs/design.md)，落地与验收记录见 [docs/rebuild-v1-plan.md](docs/rebuild-v1-plan.md)，未来合并说明见 [docs/merge-notes.md](docs/merge-notes.md)。旧 v2.4 设计记录保存在 [docs/history/v2.4-design.md](docs/history/v2.4-design.md)。

## 验证

行为 eval 覆盖：

- 不知道方向时不被单一 hypothesis 锚定；
- 用户缺知识时先 teach/show 再 ask；
- solution-disguised-as-requirement 被追溯；
- 明确 critique 直接给 findings；
- 修改过的决定不在 summary 中复活；
- 清晰请求不会因为任务大小或“可能还有盲区”被误触发；
- 非代码任务不出现 Software Architect 或软件流程。

历史 benchmark 位于 `evals/iteration-1/`、`evals/iteration-2/`。rebuild v1 的量化结果见 [benchmark](evals/rebuild-v1/benchmark.md)，逐项新旧输出可在 [static review viewer](evals/rebuild-v1/review.html) 中检查。

## License

[MIT](LICENSE)
