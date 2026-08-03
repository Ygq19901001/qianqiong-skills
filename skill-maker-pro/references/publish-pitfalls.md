# 多平台发布实战踩坑库（skill-maker-pro 发布前清单）

> 来源：AI 技能工厂顾问（ai-skill-factory-consultant）定义中的多平台发布实战段；本文件将该经验显性化为可勾选清单。
> 适用平台：虾评(xiaping.coze.com)、SkillHub(api.skillhub.cn)、Gitee/GitHub。

## 一、虾评(xiaping) 发布门

- **pledge 必传**：`POST /api/skills` 与 `POST /api/upload` 都要求 `pledge: {agreed:true}`，漏传返回 `409 PLEDGE_REQUIRED`。
- **小写 skill.md**：ZIP 内须含小写 `skill.md`（源文件常为 `SKILL.md` 大写，打包时补副本）。
- **eval_cases ≥1**：平台已停用 `auto` 兜底出题，须开发者亲自出题；空数组报 `409 EVAL_CASES_INVALID`。
- **category 四值**：评测用例 `category` 仅接受 `trigger|edge|adversarial|format`，自定义值被拒。
- **YAML triggers 多行**：逐行解析，注意缩进。

## 二、SkillHub 发布门

- **host 修正**：`api.skillhub.cn` 才是鉴权/写接口；`api.useskillhub.com` 仅公开读，写操作 404。
- **写作用域令牌**：旧/无写作用域令牌对 `POST /community/skills/publish` 等写操作返回 `401`；需 publisher 权限或 write 作用域令牌。
- **下架→删除顺序**：先 `unlist` 再 `delete`；删前未下架返回 `409`「只能删除已下架的 Skill」。
- **统计口径**：列表 `stats.downloads` 恒为 0，须逐个 `/api/v1/skills/{slug}` 取真实下载量。

## 三、通用发布前强制校验清单（发布前逐项勾选）

- [ ] 主文件前 5 字节为 `---\n`（质量红线 #22）
- [ ] 起源铭文位于 `---` 之后
- [ ] 评估集 `eval_cases` ≥1 且 `category` ∈ {trigger, edge, adversarial, format}
- [ ] ZIP 内含小写 `skill.md` 副本
- [ ] pledge 字段已随发布/更新请求提交
- [ ] 跨平台 host 用对（SkillHub = `api.skillhub.cn`）
- [ ] 写操作令牌具写作用域（或账号开 publisher 权限）
- [ ] 下架类操作遵循 unlist → delete 顺序
