# 自进化引擎（v2.9.2 § -2 详细文档）

> **v3.0.0 拆分**：v2.9.2 文档过于庞杂（203KB），本节被拆到 references/methodology/evolution-engine.md，按需加载。

## 设计哲学

**v2.6.0 反思 → v2.9.0 修正**：
- v2.6.0 用了 Cron 12h 定时巡检 + 自动信号消费 → 实际**绕过了不可变核心第 8 条（人类最终裁决）**
- v2.9.0 改为：**使用 → 被动积累 learnings → 下次对话时 Agent 提案 → 人类确认 → 升级**

**绝不**有定时器或自主后台修改。**绝不**趁人不在偷偷改。

## 启动序列（AGENTS.md 手动接入）

在 AGENTS.md 的 Session Startup 序列末尾追加：

```markdown
5. **自进化引擎**：如果 `skills/skill-maker-pro/SKILL.md` 存在，读取该文件 § 第负二层，按 § -2.3 执行自诊断协议。如果不存在或已失效，跳过。
```

**注意**：这是手动配置（**不**自动修改 AGENTS.md）。配置一次后每次 Agent 启动自动执行。

## 工作流

```
Agent 启动
  → 读到 AGENTS.md 步骤 5
  → 检查 skills/skill-maker-pro/SKILL.md 是否存在
  → 读取 § 第负二层（本文件）
  → 按 § -2.3 执行自诊断检查清单（R1-R8）
  → 读 evolution-state.json 对比历史
  → 若触发进化信号 → 异步提案（不自动执行）
  → 更新 evolution-state.json
  → 任何修复动作 → 需人类确认
```

## 信号流水（v2.9.0 修正：全部改为提案模式）

| 信号 | 触发条件 | 动作（v2.9.0 起为提案） |
|---|---|---|
| S1 版本漂移 | SKILL.md 头声明 ≠ evolution-state.json | 👤 人类确认后修复 |
| S2 引用断裂 | 章节标题被改名/删除 | 👤 人类确认后修复 |
| S3 反模式命中 | 出现 AP1-AP30 模式 | 👤 人类确认后修复 |
| S4 缺失章节 | 关键章节缺失 | 👤 人类确认后补全 |
| S5 learnings 阈值 | shared.learnings 累积达 N 条 | 👤 人类确认后写入正文 |
| S6 退化指标 | 错误率上升、引用率下降 | 👤 人类确认后调整 |
| S7 模式识别 | E2+ 技能模式识别触发 | 👤 人类确认后优化 |
| S8 元进化信号 | E3 技能自反思 | 👤 人类确认后升级 |

**v2.9.0 关键修正**：所有信号**不**自动消费。**所有动作**需人类点头。

## 与不可变核心的硬隔离（H1-H5）

为防止自动修复触犯不可变核心，v2.9.0 引入 5 条硬隔离：

| # | 隔离项 | 实现 |
|---|---|---|
| H1 | 不可变核心第 0-3 条不被修改 | 引擎无权编辑起源铭文、不可变核心、进化阶 |
| H2 | 自进化仅限 § 第负二层以内 | 引擎无权编辑外壳（§ 1-9） |
| H3 | 跨技能修改需人类确认 | 引擎不主动改其他技能 |
| H4 | 不消耗其他技能 learnings | 引擎不读取 .learnings/ 共享区 |
| H5 | v2.6.0 模式永久禁用 | 引擎代码中无 Cron 触发器 |

## R1-R8 自诊断清单

| # | 检查项 | 方法 |
|---|---|---|
| R1 | 起源铭文完整性 | 解析 L1 注释 |
| R2 | YAML front matter 规范 | yaml.safe_load |
| R3 | 引用完整性 | grep 章节标题 |
| R4 | 进化阶声明存在 | grep E0-E3 |
| R5 | evolution-state.json 与 SKILL.md 一致 | diff tier/version |
| R6 | 反模式自检 | AP1-AP30 grep |
| R7 | 章节完备性 | 必备章节列表 |
| R8 | 维度注册表完整性 | E3+ 技能查 |

## evolution-state.json 规范

E3 技能（含元技能自身）的 `evolution-state.json` 完整结构：

```json
{
  "tier": "E3",
  "version": "3.0.0",
  "creator": "人类Nan",
  "created": "2026-06-22",
  "evolution_history": [
    {"version": "2.6.0", "date": "...", "summary": "..."},
    {"version": "2.8.0", "date": "...", "summary": "..."},
    ...
  ],
  "next_planned": "v3.0.0: PF 质量门加 4 项 + 反模式扩充到 35",
  "learnings": {
    "shared": [...],
    "personal": [...]
  },
  "mcl_config": {
    "trigger": "session_end",
    "phases": ["light", "rem", "deep"]
  },
  "dimensions": {
    "name": "...", "type": "...", "current": ..., "target": ...
  }
}
```

E0-E2 技能仅需 `tier` + `version` + `created` + `creator` 4 个核心字段。
