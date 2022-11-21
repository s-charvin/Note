---
title: "aliyundrive"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-11-21 17:34:06
lastmod: 2022-11-21 17:34:29
---

docker run -d --name=aliyundrive-webdav --restart=unless-stopped -p 7564:8080 -v /etc/aliyundrive-webdav/:/etc/aliyundrive-webdav/ -e REFRESH_TOKEN='' -e WEBDAV_AUTH_USER=admin -e WEBDAV_AUTH_PASSWORD="" messense/aliyundrive-webdav:1.10
