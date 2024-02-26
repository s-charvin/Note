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
lastmod: 2023-08-16 17:02:43
---

# 个人 chatgpt 服务搭建

## 开通 Azure OpenAI 服务并部署

## 部署 openai-azure-proxy 和 ChatGPT-Next-Web

```
# 直接安装

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
nvm install 16
nvm use 16
sudo apt install npm
sudo npm install -g yarn
git clone https://github.com/Yidadaa/ChatGPT-Next-Web
cd ChatGPT-Next-Web
yarn install



bash <(curl -s https://raw.githubusercontent.com/Yidadaa/ChatGPT-Next-Web/main/scripts/setup.sh)

NODE_OPTIONS="--max-old-space-size=512" OPENAI_API_KEY="c1c11320c5f14e4284abd37b24fac4bf" CODE="Sudadenglu" PORT=3000 BASE_URL=http://127.0.0.1:8080 DISABLE_GPT4=1 HIDE_BALANCE_QUERY=1 yarn build

OPENAI_API_KEY="c1c11320c5f14e4284abd37b24fac4bf" CODE="Sudadenglu" PORT=3000 BASE_URL=http://127.0.0.1:8080 DISABLE_GPT4=1 HIDE_BALANCE_QUERY=1 yarn start
```

```bash
# docker 安装

sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo service docker restart
sudo apt install docker-compose

vi docker-compose.yml

#卸载

systemctl stop docker
apt-get autoremove docker docker-ce docker-engine  docker.io  containerd runc
apt-get autoremove docker-compose
apt-get autoremove docker-ce-*
apt-get autoremove docker-buildx-plugin docker-compose-plugin
dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P

rm -rf /etc/systemd/system/docker.service.d
rm -rf /var/lib/docker
rm -rf /etc/docker
```


```yaml

version: '3'

services:
  chatgpt-next-web:
    image: yidadaa/chatgpt-next-web:latest
    ports:
      - 3000:3000
    environment:
      OPENAI_API_KEY: "c1c11320c5f14e4284abd37b24fac4bf"
      BASE_URL: http://azure-openai:8080
      DISABLE_GPT4: 1
      HIDE_BALANCE_QUERY: 1
    depends_on:
      - azure-openai
    links:
      - azure-openai
    restart: always

  anse-demo:
    image: ddiu8081/chatgpt-demo:latest
    container_name: chatgpt-demo
    restart: always
    ports:
      - 3001:3000
	environment:
	  OPENAI_API_KEY: "c1c11320c5f14e4284abd37b24fac4bf"
	  OPENAI_API_BASE_URL: http://azure-openai:8080
	  OPENAI_API_MODEL: gpt-3.5-turbo
    depends_on:
      - azure-openai
    links:
      - azure-openai
    restart: always

  chatgpt-web:
    image: chenzhaoyu94/chatgpt-web:latest # 总是使用 latest ,更新时重新 pull 该 tag 镜像即可
    ports:
      - 3002:3002
    environment:
      OPENAI_API_KEY: "c1c11320c5f14e4284abd37b24fac4bf"
      OPENAI_API_BASE_URL: http://azure-openai:8080
      OPENAI_API_MODEL: gpt-3.5-turbo
    depends_on:
      - azure-openai
    links:
      - azure-openai
    restart: always
    
  azure-openai:
    image: stulzq/azure-openai-proxy:latest
    ports:
      - 8080:8080
    environment:
      AZURE_OPENAI_ENDPOINT: "https://scw-chatgpt.openai.azure.com/"
      AZURE_OPENAI_MODEL_MAPPER: gpt-3.5-turbo=scw-gpt35
      AZURE_OPENAI_API_VER: 2023-03-15-preview
    restart: always
```



```bash
docker-compose up --detach --build
docker-compose up -d

# 更新容器
docker ps 
docker stop *
docker rm *

docker rm -f $(docker ps -aq)

docker pull yidadaa/chatgpt-next-web
docker pull stulzq/azure-openai-proxy
docker images
docker rmi *

docker-compose up --detach --build



# 停止和运行容器

docker stop *
docker start *
docker-compose down
```

```


docker run -d -p 127.0.0.1:8080:8080 --name="azure-openai-proxy" --env AZURE_OPENAI_ENDPOINT="https://scw-chatgpt.openai.azure.com/" --env AZURE_OPENAI_MODEL_MAPPER="gpt-3.5-turbo=scw-gpt35" --env AZURE_OPENAI_API_VER="2023-03-15-preview" stulzq/azure-openai-proxy:latest

docker run -d -p 3000:3000 --name=chatgpt-next-web --env OPENAI_API_KEY="c1c11320c5f14e4284abd37b24fac4bf" --env BASE_URL="http://localhost:8080" --env DISABLE_GPT4=1 --env HIDE_BALANCE_QUERY=1 yidadaa/chatgpt-next-web:latest

docker run -d -p 3001:3001 --name=chatgpt-demo --env OPENAI_API_KEY="c1c11320c5f14e4284abd37b24fac4bf" --env OPENAI_API_BASE_URL="http://localhost:8080" ddiu8081/chatgpt-demo:latest


docker run -d -p 3002:3002 --name=chatgpt-web  --env OPENAI_API_KEY="c1c11320c5f14e4284abd37b24fac4bf" --env OPENAI_API_BASE_URL="http://localhost:8080" chenzhaoyu94/chatgpt-web:latest
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
      API_URL_REDIRECT: {"https://api.openai.com/v1/chat/completions": "http://azure-openai:8080"}

```yaml
version: '3'

services:
  gpt_academic_with_latex:
    image: ghcr.io/binary-husky/gpt_academic_with_latex:master
    environment:
      API_KEY: "c1c11320c5f14e4284abd37b24fac4bf"
      AZURE_ENDPOINT: "https://scw-chatgpt.openai.azure.com/"
      AZURE_API_KEY: "c1c11320c5f14e4284abd37b24fac4bf"
      AZURE_API_VERSION: "2023-03-15-preview"
      AZURE_ENGINE: "scw-gpt35"
      LLM_MODEL: "azure-gpt35"
      AVAIL_LLM_MODELS: ["gpt-3.5-turbo", "gpt-4", "azure-gpt35"]
      LOCAL_MODEL_DEVICE: cuda
      DEFAULT_WORKER_NUM: 10
      WEB_PORT: 3001
      ADD_WAIFU: True
    network_mode: "host"

    command: >
      bash -c "python3 -u main.py"

```

# 部署 LibreChat

```bash
git clone https://github.com/danny-avila/LibreChat.git
sudo apt install docker.io && apt install docker-compose -y

cd LibreChat
cp .env.example .env
vi .env
```

```
version: "3"

services:
  # client:
  #   image: nginx-client
  #   build:
  #     context: .
  #     target: nginx-client
  #   restart: always
  #   ports:
  #     - 3000:80
  #   volumes:
  #     - /client/node_modules
  #   depends_on:
  #     - api
  api:
    container_name: LibreChat
    ports:
      - 3080:3080               # Change it to 9000:3080 to use nginx
    depends_on:
      - mongodb
    image: librechat                # Comment this & uncomment below to build from docker hub image
    build:                                   # ^------
      context: .                              # ^------
      target: node                             # ^------v
    # image: ghcr.io/danny-avila/librechat:latest # Uncomment this & comment above to build from docker hub image
    restart: always
    extra_hosts: # if you are running APIs on docker you need access to, you will need to uncomment this line and next
    - "host.docker.internal:host-gateway"
    env_file:
      - .env
    environment:
      - HOST=0.0.0.0
      - MONGO_URI=mongodb://mongodb:27017/LibreChat
      # - CHATGPT_REVERSE_PROXY=http://host.docker.internal:8080/api/conversation # if you are hosting your own chatgpt reverse proxy with docker
      # - OPENAI_REVERSE_PROXY=http://host.docker.internal:8070/v1/chat/completions # if you are hosting your own chatgpt reverse proxy with docker
      - MEILI_HOST=http://meilisearch:7700
      - MEILI_HTTP_ADDR=meilisearch:7700
    volumes:
      - /app/client/node_modules
      - ./api:/app/api
      - ./.env:/app/.env
      - ./.env.development:/app/.env.development
      - ./.env.production:/app/.env.production
      - /app/api/node_modules
      - ./images:/app/client/public/images
  mongodb:
    container_name: chat-mongodb
    ports:
      - 27018:27017
    image: mongo
    restart: always
    volumes:
      - ./data-node:/data/db
    command: mongod --noauth
  meilisearch:
    container_name: chat-meilisearch
    image: getmeili/meilisearch:v1.0
    restart: always
    ports:
      - 7700:7700
    env_file:
      - .env
    environment:
      - MEILI_HOST=http://meilisearch:7700
      - MEILI_HTTP_ADDR=meilisearch:7700
      - MEILI_NO_ANALYTICS=true
    volumes:
      - ./meili_data:/meili_data


docker-compose up --detach --build
```
