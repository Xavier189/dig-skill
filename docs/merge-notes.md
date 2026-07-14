# Rebuild v1 Merge Notes

状态：已在独立分支完成，尚未合并到 `main`。

## 分支与基线

- source branch：`rewrite/adaptive-dig-v1`
- base branch：`main`
- base commit：`aca1ed53700da3ee9cb505724966540406d45d08`

## 合并内容

- 将 dig 重定义为 `Discover / Clarify / Challenge + STRUCTURE`；
- 解除 task size、software reviewer 与 downstream workflow 绑定；
- 新增四个 mode/reference playbook；
- 重写 README、design、roadmap 与行为 eval；
- 保留 v2.4 文档和旧 benchmark 作为 history/baseline，不让旧契约继续控制 active skill；
- 加入 9 组 rebuild v1 对照结果、grading、benchmark 和 static review viewer。

## 合并闸门

- [x] rebuild v1：34/34 assertions；
- [x] v2.4 baseline：27/34 assertions；
- [x] skill frontmatter 通过两套 validator；
- [x] JSON、Markdown 本地链接和 diff whitespace 检查通过；
- [x] `main` 保持在 base commit；
- [ ] 用户审核 [review viewer](../evals/rebuild-v1/review.html)；
- [ ] 用户明确决定合并。

## 未来合并

如果 `main` 仍停留在上述 base commit，推荐 fast-forward：

```bash
git switch main
git merge --ff-only rewrite/adaptive-dig-v1
```

如果 `main` 已前进，先检查双方 diff，再使用普通 merge 解决真实冲突；不要用 reset 或强制覆盖隐藏冲突。合并后如需整体撤回，优先 revert 本次 rebuild commit，独立分支继续保留作恢复点。
