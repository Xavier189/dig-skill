结论：`dig` 已结束。下一步应进入 **Security/Cryptography domain design review**，先形成并评审可落地的安全设计；不要直接进入 implementation，也不要重新挖需求。（置信度：高）

这项工作应由熟悉 KMS/HSM、envelope encryption、PII protection 和生产密钥轮换的安全领域负责人主导，并引入独立的 domain reviewer。该阶段至少要确定：

- KEK/DEK 层级、密文 envelope 格式、key version 与 KMS/HSM trust boundary；
- online rotation 的读写兼容窗口、重加密策略、零停机迁移与并发一致性；
- audit trail、least privilege、职责分离和 break-glass 控制；
- rollback 的触发条件、可回退边界、旧 key 保留策略与故障恢复；
- threat model、失败模式以及上线前必须提供的验证证据。

原因是需求与成功约束已经确认，但高风险的 cryptographic design 尚未完成。先通过安全与密码学领域评审，再据此进入 implementation planning，才能避免把不可审计或不可回退的设计直接带进生产实现。
