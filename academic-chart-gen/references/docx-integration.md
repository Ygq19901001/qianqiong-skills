# 数据图嵌入Word专项 | DOCX Integration

> 简化版 Word 嵌入指南。完整 Word 文档操作见 academic-docx-toolkit 技能。
> 本文件专注于数据图嵌入 Word 的格式规范与自动化。

---

## 概述 | Overview

学术论文中的数据图嵌入 Word 文档时需遵循特定格式规范。本文件提供标准图片宽度设置、中英文图题格式、多图并列排版方法，以及图表目录自动生成的脚本。

---

## 1. 标准图片宽度 | Standard Figure Widths

嵌入 Word 时，图片宽度应与目标期刊的栏宽一致。

| 期刊系列 | 单栏宽度 (mm) | 单栏宽度 (inch) | Word中推荐宽度 |
|---------|-------------|----------------|---------------|
| Nature 系列 | 89 | 3.50 | 3.50 inch |
| Science 系列 | 55 | 2.17 | 2.17 inch |
| Elsevier | 90 | 3.54 | 3.54 inch |
| 中文学报 | 80 | 3.15 | 3.15 inch |
| 双栏通栏 | 160-190 | 6.30-7.48 | 6.00 inch |

```python
# 标准宽度（inch）
FIGURE_WIDTHS = {
    'nature_single': 3.50,
    'nature_double': 7.20,
    'science_single': 2.17,
    'science_double': 4.53,
    'elsevier_single': 3.54,
    'elsevier_double': 7.48,
    'chinese_single': 3.15,
    'chinese_double': 6.30,
}
```

---

## 2. 图题格式 | Figure Captions

### 2.1 中文论文图题

```
图X 各组抗拉强度比较（均值 ± SEM，n=12/组）
注：*** p<0.001, ** p<0.01, * p<0.05 vs 对照组；误差线表示标准误。
```

**规范要点**（GB/T 7713.1-2006）：
- 图序用阿拉伯数字按章节编号（如图2-1）或全文连续编号（如图1）
- 图序与图题之间空一个中文字符
- 图题置于图的下方，居中排列
- 图注（如有）置于图题下方

### 2.2 英文论文图题

```
Fig. 1. Tensile strength across temperature conditions.
(A) Bar chart showing group means ± SEM (n=12 per group).
(B) Box plot of individual data points. *** p<0.001, ** p<0.01 vs. 20°C
group by one-way ANOVA with Tukey's post-hoc test.
```

**规范要点**：
- "Fig." 后跟数字和句点
- 首句为图的总标题（通常不加粗）
- 子图描述用 (A), (B), (C)... 开头
- 统计信息在末尾说明

### 2.3 图题生成器

```python
def generate_figure_caption(fig_num, title, subfigures=None,
                             stats_info=None, lang='zh'):
    """
    生成标准图题。

    Parameters
    ----------
    fig_num : int or str
        图编号
    title : str
        图题主体
    subfigures : list of str or None
        子图描述列表，如 ["(A) 柱状图", "(B) 箱线图"]
    stats_info : str or None
        统计信息，如 "*** p<0.001 vs 对照组"
    lang : str
        'zh' (中文) | 'en' (英文)

    Returns
    -------
    str
    """
    if lang == 'zh':
        caption = f'图{fig_num} {title}'
        if subfigures:
            caption += '\n注：' + '；'.join(subfigures)
        if stats_info:
            if subfigures:
                caption += '。' + stats_info
            else:
                caption += '\n注：' + stats_info
    else:  # English
        caption = f'Fig. {fig_num}. {title}'
        if subfigures:
            caption += '\n' + ' '.join(subfigures)
        if stats_info:
            caption += ' ' + stats_info

    return caption


# 使用示例
caption_zh = generate_figure_caption(
    1,
    '三种药物干预前后生物标志物水平变化（均值 ± SEM，n=15/组）',
    stats_info='*** p<0.001 vs Vehicle组，## p<0.01 组内干预前后比较'
)
print(caption_zh)

caption_en = generate_figure_caption(
    1,
    'Biomarker levels before and after three drug interventions '
    '(mean ± SEM, n=15 per group).',
    stats_info='*** p<0.001 vs. Vehicle; ## p<0.01 pre vs. post within group.',
    lang='en'
)
print(caption_en)
```

---

## 3. 图片嵌入Word | Embedding Figures in Word

### 3.1 单图嵌入

```python
from docx import Document
from docx.shared import Inches, Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def insert_figure(doc, image_path, width_inches=3.5,
                  caption=None, alignment='center'):
    """
    在Word文档中插入单张图片和图题。

    Parameters
    ----------
    doc : docx.Document
        目标文档对象
    image_path : str
        图片文件路径（推荐PNG 600dpi）
    width_inches : float
        图片宽度（inch）
    caption : str or None
        图题文本
    alignment : str
        'center' | 'left' | 'right'
    """
    # 插入图片
    paragraph = doc.add_paragraph()
    align_map = {
        'center': WD_ALIGN_PARAGRAPH.CENTER,
        'left': WD_ALIGN_PARAGRAPH.LEFT,
        'right': WD_ALIGN_PARAGRAPH.RIGHT,
    }
    paragraph.alignment = align_map.get(alignment, WD_ALIGN_PARAGRAPH.CENTER)

    run = paragraph.add_run()
    run.add_picture(image_path, width=Inches(width_inches))

    # 插入图题（居中、不加粗）
    if caption:
        caption_para = doc.add_paragraph()
        caption_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption_run = caption_para.add_run(caption)

        # 图题格式：仿宋_GB2312 / Times New Roman，五号(10.5pt)
        caption_run.font.size = Pt(10.5)
        caption_run.font.name = 'Times New Roman'
        caption_run.bold = False

    # 图与下文之间加空行
    doc.add_paragraph()

    return doc
```

### 3.2 多图并列（Subplots）

```python
from docx.shared import Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def insert_multi_panel_figure(doc, image_paths, panel_labels,
                               images_per_row=2, total_width=6.0,
                               gap=0.2, caption=None):
    """
    插入多面板并列图（如 Fig. 1A, 1B）。

    使用无边框表格实现对齐。

    Parameters
    ----------
    doc : docx.Document
    image_paths : list of str
        各子图文件路径
    panel_labels : list of str
        面板标签，如 ['(A)', '(B)', '(C)', '(D)']
    images_per_row : int
        每行几张图
    total_width : float
        整行总宽度 (inch)
    gap : float
        图间距 (inch)
    caption : str or None
        总图题
    """
    n = len(image_paths)
    n_rows = (n + images_per_row - 1) // images_per_row

    # 创建表格
    table = doc.add_table(rows=n_rows, cols=images_per_row)
    table.autofit = True

    single_width = (total_width - gap * (images_per_row - 1)) / images_per_row
    fig_idx = 0

    for row in range(n_rows):
        for col in range(images_per_row):
            if fig_idx >= n:
                break

            cell = table.cell(row, col)

            # 清除默认段落
            cell.paragraphs[0].clear()

            # 插入标签
            label_para = cell.paragraphs[0]
            label_para.alignment = 1  # center
            label_run = label_para.add_run(panel_labels[fig_idx])
            label_run.bold = True
            label_run.font.size = Pt(9)

            # 插入图片
            img_para = cell.add_paragraph()
            img_para.alignment = 1
            img_run = img_para.add_run()
            img_run.add_picture(image_paths[fig_idx],
                                width=Inches(single_width))

            fig_idx += 1

    # 图题
    if caption:
        caption_para = doc.add_paragraph()
        caption_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption_run = caption_para.add_run(caption)
        caption_run.font.size = Pt(10.5)
        caption_run.font.name = 'Times New Roman'

    doc.add_paragraph()
    return doc


# ========== 使用示例 ==========
# doc = Document('manuscript.docx')
# doc = insert_multi_panel_figure(
#     doc,
#     ['fig1a.png', 'fig1b.png', 'fig1c.png', 'fig1d.png'],
#     ['(A)', '(B)', '(C)', '(D)'],
#     images_per_row=2,
#     total_width=6.0,
#     caption='Fig. 1. Biomarker expression levels across treatment groups.'
# )
# doc.save('manuscript.docx')
```

---

## 4. 图表目录生成 | List of Figures

### 4.1 基于Word内置标题样式

```python
def add_figure_to_toc(doc, figure_caption):
    """
    使用"题注"样式添加图题，确保能被自动目录收录。

    Word中需先定义"Figure Caption"或"题注"样式。
    """
    paragraph = doc.add_paragraph()
    paragraph.style = doc.styles['题注']  # 或 'Figure Caption'
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    run = paragraph.add_run(figure_caption)
    run.font.size = Pt(10.5)
    run.font.name = 'Times New Roman'

    return doc
```

### 4.2 插入图表目录

```python
def insert_figure_table_of_contents(doc, title='图表目录'):
    """
    插入图表目录域代码。

    Note: python-docx不支持直接插入TOC域，此处提供手动指南。
    推荐做法：保存文档后，在Word中手动插入图表目录。
    """
    # Word 操作步骤：
    # 1. 引用 → 插入表目录
    # 2. 题注标签选择"图"
    # 3. 点击确定

    heading = doc.add_heading(title, level=1)

    # 添加占位提示
    para = doc.add_paragraph()
    run = para.add_run(
        '【在此处插入图表目录】\n'
        'Word操作：引用 → 插入表目录 → 题注标签选择"图" → 确定\n'
        '或使用 python-docx 无法直接生成 TOC，请在Word中手动操作。'
    )
    run.font.color.rgb = RGBColor(128, 128, 128)
    run.font.size = Pt(9)
    run.italic = True

    return doc
```

---

## 5. 完整嵌入脚本 | Complete Embedding Script

```python
def embed_chart_pipeline(image_files, captions, output_docx,
                          journal='chinese_single',
                          multi_panel=False, images_per_row=2):
    """
    将一组图表嵌入Word文档的完整脚本。

    Parameters
    ----------
    image_files : list of str or list of list of str
        图片文件路径列表
        如果 multi_panel=True，则为二维列表 [[fig1a, fig1b], [fig2], ...]
    captions : list of str
        图题列表
    output_docx : str
        输出Word文档路径
    journal : str
        期刊预设名称（用于确定宽度）
    multi_panel : bool
        是否使用多面板并列排版
    images_per_row : int
        每行几张图（multi_panel=True时生效）

    Returns
    -------
    str
        输出文件路径
    """
    width = FIGURE_WIDTHS.get(journal, 3.15)

    doc = Document()

    # 设置默认字体
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)

    for i, (imgs, caption) in enumerate(zip(image_files, captions)):
        if multi_panel and isinstance(imgs, list):
            # 多面板图
            labels = [f'({chr(65+j)})' for j in range(len(imgs))]
            doc = insert_multi_panel_figure(
                doc, imgs, labels,
                images_per_row=images_per_row,
                total_width=width * 2 if width < 4 else width,
                caption=caption
            )
        else:
            # 单图
            img_path = imgs if isinstance(imgs, str) else imgs[0]
            doc = insert_figure(doc, img_path, width_inches=width,
                                caption=caption)

    doc.save(output_docx)
    print(f"Document saved: {output_docx}")
    print(f"Total figures: {len(image_files)}")
    print(f"Journal preset: {journal} ({width} inch wide)")

    return output_docx


# ========== 使用示例 ==========
# embed_chart_pipeline(
#     image_files=[
#         'output/fig1_bar.png',
#         'output/fig2_scatter.png',
#         ['output/fig3a_box.png', 'output/fig3b_violin.png'],
#     ],
#     captions=[
#         '图1 各组细胞活性比较',
#         '图2 生物标志物相关性分析',
#         '图3 数据分布可视化。(A)箱线图；(B)小提琴图',
#     ],
#     output_docx='manuscript_with_figures.docx',
#     journal='chinese_single',
# )
```

---

## 6. 常见问题 | FAQ

| 问题 | 解决方案 |
|------|---------|
| 图片在Word中模糊 | 确保保存为PNG 600dpi；避免使用JPG |
| 图题编号错乱 | 使用Word的"题注"功能自动编号 |
| 多图无法对齐 | 使用无边框表格（border=0）装载图片 |
| 文件过大（>20MB） | 适度降低dpi至300；或另存矢量格式备用 |
| 图表目录不更新 | Word中右键目录 → 更新域 → 更新整个目录 |
| 图片跨页断裂 | 设置图片段落"与下段同页"属性 |

---

## 相关技能 | Related Skills

- **academic-docx-toolkit**：完整的Word学术文档操作（样式、页眉页脚、参考文献、分节）
- **academic-figure-gen**：架构图/流程图生成
- **本技能 (academic-chart-gen)**：数据统计图生成
