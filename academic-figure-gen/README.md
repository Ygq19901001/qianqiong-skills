# 学术配图生成工作流 (Academic Figure Generation Workflow)

> Graphviz DOT 引擎驱动的学术论文配图生成工具

## 概述 / Overview

**学术配图生成工作流** 是一个专为学术论文写作设计的配图工具，基于 [Graphviz](https://graphviz.org/) DOT 语言引擎。它提供预构建的图表模板、审稿安全的配色方案，以及从 PNG 渲染到 Word 文档插入的完整工作流。

**Academic Figure Generation Workflow** is a figure-generation toolkit purpose-built for academic paper writing, powered by the Graphviz DOT engine. It provides pre-built diagram templates, publication-safe color schemes, and a complete pipeline from PNG rendering to Word document insertion.

## 功能亮点 / Features

- **5 类论文图表模板** — 架构分层图、业务流程图、工序追溯图、技术演进路线图、数据流图
- **3 套学术配色方案** — 学术深蓝（默认）、色盲友好（审稿安全）、灰阶打印安全
- **色盲友好** — 方案 B 经过 Color Universal Design (CUD) 验证，约 8% 男性读者可正常区分
- **中英双语标注** — 所有模板和文档均支持中英双语内容
- **DOCX 深度联动** — 直接调用 python-docx 将生成的 PNG 规范插入 Word，图题自动编号
- **跨平台** — Windows / macOS / Linux 均可使用

## 使用示例 / Usage Example

```bash
# 1. 安装 Graphviz（见 references/graphviz-setup.md）
# 2. 选择一个模板并替换占位符
cp references/dot-templates.md my-diagram.dot
# 编辑 my-diagram.dot，替换所有 {{PLACEHOLDER}}

# 3. 渲染为 PNG（推荐 300 DPI）
dot -Tpng -Gdpi=300 my-diagram.dot -o figure1.png

# 4. 插入 Word 文档（见 references/docx-integration.md）
python insert_figure.py figure1.png "系统架构分层示意图" --doc manuscript.docx
```

## 文件结构 / File Structure

```
academic-figure-gen/
├── SKILL.md                          # 技能入口（含 frontmatter 元数据）
├── README.md                         # 本文件 — 概述与快速入门
└── references/
    ├── graphviz-setup.md             # Graphviz 安装与配置指南
    ├── dot-templates.md              # 5 类图表 DOT 源码模板
    ├── color-schemes.md              # 3 套学术配色方案详解
    └── docx-integration.md           # Python 插入图片到 Word 完整方案
```

## 依赖 / Dependencies

| 工具 | 最低版本 | 用途 |
|------|----------|------|
| Graphviz | 2.44+ | DOT 源码渲染为 PNG/SVG/PDF |
| Python 3 | 3.7+ | 运行 DOCX 插入脚本 |
| python-docx | 0.8.11+ | Word 文档读写操作 |

## 作者

人类Nan

## 许可 / License

本技能为学术工具包，供研究写作使用。
