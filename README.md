<div align="center">

# 🔧 AI Ecommerce Automation Toolkit

**Cross-border Ecommerce AI Automation — Practical Notes & Workflow Templates**
**跨境电商 AI 自动化实践笔记：n8n 工作流 / OpenClaw 配置 / 选品数据处理**

[查看文档](#-学习资源与文档) | [贡献内容](CONTRIBUTING.md) | [问题反馈](issues)

---

</div>

## 📖 目录 (Table of Contents)

- [🤖 自动化核心工具 (Core Tools)](#-自动化核心工具)
- [⚡️ 实战工作流模板 (Workflow Templates)](#-实战工作流模板)
- [🦞 OpenClaw 实战配置](#-openclaw-实战配置)
- [🧠 推荐 AI 模型与 Agent](#-推荐-ai-模型与-agent)
- [📚 学习资源与文档](#-学习资源与文档)
- [💬 交流与反馈](#-交流与反馈)

---

## 🤖 自动化核心工具

> 以下工具均经过实际业务场景验证，适用于跨境电商数据处理与流程自动化。

| 工具名称 | 类型 | 说明 | 链接 |
| :--- | :--- | :--- | :--- |
| **n8n** | 流程自动化 | 开源工作流引擎，支持私有化部署，节点生态丰富。 | [官网](https://n8n.io/) |
| **OpenClaw** | 爬虫 Agent | 适用于电商数据与素材抓取的 AI Agent 框架。 | [GitHub](https://github.com/openclaw) |
| **Firecrawl** | 网页解析 | 将任意网页转换为结构化 Markdown，适合喂给 LLM。 | [官网](https://firecrawl.dev/) |
| **Brave Search** | 搜索 API | 支持 AI 联网检索，延迟低，适合 Agent 集成。 | [官网](https://brave.com/search/api/) |

---

## ⚡️ 实战工作流模板

> 以下是在实际场景中验证可用的 n8n JSON 模板，导入即可使用。
> 每个模板附有依赖说明，请根据自身环境调整配置参数。

### 1. 跨境行业资讯自动聚合流

- **适用场景：** 自动采集多源行业资讯，AI 摘要后推送至团队协作工具
- **数据来源：** 36Kr、虎嗅、Reddit 相关板块（可自定义扩展）
- **处理节点：** HTTP Request → DeepSeek/OpenAI 摘要 → 飞书 / 企业微信推送
- **依赖节点：** `HTTP Request` `OpenAI (兼容 DeepSeek)` `Feishu/Wecom`
- **模板文件：** [下载 JSON]({
  "name": "强哥AI电商 · 信息整理工作流 · 公开分享版",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 8
            }
          ]
        }
      },
      "id": "node-schedule-trigger",
      "name": "每天早上8点触发",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.2,
      "position": [-224, 208],
      "notes": "⏰【定时触发器】每天早上8点自动运行整个工作流。\n如需修改时间，点击节点 → 修改 triggerAtHour 的数字（0-23）。\n比如改成9就是早上9点触发。"
    },
    {
      "parameters": {
        "url": "https://36kr.com/feed",
        "options": {}
      },
      "id": "node-36kr-rss",
      "name": "36氪出海RSS",
      "type": "n8n-nodes-base.rssFeedRead",
      "typeVersion": 1,
      "position": [16, -48],
      "notes": "📰【RSS订阅】自动抓取36氪出海频道的最新文章。\n无需任何配置，直接可用。\n如需换成其他RSS源，修改url字段即可。"
    },
    {
      "parameters": {
        "url": "https://www.youtube.com/feeds/videos.xml?channel_id=UCKHhA5hN2UohhFDfNXB_cvQ",
        "options": {}
      },
      "id": "node-youtube-rss",
      "name": "YouTube-Jungle Scout",
      "type": "n8n-nodes-base.rssFeedRead",
      "typeVersion": 1,
      "position": [112, 480],
      "notes": "▶️【YouTube RSS】订阅Jungle Scout频道的最新视频。\n无需API Key，直接读取YouTube公开RSS。\n如需换频道：把 channel_id= 后面的字符串换成目标频道ID。\n频道ID获取方法：打开YouTube频道页 → 地址栏最后一串字母就是ID。"
    },
    {
      "parameters": {
        "url": "https://www.reddit.com/r/FulfillmentByAmazon/.rss",
        "options": {}
      },
      "id": "node-reddit-rss",
      "name": "Reddit FBA社区",
      "type": "n8n-nodes-base.rssFeedRead",
      "typeVersion": 1,
      "position": [896, 672],
      "notes": "🤖【Reddit RSS】抓取Reddit FBA卖家社区的热门帖子。\n无需账号，直接可用。\n如需换板块：把 r/FulfillmentByAmazon 换成其他subreddit名称。"
    },
    {
      "parameters": {
        "mode": "combine",
        "combinationMode": "mergeByPosition",
        "options": {}
      },
      "id": "node-merge",
      "name": "合并所有资讯",
      "type": "n8n-nodes-base.merge",
      "typeVersion": 2.1,
      "position": [448, 304],
      "notes": "🔀【合并节点】把来自多个渠道的资讯合并成一个数据流。\n无需配置，自动处理。\n如果新增了新的资讯源，记得把新节点连接到这里。"
    },
    {
      "parameters": {
        "jsCode": "// ============================================================\n// 强哥AI电商 · 信息整理工作流 · 公开分享版\n// 欢迎关注强哥：\n//   抖音号：强哥的世界（抖音ID: 611083659）\n//   微信公众号：AI电商新基建\n// 业务交流 / 工作流定制，欢迎私信联系\n// ============================================================\n\n// 【这段代码的作用】\n// 把多个渠道抓来的文章，整理拼接成一段文字\n// 方便后面发给AI做分析，不需要修改任何内容\n\nconst items = $input.all();\nlet combinedText = \"\";\n\nfor (const item of items) {\n    const i = item.json;\n    const title = i.title || i.snippet?.title || '无标题';\n    const link = i.link || (i.id?.videoId ? `https://youtube.com/watch?v=${i.id.videoId}` : '无链接');\n    const summary = i.summary || i.snippet?.description || i.content || i.selftext || '';\n\n    if (title !== '无标题') {\n        combinedText += `【标题】${title}\\n【链接】${link}\\n【摘要】${summary}\\n\\n----------------\\n\\n`;\n    }\n}\n\n// 只输出1条合并结果，确保后续AI节点只处理一次\nreturn [{\n    json: {\n        prompt: combinedText\n    }\n}];"
      },
      "id": "node-code-format",
      "name": "整理文章数据",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [672, 304],
      "notes": "🛠️【代码节点】把多篇文章整理拼接成AI可读格式。\n无需修改，直接可用。"
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer 【在这里填入你的OpenRouter API Key】"
            },
            {
              "name": "HTTP-Referer",
              "value": "https://n8n.io"
            }
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"model\": \"openai/gpt-4o-mini\",\n  \"messages\": [\n    {\n      \"role\": \"system\",\n      \"content\": \"你是AI电商新基建的首席情报分析师。受众是跨境电商老板、DTC品牌操盘手和投资人。核心关注：AI真实ROI、净利润影响、爆款选品逻辑、供应链承载力。拒绝泛科普，只要硬核干货。\"\n    },\n    {\n      \"role\": \"user\",\n      \"content\": {{ JSON.stringify($json.prompt) }}\n    }\n  ],\n  \"max_tokens\": 2000\n}",
        "options": {}
      },
      "id": "node-openrouter-ai",
      "name": "AI分析筛选情报",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [896, 304],
      "notes": "🤖【AI分析节点 · 需要配置】\n\n📌 第一步：注册OpenRouter账号\n   → 打开 https://openrouter.ai 注册账号\n   → 点击右上角头像 → API Keys → Create Key\n   → 复制生成的Key（格式是 sk-or-v1-xxxx）\n\n📌 第二步：填入API Key\n   → 把上方 value 字段里的占位符\n   → 替换成你自己的Key\n   → 格式保持：Bearer sk-or-v1-你的key\n\n📌 第三步（可选）：修改AI提示词\n   → system content 是AI的角色设定，可按需修改\n   → model 可换成其他模型，如 anthropic/claude-3-haiku\n\n⚠️ 安全提示：API Key相当于你账户的密码\n   不要把含真实Key的工作流分享给任何人！"
    },
    {
      "parameters": {
        "jsCode": "// 【这段代码的作用】\n// 从AI返回的结果里，提取出分析文本\n// 不需要修改任何内容\nconst response = $input.first().json;\nconst content = response.choices[0].message.content;\nreturn [{ json: { analysis: content } }];"
      },
      "id": "node-code-extract",
      "name": "提取AI分析结果",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [1120, 304],
      "notes": "📤【提取结果】从AI返回的数据中提取分析文本。\n无需修改，直接可用。"
    },
    {
      "parameters": {
        "chatId": "【在这里填入你的Telegram Chat ID】",
        "text": "=🌅 AI电商新基建 · 今日情报简报\n\n{{ $json.analysis }}\n\n---\n⏰ 生成时间：{{ new Date().toLocaleString('zh-CN', {timeZone: 'Asia/Shanghai'}) }}",
        "additionalFields": {
          "parse_mode": "Markdown"
        }
      },
      "id": "node-telegram-send",
      "name": "发送到Telegram",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [1328, 304],
      "notes": "📱【Telegram发送节点 · 需要配置两项】\n\n━━━━━━━━━━━━━━━━━━\n【第一项：创建Bot并获取Token】\n━━━━━━━━━━━━━━━━━━\n① 打开Telegram，搜索 @BotFather\n② 发送 /newbot 按提示创建机器人\n③ 创建成功后BotFather会给你一串Token\n   格式：123456789:ABCdefGHI-xxxxxxxxxxxx\n④ 回到n8n → 点击此节点 → Credentials\n   → 新建 Telegram API\n   → 把Token粘贴进去保存\n\n━━━━━━━━━━━━━━━━━━\n【第二项：获取Chat ID】\n━━━━━━━━━━━━━━━━━━\n① 把你刚创建的Bot添加到目标群组\n   或者直接给Bot发一条消息\n② 浏览器打开：\n   https://api.telegram.org/bot【你的Token】/getUpdates\n③ 在返回的JSON里找 \"chat\":{\"id\": 这串数字}\n   个人对话的ID是正数，群组ID是负数\n④ 把这串数字填入上方 chatId 字段\n\n⚠️ 注意：Bot必须先收到过消息才能获取到Chat ID"
    },
    {
      "parameters": {
        "url": "https://www.huxiu.com/rss/0.xml",
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.4,
      "position": [112, 128],
      "id": "node-huxiu-rss",
      "name": "虎嗅RSS抓取",
      "notes": "📰【虎嗅网RSS】抓取虎嗅网最新科技商业资讯。\n无需配置，直接可用。\n虎嗅网没有标准RSS节点，用HTTP请求抓取XML格式内容。"
    },
    {
      "parameters": {
        "url": "https://www.googleapis.com/youtube/v3/search?part=snippet&q=cross+border+ecommerce+AI&type=video&order=date&maxResults=10&key=【在这里填入你的YouTube-API-Key】",
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.4,
      "position": [0, 304],
      "id": "node-youtube-search",
      "name": "YouTube跨境电商搜索",
      "notes": "🔍【YouTube搜索 · 需要配置】\n\n📌 获取YouTube API Key步骤：\n① 打开 https://console.cloud.google.com\n② 登录Google账号 → 新建项目\n③ 左侧菜单 → API和服务 → 启用API\n   搜索 YouTube Data API v3 → 启用\n④ 左侧菜单 → 凭据 → 创建凭据 → API密钥\n⑤ 复制API密钥，替换URL末尾 key= 后面的占位符\n\n📌 修改搜索关键词：\n把URL中 q= 后面的内容换成你想搜索的关键词\n多个词用+连接，如：amazon+FBA+2024\n\n⚠️ 免费额度：每天10,000次查询，日常使用完全够用"
    },
    {
      "parameters": {
        "url": "https://www.reddit.com/r/FulfillmentByAmazon/.rss",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.4,
      "position": [0, 624],
      "id": "node-reddit-http",
      "name": "Reddit HTTP备用抓取",
      "notes": "🔄【Reddit备用抓取】\n用HTTP方式抓取Reddit RSS，加了浏览器User-Agent避免被拦截。\n这是Reddit FBA节点的备用方案，两个选其一即可。\n无需修改，直接可用。"
    }
  ],
  "pinData": {},
  "connections": {
    "每天早上8点触发": {
      "main": [[
        {"node": "36氪出海RSS", "type": "main", "index": 0},
        {"node": "YouTube-Jungle Scout", "type": "main", "index": 0},
        {"node": "虎嗅RSS抓取", "type": "main", "index": 0},
        {"node": "合并所有资讯", "type": "main", "index": 1},
        {"node": "YouTube跨境电商搜索", "type": "main", "index": 0},
        {"node": "Reddit HTTP备用抓取", "type": "main", "index": 0}
      ]]
    },
    "36氪出海RSS": {
      "main": [[{"node": "合并所有资讯", "type": "main", "index": 1}]]
    },
    "合并所有资讯": {
      "main": [[{"node": "整理文章数据", "type": "main", "index": 0}]]
    },
    "整理文章数据": {
      "main": [[{"node": "AI分析筛选情报", "type": "main", "index": 0}]]
    },
    "AI分析筛选情报": {
      "main": [[{"node": "提取AI分析结果", "type": "main", "index": 0}]]
    },
    "提取AI分析结果": {
      "main": [[{"node": "发送到Telegram", "type": "main", "index": 0}]]
    },
    "虎嗅RSS抓取": {
      "main": [[{"node": "合并所有资讯", "type": "main", "index": 1}]]
    },
    "YouTube-Jungle Scout": {
      "main": [[{"node": "合并所有资讯", "type": "main", "index": 1}]]
    },
    "YouTube跨境电商搜索": {
      "main": [[{"node": "合并所有资讯", "type": "main", "index": 1}]]
    },
    "Reddit HTTP备用抓取": {
      "main": [[{"node": "合并所有资讯", "type": "main", "index": 1}]]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "meta": {
    "templateCredsSetupCompleted": false,
    "description": "============================================================\n强哥AI电商 · 信息整理工作流 · 公开分享版\n\n【模板说明】\n本工作流每天定时抓取跨境电商相关资讯（36氪出海、虎嗅、\nYouTube、Reddit等），经AI筛选分析后推送到Telegram。\n\n【使用前必须配置以下3项】\n1. OpenRouter API Key（AI分析节点）\n2. YouTube Data API Key（YouTube搜索节点）\n3. Telegram Bot Token + Chat ID（发送节点）\n\n【各节点均有详细使用说明，小白友好，按提示操作即可】\n\n============================================================\n欢迎关注强哥：\n  📱 抖音：强哥的世界（抖音ID: 611083659）\n  📖 微信公众号：AI电商新基建\n  💼 工作流定制 / 跨境AI落地方案，欢迎私信交流\n============================================================"
  },
  "tags": [
    {"name": "强哥AI电商"},
    {"name": "跨境电商"},
    {"name": "信息聚合"},
    {"name": "公开模板"}
  ]
})

---

### 2. 竞品价格监控流

- **适用场景：** 定时监控指定 ASIN 或关键词的竞品价格变动，触发提醒
- **状态：** 🚧 持续迭代中，近期发布

---

## 🦞 OpenClaw 实战配置

> 记录本地部署过程中遇到的配置问题与解决方案，减少重复踩坑。

### 部署参考

- [本地部署完整文档（飞书）](https://飞书文档链接)
- 推荐使用 `docker-compose` 方式部署，便于环境隔离与版本管理

### 常见报错处理

| 报错信息 | 原因 | 解决方案 |
| :--- | :--- | :--- |
| `Error 403` | 目标站点反爬 | 配置住宅代理或指纹浏览器 |
| `Ollama 连接失败` | Docker 网络隔离问题 | 将 Host 改为 `host.docker.internal` |

---

## 🧠 推荐 AI 模型与 Agent

> 根据不同任务场景的实测对比，持续更新。

| 模型 / 工具 | 适用场景 | 备注 |
| :--- | :--- | :--- |
| **DeepSeek-V3** | 文本摘要、内容生成 | 性价比高，中文理解强 |
| **Claude 3.5 Sonnet** | 长文档处理、复杂推理 | 上下文窗口大 |
| **Midjourney / Flux** | 电商主图生成 | 需结合提示词模板使用 |

---

## 📚 学习资源与文档

- [n8n 官方文档](https://docs.n8n.io/)
- [OpenClaw Wiki](https://github.com/openclaw/wiki)
- [Firecrawl API 文档](https://docs.firecrawl.dev/)
- [Brave Search API 文档](https://api.search.brave.com/app/documentation)

---

## 💬 交流与反馈

如果你在使用过程中遇到问题，或有改进建议，欢迎通过以下方式交流：

- 提交 [GitHub Issue](issues) 描述具体问题
- 如需进一步讨论，可在 Issue 中说明，视情况建立专项讨论

> 本仓库聚焦工具本身的技术讨论，不涉及课程推广或商业合作。

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/strongqiang100">strongqiang100</a> 
  · Focus on practical AI automation for e-commerce</sub>
</div>
