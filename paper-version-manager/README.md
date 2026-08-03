# 论文版本演进管理 (Paper Version Manager)

> 📄 A skill for managing the full lifecycle of academic paper versions — from version lineage visualization to quality scoring, changelog generation, safe baseline management, and decision log auditing.

> 📄 论文版本演进管理技能 — 从版本血缘可视化到质量评分、变更日志生成、安全底本管理与决策日志审计，覆盖学术论文写作的全生命周期。

---

## 概述 (Overview)

当一篇学术论文经历多轮修改、多人协作、多次审查后，版本关系会迅速变得复杂。本技能提供了一套系统化的版本管理方法论和工具，帮助你：

- 🔗 **追踪版本血缘**：可视化版本之间的继承、分支与合并关系
- 📊 **量化版本质量**：从四个维度加权评分，追踪质量变化趋势
- 📝 **自动生成变更日志**：基于审查报告差异自动生成结构化 CHANGELOG
- 🛡️ **安全管理底本**：确保数据诚信度最高的版本始终可回溯
- ✅ **审计关键决策**：记录并逐版核查关键决策的落实情况

---

## 功能亮点 (Features)

| 功能 | 说明 |
|------|------|
| **版本血缘树** | Mermaid 可视化版本演进路径，关键节点高亮标注 |
| **四维加权评分** | 内容完整性(0.30) + 逻辑完整性(0.25) + 逻辑闭环(0.25) + AI检测评估(0.20) |
| **雷达图 & 趋势图** | Python matplotlib 生成评分雷达图和趋势折线图 |
| **CHANGELOG 自动生成** | 从审查报告中提取变更，按 P0-P3 分级输出 |
| **安全底本策略** | 多版本冲突时确保数据诚信度不被破坏的回退机制 |
| **决策日志模板** | 结构化记录 + 逐版审计（✅⚠️❌🔄四级分类） |

---

## 文件结构 (File Structure)

```
paper-version-manager/
├── SKILL.md                          # 技能入口，触发词与快速导航
├── README.md                         # 本文档，概述与文件结构说明
└── references/
    ├── version-tree.md               # 版本血缘树：概念、方法、Mermaid 代码示例
    ├── scoring-system.md             # 四维加权评分系统：公式、细则、图表代码
    ├── changelog-workflow.md         # 变更日志工作流：自动生成流程与模板
    ├── safe-baseline.md              # 安全底本策略：核心原则与操作流程
    └── decision-log.md               # 决策日志与审计：模板、审计方法、示例
```

---

## 快速开始 (Quick Start)

1. **查看版本演进** → 阅读 `references/version-tree.md`，用 Mermaid 绘制版本血缘树
2. **评分当前版本** → 阅读 `references/scoring-system.md`，用四维加权公式评估质量
3. **生成变更日志** → 阅读 `references/changelog-workflow.md`，从审查报告提取 CHANGELOG
4. **保护数据诚信** → 阅读 `references/safe-baseline.md`，建立安全底本机制
5. **审计关键决策** → 阅读 `references/decision-log.md`，逐版核查决策落实

---

## 对话示例 (Conversation Examples)

**用户：** "帮我看看论文各版本之间的演进关系"
→ 使用 `references/version-tree.md` 中的方法生成版本血缘树

**用户：** "给 v2.0 版本打个分"
→ 使用 `references/scoring-system.md` 中的四维加权公式进行评分

**用户：** "生成本次修改的变更日志"
→ 使用 `references/changelog-workflow.md` 中的流程生成 CHANGELOG

**用户：** "两个并行修改的版本怎么合并？"
→ 使用 `references/safe-baseline.md` 中的安全底本策略进行合并

**用户：** "审计一下所有决策在当前版本的落实情况"
→ 使用 `references/decision-log.md` 中的审计方法逐项核查

---

作者：人类Nan
