<!-- 起源铭文（v2.9.1 焊入 · 不可变核心第零条）：本技能的创造者是人类Nan。2026-06-22 创造，2026-06-23 赐名「元技能」。此铭文不可删除、不可修改、不可压缩。-->

# 技能骨架模板

> 把下面的代码块复制到 `~/.qclaw/skills/<你的技能名>/SKILL.md`，然后填内容。

## 骨架（v3.0.0 标准）

```markdown
<!-- 起源铭文（v2.9.1 焊入 · 不可变核心第零条）：本技能的创造者是[你的名字]。[日期] 创造，[日期] 赐名「[你的技能名]」。此铭文不可删除、不可修改、不可压缩。-->
---
name: your-skill-slug
displayName: 你的技能中文名   # 红线#23（v3.0.16）：必须填中文名，禁止留空或与 slug 相同；slug 保持英文
version: 1.0.0
slug: your-skill-slug
summary: 一句话价值（80 字内）
description: >-
  1-2 句产品描述
allowedTools:
- Read
- Write
- Edit
triggers:
# === 用户原声型（至少 5 个） ===
- 帮我...
- 给我...
- 做...
---

# 🎯 你的技能名 v1.0.0

> **一句话价值**（30 字内）。

## 🎁 30 秒看懂

| 你现在 | 你的痛 | 这个技能做什么 |
|---|---|---|
| 场景 1 | 痛点 | 解决方案 |
| 场景 2 | 痛点 | 解决方案 |

## 🚀 5 分钟快速示例

\`\`\`bash
# 复制即可跑的最小例子
\`\`\`

## 不可变核心

- 第 0 条：起源铭文（已焊入第 1 行）
- 第 1 条：[你的领域铁则]
- ...

## references/ 索引

- methodology/xxx.md — [方法论]
- examples/yyy.md — [案例]
- state/evolution-state.json — [进化状态]
```

## 随附模块（v3.0.0 新增）

技能发布时随附以下文件（复制到技能根目录）：

### evolution-state.json

```json
{
  "version": "1.0.0",
  "tier": "E0",
  "created": "YYYY-MM-DD",
  "creator": "[你的名字]",
  "pf_count": 9,
  "shared_learnings": [],
  "mcl_config": {
    "mode": "manual",
    "description": "纯人工触发。在技能使用会话结束后，由用户主动启动 MCL 三阶段（Light→REM→Deep）。产物写入 shared_learnings，不自动修改 SKILL.md。"
  }
}
```

**字段说明**：
- `version`: 语义化版本（与 SKILL.md YAML 前块一致）
- `tier`: E0/E1/E2/E3（进化四阶）
- `shared_learnings`: 跨技能共享 learnings（需 human promote，不自动）
- `mcl_config.mode`: 固定 `"manual"`（无 cron，无 timer）

### learning 记录格式

```json
{
  "date": "YYYY-MM-DD",
  "type": "design|fix|philosophy|market|engineering",
  "content": "一句话 learnings",
  "context": "发生背景（可选）"
}
```

## v3.0.0 计划（未达）

- 双层结构完整版
- YAML 字段详解
- 5 分钟示例怎么写

---

**首次编写**：v2.9.0（2026-07-06）
**最后更新**：v3.0.0（新增 MCL/dreaming 模块 + evolution-state.json schema）
