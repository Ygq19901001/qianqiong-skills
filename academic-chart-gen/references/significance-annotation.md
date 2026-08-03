# 统计显著性自动标注系统 | Significance Annotation System

> 所有示例使用虚构数据。All examples use synthetic datasets.

---

## 概述 | Overview

统计显著性标注是学术数据图的关键组成部分。本系统提供完整的Python实现，支持自动计算p值并生成出版质量的显著性标注（星号 + 括号）。

---

## 1. 显著性等级 | Significance Levels

| 标注 | 含义 | p值范围 | 数学符号 |
|------|------|---------|---------|
| `***` | 极显著 | p < 0.001 | — |
| `**` | 非常显著 | p < 0.01 | — |
| `*` | 显著 | p < 0.05 | — |
| `ns` | 不显著 | p ≥ 0.05 | (not significant) |

---

## 2. 核心标注函数 | Core Annotation Functions

### 2.1 显著性字符串生成

```python
import numpy as np
from scipy import stats

def get_significance_label(p_value):
    """
    将p值转换为显著性标注字符串。

    Parameters
    ----------
    p_value : float
        来自统计检验的p值

    Returns
    -------
    str
        显著性标注: '***', '**', '*', 'ns'
    """
    if p_value < 0.001:
        return '***'
    elif p_value < 0.01:
        return '**'
    elif p_value < 0.05:
        return '*'
    else:
        return 'ns'

def get_significance_label_extended(p_value):
    """
    扩展版：包含p值精度的显著性标注

    Returns
    -------
    str
        如 'p=0.003**', 'p=0.041*', 'p=0.213ns'
    """
    sig = get_significance_label(p_value)
    if p_value < 0.001:
        p_str = f'p<0.001'
    elif p_value < 0.0001:
        p_str = f'p<0.0001'
    else:
        p_str = f'p={p_value:.3f}'
    return f'{p_str} {sig}' if sig != 'ns' else f'{p_str} (ns)'
```

### 2.2 显著性括号绘制

```python
def draw_significance_bracket(ax, x1, x2, y_base, height,
                              sig_text, color='black', fontsize=7,
                              linewidth=0.8, tip_length=0.02):
    """
    在matplotlib轴上绘制组间显著性括号。

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        目标轴对象
    x1, x2 : float
        两个待比较组的x坐标位置
    y_base : float
        括号起始的y坐标
    height : float
        括号的高度偏移量
    sig_text : str
        显著性标注文本 ('***', '**', '*', 'ns')
    color : str
        括号和文本颜色
    fontsize : int
        标注文本字体大小
    linewidth : float
        括号线宽
    tip_length : float
        垂直挂钩的长度（数据坐标）
    """
    # 水平括号线
    ax.plot([x1, x2], [y_base, y_base],
            color=color, linewidth=linewidth, clip_on=False)
    # 左侧垂直挂钩
    ax.plot([x1, x1], [y_base - tip_height, y_base],
            color=color, linewidth=linewidth, clip_on=False)
    # 右侧垂直挂钩
    ax.plot([x2, x2], [y_base - tip_height, y_base],
            color=color, linewidth=linewidth, clip_on=False)
    # 显著性文字
    ax.text((x1 + x2) / 2, y_base + tip_height * 0.3,
            sig_text, ha='center', va='bottom',
            fontsize=fontsize, fontweight='bold', color=color,
            clip_on=False)


def auto_significance_brackets(ax, data_dict, group_names, x_positions,
                                max_y, test='ttest', correction='bonferroni',
                                bar_spacing=0.15):
    """
    自动执行所有组间比较，在图上绘制显著性括号。

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        目标轴
    data_dict : dict
        {group_name: np.array} 各组数据
    group_names : list
        组名列表（对应x轴标签）
    x_positions : list
        各组在x轴上的位置
    max_y : float
        y轴最大值（数据坐标，用于确定括号起始高度）
    test : str
        'ttest' | 'mannwhitney' | 'wilcoxon'
    correction : str
        'bonferroni' | 'holm' | 'none'
    bar_spacing : float
        多层括号的垂直间距（数据坐标的分数）
    """
    from itertools import combinations
    from statsmodels.stats.multitest import multipletests

    n_groups = len(group_names)
    pairs = list(combinations(range(n_groups), 2))

    # 执行所有两两检验
    p_values = []
    for i, j in pairs:
        if test == 'ttest':
            _, p = stats.ttest_ind(data_dict[group_names[i]],
                                   data_dict[group_names[j]])
        elif test == 'mannwhitney':
            _, p = stats.mannwhitneyu(data_dict[group_names[i]],
                                      data_dict[group_names[j]])
        p_values.append(p)

    # 多重比较校正
    if correction in ('bonferroni', 'holm'):
        alpha = 0.05
        reject, p_corrected, _, _ = multipletests(p_values, alpha=alpha,
                                                   method=correction)
        final_p = p_corrected
    else:
        final_p = p_values

    # 按p值排序（最显著的画在最上面）
    sorted_indices = np.argsort(final_p)
    y_range = max_y * 0.02

    # 避免括号重叠：给每层括号分配不同的y层级
    used_levels = {}

    for rank, pair_idx in enumerate(sorted_indices):
        i, j = pairs[pair_idx]
        p = final_p[pair_idx]
        sig = get_significance_label(p)

        if sig == 'ns':
            continue  # 跳过非显著的比较（可选）

        x1, x2 = x_positions[i], x_positions[j]

        # 分配y层级
        key = (min(i, j), max(i, j))
        level = 0
        while key in used_levels:
            level += 1
        used_levels[key] = level

        bracket_y = max_y + bar_spacing * (level + 1) * y_range * 10
        draw_significance_bracket(ax, x1, x2, bracket_y,
                                  y_range * 0.5, sig)
```

---

## 3. 支持的统计检验 | Supported Statistical Tests

### 3.1 独立样本t检验

```python
# ========== 虚构数据 ==========
np.random.seed(42)
group_a = np.random.normal(5.2, 1.1, 30)
group_b = np.random.normal(3.8, 0.9, 30)

# t检验
t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"t({len(group_a)+len(group_b)-2}) = {t_stat:.2f}, "
      f"p = {p_value:.4f}, {get_significance_label(p_value)}")
# 输出: t(58) = 5.38, p = 0.0000, ***
```

### 3.2 配对t检验

```python
# ========== 虚构数据：干预前后 ==========
np.random.seed(42)
pre = np.random.normal(5.0, 1.0, 25)
post = pre - np.random.normal(1.5, 0.8, 25)  # 干预后降低

t_stat, p_value = stats.ttest_rel(pre, post)
print(f"Paired t = {t_stat:.2f}, {get_significance_label_extended(p_value)}")
```

### 3.3 单因素方差分析 (One-way ANOVA)

```python
# ========== 虚构数据：三种处理 ==========
np.random.seed(42)
group1 = np.random.normal(5.0, 1.0, 20)
group2 = np.random.normal(4.2, 1.0, 20)
group3 = np.random.normal(3.8, 1.0, 20)

f_stat, p_value = stats.f_oneway(group1, group2, group3)
print(f"F(2,57) = {f_stat:.2f}, {get_significance_label_extended(p_value)}")
```

### 3.4 Mann-Whitney U检验 (非参数两样本)

```python
# ========== 虚构数据：非正态分布 ==========
np.random.seed(42)
non_normal_a = np.random.exponential(2.0, 30)
non_normal_b = np.random.exponential(2.8, 30)

u_stat, p_value = stats.mannwhitneyu(non_normal_a, non_normal_b,
                                     alternative='two-sided')
print(f"U = {u_stat:.0f}, {get_significance_label_extended(p_value)}")
```

### 3.5 Kruskal-Wallis检验 (非参数多样本)

```python
# ========== 虚构数据 ==========
h_stat, p_value = stats.kruskal(group1, group2, group3)
print(f"H = {h_stat:.2f}, {get_significance_label_extended(p_value)}")
```

### 3.6 卡方检验

```python
# ========== 虚构数据：2×2列联表 ==========
# 观察值：[[治疗有效, 无效],
#          [治疗无效, 有效]]
observed = np.array([[42, 18],
                     [25, 35]])

chi2, p_value, dof, expected = stats.chi2_contingency(observed)
print(f"χ²({dof}) = {chi2:.2f}, {get_significance_label_extended(p_value)}")
```

---

## 4. 多重比较校正 | Multiple Comparison Correction

### 4.1 Bonferroni校正

```python
from statsmodels.stats.multitest import multipletests

# ========== 虚构数据：4组，6对比较 ==========
np.random.seed(42)
groups_data = {
    'A': np.random.normal(5.0, 1.0, 20),
    'B': np.random.normal(4.5, 1.0, 20),
    'C': np.random.normal(4.0, 1.0, 20),
    'D': np.random.normal(3.5, 1.0, 20),
}

from itertools import combinations
group_names = list(groups_data.keys())
pairs = list(combinations(group_names, 2))

# 每对做t检验，收集p值
raw_pvalues = []
comparison_labels = []
for g1, g2 in pairs:
    _, p = stats.ttest_ind(groups_data[g1], groups_data[g2])
    raw_pvalues.append(p)
    comparison_labels.append(f'{g1} vs {g2}')

# Bonferroni校正
reject_bonf, p_bonf, _, _ = multipletests(raw_pvalues, alpha=0.05,
                                          method='bonferroni')

# Holm校正（功效更高）
reject_holm, p_holm, _, _ = multipletests(raw_pvalues, alpha=0.05,
                                          method='holm')

# 打印对比结果
print("=" * 70)
print(f"{'Comparison':<12} {'p_raw':>8} {'p_bonf':>8} {'p_holm':>8} "
      f"{'Bonf':>6} {'Holm':>6}")
print("-" * 70)
for i, (label, p_raw, p_b, p_h, r_b, r_h) in enumerate(
    zip(comparison_labels, raw_pvalues, p_bonf, p_holm, reject_bonf, reject_holm)):
    print(f"{label:<12} {p_raw:>8.4f} {p_b:>8.4f} {p_h:>8.4f} "
          f"{'**' if r_b else 'ns':>6} {'**' if r_h else 'ns':>6}")
```

### 4.2 Tukey HSD事后检验

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ========== 虚构数据 ==========
all_data = np.concatenate([groups_data[g] for g in group_names])
all_labels = np.concatenate([[g]*20 for g in group_names])

tukey_result = pairwise_tukeyhsd(all_data, all_labels, alpha=0.05)
print(tukey_result)
```

---

## 5. 完整示例：带显著性标注的分组柱状图 | Complete Example

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from itertools import combinations
from statsmodels.stats.multitest import multipletests

plt.rcParams.update({
    'figure.dpi': 600, 'font.size': 7, 'font.family': 'sans-serif'
})

# ========== 虚构数据：四种培养基配方对细胞增殖的影响 ==========
np.random.seed(2024)
groups = {
    'Standard': np.random.normal(1.00, 0.12, 15),
    'Formula-X': np.random.normal(1.35, 0.15, 15),
    'Formula-Y': np.random.normal(1.28, 0.13, 15),
    'Formula-Z': np.random.normal(1.52, 0.18, 15),
}

group_names = list(groups.keys())
n = len(group_names)
means = [np.mean(groups[g]) for g in group_names]
sems = [stats.sem(groups[g]) for g in group_names]
colors = ['#D1E5F0', '#92C5DE', '#4393C3', '#2166AC']

fig, ax = plt.subplots(figsize=(4, 3.5))
x_pos = np.arange(n)

bars = ax.bar(x_pos, means, yerr=sems, capsize=4, color=colors,
              edgecolor='white', linewidth=0.5, width=0.6)

# 两两比较 + Bonferroni
pairs = list(combinations(range(n), 2))
raw_p = []
for i, j in pairs:
    _, p = stats.ttest_ind(groups[group_names[i]], groups[group_names[j]])
    raw_p.append(p)
_, p_corr, _, _ = multipletests(raw_p, alpha=0.05, method='bonferroni')

# 绘制显著性括号
max_y = max(means) + max(sems)

def get_sig(p):
    if p < 0.001: return '***'
    elif p < 0.01: return '**'
    elif p < 0.05: return '*'
    else: return 'ns'

def add_bracket(ax, x1, x2, y, h, text):
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], 'k-', lw=0.7, clip_on=False)
    ax.text((x1+x2)/2, y+h, text, ha='center', fontsize=6.5, fontweight='bold')

level = 0
bracket_heights = {}
for idx, ((i, j), p) in enumerate(zip(pairs, p_corr)):
    sig = get_sig(p)
    if sig == 'ns':
        continue
    key = (min(i,j), max(i,j))
    if key not in bracket_heights:
        bracket_heights[key] = level
        level += 1
    lvl = bracket_heights[key]
    y_pos = max_y + 0.05 + lvl * 0.08
    add_bracket(ax, x_pos[i], x_pos[j], y_pos, 0.03, sig)

ax.set_xticks(x_pos)
ax.set_xticklabels(group_names, rotation=25, ha='right')
ax.set_ylabel('Cell Proliferation (Fold Change)')
ax.set_ylim(0, max_y + 0.05 + level * 0.08 + 0.08)
ax.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.savefig('bar_with_full_significance.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 6. ANOVA + 事后检验的标注策略 | ANOVA + Post-hoc Strategy

```
流程：
1. 执行整体ANOVA
   ├─ 不显著(p≥0.05) → 只标注整体ANOVA的F值和p值，不做事后比较
   └─ 显著(p<0.05) → 继续
       2. 执行事后检验(Tukey HSD / Bonferroni / Holm)
       3. 在图上标注显著的组间比较
```

```python
def annotate_anova_posthoc(ax, groups_dict, x_positions, test_function=stats.ttest_ind,
                           correction='bonferroni'):
    """
    完整流程：ANOVA → 事后检验 → 显著性括号。

    Returns
    -------
    dict
        {'anova_F': float, 'anova_p': float, 'significant_pairs': [...], 'p_values': [...]}
    """
    # Step 1: 整体ANOVA
    group_data = list(groups_dict.values())
    f_stat, p_anova = stats.f_oneway(*group_data)

    if p_anova >= 0.05:
        # ANOVA不显著，只标注全局结果
        ax.text(0.5, 1.02, f'ANOVA: F={f_stat:.2f}, p={p_anova:.3f} (ns)',
                transform=ax.transAxes, ha='center', fontsize=6.5, style='italic')
        return {'anova_F': f_stat, 'anova_p': p_anova, 'significant_pairs': []}

    # Step 2: 事后检验
    group_names = list(groups_dict.keys())
    pairs = list(combinations(range(len(group_names)), 2))
    raw_p = [test_function(groups_dict[group_names[i]],
                          groups_dict[group_names[j]])[1]
             for i, j in pairs]

    _, p_corr, _, _ = multipletests(raw_p, alpha=0.05, method=correction)

    # Step 3: 标注
    ax.text(0.5, 1.02, f'ANOVA: F={f_stat:.2f}, p={p_anova:.4f}{get_significance_label(p_anova)}',
            transform=ax.transAxes, ha='center', fontsize=6.5, style='italic')

    return {
        'anova_F': f_stat,
        'anova_p': p_anova,
        'significant_pairs': [(group_names[i], group_names[j])
                               for (i, j), p in zip(pairs, p_corr) if p < 0.05],
        'p_values': p_corr
    }
```

---

## 7. 最佳实践 | Best Practices

1. **始终报告精确p值**：除了星号外，建议在图注或图题中给出精确p值（如 p=0.032）。
2. **多重比较必须校正**：3组及以上比较时，必须使用Bonferroni、Holm或Tukey校正。
3. **非正态用非参数**：Shapiro-Wilk检验判断正态性，非正态用Mann-Whitney或Kruskal-Wallis。
4. **标注方向**：括号应简洁，不遮挡数据点；多个括号时分层错开。
5. **ns标注策略**：一般只标注显著的比较；如需标注ns，建议在图注中说明"n.s., not significant"。
