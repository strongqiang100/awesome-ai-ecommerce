# 来源与证据 · Sources and Evidence

[中文入口](../README.md) · [English home](../README.en.md)

核验日期 / Reviewed: **2026-09-23**。访问日期不是页面发布日期。官方页面确认产品定位与接口说明，不证明商业效果。正文中的系统组合、评估方法与场景配方属于参考设计。

The review date is not a publication date. Official pages establish documented roles and interfaces, not commercial effectiveness. Architectures, evaluation methods, and recipes in the handbook are reference designs.

## 证据登记 / Evidence register

| ID | 一手来源 / Primary source | 支持范围 / Supported scope | 状态 / Status |
|---|---|---|---|
| S01 | [n8n documentation](https://docs.n8n.io/) | 编排工具定位 / Workflow orchestration | DOC |
| S02 | [n8n license](https://github.com/n8n-io/n8n/blob/master/LICENSE.md) | Sustainable Use 与其他部分许可区分 / Licensing distinctions | DOC |
| S03 | [Dify documentation](https://docs.dify.ai/en/home) | 模型与知识应用 / Model and knowledge applications | DOC |
| S04 | [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | 有状态 Agent 编排 / Stateful orchestration | DOC |
| S05 | [Temporal documentation](https://docs.temporal.io/) | 业务流程运行基础 / Workflow runtime | DOC |
| S06 | [OpenClaw documentation](https://docs.openclaw.ai/) | 网关与渠道定位 / Gateway and channels | DOC |
| S07 | [Firecrawl documentation](https://docs.firecrawl.dev/introduction) | 网页内容处理 / Web content processing | DOC |
| S08 | [Playwright documentation](https://playwright.dev/docs/intro) | 浏览器操作与测试 / Browser automation and tests | DOC |
| S09 | [Browser Use quickstart](https://docs.browser-use.com/cloud/quickstart) | Agent 与浏览器基础设施 / Agents and browser infrastructure | DOC |
| S10 | [LiteLLM documentation](https://docs.litellm.ai/) | 模型路由与费用管理 / Routing and spend controls | DOC |
| S11 | [Ollama](https://ollama.com/) | 本地模型入口 / Local model tooling | DOC |
| S12 | [ComfyUI documentation](https://docs.comfy.org/) | 视觉工作流 / Visual workflows | DOC |
| S13 | [FFmpeg documentation](https://ffmpeg.org/documentation.html) | 媒体处理 / Media processing | DOC |
| S14 | [Qdrant documentation](https://qdrant.tech/documentation/) | 向量检索 / Vector retrieval | DOC |
| S15 | [Shopify Admin GraphQL](https://shopify.dev/docs/api/admin-graphql) | 店铺应用接口 / Store application API | DOC |
| S16 | [Shopify delivery verification](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries) | 签名与重复投递 / Signatures and duplicate delivery | DOC |
| S17 | [Amazon SP-API reference](https://developer-docs.amazon/sp-api/reference/welcome-to-api-references) | 卖家接口目录 / Selling-partner interfaces | DOC |
| S18 | [TikTok Shop Partner Center](https://partner.tiktokshop.com/docv2) | 文档入口；公开页信息有限 / Entry only; limited public detail | 待授权核验 / VERIFY |
| S19 | [Etsy Open API v3](https://developers.etsy.com/documentation/) | Etsy 应用开发 / Etsy development | DOC |
| S20 | [Google Ads API](https://developers.google.com/google-ads/api/docs/get-started/introduction) | 广告接口入口 / Advertising API | DOC |
| S21 | [Gorgias developer portal](https://developers.gorgias.com/) | 客服集成入口 / Support integration | DOC |
| S22 | [Klaviyo API](https://developers.klaviyo.com/en/reference/api_overview) | 事件和营销接口 / Events and marketing API | DOC |
| S23 | [Airbyte documentation](https://docs.airbyte.com/) | 数据同步入口；连接器需单独验证 / Replication; connectors require separate checks | DOC |
| S24 | [dbt introduction](https://docs.getdbt.com/docs/introduction) | 数据转换 / Data transformation | DOC |
| S25 | [Metabase documentation](https://www.metabase.com/docs/latest/) | 分析与仪表盘 / Analytics and dashboards | DOC |
| S26 | [出海匠 OpenAPI](https://openapi-doc.chuhaijiang.com/openapi-spec) | 实际取得 JSON 规范；路径与字段 / Retrieved JSON schema, paths and fields | DOC＋[限定 LIVE 查询](integrations.md) |

S26 通过直接 HTTPS 请求取得；网页阅读工具未能解析该地址。只读样本查询成功与规范读取分开登记，不对全部接口作保证。/ S26 was retrieved directly over HTTPS when the web reader could not parse it. Schema retrieval and the scoped live query are distinct evidence; neither validates every endpoint.

## 本地方法资料的使用边界 / Treatment of local knowledge

本指南吸收了四类方法：业务动作结构化、选品约束与成本检查、按镜头组织内容、从研究到发布再回看结果。公开版本仅保留经重新组织的通用方法，不包含私人文件名、路径、会议链接、人员信息、客户记录或原始案例。

The guide incorporates general methods for structuring business actions, checking product constraints and costs, organizing content by shot, and observing results after publishing. The public edition contains no private filenames, paths, meeting links, personal details, customer records, or raw cases.

历史材料中的价格、成功比例、未核实模型名称和特定地区权限未作为当前事实采用。不能独立验证的方法以 DESIGN 呈现，不作为商业效果证据。

Historical prices, success rates, unverified model names, and region-specific access statements were not promoted to current facts. Methods without independent validation remain DESIGN, not evidence of commercial results.

## 验证范围 / Validation scope

- **LIVE：**一次出海匠商品搜索，返回 3 条，查询条件见接入文档。/ One product search, three records; conditions in the integration guide.
- **DEMO：**Python 示例与边界测试，n8n Code 节点离线行为。/ Python examples and boundary tests, offline n8n Code-node behavior.
- **STATIC：**JSON、内部链接、章节对应与公开内容模式检查。/ JSON, internal links, chapter parity, and publication-pattern checks.
- **未完成 / Not performed：**真实店铺联调、n8n 实例导入、模型质量评测、自动发布、广告执行、支付、真实客户联系。/ Live-store integration, n8n import, model benchmarking, publishing, ad execution, payment, and customer outreach.

自动扫描无法证明所有个人信息或所有错误都已排除，仍需人工审核。现有 Git 历史及平台账户元数据不属于新文档内容，更新正文不等于删除历史。

Automated scanning cannot prove the absence of all personal information or errors; human review remains necessary. Existing Git history and platform account metadata are separate from new document content. Updating files does not erase history.

## 维护规则 / Maintenance rules

采用前重新检查易变信息；接口变化后更新适配与测试；来源失效时降低证据等级。新增工具先提供官方来源、适用场景、限制与验证日期，不以宣传口号替代说明。

Recheck volatile details before adoption, update adapters and tests when interfaces change, and downgrade evidence when sources fail. New tools need official sources, applicable work, limitations, and review dates rather than promotional claims.
