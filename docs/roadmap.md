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

- 运行中按 [README 观察清单](../README.md#观察期与已知风险v1-上线备注) 记录到 [observations.md](observations.md)
- 攒一批或出现高频模式 → 按「观察结果 → 对策映射」迭代 → 发 v2，跑 `evals/iteration-2` 与 iteration-1 对比（评分基建已就位）

## 3. Harness 联动（远期）

澄清纪要落盘参数化：`status` 字段扩展、按条件自动落盘、外部 harness 通过固定五节标题锚点消费（接口契约见 README「澄清纪要落盘」一节，不可破坏性变更）。

## 4. 开源发布待办

- [ ] 确认 LICENSE（当前 MIT，可换）
- [ ] `gh repo create dig-skill --public --source . --push`
- [ ] 补充 GitHub 仓库描述与 topics（claude-code, skill, requirements, socratic）
