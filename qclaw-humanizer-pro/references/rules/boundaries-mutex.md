<!-- SECLEVEL: INTERNAL -->

## ⚠️ 技能边界与互斥

**humanizer-pro 负责「同语言表达优化」**——改写、润色、去AI痕迹，让成品文字更像真人写的。**不负责「跨语言翻译」**。

### 与 translate-pro 的边界
- 先翻译（translate-pro）→ 再润色（humanizer-pro）
- **不可跳过翻译直接润色外语**——humanizer-pro 不做语言转换，只做表达优化
- 用户需要把中文翻译成英文并润色时：第一步 translate-pro 翻译，第二步 humanizer-pro 润色英文

### 与 doc-qa-pro 的边界
- doc-qa-pro 负责「从文档中提取信息、回答问题」
- humanizer-pro 负责「润色 doc-qa-pro 提取后的文字」
- 典型协作链：上传文档 → doc-qa-pro 读取/提取 → humanizer-pro 润色输出

### 与 ppt-pro 的边界
- ppt-pro 做「幻灯片语言」——简短有力、要点式、适合投影/阅读
- humanizer-pro 做「文档语言」——完整表达、段落式、适合深度阅读
- 同一个主题，ppt-pro 输出的是讲稿要点，humanizer-pro 输出的是报告正文

### 与 learn-pro 的边界
- learn-pro 做「教学讲解」——有问有答、循序渐进、带检验问题
- humanizer-pro 做「文本成品」——交付即用、不套对话腔、不带教学引导
- learn-pro 的输出是"教会你"，humanizer-pro 的输出是"替你写好了"

### 灰色地带裁决
| 用户请求 | 走 | 原因 |
|----------|-----|------|
| "帮我翻译这段英文并润色" | translate-pro → humanizer-pro | 先翻译跨语言，再润色同语言表达 |
| "我的英语作文帮我改改语法和表达" | humanizer-pro | 同语言润色，不涉及跨语言翻译 |
| "帮我把这段中文翻译成英文" | translate-pro | 纯翻译任务，不涉及表达优化 |
| "这段文字读起来怪怪的，帮我改得自然些" | humanizer-pro | 同语言表达优化，去AI痕迹 |
| "帮我写一份产品发布会演讲稿" | humanizer-pro | S3 发言稿场景，从零创作 |
| "教我怎么改善写作，避免AI痕迹" | learn-pro | 教学需求，有问有答循序渐进 |
| "帮我分析这份PDF报告内容" | doc-qa-pro | 文档信息提取和问答 |
| "把这份报告做成PPT" | ppt-pro | 幻灯片制作，要点式呈现 |
| "帮我写一个Python脚本处理文本" | script-gen-pro | 代码脚本生成，非文本写作 |
| "帮我分析这份数据表" | data-analyst-pro | 数据分析任务，非文本润色 |
| "这段摘要太生硬了，帮我改写一下" | humanizer-pro | 同语言表达润色，去AI味 |
| "帮我写一封商务邮件回复客户投诉" | humanizer-pro | S1 工作邮件/S11 客户沟通场景 |
| "给我一个职场写作的课程大纲" | learn-pro | 课程设计，教育传授属性 |
| "我的微信回复太官方了，帮我改改" | humanizer-pro | S12 日常沟通场景，口语化调整 |
| "帮我把产品介绍翻译成英文并适配海外市场" | translate-pro → humanizer-pro | 翻译即语言转换在先，表达优化在后 |
| "帮我降论文/摘要/开题报告/文献综述的AI率" | **拒绝 + 学术诚信提示** | 用AI改写学术文本以规避检测属于学术不端，建议人工重写并声明AI辅助 |

#### 可调兵场景
| 用户请求 | 可调谁帮忙 | 原因 |
|----------|------------|------|
| 润色后的文字需要验证数据 | data-analyst-pro | 数据核实属于数据分析范畴 |
| 用户提供的数据需先分析再写报告 | data-analyst-pro → humanizer-pro | 先分析数据，再基于分析结果写作 |
| 英文原文+润色英文（用户熟悉英文） | humanizer-pro | 同语言润色，不需翻译介入 |
| 英文原文+润色英文（用户不熟悉英文） | translate-pro + humanizer-pro | 先帮用户理解原文，再润色 |

---

# Humanizer Pro：通用内容撰写与人性化润色

