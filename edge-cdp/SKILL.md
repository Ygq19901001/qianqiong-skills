---
name: edge-cdp
slug: edge-cdp
displayName: Edge CDP
version: 2.2.0
author: QianQiong
license: MIT
summary: Edge CDP 浏览器远程控制，通过 DevTools Protocol 实现截图、DOM、JS、Cookie 管理
allowedTools: []
description: Edge CDP 自动化 Skill。通过 Chrome DevTools Protocol 远程控制 Microsoft Edge 浏览器，支持页面导航、截图、DOM操作、JS执行、Cookie管理。适用于浏览器自动化场景。
metadata: {"openclaw":{"emoji":"🌐"}}
---

## When to Use / 触发场景

Trigger keywords: Edge CDP, DevTools Protocol, browser automation, msedge, 浏览器自动化, 截图, DOM操作, Cookie管理

| Usage Scenario | 说明 |
|-------|------|
| Edge CDP、浏览器自动化、msedge | 启动/控制 Edge 浏览器 |
| CDP、DevTools Protocol | 通过 CDP 执行浏览器操作 |
| 截图、DOM操作、Cookie管理 | 常见自动化任务 |

## 概述

Microsoft Edge 基于 Chromium，支持完整的 Chrome DevTools Protocol (CDP)。本 Skill 通过 WebSocket 连接 Edge 的 CDP 调试端口，实现远程自动化控制。

## 环境要求

| 项目 | 值 |
|------|-----|
| 浏览器路径 | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` |
| 版本 | 150.0.4078.65 |
| CDP 端口 | `9222` |
| WebSocket 端点 | `ws://127.0.0.1:9222/devtools/browser/<uuid>` |

## 启动命令

```powershell
Start-Process "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" -ArgumentList "--remote-debugging-port=9222"
```

健康检查：
```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\Administrator\.qclaw\workspace-departments\tiangongge\scripts\check-edge-cdp.ps1"
```

## 验证 CDP

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:9222/json/version" -TimeoutSec 5
Invoke-RestMethod -Uri "http://127.0.0.1:9222/json" -TimeoutSec 5
```

## 常用 CDP 操作

### 页面导航
```json
{ "id": 1, "method": "Page.navigate", "params": { "url": "https://example.com" } }
```

### 截图
```json
{ "id": 2, "method": "Page.captureScreenshot", "params": { "format": "png", "quality": 80 } }
```

### 执行 JavaScript
```json
{ "id": 3, "method": "Runtime.evaluate", "params": { "expression": "document.title", "returnByValue": true } }
```

### Cookie 管理
```json
{ "id": 4, "method": "Network.getCookies", "params": { "urls": ["https://example.com"] } }
```

### DOM 查询
```json
{ "id": 6, "method": "DOM.getDocument" }
{ "id": 7, "method": "DOM.querySelector", "params": { "nodeId": 1, "selector": "#main" } }
```

### 网络拦截
```json
{ "id": 9, "method": "Network.enable" }
```

## 故障排查

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 连接拒绝 | Edge 未启动或未带调试参数 | `Start-Process ... -ArgumentList "--remote-debugging-port=9222"` |
| WebSocket 断开 | 标签页关闭 | 重新获取 `json/version` 拿新 WebSocket URL |
| 端口占用 | 其他进程占 9222 | `netstat -ano | findstr 9222` 查占用 |
| 权限不足 | 防火墙阻止本地连接 | 127.0.0.1:9222 加防火墙白名单 |

## 变更记录

- v2.0.1 2026-07-20: 周检维护，补全metadata，上架ClawHub
- v2.0.0 2026-07-15: QQBrowser → Edge 全量迁移
- v1.0.0 2026-07-06: 初始版本（QQBrowser CDP）

## FAQ（高频问题速查）

**Q1：Edge 没启动/连接不上？**
先按「启动命令」用 --remote-debugging-port 启动 Edge，再测 `http://127.0.0.1:9222/json/version`（QP-E901）。

**Q2：CDP 端口被占用？**
换端口启动，注意 9222 被占用时 Edge 不会报错只是连不上。

**Q3：截图/DOM 操作失败？**
确认目标页面已加载完成；frame 内元素需先切换到对应 frame。

**Q4：这个 skill 能控制 Chrome 吗？**
CDP 协议通用，Chrome/Edge 均可；本 skill 以 Edge 为例。

## QP 错误码（专用段 E901+）

| 码 | 含义 | 修正引导 |
|----|------|---------|
| QP-E901 | CDP 连接失败 | 检查 Edge 是否以 remote-debugging 启动、端口是否正确 |
| QP-E902 | 端口占用 | 换端口重启浏览器 |
| QP-E903 | 页面加载未完成 | 等待 load 事件后再操作 |
| QP-E904 | frame 定位失败 | 显式切换到目标 frame |
| QP-E905 | WebSocket 断开 | 重连，检查浏览器是否被关闭 |

## 输入/输出约束

| 项 | 约束 |
|----|------|
| 输入 | 目标 URL + 操作指令（导航/截图/DOM/JS/Cookie） |
| 前置 | Edge 以 --remote-debugging-port 启动，CDP 端点可达 |
| 输出 | 操作结果（截图文件/DOM 结构/JS 返回值/Cookie 数据） |
