# Graphviz 安装与配置指南 (Graphviz Setup Guide)

## 版本要求

- **最低版本：Graphviz 2.44**（2020 年 4 月发布）
- **推荐版本：Graphviz 7.0+**（更好的 SVG 输出和字体支持）
- 验证安装：`dot -V`

---

## Windows 安装

### 方法一：官方安装包（推荐）

1. 访问 [Graphviz Download](https://graphviz.org/download/) 
2. 下载 Windows 安装包（如 `graphviz-7.0.0-win64.exe`）
3. 运行安装程序，**务必勾选 "Add Graphviz to the system PATH"**
4. 安装完成后 **重启终端**，运行验证：

```powershell
dot -V
```

预期输出：
```
dot - graphviz version 7.0.0 (20230908.1234)
```

### 方法二：Scoop 包管理器

```powershell
scoop install graphviz
```

### 方法三：Chocolatey

```powershell
choco install graphviz
```

### Windows 常见问题

**Q: `dot` 不是内部或外部命令**
A: Graphviz 未加入 PATH。手动添加：

1. 找到 Graphviz 安装目录下的 `bin` 文件夹（通常为 `C:\Program Files\Graphviz\bin`）
2. 将 `C:\Program Files\Graphviz\bin` 添加到系统环境变量 `PATH`
3. **重启终端**后重试

**Q: 中文字体渲染为方框**
A: Windows 下需要指定中文字体。在 DOT 文件中添加：

```dot
graph {
    fontname="Microsoft YaHei"
    node [fontname="Microsoft YaHei"]
    edge [fontname="Microsoft YaHei"]
}
```

**Q: 找不到 `dot.exe` 的具体路径**
A: 在 PowerShell 中运行：
```powershell
Get-Command dot.exe | Select-Object -ExpandProperty Source
```

---

## macOS 安装

### 方法一：Homebrew（推荐）

```bash
brew install graphviz
```

验证：
```bash
dot -V
```

### 方法二：MacPorts

```bash
sudo port install graphviz
```

### macOS 常见问题

**Q: 中文字体问题**
A: macOS 推荐使用苹方（PingFang SC）或华文宋体：

```dot
graph {
    fontname="PingFang SC"
    node [fontname="PingFang SC"]
}
```

**Q: Homebrew 安装后 dot 仍不可用**
A: 检查 Homebrew 前缀并刷新 shell：
```bash
brew --prefix
# 确保 /opt/homebrew/bin 或 /usr/local/bin 在 PATH 中
hash -r  # 刷新 zsh/bash 命令缓存
```

---

## Linux 安装

### Debian / Ubuntu

```bash
sudo apt update
sudo apt install graphviz
```

### RHEL / CentOS / Fedora

```bash
# Fedora 22+
sudo dnf install graphviz

# CentOS 7 / RHEL 7
sudo yum install graphviz
```

### Arch Linux

```bash
sudo pacman -S graphviz
```

### Linux 常见问题

**Q: 中文字体缺失**
A: 安装中文字体包：

```bash
# Ubuntu/Debian
sudo apt install fonts-wqy-microhei fonts-wqy-zenhei

# CentOS/RHEL
sudo yum install wqy-microhei-fonts wqy-zenhei-fonts

# Arch
sudo pacman -S wqy-microhei wqy-zenhei
```

然后在 DOT 文件中指定：
```dot
graph {
    fontname="WenQuanYi Micro Hei"
    node [fontname="WenQuanYi Micro Hei"]
}
```

---

## 验证 Graphviz 完整可用

运行以下命令验证所有必要组件：

```bash
# 1. 版本检查
dot -V

# 2. 查看可用输出格式（确认 png/svg/pdf 支持）
dot -T?

# 3. 快速渲染测试
echo 'digraph { A -> B; }' | dot -Tpng -o test.png
# 检查 test.png 是否正常生成
```

---

## 输出格式选择

| 格式 | 命令 | 适用场景 |
|------|------|----------|
| PNG | `dot -Tpng input.dot -o output.png` | Word 文档插入（推荐） |
| SVG | `dot -Tsvg input.dot -o output.svg` | LaTeX 排版、网页展示 |
| PDF | `dot -Tpdf input.dot -o output.pdf` | LaTeX 直接嵌入 |
| EPS | `dot -Teps input.dot -o output.eps` | 传统 LaTeX + dvips 工作流 |

**论文配图推荐参数：**

```bash
dot -Tpng -Gdpi=300 -Gsize=5.5,4! input.dot -o figure1.png
```

- `-Gdpi=300`：300 DPI 满足期刊印刷要求
- `-Gsize=5.5,4!`：强制 5.5×4 英寸（约 14×10 cm），感叹号固定尺寸
