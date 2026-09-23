<div align="center">

# Awesome AI Ecommerce

### 电商 AI 工具与自动化指南

简体中文 · [English](README.en.md)

[阅读全文](docs/zh-CN/handbook.md) · [查找工具](docs/tools.md) · [接入 API](docs/integrations.md) · [运行示例](examples/README.md)

</div>

---

做电商时，哪些工作适合交给 AI，选什么工具，怎么把它接进现有流程？这个仓库围绕这些问题整理资料和做法。

从选品、商品页、图片视频，到达人、广告、客服和履约，都有对应章节。每个场景尽量说清需要什么数据、可以怎么做，以及哪里还需要人工处理。想直接找方案，可以从下表进入；想自己开发，建议先读数据格式、接口和错误处理。

## 从这里开始

| 你想解决的问题 | 阅读入口 | 可以获得什么 |
|---|---|---|
| 从零理解电商自动化 | [系统指南 01–03](docs/zh-CN/handbook.md#c01) | 任务选择、架构与数据契约 |
| 研究商品与市场 | [研究与供应链 04–06](docs/zh-CN/handbook.md#c04) | 选品、评论、成本与事实库 |
| 制作商品页和内容 | [内容生产 07–09](docs/zh-CN/handbook.md#c07) | 本地化、视觉一致性、短视频 |
| 连接达人与广告 | [获客实验 10–11](docs/zh-CN/handbook.md#c10) | 合作管理、诊断和实验方法 |
| 改善客服与履约 | [客服与履约 12–14](docs/zh-CN/handbook.md#c12) | 检索、订单、库存和复购 |
| 开发可靠的系统 | [工程实施 15–18](docs/zh-CN/handbook.md#c15) | API、Agent、评估与成本 |
| 寻找类似方案 | [24 个场景方案](docs/zh-CN/handbook.md#c20) | 输入、工具组合和验收条件 |
| 探索还没有答案的方向 | [边界与研究路径](docs/zh-CN/handbook.md#c19) | 假设、验证方法和停止条件 |

## 文件目录

```text
.
├── README.md / README.en.md      双语入口
├── docs/
│   ├── zh-CN/handbook.md         中文完整指南
│   ├── en/handbook.md            对应英文版
│   ├── tools.md                 双语工具选型目录
│   ├── integrations.md          平台与出海匠接入说明
│   └── sources.md               来源、证据等级与验证日期
├── examples/                    合成数据与离线可运行示例
├── ai-ecommerce-news-workflow.json  n8n 手动演示模板
├── tests/                       边界测试
├── scripts/check_repo.py         链接、结构和公开内容检查
├── CONTRIBUTING.md              双语贡献规范
├── SECURITY.md                  数据与安全规则
└── .github/                     自动检查与议题模板
```

## 文档里的状态标记

| 标记 | 含义 |
|---|---|
| **LIVE** | 在写明的日期与范围内完成真实接口查询；不代表全面验证 |
| **DOC** | 官方文档确认能力存在；未完成端到端实测 |
| **DEMO** | 合成数据的离线示例；不连接生产店铺 |
| **DESIGN** | 有明确输入、步骤与验收标准的参考设计 |
| **RESEARCH** | 尚未验证的假设，仅给出推理和实现思路 |

工具目录的收录不代表付费推荐，也不代表所有工具都经过本仓库实测。价格、配额、模型版本、地区权限与许可证以官方当前说明为准。[查看来源与验证范围](docs/sources.md)。

## 先运行两个小示例

需要 Python 3.10+；以下命令不联网、不发送消息、不操作店铺。

```bash
python3 examples/research_pipeline.py
python3 examples/unit_economics.py
python3 -m unittest discover -s tests -v
python3 scripts/check_repo.py
```

第一个示例完成商品记录的字段规范化与重复记录检查；第二个示例计算合成订单的贡献利润。它们演示可校验的基础步骤，接入模型与平台的方法见[示例说明](examples/README.md)。

[n8n JSON](ai-ecommerce-news-workflow.json) 为手动触发、合成新闻输入、去重并生成待审简报的最小模板。**已做 JSON、连线与代码逻辑检查，尚未在 n8n 实例中导入验证。**接入 RSS、模型和发送渠道前，请阅读[配置说明](examples/README.md#n8n)。

## 使用这些方案时

建议先选一个商品或一项日常工作试用，记录处理时间、错误和修改量。金额计算交给程序，文案和分类交给模型；商品参数、发布内容和退款等事项保留相应核对步骤。

仓库里既有示例，也有尚未实现的方案，状态已分别标注。接口接通以后，还要检查实际结果：商品是否改对、消息是否发出、失败的任务能否接着处理。

## 参与与维护

欢迎补充可复现的场景、工具适用边界、来源与失败案例。请先阅读[贡献规范](CONTRIBUTING.md)与[安全规则](SECURITY.md)。中文与英文主指南保持章节对应；工具、接入和维护文档采用双语呈现。

本版本资料核验日期：**2026-09-23**。已有代码与文档沿用仓库 [MIT 许可证](LICENSE)；第三方工具、模型、数据和素材保留各自条款。
