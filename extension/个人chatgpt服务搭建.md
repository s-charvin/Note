---
title: "{{个人 chatgpt 服务搭建}}"
description: ""
author: ""
tags: [""]
categories: ""
keywords:  [""]
draft: true
layout: ""
date: 2023-06-29 12:28:05
lastmod: 2023-06-29 12:31:51
---

# 个人 chatgpt 服务搭建

## 开通 Azure OpenAI 服务并部署

## 部署 cf-openai-azure-proxy

```bash
docker run -d -p 8787:8787 -t --env RESOURCE_NAME=scw-chatgpt --env DEPLOY_NAME_GPT35=scw-gpt35 --env DEPLOY_NAME_GPT4=scw-gpt4 haibbo/cf-openai-azure-proxy
```
