<div align="center">

# Awesome AI Ecommerce

### 电商 AI 自动化：从一个动作，到一套系统

**让工具有位置，让事实有来源，让每一次执行都有回声。**

简体中文 · [English](README.en.md)

[阅读万字指南](docs/zh-CN/handbook.md) · [查找工具](docs/tools.md) · [接入 API](docs/integrations.md) · [运行示例](examples/README.md)

</div>

---

面向跨境卖家、独立站、品牌团队和开发者的双语知识入口。覆盖选品、商品事实、Listing、图片与视频、达人、广告、客服、库存、履约和经营分析；同时解释数据契约、Agent、可靠性、评估与尚未验证的边界。

> 自动化的价值，在于把重复交给系统，把判断留给证据。

## 从这里开始

| 你想解决的问题 | 阅读入口 | 可以获得什么 |
|---|---|---|
| 从零理解电商自动化 | [系统指南 01–03](docs/zh-CN/handbook.md#c01) | 任务选择、架构与数据契约 |
| 研究商品与市场 | [研究与供应链 04–06](docs/zh-CN/handbook.md#c04) | 选品、评论、成本与事实库 |
| 制作商品页和内容 | [内容生产 07–09](docs/zh-CN/handbook.md#c07) | 本地化、视觉一致性、短视频 |
| 连接达人与广告 | [获客实验 10–11](docs/zh-CN/handbook.md#c10) | 合作管理、诊断和实验方法 |
| 改善客服与履约 | [经营闭环 12–14](docs/zh-CN/handbook.md#c12) | 检索、订单、库存和复购 |
| 开发可靠的系统 | [工程实施 15–18](docs/zh-CN/handbook.md#c15) | API、Agent、评估与成本 |
| 寻找类似方案 | [24 个场景配方](docs/zh-CN/handbook.md#c20) | 输入、工具组合和验收条件 |
| 探索还没有答案的方向 | [边界与研究路径](docs/zh-CN/handbook.md#c19) | 假设、验证方法和停止条件 |

## 仓库地图

```text
.
├── README.md / README.en.md      双语入口
├── docs/
│   ├── zh-CN/handbook.md         中文系统长文
│   ├── en/handbook.md            对应英文版
│   ├── tools.md                 双语工具选型目录
│   ├── integrations.md          平台与出海匠接入配方
│   └── sources.md               来源、证据等级与验证日期
├── examples/                    合成数据与离线可运行示例
├── ai-ecommerce-news-workflow.json  n8n 手动演示模板
├── tests/                       边界测试
├── scripts/check_repo.py         链接、结构和公开内容检查
├── CONTRIBUTING.md              双语贡献规范
├── SECURITY.md                  数据与安全规则
└── .github/                     自动检查与议题模板
```

## 先理解证据等级

| 标记 | 含义 |
|---|---|
| **LIVE** | 在写明的日期与范围内完成真实接口查询；不代表全面验证 |
| **DOC** | 官方文档确认能力存在；未完成端到端实测 |
| **DEMO** | 合成数据的离线示例；不连接生产店铺 |
| **DESIGN** | 有明确输入、步骤与验收标准的参考设计 |
| **RESEARCH** | 尚未验证的假设，仅给出推理和实现思路 |

工具目录的收录不代表付费推荐，也不代表所有工具都经过本仓库实测。价格、配额、模型版本、地区权限与许可证以官方当前说明为准。[查看来源与验证范围](docs/sources.md)。

## 十分钟理解一个最小闭环

需要 Python 3.10+；以下命令不联网、不发送消息、不操作店铺。

```bash
python3 examples/research_pipeline.py
python3 examples/unit_economics.py
python3 -m unittest discover -s tests -v
python3 scripts/check_repo.py
```

第一个示例完成商品记录的字段规范化与重复记录检查；第二个示例计算合成订单的贡献利润。它们演示可校验的基础步骤，接入模型与平台的方法见[示例说明](examples/README.md)。

[n8n JSON](ai-ecommerce-news-workflow.json) 为手动触发、合成新闻输入、去重并生成待审简报的最小模板。**已做 JSON、连线与代码逻辑检查，尚未在 n8n 实例中导入验证。**接入 RSS、模型和发送渠道前，请阅读[配置说明](examples/README.md#n8n)。

## 设计原则

- **事实先于表达。** 商品声明、价格与政策必须有依据。
- **闭环先于规模。** 先观察一次执行的真实结果，再扩展数量。
- **规则约束模型。** 计算、权限与资金边界由确定性机制执行。
- **未知保持可见。** 不用流畅叙述填补缺失证据。
- **人的介入也是设计。** 保留审核、异常接手和停止机制。

## 参与与维护

欢迎补充可复现的场景、工具适用边界、来源与失败案例。请先阅读[贡献规范](CONTRIBUTING.md)与[安全规则](SECURITY.md)。中文与英文主指南保持章节对应；工具、接入和维护文档采用双语呈现。

本版本资料核验日期：**2026-09-23**。已有代码与文档沿用仓库 [MIT 许可证](LICENSE)；第三方工具、模型、数据和素材保留各自条款。
