# 学术配色方案 (Academic Color Schemes)

## 概述

本技能提供 3 套经过学术审稿验证的配色方案，覆盖彩色数字排版、色盲友好和灰阶打印三种场景。所有配色均经过 Color Universal Design (CUD) 原则验证。

---

## 方案 A：学术深蓝 (Academic Navy Blue) — 默认方案

**适用场景：** 彩色数字期刊投稿、会议海报、PPT 演示、网页展示

**设计理念：** 以沉稳的深蓝色为主调，符合学术论文的严肃性和专业性要求，色彩对比度适中，长时间阅读不疲劳。

| 用途 | 色值 | 色样 | 说明 |
|------|------|------|------|
| **主填充色** | `#2C5AA0` | ██████ | 深蓝，用于关键节点和强调元素 |
| **辅助浅色** | `#D6E4F4` | ██████ | 浅蓝，用于普通节点填充 |
| **边框色** | `#1A3A6B` | ██████ | 深蓝边框，增强结构感 |
| **字体色** | `#1A1A2E` | ██████ | 近黑色，高可读性 |
| **箭头色** | `#2C5AA0` | ██████ | 与主色一致 |
| **强调色** | `#E85D3A` | ██████ | 暖橙，用于高亮/警示 |
| **背景色** | `#FFFFFF` | ██████ | 纯白背景 |
| **浅色背景** | `#F0F4FA` | ██████ | 子图背景/集群背景 |

### DOT 配色片段

```dot
graph [bgcolor="white"];
node [style="filled,rounded",
      fillcolor="#D6E4F4",
      color="#1A3A6B",
      fontcolor="#1A1A2E",
      penwidth=1.2];
edge [color="#2C5AA0",
      penwidth=1.0];

// 强调节点
important_node [fillcolor="#2C5AA0", fontcolor="white"];

// 警示/高亮节点
alert_node [fillcolor="#E85D3A", fontcolor="white"];

// 集群背景
subgraph cluster_example {
    style="filled";
    fillcolor="#F0F4FA";
    color="#1A3A6B";
}
```

---

## 方案 B：色盲友好 (Colorblind-Friendly) — 审稿安全方案

**适用场景：** 国际期刊投稿（尤其 IF 期刊要求）、包含多类别对比的图表、需确保所有读者可区分

**设计理念：** 基于 Okabe-Ito 调色盘（Nature 系列期刊推荐），使用橙色 `#E69F00` + 天蓝 `#56B4E9` 作为主色调，这两种颜色在红绿色盲、蓝黄色盲和全色盲三种类型中均保持可分辨性。约 8% 的男性读者有某种形式的色觉缺陷，此方案确保图表信息对所有读者公平传达。

| 用途 | 色值 | 色样 | 说明 |
|------|------|------|------|
| **主色 A（橙）** | `#E69F00` | ██████ | 橙黄色调，色盲可辨 |
| **主色 B（天蓝）** | `#56B4E9` | ██████ | 天蓝色调，与橙色高对比 |
| **辅助绿** | `#009E73` | ██████ | 蓝绿色，第三对比色 |
| **边框色** | `#555555` | ██████ | 中灰，通用边框 |
| **字体色** | `#000000` | ██████ | 纯黑，最高对比度 |
| **箭头色** | `#555555` | ██████ | 中灰箭头 |
| **强调色** | `#CC79A7` | ██████ | 粉紫，第四高亮色 |
| **背景色** | `#FFFFFF` | ██████ | 纯白背景 |
| **浅色背景** | `#FFF5E6` | ██████ | 极淡橙，子图背景 |

### DOT 配色片段

```dot
graph [bgcolor="white"];
node [style="filled,rounded",
      fillcolor="#FFF5E6",
      color="#555555",
      fontcolor="#000000",
      penwidth=1.2];
edge [color="#555555",
      penwidth=1.0];

// 系统 A（橙色调）
sys_a [fillcolor="#E69F00", fontcolor="white"];

// 系统 B（蓝色调）
sys_b [fillcolor="#56B4E9", fontcolor="black"];

// 系统 C（绿色调，可选第三类）
sys_c [fillcolor="#009E73", fontcolor="white"];

// 高亮/强调
highlight [fillcolor="#CC79A7", fontcolor="white"];
```

---

## 方案 C：灰阶打印安全 (Grayscale Print-Safe)

**适用场景：** 纸质期刊投稿（无彩色印刷需求）、低成本打印、灰度要求严格的期刊

**设计理念：** 仅使用不同灰度的黑白配色，确保在黑白打印机输出或灰度缩印后仍可清晰区分层次。使用灰度阶梯而非色彩来传达层级信息。

| 用途 | 色值 | 色样 | 说明 |
|------|------|------|------|
| **深灰 1** | `#333333` | ██████ | 最深色，核心强调 |
| **深灰 2** | `#666666` | ██████ | 次要强调 |
| **中灰** | `#999999` | ██████ | 普通节点填充 |
| **浅灰** | `#CCCCCC` | ██████ | 最浅填充色 |
| **极浅灰** | `#EEEEEE` | ██████ | 背景/集群 |
| **边框色** | `#333333` | ██████ | 深灰边框 |
| **字体色** | `#000000` | ██████ | 纯黑字体 |
| **箭头色** | `#666666` | ██████ | 中灰箭头 |
| **强调线** | `#000000` | ██████ | 纯黑加粗 |
| **填充白** | `#FFFFFF` | ██████ | 纯白 |

### DOT 配色片段

```dot
graph [bgcolor="white"];
node [style="filled,rounded",
      fillcolor="#EEEEEE",
      color="#333333",
      fontcolor="#000000",
      penwidth=1.2];
edge [color="#666666",
      penwidth=1.0];

// 核心节点（最深）
core_node [fillcolor="#333333", fontcolor="white"];

// 重要节点（次深）
important_node [fillcolor="#666666", fontcolor="white"];

// 普通节点
normal_node [fillcolor="#CCCCCC", fontcolor="black"];

// 子图背景
subgraph cluster_example {
    style="filled";
    fillcolor="#F8F8F8";
    color="#999999";
}
```

---

## 配色方案选择决策表

| 场景 | 推荐方案 | 原因 |
|------|----------|------|
| 国内期刊投稿（彩色电子版） | 方案 A | 深蓝系符合国内学术审美 |
| 国际 SCI 期刊投稿 | 方案 B | 多满足审稿无障碍要求 |
| 会议 Oral/Poster 展示 | 方案 A | 深蓝在投影仪上表现好 |
| 纸质期刊（非彩色） | 方案 C | 灰阶打印不丢信息 |
| 包含 3 类以上对比的图表 | 方案 B | 色盲友好 + 足够区分度 |
| 低成本预印本 / arXiv | 方案 C | 减少文件复杂度 |
| 论文被要求修改图表配色 | 方案 B | 通常审稿意见针对色盲无障碍 |

---

## 快速切换配色

在实际使用中，只需替换 DOT 文件顶部的占位符即可切换方案：

```dot
// === 方案 A 参数值 ===
// {{COLOR_PRIMARY}} = "#2C5AA0"
// {{COLOR_LIGHT}}   = "#D6E4F4"
// {{COLOR_BORDER}}  = "#1A3A6B"
// {{COLOR_FONT}}    = "#1A1A2E"
// {{COLOR_ACCENT}}  = "#E85D3A"

// === 方案 B 参数值 ===
// {{COLOR_PRIMARY}} = "#E69F00"
// {{COLOR_LIGHT}}   = "#FFF5E6"
// {{COLOR_BORDER}}  = "#555555"
// {{COLOR_FONT}}    = "#000000"
// {{COLOR_ACCENT}}  = "#CC79A7"

// === 方案 C 参数值 ===
// {{COLOR_PRIMARY}} = "#333333"
// {{COLOR_LIGHT}}   = "#EEEEEE"
// {{COLOR_BORDER}}  = "#333333"
// {{COLOR_FONT}}    = "#000000"
// {{COLOR_ACCENT}}  = "#666666"
```
