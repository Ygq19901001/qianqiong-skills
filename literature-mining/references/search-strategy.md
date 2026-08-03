# 检索策略构建方法 / Search Strategy Construction

> 本文件教授检索策略的**思维方法**——实际检索执行由 `literature-review` / `literature-reviewer-skill` 完成

---

## 重要说明

本文件教你**如何思考和组织你的检索需求**，而不是执行检索。设计好策略后，使用以下技能进行实际检索：

| 你想搜什么 | 用哪个技能 |
|-----------|-----------|
| 英文文献（Semantic Scholar / PubMed / OpenAlex / Crossref） | `literature-review` |
| 中英文文献（CNKI / WoS / ScienceDirect / Scopus） | `literature-reviewer-skill` |
| 多数据库批量检索 | `literature-search` |

**本文件产出物**：一份结构化的检索策略文档，可直接"喂给"上述检索技能。

---

## PICO / PICo 框架

### PICO（适用于定量研究）

PICO 是证据检索的黄金标准框架，将研究问题拆解为四个要素：

| 要素 | 全称 | 含义 | 虚构示例 |
|------|------|------|----------|
| **P** | Population / Problem | 研究对象或问题是什么？ | "采用数字化质量管理系统的制造企业" |
| **I** | Intervention | 干预/暴露/技术是什么？ | "工业物联网 + 实时质量监控仪表盘" |
| **C** | Comparison | 对照组是什么？ | "传统人工巡检 + 纸质记录" |
| **O** | Outcome | 结局/效果是什么？ | "产品一次合格率、质量事故响应时间" |

**基于 PICO 构建研究问题**：

```text
模板：
"In [P], does [I] compared to [C] affect [O]?"

虚构示例：
"In manufacturing enterprises with digital quality management systems (P),
 does real-time IoT-based quality monitoring (I) compared to traditional
 manual inspection (C) improve first-pass yield rate and reduce quality
 incident response time (O)?"
```

**基于 PICO 构建检索词**：

| PICO 要素 | 核心检索词 | 同义词/相关词（扩展检索） |
|-----------|-----------|------------------------|
| P | manufacturing, quality management | "production line", "factory", "shop floor", "industrial production" |
| I | IoT, real-time monitoring, digital dashboard | "Industry 4.0", "smart manufacturing", "digital twin", "sensor network", "MES" |
| C | manual inspection, paper-based | "traditional QC", "conventional quality control", "visual inspection" |
| O | first-pass yield, response time | "defect rate", "quality index", "conformance rate", "quality KPI" |

### PICo（适用于定性研究）

| 要素 | 含义 | 虚构示例 |
|------|------|----------|
| **P** | Population / Problem | "产线质量管理人员" |
| **I** | Interest (现象/体验) | "数字化系统引入后工作方式的变化体验" |
| **Co** | Context | "从传统制造向智能制造转型的中小型工厂" |

---

## Boolean 逻辑构建

### 基本运算符

| 运算符 | 含义 | 效果 | 示例 |
|--------|------|------|------|
| AND | 同时包含 | 缩小范围 | `manufacturing AND IoT AND quality` |
| OR | 包含任一 | 扩大范围 | `manufacturing OR production OR factory` |
| NOT | 排除 | 缩小范围 | `manufacturing NOT pharmaceutical` |

### 构建策略：分块 + 组合

```text
步骤1：将 PICO 的每个要素构建为一个 OR 块
步骤2：用 AND 连接各块
步骤3：确认是否需要用 NOT 排除
```

**虚构示例**：

```text
# 块1：Population（制造场景）
(manufacturing OR "production line" OR factory OR "shop floor" OR "industrial production")

AND

# 块2：Intervention（数字化质量技术）
(IoT OR "Internet of Things" OR "real-time monitoring" OR "digital dashboard"
 OR "Industry 4.0" OR "smart manufacturing" OR MES OR "digital twin")

AND

# 块3：Outcome（质量指标）
("quality management" OR "quality control" OR "quality assurance"
 OR "first-pass yield" OR "defect rate" OR "conformance rate")

# 可选：排除
NOT ("pharmaceutical" OR "food processing" OR "healthcare")
```

### 嵌套括号的重要性

```text
❌ 错误（无括号，AND/OR 混用，结果不确定）：
manufacturing OR factory AND IoT OR digital AND quality

✅ 正确（括号明确分组）：
(manufacturing OR factory) AND (IoT OR digital) AND (quality)
```

---

## MeSH 术语 vs 自由文本检索

### MeSH (Medical Subject Headings) 是什么

MeSH 是 PubMed 使用的受控词表（controlled vocabulary），每个概念有一个唯一的规范词。**PubMed 会自动将你的自由文本映射到 MeSH 术语**。

### MeSH vs 自由文本的权衡

| | MeSH 术语检索 | 自由文本检索 |
|------|-------------|------------|
| **优点** | 高精确度（搜到的是该概念的文献，无论作者用什么词表达） | 高灵敏度（搜到所有提到了这些词的文献） |
| **缺点** | 可能漏掉最新的文献（MeSH 索引有延迟 3-6 个月） | 精确度低（可能返回大量无关结果） |
| **适用场景** | 系统综述的核心检索 | 补充检索、最新文献、灰色文献 |

### 推荐策略：MeSH + 自由文本双检索

```text
# PubMed 检索式（虚构）
((("Quality Control"[Mesh]) OR ("Quality Improvement"[Mesh])) 
 OR ("quality management"[tiab] OR "quality control"[tiab] OR "quality assurance"[tiab]))
AND
((("Manufacturing Industry"[Mesh]) OR ("Industrial Production"[Mesh]))
 OR (manufacturing[tiab] OR "production line"[tiab] OR factory[tiab] OR industrial[tiab]))

# 说明：
# [Mesh] = 使用 PubMed 的受控词检索
# [tiab] = 在标题和摘要中搜索自由文本
```

### 非 PubMed 数据库怎么办

大多数工程/CS 数据库（如 IEEE Xplore、Scopus、Web of Science）没有 MeSH。这些数据库使用自己的索引词或仅支持自由文本检索。在撰写检索策略时，应**为每个数据库单独写检索式**。

---

## 检索日志模板

检索日志（Search Log）是 PRISMA 报告的基础——记录每次检索的"何人何时在何处搜了什么搜到多少"。

### 模板

```markdown
## 检索日志 / Search Log

### 检索基本信息
- **检索日期**：YYYY-MM-DD
- **检索人**：[姓名]
- **研究问题（PICO）**：[一句话]

### 数据库检索记录

| # | 数据库 | 检索策略（简化） | 限制条件 | 命中数 | 备注 |
|---|--------|----------------|---------|--------|------|
| 1 | Web of Science Core Collection | TS=((manufactur* OR "production line") AND (IoT OR "digital twin") AND (quality)) | 2015-2025 | 347 | 检索范围：Topic |
| 2 | Scopus | TITLE-ABS-KEY((manufactur* OR factory) AND ("real-time monitoring" OR MES) AND ("quality control")) | 2015-2025, Article/Review only | 412 | — |
| 3 | IEEE Xplore | ("All Metadata":manufacturing AND "All Metadata":quality AND "All Metadata":IoT) | 2015-2025, Journals & Conferences | 156 | — |
| 4 | CNKI (中国知网) | SU=('制造' * '质量' * ('数字化' + '物联网')) | 2015-2025, 核心期刊 | 203 | 专业检索模式 |

### 检索策略存档
- [ ] 完整检索式已保存为 `.txt` 文件
- [ ] 检索结果已导出为 RIS/BibTeX 格式
- [ ] 检索截图已保存

### 补充检索

| # | 来源 | 方式 | 新增记录 | 日期 |
|---|------|------|---------|------|
| 1 | 正向引用追踪 (Forward) | Web of Science 引用网络 | 18 | YYYY-MM-DD |
| 2 | 反向引用追踪 (Backward) | 核心文献的参考文献列表 | 31 | YYYY-MM-DD |
| 3 | 灰色文献 | Google Scholar + 机构知识库 | 5 | YYYY-MM-DD |

### 更新记录

| 日期 | 更新内容 | 新增/排除数量 |
|------|---------|-------------|
| YYYY-MM-DD | 初次检索 | 792 (去重后) |
| YYYY-MM-DD | 更新检索（新的 6 个月） | +87 (新增), -3 (重复) |
```

### 虚构示例（填充后）

```markdown
## 检索日志示例：数字化技术在工业质量管理中的应用

### 检索基本信息
- **检索日期**：2025-06-15
- **检索人**：[研究者姓名]
- **PICO**：制造企业 (P) 采用物联网实时质量监控 (I) vs 传统人工巡检 (C) 对一次合格率的影响 (O)

### 数据库检索记录

| # | 数据库 | 检索策略（简化） | 限制条件 | 命中数 | 备注 |
|---|--------|----------------|---------|--------|------|
| 1 | Web of Science | (manufactur* OR factory) AND (IoT OR "digital twin") AND ("quality control" OR "defect rate") | 2015-2025, English, Article | 347 | Topic 范围检索 |
| 2 | Scopus | 同上，增加 AND ("real-time" OR "predictive") | 同上 | 412 | 扩大 I 的覆盖 |
| 3 | IEEE Xplore | (manufacturing AND quality AND (IoT OR sensor OR Industry 4.0)) | 2015-2025 | 156 | 仅限期刊和会议 |
| 4 | CNKI | SU=('制造'+'生产') * '质量' * ('物联网'+'数字化'+'信息化') | 2015-2025 | 203 | 核心期刊以上 |

### 补充检索

| # | 来源 | 方式 | 新增记录 | 日期 |
|---|------|------|---------|------|
| 1 | 正向引用追踪 | WoS：引用量 Top 5 核心论文的后续引用 | 18 | 2025-06-16 |
| 2 | 反向引用追踪 | 核心论文参考文献列表交叉并集 | 31 | 2025-06-16 |
```

---

## 雪球法（Snowballing）

### 正向引用追踪 (Forward Citation Tracking)

**定义**：找到一篇核心论文后，搜索**谁引用了它**。

**操作**：
1. 在 Web of Science / Scopus / Google Scholar 中打开核心论文
2. 点击 "Cited by" / "被引"
3. 筛选最近 3 年、高被引的论文
4. 将相关论文加入候选列表

**适用场景**：核心论文发表于 3-5 年前，你需要找到基于该论文的最新进展。

### 反向引用追踪 (Backward Citation Tracking)

**定义**：阅读核心论文的**参考文献列表**，找出值得追读的原始文献。

**操作**：
1. 打开核心论文的参考文献列表
2. 标记重复被多篇核心论文引用的文献（被引频次高的基础文献）
3. 将标记文献加入候选列表

**适用场景**：你需要系统追溯一个研究方向的基础和源头文献。

### 雪球法的优缺点

| | 优点 | 缺点 |
|------|------|------|
| 正向追踪 | 发现最新进展；发现跨学科引用 | 可能错过独立发展的平行方向 |
| 反向追踪 | 覆盖基础文献；高覆盖度 | 只能找到"被作者团队知道的"文献 |

**最佳实践**：数据库检索 + 雪球法（正向+反向）= 覆盖度最大化的检索策略。

---

## 检索策略文档模板（可直接发给检索技能）

```markdown
## 检索请求

### 研究问题
[一句话描述]

### PICO 拆解
- P (Population/Problem)：[描述]
- I (Intervention)：[描述]
- C (Comparison)：[描述]
- O (Outcome)：[描述]

### 数据库要求
- [ ] Web of Science
- [ ] Scopus
- [ ] IEEE Xplore
- [ ] PubMed
- [ ] CNKI
- [ ] Semantic Scholar
- [ ] 其他：[指定]

### 检索式（供修改）
{检索式}

### 限制条件
- 发表年份：[起始]-[结束]
- 语言：[中/英/不限]
- 文献类型：[期刊/会议/学位论文/不限]
- 其他：[如：仅核心期刊、影响因子>2 等]

### 期望数量
- 预期命中：[约 xx 篇]
- 目标纳入：[xx 篇]
```

---

## 常见误区

### 误区 1：一个检索式打天下

**错误**：用同一个检索式在 Web of Science、Scopus、CNKI 中检索。

**正确**：每个数据库的字段、语法、索引方式不同，必须单独适配。至少调整字段限定符和通配符。

### 误区 2：只搜一次

**错误**：在项目开始时检索一次，6 个月后提交论文时不更新。

**正确**：在提交/答辩前 1-2 周执行一次更新检索（search update），以覆盖新发表的文献。在 PRISMA 流程图中注明更新检索的日期和新增记录数。

### 误区 3：检索词太窄

**错误**：`"digital twin assisted quality prediction for CNC machining"`（太具体，命中=0）

**正确**：`(("digital twin" OR simulation) AND ("quality prediction" OR "quality control") AND (CNC OR machining OR manufacturing))`（拆成块，用 OR 扩大）

---

## 相关文件

- [PRISMA 指南](prisma-guide.md) — 基于检索日志生成筛选流程图
- [文献矩阵](literature-matrix.md) — 检索完成后，用矩阵组织文献
- [Gap 识别](gap-identification.md) — 基于检索结果识别研究空白

---

## 推荐阅读

- Booth, A., Sutton, A., & Papaioannou, D. (2016). *Systematic Approaches to a Successful Literature Review* (2nd ed.). SAGE. — 第 5 章详细讲解检索策略设计
- Higgins, J. P. T., et al. (2022). *Cochrane Handbook for Systematic Reviews of Interventions* (v6.3). — 第 4 章是医学领域检索策略的权威参考
- Kitchenham, B., & Charters, S. (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. — 软件工程/CS 领域系统综述的检索标准
