# 支持的图表类型 | Supported Chart Types

> 所有示例使用虚构数据。All examples use synthetic/fabricated datasets.

---

## 目录 | Index

1. [柱状图 (Bar Chart)](#1-柱状图-bar-chart)
2. [箱线图 (Box Plot)](#2-箱线图-box-plot)
3. [小提琴图 (Violin Plot)](#3-小提琴图-violin-plot)
4. [散点图 (Scatter Plot)](#4-散点图-scatter-plot)
5. [折线图 (Line Chart)](#5-折线图-line-chart)
6. [热力图 (Heatmap)](#6-热力图-heatmap)
7. [森林图 (Forest Plot)](#7-森林图-forest-plot)
8. [ROC曲线 (ROC Curve)](#8-roc曲线-roc-curve)
9. [Bland-Altman图 (Bland-Altman Plot)](#9-bland-altman图-bland-altman-plot)
10. [雷达图 (Radar Chart)](#10-雷达图-radar-chart)

---

## 1. 柱状图 (Bar Chart)

**适用数据类型**：分类变量 × 连续变量（均值比较）

**学术场景**：实验组与对照组疗效对比、不同条件下性能指标比较、问卷调查得分对比

**显著性标注方法**：
- 两两比较：t检验 + Bonferroni校正
- 多组比较：单因素ANOVA + Tukey HSD事后检验
- 星号标注：p < 0.05 (*)、p < 0.01 (**)、p < 0.001 (***)

### 1.1 分组柱状图 + 误差线 + 显著性星号

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import rcParams

rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'axes.labelsize': 7,
    'axes.titlesize': 8,
    'font.family': 'sans-serif',
})

# ========== 虚构数据：三种药物干预前后生物标志物变化 ==========
np.random.seed(2024)
groups = ['Vehicle', 'Drug-Low', 'Drug-High']
categories = ['Pre-treatment', 'Post-treatment']
n = 15  # 每组样本量

data = {}
for g in groups:
    data[g] = {}
    for c in categories:
        if g == 'Vehicle':
            loc = 5.0 if c == 'Pre-treatment' else 5.2
        elif g == 'Drug-Low':
            loc = 5.1 if c == 'Pre-treatment' else 3.8
        else:  # Drug-High
            loc = 4.9 if c == 'Pre-treatment' else 2.5
        data[g][c] = np.random.normal(loc, 0.6, n)

# 计算均值和SEM
means = {}
sems = {}
for g in groups:
    means[g] = [np.mean(data[g][c]) for c in categories]
    sems[g] = [stats.sem(data[g][c]) for c in categories]

# 绘图
fig, ax = plt.subplots(figsize=(3.5, 3))
x = np.arange(len(categories))
width = 0.22
colors = ['#D1E5F0', '#67A9CF', '#2166AC']

for i, g in enumerate(groups):
    offset = (i - 1) * width
    bars = ax.bar(x + offset, means[g], width, yerr=sems[g],
                  color=colors[i], capsize=3, edgecolor='white',
                  linewidth=0.5, label=g)

# 显著性自动标注
def add_significance_bracket(ax, x1, x2, y, h, sig_text, color='k'):
    """绘制显著性括号"""
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=color, lw=0.8, clip_on=False)
    ax.text((x1+x2)/2, y+h, sig_text, ha='center', va='bottom',
            fontsize=7, fontweight='bold', color=color)

def get_sig(p):
    if p < 0.001:
        return '***'
    elif p < 0.01:
        return '**'
    elif p < 0.05:
        return '*'
    else:
        return 'ns'

# 组间比较（Post-treatment: Vehicle vs Drug-High）
_, p_post = stats.ttest_ind(data['Vehicle']['Post-treatment'],
                             data['Drug-High']['Post-treatment'])
y_bar = max([means[g][1] + sems[g][1] for g in groups])
add_significance_bracket(ax, x[1]+width, x[1]-width, y_bar+0.1, 0.08,
                         get_sig(p_post))

# 组内比较（Drug-High: Pre vs Post）
_, p_within = stats.ttest_ind(data['Drug-High']['Pre-treatment'],
                               data['Drug-High']['Post-treatment'])
y_top = max(means['Drug-High'][0] + sems['Drug-High'][0],
            means['Drug-High'][1] + sems['Drug-High'][1])
add_significance_bracket(ax, x[0]-width, x[1]-width, y_top+0.2, 0.1,
                         get_sig(p_within))

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel('Biomarker Concentration\n(arbitrary units)')
ax.legend(frameon=False, fontsize=6)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('bar_chart_significance.png', dpi=600, bbox_inches='tight')
plt.show()
```

### 1.2 堆叠柱状图

```python
# ========== 虚构数据：不同材料成分比例 ==========
materials = ['Alloy-A', 'Alloy-B', 'Alloy-C', 'Alloy-D']
components = ['Component X', 'Component Y', 'Component Z']

np.random.seed(42)
proportions = np.random.dirichlet(np.ones(3), size=4) * 100

fig, ax = plt.subplots(figsize=(3.5, 3))
bottom = np.zeros(4)
colors_stack = ['#2166AC', '#67A9CF', '#D1E5F0']

for i, comp in enumerate(components):
    bars = ax.bar(materials, proportions[:, i], bottom=bottom,
                  color=colors_stack[i], label=comp, edgecolor='white', linewidth=0.5)
    # 添加百分比标注
    for j, (bar, val) in enumerate(zip(bars, proportions[:, i])):
        if val > 10:  # 只标注大于10%的
            ax.text(bar.get_x() + bar.get_width()/2, bottom[j] + val/2,
                    f'{val:.0f}%', ha='center', va='center', fontsize=5.5)
    bottom += proportions[:, i]

ax.set_ylabel('Composition (%)')
ax.legend(frameon=False, fontsize=6)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('bar_chart_stacked.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 2. 箱线图 (Box Plot)

**适用数据类型**：分类变量 × 连续变量（分布比较，非正态数据）

**学术场景**：生物标志物表达水平分布、算法性能的中位数比较、非正态数据的组间差异

**显著性标注方法**：
- Mann-Whitney U检验（两两比较）
- Kruskal-Wallis + Dunn事后检验（多组）
- 括号 + 星号标注在箱体上方

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'axes.labelsize': 7,
    'axes.titlesize': 8,
    'font.family': 'sans-serif',
})

# ========== 虚构数据：三种培养条件下细胞活力 ==========
np.random.seed(2024)
conditions = ['Normal', 'Hypoxia', 'Hypoxia+\nInhibitor']
n = 25

# 非正态分布数据（故意用偏态分布）
data_normal = np.random.lognormal(0.0, 0.15, n)
data_hypoxia = np.random.lognormal(-0.15, 0.25, n)
data_inhibitor = np.random.lognormal(0.2, 0.2, n)
all_data = [data_normal, data_hypoxia, data_inhibitor]

# 颜色
colors = ['#D1E5F0', '#67A9CF', '#2166AC']

fig, ax = plt.subplots(figsize=(3.5, 3))

# 绘制箱线图
bp = ax.boxplot(all_data, patch_artist=True, widths=0.5,
                medianprops={'color': 'black', 'linewidth': 1.2},
                flierprops={'marker': 'o', 'markerfacecolor': 'red',
                            'markersize': 3, 'alpha': 0.6},
                whiskerprops={'linewidth': 0.8},
                capprops={'linewidth': 0.8})

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

# 标注中位数数值
medians = [np.median(d) for d in all_data]
q25 = [np.percentile(d, 25) for d in all_data]
q75 = [np.percentile(d, 75) for d in all_data]

for i, (med, q1, q3) in enumerate(zip(medians, q25, q75)):
    ax.text(i+1, q3 + 0.02, f'M={med:.3f}', ha='center', fontsize=5.5, color='#333')
    ax.text(i+1, q1 - 0.04, f'Q1={q1:.3f}', ha='center', fontsize=5, color='#666')

# Mann-Whitney U检验
_, p_mw1 = stats.mannwhitneyu(data_normal, data_hypoxia)
_, p_mw2 = stats.mannwhitneyu(data_hypoxia, data_inhibitor)
_, p_mw3 = stats.mannwhitneyu(data_normal, data_inhibitor)

# 显著性括号
def get_sig(p):
    if p < 0.001: return '***'
    elif p < 0.01: return '**'
    elif p < 0.05: return '*'
    else: return 'ns'

def add_bracket(ax, x1, x2, y, h, text):
    ax.plot([x1, x1, x2, x2], [y, y+h*0.5, y+h*0.5, y], 'k-', lw=0.7)
    ax.text((x1+x2)/2, y+h*0.5, text, ha='center', fontsize=7, fontweight='bold')

y_max = max([max(d) for d in all_data])
add_bracket(ax, 1, 2, y_max+0.03, 0.04, get_sig(p_mw1))
add_bracket(ax, 2, 3, y_max+0.10, 0.04, get_sig(p_mw2))
add_bracket(ax, 1, 3, y_max+0.17, 0.04, get_sig(p_mw3))

ax.set_xticklabels(conditions)
ax.set_ylabel('Cell Viability (Fold Change)')
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('box_plot.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 3. 小提琴图 (Violin Plot)

**适用数据类型**：分类变量 × 连续变量（数据分布形态可视化）

**学术场景**：基因表达分布比较、多模态数据检测、样本量较大时的分布展示

**显著性标注方法**：t检验/ANOVA + 星号（同柱状图）

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats

rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'axes.labelsize': 7,
    'font.family': 'sans-serif',
})

# ========== 虚构数据：三种教学方法下学生成绩分布 ==========
np.random.seed(2024)
methods = ['Lecture', 'Flipped\nClassroom', 'Project-\nBased']
n = 50

# 不同分布形态：Lecture是正态，Flipped是宽分布，Project是双峰
scores_lecture = np.random.normal(72, 8, n)
scores_flipped = np.random.normal(78, 14, n)
scores_project = np.concatenate([
    np.random.normal(68, 5, n//2),
    np.random.normal(85, 6, n - n//2)
])

df = pd.DataFrame({
    'Score': np.concatenate([scores_lecture, scores_flipped, scores_project]),
    'Method': np.repeat(methods, n)
})

fig, ax = plt.subplots(figsize=(4, 3.5))

# 绘制小提琴图（内嵌箱线）
parts = ax.violinplot([scores_lecture, scores_flipped, scores_project],
                      positions=[1, 2, 3],
                      showmeans=False, showmedians=False,
                      widths=0.7)

colors = ['#D1E5F0', '#67A9CF', '#2166AC']
for i, (pc, color) in enumerate(zip(parts['bodies'], colors)):
    pc.set_facecolor(color)
    pc.set_alpha(0.7)
    pc.set_edgecolor('black')
    pc.set_linewidth(0.8)

# 内嵌箱线图
bp = ax.boxplot([scores_lecture, scores_flipped, scores_project],
                positions=[1, 2, 3], widths=0.15,
                patch_artist=True,
                medianprops={'color': 'black', 'linewidth': 1},
                flierprops={'marker': '.', 'markerfacecolor': 'black',
                            'markersize': 2, 'alpha': 0.4},
                zorder=10)

for patch in bp['boxes']:
    patch.set_facecolor('white')
    patch.set_alpha(0.6)

# ANOVA显著性
f_stat, p_anova = stats.f_oneway(scores_lecture, scores_flipped, scores_project)
sig_text = '***' if p_anova < 0.001 else '**' if p_anova < 0.01 else '*'
ax.text(2, 102, f'ANOVA p={p_anova:.3e}{sig_text}', ha='center',
        fontsize=6, style='italic')

ax.set_xticks([1, 2, 3])
ax.set_xticklabels(methods)
ax.set_ylabel('Score')
ax.set_ylim(35, 108)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('violin_plot.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 4. 散点图 (Scatter Plot)

**适用数据类型**：两个连续变量（相关性分析）

**学术场景**：基因表达相关性、技术重复一致性、剂量-反应关系

**显著性标注方法**：Pearson/Spearman相关系数 + R² + p值标注

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'axes.labelsize': 7,
    'font.family': 'sans-serif',
})

# ========== 虚构数据：PCR技术与新一代测序在基因表达定量的一致性 ==========
np.random.seed(42)
n = 40
x = np.random.uniform(2, 12, n)  # PCR Log2 expression
# 存在一定测量误差的相关数据
y = 0.85 * x + 1.2 + np.random.normal(0, 0.7, n)

# 添加2个离群点
x = np.append(x, [3.0, 10.0])
y = np.append(y, [1.0, 13.5])

fig, ax = plt.subplots(figsize=(3.5, 3))

# 散点 + 边缘密度
ax.scatter(x, y, c='#2166AC', s=30, alpha=0.6, edgecolors='white',
           linewidth=0.3, zorder=5)

# 线性回归
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
x_line = np.linspace(x.min(), x.max(), 100)
y_line = slope * x_line + intercept

ax.plot(x_line, y_line, '--', color='#B2182B', linewidth=1.2, label='Regression')
ax.fill_between(x_line,
                y_line - 1.96*std_err*np.sqrt(1/n + (x_line-x.mean())**2 /
                                              np.sum((x-x.mean())**2)),
                y_line + 1.96*std_err*np.sqrt(1/n + (x_line-x.mean())**2 /
                                              np.sum((x-x.mean())**2)),
                alpha=0.12, color='#B2182B')

# 标注统计量
stats_text = f'$r$ = {r_value:.3f}\n$R^2$ = {r_value**2:.3f}\n$p$ = {p_value:.2e}'
ax.text(0.05, 0.95, stats_text, transform=ax.transAxes,
        fontsize=7, va='top',
        bbox={'boxstyle': 'round,pad=0.3', 'fc': 'white', 'ec': '#ccc', 'alpha': 0.8})

# 等值线 (y=x) 作为参考
ax.axline((min(x.min(), y.min()), min(x.min(), y.min())), slope=1,
          color='gray', linestyle=':', linewidth=0.6, alpha=0.5)

ax.set_xlabel('PCR (Log2 Expression)')
ax.set_ylabel('NGS (Log2 Expression)')
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('scatter_regression.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 5. 折线图 (Line Chart)

**适用数据类型**：有序自变量 × 连续因变量（趋势分析）

**学术场景**：时间序列、剂量-反应关系、药物代谢动力学曲线

**显著性标注方法**：重复测量ANOVA或线性混合模型（图中标注整体趋势显著性）

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'axes.labelsize': 7,
    'font.family': 'sans-serif',
})

# ========== 虚构数据：两种处理条件下pH值随时间变化 ==========
np.random.seed(2024)
time_points = np.array([0, 5, 10, 15, 20, 25, 30])  # minutes
n_replicates = 10

# 处理A：pH先升后降
mean_a = np.array([7.0, 7.4, 7.8, 7.6, 7.3, 7.1, 7.0])
# 处理B：pH持续上升
mean_b = np.array([7.0, 7.1, 7.3, 7.6, 7.8, 7.9, 8.0])

sd = 0.15
means_a = mean_a + np.random.normal(0, 0.05, len(time_points))
means_b = mean_b + np.random.normal(0, 0.05, len(time_points))

# 计算SEM
sem_a = sd / np.sqrt(n_replicates)
sem_b = sd / np.sqrt(n_replicates)

# 95% CI
ci_a = 1.96 * sem_a
ci_b = 1.96 * sem_b

fig, ax = plt.subplots(figsize=(4, 3))

# 误差带 + 连线
ax.fill_between(time_points, means_a - ci_a, means_a + ci_a,
                alpha=0.15, color='#2166AC')
ax.errorbar(time_points, means_a, yerr=sem_a,
            fmt='o-', color='#2166AC', linewidth=1.5, markersize=5,
            capsize=3, capthick=0.8, label='Condition A',
            markerfacecolor='white', markeredgewidth=1)

ax.fill_between(time_points, means_b - ci_b, means_b + ci_b,
                alpha=0.15, color='#B2182B')
ax.errorbar(time_points, means_b, yerr=sem_b,
            fmt='s-', color='#B2182B', linewidth=1.5, markersize=5,
            capsize=3, capthick=0.8, label='Condition B',
            markerfacecolor='white', markeredgewidth=1)

# 图例中说明误差线的含义
from matplotlib.lines import Line2D
handles = [
    Line2D([0], [0], color='#2166AC', marker='o', markersize=5,
           markerfacecolor='white', linewidth=1.5, label='Condition A'),
    Line2D([0], [0], color='#B2182B', marker='s', markersize=5,
           markerfacecolor='white', linewidth=1.5, label='Condition B'),
]
legend_labels = ['Condition A (mean ± SEM)', 'Condition B (mean ± SEM)']
ax.legend(handles, legend_labels, frameon=False, fontsize=6)

ax.set_xlabel('Time (min)')
ax.set_ylabel('pH Value')
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('line_chart_error_band.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 6. 热力图 (Heatmap)

**适用数据类型**：矩阵数据（多变量相关性/表达量）

**学术场景**：相关性矩阵可视化、基因表达谱、组学数据聚类热图

**显著性标注方法**：相关系数 + p值星号标注在格子内

```python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist

rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'font.family': 'sans-serif',
})

# ========== 虚构数据：8个生理指标的相关性矩阵 ==========
np.random.seed(2024)
variables = ['BMI', 'SBP', 'DBP', 'Glucose', 'HDL', 'LDL', 'Trig', 'CRP']
n_samples = 100

# 生成具有内在相关结构的数据
cov = np.array([
    [1.0, 0.35, 0.28, 0.20, -0.15, 0.10, 0.18, 0.05],
    [0.35, 1.0, 0.65, 0.25, -0.05, 0.15, 0.20, 0.10],
    [0.28, 0.65, 1.0, 0.22, -0.08, 0.12, 0.15, 0.08],
    [0.20, 0.25, 0.22, 1.0, -0.30, 0.15, 0.40, 0.22],
    [-0.15, -0.05, -0.08, -0.30, 1.0, -0.20, -0.35, -0.18],
    [0.10, 0.15, 0.12, 0.15, -0.20, 1.0, 0.50, 0.08],
    [0.18, 0.20, 0.15, 0.40, -0.35, 0.50, 1.0, 0.15],
    [0.05, 0.10, 0.08, 0.22, -0.18, 0.08, 0.15, 1.0],
])
data_synth = np.random.multivariate_normal(np.zeros(8), cov, n_samples)
df_heatmap = pd.DataFrame(data_synth, columns=variables)

# 计算相关性矩阵
corr_matrix = df_heatmap.corr()

# 层次聚类
linkage_matrix = linkage(pdist(corr_matrix), method='average')
order = dendrogram(linkage_matrix, no_plot=True)['leaves']
corr_clustered = corr_matrix.iloc[order, order]

# 生成显著性标注矩阵
n_vars = len(variables)
annot_matrix = np.empty((n_vars, n_vars), dtype=object)
for i in range(n_vars):
    for j in range(n_vars):
        r = corr_clustered.iloc[i, j]
        stars = ''
        # 基于相关性大小的近似显著性
        t_stat = r * np.sqrt((n_samples - 2) / (1 - r**2))
        p = 2 * (1 - stats.t.cdf(abs(t_stat), n_samples - 2))
        if p < 0.001:
            stars = '***'
        elif p < 0.01:
            stars = '**'
        elif p < 0.05:
            stars = '*'
        annot_matrix[i, j] = f'{r:.2f}\n{stars}'

# 绘图
fig, ax = plt.subplots(figsize=(5.5, 5))
cmap = sns.diverging_palette(250, 15, s=75, l=40, n=11, center='light')

sns.heatmap(corr_clustered, annot=annot_matrix, fmt='',
            cmap=cmap, center=0, vmin=-1, vmax=1,
            square=True, linewidths=0.5, linecolor='white',
            cbar_kws={'shrink': 0.8, 'label': "Pearson's r"},
            xticklabels=corr_clustered.columns,
            yticklabels=corr_clustered.columns,
            ax=ax)

ax.set_title('Correlation Matrix with Clustering\n(* p<0.05, ** p<0.01, *** p<0.001)',
             fontsize=8, fontweight='bold', pad=12)

plt.tight_layout()
plt.savefig('heatmap_correlation.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 7. 森林图 (Forest Plot)

**适用数据类型**：Meta分析效应量（OR/RR/HR + 95%CI）

**学术场景**：系统评价/Meta分析、亚组分析、多中心研究汇总

**显著性标注方法**：95%CI是否跨越无效线（OR=1或MD=0）

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch

rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'font.family': 'sans-serif',
})

# ========== 虚构数据：某药物疗效的Meta分析森林图 ==========
# 假设10项研究的 OR 和 95% CI
studies = [
    'Smith et al. (2018)',
    'Johnson et al. (2019)',
    'Lee et al. (2019)',
    'Wang et al. (2020)',
    'Garcia et al. (2020)',
    'Kim et al. (2021)',
    'Chen et al. (2021)',
    'Patel et al. (2022)',
    'Brown et al. (2022)',
    'Davis et al. (2023)',
]

# 虚构效应量数据
or_values = np.array([0.82, 1.12, 0.68, 0.95, 0.55, 0.78, 1.25, 0.60, 0.72, 0.88])
ci_low = np.array([0.48, 0.58, 0.38, 0.40, 0.28, 0.42, 0.52, 0.30, 0.40, 0.44])
ci_high = np.array([1.40, 2.16, 1.22, 2.26, 1.08, 1.45, 3.01, 1.20, 1.30, 1.76])

# Meta分析合并效应量（随机效应）
pooled_or = 0.79
pooled_ci_low = 0.62
pooled_ci_high = 1.00

weights = np.array([8.5, 5.2, 12.1, 6.8, 15.3, 9.7, 4.1, 14.2, 11.8, 12.3])

fig, ax = plt.subplots(figsize=(5, 4.5))

# 无效线
ax.axvline(1.0, color='red', linestyle='--', linewidth=1.2, alpha=0.7, zorder=1)
ax.text(1.0, len(studies)+1.8, 'OR=1 (null)', ha='center',
        fontsize=6, color='red', alpha=0.8)

y_positions = list(range(len(studies), 0, -1))

for i, (study, or_val, low, high, w) in enumerate(
    zip(studies, or_values, ci_low, ci_high, weights)):
    y = y_positions[i]

    # CI线
    ax.plot([low, high], [y, y], '-', color='#333', linewidth=w/3+1)
    # OR点
    marker_size = np.sqrt(w) * 12
    ax.scatter(or_val, y, s=marker_size, c='#2166AC', zorder=5, edgecolors='white',
               linewidth=0.5)

    # OR和CI文本
    ax.text(4.0, y, f'{or_val:.2f} [{low:.2f}, {high:.2f}]',
            fontsize=5.5, va='center', fontfamily='monospace')
    # 权重
    ax.text(4.0, y-0.25, f'{w:.1f}%', fontsize=4.5, va='center', color='gray')

    # 研究名
    ax.text(-0.05, y, study, fontsize=5.5, va='center', ha='right')

# 合并效应量（菱形）
ax.plot([pooled_ci_low, pooled_or, pooled_ci_high, pooled_or, pooled_ci_low],
        [0.2, 0.6, 0.2, -0.2, 0.2],
        '-', color='#B2182B', linewidth=1.5)
ax.fill([pooled_ci_low, pooled_or, pooled_ci_high, pooled_or, pooled_ci_low],
        [0.2, 0.6, 0.2, -0.2, 0.2],
        color='#B2182B', alpha=0.5)
ax.text(4.0, 0.2, f'{pooled_or:.2f} [{pooled_ci_low:.2f}, {pooled_ci_high:.2f}]',
        fontsize=6, va='center', fontfamily='monospace', fontweight='bold')

# 标签
ax.text(-0.05, len(studies)+1, 'Study', fontsize=6.5, fontweight='bold', va='center',
        ha='right')
ax.text(4.0, len(studies)+1, 'OR [95% CI]', fontsize=6.5, fontweight='bold',
        va='center')

ax.set_xlim(-2.5, 6.5)
ax.set_ylim(-0.8, len(studies)+1.5)
ax.set_xscale('log')  # 对数尺度
ax.set_xlabel('Odds Ratio (log scale)', fontsize=6.5)
ax.spines[['top', 'right']].set_visible(False)
ax.set_yticks([])

plt.tight_layout()
plt.savefig('forest_plot.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 8. ROC曲线 (ROC Curve)

**适用数据类型**：二分类诊断/预测模型评价

**学术场景**：生物标志物诊断效能、机器学习分类器性能对比、临床预测模型评价

**显著性标注方法**：AUC值 + 95%CI（DeLong检验）+ 约登指数最佳截断点

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats, interp
from sklearn.metrics import roc_curve, auc, roc_auc_score

rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'font.family': 'sans-serif',
})

# ========== 虚构数据：三种诊断标志物的ROC比较 ==========
np.random.seed(2024)
n = 200

# 真实标签
y_true = np.concatenate([np.zeros(n//2), np.ones(n//2)])
np.random.shuffle(y_true)

# 三种标志物的预测分数（不同诊断效能）
# 标志物A：较好 (AUC≈0.85)
score_a = np.where(y_true == 1,
                   np.random.normal(0.8, 0.3, n//2),
                   np.random.normal(0.2, 0.2, n//2))
# 标志物B：中等 (AUC≈0.72)
score_b = np.where(y_true == 1,
                   np.random.normal(0.65, 0.35, n//2),
                   np.random.normal(0.3, 0.3, n//2))
# 标志物C：参考（随机）
score_c = np.random.uniform(0, 1, n)

fig, ax = plt.subplots(figsize=(3.5, 3.5))

colors_roc = ['#2166AC', '#67A9CF', '#999999']
marker_labels = ['Biomarker A', 'Biomarker B', 'Random']

for scores, color, label in zip([score_a, score_b, score_c], colors_roc, marker_labels):
    fpr, tpr, thresholds = roc_curve(y_true, scores)
    roc_auc = auc(fpr, tpr)

    # 计算AUC的95%CI（DeLong方法的近似）
    n_pos = np.sum(y_true)
    n_neg = len(y_true) - n_pos
    se_auc = np.sqrt((roc_auc*(1-roc_auc) + (n_pos-1)*(0.5-roc_auc)/(n-1) +
                       (n_neg-1)*(roc_auc-0.5)/(n-1)) / n)
    auc_ci_low = roc_auc - 1.96*se_auc
    auc_ci_high = roc_auc + 1.96*se_auc

    # 约登指数找最佳截断点
    youden = tpr - fpr
    best_idx = np.argmax(youden)

    ax.plot(fpr, tpr, '-', color=color, linewidth=1.5,
            label=f'{label} (AUC={roc_auc:.2f} [{auc_ci_low:.2f}-{auc_ci_high:.2f}])')

    # 标记最佳截断点
    if label != 'Random':
        ax.scatter(fpr[best_idx], tpr[best_idx], s=30, c=color, zorder=10,
                   edgecolors='white', linewidth=0.5)
        ax.annotate(f'Cut={thresholds[best_idx]:.2f}\nJ={youden[best_idx]:.2f}',
                    (fpr[best_idx], tpr[best_idx]),
                    xytext=(10, -10), textcoords='offset points',
                    fontsize=5, color=color,
                    arrowprops={'arrowstyle': '-', 'color': color, 'alpha': 0.5})

# 对角线
ax.plot([0, 1], [0, 1], 'k--', linewidth=0.8, alpha=0.4)

ax.set_xlabel('1 - Specificity (FPR)', fontsize=7)
ax.set_ylabel('Sensitivity (TPR)', fontsize=7)
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)
ax.legend(fontsize=5.5, loc='lower right', frameon=False)
ax.spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.savefig('roc_curve.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 9. Bland-Altman图 (Bland-Altman Plot)

**适用数据类型**：两种测量方法的一致性评价

**学术场景**：新方法与金标准的一致性验证、仪器比对、方法学评价

**显著性标注方法**：均值偏倚（bias）+ 95%一致性界限（LoA = bias ± 1.96×SD）

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'font.family': 'sans-serif',
})

# ========== 虚构数据：新型便携式血糖仪 vs 实验室标准方法 ==========
np.random.seed(2024)
n = 80

# 模拟实验室标准值
lab_values = np.random.uniform(3.0, 18.0, n)

# 便携式测量值（存在一定比例的误差）
true_error_pct = np.random.normal(0.03, 0.08, n)  # 平均高估3%
portable_values = lab_values * (1 + true_error_pct)

# 计算差值
diff = portable_values - lab_values
mean_vals = (portable_values + lab_values) / 2

# Bland-Altman统计量
bias = np.mean(diff)
sd_diff = np.std(diff, ddof=1)
loa_lower = bias - 1.96 * sd_diff
loa_upper = bias + 1.96 * sd_diff

# 95%置信区间
se_bias = sd_diff / np.sqrt(n)
ci_bias_low = bias - 1.96 * se_bias
ci_bias_high = bias + 1.96 * se_bias
se_loa = np.sqrt(3 * sd_diff**2 / n)
ci_loa_lower_low = loa_lower - 1.96 * se_loa
ci_loa_lower_high = loa_lower + 1.96 * se_loa
ci_loa_upper_low = loa_upper - 1.96 * se_loa
ci_loa_upper_high = loa_upper + 1.96 * se_loa

fig, ax = plt.subplots(figsize=(4.5, 3.5))

# 散点
ax.scatter(mean_vals, diff, c='#2166AC', s=25, alpha=0.5,
           edgecolors='white', linewidth=0.3, zorder=5)

# 均值偏倚线
ax.axhline(bias, color='#333', linewidth=1, linestyle='--')
ax.text(mean_vals.max()*0.98, bias + 0.02, f'Bias = {bias:.3f}',
        fontsize=6, ha='right', fontweight='bold')

# 95%一致限
ax.axhline(loa_upper, color='#B2182B', linewidth=0.8, linestyle=':')
ax.axhline(loa_lower, color='#B2182B', linewidth=0.8, linestyle=':')

# 95%一致限的95%CI（虚线）
ax.axhline(ci_loa_upper_high, color='#B2182B', linewidth=0.5, linestyle=':',
           alpha=0.4)
ax.axhline(ci_loa_upper_low, color='#B2182B', linewidth=0.5, linestyle=':',
           alpha=0.4)

# 文本标注
ax.text(mean_vals.max()*0.98, loa_upper + 0.03,
        f'+1.96SD = {loa_upper:.3f}', fontsize=5.5, ha='right', color='#B2182B')
ax.text(mean_vals.max()*0.98, loa_lower - 0.06,
        f'-1.96SD = {loa_lower:.3f}', fontsize=5.5, ha='right', color='#B2182B')

# 百分比落在界限内
within_loa = np.sum((diff >= loa_lower) & (diff <= loa_upper)) / n * 100
ax.text(0.5, 0.95, f'{within_loa:.1f}% within ±1.96SD\nn = {n}',
        transform=ax.transAxes, fontsize=6, va='top', ha='center',
        bbox={'boxstyle': 'round', 'fc': 'white', 'alpha': 0.8})

ax.set_xlabel('Mean of Two Methods (mmol/L)')
ax.set_ylabel('Difference (Portable - Lab, mmol/L)')
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('bland_altman.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 10. 雷达图 (Radar Chart)

**适用数据类型**：多维指标同时对比

**学术场景**：多维度性能评估、教学评估、产品质量多指标对比

**显著性标注方法**：不直接标注显著性；用于描述性多维对比

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

rcParams.update({
    'figure.dpi': 600,
    'font.size': 7,
    'font.family': 'sans-serif',
})

# ========== 虚构数据：四种算法在五维性能指标上的对比 ==========
categories = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'AUC']
N = len(categories)

algorithms = {
    'Algorithm A': [0.92, 0.91, 0.93, 0.92, 0.96],
    'Algorithm B': [0.85, 0.82, 0.88, 0.85, 0.89],
    'Algorithm C': [0.89, 0.94, 0.82, 0.88, 0.92],
    'Algorithm D': [0.78, 0.76, 0.81, 0.78, 0.83],
}

colors = ['#2166AC', '#67A9CF', '#D1E5F0', '#F4A582']
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # 闭合

fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={'projection': 'polar'})

for (algo_name, values), color in zip(algorithms.items(), colors):
    values_plot = values + values[:1]
    ax.fill(angles, values_plot, alpha=0.25, color=color)
    ax.plot(angles, values_plot, 'o-', color=color, linewidth=1.5,
            markersize=5, label=algo_name)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=6.5)
ax.set_ylim(0.6, 1.0)
ax.set_yticks([0.7, 0.8, 0.9, 1.0])
ax.set_yticklabels(['0.7', '0.8', '0.9', '1.0'], fontsize=5.5,
                    color='gray')
ax.set_rlabel_position(30)

# 图例
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1),
          fontsize=6, frameon=False)

plt.tight_layout()
plt.savefig('radar_chart.png', dpi=600, bbox_inches='tight')
plt.show()
```

---

## 总结 | Summary

| 图表类型 | 数据格式 | 推荐显著性检验 | 典型学术应用 |
|---------|---------|--------------|------------|
| 柱状图 | 分组 ± SEM/SD | t检验 / ANOVA | 组间均值比较 |
| 箱线图 | 非正态连续 | Mann-Whitney U | 分布形态比较 |
| 小提琴图 | 连续+分组 | t检验 / ANOVA | 分布可视化 |
| 散点图 | 两连续变量 | Pearson/Spearman | 相关性分析 |
| 折线图 | 有序x+连续y | 重复测量ANOVA | 趋势分析 |
| 热力图 | 矩阵 | 相关+显著性 | 多变量关系 |
| 森林图 | OR+95%CI | Meta分析 | 系统评价 |
| ROC曲线 | 预测概率 | DeLong检验 | 诊断评价 |
| Bland-Altman | 配对连续 | — | 一致性评价 |
| 雷达图 | 多维指标 | — | 多维对比 |
