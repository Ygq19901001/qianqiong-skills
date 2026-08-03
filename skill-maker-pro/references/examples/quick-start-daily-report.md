# 快速示例：5 分钟做"日报生成"技能

> 这个示例展示 v3.0.0 元技能的核心工作流：把"现有的脚本/工作流"变成"能发布的技能"。

## 前置条件

- 已有 Python 脚本 `make-daily-report.py`（或类似工作流）
- 知道怎么用命令 `python make-daily-report.py --input data.json --output report.md` 跑
- 5 分钟时间

## Step 1（30 秒）：定位核心方法

打开 `make-daily-report.py`，问自己 3 个问题：
1. 它解决了什么痛点？（例如：从销售数据自动生成可读日报）
2. 谁会用？（销售主管？运营？老板？）
3. 一句话价值是什么？（"3 秒从 Excel 数据生成老板能直接看的日报"）

**输出**：3 句话，30 秒搞定。

## Step 2（1 分钟）：创建技能骨架

```bash
# 1. 决定技能目录名（slug 风格）
SKILL_DIR=~/.qclaw/skills/daily-report-gen

# 2. 创建目录
mkdir -p $SKILL_DIR/references/{methodology,examples,templates,quality-gate}
mkdir -p $SKILL_DIR/.learnings

# 3. 复制骨架模板
cp references/templates/skill-skeleton.md $SKILL_DIR/SKILL.md
```

## Step 3（2 分钟）：填外壳

打开 `$SKILL_DIR/SKILL.md`，按顺序填 5 块：

### 3.1 起源铭文（L1）
```markdown
<!-- 起源铭文（v3.0.0 焊入 · 不可变核心第零条）：本技能的创造者是人类Nan。{日期} 创造，{日期} 赐名「日报生成专家」。此铭文不可删除、不可修改、不可压缩。-->
```

### 3.2 YAML front matter（前 10 行）

按 skill-skeleton.md 模板填 name/slug/version/triggers/allowedTools。

**关键**：触发词至少 5 个用户原声型：
- "生成日报"
- "做个日报"
- "帮我做日报"
- "我有个脚本想分享"
- "日报自动化"
- "数据 → 日报"
- "daily report"

### 3.3 一句话价值（L20-30）

```markdown
**3 秒从销售数据生成老板能直接看的日报。**
```

### 3.4 5 分钟示例（L40-60）

```markdown
## 5 分钟快速开始

```bash
# 安装
git clone https://github.com/yourname/daily-report-gen ~/.qclaw/skills/daily-report-gen

# 准备数据
echo '{"date":"2026-07-06","sales":1000,"refunds":50}' > data.json

# 生成日报
python -c "from daily_report_gen import gen; print(gen('data.json'))"
```

**输出**：可读的日报 Markdown
```

### 3.5 痛点对照（L80-100）

```markdown
| 你现在 | 痛 | 这个技能做什么 |
|---|---|---|
| 手动写日报 1 小时 | 没时间 | **3 秒**从数据生成 |
| 用 Excel 公式拼凑 | 易错 | 一行命令搞定 |
| 日报格式每次不同 | 不规范 | 固定模板 |
```

## Step 4（1 分钟）：填 references/

### 4.1 references/methodology/quick-method.md
写 1 页：核心算法/方法/数据流。

### 4.2 references/examples/sale-2026-07-06.md
写 1 个真实案例：输入数据 + 输出日报。

### 4.3 其他子目录
如果暂时没内容，留 `README.md` 占位。

## Step 5（30 秒）：PF 质量门自检

```bash
python references/quality-gate/auto-test.py $SKILL_DIR
```

**期望输出**：
```
[STAT] 统计：8 PASS, 0 FAIL
[PASS] 全部通过！可以发布。
```

**如果 FAIL**：
- PF1 体量过大 → 删 SKILL.md 中非关键内容
- PF2 子目录不足 → 把空目录加 README.md
- PF3 钩子靠后 → 把"5 分钟快速开始"提到文档前 1/3
- PF4 触发词不足 → 补 5+ 个用户原声型

## Step 6（30 秒）：发布

```bash
# 1. zip 打包（注意 BOM/隐藏文件）
cd ~/.qclaw/skills
zip -r daily-report-gen-v1.0.0.zip daily-report-gen/ \
    -x "*.git*" "*.DS_Store" "*__pycache__*"

# 2. 上传 SkillHub
# （通过 CLI 或网页）
```

## 总时间

| 步骤 | 时间 |
|---|---|
| Step 1 定位核心方法 | 30 秒 |
| Step 2 创建骨架 | 1 分钟 |
| Step 3 填外壳 | 2 分钟 |
| Step 4 填 references/ | 1 分钟 |
| Step 5 PF 自检 | 30 秒 |
| Step 6 发布 | 30 秒 |
| **总计** | **5-6 分钟** |

## 下次迭代（v1.1.0）

跑 1 周后，看 `.learnings/`：
- 用户最常问什么？（加触发词）
- 哪部分最容易出错？（加 PF9 自检）
- 哪个案例最有共鸣？（加更多类似案例）

**v3.0.0 元技能的设计哲学**：让"做技能"从 4 小时压到 5 分钟，同时质量不降（甚至更高）。
