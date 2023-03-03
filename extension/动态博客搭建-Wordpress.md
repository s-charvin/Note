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
lastmod: 2023-03-03 15:39:08
---


> [!info] 
> 1. 服务器: 华为云 HECS (1vCPUs | 2GiB | 带宽 1 Mbit/s)
> 2. 操作系统: Ubuntu 20.04 64 位

## 软件环境配置

1. 登录(没有就去[创建](../Research/计算机/{8}_linux.md#初始服务器设置))日常使用用户
```bash
ssh charvin@[服务器 IP]
# 示例: ssh charvin@111.222.066
```

2. 安装 LEMP 软件环境

> [!info] LEMP
> LEMP 代表由 **L**inux 操作系统, Nginx (发音像“**E**ngine-X”) Web 服务器, **M**ySQL 数据库和 **P**HP 脚本语言构成的软件组合，可用于提供用于编写动态网页和 Web 应用程序的基础环境。

1. 安装 Nginx Web 服务器

为了向网站访问者显示网页，这里采用高性能 Web 服务器 Nginx, 通过包管理器 `apt` 可以获取此软件.

```
sudo apt update
sudo apt install nginx
```

> [!tip] 提示
> 第一次进行会话，从更新服务器的包索引开始.


安装过程会出现确认提示时，输入 `Y` 以确认要安装 Nginx. 安装完成后, Nginx Web 服务器将自行处于活动状态并在服务器上运行.


> [!Quote] 论文信息
>1. [How to Install WordPress with LEMP on Ubuntu 20.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lemp-on-ubuntu-20-04)
>2. [基于Ubuntu20.4搭建WordPress个人博客-CSDN博客](https://blog.csdn.net/TM2022/article/details/124386462)
