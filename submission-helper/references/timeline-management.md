# 投稿周期管理 (Submission Timeline Management)

> 跟踪投稿状态、了解等待时间、催稿邮件、撤稿邮件、一稿多投警示。所有示例中的期刊名、论文标题、作者名均为**虚构**。

---

## 一、投稿状态解读 (Understanding Submission Status)

投稿后的每一步，投稿系统都会显示一个状态。以下是常见状态及其含义：

| 状态 | 英文 | 含义 | 你的操作 |
|------|------|------|---------|
| 已提交 | Submitted / Manuscript Submitted | 稿件已成功上传，等待编辑部处理 | 检查所有文件是否正确上传 |
| 分配给编辑 | With Editor / Editor Assigned | 稿件已分配给某位编辑 | 等待，勿催 |
| 编辑初审中 | Editor Invited / With Editor | 编辑正在决定是否送审（部分期刊此阶段可能 desk reject） | 等待，此阶段通常 3-14 天 |
| 邀请审稿人中 | Reviewer Invited / Awaiting Reviewer Assignment | 编辑已决定送审，正在联系审稿人 | 等待 |
| 审稿中 | Under Review / In Review | 至少一名审稿人已接受邀请，正在审稿 | **最长等待阶段**，请耐心 |
| 所需审稿已完成 | Required Reviews Complete | 所有要求的审稿意见已返回，编辑正在做决定 | 通常 1-2 周内会收到决定 |
| 决定中 | Decision in Process / Awaiting Decision | 编辑正在撰写决定信 | 通常 3-7 天内出结果 |
| 已决定 | Decision Made / Decision Sent | 决定已发出，检查邮箱（含垃圾邮件箱） | 查看邮箱，依决定类型行动 |

---

## 二、各阶段预期等待时间 (Expected Wait Times)

以下等待时间基于虚构数据，仅作一般参考。实际等待时间因学科、期刊级别、投稿季节（如暑假）差异很大。

### 按学科分类

| 学科 | Editor Assigned | Reviewer Invited | Under Review | Decision | 总计（投稿到首次决定） |
|------|----------------|-----------------|-------------|---------|---------------------|
| 工程与技术 | 3-10 天 | 1-3 周 | 6-16 周 | 1-3 周 | 2-5 个月 |
| 管理/社科 | 5-14 天 | 1-4 周 | 8-20 周 | 1-3 周 | 3-6 个月 |
| 医学/生科 | 2-5 天 | 1-2 周 | 4-12 周 | 1-2 周 | 1.5-3.5 个月 |
| 计算机科学 | 3-7 天 | 1-3 周 | 5-14 周 | 1-2 周 | 1.5-4 个月 |

### 按期刊级别

| 期刊级别 | 典型审稿周期 |
|---------|------------|
| 顶级期刊（Nature/Science/Cell 级） | 2-4 个月（但 desk rejection 率极高，通常 3-7 天出结果） |
| 一区/二区期刊（领域旗舰刊） | 3-6 个月 |
| 三区/四区期刊 | 2-4 个月 |
| 开源期刊（Mega-journals，如 PLOS ONE 级） | 1-3 个月 |
| 中文核心期刊 | 2-6 个月（部分快讯/简报栏目可 1-2 个月） |

---

## 三、催稿邮件模板 (Inquiry Email Templates)

### 何时催稿？

催稿不是无代价的——过于频繁的催促可能给编辑留下不良印象。仅在以下情况下催稿：

| 情况 | 建议操作 |
|------|---------|
| 投稿后 2 周状态仍为 "Submitted" | 可礼貌询问是否收到稿件 |
| "Under Review" 超过期刊公布的**平均审稿周期的 1.5 倍** | 发第一次催稿邮件 |
| 第一次催稿后 3-4 周仍无回复 | 发第二次催稿邮件 |
| "Required Reviews Complete" 超过 3 周 | 发催稿邮件询问 |
| "Decision in Process" 超过 2 周 | 发催稿邮件询问 |

### 英语催稿邮件模板

```
Subject: Inquiry Regarding Manuscript Status — {{MANUSCRIPT_ID}}

Dear Editor {{EDITOR_NAME}},

I am writing to inquire about the status of our manuscript entitled
"{{TITLE}}" (Manuscript ID: {{MANUSCRIPT_ID}}), which was submitted on
{{SUBMISSION_DATE}}.

The submission system indicates that the manuscript has been [Under Review /
With Editor / Required Reviews Complete] since {{STATUS_DATE}}, which is
approximately {{WAIT_TIME}} ago.

I understand that the review process takes time, and I appreciate the
efforts of the editorial team and reviewers. I would be grateful if you
could provide an update on the expected timeline for a decision.

Thank you for your time and consideration.

Sincerely,

{{CORRESPONDING_AUTHOR}}
{{CORRESPONDING_INSTITUTION}}
Email: {{CORRESPONDING_EMAIL}}
```

### 中文催稿邮件模板

```
尊敬的编辑老师：

我是论文"{{TITLE}}"（稿号：{{MANUSCRIPT_ID}}）的通讯作者。本文于
{{SUBMISSION_DATE}} 投稿至贵刊，目前系统显示状态为"[审稿中/已修回/待决定]"，
至今已有 {{WAIT_TIME}}。

非常理解审稿工作需要时间，感谢编辑部和审稿专家的辛勤付出。冒昧来信，希望了
解一下稿件的大致处理进度和预期决定时间，以便我们做好后续安排。

感谢您的关注与帮助。

此致
敬礼

{{CORRESPONDING_AUTHOR}}
{{CORRESPONDING_INSTITUTION}}
{{CORRESPONDING_EMAIL}}
```

### 虚构示例

> **场景：** 论文 2025 年 3 月 1 日投稿至 *Engineering Applications International*，3 月 10 日变为 "Under Review"。期刊官网公布的"平均首次决定时间"为 8 周（即 5 月 1 日前后）。到 6 月 1 日（已超期 4 周，即 1.5 倍），发催稿邮件。
>
> **催稿邮件正文：**
>
> "I am writing to inquire about the status of our manuscript entitled 'A Digital Traceability System for Dished Head Manufacturing' (Manuscript ID: EAI-2025-0342), which was submitted on March 1, 2025. The submission system has indicated 'Under Review' since March 10, 2025 — approximately 12 weeks ago, which exceeds the average first-decision time of 8 weeks stated on the journal's website. I would be grateful if you could provide an update on the expected timeline."

---

## 四、撤稿邮件模板 (Withdrawal Email Templates)

### 什么情况下应当撤稿？

| 情况 | 是否建议撤稿 |
|------|------------|
| 发现论文中的重大数据错误 | ✅ 必须撤稿，修复后重新投 |
| 审稿超过 1 年无结果 | ✅ 可以撤稿改投 |
| 个人原因（离职/毕业，无法继续修改） | ✅ 可以撤稿 |
| 论文已被更高级别期刊接收 | ✅ 应当立即撤稿（避免一稿多投） |
| 审稿刚过正常周期 1-2 周就失去耐心 | ❌ 建议先发催稿邮件 |
| 审稿意见很好，只是修改太麻烦 | ❌ 建议坚持修改 |

### 英语撤稿邮件模板

```
Subject: Request to Withdraw Manuscript — {{MANUSCRIPT_ID}}

Dear Editor {{EDITOR_NAME}},

I am writing to request the withdrawal of our manuscript entitled
"{{TITLE}}" (Manuscript ID: {{MANUSCRIPT_ID}}), submitted on
{{SUBMISSION_DATE}}.

[选择最合适的理由]
- We have identified an error in the data analysis that requires substantial
  revision. We plan to correct this and resubmit as a new manuscript.

- After careful consideration, we have decided to revise the manuscript
  substantially based on internal review, which will result in a significantly
  different paper. We believe withdrawing and resubmitting as a new submission
  is more appropriate.

- Due to [legitimate reason, e.g., changes in author availability / unforeseen
  circumstances], we are unable to continue with the revision process at this
  time.

We apologize for any inconvenience this may cause and sincerely appreciate
the time the editorial team and reviewers have invested in our submission.

Thank you for your understanding.

Sincerely,

{{CORRESPONDING_AUTHOR}}
{{CORRESPONDING_INSTITUTION}}
Email: {{CORRESPONDING_EMAIL}}
```

### 中文撤稿邮件模板

```
尊敬的编辑老师：

我是论文"{{TITLE}}"（稿号：{{MANUSCRIPT_ID}}）的通讯作者，本文于
{{SUBMISSION_DATE}} 投稿至贵刊。

因 [撤稿理由，如：在进一步的数据核查中发现分析方法需要重大调整
/ 作者团队人员变动导致无法按时完成修改 / 经团队讨论决定对论文
进行大幅改写]，特此申请撤回该稿件。

由此给编辑部和审稿专家带来的不便，我们深表歉意，并衷心感谢各位
对本文付出的时间与精力。

感谢您的理解。

此致
敬礼

{{CORRESPONDING_AUTHOR}}
{{CORRESPONDING_INSTITUTION}}
{{CORRESPONDING_EMAIL}}
```

---

## 五、一稿多投规避提醒 (Avoiding Simultaneous Submission)

### ⚠️ 一稿多投是学术出版的红线

> **定义：** 将同一篇论文（或内容实质相同的论文）同时投稿到两个或更多期刊。这包括：
> - 完全相同的论文同时投多个期刊
> - 仅修改标题和摘要但核心内容不变
> - 不同语言版本同时投（如中文版投中文期刊、英文版投英文期刊，但数据相同）

### 为什么不能一稿多投？

1. **违反出版伦理** — COPE（出版伦理委员会）明确禁止
2. **浪费审稿资源** — 同一篇论文可能被多个期刊的审稿人审阅
3. **法律风险** — 如果两个期刊都接收了，你将面临版权纠纷
4. **学术声誉损害** — 被列入期刊黑名单，影响未来投稿

### 合法替代方案

| 你的情况 | 合法做法 |
|---------|---------|
| 急于发表，担心审稿慢 | 选择审稿周期短的期刊；或选择有"快速通道"的期刊 |
| 同时投中英文期刊 | **先投一个**，等结果后再投另一个。如果同一研究的中英文版本数据和分析有显著差异（如样本扩大、方法改进），可作为不同论文处理，但需在 Cover Letter 中说明与已有版本的关系 |
| 会议论文扩展投期刊 | 如果新增内容 ≥ 30%，多数期刊接受。必须在 Cover Letter 中声明"This paper is an extension of..."并引用会议论文 |
| 担心被拒后浪费时间 | 提前准备好 B 计划期刊；被拒后快速转投（格式调整通常 1-3 天） |

### 投稿记录管理建议

维护一个简单的投稿追踪表，避免误操作：

| 论文简称 | 当前状态 | 当前期刊 | 投稿日期 | B计划期刊 | 备注 |
|---------|---------|---------|---------|----------|------|
| 封头追溯系统 | Under Review | Journal of Applied Engineering | 2025-06-01 | Manufacturing Systems Review | — |
| 数字化转型案例 | 准备中 | — | — | Management Science Review | 目标9月投出 |
| 质量数据分析 | Rejected | — | — | Quality Engineering Journal | 已根据审稿意见修改，准备转投 |

---

## 重要提示

1. **每个期刊的投稿系统状态命名略有不同** — 以上状态类型为通用分类，具体以目标期刊系统显示为准
2. **暑假（6-8月）和年底假期（12月）审稿速度会明显变慢** — 在这些时段投稿，对审稿周期有合理的心理预期
3. **催稿邮件保持礼貌和专业** — 编辑也是研究者，理解等待的焦虑；一封礼貌的催稿邮件比抱怨和质问有效得多
4. **撤稿是严肃的操作** — 一旦撤稿，通常不能再以同一篇论文重新投回该期刊（除非编辑明确表示欢迎重投）
5. **做好被拒的心理准备** — 大多数论文的首次投稿都会被拒（顶级期刊的接受率通常 5-15%），这不代表你的研究不好。准备多个目标期刊，被拒后及时转投
