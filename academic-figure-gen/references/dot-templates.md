# DOT 图表模板库 (DOT Diagram Templates)

## 模板使用说明

每个模板使用 `{{PLACEHOLDER}}` 标记可替换参数。使用时按以下步骤操作：

1. 复制模板到新文件
2. 全局替换 `{{PLACEHOLDER}}` 为实际内容
3. 根据 [color-schemes.md](color-schemes.md) 选择合适的配色方案
4. 渲染：`dot -Tpng -Gdpi=300 template.dot -o output.png`

---

## 模板一：架构分层图 (Architecture Layered Diagram)

**适用场景：** 系统架构图、技术栈分层、网络协议栈

```dot
// ============================================================
// 模板：架构分层图
// 说明：类似 OSI 分层的架构示意，自底向上逐层展示
// 替换清单：
//   {{TITLE}}            — 图表标题
//   {{LAYER1_NAME}}      — 第一层（最底层）名称
//   {{LAYER1_ITEMS}}     — 第一层组件，用 \n 分隔
//   {{LAYER2_NAME}}      — 第二层名称
//   {{LAYER2_ITEMS}}     — 第二层组件
//   {{LAYER3_NAME}}      — 第三层名称
//   {{LAYER3_ITEMS}}     — 第三层组件
//   {{LAYER4_NAME}}      — 第四层（最顶层）名称
//   {{LAYER4_ITEMS}}     — 第四层组件
//   {{COLOR_PRIMARY}}    — 主色（节点填充色）
//   {{COLOR_LIGHT}}      — 浅色（层级背景色）
//   {{COLOR_BORDER}}     — 边框色
//   {{COLOR_FONT}}       — 字体色
// ============================================================

digraph Architecture {
    rankdir=TB;
    splines=ortho;
    nodesep=0.5;
    ranksep=0.3;
    
    // 全局样式
    graph [
        fontname="Microsoft YaHei",
        fontsize=16,
        label="{{TITLE}}",
        labelloc="t",
        pad=0.5,
        bgcolor="white"
    ];
    node [
        fontname="Microsoft YaHei",
        fontsize=11,
        shape=box,
        style="filled,rounded",
        fillcolor="{{COLOR_LIGHT}}",
        color="{{COLOR_BORDER}}",
        fontcolor="{{COLOR_FONT}}",
        penwidth=1.2
    ];
    edge [
        color="{{COLOR_BORDER}}",
        penwidth=0.8,
        arrowsize=0.6
    ];
    
    // === 第四层（顶层）===
    subgraph cluster_layer4 {
        label="{{LAYER4_NAME}}";
        fontname="Microsoft YaHei";
        fontsize=12;
        style="filled,rounded";
        fillcolor="#F5F7FA";
        color="{{COLOR_BORDER}}";
        penwidth=1.5;
        
        l4_node [label="{{LAYER4_ITEMS}}", shape=box, style="filled,rounded", fillcolor="{{COLOR_LIGHT}}"];
    }
    
    // === 第三层 ===
    subgraph cluster_layer3 {
        label="{{LAYER3_NAME}}";
        fontname="Microsoft YaHei";
        fontsize=12;
        style="filled,rounded";
        fillcolor="#F5F7FA";
        color="{{COLOR_BORDER}}";
        penwidth=1.5;
        
        l3_node [label="{{LAYER3_ITEMS}}", shape=box, style="filled,rounded", fillcolor="{{COLOR_LIGHT}}"];
    }
    
    // === 第二层 ===
    subgraph cluster_layer2 {
        label="{{LAYER2_NAME}}";
        fontname="Microsoft YaHei";
        fontsize=12;
        style="filled,rounded";
        fillcolor="#F5F7FA";
        color="{{COLOR_BORDER}}";
        penwidth=1.5;
        
        l2_node [label="{{LAYER2_ITEMS}}", shape=box, style="filled,rounded", fillcolor="{{COLOR_LIGHT}}"];
    }
    
    // === 第一层（底层）===
    subgraph cluster_layer1 {
        label="{{LAYER1_NAME}}";
        fontname="Microsoft YaHei";
        fontsize=12;
        style="filled,rounded";
        fillcolor="#F5F7FA";
        color="{{COLOR_BORDER}}";
        penwidth=1.5;
        
        l1_node [label="{{LAYER1_ITEMS}}", shape=box, style="filled,rounded", fillcolor="{{COLOR_LIGHT}}"];
    }
    
    // 层级间的边（依实际架构调整）
    l4_node -> l3_node [style=dashed, dir=both];
    l3_node -> l2_node [style=dashed, dir=both];
    l2_node -> l1_node [style=dashed, dir=both];
}
```

---

## 模板二：业务流程图 (Business Process Flow)

**适用场景：** 审批流程、业务操作步骤、判断分支流程

```dot
// ============================================================
// 模板：业务流程图（报价→合同→执行 通用流程）
// 说明：带判断节点的横向业务流
// 替换清单：
//   {{TITLE}}              — 图表标题
//   {{STEP1}} ~ {{STEP6}}  — 各步骤名称
//   {{DECISION}}           — 判断节点条件文字
//   {{YES_BRANCH}}         — 条件成立分支标签
//   {{NO_BRANCH}}          // 条件不成立分支标签
//   {{COLOR_PRIMARY}}      — 主色
//   {{COLOR_LIGHT}}        — 浅色
//   {{COLOR_BORDER}}       — 边框色
//   {{COLOR_FONT}}         — 字体色
// ============================================================

digraph ProcessFlow {
    rankdir=LR;
    nodesep=0.6;
    ranksep=1.0;
    
    graph [
        fontname="Microsoft YaHei",
        fontsize=16,
        label="{{TITLE}}",
        labelloc="t",
        bgcolor="white"
    ];
    
    // 普通步骤节点
    node [
        fontname="Microsoft YaHei",
        fontsize=11,
        shape=box,
        style="filled,rounded",
        fillcolor="{{COLOR_LIGHT}}",
        color="{{COLOR_BORDER}}",
        fontcolor="{{COLOR_FONT}}",
        penwidth=1.2,
        width=2.0,
        height=0.6
    ];
    edge [
        fontname="Microsoft YaHei",
        fontsize=9,
        color="{{COLOR_BORDER}}",
        penwidth=1.0
    ];
    
    // 流程步骤
    step1 [label="{{STEP1}}"];
    step2 [label="{{STEP2}}"];
    step3 [label="{{STEP3}}"];
    step4 [label="{{STEP4}}"];
    step5 [label="{{STEP5}}"];
    step6 [label="{{STEP6}}"];
    
    // 判断节点（菱形）
    decision [label="{{DECISION}}", shape=diamond, style=filled, fillcolor="#FFF8E1", color="{{COLOR_BORDER}}", fontcolor="{{COLOR_FONT}}"];
    
    // 起止标记
    start [label="开始", shape=ellipse, style=filled, fillcolor="{{COLOR_PRIMARY}}", fontcolor="white"];
    end [label="结束", shape=ellipse, style=filled, fillcolor="{{COLOR_PRIMARY}}", fontcolor="white"];
    
    // 主流程边
    start -> step1 -> step2 -> step3 -> decision;
    
    // 分支流程
    decision -> step4 [label="{{YES_BRANCH}}"];
    decision -> step5 [label="{{NO_BRANCH}}"];
    
    step4 -> step6 -> end;
    step5 -> end [style=dashed, color="#888888"];
}
```

---

## 模板三：工序追溯图 (Process Traceability)

**适用场景：** 制造工序追溯、质量追溯链、批次流转

```dot
// ============================================================
// 模板：工序追溯图
// 说明：多步骤串联 + 每步扫码追溯节点
// 替换清单：
//   {{TITLE}}              — 图表标题
//   {{PROCESS1}} ~ {{PROCESS5}} — 各工序名称
//   {{TRACE_DETAIL_n}}     — 各追溯节点详情（扫码时间/操作人等）
//   {{COLOR_PRIMARY}}      — 主色
//   {{COLOR_LIGHT}}        — 浅色
//   {{COLOR_BORDER}}       — 边框色
//   {{COLOR_FONT}}         — 字体色
//   {{COLOR_ACCENT}}       — 强调色（追溯节点）
// ============================================================

digraph Traceability {
    rankdir=LR;
    nodesep=0.4;
    ranksep=0.8;
    
    graph [
        fontname="Microsoft YaHei",
        fontsize=16,
        label="{{TITLE}}",
        labelloc="t",
        bgcolor="white"
    ];
    
    // 工序节点
    node [
        fontname="Microsoft YaHei",
        fontsize=11,
        shape=box,
        style="filled,rounded",
        fillcolor="{{COLOR_LIGHT}}",
        color="{{COLOR_BORDER}}",
        fontcolor="{{COLOR_FONT}}",
        penwidth=1.2
    ];
    
    // 追溯节点
    node [shape=component, style=filled, fillcolor="{{COLOR_ACCENT}}", color="{{COLOR_PRIMARY}}", fontcolor="white", fontsize=9];
    
    // 数据库节点
    node [shape=cylinder, style=filled, fillcolor="#E8EAF6", color="{{COLOR_BORDER}}", fontcolor="{{COLOR_FONT}}", fontsize=10];
    
    edge [color="{{COLOR_BORDER}}", penwidth=1.0, arrowsize=0.8];
    
    // === 工序链 ===
    p1 [label="{{PROCESS1}}"];
    p2 [label="{{PROCESS2}}"];
    p3 [label="{{PROCESS3}}"];
    p4 [label="{{PROCESS4}}"];
    p5 [label="{{PROCESS5}}"];
    
    // === 追溯节点（扫码记录点）===
    qr1 [label="{{TRACE_DETAIL_1}}"];
    qr2 [label="{{TRACE_DETAIL_2}}"];
    qr3 [label="{{TRACE_DETAIL_3}}"];
    qr4 [label="{{TRACE_DETAIL_4}}"];
    qr5 [label="{{TRACE_DETAIL_5}}"];
    
    // === 追溯数据库 ===
    db [label="追溯数据库\nTraceability DB", width=2.5, height=1.2];
    
    // 工序流转
    p1 -> p2 -> p3 -> p4 -> p5;
    
    // 扫码追溯关联
    p1 -> qr1 [style=dotted];
    p2 -> qr2 [style=dotted];
    p3 -> qr3 [style=dotted];
    p4 -> qr4 [style=dotted];
    p5 -> qr5 [style=dotted];
    
    // 追溯数据入数据库
    qr1 -> db [style=dashed, color="{{COLOR_ACCENT}}"];
    qr2 -> db [style=dashed, color="{{COLOR_ACCENT}}"];
    qr3 -> db [style=dashed, color="{{COLOR_ACCENT}}"];
    qr4 -> db [style=dashed, color="{{COLOR_ACCENT}}"];
    qr5 -> db [style=dashed, color="{{COLOR_ACCENT}}"];
    
    // 数据库反馈（可选）
    db -> p3 [style=dashed, color="#888888", dir=both, label="状态反馈"];
}
```

---

## 模板四：技术演进路线图 (Technology Evolution Roadmap)

**适用场景：** 技术发展历程、产品迭代时间线、方案演进

```dot
// ============================================================
// 模板：技术演进路线图
// 说明：水平时间轴，展示阶段演进
// 替换清单：
//   {{TITLE}}             — 图表标题
//   {{PHASE1_NAME}} ~ {{PHASE4_NAME}}   — 各阶段名称
//   {{PHASE1_DESC}} ~ {{PHASE4_DESC}}   — 各阶段描述
//   {{PHASE1_TIME}} ~ {{PHASE4_TIME}}   — 各阶段时间标注
//   {{COLOR_PRIMARY}}     — 主色
//   {{COLOR_LIGHT}}       — 浅色
//   {{COLOR_BORDER}}      — 边框色
//   {{COLOR_FONT}}        — 字体色
// ============================================================

digraph Roadmap {
    rankdir=LR;
    nodesep=0.3;
    
    graph [
        fontname="Microsoft YaHei",
        fontsize=16,
        label="{{TITLE}}",
        labelloc="t",
        bgcolor="white",
        pad=0.5
    ];
    
    // 阶段节点
    node [
        fontname="Microsoft YaHei",
        fontsize=11,
        shape=box,
        style="filled,rounded",
        width=2.8,
        height=1.2,
        penwidth=1.2
    ];
    
    // 各阶段使用渐变色（从浅到深）
    phase1 [label="{{PHASE1_NAME}\n\n{{PHASE1_DESC}}\n{{PHASE1_TIME}}",
            fillcolor="#F0F4FA", color="{{COLOR_BORDER}}", fontcolor="{{COLOR_FONT}}"];
    phase2 [label="{{PHASE2_NAME}\n\n{{PHASE2_DESC}}\n{{PHASE2_TIME}}",
            fillcolor="{{COLOR_LIGHT}}", color="{{COLOR_BORDER}}", fontcolor="{{COLOR_FONT}}"];
    phase3 [label="{{PHASE3_NAME}\n\n{{PHASE3_DESC}}\n{{PHASE3_TIME}}",
            fillcolor="#8FBCE0", color="{{COLOR_PRIMARY}}", fontcolor="white"];
    phase4 [label="{{PHASE4_NAME}\n\n{{PHASE4_DESC}}\n{{PHASE4_TIME}}",
            fillcolor="{{COLOR_PRIMARY}}", color="{{COLOR_PRIMARY}}", fontcolor="white"];
    
    // 箭头连接
    edge [
        color="{{COLOR_PRIMARY}}",
        penwidth=2.5,
        arrowsize=1.2,
        arrowhead="normal"
    ];
    
    phase1 -> phase2 -> phase3 -> phase4;
    
    // 里程碑标记（可选）
    node [shape=point, width=0, height=0, fillcolor="{{COLOR_PRIMARY}}", color="{{COLOR_PRIMARY}}"];
    milestone [label="关键里程碑", shape=plaintext, fontsize=9, fontcolor="{{COLOR_PRIMARY}}"];
    
    milestone -> phase3 [style=dotted, color="{{COLOR_PRIMARY}}", penwidth=1.0];
}
```

---

## 模板五：数据流图 (Data Flow Diagram)

**适用场景：** 系统间数据流转、接口交互、微服务通信

```dot
// ============================================================
// 模板：数据流图
// 说明：展示多个系统/模块间的数据流转
// 替换清单：
//   {{TITLE}}               — 图表标题
//   {{SYSTEM_A}} ~ {{SYSTEM_D}} — 各系统名称
//   {{DATA_FLOW_1}} ~ {{DATA_FLOW_5}} — 各数据流标签
//   {{STORAGE_NAME}}        — 数据存储名称
//   {{COLOR_PRIMARY}}       — 主色
//   {{COLOR_LIGHT}}         — 浅色
//   {{COLOR_BORDER}}        — 边框色
//   {{COLOR_FONT}}          — 字体色
// ============================================================

digraph DataFlow {
    rankdir=LR;
    nodesep=0.8;
    ranksep=1.2;
    
    graph [
        fontname="Microsoft YaHei",
        fontsize=16,
        label="{{TITLE}}",
        labelloc="t",
        bgcolor="white"
    ];
    
    // 系统节点（圆角矩形）
    node [
        fontname="Microsoft YaHei",
        fontsize=11,
        shape=box,
        style="filled,rounded",
        fillcolor="{{COLOR_LIGHT}}",
        color="{{COLOR_BORDER}}",
        fontcolor="{{COLOR_FONT}}",
        penwidth=1.2,
        width=2.2,
        height=0.8
    ];
    
    // 外部实体
    node [shape=folder, style=filled, fillcolor="#ECEFF1", color="#90A4AE", fontcolor="{{COLOR_FONT}}"];
    
    // 数据存储（圆柱）
    node [shape=cylinder, style=filled, fillcolor="#E8EAF6", color="{{COLOR_BORDER}}", fontcolor="{{COLOR_FONT}}", width=3.0, height=1.2];
    
    // 数据流边
    edge [
        fontname="Microsoft YaHei",
        fontsize=9,
        color="{{COLOR_PRIMARY}}",
        penwidth=1.2,
        arrowsize=0.8
    ];
    
    // === 系统节点 ===
    sys_a [label="{{SYSTEM_A}}"];
    sys_b [label="{{SYSTEM_B}}"];
    sys_c [label="{{SYSTEM_C}}"];
    sys_d [label="{{SYSTEM_D}}"];
    
    // === 数据存储 ===
    storage [label="{{STORAGE_NAME}}"];
    
    // === 外部系统 ===
    external [label="外部系统\nExternal", shape=folder];
    
    // === 数据流（带标签）===
    external -> sys_a [label="{{DATA_FLOW_1}}"];
    
    sys_a -> sys_b [label="{{DATA_FLOW_2}}"];
    sys_b -> sys_c [label="{{DATA_FLOW_3}}"];
    sys_a -> storage [label="{{DATA_FLOW_4}}", style=dashed, dir=both];
    storage -> sys_c [label="{{DATA_FLOW_5}}", style=dashed];
    
    sys_c -> sys_d [label="处理结果", style=bold];
    
    // === 外部输出（可选）===
    sys_d -> external [label="反馈/输出", style=dotted, color="#888888"];
    
    // 同层对齐
    { rank=same; sys_a; storage; }
    { rank=same; sys_b; sys_c; }
}
```

---

## DOT 通用最佳实践

### 1. 方向控制 (`rankdir`)

| 值 | 含义 | 适用场景 |
|----|------|----------|
| `TB` | 从上到下 (Top→Bottom) | 分层架构、组织结构 |
| `LR` | 从左到右 (Left→Right) | 流程、时间线、数据流 |
| `BT` | 从下到上 | 反向追溯 |
| `RL` | 从右到左 | 阿拉伯语/希伯来语 |

### 2. 节点形状 (`shape`)

```dot
// 常用形状及其学术论文适用场景
node [shape=box]           // 矩形 — 通用节点
node [shape=box,style=rounded]  // 圆角矩形 — 系统/模块（推荐）
node [shape=diamond]       // 菱形 — 判断/决策
node [shape=ellipse]       // 椭圆 — 起点/终点
node [shape=cylinder]      // 圆柱 — 数据库/存储
node [shape=component]     // 组件 — 追溯/扫码节点
node [shape=folder]        // 文件夹 — 外部系统/文件
node [shape=plaintext]     // 纯文本 — 标签/注释
node [shape=record]        // 记录 — 复杂表格结构
```

### 3. 边样式 (`edge`)

```dot
edge [style=solid]         // 实线 — 主流程
edge [style=dashed]        // 虚线 — 辅助关系/异步
edge [style=dotted]        // 点线 — 弱关联/可选
edge [style=bold]          // 粗线 — 关键路径
edge [dir=both]            // 双箭头 — 双向数据流
edge [dir=none]            // 无箭头 — 关联关系
edge [arrowhead=none]      // 无箭头头 — 纯连接线
edge [arrowhead=normal]    // 标准箭头
edge [arrowhead=open]      // 空心箭头（UML 风格）
```

### 4. 子图分组 (`subgraph cluster`)

```dot
// cluster 前缀使子图显示为带边框的组
subgraph cluster_name {
    label="分组名称";
    style=filled;          // 填充背景
    color="#CCCCCC";       // 边框颜色
    fillcolor="#F5F5F5";   // 背景色
}
```

### 5. 同层对齐 (`rank=same`)

```dot
// 强制某些节点在同一水平/垂直位置
{ rank=same; node_a; node_b; node_c; }
```

### 6. 间距控制

```dot
graph [nodesep=0.5   // 同级节点水平间距
       ranksep=0.8]  // 不同层垂直间距
```

### 7. 高 DPI 渲染命令

```bash
# 300 DPI PNG（论文推荐）
dot -Tpng -Gdpi=300 input.dot -o output.png

# 固定尺寸 + 300 DPI
dot -Tpng -Gdpi=300 -Gsize=5.5,4\! input.dot -o output.png

# SVG 输出（矢量，推荐用于 LaTeX）
dot -Tsvg input.dot -o output.svg
```
