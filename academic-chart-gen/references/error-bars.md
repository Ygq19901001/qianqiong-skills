# 误差线完整指南 | Error Bars Guide

> 所有示例使用虚构数据。All examples use synthetic datasets.

---

## 概述 | Overview

误差线（Error Bars）是学术数据图中传播离散度的关键元素。选择合适的误差线类型直接影响读者对数据变异性的理解。本指南系统阐述三种主流误差线并给出选择和绘制方案。

---

## 1. 三种误差线对比 | Three Error Bar Types

| 误差线类型 | 全称 | 公式 | 反映内容 | 典型用途 |
|-----------|------|------|---------|---------|
| **SD** | Standard Deviation | $\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}$ | 样本数据的离散程度 | 描述性统计、质量控制 |
| **SEM** | Standard Error of Mean | $SEM = \frac{SD}{\sqrt{n}}$ | 均值估计的精确度 | 推断统计、组间比较 |
| **CI** | Confidence Interval (95%) | $\bar{x} \pm t_{0.025, n-1} \times SEM$ | 总体均值所在的范围 | 推断统计、临床研究 |

---

## 2. 选择依据 | Selection Criteria

### 2.1 决策流程图

```
需要展示什么？
├─ 展示数据本身的分布宽度 → 选 SD
│   ├─ 样本量 < 10 → SD（样本量小时SEM不可靠）
│   └─ 样本量 ≥ 10 → SD 或 SEM 均可
├─ 展示均值估计的精确度 → 选 SEM
│   ├─ 多组比较（柱状图/折线图） → SEM + 星号显著性
│   └─ 样本量大（n>30） → SEM
└─ 展示总体均值的可能范围 → 选 95% CI
    ├─ 临床研究 → CI（必选，CONSORT规范）
    ├─ 森林图/Meta分析 → CI
    └─ 样本量 > 30 → CI最稳定
```

### 2.2 期刊偏好

| 期刊类型 | 推荐 | 备注 |
|---------|------|------|
| 基础研究（Nature/Science/Cell） | SEM | 标准做法，但也接受SD |
| 临床研究（NEJM/Lancet/JAMA） | 95% CI | 强制性要求 |
| 心理学/社会科学 | SEM 或 95% CI | APA格式偏好CI |
| 中文学报 | SD 或 SEM（图注中说明） | GB/T规范无强制性要求 |
| 工程类期刊 | SD | 展示工艺稳定性 |

### 2.3 样本量考量

| 样本量 | 建议 |
|--------|------|
| n < 10 | 展示全部数据点 + 均值线，避免仅用误差线 |
| 10 ≤ n < 30 | SD 或 SEM均可，必须在图注中明确说明 |
| n ≥ 30 | SEM或95% CI均可，95%CI会收敛到±1.96×SEM |

---

## 3. Python实现 | Python Implementation

### 3.1 三种误差线的计算

```python
import numpy as np
from scipy import stats

def compute_error_measures(data):
    """
    计算一组数据的三种误差度量。

    Parameters
    ----------
    data : array-like
        原始数据

    Returns
    -------
    dict
        {'sd': float, 'sem': float, 'ci95_low': float, 'ci95_high': float}
    """
    n = len(data)
    mean = np.mean(data)
    sd = np.std(data, ddof=1)  # 样本标准差
    sem = sd / np.sqrt(n)      # 标准误

    # 95% 置信区间 (t分布)
    ci_radius = stats.t.ppf(0.975, n-1) * sem

    return {
        'mean': mean,
        'sd': sd,
        'sem': sem,
        'ci95_low': mean - ci_radius,
        'ci95_high': mean + ci_radius,
        'ci95_radius': ci_radius,
        'n': n,
    }
```

### 3.2 分组数据批量计算

```python
import pandas as pd

def compute_group_error_measures(df, x_column, y_column, error_type='sem'):
    """
    按分组计算各组的误差度量。

    Parameters
    ----------
    df : pd.DataFrame
        数据框
    x_column : str
        分组变量列名
    y_column : str
        数值变量列名
    error_type : str
        'sd' | 'sem' | 'ci95'

    Returns
    -------
    pd.DataFrame
        含 mean, error_low, error_high, n 列
    """
    result = df.groupby(x_column)[y_column].agg(
        mean='mean',
        sd=lambda x: np.std(x, ddof=1),
        n='count'
    ).reset_index()

    result['sem'] = result['sd'] / np.sqrt(result['n'])

    if error_type == 'sd':
        result['error_low'] = result['sd']
        result['error_high'] = result['sd']
        result['error_label'] = 'SD'
    elif error_type == 'sem':
        result['error_low'] = result['sem']
        result['error_high'] = result['sem']
        result['error_label'] = 'SEM'
    elif error_type == 'ci95':
        # 使用t分布临界值
        t_crit = [stats.t.ppf(0.975, max(n-1, 1)) for n in result['n']]
        ci_radius = t_crit * result['sem']
        result['error_low'] = result['mean'] - ci_radius
        result['error_high'] = result['mean'] + ci_radius
        result['error_label'] = '95% CI'

    return result
```

---

## 4. 完整绘图示例 | Complete Plotting Examples

### 4.1 三元组对比：同一数据用SD/SEM/CI绘制

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.rcParams.update({
    'figure.dpi': 600, 'font.size': 7, 'font.family': 'sans-serif'
})

# ========== 虚构数据：某实验材料在不同温度下的抗拉强度 ==========
np.random.seed(2024)
temperatures = ['20°C', '50°C', '80°C', '110°C']
n = 12

strength = {
    '20°C':  np.random.normal(42.5, 3.2, n),
    '50°C':  np.random.normal(40.1, 3.5, n),
    '80°C':  np.random.normal(35.8, 4.1, n),
    '110°C': np.random.normal(28.3, 5.0, n),
}

# 计算三种度量
results = {}
for error_type in ['sd', 'sem', 'ci95']:
    results[error_type] = {}
    for temp in temperatures:
        results[error_type][temp] = compute_error_measures(strength[temp])

# 三子图并排对比
fig, axes = plt.subplots(1, 3, figsize=(9, 3.5))

x = np.arange(len(temperatures))
colors_bar = ['#D1E5F0', '#92C5DE', '#4393C3', '#2166AC']

for ax_idx, (error_type, title) in enumerate(
    [('sd', 'Standard Deviation (SD)'),
     ('sem', 'Standard Error of Mean (SEM)'),
     ('ci95', '95% Confidence Interval (CI)')]):

    ax = axes[ax_idx]

    for i, temp in enumerate(temperatures):
        r = results[error_type][temp]
        if error_type == 'ci95':
            # CI不对称（上下不等）
            yerr = [[r['mean'] - r['ci95_low']], [r['ci95_high'] - r['mean']]]
        else:
            yerr = r[error_type]

        ax.bar(i, r['mean'], yerr=yerr, color=colors_bar[i],
               capsize=4, edgecolor='white', linewidth=0.5, width=0.6)

        # 标注样本量
        ax.text(i, r['mean'] + yerr if not isinstance(yerr, list) else r['ci95_high'],
                f'n={n}', ha='center', fontsize=5, color='#666')

    ax.set_xticks(x)
    ax.set_xticklabels(temperatures)
    ax.set_title(title, fontsize=7.5, fontweight='bold')
    ax.set_ylabel('Tensile Strength (MPa)')
    ax.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.savefig('error_bar_comparison.png', dpi=600, bbox_inches='tight')
plt.show()
```

### 4.2 折线图中的CI带

```python
# ========== 虚构数据：药物浓度随时间变化 ==========
np.random.seed(2024)
time_points = np.array([0, 2, 4, 6, 8, 12, 24])
n_subjects = 15

# 模拟药代动力学曲线
conc_a = 50 * np.exp(-0.15 * time_points)
conc_b = 60 * np.exp(-0.22 * time_points)

# 每个时间点的模拟数据
all_conc_a = np.array([np.random.normal(c, c*0.12, n_subjects) for c in conc_a])
all_conc_b = np.array([np.random.normal(c, c*0.15, n_subjects) for c in conc_b])

# 计算均值+SEM和95%CI
def compute_series(data_matrix, n_subjects):
    means = data_matrix.mean(axis=1)
    sems = data_matrix.std(axis=1, ddof=1) / np.sqrt(n_subjects)
    ci_radius = stats.t.ppf(0.975, n_subjects-1) * sems
    return means, sems, ci_radius

means_a, sems_a, ci_a = compute_series(all_conc_a, n_subjects)
means_b, sems_b, ci_b = compute_series(all_conc_b, n_subjects)

fig, ax = plt.subplots(figsize=(4, 3))

# SEM误差棒 + CI带
ax.fill_between(time_points, means_a - ci_a, means_a + ci_a,
                alpha=0.12, color='#2166AC', label='_nolegend_')
ax.errorbar(time_points, means_a, yerr=sems_a,
            fmt='o-', color='#2166AC', linewidth=1.5, markersize=5,
            capsize=3, label='Drug-X (SEM + 95%CI band)')

ax.fill_between(time_points, means_b - ci_b, means_b + ci_b,
                alpha=0.12, color='#B2182B', label='_nolegend_')
ax.errorbar(time_points, means_b, yerr=sems_b,
            fmt='s-', color='#B2182B', linewidth=1.5, markersize=5,
            capsize=3, label='Drug-Y (SEM + 95%CI band)')

ax.set_xlabel('Time (hours)')
ax.set_ylabel('Plasma Concentration (ng/mL)')
ax.legend(fontsize=5.5, frameon=False)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('line_with_ci_band.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 5. 图例/图注说明规范 | Caption Standards

### 5.1 中文论文图注规范

```
图X 各组抗拉强度比较（均值 ± SEM，n=12/组）
注：*** p<0.001, ** p<0.01, * p<0.05 vs 20°C组；误差线表示标准误（Standard Error of Mean）。
```

### 5.2 英文论文图注规范

```
Figure X. Tensile strength across temperature conditions (mean ± SEM, n=12 per group).
*** p<0.001, ** p<0.01, * p<0.05 vs. 20°C group by one-way ANOVA followed by Tukey's post-hoc test.
Error bars represent the standard error of the mean (SEM).
```

### 5.3 误差线图注模板

```python
# 误差线图注生成函数
def generate_caption(error_type, n_per_group, test_method='one-way ANOVA'):
    """
    生成标准的图注模板。
    """
    error_descriptions = {
        'sd': 'standard deviation (SD)',
        'sem': 'standard error of the mean (SEM)',
        'ci95': '95% confidence intervals (CI)',
    }

    if error_type == 'ci95':
        template = (
            f"Data are presented as mean with 95% confidence intervals "
            f"(n={n_per_group} per group). Statistical analysis was performed "
            f"using {test_method}."
        )
    else:
        template = (
            f"Data are presented as mean ± {error_descriptions[error_type]} "
            f"(n={n_per_group} per group). Statistical analysis was performed "
            f"using {test_method}. * p<0.05, ** p<0.01, *** p<0.001."
        )

    return template

# 使用示例
caption_en = generate_caption('sem', 15, 'one-way ANOVA with Tukey\'s HSD')
print(caption_en)
# Data are presented as mean ± standard error of the mean (SEM) (n=15 per group).
# Statistical analysis was performed using one-way ANOVA with Tukey's HSD.
# * p<0.05, ** p<0.01, *** p<0.001.
```

---

## 6. 常见误区 | Common Pitfalls

| 误区 | 正确做法 |
|------|---------|
| ❌ 用SEM但声称是SD | 必须明确在图注中标注误差线类型 |
| ❌ 小样本(n<5)用SEM | 小样本展示全部数据点（strip plot + 均值线） |
| ❌ 不同组用不同误差线类型 | 整个图统一误差线类型 |
| ❌ 误差线括号重叠 | 分层绘制或使用字母标注(a, b, c)代替括号 |
| ❌ CI计算用z分布（正常近似） | n<30时应用t分布计算CI |

---

## 7. 字母标注替代法 | Letter-Based Annotation

当组数较多时（4组及以上），显著性括号容易重叠混淆。替代方案是使用**字母标注**：

- 共享同一个字母的组之间无显著差异
- 字母不同的组之间有显著差异

```python
# ========== 字母标注示例 ==========
# 假设Tukey HSD结果：A组 ≠ B组 ≠ C组和D组（C=D）
letter_groups = {
    'Group A': 'a',
    'Group B': 'b',
    'Group C': 'c',
    'Group D': 'c',  # 与C无显著差异
}

# 在柱状图上方标注字母
for i, (group, letter) in enumerate(letter_groups.items()):
    ax.text(i, max_y + 0.05, letter, ha='center', fontsize=8, fontweight='bold')
```
