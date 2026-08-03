# 证据质量分级体系 / Evidence Quality Hierarchy

> 不是所有论文的证据分量都一样重——学会区分"铁证"和"弱证"

---

## 为什么需要证据分级

在文献综述中，同等地引述所有已发表论文是一个常见错误。事实上：

- **1 篇高质量的 RCT 可能推翻 10 篇案例报告**的结论
- **1 篇 meta-analysis 的发现比 1 篇单独的实验更有权被强调**
- **在缺乏 RCT 的工程领域，工业部署验证的权重远高于模拟实验**

证据分级体系帮助你在写作时：
- **决定引述的侧重**：高质量证据应该占据更多篇幅和讨论权重
- **识别结论的稳健性**：如果主要结论依赖低质量证据，需要谨慎表述
- **论证 Gap 更有力**："没有一篇超过案例报告水平的证据" = 强力 Gap 论据

---

## 经典证据金字塔（医学/社会科学标准）

```
           ┌─────────────────┐
           │ Systematic       │  ← 最高
           │ Review /         │
           │ Meta-analysis    │
           ├─────────────────┤
           │ RCT              │
           │ (Randomized      │
           │  Controlled      │
           │  Trial)          │
           ├─────────────────┤
           │ Cohort Study     │
           ├─────────────────┤
           │ Case-Control     │
           ├─────────────────┤
           │ Case Series /    │
           │ Case Report      │
           ├─────────────────┤
           │ Expert Opinion / │  ← 最低
           │ Editorial        │
           └─────────────────┘
```

| 等级 | 类型 | 描述 | 可信度 |
|------|------|------|--------|
| L1 | Systematic Review / Meta-analysis | 对多篇同质研究的系统整合和统计合并 | ★★★★★ |
| L2 | Randomized Controlled Trial (RCT) | 随机分配干预和对照，控制混淆变量 | ★★★★ |
| L3 | Cohort Study | 追踪一组人/对象，比较暴露/非暴露组的差异 | ★★★ |
| L4 | Case-Control Study | 从结果回溯到原因，比较有/无结果的组 | ★★ |
| L5 | Case Series / Case Report | 对单个或少数案例的描述，无对照组 | ★ |
| L6 | Expert Opinion / Editorial | 个人经验或观点，无系统实证 | ☆ |

---

## 工程/CS 领域的修正金字塔

经典证据金字塔是为医学/公共卫生设计的，在工程和计算机科学领域，RCT 很少见（你很难对"某个软件架构好不好"做随机对照实验）。因此需要一个修正版。

```
           ┌─────────────────────────────────┐
           │ Industrial Deployment           │  ← 最高
           │ (真实产线/用户的大规模部署验证)   │
           ├─────────────────────────────────┤
           │ Multi-Site Controlled           │
           │ Experiment                      │
           │ (多站点/多团队的可控实验)         │
           ├─────────────────────────────────┤
           │ Replication Study               │
           │ (独立团队复现先前结果)            │
           ├─────────────────────────────────┤
           │ Controlled Experiment           │
           │ (有基线的可控对比实验)             │
           ├─────────────────────────────────┤
           │ Benchmark / Simulation          │
           │ (标准数据集/仿真环境评估)          │
           ├─────────────────────────────────┤
           │ Case Study (Industrial)         │
           │ (单个真实场景的深入分析)            │
           ├─────────────────────────────────┤
           │ Proof of Concept / Demo         │
           │ (原型系统演示，无系统评估)          │
           ├─────────────────────────────────┤
           │ Anecdotal / Blog Post           │  ← 最低
           │ (个人经验、技术博客、白皮书)        │
           └─────────────────────────────────┘
```

| 等级 | 类型 | 描述 | 可信度 | 示例（虚构） |
|------|------|------|--------|------------|
| E1 | Industrial Deployment | 在真实生产环境中长时间运行，有生产级指标（可用率、吞吐量、真实用户反馈） | ★★★★★ | "某制造企业产线部署质量预测系统6个月，产品返修率降低18%" |
| E2 | Multi-Site Experiment | 在多个独立场景/数据集上重复验证，可排除单站点偏差 | ★★★★ | "在3家独立工厂的5条产线上测试，平均F1=0.89±0.03" |
| E3 | Replication Study | 独立团队使用相同/相似方法复现先前结果 | ★★★★ | "独立复现Doe et al.的预训练框架，在新增3个数据集上确认性能" |
| E4 | Controlled Experiment | 有明确对比基线，控制关键变量，统计检验显著 | ★★★ | "在标准预处理管线下对比12种方法，Wilcoxon检验p<0.05" |
| E5 | Benchmark / Simulation | 在标准数据集或仿真环境中的系统评估 | ★★ | "在OpenML 45个分类数据集上10折交叉验证" |
| E6 | Case Study (Industrial) | 单个真实场景的深入分析，但无严格对照组 | ★★ | "在某工厂的月报数据上应用方法X，质量指标有改善趋势" |
| E7 | Proof of Concept | 展示方法"能做"但缺乏系统评估 | ★ | "在Jupyter Notebook上演示方法X在样例数据上的工作流程" |
| E8 | Anecdotal / Blog | 个人经验或非正式报告，无同行评审 | ☆ | "某数据科学家博客文章称方法X在Kaggle竞赛中效果很好" |

**注意**：在你的论文中，如果核心论据主要依赖 E5 及以下等级的证据，这是一个需要在"局限性"部分诚实披露的问题。

---

## 质量评估工具介绍

以下工具帮助你对纳入的文献进行**结构化质量评估**——超越"我觉得这篇论文不错"。

### CASP Checklist (Critical Appraisal Skills Programme)

最广泛使用的文献质量评估清单，针对不同研究设计有不同的 checklist：

| 研究设计 | Checklist 名称 | 题数 | 官网 |
|----------|---------------|------|------|
| RCT | CASP Randomised Controlled Trial Checklist | 11 题 | casp-uk.net |
| 系统综述 | CASP Systematic Review Checklist | 10 题 | casp-uk.net |
| 队列研究 | CASP Cohort Study Checklist | 12 题 | casp-uk.net |
| 案例对照 | CASP Case-Control Study Checklist | 11 题 | casp-uk.net |
| 质性研究 | CASP Qualitative Checklist | 10 题 | casp-uk.net |

**典型问题示例**（CASP RCT Checklist 摘要）：

```text
1. 研究问题是否清晰聚焦？
2. 受试者是否被随机分配到各组？
3. 所有受试者是否都被纳入结果分析？
4. 受试者、研究者、评估者是否对分组设盲？
5. 各组在基线时是否相似？
6. 除实验干预外，各组是否被同等对待？
... （共 11 题，每题回答 Yes / No / Can't Tell）
```

### Newcastle-Ottawa Scale (NOS)

专门用于评估**非随机研究**（队列研究和病例对照研究）的质量。

**评估维度**（总分 9 分）：

```text
队列研究版：
- 选择 (Selection)：4 分
  · 暴露队列的代表性
  · 非暴露队列的选择
  · 暴露的确定方式
  · 研究开始时结局尚未发生

- 可比性 (Comparability)：2 分
  · 队列在设计或分析中的可比性

- 结局 (Outcome)：3 分
  · 结局评估方式
  · 随访时间是否足够
  · 随访的完整性
```

### GRADE (Grading of Recommendations, Assessment, Development, and Evaluation)

不是评估单篇文献，而是评估**一组证据的整体质量**（如 meta-analysis 纳入的所有研究）。

| 初始等级 | 降级因素 | 升级因素 |
|----------|---------|---------|
| RCT → 高 (High) | 偏倚风险 (-1) | 效应量大 (+1) |
| 观察性研究 → 低 (Low) | 不一致性 (-1) | 剂量-反应关系 (+1) |
| | 间接性 (-1) | 所有合理的混淆因素会使效应降低 (+1) |
| | 不精确性 (-1) | |
| | 发表偏倚 (-1) | |

**最终等级**：High → Moderate → Low → Very Low

---

## 在文献矩阵中标注证据等级

### 两种标注方式

#### 方式 A：在矩阵中增加一列（推荐）

```markdown
| # | 作者/年份 | ... | 证据等级 | 等级依据 |
|---|----------|-----|---------|---------|
| 1 | Doe et al., 2025 | ... | E5 | 45个公开数据集benchmark实验，但非工业场景 |
| 2 | Smith & Kumar, 2024 | ... | E6 | 单个CNC工厂的真实数据，但无多站点验证，N较小 |
| 3 | Chen et al., 2023 | ... | E5 | 仿真数据+1条真实产线，但仿真数据可能过于理想 |
| 4 | Williams & Zhao, 2022 | ... | N/A | 系统综述（综述本身是L1，但主题不同需区分） |
```

#### 方式 B：使用证据等级分布总结

在文献综述的方法论部分或结果部分插入一段证据等级总结：

```markdown
### 纳入文献的证据等级分布

在 68 篇纳入文献中：
- E1（工业部署验证）：2 篇（3%）
- E2（多站点实验）：0 篇（0%）
- E3（独立复现）：1 篇（1%）
- E4（可控实验）：5 篇（7%）
- E5（Benchmark/仿真）：38 篇（56%）
- E6（工业案例研究）：15 篇（22%）
- E7（概念验证）：5 篇（7%）
- E8（非正式报告）：2 篇（3%）

**解读**：56% 的文献证据等级为 E5（Benchmark/仿真），仅 3% 达到 E1（工业部署验证）。
这表明该领域的工业落地验证严重不足——这也是本研究的出发点之一。
```

---

## 虚构示例：证据等级如何影响论文写作

### 场景

你发现了两篇论文都在讨论"方法 X 对工业质量预测有效"：

- **论文 A**（证据等级 E1）：某制造企业在 3 条产线上部署方法 X 并运行 12 个月，报告产品缺陷率下降 23%，且有成本-效益分析。
- **论文 B**（证据等级 E5）：在 10 个 UCI 公开数据集上测试方法 X，平均 AUC 为 0.86。

### 在论文中应该怎么写？

```markdown
❌ 错误写法（同等对待）：
"Previous studies have shown that Method X is effective for quality
prediction (Author A, 2025; Author B, 2024)."

✅ 正确写法（按证据等级区分权重）：
"In the only industrial-scale deployment study to date, Author A (2025)
reported that Method X reduced defect rates by 23% over a 12-month period
across three production lines. While benchmark studies have also demonstrated
the method's potential on public datasets (Author B, 2024), the generalizability
of these results to real manufacturing environments remains to be validated."
```

**关键原则**：高质量证据获得"详细引述 + 具体数字"，低质量证据获得"压缩引述 + 注意事项"。

---

## 常见问题

### Q: 如果我的研究领域几乎没有 E1-E4 级别的文献怎么办？

**A:** 这本身就是一条重要的发现——在论文的"方法论质量"或"局限性"部分坦诚讨论：*"A notable limitation of the existing literature is the predominance of benchmark-level evidence (E5) and the near-absence of industrial deployment studies (E1), which constrains the external validity of current findings."*

这同时也是在论证你的研究的必要性——你用更高的证据等级来填补这个 Gap。

### Q: 我自己做的研究应该达到什么证据等级？

**A:** 取决于研究类型：
- **博士论文**：至少 E4（可控实验），最好 E3（有独立复现或外部验证）
- **硕士论文**：E5-E6 可接受
- **期刊论文**：取决于目标期刊——顶刊通常期望 E3 以上

---

## 相关文件

- [文献矩阵](literature-matrix.md) — 在矩阵中实践证据等级标注
- [Gap 识别](gap-identification.md) — 低证据等级的高密度区 = 强力 Gap 信号
- [阅读笔记](reading-notes.md) — 深度阅读模板中包含"证据等级"字段
