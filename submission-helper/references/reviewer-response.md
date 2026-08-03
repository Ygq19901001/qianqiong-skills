# 审稿意见解析与分类应对 (Reviewer Response Analysis)

> 读懂审稿信、分类审稿意见、处理分歧、撰写申诉信、估算修改时间。所有审稿意见、作者名、期刊名均为**虚构**。

---

## 一、如何阅读审稿信 (How to Read a Decision Letter)

### 审稿信的结构

一份典型的审稿决定信（Decision Letter）包含以下层次：

```
┌─────────────────────────────────────────────┐
│ 编辑总结段 (Editor's Summary)                 │
│  ├── 告知决定（Accept / Minor / Major / Reject) │
│  ├── 编辑的整体评价（1-3 句）                  │
│  └── 编辑的附加要求（如有）                    │
├─────────────────────────────────────────────┤
│ 审稿人意见 (Reviewer Comments)                 │
│  ├── 审稿人 1：总体评价 + 逐条意见              │
│  ├── 审稿人 2：总体评价 + 逐条意见              │
│  └── 审稿人 3（如有）...                       │
├─────────────────────────────────────────────┤
│ 编辑给作者的额外指示（如有）                    │
│  ├── 修改截止日期                              │
│  ├── 格式要求                                  │
│  └── 重新投稿说明                              │
└─────────────────────────────────────────────┘
```

### 区分三类信息

| 信息类型 | 特征 | 如何处理 |
|---------|------|---------|
| **编辑意见 (Editor's Comments)** | 通常出现在信的开头或结尾，由编辑直接撰写 | **必须全部回应**，编辑意见的优先级高于审稿人意见 |
| **审稿人意见 (Reviewer Comments)** | 逐条列出，标记为 Reviewer 1/2/3 | 逐条回应，但可以判断哪些是建议性、哪些是强制性 |
| **系统/格式要求 (Administrative Notes)** | 来自编辑部而非编辑本人，如格式问题、版权协议 | 按要求执行即可，一般不需要在 Reply Letter 中长篇回应 |

### 判断"建议性"vs"强制性"

审稿人语气往往透露了这条意见的性质：

| 语气线索 | 性质判断 |
|---------|---------|
| "must be addressed" / "should be corrected" / "is required" | **强制性**（必须改或必须给出充分理由） |
| "could be improved" / "might consider" / "it would be interesting" | **建议性**（最好改，但如有合理原因可不改） |
| "I wonder whether..." / "Perhaps the authors..." | **建议性**（可供参考的拓展方向） |

---

## 二、审稿意见分类与优先级 (Comment Classification & Prioritization)

### 分类框架

收到审稿意见后，第一步是**分类**，而不是逐句回复。

| 分类 | 定义 | 优先级 | 典型修改量 | 示例 |
|------|------|--------|-----------|------|
| **Major — 方法/实验** | 要求补充实验、重做分析、修改核心方法 | 🔴 P0 最高 | 2-4周 | "The sample size is insufficient." |
| **Major — 理论/框架** | 质疑创新性、理论框架、研究设计 | 🔴 P0 最高 | 2-4周 | "The theoretical contribution is unclear." |
| **Minor — 分析/讨论** | 要求额外分析、补充讨论、加强论证 | 🟡 P1 中 | 1-2周 | "The authors should discuss alternative explanations." |
| **Minor — 文献/引用** | 要求补充或更正文献引用 | 🟡 P1 中 | 3-5天 | "The following relevant papers should be cited." |
| **Editorial — 写作/图表** | 语言问题、格式、图表优化、错别字 | 🟢 P2 低 | 3-7天 | "Several typos need correction." |

### 分类操作流程

```
Step 1: 打开一个新的 Excel/CSV，创建以下列：
  Reviewer | Point # | Original Comment | Category | Priority | Action | Status

Step 2: 逐条读取审稿意见，填入"Original Comment"

Step 3: 判断每条意见的 Category (Major/Minor/Editorial) 和 Priority (P0/P1/P2)

Step 4: 在"Action"列写下你的初步修改计划

Step 5: 按 Priority 排序，按序执行修改

Step 6: 修改完成后更新"Status"
```

### 分类示例（虚构）

| Reviewer | Point # | Original Comment | Category | Priority | Action | Status |
|----------|---------|-----------------|----------|----------|--------|--------|
| R1 | 1 | Sample size too small (n=15), provide power analysis | Major-方法 | P0 | Conduct G*Power post-hoc analysis; add to Methods | ✓ Done |
| R1 | 2 | Literature review misses recent work on blockchain traceability (year 2023-2025) | Minor-文献 | P1 | Search and add 5-8 recent refs; update Section 2 | ✓ Done |
| R1 | 3 | Figure 3 resolution is low, axis labels illegible | Editorial | P2 | Re-export at 600 dpi | ✓ Done |
| R2 | 1 | The contribution over existing MES systems is not clearly articulated | Major-理论 | P0 | Add comparative table; clarify novelty in Introduction | ✓ Done |
| R2 | 2 | Discussion section overstates conclusions | Minor-讨论 | P1 | Temper claims; add limitation paragraph | ✓ Done |
| R2 | 3 | Several grammatical errors throughout | Editorial | P2 | Full proofread by native speaker | ✓ Done |

---

## 三、分歧审稿意见处理 (Handling Conflicting Reviewer Comments)

### 常见分歧场景

**场景A：审稿人 A 正面 / 审稿人 B 负面**

```
审稿人 A: "This is a well-designed study with clear practical implications."
审稿人 B: "The paper lacks theoretical contribution and the method is problematic."
```

**应对策略：**

1. **不要在回复中选边站** — 不要说"审稿人A认为好，所以我们不改"
2. **认真对待 B 的每一条批评** — 编辑会重点看负面意见
3. **如果 B 的批评合理** → 大幅修改
4. **如果 B 有误解** → 礼貌澄清，引用 A 的正面评价佐证（如"审稿人A也注意到..."）
5. **如果分歧根本性** → 做出你的学术判断，解释为什么 B 的担忧虽合理但不影响核心结论

**场景B：两个审稿人给出矛盾的具体建议**

```
审稿人 A: "The results should be presented as a bar chart."
审稿人 B: "I suggest presenting the results as a line plot."
```

**应对策略：**

1. 判断哪个呈现方式更适合你的数据 → 选一个
2. 回复审稿人B："We thank Reviewer 2 for the suggestion. After careful consideration, we believe the bar chart format (as suggested by Reviewer 1) better communicates the between-condition comparisons that are central to our analysis. We have added a supplementary line plot (Supplementary Figure S1) to show temporal trends as suggested by Reviewer 2."
3. **关键原则**：展示你认真考虑了双方意见，而非无视某一方

---

## 四、拒绝后申诉信 (Appeal Letter After Rejection)

### 什么情况下值得申诉

| 情况 | 是否建议申诉 |
|------|------------|
| 审稿人误解了你的核心方法/发现 | ✅ 可以申诉 |
| 审稿人引用了错误事实（如称某方法不存在，但你能引用文献证明） | ✅ 可以申诉 |
| 编辑将你的论文发给了明显不合适的审稿人 | ✅ 可以申诉 |
| 审稿意见总体正面，但编辑做了 Editorial Rejection | ✅ 可以申诉（但机会不大） |
| 审稿人一致认为创新性不足 | ❌ 建议改投而非申诉 |
| 你的实验/方法确实有硬伤 | ❌ 建议修改后改投 |

### Appeal Letter 模板

```
Dear Editor,

I am writing to respectfully appeal the decision on our manuscript entitled
"{{TITLE}}" (Manuscript ID: {{MANUSCRIPT_ID}}), which received an editorial
rejection on {{DATE}}.

We fully respect the editorial process and the reviewers' time. However, after
carefully reviewing the decision letter and the reviewer comments, we believe
there are substantive grounds for reconsideration:

[逐条列出申诉理由，对应每条误解/事实错误]
1. [具体理由一] — [证据]
2. [具体理由二] — [证据]

We have prepared a revised manuscript that addresses all factual concerns
raised during review.

We would be grateful if you could reconsider the decision, or alternatively,
advise on what additional work would be required for the manuscript to meet
the journal's standards.

Thank you for your time and consideration.

Sincerely,

{{CORRESPONDING_AUTHOR}}
{{CORRESPONDING_INSTITUTION}}
```

### 虚构示例

> **场景：** 论文投稿至 *International Journal of Production Research*，收到 Editorial Rejection。审稿人核心批评是"the proposed traceability architecture is not novel because RFID-based tracking systems already exist in manufacturing"。
>
> **申诉信片段：**
>
> "We respectfully note that Reviewer 2's assessment of novelty appears to be based on a misunderstanding of our contribution. The reviewer states that RFID-based tracking systems already address traceability — we agree. However, our paper does not propose RFID tracking; it proposes a **blockchain-based immutability layer** that sits above existing tracking systems (RFID, barcode, or manual entry) to ensure that once data is recorded, it cannot be altered during quality audits — a fundamentally different problem from data capture. This is clearly stated in our Abstract (Lines 12-15) and Section 1.2 (the second paragraph)."
>
> "To avoid future misunderstanding, we have revised the Introduction to more explicitly position our work *above* the data-capture layer. We have also added a comparison table (Table 1) distinguishing data capture, data management, and data immutability — three layers often conflated in the traceability literature."

---

## 五、修改时间估算 (Revision Time Estimation)

### 各类型修改的预期耗时

| 决定类型 | 通常截止日期 | 建议开始修改时间 | 建议完成时间 |
|---------|------------|---------------|------------|
| Minor Revision | 2-4 周 | 收到后 1-3 天 | 截止前 1 周 |
| Major Revision | 4-8 周 | 收到后 1 周内制定计划 | 截止前 2 周 |
| Reject & Resubmit | 通常无硬性截止，但 3 个月内为宜 | 收到后 2 周内评估是否值得 | 3 个月内 |
| Editorial Only | 1-2 周 | 收到后 1-2 天 | 截止前 3 天 |

### 修改时间分配建议（以 Major Revision 8 周为例）

```
Week 1:        阅读+分类+制定修改计划
Week 2-3:      处理 Major 意见（补充实验/重写框架）
Week 4:        处理 Minor 意见（补充分析/文献）
Week 5:        处理 Editorial 意见（语言润色/图表优化）
Week 6:        全文通读+一致性检查+撰写 Reply Letter
Week 7:        内部审阅（请同事/导师看一遍修改稿和回复）
Week 8:        最终修改+提交
```

### 如果无法在截止日期前完成

```
Dear Editor,

Regarding our manuscript "{{TITLE}}" (ID: {{MANUSCRIPT_ID}}), we are making
good progress on the revisions but require additional time to [具体原因,
如：complete the supplementary experiments / conduct the additional analyses
suggested by the reviewers].

We respectfully request an extension of [X weeks] beyond the current deadline
of {{DEADLINE}}. We anticipate submitting the revised manuscript by
{{NEW_DATE}}.

Thank you for your understanding.

Sincerely,

{{CORRESPONDING_AUTHOR}}
```

---

## 重要提示

1. **冷静期**：收到审稿意见后，特别是负面意见，先放 24 小时再读第二遍。情绪化回复是 Rebuttal 的大忌
2. **不要忽略正面意见**：在 Reply Letter 中也要回应审稿人的正面评价（"We thank the reviewer for the positive assessment of..."），这能展示你认真读了每一条
3. **审稿人不是敌人**：审稿人的目标是帮助提高论文质量。即使有误解，也是你的论文表述不够清晰的可能性更大
4. **编辑是最终决策者**：Reply Letter 的直接读者是编辑，审稿人是间接读者。要让编辑感受到你认真、专业、尊重审稿流程
