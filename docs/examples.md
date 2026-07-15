# 跨领域路由示例

本页用于校准一个不变量：**route 由当前 thinking state 决定，不由请求来源、输入格式、领域、生命周期或任务大小决定。** 案例不定义新 trigger。

## 同一表面任务，不同 thinking state

| 场景 | Starting point | 当前缺口 | Route |
|---|---|---|---|
| 产品需求 | “订单支持撤回。” | 先查状态机与补偿事实；谁可撤回、何时可撤回仍需 owner 决定 | inspect → Clarify |
| 产品需求 | “仅待支付订单可由下单人撤回；补偿、通知和验收已确认。” | action-ready | direct delivery + verification |
| 自发重构 | “改业务总要碰很多地方，不知道重划模块还是先改最痛链路。” | outcome 与选择依据未稳定 | inspect → Discover/Clarify |
| 自发重构 | “只提取现有校验到 helper，public contract 不变，测试已列清。” | 局部、可逆 | direct delivery + targeted tests |
| 性能优化 | “接口最近慢了，帮我优化。” | 根因是 fact uncertainty | diagnose；出现 SLO/成本/一致性 trade-off 再 Clarify |
| 依赖升级 | “把所有依赖升到最新版。” | 缺维护状态与 compatibility evidence | research；出现迁移选择再 Clarify |
| 个人小程序 | “想做自己的小程序，但不知道解决什么问题。” | 缺方向与判断依据 | Discover |
| 个人博客 | “Hugo、Cloudflare Pages、build 和 rollback 都已确认，直接部署。” | action-ready，只需核查配置 | inspect → direct delivery + smoke test |
| 资料目录 | “帮我整理积累多年的学习资料。” | 先缺目录事实，分类和删除原则可能未决 | inspect → 必要时 Clarify |
| 资料目录 | “按年份/主题移动，重复文件只报告不删除，未知类型进 `_review`，先 dry-run。” | 操作和风险边界明确 | execute dry-run + verify |
| 非代码方案 | “复盘会要求公开自我归责，同时希望大家主动暴露问题。” | goal 与 incentives 存在 material conflict | Challenge |

## 相同 thinking state，跨领域同一路线

| Thinking state | 软件/业务例子 | 非软件/个人例子 | Invariant |
|---|---|---|---|
| Direction uncertainty | 不知道监控改造要优化告警疲劳、可观测性还是值班响应 | 不知道博客是写作归档、知识库还是作品展示 | Discover |
| Decision uncertainty | partial success 会改变 API contract 与 recovery | 资料库按主题还是项目组织会改变检索方式 | Clarify |
| Validity uncertainty | PRD 同时要求“任何时候可撤回”和“审批后不可变更” | 公开归责却希望提高心理安全 | Challenge |
| Fact uncertainty | 性能退化根因未知 | 平台价格或部署限制未知 | inspect/research |
| Action-ready | 明确的局部 refactor | 明确的博客部署或目录 dry-run | skip shared-understanding work |
| Stable shared decisions | 汇总 confirmed/assumed/deferred/risk 给下一位开发 agent | 汇总活动范围、预算假设和隐私风险给下一次 session | STRUCTURE-only |

## STRUCTURE-only 反例

| 请求 | 使用 STRUCTURE-only？ | 原因 |
|---|---|---|
| “把这轮讨论中的 confirmed、assumed、invalidated、deferred 和 risk 整理成交接。” | 是 | 需要保存 decision-state semantics |
| “把邮件压缩到 150 字。” | 否 | 普通改写 |
| “按明确规则整理文件夹并输出移动报告。” | 否 | 普通文件操作 |
| “把两个 CSV 按订单号对齐并标出差异。” | 否 | 数据转换；规则冲突出现后才可能需要 owner decision |
| “总结文章的三条观点。” | 否 | 普通摘要 |
