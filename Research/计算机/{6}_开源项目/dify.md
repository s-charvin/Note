---
title: "Dify"
description: ""
author: ""
tags: [""]
categories: ""
keywords:  [""]
draft: true
layout: ""
date: 2025-04-17 17:27:33
lastmod: 2025-07-09 19:39:38
---

## Dify 安装和使用

### 安装

```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env

// .env 配置文件注意事项
// - 更改 `FORCE_VERIFYING_SIGNATURE` 为 `false` 可以安装未验证插件.
docker compose up -d

// 插件调试
python -m main
```
