# Dig 场景校准矩阵

本页只用于验证一个产品不变量：**route 由当前思考状态决定，不由请求来源、输入格式、领域、生命周期阶段或任务大小决定。**

这些案例是 calibration，不是 trigger 列表。遇到新场景时，应先套用通用 gate；不要再为“重构”“博客”或“文件整理”增加专属 mode。

## 同一种表面任务，因状态不同走不同路线

| 领域或载体 | Starting point | 当前真正缺口 | 最小路线 |
|---|---|---|---|
| 产品需求 | “订单支持撤回。” | 先查状态机、权限与补偿事实；仍有谁可撤回、何时可撤回等 owner decision | inspect → Clarify 剩余决定 |
| 产品需求 | “仅待支付订单可由下单人撤回；字段、补偿、通知和验收已确认，直接实现。” | 没有 consequential uncertainty | skip dig → direct delivery + verification |
| 自发重构 | “这个模块改需求越来越慢，我想重构，但不知道该重划模块还是拆服务。” | outcome 与选择依据尚未稳定 | inspect current coupling → Discover/Clarify |
| 自发重构 | “只提取现有校验逻辑到 package-private helper，public contract 不变，调用点和测试已列清。” | 局部、可逆、agent-owned 实现 | skip dig → direct delivery + targeted tests |
| 性能优化 | “接口最近慢了，帮我优化。” | 根因和现状是可查事实 | diagnose first；只有 SLO、成本或一致性 trade-off 未决时再 Clarify |
| 性能优化 | “已确认瓶颈是 N+1；改为现有 batch API，响应 contract 不变，目标与测试已明确。” | 已 action-ready | skip dig → direct delivery + measurement |
| 依赖升级 | “把所有依赖都升到最新版。” | 先缺 compatibility、breaking changes 与维护状态证据 | inspect/research；证据暴露迁移或风险选择时再 Clarify |
| 依赖升级 | “将库从 4.2.1 升到 4.2.3；release notes 无 breaking change，锁文件与回归范围已确认。” | 已 action-ready | skip dig → upgrade + verification |
| 个人小程序 | “想做个自己的小程序，但还不知道解决什么问题。” | 缺方向与判断依据 | Discover |
| 个人小程序 | “按现有 Taro 项目新增本地记账页，字段、交互、离线边界和验收已给出。” | 已 action-ready | skip dig；是否 planning 只看协调需要 |
| 个人博客 | “想弄个博客，但不知道是写作归档、知识库还是作品展示。” | 缺方向与比较标准 | Discover |
| 个人博客 | “把现有 Hugo 站点部署到 Cloudflare Pages；域名、build command、preview 和 rollback 已确认。” | 部署事实可查，目标已明确 | inspect config → direct delivery + smoke test；可按步骤维护 task state |
| 资料目录 | “帮我整理这个学习资料文件夹。” | 先缺目录现状；分类、保留/删除原则可能是 owner decision | inspect first → 仅对 consequential taxonomy/deletion choices Clarify |
| 资料目录 | “按年份/主题移动文件，重复文件只生成报告不删除，未知类型放 `_review`，先 dry-run。” | 操作与风险边界已明确 | skip dig → execute dry-run + verify |

## 相同思考状态，跨领域保持同一路线

| Thinking state | 软件或业务例子 | 非软件或个人例子 | Route invariant |
|---|---|---|---|
| Direction uncertainty | 不知道监控改造到底要解决告警疲劳、可观测性还是值班响应 | 不知道博客是为了长期写作、作品展示还是知识管理 | Discover |
| Decision uncertainty | API 是否允许 partial success 会改变 contract 和 recovery | 资料库按主题还是按项目组织会改变长期检索方式 | Clarify |
| Validity uncertainty | PRD 同时要求“任何时候可撤回”和“审批后不可变更” | 复盘会要求公开归责，却希望提高主动暴露问题的意愿 | Challenge，先给 finding |
| Fact uncertainty | 不知道性能退化的根因 | 不知道某博客平台当前价格或部署限制 | inspect/research，不因“未知”自动 dig |
| Action-ready | 明确的局部 refactor | 明确的博客部署或目录 dry-run | skip dig；按风险选择下游动作 |
| Stable shared decisions | 汇总已确认、假设、暂缓和风险给下一位开发 agent | 汇总已决定的活动范围、预算假设和隐私风险给下一次 session | narrow STRUCTURE-only |

## STRUCTURE-only 的边界

| 请求 | 是否使用 STRUCTURE-only | 原因 |
|---|---|---|
| “把这轮讨论中的 confirmed、assumed、invalidated、deferred 和 risk 整理成交接。” | 是 | 需要保存 shared-decision state |
| “把这封邮件压缩到 150 字。” | 否 | 普通改写，直接执行 |
| “按明确规则整理文件夹并输出移动报告。” | 否 | 普通文件操作，直接执行并验证 |
| “把两个 CSV 按订单号对齐并标出差异。” | 否 | 数据转换/核对；除非结果暴露需要 owner 决定的规则冲突 |
| “总结这篇文章的三条观点。” | 否 | 普通内容摘要，不含 decision-state semantics |

## 下游组合示例

dig 只决定 shared understanding 这一维，不决定整条工作流：

- 明确但复杂的博客迁移可以 `skip dig + inspect + compact design + plan + smoke test`。
- 模糊但很小的重构可以 `inspect + Clarify + direct delivery`，无需 subagent 或落盘。
- 高风险 encryption 需求可以 `skip dig + technical design + Security/Privacy review + rollout plan`。
- 文件夹整理可以 `inspect + direct dry-run + verification`；只有分类或删除原则存在真实 owner choice 时才短暂进入 Clarify。
