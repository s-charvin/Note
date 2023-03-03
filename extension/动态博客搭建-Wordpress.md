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
lastmod: 2023-03-03 19:28:39
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

如果启用了防火墙, 需要开启服务器中 Nginx 程序与外部连接的 80 和 443 端口, 详细查看指南: [常用防火墙设置](../Research/计算机/{8}_linux.md#常用防火墙设置) 或 [云服务器安全组](../Research/计算机/{8}_linux.md#华为云服务器安全组)


测试 Nginx Web 服务器是否启用

```
curl -4 icanhazip.com
http://[服务器 IP 或域名]
```
现在已经启动并运行了 Web 服务器, 并且通过 http 协议简单的访问了此 Web 服务器. 

2. 安装 MySQL

为了更好的存储和管理当前 Web 站点的数据, 而 MySQL 是 PHP 环境中流行的数据库管理系统.

同样, 先通过包管理器 `apt` 获取此软件.

```
sudo apt install mysql-server
```
安装过程会出现确认提示时，输入 `Y` 以确认要安装 Mysql. 安装完成后, Mysql 服务器将自行处于活动状态并在服务器上运行.

安装完成后, 建议运行 MySQL 预安装的一个安全脚本, 此脚本会删除一些不安全的默认设置并锁定对数据库系统的访问. 通过运行以下命令可以启动此交互式脚本:

```
sudo mysql_secure_installation
```

之后, 首先会询问是否安装密码验证插件, 此插件安装后, 将会根据你之后提供的密码难度等级, 判断密码是否有效, 无效则会重新让你设置. 回答 `y|Y` , 同意安装即可(或者其他任何内容都可以在不启用此插件的情况下继续执行后续操作).


如果回答了 `y|Y` ，系统会要求选择密码难度验证级别. `0/LOW`  只检查密码长度。
`1/MEDIUM：检查长度、数字、大小写、特殊字符。`  
`2/STRONG：检查长度、数字、大小写、特殊字符、字典文件。`

请记住，如果您输入最强级别，则在尝试设置任何不包含数字，大写和小写字母和特殊字符或基于常见字典单词的密码时，您将收到错误。 `2`

> [!Quote] 论文信息
>1. [How to Install WordPress with LEMP on Ubuntu 20.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lemp-on-ubuntu-20-04)
>2. [基于Ubuntu20.4搭建WordPress个人博客-CSDN博客](https://blog.csdn.net/TM2022/article/details/124386462)
