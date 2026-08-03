# 学术写作语料库 / Academic Writing Bank

> 学术论文写作的短语库 + 模板引擎 —— 让 AI 知道论文每个段落怎么写、用什么词。

**Academic Writing Bank** is a phrase library and template engine for scholarly paper writing — providing chapter-level paragraph skeletons, a categorized academic phrase bank, and a rich transition-word system. Designed for both Chinese and English academic writing.

---

## 功能亮点 / Highlights

| 功能 / Feature | 说明 / Description |
|---|---|
| **8章模板 / 8-Chapter Templates** | 引言→结论，每章 3-5 个段落骨架，{{PLACEHOLDER}} 标记填充位 |
| **6类短语库 / 6-Category Phrase Bank** | 立论·承转·定义·举证·对比·结论，中英双语，标注适用章节与正式度 |
| **100+过渡词 / 100+ Transition Words** | 因果·递进·转折·并列·总结·举例·强调，附频率建议 |
| **中文规范 / Chinese Conventions** | 人称·语态·数字·图表·中英混排的规范性指南 |
| **避坑指南 / Common Pitfalls** | 各章常见错误 + 修改建议，初稿自查利器 |

## 与已有技能的关系 / Relationship with Existing Skills

```
你的需求 / Your Need                    适用技能 / Use
─────────────────────────              ─────────────────
"这章不知道怎么写"                      academic-writing-bank ← 模板 + 句式
"写好了但读起来很AI"                    humanizer-zh ← 去AI痕迹
"英文论文想润色"                        writing-polish ← 通用润色
"CS顶会论文需要专门润色"                academic-writing-refiner ← 专业润色
```

本技能是 **写作工具箱**（解决"怎么写"），与润色类技能（解决"怎么改"）互补，互不替代。

## 文件结构 / File Structure

```
academic-writing-bank/
├── SKILL.md                          # 技能入口文件
├── README.md                         # 本文件（中英双语说明）
└── references/
    ├── chapter-templates.md          # 8章段落骨架模板
    ├── phrase-bank.md                # 6类学术短语库（中英双语）
    ├── transition-library.md         # 100+学术过渡词库
    ├── chinese-conventions.md        # 中文学术写作规范
    └── common-pitfalls.md            # 各章常见错误与修改建议
```

## 快速开始 / Quick Start

1. **写作前**：查阅 `chapter-templates.md`，按模板搭建章节骨架
2. **写作中**：打开 `phrase-bank.md` + `transition-library.md`，替换平庸表达
3. **初稿后**：对照 `common-pitfalls.md` 逐章自查
4. **中文论文**：额外查阅 `chinese-conventions.md`

---

> ⚠️ **隐私声明**：本技能所有示例均基于虚构的通用学术场景，不包含任何真实论文标题、公司名、系统名或人名。

---

作者：人类Nan
