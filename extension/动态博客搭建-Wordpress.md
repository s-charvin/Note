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
lastmod: 2023-03-03 20:08:40
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

之后, 首先会询问是否安装密码验证插件, 此插件安装后, 将会根据你之后提供的密码难度等级, 判断设置的数据库用户密码是否有效, 无效则会重新让你设置. 回答 `y|Y` , 同意安装即可(或者回答其他任何内容, 都是不启用此插件). 无论是否选择安装插件, 都不会影响后续操作的进行.

如果回答了 `y|Y` ，系统会要求选择密码难度验证级别, 根据需要选择即可, 建议是 `1` (中等难度). 

- `0/LOW` :只检查密码长度; 
- `1/MEDIUM` : 检查长度、数字、大小写、特殊字符.
- `2/STRONG` : 检查长度、数字、大小写、特殊字符、常见密码字典文件.

  
接下来会要求确认并设置 MySQL 数据库的 root 用户的密码. 数据库的 root 用户仅对 MySQL 数据库系统具有完全管理权限, 因此不同于系统的 root 用户. 

> [!bug] 安装失败
> 因为 MySQL 数据库 root 用户的默认身份验证方法免除了使用密码的方式, 因此如果想要为 MySQL 数据库的 root 用户设置密码, 可能会出错. 
> 
> 如果在这里遇到了如下错误提示:  `Failed! Error: SET PASSWORD has no significance for user 'root'@'localhost' as the authentication method used doesn't store authentication data in the MySQL server. Please consider using ALTER USER instead if you want to change authentication parameters.`
> 
> 可以通过指令 `sudo mysql` 进入数据库命令行, 执行指令 `ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket BY 'your_password';` 来解决. 注意, 这里的密码可以任意设置, 后面还需要更改. 
> 
> 通过 `quit` 指令退出当前命令行, 然后重新执行 `sudo mysql_secure_installation ` 指令, 输入刚设置的密码, 重复以上操作, 即可解决问题.


如果启用了密码验证, 你将看到刚刚输入的 root 用户的密码的密码强度, 以及对是否要继续使用该密码的询问. 如果对当前密码满意, 输入 `Y` 表示确认, 否则会重新请你输入新密码.

对于剩下的操作, 建议在每次出现提示时按 `Y` 并按 `ENTER` 键, 确认执行. 这将删除一些匿名用户和测试用的数据库, 禁用远程登录数据库 root 用户的方式，并使得 MySQL 重新加载新定义的规则. 当然, 也可以根据需要保留一些操作, 不过要注意, 以上的操作都是为了让你的数据库更安全!

安装和配置完成后，可以通过键入以下内容测试是否可以通过登录到 MySQL 控制台: 

```bash
sudo mysql
```


请注意, 因为 MySQL 数据库 root 用户的默认身份验证方法免除了使用密码的方式, 因此, 正常情况下, 即使你在运行 mysql_secure_installation 脚本时, 为 root 用户定义了一个密码, 但也无需以提供密码的方式登录 root 用户. 也就是上述的简单连接指令: `sudo mysql` .

但是如果安装过程中, 遇到了上面展示的错误, 并使用了相同的wen'ti'jie'jue
```bash
sudo mysql -u root -p
```



这里建议不通过密码的方式登录 root 用户, 因为这会让后面操作出现 bug, 同时也不会使你更安全. 当然, 设置一个高强度密码也是很好的安全保护措施, 因此如果选择设置密码, 可以查看下述可能遇到的安装失败的解决方案.





这是因为管理 MySQL 用户的默认身份验证方法是 unix_socket 而不是密码。 尽管一开始这看起来像是一个安全问题，但它使数据库服务器更加安全，因为唯一允许以 MySQL 根用户身份登录的用户是具有 sudo 权限的系统用户，这些用户从控制台连接或通过使用 相同的特权。 实际上，这意味着您将无法使用管理数据库根用户从您的 PHP 应用程序进行连接。 为根 MySQL 帐户设置密码作为一种保护措施，以防默认身份验证方法从 unix_socket 更改为密码。为了提高安全性，最好为每个数据库设置具有较少扩展权限的专用用户帐户，特别是如果您计划在服务器上托管多个数据库。

> [!Quote] 论文信息
>1. [How to Install WordPress with LEMP on Ubuntu 20.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lemp-on-ubuntu-20-04)
>2. [基于Ubuntu20.4搭建WordPress个人博客-CSDN博客](https://blog.csdn.net/TM2022/article/details/124386462)
