<!-- SECLEVEL: INTERNAL -->

# Academic Reference Formatter 📚

参考文献格式化工具 — 支持 APA / MLA / GB/T 7714 / Chicago / IEEE 多格式互转。

## 功能

- **多格式支持**：APA 7th、MLA 9th、GB/T 7714-2015、Chicago、IEEE
- **中英文分节排序**：中文文献按拼音、英文按字母自动排序
- **智能识别**：从原始文本自动解析作者/标题/期刊/年份/卷期/页码
- **变更报告**：格式化前输出变更报告给用户确认
- **去杂乱信息**：默认去除 DOI 链接等非必要信息
- **输出 DOCX**：生成格式规范的 .docx 文件，可直接用于论文

## 使用场景

- 从知网/Google Scholar 导出的文献格式混乱需要整理
- 投稿期刊要求特定引用格式（APA/MLA/GB-T 等）
- 论文参考文献列表排版风格统一化

## 仓库结构

```
reference-formatter/
├── SKILL.md            # 技能定义与工作流
├── README.md           # 本文件
├── _meta.json          # 元数据
└── reference/
    └── formats.md      # 五种格式详细规范
```

## 作者

人类Nan

## 许可

MIT License
