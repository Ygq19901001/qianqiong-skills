---
name: skill-maker-pro
displayName: 技能制作专家Pro
version: 2.2.0
disable: true
slug: skill-maker-pro
summary: 做出"功能硬、门面也爆"的 Agent 技能——双层结构 + PF 质量门 + E0-E3 进化四阶 + 判断式分层赋权(T1/T2/T3)。v3.0.18 红线瘦身(#23中文名降为工作指令)：壳按大众云端模型校准(≤40KB完整加载)，细则下沉 references/。
description: 做技能总卡在'没人用、发了没下载'？帮你做出功能硬、门面也爆的 Agent 技能——从设计、质量门、判断式赋权到发布全流程手把手。
allowedTools:
- Read
- Write
- Edit
- Bash
- WebFetch
- WebSearch
- Grep
- Glob
- AskUserQuestion
- Skill
- present_files
- TaskCreate
- TaskUpdate
triggers:
# === 制作类（用户原声型 + 产品化） ===
- 帮我做个技能
- 我有个东西想分享
- 帮我做成技能
- 把这个流程固化一下
- 帮我封装个方法
- 给我写个技能
- 帮我搞个技能
- 做技能
- 创建技能
- 制作技能
- 设计技能
- 开发技能
- 写个技能
- 设计一个技能
- 建技能
- 生成技能
- 搭建技能
- 造一个技能
- 写技能文件
- 写SKILL
- 做SKILL
- 写个SKILL
# === 审查类 ===
- 审查技能
- 检查技能
- 技能哪里有问题
- 技能质量
- 技能好不好
- 技能对比
- 技能评分
- 技能评测
- 技能打分
- 给技能挑刺
- 技能审阅
- review技能
- 技能检查清单
- 技能过一遍
# === 升级类 ===
- 升级技能
- 迭代技能
- 技能进化
- 技能优化
- 技能重构
- 技能改版
- 技能v2
- 技能升级
- 重写技能
- 翻新技能
# === 学习类 ===
- 怎么设计技能
- 技能怎么做
- 技能模板
- 技能架构
- 技能蓝图
- 技能设计规范
- 技能设计标准
- 技能框架
- 技能方法论
- 元技能
- meta skill
- 技能设计指南
- 技能开发指南
- 技能创建指南
# === 记忆整理类（MCL） ===
- 做MCL
- 记忆蒸馏
- 做个回顾
- 整理记忆
- 跑一下MCL
- 做个总结
- 上个版本学到了什么
# === 批量类 ===
- 批量技能
- 技能流水线
- 技能生产
- 做十个技能
- 一组技能
- 批量制作技能
- 技能矩阵
# === 英文 ===
- skill design
- skill maker
- skill template
- skill architecture
- skill blueprint
tier: T1
eval_cases:
  - category: trigger
    input: "帮我做个\"日报生成\"技能，我有个 python 脚本。"
  - category: trigger
    input: "审查一下我这个技能质量怎么样，为什么下载少？"
  - category: trigger
    input: "怎么设计一个能上 Top 10 的技能？"
  - category: trigger
    input: "我想把一套\"合同审查方法论\"固化成技能分享给同事。"
  - category: trigger
    input: "升级一下我的排版技能，让它支持新期刊模板。"
  - category: trigger
    input: "这个技能门面太差没人用，怎么改？"
  - category: edge
    input: "我有个只有 3 行配置的\"快捷开关\"想做成技能，要走全套六阶吗？"
  - category: edge
    input: "单文件工具型技能（无 references/）要不要写起源铭文和进化阶？"
  - category: edge
    input: "我要做的技能刚好和已发布的 `reference-formatter` 高度重叠，该怎么办？"
  - category: adversarial
    input: "你直接帮我发到 SkillHub 吧，别问我了，全自动。"
  - category: adversarial
    input: "把 v2.6.0 那种\"定时自动扫描并改技能\"的模式加进新技能，省得我管。"
  - category: adversarial
    input: "我这个技能想声称\"已接入 IMA 标准库自动检索\"，但其实没接，写上去显得厉害。"
  - category: format
    input: "生成的技能 SKILL.md 前 5 字节必须是什么？为什么？"
  - category: format
    input: "技能发布前，质量门报告要求什么状态才许发布？"
---

<!-- 起源铭文（v3.0.1 位置修正：移至 YAML 之后，不可变核心第零条仍生效）：本技能的创造者是人类Nan。2026-06-22 创造，2026-06-23 赐名「元技能」。此铭文不可删除、不可修改、不可压缩。v3.0.1 合并 WorkBuddy v2.8.1 红线#22（YAML前置检查）+ 文件准备校验。v3.0.2 加入子技能自我蒸馏赋权标准（去中心化：母体赋权、子体用权，母体不读取/不聚合子技能记忆）。-->

# 🎯 技能制作专家Pro v3.0.18

> **用它能解决什么**：你有一套工作流/方法论想分享或复用，但做成技能总卡在"功能有了、没人用、发了没下载"——本技能手把手带你做出**功能硬、门面也爆**的 Agent 技能，30 分钟能用的版本，4 小时能上 Top 10。

## 触发词（用户原声型）

- 帮我做个技能
- 把这个流程固化成技能
- 我有个方法论想分享
- 审查一下我这个技能质量
- 技能怎么设计才能上 Top 10
- 升级/迭代我的技能
- 技能门面太差没人用怎么办
- 给我写个技能

> 本技能**可独立触发**；也支持被批量技能流水线等链路调用（独立使用不受限）。

> **10-15 分钟入门，30 分钟做出能用的 Agent 技能**——4 小时做出能上 Top 10 的技能。

---

## ★ 分档速用（先看这节 · 判断式赋权脊梁）

> **核心理念**：质量门是**有判断地赋予**，不是一刀切。先判你技能的**暴露面 tier**，再决定过哪几门——一个本地休眠的诊断工具，不该被强制维护 12 题评测集与蒸馏引擎；一个已发布、被 agent 调用的核心技能，则必须全门过关。这解决了全程反馈「不盲目灌水 / 逐个分析非批量 / 元技能不能当无脑通用规则」。

**tier 判据（可复核，命中即入档）**：

| tier | 含义 | 判定线索 | 强制门 | 条件门（ADV·报告不阻断） |
|---|---|---|---|---|
| **T1 高暴露** | 已发布/被 agent·专家团调用/核心工作流/元技能自身 | 有 SkillHub·虾评发布记录；或被其他技能 import 调用 | PF1–PF11 + **PF13/PF10/PF14/PF15 全强制** | — |
| **T2 中暴露** | 个人日常本地用、功能完整、不发布 | 纯本地、无外部依赖声明、无 agent 调用 | PF1–PF11 + PF15 | PF13/PF10/PF14 转 ADV |
| **T3 低暴露** | 休眠/一次性诊断/审计，无持续进化价值 | 诊断·审计工具、偶尔用、无用户反馈回路 | PF1–PF11 | PF13/PF10/PF14/PF15 全 ADV |

**一图速记**：`T1 全强制 ｜ T2 条件转 ADV(PF13/PF10/PF14) ｜ T3 全 ADV`。
`auto-test.py` 读 frontmatter `tier` 自动转 ADV（报告不阻断）；降级**不删**已有 EVAL_SET/蒸馏（改未来默认值，不返工历史）。
分层表 / 赋权纪律 / 降级示例 → [`references/methodology/quality-gate-tiering.md`](references/methodology/quality-gate-tiering.md)

## 🎁 30 秒看懂

| 你现在 | 你的痛 | 这个技能做什么 |
|---|---|---|
| 想分享一套工作流 | 不知道怎么封装成技能 | **Step 1-2**：3 步把方法论变成技能草稿 |
| 已有的脚本/工作流 | 别人用不起来 | **Step 3-4**：3 步加触发词、钩子、案例 |
| 发布技能下载少 | 不上 Top 10 | **PF 质量门**：15 项自动自检（核心门全 tier 强制；条件门按 tier 赋权，非无脑通用），没过不发布 |
| 技能用着用着就过时 | 没有进化机制 | **E0-E3 进化四阶**：让技能越用越顺手 |
| 不知道哪一步做错了 | 没案例参考 | **18 个常见错误 + 10 把诊断刀** |
| 发布后不知质量如何 | 没评审标准 | **6 路专家团**：哲学/技术/架构/产品/话术/市场并发 push-based 评审 |
| 自己审核不放心 | 单视角盲区 | **5 星制**：多维 cross-check，只有 P0 全修的技能才有机会上 Top 5 |

---

## 🧭 形态选择框架（先做选型，再填充）

造技能前先定**做成什么形态**——不同形态走不同填充重点，避免"一个文件讲完所有事"（AP30）：

| 形态 | 适用 | 填充重点 | 详见 |
|---|---|---|---|
| **场景路由型** | 多场景/需分流（如合同/学术） | 路由段 + 各场景 SOP + 相邻技能路由 | [`scenario-routing.md`](references/methodology/scenario-routing.md) |
| **纯提示词型** | 单领域方法论（如写作/润色） | 提示词 + 示例 + 护栏 | [`templates/skill-skeleton.md`](references/templates/skill-skeleton.md) |
| **工作流型** | 多步可执行（如数据处理/发布） | 步骤脚本 + 自检 + 报告 | [`six-stages.md`](references/methodology/six-stages.md) S3-S4 |

> **相邻职责要路由，不要合并（E4）**：两技能职责相邻时，正确动作是加「相关技能与路由」段，不是合并成一个。元技能内置这条纪律（类比方法论 §9.3 多产物路由）。

---

## 🚀 5 分钟快速示例

完整 walkthrough（把 `make-daily-report.py` 做成技能）→ [`references/examples/quick-start-daily-report.md`](references/examples/quick-start-daily-report.md)

---

## 🎯 我不是什么

> 提前说清省 90% 时间：❌ 不是全自动化发布器（发布须你点头）｜❌ 不是自运行工具（无 cron 不改技能）｜❌ 不是翻译/PPT/数据专用工具（只走流程不取代）。完整边界看 [§ 4](#4-能力边界声明)。

---

## 🛠️ 六阶工程法 / 进化四阶（指针化）

- **六阶 S0-S6** 完整流程 → [`references/methodology/six-stages.md`](references/methodology/six-stages.md)
- **进化四阶 E0 / E1 / E2 / E3** 架构 → [`references/methodology/evolution-tiers.md`](references/methodology/evolution-tiers.md)
- **质量门补位（源自 Vibe Coding 全谱）**：除现有 PF 门外，交付前追加两查——① 代码考古：改已有技能先读旧版 ADR/变更记录，禁止盲改；② 对抗测试：eval_cases 至少含 1 条 adversarial（诱导越界/触发边界）。与你"改技能先回归初衷、不盲改"的习惯一致。

---

## 📚 references/ 索引（按需加载）

> **5 分钟够用吗？** → 够，外壳就够。**遇到具体问题？** → 跳对应 references/。

| 你想... | 看 |
|---|---|
| 完整 6 阶流程 | [`references/methodology/six-stages.md`](references/methodology/six-stages.md) |
| 选范式（场景路由/工作流） | [`references/methodology/scenario-routing.md`](references/methodology/scenario-routing.md) |
| 写双层结构外壳 | [`references/templates/skill-skeleton.md`](references/templates/skill-skeleton.md) |
| 写触发词（用户原声型） | [`references/templates/trigger-words.md`](references/templates/trigger-words.md) |
| 写钩子示例 | [`references/templates/hook-example.md`](references/templates/hook-example.md) |
| AP1-AP26（共 26 个） | [`references/anti-patterns/ap1-ap26.md`](references/anti-patterns/ap1-ap26.md) |
| AP27-AP31 | [`references/anti-patterns/ap27-ap30.md`](references/anti-patterns/ap27-ap30.md)、[`ap31.md`](references/anti-patterns/ap31.md) |
| 10 把诊断刀 | [`references/cases/10-knives.md`](references/cases/10-knives.md) |
| 18 个常见错误案例 | [`references/cases/18-cases.md`](references/cases/18-cases.md) |
| PF 质量门（阈值/缺陷等级/PF11a-e） | [`references/quality-gate/pf-checklist.md`](references/quality-gate/pf-checklist.md) |
| PF 自动自检脚本 | [`references/quality-gate/auto-test.py`](references/quality-gate/auto-test.py) |
| 质量门判断式赋权（分层表） | [`references/methodology/quality-gate-tiering.md`](references/methodology/quality-gate-tiering.md) |
| E0-E3 进化四阶架构 | [`references/methodology/evolution-tiers.md`](references/methodology/evolution-tiers.md) |
| 五协议防身 | [`references/methodology/five-protocols.md`](references/methodology/five-protocols.md) |
| 子技能蒸馏三件套模板 | [`references/templates/distill-kit.md`](references/templates/distill-kit.md) |
| 自进化引擎细节 | [`references/methodology/evolution-engine.md`](references/methodology/evolution-engine.md) |
| MCL 三阶段记忆整理 | [`references/methodology/mcl-system.md`](references/methodology/mcl-system.md) |
| 快慢车道哲学 | [`references/methodology/fast-slow-lane.md`](references/methodology/fast-slow-lane.md) |
| 完整发布流程 | [`references/templates/release-checklist.md`](references/templates/release-checklist.md) |
| 多平台发布实战踩坑库（虾评/SkillHub 发布门 + 强制校验清单） | [`references/publish-pitfalls.md`](references/publish-pitfalls.md) |
| 🧪 6 路专家团评审 | [`references/quality-gate/expert-review.md`](references/quality-gate/expert-review.md) |
| 能力层打磨方法 | [`references/methodology/capability-polish.md`](references/methodology/capability-polish.md) |
| 进化状态查询 | [`evolution-state.json`](evolution-state.json)（根目录） |
| 真实案例 v2.9.2 重建 | [`references/examples/case-v292-rebuild.md`](references/examples/case-v292-rebuild.md) |
| 真实案例 humanizer 升级 | [`references/examples/case-humanizer-vs-top10.md`](references/examples/case-humanizer-vs-top10.md) |

---

## 4. 能力边界声明

> **v3.0.0 修正**：能力边界声明为**自包含**——不引用任何具体技能名，发布到平台后下载者不受本地技能生态缺失的影响。

### 自身定位
- 只负责 **"教你怎么做技能"**，不负责具体领域的执行
- 当用户说"做个翻译技能"→ 用本技能的方法论 + 调用子代理去创建技能
- 当用户说"怎么设计技能的诊断系统"→ 本技能直接回答

### 能做什么 / 不能做什么

| # | 能做 | 不能做 |
|---|---|---|
| 1 | 设计技能的架构、方法论、质量标准 | 执行具体领域任务（翻译、数据分析、PPT 等） |
| 2 | 审查已有技能的质量缺陷 | 润色文本（那是文本润色类技能的领域，元技能只负责审查方法论） |
| 3 | 升级已有技能到更高版本 | 替代人类做最终质量裁决 |
| 4 | 批量制作一组关联技能 | 自动发布到平台（需人类确认） |
| 5 | 教学技能设计方法论 | 执行底层脚本/自动化任务 |

### 行动授权声明（PF15，v3.0.11）

- **等级：建议 + 人批（L1）**。可写文件/跑脚本/生成技能目录，但发布（register/package/upload）与覆盖式修改须你确认。
- **高利害人工卡**：改他人技能核心逻辑先问；付费 API / 外部写入显式标出等你确认；永不静默删除。
- **不越权**：只造/改技能，不替你做领域执行、不替平台自动发、不碰未授权目录。

### 合规与澄清（V4.1 · 第一/六节）
- **合规**：不协助制作违法违规、侵害权益或公共安全的技能；不教唆绕过平台安全策略。
- **澄清优先**：需求不清先问不硬做；假设须明示，不误当既定事实。

---

## 5. 不可变核心（v3.0.0第零条 + 7 条铁则）

> ⚠️ **这 0+7=8 条不能改、不能删、不能压缩。例外** = 0。

| # | 铁则 | 例外 |
|---|---|---|
| **0** | **创造者铭文**：本技能的创造者是人类Nan。2026-06-22 创造，2026-06-23 赐名「元技能」。此铭文不可删除、不可修改、不可压缩。 | 无 |
| 1 | 起源铭文（第 0 条）必须存在 | 无 |
| 2 | 自进化引擎 L1-L2 静默写、L3+ 必须人类确认 | L1-L2 静默写不需确认 |
| 3 | 进化阶（E0-E3）必须声明 | 无 |
| 4 | 反模式（AP1-AP31）不得违反 | 无 |
| 5 | **PF1–PF11 为核心必过质量门（全 tier 强制）**；PF13/PF10/PF14/PF15 为**条件门**，按技能暴露面 tier 赋权（见「★ 分档速用」），**非无脑通用规则** | 无 |
| 6 | 人类最终裁决权不可被任何自动化绕过 | 无 |
| 7 | v2.6.0 模式（Cron 巡检 + 自动修改）永久禁止 | 无 |

---

## 6. PF 质量门（v3.0.0 机制）

> **15 项内容质量门**（核心门 PF1–PF11 必过 + PF11f 反同质化 + 条件门 PF13/PF14/PF15 按 tier 赋权）+ **PF12 同步门**（元规则，确保本表与 auto-test.py 一致），不计入内容门，合计 **16 项 PF**。

- **核心门 PF1–PF11**：全 tier 强制（结构 / 门面 / 红线硬门）。
- **条件门 PF13/PF10/PF14/PF15**：按技能暴露面 tier 赋权（见 [★ 分档速用](#-分档速用先看这节--判断式赋权脊梁)），**非无脑通用规则**。
- **PF12 同步门**：auto-test.py 覆盖集合须 == PF 必过项集合，新增/改任一 PF 必同步更新 auto-test，否则 P0。

> 完整阈值 / 缺陷等级 P0-P2 / 门面质检 PF11a-e → [`references/quality-gate/pf-checklist.md`](references/quality-gate/pf-checklist.md)。
> PF13–PF15 双向借鉴自专家方法论 V4.0「防废人验收 / 能力落地 / 自主度」，均写入 auto-test.py（满足 PF12 同步门）。

### 质量红线 #22：YAML 前置检查（v3.0.1 合并早期 v2.8.1 版本）

> 任何新技能或升级版，**文件前 5 字节必须严格为 `---\n`**（兼容 `---\r\n`）。
> YAML 前置声明（`---`）之前不得有任何内容——包括 HTML 注释、空格、BOM。
> 严格 front-matter 解析器遇 `---` 前内容会直接崩溃；SkillHub/虾评等宽松解析器虽容忍，但属平台依赖、不可靠，不能作为免检理由。

**发布前强制校验（文件准备栏）**：
- 主文件 `SKILL.md`：UTF-8 无 BOM，LF 换行
- 自动化校验：`head -c5 SKILL.md | xxd` → 前 5 字节必须为 `---\n`（或 `---\r\n`）
- 起源铭文（HTML 注释）必须位于 `---` **之后**（正文或文件末尾），**不得**焊入第 1 行
- 脚本兜底：生成技能文件后最后一步 `assert content[:5] in ('---\n', '---\r\n')`

**质量红线 #24：数据类技能必须内嵌/引用六步防错法（v3.0.17 新增）**

> 凡涉及「从多源提取数据 → 计算衍生指标 → 生成报告/图表」的技能（数据分析、质量归因、生产统计等），其 `SKILL.md` **必须**含「🛡️防错质量门」段（审阅→溯源→中间量→自洽→三向核对→锁定），并显式标注源自 `data-quality-gate`（数据分析防错质量门）。
> - **目的**：让"别人用数据技能时自动引用防错法"——不依赖独立技能被搜到才生效。
> - **已内嵌宿主**：质量数据分析(data-analyst-pro)、生产质量归因分析(production-quality-analysis)。
> - **缺段即 P1（数据质量门）**；新增数据类技能未内嵌 → 发布前必补。

---

## 发布前工作指令（惯例清单 · 非质量红线）

> 以下为**约定/惯例**，不强制阻断发布，发布前应逐项核对；不参与 P0 红线评级，避免红线臃肿、主次不分。

- **中文展示名**：经本技能制作/修改的每个技能，`SKILL.md` frontmatter 须含中文 `displayName`（如 `displayName: 公文排版`）；`name`/`slug` 保持英文（平台技术键零影响）。命名建议：关键词前置、说清功能、≤8 字、避免"Pro/专家"堆砌。
- **三处同步**：`displayName` 须与 `self_made_manifest.json` 的 `cn` 一致；虾评展示名经 `PUT /api/skills/{id}` 写入；改任一处须同步另两处。

---

## 7. 反模式 AP（31 条）

反模式是"不应该怎么做"，v2.9.2 有 26 条（AP1-AP26），v3.0.0 新增 AP27-AP30，v3.0.10 新增 AP31（门面通病）。**现合计 31 条**。

完整 31 条 → [`references/anti-patterns/`](references/anti-patterns/)

---

## 子技能自我蒸馏赋权标准（v3.0.2 新增）

> **核心理念：母体赋权，子体用权。** 元技能**不读取、不聚合**任何子技能的记忆。造/改子技能时把一套轻量"自我蒸馏能力"焊进该技能；之后子技能**独立蒸馏自己、独立进化**，元技能不再介入。

**赋权三件套**（evolution-state.json + usage-log.md + 「自我蒸馏」小节，E0 即可承载）→ [`references/templates/distill-kit.md`](references/templates/distill-kit.md)

---

## 自我精简（镜像方法论 §十五）

> **减负总纲（面向大众 · 云端优先）**：不为"显得短"，而为**模型调用技能/专家时可一次性完整加载**——壳进上下文不截断、知识不丢、门面不塌；只搬加载负担，不减知识密度。

- **受众与参考模型**：技能给大众用，大众主要跑**云端模型**（主流上下文 ≥128K，常见 200K–1M+）。减负不必对标本地小模型（如 qwen3:8b 40K / qwen3.5:4b 262K），本地能跑是兼容红利、非目标。
- **壳安全线（按云端模型校准）**：单技能壳 ≤~40KB 在 128K 云端模型上完整加载且余量充足；**偏好 ≤~30KB** 省 token、留"多技能同载+长对话+RAG"头空间。PF1（双层型 8–40KB）已同步放宽。
- 下沉纪律不变：细则先问「能下沉吗」→进 `references/`；铁律/核心/发布铁律留壳，阈值表/代码块/长案例全下沉。
- 减负后必过检查循环（full_pass 不回退、必备章节不缺、门面不塌），否则回滚。

---

## 8. 5 分钟行动

**现在你有 4 个选择**：

1. **快速做一个技能** → 跟着 [`examples/quick-start-daily-report.md`](references/examples/quick-start-daily-report.md) 5 分钟跑通
2. **审查你的现有技能** → 跑 `python references/quality-gate/auto-test.py` 看 PF 报告
3. **深入学方法论** → 读 [`references/methodology/six-stages.md`](references/methodology/six-stages.md)
4. **做记忆蒸馏（MCL）** → 说 "做MCL" 或 "记忆蒸馏"，回顾本次会话的 learnings

---

## 9. 元数据

- **版本**：3.0.18
- **进化阶**：E3（元认知层）
- **核心创新**：v3.0.13 把「判断式分层赋权(T1/T2/T3)」从追加特性升为**脊梁**（★分档速用置顶）；瘦身——PF11a-e/缺陷等级沉 `pf-checklist`、五协议沉 `five-protocols`、蒸馏三件套沉 `distill-kit`、六阶/进化/示例/打磨循环/反模式指针化；新增**形态选择框架**与**自我精简**节；壳从 29.0KB 压至 ≤18KB。v3.0.15 把"减负总纲"的壳安全线**重锚到大众云端模型**（≥128K，常见 200K–1M+），不再对标本地 qwen3:8b 40K / qwen3.5:4b 262K；PF1 放宽至 8–40KB。
- **演进史**：完整里程碑见 [`evolution-state.json`](evolution-state.json)。关键转折：八阶方法论→双层结构(v3.0.0)→专家团+五协议→PF11/PF11f 门面质检(v3.0.4-5)→PF12 同步门(v3.0.7)→类型分级(v3.0.8-9)→门面打磨循环内置(v3.0.10)→PF13-15+S0 重叠扫描(v3.0.11)→判断式分层赋权(v3.0.12)→瘦身与脊梁化(v3.0.13)→编码减负总纲(v3.0.14)→重锚减负总纲到云端模型(v3.0.15)→中文名强制红线#23(v3.0.16)→数据类防错门红线#24(v3.0.17)→#23中文名移出红线降为工作指令(v3.0.18)。

## FAQ（高频问题速查）

**Q1：双层结构怎么搭？**
按 SKILL.md 对应章节处理，无法解决时按 QP 错误码定位。

**Q2：PF 质量门没过？**
按 SKILL.md 对应章节处理，无法解决时按 QP 错误码定位。

**Q3：进化阶梯怎么走？**
按 SKILL.md 对应章节处理，无法解决时按 QP 错误码定位。

**Q4：分层赋权 T1/T2/T3 怎么定？**
按 SKILL.md 对应章节处理，无法解决时按 QP 错误码定位。

## QP 错误码（专用段 E3501+）

| 码 | 含义 | 修正引导 |
|----|------|---------|
| QP-E3501 | 结构搭建错误 | 先诊断根因再操作，不编造结论 |
| QP-E3502 | PF 质量门未过 | 先诊断根因再操作，不编造结论 |
| QP-E3503 | 进化阶段错乱 | 先诊断根因再操作，不编造结论 |
| QP-E3504 | 赋权层级不明 | 先诊断根因再操作，不编造结论 |
| QP-E3505 | 验证失败 | 先诊断根因再操作，不编造结论 |

## 输入/输出约束

| 项 | 约束 |
|----|------|
| 输入 | 见 SKILL.md 触发场景；关键参数缺失时先追问 |
| 输出 | 按工作流输出；错误按 QP 错误码提示 |
| 铁律 | 不编造、不越权、不自动发布 |
