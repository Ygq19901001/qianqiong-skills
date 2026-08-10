# 即用模板库

> 14 条即写即用模板，按主题分组。每条给出**完整结构**（主体 + 场景 + 风格 + 光线 + 镜头 + 平台参数）。覆盖 8 条文生图 + 6 条文生视频。复制后按 `[方括号]` 替换即可。

---

## A. 文生图模板（8 条）

### A1 · 电商白底产品图
- **主体**：不锈钢保温杯，直立居中
- **场景**：纯白背景，无杂物
- **风格**：商业产品摄影
- **光线**：柔光箱两侧打光，均匀无投影
- **镜头**：85mm 微距，正面平视
- **平台参数**：
  - MJ：`a stainless steel thermos cup standing upright, pure white background, commercial product photography, softbox side light, 85mm macro, front view --ar 3:2 --v 7 --style raw --s 120 --no shadow, text, watermark`
  - SDXL：正向 `masterpiece, product shot, thermos cup, white background, studio light, 85mm, sharp focus`；负向 `shadow, text, watermark, blurry`；DPM++ 2M Karras, Steps 30, CFG 6, 1024x1024
  - 可图：`不锈钢保温杯直立居中，纯白背景，商业产品摄影，两侧柔光，85mm微距正视角`；负向 `阴影,文字,水印`；风格通用，尺寸 3:4

### A2 · 场景化产品图（生活氛围）
- **主体**：香薰蜡烛，点燃
- **场景**：木质茶几，旁边书本与咖啡
- **风格**：生活方式摄影（lifestyle）
- **光线**：窗边自然光 + 烛光暖点
- **镜头**：50mm，45°俯拍
- **平台参数**：
  - MJ：`a lit scented candle on a wooden coffee table with books and coffee, lifestyle photography, window natural light plus warm candle glow, 50mm, 45 degree top view --ar 4:3 --v 7 --style raw --s 200`
  - 即梦：`一支点燃的香薰蜡烛放在木质茶几上，旁有书本与咖啡，生活方式摄影，窗边自然光加烛光暖点，50mm，45度俯拍`

### A3 · 人像写真（复古胶片）
- **主体**：东亚女性，自然妆容，长发
- **场景**：老城巷弄，斑驳砖墙
- **风格**：柯达胶片人像
- **光线**：午后斜阳，柔光
- **镜头**：85mm，半身中景
- **平台参数**：
  - MJ：`an east asian woman with natural makeup and long hair, in an old alley with weathered brick walls, kodak film portrait, afternoon slant light, 85mm, waist-up medium shot --ar 3:4 --v 7 --style raw --s 300 --chaos 10`
  - SDXL：正向 `film portrait, woman, long hair, old alley, kodak portra, 85mm, soft sunlight`；负向 `oversaturated, anime, extra fingers, bad eyes`；Euler a, Steps 28, CFG 7, 768x1024

### A4 · 风景氛围（晨雾山林）
- **主体**：层叠远山
- **场景**：清晨薄雾，松林剪影
- **风格**：东方水墨意境 / 写实风光
- **光线**：晨光散射，低对比
- **镜头**：24mm 广角，地平线居中
- **平台参数**：
  - MJ：`layered distant mountains in morning mist, pine silhouettes, ink-wash mood meets realistic landscape, soft dawn scattering light, 24mm wide, horizon centered --ar 16:9 --v 7 --s 400`
  - 可图：`晨雾中的层叠远山，松林剪影，东方水墨意境写实风光，晨光散射低对比，24mm广角`；风格插画，尺寸 16:9

### A5 · 插画绘本（儿童风）
- **主体**：小女孩与一只狐狸
- **场景**：开满野花的草地，小木桥
- **风格**：温暖手绘绘本
- **光线**：明亮散射光
- **镜头**：中景，略仰
- **平台参数**：
  - MJ：`a little girl and a fox in a meadow of wildflowers with a small wooden bridge, warm hand-drawn children's book illustration, bright diffuse light, medium shot slight low angle --ar 4:3 --v 7 --style raw --s 500`
  - 可图：`小女孩和一只狐狸在开满野花的草地，有小木桥，温暖手绘绘本风，明亮散射光`；风格插画，尺寸 4:3

### A6 · 电商海报（促销大促）
- **主体**：主推商品（耳机）+ 大标题留白
- **场景**：霓虹渐变背景，粒子光斑
- **风格**：现代电商 banner
- **光线**：高调打光，霓虹补色
- **镜头**：平视，中心构图
- **平台参数**：
  - MJ：`wireless earbuds as hero product with reserved headline space, neon gradient background, bokeh light particles, modern e-commerce banner, high-key lighting, centered composition --ar 16:9 --v 7 --s 350 --no text`
  - 即梦：`无线耳机作主推商品，上方留标题空白，霓虹渐变背景加光斑粒子，现代电商banner，高调打光，中心构图` （标题文字请后期加）

### A7 · 美食（精致料理）
- **主体**：日式拉面碗，热气
- **场景**：木质吧台，暗调
- **风格**：美食摄影
- **光线**：顶光 + 侧逆光勾边
- **镜头**：50mm，45°俯拍特写
- **平台参数**：
  - MJ：`a bowl of japanese ramen with rising steam, wooden counter, dark moody tone, food photography, top light and rim backlight, 50mm, 45 degree close-up --ar 4:3 --v 7 --style raw --s 250`
  - SDXL：正向 `food photography, ramen bowl, steam, wooden bar, dark moody, top light, 50mm`；负向 `blurry, plastic, text`；DPM++ 2M Karras, Steps 30, CFG 6.5

### A8 · 科技感概念图（未来城市）
- **主体**：悬浮飞行器 + 玻璃幕墙塔楼
- **场景**：夜色未来都市，全息广告
- **风格**：科幻概念艺术
- **光线**：霓虹冷暖对比，体积光
- **镜头**：16mm 广角，低角度仰拍
- **平台参数**：
  - MJ：`floating vehicles and glass tower skyline, futuristic night city with holographic ads, sci-fi concept art, neon cyan-orange contrast, volumetric light, 16mm wide low angle --ar 16:9 --v 7 --s 600 --chaos 25`
  - 可图：`悬浮飞行器与玻璃幕墙塔楼的夜色未来都市，全息广告，科幻概念艺术，霓虹冷暖对比体积光，16mm广角仰拍`；风格通用，尺寸 16:9

---

## B. 文生视频模板（6 条）

### B1 · 产品 360° 展示
- **主体**：运动鞋，缓慢自转
- **场景**：纯色棚背景
- **风格**：产品广告
- **光线**：环形柔光
- **镜头**：固定机位，主体旋转（运镜=转台）
- **平台参数**：
  - 可灵：`一双运动鞋在纯色棚拍背景中缓慢自转展示全身，环形柔光，产品广告风。运镜：固定机位+转台旋转。时长10秒，比例1:1，高品质。`
  - 即梦：`一双运动鞋在纯色背景中缓慢自转360度展示，环形柔光，产品广告，固定机位`；时长10秒，比例1:1

### B2 · 人物行走运镜（跟随）
- **主体**：男性，风衣，行走
- **场景**：雨后的城市街道
- **风格**：电影感
- **光线**：路灯暖光 + 地面反光
- **镜头**：侧后方跟随（运镜=跟随）
- **平台参数**：
  - 即梦：`一位穿风衣的男性在雨后城市街道行走，镜头从侧后方缓慢跟随，路灯暖光映出地面反光，电影感，中景`；时长10秒，比例16:9，运动幅度中
  - 可灵：`男性风衣行走于雨后街道，运镜：侧后方跟随。风格电影感，路灯暖光地面反光。时长10秒，16:9，高品质。`

### B3 · 风景延时 / 云海流动
- **主体**：山巅云海
- **场景**：日出，云层翻涌
- **风格**：自然纪录片
- **光线**：晨光金边
- **镜头**：固定广角，缓慢上摇（运镜=摇+延时感）
- **平台参数**：
  - 可灵：`山顶云海在日出中翻涌流动，延时感，自然纪录片风，晨光金边，运镜：固定广角缓慢上摇。时长10秒，16:9，高品质。`
  - 即梦：`山巅云海在日出下缓缓流动如延时摄影，自然纪录片，晨光金边，固定广角缓慢上摇`；时长10秒，比例16:9

### B4 · 第一人称 Vlog
- **主体**：手持视角（POV）
- **场景**：逛市集，摊位掠过
- **风格**：纪实 Vlog
- **光线**：自然光
- **镜头**：手持微晃，前行（运镜=手持+前移）
- **平台参数**：
  - 即梦：`第一人称视角漫步热闹市集，摊位与人群从眼前掠过，手持微晃纪实vlog，自然光，镜头随步伐前移`；时长10秒，比例9:16，运动幅度中
  - 可灵：`POV手持逛市集，摊位人群掠过，运镜：手持前移。纪实vlog，自然光。时长10秒，9:16，标准。`

### B5 · 转场模板（变身 / 万物归尘）
- **主体**：人物 → 粒子消散 / 沙化
- **场景**：逆光剪影
- **风格**：特效短片
- **光线**：强逆光
- **镜头**：固定，主体由实到虚（运镜=固定+粒子化）
- **平台参数**：
  - 可灵：`逆光剪影人物逐渐化为金色粒子消散于风中（万物归尘），固定机位，强逆光，电影特效。时长10秒，16:9，高品质。` （可用首尾帧锁定人物）
  - 即梦：`一个逆光人物慢慢变成粒子随风消散，固定镜头，强逆光，电影特效感`；时长10秒，比例16:9

### B6 · 城市夜景车流
- **主体**：高架桥车流光轨
- **场景**：繁华都市夜
- **风格**：赛博夜景
- **光线**：车灯与霓虹
- **镜头**：无人机缓慢拉升（运镜=俯拍+上移）
- **平台参数**：
  - 可灵：`繁华都市夜景，高架桥上车流拉出光轨，运镜：无人机缓慢拉升俯拍。赛博夜景风，车灯与霓虹。时长10秒，16:9，高品质。`
  - 即梦：`繁华都市夜景，高架桥车流拉出光轨，无人机缓慢拉升俯拍，赛博夜景，车灯与霓虹`；时长10秒，比例16:9

---

## 使用提示
- 图：先定**主体+场景**，再加**风格+光线+镜头**，最后补平台参数。
- 视频：务必写清**运镜方式**与**时长/比例**，否则模型默认随机。
- 负向提示（图用 `--no`/负向框，视频用负向框）列 `畸变,文字,水印,跳变,肢体扭曲` 通用。
