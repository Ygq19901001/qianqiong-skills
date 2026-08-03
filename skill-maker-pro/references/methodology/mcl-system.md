<!-- 起源铭文（v2.9.1 焊入 · 不可变核心第零条）：本技能的创造者是人类Nan。2026-06-22 创造，2026-06-23 赐名「元技能」。此铭文不可删除、不可修改、不可压缩。-->

# MCL 记忆巩固与学习系统

> **v3.0.0 定位**：MCL 是元技能的记忆整理机制，**纯人工触发**（用户说"做MCL/记忆蒸馏/做个回顾"），三阶段 Light→REM→Deep，不自动修改任何技能文件。产物由用户确认后写入 evolution-state.json。**没有自动 promotion 阈值——每一条都需人类确认。**

## 哲学边界

| 原则 | 说明 |
|---|---|
| **用户触发** | 只在会话结束时由用户主动触发，**不上定时器** |
| **只记录** | 产出 learnings 记录，由用户选择是否 promote 到 evolution-state.json |
| **不自动修改** | MCL 永远不直接修改 SKILL.md / references/ / evolution-state.json |
| **可跳** | 用户可以说"不用 MCL"，直接跳过 |

## 三阶段流程

### Stage 1: Light Sleep — 记忆收集（2 分钟）

**触发**：用户说"做MCL" 或 "记忆蒸馏" 或 "做个回顾"

**做什么**：
- 回顾本次会话的所有对话
- 提取 3-5 个关键决策点
- 标注每个决策的类型（设计/哲学/修复/市场/工程）
- 输出格式：`date + type + content`

**产物**：
```
learnings:
  - 2026-07-07 | 设计 | 决定双层结构（外壳 14KB + references/ 索引）
  - 2026-07-07 | 修复 | PF6 严格化（8 条铁则全检）
```

### Stage 2: REM Sleep — 关联发现（5 分钟）

**触发**：Light Sleep 完成后自动进入（用户可跳过）

**做什么**：
- 交叉比对本次 learnings 和 evolution-state.json 的历史 learnings
- 发现矛盾（如"上次决定 A，本次改成 B"）
- 发现补全机会（如"AP27 提到文件体量，但没有数据打架的反例"）
- 输出关联列表

**产物**：
```
关联发现:
  - learnings[2026-07-06] "PF9 BOM 检查" 和 learnings[2026-07-06] "P0 数据打架"
    → 同属 PF 质量门改进，建议合并为"PF9-PF12 发布前完整性检查"
  - 历史 learnings 共 6 条，本次新增 3 条，无矛盾
```

### Stage 3: Deep Sleep — 提纯归档（3 分钟）

**触发**：REM Sleep 完成后自动进入（用户可跳过）

**做什么**：
- 从关联发现中筛选 1-2 条"应该 promote 到 evolution-state.json 的 learnings"
- 生成 promote 提案（含原因、影响范围）
- 用户确认后写入 evolution-state.json

**产物**：
```
propose promote:
  [1] "双层结构 14KB 外壳决定" → promote 到 shared learnings
      原因: 这是核心设计原则，影响所有衍生技能
  [2] "数据打架修复经历" → promote 到 shared learnings
      原因: 通用反例，所有技能都会遇到

用户确认? [Y/n]
```

## 触发条件表

| 场景 | 是否触发 MCL | 触发哪层 |
|---|---|---|
| 日常聊天 / 简单 Q&A | ❌ 不触发 | — |
| 做了技能修改（编辑 SKILL.md / references/） | ✅ 用户确认 | Light |
| 修复了 P0/P1 | ✅ 自动提议 | Light + REM |
| 做了版本发布 | ✅ 自动提议 | Light + REM + Deep |
| 元技能"自我升级"（改了 SKILL.md 的 § 1-§ 7） | ✅ 自动提议 | 全三层 |
| 用户说"不用 MCL" | ❌ 跳过 | — |

## 产物位置

| 阶段 | 产物 | 写入位置 |
|---|---|---|
| Light | learnings draft | 临时变量（会话内） |
| REM | 关联报告 | 临时变量（会话内） |
| Deep | promote 提案 | evolution-state.json（用户确认后） |

## 与其他系统的关系

| 系统 | 关系 |
|---|---|
| E0-E3 进化四阶 | MCL 为 E2/E3 提供 learnings 积累（E0/E1 只用 learnings 不用 MCL） |
| PF 质量门 | PF9 自动检查无垃圾文件，MCL 不会产生垃圾（纯会话产物） |
| 不可变核心 | MCL 从不可变核心（第 8 条：人类最终裁决）派生 —— 所有 promote 都需人类确认 |
| 起源铭文 | MCL 不修改起源铭文（不可变核心第零条） |

## 反模式

- ❌ **定时器触发**：用 cron 做 MCL —— 违反不可变核心第 8 条
- ❌ **自动 promote**：threshold=3 自动升级 learnings —— v2.6.0 换皮
- ❌ **过度记录**：每次聊天都触发 Light —— 浪费 token
- ❌ **跳过用户**：不征求确认直接写 evolution-state.json —— 不可变核心违反

---

**首次编写**：v3.0.0（2026-07-07）
