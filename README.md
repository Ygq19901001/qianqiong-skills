# 乾穹技能集 · QianQiong Skills

天工阁出品——乾穹公司 AI Agent 技能集合。每个 Skill 独立封装，可跨平台复用。

## 技能列表

| 技能 | 版本 | 说明 |
|------|------|------|
| data-analyst-pro | v2.2.0 | 写作素材引擎——三精标准（口径/来源/时效）+ 多源交叉验证，段落式输出可直接嵌入文章 |
| humanizer-pro | v2.2.0 | AI痕迹清洗——10种AI典型痕迹精准诊断+逐一修复，不改原意不改术语 |
| ima | v2.2.0 | IMA 知识库与笔记管理 OpenAPI（搜索/笔记/知识库/上传） |
| learn-pro | v2.2.0 | 学习教练——问题链引导+水平感知+五阶教学法+强化闭环，不替你学带你学 |
| ppt-pro | v2.2.0 | PPT内容架构师——一页一观点，每页完整可落地内容，绝不出占位符 |
| prompt-engineer | v2.2.0 | 提示词工程专家——四步工作流+策略选择决策表+QP错误码体系 |
| reference-formatter | v2.2.0 | 参考文献格式化——GB/T 7714 / APA 7th / MLA / Chicago，保留DOI |
| translate-pro | v2.2.0 | 专业翻译——三元策略（直译/意译/本地化），不确定必标⚠️，绝不编造等效表述 |

## v2.2.0 升级说明（2026-08-03）

评估驱动升级（基于 SkillHub 平台五维评估：trust/adaptability/convention/effectiveness/reliability）：

- **P0 重写**：prompt-engineer（能力边界/调用变体/策略决策表/QP错误码E101+/FAQ/Checklist）、learn-pro（去重/QP错误码E201+/降级阶梯/防漂移/强化层接入）
- **P1 三件套**：全部 skill 加装 FAQ + QP 错误码专用段 + 输入输出约束（E301+~E801+）
- **统一编码**：错误码前缀 `QP-`（QianQiong），全司 skill 复用同一套规则

## 维护

天工阁每周一 10:00 技能周检（cron 驱动）。

## 许可

MIT License — 乾穹 (QianQiong)
