# 贡献指南 · Contributing

[中文入口](README.md) · [English home](README.en.md)

欢迎补充做过的方案、遇到的问题，以及工具在哪些条件下不适用。/ Contributions can describe approaches you have tried, problems you encountered, and conditions where a tool did not fit.

## 提交要求 / Submission requirements

1. 写明问题、输入、输出、工具与适用范围。/ State the problem, inputs, outputs, tools, and scope.
2. 提供官方来源、核验日期和证据等级。/ Supply official sources, review date, and evidence level.
3. 区分 LIVE、DOC、DEMO、DESIGN、RESEARCH；不能将可导入写成生产验证。/ Distinguish evidence levels; importability is not production validation.
4. 示例默认合成数据、无凭证、无个人信息、无自动外发。/ Default to synthetic data without secrets, personal details, or automatic delivery.
5. 更新中英文对应内容；保留适用边界和未知项。/ Update corresponding language content and preserve limitations.
6. 第三方代码、模型与素材说明许可；不得擅自修改他人版权声明。/ State third-party terms and preserve third-party copyright notices.

## 本地检查 / Local checks

```bash
python3 -m unittest discover -s tests -v
node tests/test_workflow.js
python3 scripts/check_repo.py
```

涉及真实平台时，附上脱敏的测试范围、版本和结果，不提交原始账户响应。高后果动作先在沙箱或 dry run 中验证。文档中的建议应解释为什么适用、何时失效，而不是只写工具名字。

For platform work, report de-identified scope, version, and results rather than raw account responses. Test consequential actions in a sandbox or dry run first. Explain when recommendations work and fail rather than merely adding tool names.

## 公开前复核 / Before publication

每句话是否服务读者？是否混入私人记录或工作过程？是否有无依据承诺？能否更简洁？发布后回读最终文件，确认格式、链接和内容。

Does each sentence serve readers? Does it disclose private records or process notes? Does it promise unsupported results? Can it be clearer? Read published files back to verify formatting, links, and content.
