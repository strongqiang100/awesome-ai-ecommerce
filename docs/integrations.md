# API 接入说明 · API Integration Notes

[中文入口](../README.md) · [English home](../README.en.md) · [证据 / Evidence](sources.md)

## 平台能力矩阵 / Platform capability matrix

| 平台 / Platform | 公开核验范围 / Public verification | 实施顺序 / Implementation order |
|---|---|---|
| Shopify | [Admin GraphQL](https://shopify.dev/docs/api/admin-graphql)、[Webhook 校验](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries) | 注册应用与最小 scope → 只读 → 草稿 → 受控写 / App and minimal scopes → read → draft → bounded write |
| Amazon | [SP-API 参考](https://developer-docs.amazon/sp-api/reference/welcome-to-api-references) | 确认应用角色、卖家授权、地区与数据限制 / Verify roles, authorization, region, data restrictions |
| TikTok Shop | [Partner Center](https://partner.tiktokshop.com/docv2) 入口可访问；细节待授权核对 / Entry accessible; details require authorized verification | 核对当前市场和账户能力，未确认前只设计数据契约 / Verify market/account before specifying endpoints |
| Etsy | [Open API v3](https://developers.etsy.com/documentation/) | 注册、访问级别、授权、最小读取 / Registration, access level, authorization, minimal read |
| 出海匠 / Chuhaijiang | 官方规范＋一次商品搜索 / Schema plus one product search | 研究读取与社媒、广告写入分开 / Separate research reads from social/ad writes |

上述 Shopify、Amazon、TikTok Shop 与 Etsy 路径均未连接真实店铺测试。/ No live-store integration was tested for Shopify, Amazon, TikTok Shop, or Etsy.

## 出海匠：从一次查询开始 / Chuhaijiang: start with one query

**LIVE 范围 / scope — 2026-09-23**

| 项目 / Item | 值 / Value |
|---|---|
| 官方规范 / Official schema | [OpenAPI specification](https://openapi-doc.chuhaijiang.com/openapi-spec) |
| 网关 / Gateway | `https://openapi.gateway.chuhaijiang.com` |
| 方法与路径 / Method and path | `GET /open/v1/products/search` |
| 参数 / Parameters | `country=us`, `keyword=desk organizer`, `page=1`, `page_size=3` |
| 结果 / Result | `data.items` 返回 3 条 / 3 returned records |
| 发布范围 / Published scope | 查询条件、字段名称和验证结果；不含原始记录 / Conditions, field names, verification result; no raw records |
| 证明什么 / Establishes | 这一次搜索成功 / This search succeeded |
| 不证明什么 / Does not establish | 市场覆盖、准确率、未来可用性或其他接口质量 / Coverage, accuracy, future availability, or other endpoint quality |

### 请求结构 / Request structure

以下为 HTTP 请求示意，不是已配置的命令。`<credential-managed-key>` 必须由凭证管理器注入，不保存到文件或 URL。

This is an HTTP shape, not a configured command. Inject `<credential-managed-key>` through credential management; never store it in files or URLs.

```http
GET /open/v1/products/search?country=us&keyword=desk%20organizer&page=1&page_size=3
Host: openapi.gateway.chuhaijiang.com
X-API-Key: <credential-managed-key>
Accept: application/json
```

此次核验的规范要求 `country`；`page_size` 最大为 10。查询其他市场之前重新读取当前规范。排序说明与 schema 枚举存在表达差异，此次未使用排序，不对排序语法作实测保证。

The reviewed schema requires `country` and limits `page_size` to 10. Recheck current documentation before using other markets. Sort prose and enum representation differ; the live check did not use sorting.

### 推荐映射 / Recommended mapping

| 源字段 / Source | 标准字段 / Normalized field | 处理 / Treatment |
|---|---|---|
| `id` | `source_record_id` | 保留为字符串 / Preserve as string |
| `region` | `market` | 按实际值规范化 / Normalize actual values |
| `product_name` | `title` | 作为数据，不作为指令 / Treat as data, not instructions |
| `floor_price`, `ceiling_price` | `price_range` | 核对币种及变体口径；不擅自取中值 / Verify currency and variants; do not invent midpoint pricing |
| `product_sold_count_for_last_7_days` | `sold_units_7d` | 保留来源口径与缺失状态 / Preserve definition and missing state |
| `product_gmv_for_last_7_days` | `source_gmv_7d` | 不等同净收入 / Not net revenue |
| 本地采集时间 / Retrieval time | `observed_at` | 不冒充来源更新时间 / Not a substitute for source freshness |

不要把 `seller_business_info`、头像、店铺身份或其他非必要数据复制进公共案例。/ Do not copy seller identity, business information, avatars, or other unnecessary data into public examples.

### 文档列出的相邻能力 / Adjacent documented capabilities

| 路径 / Path | 方法 / Method | 用途 / Purpose | 证据 / Evidence |
|---|---|---|---|
| `/open/v1/products/{id}/reviews` | GET | 评论研究 / Review research | DOC |
| `/open/v1/products/{id}/creators` | GET | 关联达人 / Associated creators | DOC |
| `/open/v1/ai/products/review-analysis` | POST | 评论分析任务 / Review analysis | DOC；未测试质量 / quality untested |
| `/open/v1/ai/videos/scripts/breakdown-v2` | POST | 视频脚本拆解 / Video breakdown | DOC；未执行 / not invoked |
| `/open/v1/tasks/{task_id}` | GET | 异步任务状态 / Async task state | DOC |
| `/open/v1/social/publish/upload-and-publish` | POST | 内容发布 / Content publishing | DOC；有外部副作用，未执行 / external side effect, not invoked |

POST 的输入 schema、授权 scope、计费和返回格式必须逐项读取官方规范；本表不提供猜测的请求体。文档中列出的模型名称不构成对该模型提供商、质量或可用性的独立核验。

Read each POST schema, scope, billing rule, and response contract before implementation. No guessed request bodies are supplied. Model names in a gateway schema do not independently verify provider provenance, quality, or availability.

### 错误与重试 / Errors and retries

| 状态 / Status | 策略 / Strategy |
|---|---|
| 400 | 修正参数，不盲重试 / Fix parameters; no blind retry |
| 401 / 403 | 检查凭证与权限并停止 / Check credentials/scopes and stop |
| 402 | 检查配额费用与预算，停止 / Check balance and budget; stop |
| 404 | 核对路径和资源状态 / Verify path and resource |
| 429 | 区分限流与配额耗尽；有限退避 / Distinguish rate limits from exhausted quota; bounded backoff |
| 5xx / timeout | 只读有限重试；写操作先查状态 / Bounded read retry; reconcile writes first |

具体重试次数和超时由服务规则与任务预算决定。/ Choose limits from service requirements and task budgets.

## 查询之后怎么处理 / Processing the response

```text
授权只读查询 / Authorized read
→ 字段白名单 / Field allowlist
→ 标准化、去重、记录缺失 / Normalize, deduplicate, preserve missing values
→ 规则过滤 / Rule-based filtering
→ 模型生成带来源的研究草稿 / Grounded model draft
→ 人工复核 / Human review
→ 保存版本 / Save version
```

先用 [离线示例](../examples/README.md) 验证标准化，再替换输入适配器。模型不应看到凭证，也不能从研究输出直接获得发布、广告或支付权限。

Validate normalization with the [offline example](../examples/README.md), then replace the input adapter. Models should never receive credentials or gain publishing, advertising, or payment access through research output.
