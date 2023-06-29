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
lastmod: 2023-06-29 16:14:59
---

# 个人 chatgpt 服务搭建

## 开通 Azure OpenAI 服务并部署

## 部署 openai-azure-proxy 和 ChatGPT-Next-Web

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

## 部署 chatpaper

```bash
docker-compose up --detach --build
```


```yaml
version: '3'

volumes:
  chatpaper_log:
  chatpaper_export:
  chatpaper_pdf_files:
  chatpaper_response_file:
services:
  chatpaper:
    container_name: chatpaper
    expose:
      - 28460
    ports:
      - "3001:8088"
    volumes:
      - "chatpaper_log:/var/log"
      - "chatpaper_export:/opt/chatpaper/export"
      - "chatpaper_pdf_files:/opt/chatpaper/pdf_files"
      - "chatpaper_response_file:/opt/chatpaper/response_file"
    environment:
      API_URL_REDIRECT: {"https://api.openai.com/v1/chat/completions": "重定向的URL"}
      OPENAI_KEY: "c1c11320c5f14e4284abd37b24fac4bf"
      OPENAI_API_BASE: "https://scw-chatgpt.openai.azure.com/"
      OPENAI_API_VERSION: "2023-03-15-preview"
      CHATGPT_MODEL: "scw-gpt35"
    image: "panda1024/chatpaper:v1.0"
    restart: always
```

## 部署 gpt_academic/

```bash
docker-compose up --detach --build
```


```yaml
version: '3'

services:
  gpt_academic_with_latex:
    image: ghcr.io/binary-husky/gpt_academic_with_latex:master
    environment:
      AZURE_ENDPOINT: "https://scw-chatgpt.openai.azure.com/"
      AZURE_API_KEY: "c1c11320c5f14e4284abd37b24fac4bf"
      AZURE_API_VERSION: "2023-03-15-preview"
      AZURE_ENGINE: "scw-gpt35"
      LLM_MODEL: gpt-3.5-turbo
      AVAIL_LLM_MODELS: ["gpt-3.5-turbo", "gpt-4"]
      LOCAL_MODEL_DEVICE: cuda
      DEFAULT_WORKER_NUM: 10
      WEB_PORT: 3002
      
    network_mode: "host"

    command: >
      bash -c "python3 -u main.py"

```
