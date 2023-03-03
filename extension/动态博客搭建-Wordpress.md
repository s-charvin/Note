---
title: "{{动态博客搭建-Wordpress_LEMP}}"
description: ""
author: ""
tags: []
categories: ""
keywords:  ["wordpress","blog","LEMP", "Ubuntu 20.04","建站"]
draft: true
layout: ""
date: 2023-03-03 13:06:08
lastmod: 2023-03-03 13:31:19
---


> [!info] 
> 1. 服务器: 华为云 HECS (1vCPUs | 2GiB | 带宽 1 Mbit/s)
> 2. 操作系统: Ubuntu 20.04 64 位

## 软件环境配置

1. 登录(没有就去 [[0. 情感语音方向研究.assets/image-20210912123829744.png#]])日常使用用户

```bash
adduser charvin
```
```bash
# 记得更换下载源, 不然有时下载速度会很慢
sudo apt-get update && apt-get upgrade
```




> [!Quote] 论文信息
>1. [How to Install WordPress with LEMP on Ubuntu 20.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lemp-on-ubuntu-20-04)
>2. [基于Ubuntu20.4搭建WordPress个人博客-CSDN博客](https://blog.csdn.net/TM2022/article/details/124386462)
