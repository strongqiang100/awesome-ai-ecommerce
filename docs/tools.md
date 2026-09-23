# 工具选型目录 · Tool Selection Catalog

[中文入口](../README.md) · [English home](../README.en.md) · [来源 / Sources](sources.md)

下面按用途整理工具，链接指向官方资料。**DOC** 表示查过文档，不代表已经在店铺里用过；表里的组合建议标为 **DESIGN**。选好工具后，还需确认自己的账号、地区和版本是否支持所需功能，以及费用、配额和许可是否合适。

Tools are grouped by task and linked to official material. **DOC** means the documentation was checked, not that the tool was tested in a store. Proposed combinations are **DESIGN**. Before adopting one, check whether your account, region, and version support the features you need, along with fees, quotas, and licensing.

## 01 · 编排与 Agent / Orchestration and agents

| 工具 / Tool | 适合解决 / Suitable work | 采用前判断 / Adoption check | 证据 / Evidence |
|---|---|---|---|
| [n8n](https://docs.n8n.io/) | 连接数据与业务步骤 / Connecting APIs and business steps | 自托管需维护；fair-code，不等同无限制开源 / Hosting requires operations; fair-code is not unrestricted open source | DOC |
| [Dify](https://docs.dify.ai/en/home) | 知识问答与模型工作流 / Knowledge applications and model workflows | 测试检索、权限、部署与许可 / Evaluate retrieval, access, deployment, license | DOC |
| [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) | 有状态 Agent / Stateful agent workflows | 适合具备工程维护能力的团队 / Requires engineering ownership | DOC |
| [Temporal](https://docs.temporal.io/) | 长时间业务流程 / Durable business processes | 不替代业务幂等与外部状态核对 / Business idempotency and reconciliation still required | DOC |
| [OpenClaw](https://docs.openclaw.ai/) | 消息渠道连接 Agent / Messaging gateway for agents | 非专用电商爬虫；工具权限单独配置 / Not a commerce crawler; configure tool access separately | DOC |

## 02 · 数据与浏览器 / Data and browsers

| 工具 / Tool | 适合解决 / Suitable work | 采用前判断 / Adoption check | 证据 / Evidence |
|---|---|---|---|
| [出海匠 / Chuhaijiang](https://openapi-doc.chuhaijiang.com/openapi-spec) | 商品、内容与相关数据接入 / Product and content data | 查询市场与字段口径；写操作权限分离 / Validate market and metrics; separate writes | DOC；商品搜索一例 LIVE / one product-search LIVE check |
| [Firecrawl](https://docs.firecrawl.dev/introduction) | 将网页变成模型可读资料 / Web content for model workflows | 核对访问权、解析完整性与新鲜度 / Check access, completeness, freshness | DOC |
| [Playwright](https://playwright.dev/docs/intro) | 确定性的浏览器操作与测试 / Browser control and testing | 页面变化和登录状态需维护 / Maintain selectors and sessions | DOC |
| [Browser Use](https://docs.browser-use.com/cloud/quickstart) | 浏览器 Agent 与基础设施 / Browser agents and infrastructure | 云端与本地方案不同；限制任务权限 / Cloud and local differ; bound permissions | DOC |
| [Airbyte](https://docs.airbyte.com/) | 数据同步 / Data replication | 逐个确认连接器与增量行为 / Verify each connector and incremental behavior | DOC |

## 03 · 模型、媒体与知识 / Models, media, and knowledge

| 工具 / Tool | 适合解决 / Suitable work | 采用前判断 / Adoption check | 证据 / Evidence |
|---|---|---|---|
| [LiteLLM](https://docs.litellm.ai/) | 模型接口路由与费用控制 / Model routing and spend controls | 统一接口不保证模型输出一致 / A common API does not equal identical behavior | DOC |
| [Ollama](https://ollama.com/) | 本地模型试验 / Local model experiments | 硬件、模型许可和数据出站行为分别检查 / Check hardware, model terms, and data egress | DOC |
| [ComfyUI](https://docs.comfy.org/) | 节点式视觉生成 / Node-based visual workflows | 节点、权重和素材许可各不相同 / Nodes, weights, and assets have separate terms | DOC |
| [FFmpeg](https://ffmpeg.org/documentation.html) | 拼接、转码、音视频处理 / Assembly, transcoding, media processing | 构建选项与编码器许可需核对 / Check build and codec licensing | DOC |
| [Qdrant](https://qdrant.tech/documentation/) | 向量检索 / Vector retrieval | 权限、版本与租户过滤由系统设计保证 / Design authorization and tenant/version filtering | DOC |

选模型时，可以拿同一批商品资料和问题分别试一下，记录事实错误、格式错误、延迟和人工修改时间。演示里最好的一次结果未必有代表性，多跑几次再比较。实际采用的模型名称与版本记在配置里，后续换版本时用原样本复测。

Try models on the same product information and questions. Record factual and formatting errors, delay, and editing time. Repeat the trial rather than choosing from a single best output. Save the adopted model and version in configuration, and reuse the samples when upgrading.

## 04 · 平台、服务与分析 / Platforms, service, and analytics

| 工具 / Tool | 适合解决 / Suitable work | 采用前判断 / Adoption check | 证据 / Evidence |
|---|---|---|---|
| [Shopify GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql) | 获授权的店铺管理 / Authorized store operations | API 版本、scope 与字段限制 / API version, scopes, and field constraints | DOC |
| [Amazon SP-API](https://developer-docs.amazon/sp-api/reference/welcome-to-api-references) | 卖家数据与运营接口 / Selling-partner operations | 注册角色、地区、敏感数据权限 / Roles, regions, restricted data | DOC |
| [TikTok Shop Partner Center](https://partner.tiktokshop.com/docv2) | 平台接入入口 / Partner integration entry | 本次公开页未提供完整接口细节；需登录核验 / Public page did not expose full detail; verify in portal | 待核 / VERIFY |
| [Etsy Open API v3](https://developers.etsy.com/documentation/) | Etsy 应用接入 / Etsy application integration | 访问级别与账户授权 / Access level and authorization | DOC |
| [Google Ads API](https://developers.google.com/google-ads/api/docs/get-started/introduction) | 广告数据与管理 / Advertising integration | 权限和开发者配置；先只读 / Permissions and developer setup; read first | DOC |
| [Gorgias](https://developers.gorgias.com/) | 客服系统集成 / Support integrations | 测试工单状态、权限和升级流程 / Verify ticket state, access, escalation | DOC |
| [Klaviyo](https://developers.klaviyo.com/en/reference/api_overview) | 事件与营销集成 / Events and marketing integration | 授权、退订与发送限制 / Permission, suppression, sending limits | DOC |
| [dbt](https://docs.getdbt.com/docs/introduction) | 数据转换与指标建模 / Transformation and analytics models | 口径由业务定义，工具不会自动纠错 / Business definitions remain necessary | DOC |
| [Metabase](https://www.metabase.com/docs/latest/) | 经营查询与仪表盘 / Queries and dashboards | 数据权限、刷新与查询成本 / Data access, refresh, query cost | DOC |

## 05 · 可以从哪些组合开始 / Starting combinations

| 场景 / Context | 最小组合 / Minimal stack | 暂不增加 / Defer until justified |
|---|---|---|
| 小团队验证 / Small team pilot | 表格＋一个编排器＋一个模型＋人工复核 / Table, one orchestrator, one model, review | 多 Agent 与复杂基础设施 / Multiple agents and complex infrastructure |
| 多店铺运营 / Multiple stores | 平台 API＋数据库＋队列＋明确租户隔离 / APIs, database, queue, tenant isolation | 跨店铺自动共享敏感数据 / Automatic sensitive-data sharing |
| 内容生产团队 / Content team | 事实库＋资产库＋生成与剪辑＋版本评估 / Facts, assets, generation/editing, evaluation | 未验证的无人发布 / Unvalidated unattended publishing |

## 06 · 其他平台 / Other platforms

WooCommerce、eBay、Shopee、Lazada、Walmart、Mercado Libre、Temu、SHEIN 等平台可以沿用数据契约与审批思路，但本版本没有完成逐平台接口、账号和地区验证。未为它们编造 endpoint 或连接器。后续贡献应先补官方来源、实际权限和最小读请求，再提交可复现适配。

The same design principles may transfer to WooCommerce, eBay, Shopee, Lazada, Walmart, Mercado Libre, Temu, and SHEIN. This edition has not completed platform-specific account, regional, and endpoint verification. It invents no endpoints or connectors. Contributions should establish official sources, permissions, and a minimal read request first.
