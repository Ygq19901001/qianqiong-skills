# 数据管道：CSV/Excel → 出版级图表 | Data Pipeline

> 所有示例使用虚构数据。All examples use synthetic datasets.

---

## 概述 | Overview

本文件提供从原始数据文件（CSV/Excel）到出版级图表（PNG 600dpi + SVG + PDF）的完整自动化工作流，覆盖数据读取、清洗、统计计算、检验选择到图表产出的全流程。

---

## 工作流总览 | Workflow Overview

```
[CSV/Excel] → pandas读取 → 数据清洗 → 格式转换(wide/long)
    → 描述统计(mean/SD/SEM/median/IQR)
    → 正态性检验(Shapiro-Wilk)
    → 统计检验选择(t-test/Mann-Whitney/ANOVA/Kruskal-Wallis)
    → 显著性标注
    → 图表生成(matplotlib/seaborn)
    → 多格式保存(PNG 600dpi + SVG + PDF)
    → (可选)嵌入Word文档
```

---

## 1. 数据读取与清洗 | Data Reading & Cleaning

```python
import pandas as pd
import numpy as np

def load_and_clean_data(filepath, sheet_name=None, drop_na=True,
                        remove_outliers=False, outlier_method='iqr',
                        outlier_threshold=1.5):
    """
    读取数据文件并进行基本清洗。

    Parameters
    ----------
    filepath : str
        文件路径（支持 .csv, .xlsx, .xls, .tsv）
    sheet_name : str or None
        Excel工作表名（None表示第一个）
    drop_na : bool
        是否删除缺失值
    remove_outliers : bool
        是否移除离群值
    outlier_method : str
        'iqr' | 'zscore'
    outlier_threshold : float
        IQR倍数或Z分数阈值

    Returns
    -------
    pd.DataFrame
        清洗后的数据框
    """
    # 根据扩展名选择读取方式
    ext = filepath.lower().split('.')[-1]

    if ext == 'csv':
        df = pd.read_csv(filepath, encoding='utf-8')
    elif ext == 'tsv':
        df = pd.read_csv(filepath, sep='\t', encoding='utf-8')
    elif ext in ('xlsx', 'xls'):
        df = pd.read_excel(filepath, sheet_name=sheet_name)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    print(f"Loaded: {df.shape[0]} rows × {df.shape[1]} columns")

    # 清洗
    if drop_na:
        before = df.shape[0]
        df = df.dropna()
        print(f"Dropped {before - df.shape[0]} rows with missing values")

    # 移除离群值（按数值列）
    if remove_outliers:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if outlier_method == 'iqr':
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - outlier_threshold * IQR
                upper = Q3 + outlier_threshold * IQR
                mask = (df[col] >= lower) & (df[col] <= upper)
            elif outlier_method == 'zscore':
                z = np.abs((df[col] - df[col].mean()) / df[col].std())
                mask = z <= outlier_threshold

            removed = (~mask).sum()
            if removed > 0:
                print(f"  {col}: removed {removed} outliers")
            df = df[mask]

    df = df.reset_index(drop=True)
    print(f"Final: {df.shape[0]} rows × {df.shape[1]} columns")

    return df
```

---

## 2. 格式转换 | Format Conversion

### 2.1 宽格式 → 长格式（melt）

适合从"每列一个组"转换为 seaborn/matplotlib 友好的长格式。

```python
# ========== 虚构数据：宽格式 ==========
#    SampleID    Control    TreatmentA    TreatmentB
# 0        1         4.8           6.1           7.2
# 1        2         5.2           5.8           7.5
# ...

df_wide = pd.DataFrame({
    'SampleID': range(1, 21),
    'Control': np.random.normal(5.0, 1.0, 20),
    'TreatmentA': np.random.normal(6.5, 1.2, 20),
    'TreatmentB': np.random.normal(7.2, 1.1, 20),
})

# 转换为长格式
df_long = df_wide.melt(
    id_vars=['SampleID'],
    var_name='Group',
    value_name='Value'
)
print(df_long.head())
#    SampleID Group  Value
# 0         1 Control  4.80
# 1         2 Control  5.20
# ...
```

### 2.2 长格式 → 描述统计宽格式（pivot + groupby）

```python
# groupby + agg 获取描述统计
desc_stats = df_long.groupby('Group')['Value'].agg([
    ('N', 'count'),
    ('Mean', 'mean'),
    ('SD', 'std'),
    ('SEM', lambda x: x.std() / np.sqrt(x.count())),
    ('Median', 'median'),
    ('IQR', lambda x: x.quantile(0.75) - x.quantile(0.25)),
]).reset_index()

print(desc_stats.to_string(index=False))
```

### 2.3 pivot → 宽格式矩阵

```python
# 适合热力图的矩阵格式
matrix_wide = df_long.pivot(index='SampleID', columns='Group', values='Value')
print(matrix_wide.head())
```

---

## 3. 描述统计自动计算 | Automated Descriptive Statistics

```python
def compute_descriptive_stats(df, group_col, value_col):
    """
    计算各组的完整描述性统计。

    Returns
    -------
    pd.DataFrame
        含 N, Mean, SD, SEM, Median, IQR, CI95_Low, CI95_High,
        Min, Max, Skewness, Kurtosis
    """
    from scipy import stats as sp_stats

    def sem(x):
        return x.std() / np.sqrt(x.count())

    def ci95_radius(x):
        n = x.count()
        if n < 2:
            return np.nan
        return sp_stats.t.ppf(0.975, n - 1) * (x.std() / np.sqrt(n))

    result = df.groupby(group_col)[value_col].agg(
        N='count',
        Mean='mean',
        SD=lambda x: x.std(),
        SEM=sem,
        Median='median',
        Q25=lambda x: x.quantile(0.25),
        Q75=lambda x: x.quantile(0.75),
        IQR=lambda x: x.quantile(0.75) - x.quantile(0.25),
        CI95_Radius=ci95_radius,
        Min='min',
        Max='max',
        Skewness=lambda x: x.skew(),
        Kurtosis=lambda x: x.kurtosis(),
    ).reset_index()

    result['CI95_Low'] = result['Mean'] - result['CI95_Radius']
    result['CI95_High'] = result['Mean'] + result['CI95_Radius']

    return result
```

---

## 4. 统计检验自动选择与执行 | Auto Test Selection

```python
from scipy import stats

def auto_statistical_test(df, group_col, value_col, alpha=0.05,
                          paired=False):
    """
    根据数据特征自动选择并执行适当的统计检验。

    决策逻辑：
    1. 检查组数 → 2组用t检验/Mann-Whitney，3+组用ANOVA/Kruskal-Wallis
    2. 正态性检验(Shapiro-Wilk) → 正态用参数检验，非正态用非参数检验
    3. 方差齐性(Levene) → 不齐时t检验用Welch校正

    Parameters
    ----------
    df : pd.DataFrame
        数据框（长格式）
    group_col : str
        分组列名
    value_col : str
        数值列名
    alpha : float
        显著性水平
    paired : bool
        是否为配对设计

    Returns
    -------
    dict
        {'test_name': str, 'statistic': float, 'p_value': float,
         'significant': bool, 'normality_results': dict, ...}
    """
    groups = df[group_col].unique()
    n_groups = len(groups)

    # 正态性检验
    normality = {}
    all_normal = True
    for g in groups:
        data = df[df[group_col] == g][value_col]
        if len(data) >= 3:
            _, p = stats.shapiro(data)
            normality[g] = {'W': _, 'p': p, 'normal': p >= alpha}
            if p < alpha:
                all_normal = False
        else:
            normality[g] = {'normal': True}  # 样本太小，假设正态

    print(f"Normality check ({'PASS' if all_normal else 'FAIL'}):")
    for g, r in normality.items():
        print(f"  {g}: {'normal' if r['normal'] else 'NON-normal'}")

    # 选择检验
    result = {'normality_results': normality, 'n_groups': n_groups}

    if n_groups == 2:
        g1, g2 = groups
        d1 = df[df[group_col] == g1][value_col]
        d2 = df[df[group_col] == g2][value_col]

        if paired:
            if all_normal:
                stat, p = stats.ttest_rel(d1, d2)
                test_name = 'Paired t-test'
            else:
                stat, p = stats.wilcoxon(d1, d2)
                test_name = 'Wilcoxon signed-rank test'
        else:
            if all_normal:
                # 方差齐性检验
                _, p_levene = stats.levene(d1, d2)
                if p_levene < alpha:
                    stat, p = stats.ttest_ind(d1, d2, equal_var=False)
                    test_name = "Welch's t-test (unequal variance)"
                else:
                    stat, p = stats.ttest_ind(d1, d2)
                    test_name = "Student's t-test"
            else:
                stat, p = stats.mannwhitneyu(d1, d2)
                test_name = 'Mann-Whitney U test'

    else:  # 3组及以上
        data_list = [df[df[group_col] == g][value_col] for g in groups]
        if all_normal:
            stat, p = stats.f_oneway(*data_list)
            test_name = 'One-way ANOVA'
        else:
            stat, p = stats.kruskal(*data_list)
            test_name = 'Kruskal-Wallis H test'

    result.update({
        'test_name': test_name,
        'statistic': stat,
        'p_value': p,
        'significant': p < alpha,
        'alpha': alpha,
    })

    print(f"\nTest: {test_name}")
    print(f"Statistic = {stat:.4f}, p = {p:.4e}")
    print(f"Significant: {result['significant']} "
          f"({get_significance_label(p)})")

    return result
```

---

## 5. 完整数据管道示例 | Complete Pipeline Example

```python
# ========== 构建虚构数据并运行完整管道 ==========
np.random.seed(2024)

# 生成CSV格式的虚构数据
csv_data = []
for i in range(1, 51):
    csv_data.append({
        'SampleID': f'S{i:03d}',
        'Group': np.random.choice(['Control', 'LowDose', 'HighDose']),
        'Biomarker_A': 0,
        'Biomarker_B': 0,
    })

df_raw = pd.DataFrame(csv_data)
# 根据分组填充不同的均值
for idx, row in df_raw.iterrows():
    if row['Group'] == 'Control':
        df_raw.at[idx, 'Biomarker_A'] = np.random.normal(3.2, 0.5)
        df_raw.at[idx, 'Biomarker_B'] = np.random.normal(8.5, 1.2)
    elif row['Group'] == 'LowDose':
        df_raw.at[idx, 'Biomarker_A'] = np.random.normal(4.1, 0.6)
        df_raw.at[idx, 'Biomarker_B'] = np.random.normal(7.2, 1.0)
    else:
        df_raw.at[idx, 'Biomarker_A'] = np.random.normal(5.8, 0.7)
        df_raw.at[idx, 'Biomarker_B'] = np.random.normal(5.5, 1.1)

# 保存为CSV（模拟真实输入）
df_raw.to_csv('biomarker_data.csv', index=False)

# === 管道开始 ===
# Step 1: 加载
df = load_and_clean_data('biomarker_data.csv')
print(f"\nLoaded: {df.shape}")

# Step 2: 描述统计
for marker in ['Biomarker_A', 'Biomarker_B']:
    print(f"\n{'='*60}")
    print(f"Descriptive Statistics: {marker}")
    print(f"{'='*60}")
    stats_df = compute_descriptive_stats(df, 'Group', marker)
    print(stats_df.to_string(index=False))

    # Step 3: 统计检验
    print(f"\nStatistical Test: {marker}")
    test_result = auto_statistical_test(df, 'Group', marker)
```

---

## 6. 图表生成与多格式保存 | Figure Generation & Export

```python
def save_figure_multi_format(fig, base_path, formats=None):
    """
    以多种格式保存图形。

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        图形对象
    base_path : str
        基础文件名（不含扩展名），如 'results/figure1'
    formats : list
        保存格式列表，默认 ['png', 'svg', 'pdf']
    """
    if formats is None:
        formats = ['png', 'svg', 'pdf']

    saved_files = []
    for fmt in formats:
        path = f'{base_path}.{fmt}'
        kwargs = {'bbox_inches': 'tight', 'pad_inches': 0.02}

        if fmt == 'png':
            kwargs['dpi'] = 600
        elif fmt == 'svg':
            kwargs['dpi'] = 300  # SVG中对DPI要求较低
        elif fmt == 'pdf':
            kwargs['dpi'] = 300

        fig.savefig(path, **kwargs)
        saved_files.append(path)

    print(f"Saved: {', '.join(saved_files)}")
    return saved_files


# === 完整管道：从CSV到最终图表 ===
def pipeline_csv_to_figure(csv_path, group_col, value_col,
                           chart_type='bar', journal_preset=None,
                           output_prefix='output/figure'):
    """
    一键：CSV → 出版级图表

    Parameters
    ----------
    csv_path : str
        数据文件路径
    group_col : str
        分组列
    value_col : str
        数值列
    chart_type : str
        'bar' | 'box' | 'violin' | 'scatter'（需要两列）| 'line'
    journal_preset : str or None
        'nature_single', 'elsevier_single' 等
    output_prefix : str
        输出文件前缀

    Returns
    -------
    dict
        含图文件路径、描述统计、检验结果
    """
    # 1. 加载数据
    df = load_and_clean_data(csv_path)

    # 2. 应用期刊预设
    if journal_preset:
        load_journal_preset(journal_preset)

    # 3. 描述统计
    desc = compute_descriptive_stats(df, group_col, value_col)

    # 4. 统计检验
    test = auto_statistical_test(df, group_col, value_col)

    # 5. 绘图
    groups = df[group_col].unique()
    fig, ax = plt.subplots()

    if chart_type == 'bar':
        means = []
        sems = []
        for g in groups:
            d = df[df[group_col] == g][value_col]
            means.append(d.mean())
            sems.append(d.std() / np.sqrt(len(d)))
        ax.bar(groups, means, yerr=sems, capsize=4,
               color=['#D1E5F0', '#67A9CF', '#2166AC'][:len(groups)])

    elif chart_type == 'box':
        data_list = [df[df[group_col] == g][value_col] for g in groups]
        bp = ax.boxplot(data_list, patch_artist=True)
        for patch, c in zip(bp['boxes'],
                            ['#D1E5F0', '#67A9CF', '#2166AC'][:len(groups)]):
            patch.set_facecolor(c)

    # 6. 显著性标注
    sig = get_significance_label(test['p_value'])
    ax.text(0.5, 1.05, f"{test['test_name']}: p={test['p_value']:.4f} {sig}",
            transform=ax.transAxes, ha='center', fontsize=7, style='italic')

    ax.set_ylabel(value_col)
    ax.spines[['top', 'right']].set_visible(False)
    plt.tight_layout()

    # 7. 保存
    files = save_figure_multi_format(fig, output_prefix)

    return {
        'files': files,
        'descriptive_stats': desc,
        'test': test,
    }


# 使用示例
# result = pipeline_csv_to_figure(
#     'biomarker_data.csv', 'Group', 'Biomarker_A',
#     chart_type='bar', journal_preset='nature_single',
#     output_prefix='output/fig1_biomarker'
# )
```

---

## 7. 与 academic-docx-toolkit 联动 | Word Integration

```python
def embed_figure_in_word(figure_path, docx_path, caption,
                         width_inches=None, position='after'):
    """
    将生成的图表嵌入Word文档。

    Requires: python-docx

    Parameters
    ----------
    figure_path : str
        图表文件路径
    docx_path : str
        目标Word文档路径
    caption : str
        图题（如 "图1 各组生物标志物水平比较"）
    width_inches : float or None
        图片宽度。如不指定，自动匹配单栏宽度
    position : str
        'after' | 'before' | 'append'（插入到最后一段之后）
    """
    try:
        from docx import Document
        from docx.shared import Inches, Cm
        from docx.enum.text import WD_ALIGN_PARAGRAPH
    except ImportError:
        print("Error: python-docx not installed. Run: pip install python-docx")
        return

    doc = Document(docx_path)

    # 添加图
    if width_inches:
        width = Inches(width_inches)
    else:
        width = Inches(3.5)  # 默认单栏宽度

    last_paragraph = doc.paragraphs[-1]
    run = last_paragraph.add_run()
    run.add_picture(figure_path, width=width)

    # 居中对齐
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # 添加图题
    caption_para = doc.add_paragraph()
    caption_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = caption_para.add_run(caption)
    run.font.size = doc.styles['Normal'].font.size  # 正文字号
    run.bold = False

    doc.save(docx_path)
    print(f"Figure embedded: {figure_path} → {docx_path}")
```
