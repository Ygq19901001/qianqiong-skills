# 五协议防身（v3.0.0 补充）

> 从 v2.9.x→v3.0.0 踩坑中提炼的 5 条防翻车协议，适用于所有衍生技能。本文件从元技能壳下沉（v3.0.13 瘦身），原壳仅保留指针。

| # | 协议 | 说明 |
|---|---|---|
| **P1** | **双轨验证** | 任何改动必须在 SKILL.md + evolution-state.json 两轨同步（避免数据打架） |
| **P2** | **沙箱验证** | 发版前 dry-run 完整 PF 15/15 内容质量门（避免假数据自报） |
| **P3** | **回滚协议** | 版本号诚实标记（未达目标不给虚假版本号），回退时完整审计越位 |
| **P4** | **渐变切换** | 大版本分批发布——先 P0→P1→P2，每层跑 PF 15/15 内容质量门 + 6 路专家团 |
| **P5** | **版本体系** | 语义化版本 + evolution-state.json 的 `version` 字段三重一致（SKILL.md YAML / § 9 / evolution-state.json） |

**怎么用**：

```bash
# 1. 写完 SKILL.md
# 2. 运行自检
python references/quality-gate/auto-test.py ~/.qclaw/skills/my-skill/

# 3. 15 项内容质量门全 PASS → 才能发布
# 4. 任何 FAIL → 修复后重跑
```

完整 checklist 看 [`../quality-gate/pf-checklist.md`](../quality-gate/pf-checklist.md)。
