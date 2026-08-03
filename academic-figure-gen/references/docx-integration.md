# DOCX 图片插入方案 (DOCX Figure Integration)

## 概述

本方案基于 `python-docx` 库，将 Graphviz 生成的 PNG 图片规范插入 Word 文档（.docx），包含图片居中缩放、图题格式化和编号自动重排。

## 依赖安装

```bash
pip install python-docx Pillow
```

---

## 完整插入脚本

```python
"""
academic_figure_insert.py
学术论文配图插入 Word 文档工具
支持：图片居中缩放、图题格式化、编号自动重排、逆向插入防漂移
"""

import os
import re
from docx import Document
from docx.shared import Cm, Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from PIL import Image


class AcademicFigureInserter:
    """学术论文配图插入器"""
    
    def __init__(self, doc_path: str):
        """
        初始化
        :param doc_path: Word 文档路径
        """
        self.doc_path = doc_path
        if os.path.exists(doc_path):
            self.doc = Document(doc_path)
        else:
            self.doc = Document()
            # 设置默认页面边距（A4，上下 2.54cm，左右 3.17cm）
            for section in self.doc.sections:
                section.top_margin = Cm(2.54)
                section.bottom_margin = Cm(2.54)
                section.left_margin = Cm(3.17)
                section.right_margin = Cm(3.17)
    
    def insert_figure(self,
                      image_path: str,
                      caption: str,
                      width_cm: float = 11.0,
                      insert_position: int = None) -> int:
        """
        插入一张图片到 Word 文档
        
        :param image_path: 图片文件路径（PNG 推荐）
        :param caption: 图题文字（不含"图X"前缀，编号自动生成）
        :param width_cm: 图片显示宽度（cm），默认 11cm（学术论文常用）
        :param insert_position: 插入位置（段落索引），None 则插入文档末尾
        :return: 图片序号
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"图片文件不存在: {image_path}")
        
        # 获取当前图片总数（用于编号）
        figure_number = self._count_existing_figures() + 1
        
        # === 1. 插入图片段落 ===
        image_paragraph = self._create_paragraph(insert_position)
        image_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # 计算图片实际尺寸（保持宽高比）
        with Image.open(image_path) as img:
            img_w_px, img_h_px = img.size
            img_dpi = img.info.get('dpi', (300, 300))
            # 如果 dpi 信息不可靠，默认 300 DPI
            dpi_x = img_dpi[0] if img_dpi[0] > 0 else 300
            aspect = img_h_px / img_w_px
            img_width_inches = img_w_px / dpi_x
            img_height_inches = img_width_inches * aspect
        
        # 插入图片并缩放
        run = image_paragraph.add_run()
        picture = run.add_picture(
            image_path,
            width=Cm(width_cm),
            height=Cm(width_cm * aspect)
        )
        
        # === 2. 插入图题段落 ===
        caption_paragraph = self._create_paragraph(insert_position + 1 if insert_position is not None else None)
        caption_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # 图题格式：宋体、10.5pt（五号）、居中
        run_caption = caption_paragraph.add_run(f"图{figure_number}  {caption}")
        run_caption.font.name = "宋体"
        run_caption._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
        run_caption.font.size = Pt(10.5)
        run_caption.font.color.rgb = RGBColor(0, 0, 0)
        
        # 图题段前间距 6pt、段后间距 12pt
        caption_paragraph.paragraph_format.space_before = Pt(6)
        caption_paragraph.paragraph_format.space_after = Pt(12)
        caption_paragraph.paragraph_format.line_spacing = 1.5
        
        return figure_number
    
    def _create_paragraph(self, position: int = None):
        """在指定位置创建段落"""
        if position is not None and 0 <= position < len(self.doc.paragraphs):
            # 在指定段落前插入
            ref_paragraph = self.doc.paragraphs[position]
            new_paragraph = ref_paragraph.insert_paragraph_before()
            return new_paragraph
        else:
            # 追加到文档末尾
            return self.doc.add_paragraph()
    
    def _count_existing_figures(self) -> int:
        """统计文档中已有的图片数量（通过图题"图X"格式匹配）"""
        count = 0
        for para in self.doc.paragraphs:
            if re.search(r'图\s*\d+', para.text):
                count += 1
        return count
    
    def renumber_figures(self):
        """
        重排所有图片编号
        遍历所有段落，将"图X"依次重编号为图1、图2、图3...
        """
        fig_index = 0
        for para in self.doc.paragraphs:
            text = para.text
            match = re.search(r'图\s*\d+', text)
            if match:
                fig_index += 1
                new_text = re.sub(r'图\s*\d+', f'图{fig_index}', text, count=1)
                # 替换段落文本（通过 run 级别替换以保证格式不变）
                for run in para.runs:
                    if re.search(r'图\s*\d+', run.text):
                        run.text = re.sub(r'图\s*\d+', f'图{fig_index}', run.text, count=1)
                        break
    
    def save(self, output_path: str = None):
        """
        保存文档
        
        :param output_path: 输出路径，None 则覆盖原文件
        """
        save_path = output_path or self.doc_path
        self.doc.save(save_path)
        print(f"✅ 文档已保存至: {save_path}")


# ============================================================
# 使用示例
# ============================================================
if __name__ == "__main__":
    # 初始化插入器
    inserter = AcademicFigureInserter("manuscript.docx")
    
    # 插入多张图片（逆向插入，防止索引漂移）
    figures = [
        ("output/architecture.png", "系统架构分层示意图"),
        ("output/process_flow.png", "业务处理流程"),
        ("output/traceability.png", "全流程工序追溯链"),
        ("output/roadmap.png", "技术演进路线"),
        ("output/data_flow.png", "系统间数据流"),
    ]
    
    # === 关键：逆向插入（从后往前），防止索引漂移 ===
    # 如果没有使用逆向插入，每插入一张图片后，
    # 后续图片的目标插入位置都会偏移，导致顺序混乱
    for image_path, caption in reversed(figures):
        try:
            num = inserter.insert_figure(
                image_path=image_path,
                caption=caption,
                width_cm=11.0,      # 学术论文常用图片宽度
                insert_position=0    # 插入到文档最前面
            )
            print(f"✅ 图{num} 已插入: {caption}")
        except FileNotFoundError as e:
            print(f"⚠️ 跳过: {e}")
    
    # 保存文档
    inserter.save("manuscript_with_figures.docx")
```

---

## 关键参数说明

### 图片宽度

| 场景 | 推荐宽度 | 说明 |
|------|----------|------|
| **双栏排版** | 8 cm | IEEE/ACM 双栏模板 |
| **单栏全宽** | 14 cm | 学位论文、单栏期刊 |
| **通用推荐** | 11 cm | 适合大多数国内学术论文 |
| **并排小图** | 5.5 cm | 两张图并排展示 |

```python
# 双栏排版
inserter.insert_figure("img.png", "图题", width_cm=8.0)

# 单栏全宽
inserter.insert_figure("img.png", "图题", width_cm=14.0)

# 通用推荐
inserter.insert_figure("img.png", "图题", width_cm=11.0)
```

### 图题格式

| 属性 | 标准值 | 说明 |
|------|--------|------|
| 字体 | 宋体 | 中文图题标准字体 |
| 字号 | 10.5pt（五号） | 大多数学位论文/期刊要求 |
| 对齐 | 居中 | 图题居中于图片下方 |
| 段前间距 | 6pt | 与图片轻微间隔 |
| 段后间距 | 12pt | 与正文清晰分隔 |
| 编号格式 | 图1、图2... | 阿拉伯数字顺序编号 |

### 图片 DPI

```bash
# 生成图片时显式指定 300 DPI
dot -Tpng -Gdpi=300 input.dot -o output.png

# 若已生成低 DPI 图片，可用 ImageMagick 提升：
# convert input.png -density 300 output.png
```

---

## 逆向插入防索引漂移原理

**问题：** 当按正序在文档前部依次插入图片时：

1. 插入图1 到段落0 → 原文段落0 变成段落2
2. 插入图2 到段落2（原本想插入段落0） → 实际插入到了错误位置
3. 后续图片位置全部错乱

**解决：** 使用 `for ... in reversed(figures)` 从后往前插入：

1. 插入图5 到段落0 → 不影响后面的插入位置
2. 插入图4 到段落0 → 同样不受影响
3. ... 最终顺序为图1→图5 顺序正确

**等价操作：** 也可以用 `insert_position=None`（追加到末尾）来避免此问题，但图片将出现在文档末尾而非前部。

---

## 批量生成与插入（Shell 脚本）

```bash
#!/bin/bash
# batch_generate_and_insert.sh
# 批量渲染 DOT 图并插入 Word

DOT_DIR="./dot_sources"
PNG_DIR="./output"
DOC_FILE="manuscript.docx"

mkdir -p "$PNG_DIR"

# 1. 批量渲染所有 DOT 文件
for dotfile in "$DOT_DIR"/*.dot; do
    basename=$(basename "$dotfile" .dot)
    echo "渲染: $basename"
    dot -Tpng -Gdpi=300 "$dotfile" -o "$PNG_DIR/${basename}.png"
done

# 2. 调用 Python 脚本插入
python academic_figure_insert.py

echo "✅ 全部完成！"
```

Windows PowerShell 等效：

```powershell
# batch_generate_and_insert.ps1
$DOT_DIR = ".\dot_sources"
$PNG_DIR = ".\output"
$DOC_FILE = "manuscript.docx"

New-Item -ItemType Directory -Force -Path $PNG_DIR

# 1. 批量渲染
Get-ChildItem "$DOT_DIR\*.dot" | ForEach-Object {
    $basename = $_.BaseName
    Write-Host "渲染: $basename"
    dot -Tpng -Gdpi=300 $_.FullName -o "$PNG_DIR\$basename.png"
}

# 2. 插入 Word
python academic_figure_insert.py

Write-Host "✅ 全部完成！"
```

---

## 常见问题

**Q: 图片插入后显示模糊？**
A: 检查渲染时的 DPI 设置。确保使用 `dot -Tpng -Gdpi=300`，Word 默认使用 96 DPI 显示但 300 DPI 保证印刷质量。

**Q: 图题字体未显示为宋体？**
A: 确保系统已安装宋体（SimSun），Windows 通常默认安装。若使用 macOS/Linux，可替换为系统可用中文字体（如 PingFang SC）。

**Q: 图片插入后文档体积过大？**
A: 可在插入前使用 `pngquant` 或 `optipng` 压缩 PNG：
```bash
pngquant --quality=65-80 figure1.png --output figure1_compressed.png
```
