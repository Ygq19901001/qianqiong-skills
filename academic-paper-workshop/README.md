# 学术论文工坊 / Academic Paper Workshop

> 论文写作全流程技能套件 —— 审查 / 配图 / 排版 / 版本管理 / 参考文献，五合一

A unified skill suite for full-cycle academic paper production: review, figures, formatting, versioning, and references.

---

## 为什么需要这个套件？

写论文不是线性流程。你在审查中发现配图问题 → 改了配图排版乱了 → 排版后版本号又乱了 → 最后参考文献格式还不一致。这五个技能各自解决一个环节，套件把它们串联起来。

## 五件套

| 技能 | 一句话 |
|------|--------|
| **paper-review-methodology** | 29类审查方法，P0-P3分级，从宏观架构到微观措辞全覆盖 |
| **academic-figure-gen** | Graphviz DOT 引擎驱动的学术配图，5类模板+3套配色+色盲友好 |
| **academic-docx-toolkit** | python-docx 深度排版，表格/图片/段落/XML级操作+安全策略 |
| **paper-version-manager** | 版本血缘树+四维加权评分+决策日志审计 |
| **academic-reference-formatter** | GB/T 7714 + APA + MLA + IEEE + Chicago，DOI自动填充 |

## 安装

```bash
# 安装套件入口
skillhub install academic-paper-workshop

# 安装五个子技能
skillhub install paper-review-methodology
skillhub install academic-figure-gen
skillhub install academic-docx-toolkit
skillhub install paper-version-manager
skillhub install academic-reference-formatter
```

## 典型工作流

```
框架设计 → 内容撰写+配图 → 审查迭代 → 格式终审
   ↓            ↓              ↓            ↓
 version     figure        review       reference
 review      docx          version       docx
                           docx          review
```

## 文件结构

```
academic-paper-workshop/
├── SKILL.md              # 套件入口 + 全流程工作流 + 跨技能联动
└── README.md             # 本文件
```

> 五个子技能各有独立文件夹，内含详细的 reference 文档。

## 作者

人类Nan

## 许可

MIT License

## 作者

基于真实的学术论文生产全流程经验提炼
