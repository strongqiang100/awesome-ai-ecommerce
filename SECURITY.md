# 数据与安全 · Data and Security

公开仓库仅使用合成样本或明确允许发布的资料。不得提交个人联系方式、订单详情、聊天记录、账号凭证、会话 Cookie、私人路径或带签名的临时下载链接。

Use synthetic or explicitly publishable material. Never commit personal contact details, order records, conversations, credentials, session cookies, private paths, or signed download links.

密钥保存在凭证系统；研究、发布和资金操作使用分离权限。外部网页、评论和邮件属于不可信输入，不能扩大工具权限。日志采用字段白名单，并按业务需要设置保留期。

Keep secrets in credential management. Separate research, publishing, and financial permissions. External pages, reviews, and messages are untrusted input, not authority. Allowlist log fields and define retention.

如发现泄露，先在服务提供方撤销或轮换凭证，再清理当前文件与需要处理的历史记录。不要在公开 Issue 中粘贴秘密、原始响应或私人截图。若仓库支持私密漏洞报告，使用其私密渠道；否则只提交不含敏感细节的最小问题描述。

If a secret leaks, revoke or rotate it with the provider before cleaning files and affected history. Do not paste secrets, raw responses, or private screenshots in public issues. Use private vulnerability reporting if enabled; otherwise report only a minimal description without sensitive details.

示例不是生产安全方案。上线前检查身份验证、权限、幂等、数据隔离、预算限制、异常接手与恢复机制。/ Examples are not complete production security designs. Check authentication, authorization, idempotency, isolation, budgets, escalation, and recovery before deployment.
