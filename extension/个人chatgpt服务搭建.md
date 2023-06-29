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
lastmod: 2023-06-29 13:27:46
---

# 个人 chatgpt 服务搭建

## 开通 Azure OpenAI 服务并部署

## 部署 openai-azure-proxy 和 

```bash
docker-compose up --detach --build
```




```yaml
version: '3'

services:
  chatgpt-next-web:
    image: yidadaa/chatgpt-next-web
    ports:
      - 3000:3000
    environment:
      OPENAI_API_KEY: "c1c11320c5f14e4284abd37b24fac4bf"
      BASE_URL: http://azure-openai:8080
      DISABLE_GPT4: 1
      CODE: "Sudadenglu"
      HIDE_BALANCE_QUERY: 1
    depends_on:
      - azure-openai
    links:
      - azure-openai
    restart: always


  azure-openai:
    image: stulzq/azure-openai-proxy
    ports:
      - 8080:8080
    environment:
      AZURE_OPENAI_ENDPOINT: "https://scw-chatgpt.openai.azure.com/"
      AZURE_OPENAI_MODEL_MAPPER: gpt-3.5-turbo=scw-gpt35
      AZURE_OPENAI_API_VER: 2023-03-15-preview
    restart: always
```

## 部署 ChatGPT-Next-Web

```bash
docker pull yidadaa/chatgpt-next-web

docker run -d -p 3000:3000 \
   -e BASE_URL="http://localhost:8787/v1/chat/completions" \
   -e OPENAI_API_KEY="c1c11320c5f14e4284abd37b24fac4bf" \
   -e CODE="Sudadenglu" \
   -e DISABLE_GPT4=0 \
   -e HIDE_BALANCE_QUERY=1 \
   yidadaa/chatgpt-next-web


```
