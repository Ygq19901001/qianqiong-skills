# 期刊尺寸预设 | Journal Size Presets

> 完整的 matplotlib rcParams 配置，覆盖 Nature/Science/Elsevier/中文学报四大系列。

---

## 概述 | Overview

学术期刊对图表尺寸有严格要求。正确的图形尺寸可确保投稿时不需要重新调整，避免字体大小不合规导致的返修。本文件提供四种主流期刊系列的完整 `rcParams` 预设配置。

---

## 尺寸对照 | Size Reference

| 期刊系列 | 单栏 (mm) | 单栏 (inch) | 双栏 (mm) | 双栏 (inch) |
|---------|----------|------------|----------|------------|
| **Nature 系列** | 89 | 3.50 | 183 | 7.20 |
| **Science 系列** | 55 | 2.17 | 115 | 4.53 |
| **Elsevier** | 90 | 3.54 | 190 | 7.48 |
| **中文学报 (GB/T)** | 80 | 3.15 | 160 | 6.30 |

---

## 1. Nature 系列预设 | Nature-Series Preset

**适用期刊**：Nature, Nature Communications, Nature Medicine, Nature Materials, Scientific Reports 等。

**规范要点**：
- 字体：Arial / Helvetica（sans-serif）
- 图形宽度：单栏 89mm (3.50 inch)，双栏 183mm (7.20 inch)
- 分辨率：≥300 dpi（推荐600 dpi）
- 线宽：细线 0.5pt，主线 1.0pt

```python
import matplotlib.pyplot as plt
from matplotlib import rcParams

NATURE_SINGLE_COLUMN = {
    # === 图形尺寸 ===
    'figure.figsize': (3.50, 3.00),      # 宽x高 (inch)，高可按需调整
    'figure.dpi': 600,
    'savefig.dpi': 600,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,

    # === 字体设置 ===
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 7,                       # 基础字号
    'axes.labelsize': 7,                  # 轴标签
    'axes.titlesize': 8,                  # 图标题
    'xtick.labelsize': 6,                 # 刻度标签
    'ytick.labelsize': 6,
    'legend.fontsize': 6,                 # 图例
    'legend.title_fontsize': 6.5,

    # === 线宽与标记 ===
    'axes.linewidth': 0.5,               # 轴线宽
    'grid.linewidth': 0.3,
    'lines.linewidth': 1.0,              # 数据线宽
    'lines.markersize': 4,
    'lines.markeredgewidth': 0.5,

    # === 刻度 ===
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.minor.width': 0.3,
    'ytick.minor.width': 0.3,
    'xtick.major.size': 2.5,
    'ytick.major.size': 2.5,
    'xtick.minor.size': 1.5,
    'ytick.minor.size': 1.5,
    'xtick.major.pad': 2,
    'ytick.major.pad': 2,

    # === 图例 ===
    'legend.frameon': False,
    'legend.handlelength': 1.0,
    'legend.handletextpad': 0.5,
    'legend.borderpad': 0.3,
    'legend.labelspacing': 0.3,

    # === 颜色 ===
    'axes.prop_cycle': plt.cycler('color', [
        '#2166AC', '#B2182B', '#4DAF4A', '#FF7F00',
        '#984EA3', '#A65628', '#F781BF', '#999999'
    ]),

    # === 科学计数 ===
    'axes.formatter.use_mathtext': True,
    'axes.formatter.limits': (-3, 4),

    # === 后端 ===
    'savefig.format': 'pdf',              # 默认保存为PDF（矢量）
}

NATURE_DOUBLE_COLUMN = {**NATURE_SINGLE_COLUMN,
    'figure.figsize': (7.20, 4.50),       # 双栏更宽
}


def apply_preset(preset_name='nature_single'):
    """应用期刊预设到全局 rcParams。"""
    presets = {
        'nature_single': NATURE_SINGLE_COLUMN,
        'nature_double': NATURE_DOUBLE_COLUMN,
    }
    if preset_name in presets:
        rcParams.update(presets[preset_name])
        print(f"Applied: {preset_name}")
    else:
        raise ValueError(f"Unknown preset: {preset_name}")
```

---

## 2. Science 系列预设 | Science-Series Preset

**适用期刊**：Science, Science Advances, Science Translational Medicine。

**规范要点**：
- 图形宽度极窄：单栏 55mm (2.17 inch)
- 字体：Helvetica 优先
- 建议使用矢量格式保存

```python
SCIENCE_SINGLE_COLUMN = {
    # === 图形尺寸 ===
    'figure.figsize': (2.17, 2.00),
    'figure.dpi': 600,
    'savefig.dpi': 600,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.01,

    # === 字体设置 ===
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 6,
    'axes.labelsize': 6,
    'axes.titlesize': 7,
    'xtick.labelsize': 5.5,
    'ytick.labelsize': 5.5,
    'legend.fontsize': 5.5,
    'legend.title_fontsize': 6,

    # === 线宽与标记 ===
    'axes.linewidth': 0.4,
    'grid.linewidth': 0.25,
    'lines.linewidth': 0.8,
    'lines.markersize': 3,
    'lines.markeredgewidth': 0.4,

    # === 刻度 ===
    'xtick.major.width': 0.4,
    'ytick.major.width': 0.4,
    'xtick.major.size': 2,
    'ytick.major.size': 2,
    'xtick.major.pad': 1.5,
    'ytick.major.pad': 1.5,

    # === 图例 ===
    'legend.frameon': False,
    'legend.handlelength': 0.8,
    'legend.handletextpad': 0.3,
    'legend.borderpad': 0.2,
    'legend.labelspacing': 0.2,

    # === 颜色 ===
    'axes.prop_cycle': plt.cycler('color', [
        '#0072B2', '#D55E00', '#009E73', '#CC79A7',
        '#F0E442', '#56B4E9', '#E69F00', '#000000'
    ]),
}

SCIENCE_DOUBLE_COLUMN = {**SCIENCE_SINGLE_COLUMN,
    'figure.figsize': (4.53, 3.50),
}

# 字体组合建议（Science推荐）
# 标题: Helvetica Bold 8pt
# 轴标签: Helvetica 7pt
# 刻度标签: Helvetica 6pt
# 图例: Helvetica 6pt
```

---

## 3. Elsevier 预设 | Elsevier Preset

**适用期刊**：The Lancet, Cell, Joule, Biomaterials 等Elsevier旗下期刊。

**规范要点**：
- 单栏 90mm (3.54 inch)，双栏 190mm (7.48 inch)
- 字号略大于Nature（Elsevier指南通常要求≥6pt）
- 大多数期刊接受 Helvetica / Arial

```python
ELSEVIER_SINGLE_COLUMN = {
    # === 图形尺寸 ===
    'figure.figsize': (3.54, 2.80),
    'figure.dpi': 600,
    'savefig.dpi': 600,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,

    # === 字体设置 ===
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 8,
    'axes.labelsize': 8,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'legend.title_fontsize': 7.5,

    # === 线宽与标记 ===
    'axes.linewidth': 0.6,
    'grid.linewidth': 0.4,
    'lines.linewidth': 1.2,
    'lines.markersize': 5,
    'lines.markeredgewidth': 0.6,

    # === 刻度 ===
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'xtick.major.pad': 3,
    'ytick.major.pad': 3,

    # === 图例 ===
    'legend.frameon': False,
    'legend.handlelength': 1.2,
    'legend.handletextpad': 0.5,
    'legend.borderpad': 0.3,
    'legend.labelspacing': 0.3,

    # === 颜色 ===
    'axes.prop_cycle': plt.cycler('color', [
        '#0072BD', '#D95319', '#EDB120', '#7E2F8E',
        '#77AC30', '#4DBEEE', '#A2142F', '#999999'
    ]),
}

ELSEVIER_DOUBLE_COLUMN = {**ELSEVIER_SINGLE_COLUMN,
    'figure.figsize': (7.48, 5.00),
}
```

---

## 4. 中文学报预设 | Chinese Journal Preset

**适用期刊**：各大学学报、中国科技期刊（GB/T 7713-1987 论文编写规范）。

**规范要点**：
- 单栏 80mm (3.15 inch)，双栏 160mm (6.30 inch)
- 中文字体：宋体（正文）、黑体（标题）
- 因 matplotlib 中文渲染限制，推荐使用 SimHei / Microsoft YaHei
- 字号：正文小五号（9pt）或五号（10.5pt），图表内可适当缩小

```python
import matplotlib

# 中文字体检测与设置
def setup_chinese_font():
    """自动检测并设置中文字体。"""
    import matplotlib.font_manager as fm
    available_fonts = [f.name for f in fm.fontManager.ttflist]

    chinese_fonts = ['SimHei', 'Microsoft YaHei', 'SimSun',
                     'WenQuanYi Micro Hei', 'Noto Sans CJK SC',
                     'Source Han Sans SC', 'STSong', 'KaiTi',
                     'Heiti SC']

    for font in chinese_fonts:
        if font in available_fonts:
            return font
    # 如果没有中文字体，回退到默认
    print("Warning: No Chinese font found. Falling back to default.")
    return 'sans-serif'


CHINESE_JOURNAL_SINGLE = {
    # === 图形尺寸 ===
    'figure.figsize': (3.15, 2.50),
    'figure.dpi': 600,
    'savefig.dpi': 600,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,

    # === 字体设置 ===
    'font.family': 'sans-serif',
    'font.sans-serif': ['SimHei', 'Microsoft YaHei', 'DejaVu Sans'],
    'font.size': 8,                       # 基础字号
    'axes.labelsize': 8,                  # 轴标签
    'axes.titlesize': 9,                  # 图标题
    'xtick.labelsize': 7,                 # 刻度标签
    'ytick.labelsize': 7,
    'legend.fontsize': 7,                 # 图例
    'legend.title_fontsize': 7.5,

    # === 线宽与标记 ===
    'axes.linewidth': 0.6,
    'grid.linewidth': 0.4,
    'lines.linewidth': 1.0,
    'lines.markersize': 4,
    'lines.markeredgewidth': 0.5,

    # === 刻度 ===
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.major.size': 2.5,
    'ytick.major.size': 2.5,
    'xtick.major.pad': 2.5,
    'ytick.major.pad': 2.5,

    # === 图例 ===
    'legend.frameon': False,
    'legend.handlelength': 1.0,
    'legend.handletextpad': 0.5,
    'legend.borderpad': 0.3,

    # === 颜色（适合中文期刊黑白印刷） ===
    'axes.prop_cycle': plt.cycler('color', [
        '#000000', '#666666', '#333333', '#999999',
        '#CCCCCC', '#1A1A1A', '#808080', '#4D4D4D'
    ]),
}

CHINESE_JOURNAL_DOUBLE = {**CHINESE_JOURNAL_SINGLE,
    'figure.figsize': (6.30, 4.00),
}
```

---

## 5. 统一预设加载器 | Unified Preset Loader

```python
def load_journal_preset(journal, column='single'):
    """
    加载期刊尺寸预设。

    Parameters
    ----------
    journal : str
        'nature' | 'science' | 'elsevier' | 'chinese'
    column : str
        'single' | 'double'

    Examples
    --------
    >>> load_journal_preset('nature', 'single')
    >>> load_journal_preset('elsevier', 'double')
    """
    ALL_PRESETS = {
        ('nature', 'single'): NATURE_SINGLE_COLUMN,
        ('nature', 'double'): NATURE_DOUBLE_COLUMN,
        ('science', 'single'): SCIENCE_SINGLE_COLUMN,
        ('science', 'double'): SCIENCE_DOUBLE_COLUMN,
        ('elsevier', 'single'): ELSEVIER_SINGLE_COLUMN,
        ('elsevier', 'double'): ELSEVIER_DOUBLE_COLUMN,
        ('chinese', 'single'): CHINESE_JOURNAL_SINGLE,
        ('chinese', 'double'): CHINESE_JOURNAL_DOUBLE,
    }
    key = (journal.lower(), column.lower())
    if key not in ALL_PRESETS:
        raise ValueError(f"Unknown preset: {journal}/{column}")

    rcParams.update(ALL_PRESETS[key])
    figsize = ALL_PRESETS[key]['figure.figsize']
    print(f"Applied preset: {journal} {column}-column "
          f"({figsize[0]*25.4:.0f}mm × {figsize[1]*25.4:.0f}mm)")
```

---

## 6. 快速参考 | Quick Reference

```python
# === 最简用法：一行应用预设 ===

# Nature 单栏（89mm）
load_journal_preset('nature', 'single')

# Science 双栏（115mm）
load_journal_preset('science', 'double')

# Elsevier 单栏（90mm）
load_journal_preset('elsevier', 'single')

# 中文学报单栏（80mm）
load_journal_preset('chinese', 'single')
```

---

## 7. 临时预设（不修改全局）| Temporary Preset (Context Manager)

```python
from contextlib import contextmanager

@contextmanager
def journal_style(journal, column='single'):
    """临时应用期刊样式，退出后自动恢复。"""
    import copy
    original = copy.deepcopy(dict(rcParams))
    try:
        load_journal_preset(journal, column)
        yield
    finally:
        rcParams.update(original)

# 使用示例
with journal_style('nature', 'single'):
    fig, ax = plt.subplots()
    ax.bar(['A', 'B'], [1, 2])
    fig.savefig('nature_figure.pdf')
# 退出后 rcParams 自动恢复
```
