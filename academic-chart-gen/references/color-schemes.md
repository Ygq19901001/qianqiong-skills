# 数据图学术配色方案 | Academic Color Schemes for Data Charts

> 以下方案与 academic-figure-gen（架构图配色）互补，专为统计数据图表优化。
> 所有方案含完整hex色值 + matplotlib自定义colormap代码。

---

## 配色方案总览 | Color Scheme Overview

| 方案 | 名称 | 适用场景 | 色盲友好 | 灰阶安全 |
|------|------|---------|---------|---------|
| **A** | 数据图学术蓝 | 单组数据、梯度渐变 | ❌ | ✅ |
| **B** | Okabe-Ito 色盲友好 | 多组对比（≤8组） | ✅ | ⚠️ |
| **C** | Nature/Science 推荐 | 通用学术出版 | ⚠️ | ✅ |
| **D** | 灰阶打印安全 + 纹理 | 黑白期刊/打印 | ✅ | ✅ |

---

## 方案A：数据图学术蓝（单色渐变）| Academic Blue Monochrome

**适用**：单组数据的梯度变化、单一变量的多水平/多时间点

**色值**：

| 级别 | Hex | RGB | 用途 |
|------|-----|-----|------|
| 最浅 | `#D1E5F0` | (209,229,240) | 背景/低值 |
| 浅 | `#92C5DE` | (146,197,222) | 次低值 |
| 中 | `#67A9CF` | (103,169,207) | 中值 |
| 深 | `#4393C3` | (67,147,195) | 次高值 |
| 最深 | `#2166AC` | (33,102,172) | 高值/主色 |

```python
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# 离散色列表
BLUE_MONOCHROME = ['#D1E5F0', '#92C5DE', '#67A9CF', '#4393C3', '#2166AC']

# 自定义连续colormap
blue_mono_cmap = mcolors.LinearSegmentedColormap.from_list(
    'AcademicBlue',
    ['#D1E5F0', '#67A9CF', '#2166AC'],
    N=256
)

# 注册到matplotlib
plt.cm.register_cmap(name='AcademicBlue', cmap=blue_mono_cmap)

# 使用示例
fig, ax = plt.subplots(figsize=(3.5, 2.5))
x = np.linspace(0, 1, 50)
y = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X*5) + np.cos(Y*5)
ax.contourf(X, Y, Z, cmap='AcademicBlue', levels=15)
plt.show()
```

---

## 方案B：Okabe-Ito 色盲友好对比色 | Colorblind-Friendly

**适用**：多组对比（2-8组），确保红绿色盲可区分

**来源**：Okabe & Ito (2008) "Color Universal Design"

**色值**：

| 序号 | 名称 | Hex | RGB | 用于 |
|------|------|-----|-----|------|
| 1 | 橙 | `#E69F00` | (230,159,0) | 组1 / 对照 |
| 2 | 天蓝 | `#56B4E9` | (86,180,233) | 组2 |
| 3 | 蓝绿 | `#009E73` | (0,158,115) | 组3 |
| 4 | 黄 | `#F0E442` | (240,228,66) | 组4 |
| 5 | 蓝 | `#0072B2` | (0,114,178) | 组5 |
| 6 | 朱红 | `#D55E00` | (213,94,0) | 组6 |
| 7 | 粉紫 | `#CC79A7` | (204,121,167) | 组7 |
| 8 | 黑 | `#000000` | (0,0,0) | 组8 / 边框 |

```python
OKABE_ITO = [
    '#E69F00',  # Orange
    '#56B4E9',  # Sky Blue
    '#009E73',  # Bluish Green
    '#F0E442',  # Yellow
    '#0072B2',  # Blue
    '#D55E00',  # Vermillion
    '#CC79A7',  # Reddish Purple
    '#000000',  # Black
]

# 注册为matplotlib color cycle
plt.rcParams['axes.prop_cycle'] = plt.cycler('color', OKABE_ITO)

# ========== 使用示例：8组柱状图 ==========
np.random.seed(42)
groups = [f'Group {i+1}' for i in range(8)]
values = [3 + i*0.5 + np.random.normal(0, 0.3) for i in range(8)]
errors = [0.3] * 8

fig, ax = plt.subplots(figsize=(5, 3))
bars = ax.bar(groups, values, yerr=errors, color=OKABE_ITO,
              capsize=3, edgecolor='white', linewidth=0.5)
ax.set_ylabel('Value')
ax.spines[['top', 'right']].set_visible(False)
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.show()
```

---

## 方案C：Nature/Science 推荐配色 | Journal-Approved Palettes

### C1: Nature 推荐色

```python
# Nature Publishing Group 常用色板
NATURE_COLORS = [
    '#E64B35',  # Red
    '#4DBBD5',  # Cyan
    '#00A087',  # Green
    '#3C5488',  # Blue
    '#F39B7F',  # Salmon
    '#8491B4',  # Grey-Blue
    '#91D1C2',  # Mint
    '#DC0000',  # Deep Red
]

# Nature 风格对比色（4组）
NATURE_CONTRAST_4 = [
    '#E64B35',  # Red (primary)
    '#4DBBD5',  # Cyan (contrast)
    '#00A087',  # Green
    '#3C5488',  # Dark Blue
]
```

### C2: Science 推荐色

```python
# Science/AAAS 常用色板
SCIENCE_COLORS = [
    '#0072B2',  # Blue
    '#D55E00',  # Orange-Red
    '#009E73',  # Green
    '#CC79A7',  # Pink
    '#F0E442',  # Yellow
    '#56B4E9',  # Light Blue
    '#E69F00',  # Gold
    '#000000',  # Black
]
```

### C3: 柔和学术色

```python
# 降低饱和度，适合大面积填充
SOFT_ACADEMIC = [
    '#7EA6C4',  # Muted Blue
    '#C47E7E',  # Muted Red
    '#7EC47E',  # Muted Green
    '#C4A87E',  # Muted Gold
    '#A87EC4',  # Muted Purple
    '#7EC4C4',  # Muted Teal
]

# 注册
plt.rcParams['axes.prop_cycle'] = plt.cycler('color', SOFT_ACADEMIC)
```

---

## 方案D：灰阶打印安全 + 纹理填充 | Print-Safe Grayscale with Patterns

**适用**：纸质期刊黑白印刷、要求灰度图的期刊

**策略**：灰度色 + hatch纹理确保即使黑白印刷也能区分各组。

```python
GRAYSCALE_COLORS = [
    '#FFFFFF',  # White (0%)
    '#E0E0E0',  # 12% gray
    '#BDBDBD',  # 26% gray
    '#9E9E9E',  # 38% gray
    '#757575',  # 54% gray
    '#4F4F4F',  # 69% gray
    '#2E2E2E',  # 82% gray
    '#000000',  # Black (100%)
]

HATCH_PATTERNS = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']

def draw_grayscale_with_patterns(ax, groups, values, errors=None,
                                  colors=None, patterns=None):
    """
    绘制灰阶安全的分组柱状图（带纹理填充）。
    """
    if colors is None:
        colors = GRAYSCALE_COLORS
    if patterns is None:
        patterns = HATCH_PATTERNS

    n = len(groups)
    x = np.arange(n)

    for i, (group, val, color, pattern) in enumerate(
        zip(groups, values, colors[:n], patterns[:n])):

        bar = ax.bar(i, val, color=color, edgecolor='black',
                     linewidth=0.8, hatch=pattern)

    if errors is not None:
        ax.errorbar(x, values, yerr=errors, fmt='none',
                    ecolor='black', capsize=4, capthick=0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    return ax


# ========== 使用示例 ==========
np.random.seed(42)
groups_demo = ['Control', 'Low', 'Medium', 'High', 'Very High']
values_demo = [5.2, 4.8, 6.1, 7.3, 8.5]
errors_demo = [0.5, 0.6, 0.5, 0.7, 0.8]

fig, ax = plt.subplots(figsize=(4, 3))
draw_grayscale_with_patterns(ax, groups_demo, values_demo, errors_demo)
ax.set_ylabel('Response')
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('grayscale_pattern.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 配色工具箱 | Color Toolkit

### 色值预览与验证

```python
def preview_palette(colors, names=None, title=None):
    """可视化配色方案的色块预览。"""
    fig, ax = plt.subplots(figsize=(len(colors)*0.8, 1.2))
    for i, color in enumerate(colors):
        rect = plt.Rectangle((i, 0), 1, 1, facecolor=color,
                              edgecolor='black', linewidth=0.5)
        ax.add_patch(rect)
        if names and i < len(names):
            ax.text(i + 0.5, -0.3, names[i], ha='center', fontsize=6)
        ax.text(i + 0.5, 0.5, color, ha='center', va='center', fontsize=6,
                color='white' if sum(int(color[j:j+2], 16)
                                     for j in (1,3,5)) < 384 else 'black')
    ax.set_xlim(0, len(colors))
    ax.set_ylim(-1, 1.5)
    ax.axis('off')
    if title:
        ax.set_title(title, fontsize=9, fontweight='bold')
    plt.show()


# 预览所有方案
preview_palette(BLUE_MONOCHROME, title='Scheme A: Academic Blue Monochrome')
preview_palette(OKABE_ITO, title='Scheme B: Okabe-Ito Colorblind-Friendly')
preview_palette(NATURE_COLORS, title='Scheme C1: Nature Colors')
preview_palette(SCIENCE_COLORS, title='Scheme C2: Science Colors')
preview_palette(GRAYSCALE_COLORS, title='Scheme D: Grayscale')
```

### 发散型配色（用于热力图）

```python
# 蓝-白-红发散色（适合相关性矩阵）
DIVERGING_BLUE_RED = mcolors.LinearSegmentedColormap.from_list(
    'DivergingBlueRed',
    ['#2166AC', '#F7F7F7', '#B2182B'],
    N=256
)

# 科学色板（coolwarm替代）
SCIENTIFIC_DIVERGING = mcolors.LinearSegmentedColormap.from_list(
    'ScientificDiverging',
    ['#053061', '#2166AC', '#4393C3', '#92C5DE', '#D1E5F0',
     '#F7F7F7',
     '#FDDBC7', '#F4A582', '#D6604D', '#B2182B', '#67001F'],
    N=256
)

plt.cm.register_cmap(name='ScientificDiverging', cmap=SCIENTIFIC_DIVERGING)
```

---

## 配色选择决策树 | Color Scheme Decision Tree

```
你的图表需要什么？
├─ 单组数据（如时间序列、梯度变化）
│   └─ 方案A：学术蓝单色渐变
├─ 多组对比（2-4组）
│   ├─ 有色盲读者 → 方案B：Okabe-Ito
│   ├─ 投Nature → 方案C1：Nature色
│   ├─ 投Science → 方案C2：Science色
│   └─ 通用 → 方案C3：柔和学术色
├─ 多组对比（5-8组）
│   └─ 方案B：Okabe-Ito（最多支持8色）
├─ 需要印刷/黑白版
│   └─ 方案D：灰阶 + 纹理
└─ 热力图/渐变
    └─ ScientificDiverging colormap
```

---

## 注意事项 | Notes

1. **方案D的hatch纹理**在PDF/SVG矢量输出中效果最佳，PNG位图中可能显示为锯齿。
2. **方案B的黄色(`#F0E442`)**在白色背景上可读性较差，建议用于深色背景或配合深色描边。
3. 多组比较时，每组分配不同颜色，始终在图例中注明颜色含义。
4. 连续型colormap（如Blue Monochrome）避免用于分类数据——分类数据应使用离散色。
