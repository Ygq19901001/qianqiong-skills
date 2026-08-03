# 四维加权评分系统 (Four-Dimensional Weighted Scoring System)

## 评分公式

论文版本质量通过以下四个维度加权计算综合得分：

```
综合得分 = 内容完整性 × 0.30 + 逻辑完整性 × 0.25 + 逻辑闭环 × 0.25 + AI检测评估 × 0.20
```

**权重设计理由**：

- **内容完整性 (0.30)**：权重最高，论文的根本在于内容是否完整、数据是否可信
- **逻辑完整性 (0.25)**：论证链是否完整、推理是否有跳跃
- **逻辑闭环 (0.25)**：问题提出→分析→解决→验证的闭环是否形成
- **AI检测评估 (0.20)**：语言表达的自然度和学术性，权重略低但不可忽视

## 评分细则（1-100分尺度）

### 1. 内容完整性（权重 0.30）

| 分数区间 | 等级 | 判定标准 |
|----------|------|----------|
| 90-100 | 优秀 | 各章节内容充实，数据来源可信，关键要素无遗漏 |
| 80-89 | 良好 | 主体内容完整，少数小节有待补充 |
| 70-79 | 中等 | 核心章节完整，辅助章节存在内容缺口 |
| 60-69 | 及格 | 关键章节基本覆盖，但深度不足 |
| 40-59 | 不足 | 存在章节缺失或内容严重不完整 |
| 1-39 | 严重不足 | 多个核心章节空白或仅占位符 |

### 2. 逻辑完整性（权重 0.25）

| 分数区间 | 等级 | 判定标准 |
|----------|------|----------|
| 90-100 | 优秀 | 论证链无断裂，前提→推理→结论一以贯之 |
| 80-89 | 良好 | 主论证完整，个别推理步骤可强化 |
| 70-79 | 中等 | 论证框架合理，部分推导存在跳跃 |
| 60-69 | 及格 | 有基本论证思路，但逻辑链多处不连贯 |
| 40-59 | 不足 | 论证方向不清，推理跳跃频繁 |
| 1-39 | 严重不足 | 逻辑混乱，前提与结论脱节 |

### 3. 逻辑闭环（权重 0.25）

| 分数区间 | 等级 | 判定标准 |
|----------|------|----------|
| 90-100 | 优秀 | 问题→分析→方案→验证形成完整闭环 |
| 80-89 | 良好 | 闭环形成，验证环节可进一步强化 |
| 70-79 | 中等 | 主闭环存在，但分支问题未完全收束 |
| 60-69 | 及格 | 部分闭环形成，多个悬而未决的问题 |
| 40-59 | 不足 | 闭环断裂，提出问题但无有效回应 |
| 1-39 | 严重不足 | 无闭环意识，问题与结论相互独立 |

### 4. AI检测评估（权重 0.20）

| 分数区间 | 等级 | 判定标准 |
|----------|------|----------|
| 90-100 | 优秀 | 语言自然流畅，无AI写作痕迹 |
| 80-89 | 良好 | 基本自然，偶有模板化表达 |
| 70-79 | 中等 | 存在少量AI特征词汇和句式 |
| 60-69 | 及格 | 多处AI特征明显，需人工润色 |
| 40-59 | 不足 | 大面积AI写作痕迹，需重点修改 |
| 1-39 | 严重不足 | 全文AI生成特征强烈，不宜送审 |

## 优质线阈值

| 阈值 | 含义 |
|------|------|
| **85分** | **送审就绪线** — 综合得分≥85分，论文具备送审基本条件 |
| **75分** | **修改完成线** — 综合得分≥75分，本轮修改基本达标 |
| **60分** | **初稿完成线** — 综合得分≥60分，初稿框架搭建完成 |

## 评分趋势示例

以下为完全虚构的论文版本评分趋势数据：

| 版本 | 内容完整性 | 逻辑完整性 | 逻辑闭环 | AI检测评估 | 综合得分 |
|------|-----------|-----------|----------|-----------|----------|
| v1.0 | 60 | 55 | 50 | 72 | 58.65 |
| v1.1 | 68 | 62 | 58 | 70 | 64.20 |
| v2.0 | 78 | 72 | 70 | 68 | 72.10 |
| v2.1 | 85 | 80 | 78 | 75 | 79.65 |
| v3.0 | 90 | 87 | 85 | 82 | 86.15 |
| v4.0 | 95 | 92 | 90 | 88 | 91.35 |

## 雷达图生成代码

以下 Python 代码使用 matplotlib 生成四维评分雷达图（使用虚构数据）：

```python
import matplotlib.pyplot as plt
import numpy as np

# 虚构示例数据
categories = ['内容完整性\n(0.30)', '逻辑完整性\n(0.25)', '逻辑闭环\n(0.25)', 'AI检测评估\n(0.20)']
weights = [0.30, 0.25, 0.25, 0.20]

# 多个版本的评分（完全虚构）
versions = {
    'v1.0 (58.65分)': [60, 55, 50, 72],
    'v2.0 (72.10分)': [78, 72, 70, 68],
    'v3.0 (86.15分)': [90, 87, 85, 82],
    'v4.0 (91.35分)': [95, 92, 90, 88],
}

# 雷达图设置
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # 闭合

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

colors = ['#e74c3c', '#f39c12', '#2ecc71', '#3498db']
for (label, values), color in zip(versions.items(), colors):
    values_plot = values + values[:1]
    ax.fill(angles, values_plot, alpha=0.1, color=color)
    ax.plot(angles, values_plot, 'o-', linewidth=2, color=color, label=label)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=10)
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], size=8)
ax.set_title('论文版本四维评分雷达图', size=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.savefig('paper_version_radar.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 评分趋势折线图代码

```python
import matplotlib.pyplot as plt
import numpy as np

# 虚构示例数据
versions_labels = ['v1.0', 'v1.1', 'v2.0', 'v2.1', 'v3.0', 'v4.0']
composite_scores = [58.65, 64.20, 72.10, 79.65, 86.15, 91.35]
dimension_labels = ['内容完整性', '逻辑完整性', '逻辑闭环', 'AI检测评估']
dimension_scores = {
    '内容完整性': [60, 68, 78, 85, 90, 95],
    '逻辑完整性': [55, 62, 72, 80, 87, 92],
    '逻辑闭环':    [50, 58, 70, 78, 85, 90],
    'AI检测评估':  [72, 70, 68, 75, 82, 88],
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# 左图：综合得分趋势
ax1.plot(versions_labels, composite_scores, 'o-', linewidth=2.5, color='#2c3e50', markersize=8)
ax1.axhline(y=85, color='#27ae60', linestyle='--', linewidth=1.5, label='送审就绪线 (85分)')
ax1.axhline(y=75, color='#f39c12', linestyle='--', linewidth=1.5, label='修改完成线 (75分)')
ax1.fill_between(range(len(versions_labels)), composite_scores, alpha=0.15, color='#3498db')
for i, (v, s) in enumerate(zip(versions_labels, composite_scores)):
    ax1.annotate(f'{s:.1f}', (i, s), textcoords="offset points", xytext=(0, 12), ha='center', fontsize=9)
ax1.set_xticks(range(len(versions_labels)))
ax1.set_xticklabels(versions_labels)
ax1.set_ylim(40, 100)
ax1.set_ylabel('综合得分')
ax1.set_title('论文版本综合得分趋势')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 右图：各维度得分趋势
for dim, scores in dimension_scores.items():
    ax2.plot(versions_labels, scores, 'o-', linewidth=1.8, markersize=6, label=dim)
ax2.axhline(y=85, color='#27ae60', linestyle='--', linewidth=1.5, alpha=0.6)
ax2.set_xticks(range(len(versions_labels)))
ax2.set_xticklabels(versions_labels, rotation=30)
ax2.set_ylim(40, 100)
ax2.set_ylabel('维度得分')
ax2.set_title('各维度得分趋势')
ax2.legend(loc='lower right')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('paper_version_trend.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 使用建议

1. **每次版本更新后评分**：量化变化趋势，识别退步或停滞的维度
2. **关注综合得分是否持续上升**：如出现下降，分析原因（是否因架构重构导致短暂下降）
3. **送审前确保≥85分**：低于85分的版本不建议送审
4. **AI检测评估维度单独关注**：即使综合得分高，若AI检测评估维度持续偏低，需重点润色
