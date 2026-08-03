# Rebuttal 审稿意见回复框架 (Rebuttal Framework)

> 6大审稿意见类型 × 逐点回复结构 × 实际话术模板。所有审稿意见、论文标题、期刊名均为**虚构**。

---

## 总体回复结构 (Overall Rebuttal Structure)

无论审稿意见类型如何，Reply Letter 都应遵循以下结构：

```
┌──────────────────────────────────────────┐
│ 1. 致谢段 — 感谢编辑和审稿人               │
├──────────────────────────────────────────┤
│ 2. 修改总结表 — 一句话概括修改了哪些         │
├──────────────────────────────────────────┤
│ 3. 逐点回复（每一条审稿意见 = 一个回复块）   │
│    ├── 复述审稿意见（编号引用）              │
│    ├── 我们的回应（同意/部分同意/解释）       │
│    ├── 具体修改措施                         │
│    └── 修改位置标注（页/行号）               │
├──────────────────────────────────────────┤
│ 4. 收尾 — 希望修改令审稿人满意              │
└──────────────────────────────────────────┘
```

---

## 回复语气指南 (Tone Guidelines)

| 场景 | ✅ 推荐表达 | ❌ 避免表达 |
|------|------------|------------|
| 感谢意见 | "We thank the reviewer for this insightful comment." | "Thanks for pointing this out." |
| 同意修改 | "We agree with the reviewer and have revised accordingly." | "OK, we fixed it." |
| 部分同意 | "We appreciate the reviewer's concern. While we agree that..., we would like to clarify that..." | "The reviewer is partially wrong." |
| 礼貌坚持 | "We respectfully maintain that..., and we provide additional justification below." | "We disagree. Our method is better." |
| 解释局限 | "We acknowledge this limitation and have added a discussion in Section X." | "This is not really a problem." |
| 超出范围 | "We agree this is an important direction, but it lies beyond the scope of the current study." | "This isn't relevant to our paper." |

---

## 类型一：方法论质疑 (Methodology Concerns)

> 审稿人质疑你的实验设计、分析方法、样本量等。

### 回复策略

1. **如果质疑合理** → 补充实验/分析 + 引用文献佐证 + 若无法补充则承认局限
2. **如果质疑有误解** → 澄清方法细节 + 提供额外解释 + 引用原文已述内容
3. **如果质疑核心方法** → 补充验证 + 引用权威文献支持你的方法选择

### 回复模板

```
We thank the reviewer for raising this important methodological concern.

[如果是合理质疑 + 可以补充]
We agree that [具体质疑内容] could strengthen our analysis. In response, we have
conducted [补充的实验/分析]. The results are presented in [新增的图/表/段落] and
discussed in Section [X], Page [Y], Lines [Z1-Z2].

[如果是质疑有误解]
We appreciate the reviewer's careful reading. We would like to clarify that
[解释方法细节], as described in the original manuscript (Section X, Lines Y-Z).
To avoid future misunderstanding, we have revised the relevant text to make
this point more explicit (see Section X, Lines Y1-Y2).

[如果无法补充，承认局限]
We acknowledge this limitation. While [理想做法] would be ideal, it was not
feasible in our study due to [合理原因]. We have now added a discussion of this
limitation in Section [X] and suggested it as a direction for future work.
```

### 虚构示例 (Fictional Example)

> **审稿意见：** "The sample size of 15 manufacturing firms is insufficient to support the generalizability claims. A power analysis should be provided."

> **Reply Letter 回复：**
>
> We thank the reviewer for this important comment on sample size.
>
> We agree that a formal power analysis would strengthen the methodological rigor. In response, we have:
> (1) Conducted a post-hoc power analysis using G*Power 3.1, which shows that with N=15 and a medium effect size (Cohen's d = 0.6), the achieved power is 0.82 — exceeding the commonly accepted threshold of 0.80. This analysis is now presented in Section 3.4 (Page 12, Lines 285-298).
> (2) Tempered our generalizability claims throughout the manuscript. We now state that the findings are "transferable to similar small-to-medium manufacturing contexts" rather than "broadly generalizable." The revised language appears in Section 5.1 (Page 22, Lines 540-552).
>
> We acknowledge that a larger, multi-industry sample would further strengthen external validity, and we have added this as a future research direction in Section 5.3 (Page 25, Lines 610-618).

---

## 类型二：创新性质疑 (Novelty Questions)

> 审稿人认为你的贡献不够新颖，或与已有工作区分度不足。

### 回复策略

1. **精准定位贡献** — 不要泛泛而谈，说清楚你和已有工作的**层级差异**（你处于更高层次/不同视角/新场景）
2. **对比已有工作** — 用表格对比你的方法和已有方法的核心区别
3. **强调不足** — 礼貌但坚定地指出已有工作在你关注的维度上的不足

### 回复模板

```
We thank the reviewer for encouraging us to better articulate the novelty of
this work.

We respectfully clarify that our contribution differs from prior work in the
following key aspects:

1. [贡献维度一] — While [已有方法A] focuses on [已有方法的关注点], our work
   addresses [本工作的独特关注点], which has not been explored in the existing
   literature.

2. [贡献维度二] — Unlike [已有方法B] that [已有方法的做法], we propose
   [本工作的做法], which enables [额外能力/效果].

To make these distinctions clearer, we have added a comparative summary table
(Table [X]; Section [Y], Page [Z]) that highlights the differences between our
approach and representative prior works across [对比维度].
```

### 虚构示例 (Fictional Example)

> **审稿意见：** "Digital twin in manufacturing has been extensively studied. The proposed digital twin framework for dished head production does not appear to offer substantial novelty over existing work by Chen et al. (2022) and Liu et al. (2023)."

> **Reply Letter 回复：**
>
> We thank the reviewer for this comment and the opportunity to better articulate our contribution.
>
> We respectfully clarify that our work differs from Chen et al. (2022) and Liu et al. (2023) along three critical dimensions:
>
> 1. **Process specificity**: Chen et al. (2022) proposed a generic digital twin framework for discrete manufacturing — applicable to assembly lines with interchangeable parts. Dished head manufacturing involves metal forming processes (stamping, spinning) where the material undergoes irreversible deformation, requiring a fundamentally different data model. Our contribution addresses this under-studied process type.
>
> 2. **Traceability integration**: Liu et al. (2023) focused on real-time monitoring via digital twin, but did not integrate quality traceability — a regulatory requirement in pressure vessel component manufacturing. Our framework is the first to combine digital twin visualization with full-process traceability, enabling compliance with ASME BPVC Section VIII.
>
> 3. **Industrial validation**: While prior work validated digital twins in laboratory settings or simulated environments, our system has been deployed and validated on an active production line processing 5,000 tons of dished heads per year.
>
> To make these distinctions clearer, we have added a comparative table (Table 2; Section 2.3, Page 7) summarizing the differences between our approach and 8 representative prior works across 6 dimensions (process type, traceability, real-time capability, industrial validation scale, standard compliance, and data model).

---

## 类型三：写作/表达问题 (Writing/Presentation)

> 审稿人指出语言问题、组织结构混乱、图表不清等。

### 回复策略

- 逐条确认修改 — 不要笼统说"我们改了"，每条列出来
- 标注修改位置 — 页面号 + 行号
- 如果审稿人列举了多个语言问题 → 建议声明"全文已由 native English speaker 润色"（如确实做过）

### 回复模板

```
We thank the reviewer for the careful reading and constructive suggestions on
improving the presentation.

We have addressed each point as follows:

[逐条回复]
(1) [审稿人指出的问题一] → Revised as suggested. See Section [X], Page [Y],
    Lines [Z1-Z2].

(2) [审稿人指出的问题二] → We have restructured [段落/章节] to improve clarity.
    The revised text is in Section [X], Page [Y].

(3) [审稿人指出的问题三] → [具体的措辞修改]. See Page [Y], Line [Z].

In addition, the entire manuscript has been carefully proofread [or: has been
reviewed by a professional English editing service] to address language issues
throughout.
```

### 虚构示例 (Fictional Example)

> **审稿意见：** "Section 2 is overly long and difficult to follow. The literature review mixes background with related work. Several paragraphs (e.g., Page 6, Paragraph 2) contain run-on sentences that obscure the argument."

> **Reply Letter 回复：**
>
> We thank the reviewer for these constructive suggestions to improve readability.
>
> We have addressed each point as follows:
>
> (1) **Section 2 restructuring**: We have split the original Section 2 into two sections: Section 2 ("Background: Dished Head Manufacturing Processes") provides essential domain context, and Section 3 ("Related Work") surveys the academic literature on digital traceability and MES systems. This separation makes the argument flow clearer.
>
> (2) **Run-on sentences**: We have revised Page 6, Paragraph 2 into three shorter, focused sentences. The revised text now reads: "Traditional traceability in dished head manufacturing relies on paper-based work orders. These records are manually transcribed into ERP systems, introducing a median delay of 4.7 hours. This gap between physical production and digital record creates a blind spot in quality audits." (Page 7, Lines 142-148).
>
> (3) **Overall proofreading**: The entire manuscript has been reviewed for language clarity, and we have corrected several other instances of overly complex sentence structures identified during this revision.

---

## 类型四：实验/数据问题 (Experimental/Data)

> 审稿人要求补充实验、质疑数据可靠性、要求开放数据等。

### 回复策略

1. **可补充的实验** → 做实验 + 报告结果
2. **无法补充的实验** → 解释原因 + 承认局限 + 列为未来工作
3. **数据可靠性** → 提供额外证据（原始数据统计/第三方验证/审计轨迹）
4. **数据开放** → 如可行则提供；如不可行则说明原因（商业机密/隐私/伦理约束）

### 回复模板

```
We thank the reviewer for this comment regarding [实验/数据方面].

[如果补充了实验]
In response, we have conducted additional experiments on [实验内容]. The results
are summarized in [Table/Figure X] (Page Y). [核心发现]. These additional results
further support our original conclusions.

[如果无法补充实验]
We acknowledge the value of [审稿人建议的实验]. However, [合理原因 — 设备不可用/
数据不可获取/时间限制/超出论文范围]. We have added a discussion of this point
in Section [X] (Page Y) and identified it as an important direction for future
investigation.

[如果开放数据]
In support of open science, we have made [数据集/代码] publicly available at
[repository URL / as Supplementary Material]. The data documentation is provided
in [Supplementary File X].
```

### 虚构示例 (Fictional Example)

> **审稿意见：** "The authors claim that their blockchain-based traceability system ensures data immutability, but no empirical evidence is provided. At minimum, a tampering-attempt experiment should be conducted and reported."

> **Reply Letter 回复：**
>
> We thank the reviewer for this rigorous and important suggestion.
>
> In response, we have designed and conducted a tampering-attempt experiment as follows:
>
> **Experiment design**: We simulated 3 types of tampering attempts on historical traceability records: (a) direct database modification, (b) hash chain break attempt, and (c) consensus bypass attempt. Each type was tested across 100 randomly selected records.
>
> **Results**: All 300 tampering attempts were detected by the system. Direct modifications triggered instant hash mismatch alerts (mean detection time: 0.3s). Hash chain breaks were detected at the next block verification (within block interval of 10s). Consensus bypass attempts were rejected by the multi-node validation protocol. These results are presented in new Section 4.3 ("Tamper Resistance Validation," Pages 16-17) and summarized in Table 5.
>
> **Data availability**: The tampering experiment scripts and the 300 test records (with synthetic tampering operations) are provided as Supplementary Material S2, enabling full reproducibility.

---

## 类型五：范围/定位问题 (Scope/Positioning)

> 审稿人认为研究范围太窄/太宽、定位不清、与期刊方向不匹配等。

### 回复策略

1. **重新定位** — 在引言中更明确地界定研究边界
2. **承认边界** — 说明你选择的范围是经过深思熟虑的（什么在研究范围内，什么不在）
3. **建议方向** — 将审稿人建议的扩展方向列为未来工作

### 回复模板

```
We thank the reviewer for this thoughtful comment on the scope and positioning
of our work.

We agree that clearly defining the boundaries of this study is important.
In response, we have:

(1) Added an explicit scope statement in the Introduction (Section 1, Page 3,
    Lines [X-Y]): "This study focuses on [研究范围]. We do not address [明确排除
    的内容], which warrants separate investigation."

(2) Re-positioned our contribution within the broader literature. Specifically,
    [说明你的工作在更大的研究版图中的位置].

(3) Acknowledged the reviewer's suggestion to consider [审稿人建议的方向] as a
    meaningful extension, which we now discuss in Section [X] (Page Y) as a
    direction for future work.
```

### 虚构示例 (Fictional Example)

> **审稿意见：** "The paper claims to present a 'full-process digital traceability system,' but it only covers the manufacturing phase. Pre-manufacturing (raw material sourcing) and post-manufacturing (installation, in-service inspection) are not addressed. The title is therefore misleading."

> **Reply Letter 回复：**
>
> We thank the reviewer for this careful observation regarding scope.
>
> We agree that the term "full-process" should be more precisely defined. In response, we have:
>
> (1) **Revised the title** to: "A Digital Traceability System for the Manufacturing Phase of Dished Head Production: Design and Industrial Application." This accurately reflects the actual scope of our work.
>
> (2) **Added an explicit scope statement** in Section 1 (Page 3, Lines 55-62): "In this study, 'manufacturing phase' encompasses all operations from incoming raw material inspection to final product certification — the span over which the manufacturer has direct operational control. Raw material sourcing and post-delivery lifecycle stages, while important, involve different stakeholders (suppliers, end-users) and data governance regimes, and are beyond the scope of the current system."
>
> (3) **Acknowledged the reviewer's suggestion** that extending traceability to pre- and post-manufacturing phases would be a valuable direction. We now discuss this in Section 6.2 (Page 26, Lines 648-660), noting that integrating supplier quality certificates and in-service inspection records would require standardizing data exchange protocols between organizations — a significant undertaking we identify as future work.

---

## 类型六：拒稿倾向意见 (Rejection-Leaning Comments)

> 审稿人整体评价负面，但编辑给了修改机会（Major Revision 或 Reject & Resubmit）。

### 回复策略

这是**最难回复的类型**，需要：
1. **逐点回应** — 不能跳过任何一条批评，即使是语气不好的
2. **展示修改量** — 用修改总结表展示你做了大量工作
3. **争取修改机会** — 如果审稿人说"fundamentally flawed"，你需要有力的反驳或大幅修改
4. **礼貌坚持** — 不卑不亢，用证据说话

### 回复模板

```
We sincerely thank the reviewer for the thorough and critical evaluation of
our manuscript. We have taken every comment seriously and have substantially
revised the manuscript in response.

Below, we provide a point-by-point response to each concern. To facilitate the
reviewer's assessment, we also provide a Summary of Revisions table at the
end of this letter.

[逐条回复，遵循前面5种类型的策略]

**Summary of Major Revisions:**
| Reviewer Concern | Our Response | Manuscript Changes |
|-----------------|-------------|-------------------|
| Concern 1 | [简要回应] | [修改位置和内容] |
| Concern 2 | [简要回应] | [修改位置和内容] |
| ... | ... | ... |

We hope that these revisions address the reviewer's concerns. We remain open
to further suggestions and are committed to bringing this manuscript to the
standard expected by {{JOURNAL_NAME}}.
```

### 虚构示例 (Fictional Example)

> **审稿人2 (整体评价负面)：** "The paper addresses a practical problem but lacks theoretical depth. The proposed system is essentially an engineering implementation with no scientific contribution. The evaluation is anecdotal rather than rigorous. I cannot recommend publication in its current form."

> **Reply Letter 回复：**
>
> We sincerely thank Reviewer 2 for the thorough and candid evaluation. We have taken these concerns seriously and have substantially revised the manuscript.
>
> Below is our point-by-point response:
>
> ---
>
> **Concern 1: "The paper lacks theoretical depth; it is an engineering implementation."**
>
> We appreciate this critique and acknowledge that the original manuscript insufficiently articulated the theoretical underpinnings. In response, we have:
>
> (a) Added a new theoretical framework (Section 2.2, Pages 5-7) that formalizes the traceability problem in non-conforming-product discrete manufacturing as a "state-transition completeness" problem. We define three completeness conditions (observability, immutability, auditability) and prove that our system architecture satisfies all three.
>
> (b) Generalized our approach beyond dished head manufacturing. In new Section 5.2 (Pages 23-25), we show how the proposed traceability architecture applies to other non-conforming-product domains (forged components, cast parts, welded assemblies), each with different state-transition graphs but satisfying the same completeness conditions.
>
> **Concern 2: "The evaluation is anecdotal rather than rigorous."**
>
> We acknowledge that our original evaluation relied primarily on descriptive case reporting. To strengthen methodological rigor, we have added:
>
> (a) A quasi-experimental design comparing the digital traceability system against the paper-based baseline across 1,247 production batches. We report standardized effect sizes (Cohen's d) for time efficiency (d = 2.31, large effect) and data accuracy (d = 1.87, large effect). See Section 4.2 (Pages 14-16).
>
> (b) An inter-rater reliability analysis for the quality audit outcome (Fleiss' κ = 0.91 between digital and paper-based audit results), addressing potential confirmation bias. See Section 4.3 (Page 17).
>
> **Concern 3: "Cannot recommend publication in its current form."**
>
> We fully understand this assessment of the original submission and hope the substantial revisions — including the new theoretical framework, generalized applicability analysis, and rigorous evaluation design — bring the manuscript to the level expected by the journal.
>
> ---
>
> **Summary of Major Revisions:**
>
> | Reviewer Concern | Our Response | Manuscript Changes |
> |---|---|---|
> | Lack of theoretical depth | Formalized traceability as state-transition completeness (new framework) | New Section 2.2 (5 pages) |
> | Engineering-only contribution | Generalized to non-conforming-product manufacturing domain | New Section 5.2 (3 pages) |
> | Anecdotal evaluation | Added quasi-experimental design + effect sizes + inter-rater reliability | Revised Section 4 (5 pages) |
> | Various minor issues | All addressed as detailed above | Throughout |

---

## 修改标记规范 (Revision Marking Conventions)

### 使用修订模式（Track Changes）

> **强烈建议**：使用 Word 的"修订"（Track Changes）模式或 LaTeX 的 `changes` 包，让审稿人清晰看到所有改动。

### 颜色标注（如果不用修订模式）

```
新增文本：蓝色字体
删除文本：红色删除线
修改文本：绿色高亮
```

### 页/行号引用规范

```
正确 ✅：
- "See Section 3.2, Page 9, Lines 215-228."
- "The revised text appears on Page 14, Paragraph 3."
- "We have added Figure 5 (Page 18)."

错误 ❌：
- "We changed it in the paper." （太模糊）
- "See the revised manuscript." （审稿人找不到在哪）
```

### Response Letter 中引用修改文本

```
We have revised the relevant paragraph as follows
（修改后的文本以缩进/引用块形式展示）:

    The digital traceability system achieved a mean query response time
    of 0.42s (SD = 0.08) across 10,000 simulated audit queries, representing
    an 85.3% reduction compared to the manual record retrieval baseline
    (mean = 2.86s, SD = 1.34; t(9999) = 183.4, p < .001, Cohen's d = 2.57).

(Page 15, Lines 356-362; revised text)
```

---

## Rebuttal Cover Letter 模板 (用于 Resubmission)

当提交修改稿时，需要一封**Resubmission Cover Letter**，随修改稿和Response to Reviewers 一起提交：

```
Dear Editor,

We are pleased to resubmit our revised manuscript entitled "{{TITLE}}"
(Manuscript ID: {{MANUSCRIPT_ID}}) for consideration in {{JOURNAL_NAME}}.

We sincerely thank you and the reviewers for the constructive and thorough
evaluation of our manuscript. The comments have significantly improved the
quality and clarity of this work.

We have carefully addressed all comments in a point-by-point manner in the
attached "Response to Reviewers" document. All revisions are marked using
Track Changes in the revised manuscript for ease of review.

The key revisions include:
[3-5 bullet points summarizing the most important changes]

We believe the revised manuscript now meets the standards of {{JOURNAL_NAME}}
and hope that the reviewers find our responses satisfactory.

Thank you for your continued consideration.

Sincerely,

{{CORRESPONDING_AUTHOR}}
{{CORRESPONDING_INSTITUTION}}
Email: {{CORRESPONDING_EMAIL}}
```

---

## 重要提示

1. **回复审稿意见不是辩论赛** — 即使审稿人明显说错了，也先感谢再解释。"We thank the reviewer..." 开头永远不会错
2. **不要把问题留给编辑判断** — 如果两个审稿人意见冲突，不要简单说"审稿人A说X，审稿人B说Y，请编辑决定"。你应该给出你的判断和建议
3. **不要忽略任何一条意见** — 哪怕只是说"Thank you for pointing out this typo; we have corrected it on Page X"
4. **修改标注必须清晰** — 审稿人会快速扫描，找不到修改位置很可能导致再次负面评价
5. **回复要自己写，不能套用模板** — 本框架提供结构和话术参考，但具体内容必须基于审稿意见定制。生硬的模板回复会被审稿人一眼识破
