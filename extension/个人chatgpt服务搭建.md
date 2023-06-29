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
lastmod: 2023-06-29 12:49:08
---

# 个人 chatgpt 服务搭建

## 开通 Azure OpenAI 服务并部署

## 部署 cf-openai-azure-proxy

```bash
docker pull yidadaa/chatgpt-next-web

docker run -d -p 8787:8787 -t --env RESOURCE_NAME=scw-chatgpt --env DEPLOY_NAME_GPT35=scw-gpt35 --env DEPLOY_NAME_GPT4=scw-gpt4 haibbo/cf-openai-azure-proxy
```

## 部署 ChatGPT-Next-Web

```bash
docker pull yidadaa/chatgpt-next-web

docker run -d -p 3000:3000 \
   -e BASE_URL="http://localhost:8787/" \
   -e OPENAI_API_KEY="c1c11320c5f14e4284abd37b24fac4bf" \
   -e CODE="Sudadenglu" \
   -e DISABLE_GPT4=0 \
   -e HIDE_BALANCE_QUERY=1 \
   yidadaa/chatgpt-next-web
```
