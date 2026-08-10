# 风格预设速查

> 每条给出"风格名 + 可直接用的提示词片段 + 适用场景"。改 `[主体]` 即可套用。

## 写实类

- **工业摄影**：`industrial photography, side lighting, 85mm, sharp detail` → 产品/设备/车间
- **纪录片**：`documentary style, natural light, handheld realism` → 产线/人物/过程
- **产品棚拍**：`studio product shot, softbox, clean background, 8k` → 电商主图
- **新闻摄影**：`photojournalism, candid, 35mm, available light` → 现场纪实
- **微距摄影**：`macro photography, shallow depth of field, fine texture` → 材料/纹理特写

## 插画类

- **扁平矢量**：`flat vector illustration, minimal, bold color blocks` → 信息图/示意
- **2.5D 厚涂**：`2.5D illustration, soft shading, rounded form` → 儿童/科普
- **手绘水彩**：`watercolor painting, paper texture, loose brush` → 文艺/绘本
- **版画风**：`linocut / woodcut style, high contrast, ink` → 装饰/海报
- **信息图**：`infographic style, clean icon, legible label` → 数据呈现

## 学术类（论文配图，深蓝体系）

- **示意图**：`flat vector diagram, deep blue #2C5AA0 + light blue #D6E4F4, rounded rectangle, 300dpi PNG, ample whitespace` → 系统/流程架构
- **流程图/架构图**：`flat schematic, no photo texture, clear arrow, muted palette` → 方法/框架
- **数据图注**：`scientific chart companion figure, monochrome axis, sans-serif label` → 图表说明
- 学术图铁则：无照片质感、无重阴影、文字不溢出、配色不刺眼

## 影视类

- **赛博朋克**：`cyberpunk, neon glow, volumetric light, rain-slick street` → 未来/夜景
- **复古胶片**：`analog film, 35mm, film grain, faded color, Fujifilm tone` → 怀旧/人像
- **冷暖对比**：`chiaroscuro, warm key + cool fill, dramatic` → 情绪/产品
- **莫兰迪**：`Morandi palette, low saturation, muted elegant` → 家居/服饰
- **蒸汽波**：`vaporwave, pink cyan gradient, grid, retro 80s` → 潮流/音乐

## 光线预设（可单独叠加）

- `golden hour, warm rim light` / `blue hour, cinematic` / `studio softbox` / `hard sunlight, high contrast` / `neon nocturnal` / `overcast diffuse`

## 平台提示词习惯小结

| 平台 | 写法要点 |
|------|---------|
| Midjourney v7 | 英文自然语言 + `--ar` 画幅 + `--v 7` + `--style raw` + `--no` 负向 |
| Stable Diffusion | 逗号分隔标签 + 权重 `( )` + 独立 Negative 框 + 采样器/步数/CFG |
| 即梦 / 可灵 / 可图 | 中文自然语言 + 运镜词句中 + 风格词句尾 |
| Sora / 可灵视频 | 强调运镜 + 时序 + 一致性锚点（首帧/参考图）|

## 风格选择建议

- 要"高级感"→ 写实棚拍 / 莫兰迪 / 冷暖对比
- 要"科技感"→ 赛博朋克 / 体积光 / 未来城市
- 要"可信论文图"→ 学术类深蓝扁平，绝不照片化
- 要"短视频种草"→ 即梦/可灵中文写实 + 句中运镜
