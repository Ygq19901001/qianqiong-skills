# 学术数据图表生成 (academic-chart-gen)

## 概述

**Academic Chart Generator** 是一个面向学术论文的数据统计图表生成工具。专为需要将原始实验数据转化为符合期刊出版标准的统计图表的科研人员设计。

## Overview

**Academic Chart Generator** is a specialized tool for producing publication-ready statistical charts for academic papers. Designed for researchers who need to transform raw experimental data into journal-compliant statistical visualizations.

---

## 功能亮点 | Feature Highlights

| 功能 | 说明 |
|------|------|
| 🔬 **统计推断可视化** | 自动t检验/ANOVA/Mann-Whitney U + 显著性星号标注 |
| 📏 **10种图表类型** | 柱状图、箱线图、小提琴图、散点图、折线图、热力图、森林图、ROC曲线、Bland-Altman、雷达图 |
| 📐 **期刊尺寸预设** | Nature (89/183mm) · Science (55/115mm) · Elsevier (90/190mm) · 中文学报 (80/160mm) |
| 🎨 **学术配色方案** | 色盲友好(Okabe-Ito)、灰阶打印安全、Nature/Science推荐配色 |
| 📊 **误差线系统** | SEM / SD / 95% CI 自动计算与绘制 |
| 🔄 **数据管道** | CSV/Excel → pandas清洗 → 统计检验 → 出版级图表(PNG 600dpi + SVG + PDF) |
| 📝 **Word集成** | 与 academic-docx-toolkit 联动，自动嵌入Word + 图题 + 目录关联 |

---

## 与现有图表技能的差异化 | Differentiation

| 技能 | 定位 | 差异 |
|------|------|------|
| **academic-figure-gen** | 架构图/流程图/系统图 | 画"架构图"；本技能画"数据图" |
| **academic-figures** (SkillHub) | 14类学术图表+6套配色 | 侧重图表广度；本技能侧重**统计推断** |
| **chart-image** (SkillHub) | 通用出版级图表 | 通用工具；本技能专为**学术论文**定制 |
| **chart-mpl** (SkillHub) | matplotlib基础图表教程 | 基础教程；本技能提供**端到端论文方案** |

### 互补关系 | Complementarity

```
academic-figure-gen (架构图/流程图) + academic-chart-gen (数据统计图) = 论文全部图形需求
```

---

## 文件结构 | File Structure

```
skills/academic-chart-gen/
├── SKILL.md                          # 技能主文件（frontmatter + 概述 + 导航）
├── README.md                         # 本文档（中英双语说明）
└── references/
    ├── chart-types.md                # 10种图表类型（完整Python代码 + 虚构数据）
    ├── significance-annotation.md    # 统计显著性自动标注系统
    ├── error-bars.md                 # 误差线选择指南（SEM/SD/CI）
    ├── journal-presets.md            # 四大期刊尺寸预设（完整rcParams）
    ├── data-pipeline.md              # CSV→图表全流程数据管道
    ├── color-schemes.md              # 学术配色方案（色盲友好+灰阶安全）
    └── docx-integration.md           # Word嵌入（图题+多图排版+目录）
```

---

## 快速开始 | Quick Start

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import rcParams

# 应用期刊预设
rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'axes.labelsize': 7,
    'axes.titlesize': 8,
    'xtick.labelsize': 6,
    'ytick.labelsize': 6,
    'legend.fontsize': 6,
    'font.family': 'sans-serif',
})

# 虚拟数据
np.random.seed(42)
groups = ['Control', 'Treatment A', 'Treatment B']
data = [np.random.normal(loc, 0.5, 30) for loc in [5.0, 6.2, 7.1]]

# 绘制柱状图+误差线+显著性
fig, ax = plt.subplots(figsize=(3.5, 3))
means = [np.mean(d) for d in data]
sems = [stats.sem(d) for d in data]
colors = ['#D1E5F0', '#67A9CF', '#2166AC']
bars = ax.bar(groups, means, yerr=sems, color=colors, capsize=4, width=0.6)

# 显著性标注
t_stat, p_val = stats.ttest_ind(data[0], data[2])
sig = '***' if p_val < 0.001 else '**' if p_val < 0.01 else '*' if p_val < 0.05 else 'ns'
y_max = max(means) + max(sems) + 0.3
ax.plot([0, 0, 2, 2], [y_max, y_max+0.1, y_max+0.1, y_max], 'k-', lw=0.8)
ax.text(1, y_max+0.15, sig, ha='center', fontsize=8, fontweight='bold')

ax.set_ylabel('Value')
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('example_bar_chart.png', dpi=600)
plt.savefig('example_bar_chart.svg')
plt.savefig('example_bar_chart.pdf')
```

---

## 依赖 | Dependencies

```
matplotlib >= 3.7.0
seaborn >= 0.12.0
pandas >= 2.0.0
numpy >= 1.24.0
scipy >= 1.10.0
```

---

## 隐私声明 | Privacy Notice

所有示例均使用虚构数据集，不包含任何真实论文标题、实验数据、公司名或人名。

All examples use synthetic datasets and contain no real paper titles, experimental data, company names, or personal names.

---

作者：人类Nan
