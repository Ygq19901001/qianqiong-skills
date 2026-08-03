# 乾穹技能集 · QianQiong Skills

天工阁出品——乾穹公司 AI Agent 技能集合。每个 Skill 独立封装，可跨平台复用。

> 本仓库为乾穹全部 Skill 资产归档（v2.2.0 评估驱动升级），共 42 个，按产品线分类。

## 核心 8 件套（主产品线 · v2.2.0）

| 技能 | 版本 | 说明 |
|------|------|------|
| data-analyst-pro | v2.2.0 | 写作素材引擎——三精标准（口径/来源/时效）+ 多源交叉验证 |
| humanizer-pro | v2.2.0 | AI痕迹清洗——10种AI典型痕迹精准诊断+逐一修复 |
| ima | v2.2.0 | IMA 知识库与笔记管理 OpenAPI |
| learn-pro | v2.2.0 | 学习教练——问题链引导+水平感知+五阶教学法+强化闭环 |
| ppt-pro | v2.2.0 | PPT内容架构师——一页一观点，每页完整可落地内容 |
| prompt-engineer | v2.2.0 | 提示词工程专家——四步工作流+策略决策表+QP错误码体系 |
| reference-formatter | v2.2.0 | 参考文献格式化——GB/T 7714 / APA 7th / MLA / Chicago |
| translate-pro | v2.2.0 | 专业翻译——三元策略，不确定必标⚠️，绝不编造等效表述 |

## 学术助手产品线（academic-* · v2.2.0）

论文全生命周期 14 件套：academic-docx-toolkit（DOCX排版）/ paper-review-methodology（33类审查）/ literature-mining（文献挖掘）/ academic-chart-gen（统计图表）/ academic-paper-workshop（14件套入口）/ academic-search-pro（学术检索）/ academic-figure-gen（结构示意图）/ academic-writing-bank（写作词库）/ plagiarism-precheck（查重预检）/ paper-version-manager（版本管理）/ submission-helper（投稿助手）/ readability-pro（流畅度诊断）/ production-quality-analysis（质量归因）/ data-quality-gate（防错质量门）

## AI 原生公司产品线（v2.2.0）

- agent-org-manager：多 Agent 组建公司（部门/通讯/日报/质检）
- opc-os-core：一人公司 AI 操作系统（7 部门自动运转）
- intelligence-brain：公司级 AI 情报引擎（八步代谢管道）
- openclaw-cron-health-monitor：定时任务健康卫士
- digital-persona：已故人物数字永生（v2.3.1）
- edge-cdp：Edge/Chrome CDP 远程控制
- biobrain-* ×5：上述产品线早期代（ClawHub 同步源，已同步 v2.2.0）

## 历史命名空间（qclaw-* · v2.2.0）

SkillHub 历史账号（user_8d26dabd）同源旧版，内容已同步核心 v2.2.0：
qclaw-data-analyst-pro / qclaw-humanizer-pro / qclaw-ppt-pro / qclaw-prompt-engineer / qclaw-reference-formatter / qclaw-translate-pro

## 其他

- qclaw-doc-formatter：公文排版（v2.2.0）
- skill-maker-pro：技能制作专家（v2.2.0）
- image-video-prompt-lib：图视频生成提示词库（v2.2.0）

## 统一升级说明（v2.2.0，2026-08-03）

- **P0 重写**：prompt-engineer（QP错误码E101+）、learn-pro（E201+，降级阶梯/防漂移）
- **P1 三件套**：全部 skill 加装 FAQ + QP 错误码专用段 + 输入输出约束（E301+~E3601+）
- **统一编码**：错误码前缀 `QP-`（QianQiong），全司 skill 复用同一套规则
- **平台状态**：主账号（user_3ef04463）25 个 skill 平台侧已全部 v2.2.0；历史账号（user_8d26dabd）23 个因凭证丢失平台侧保持原版本，本仓库为维护版归档

## 维护

天工阁每周一 10:00 技能周检（cron 驱动）。

## 许可

MIT License — 乾穹 (QianQiong)
