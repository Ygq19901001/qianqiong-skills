# Learnings（v3.0.0 正式）

> **v3.0.0 决定（未达）**：`.learnings/` 与 `references/learnings/` 合并为 **单源** —— 本目录。
> 实际 learnings 存储位置：`references/learnings/`

## 文件命名规范

`<date>_<type>_<short>.md`

例如：
- `2026-07-07_shared_anti-pattern-mcl-vest.md`
- `2026-07-07_personal_workflow-preference.md`

## type 字段

- `shared` — 跨技能通用的学习（达到阈值后升级到 evolution-state.json）
- `personal` — 本技能特有的工作流偏好

## v3.0.0 决策（未达）记录

**为什么不放 .learnings/？**（v3.0.0 → v3.0 演进原因）
- PF2 子目录数计算：`.learnings/` 是 dotfile，不被算入 9 子目录
- 双目录（.learnings/ + references/learnings/）易漂移
- 单源管理：所有 learnings 都在 `references/learnings/`

## v3.0.0 计划（未达）

- 拆分 evolution-state.json 的 `learnings.shared/personal` 到独立文件
- 自动化 learnings 提取工具
