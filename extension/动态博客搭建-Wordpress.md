---
title: "{{动态博客搭建-Wordpress_LEMP}}"
description: ""
author: ""
tags: []
categories: ""
keywords:  ["wordpress", "blog", "LEMP",  "Ubuntu 20.04", "建站"]
draft: true
layout: ""
date: 2023-03-03 13:06:08
lastmod: 2023-03-03 22:29:17
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
> LEMP 代表由 **L**inux 操作系统,  Nginx (发音像“**E**ngine-X”) Web 服务器,  **M**ySQL 数据库和 **P**HP 脚本语言构成的软件组合, 可用于提供用于编写动态网页和 Web 应用程序的基础环境. 

1. 安装 Nginx Web 服务器

为了向网站访问者显示网页, 这里采用高性能 Web 服务器 Nginx,  通过包管理器 `apt` 可以获取此软件.

```
sudo apt update
sudo apt install nginx
```

> [!tip] 提示
> 第一次进行会话, 从更新服务器的包索引开始.


安装过程会出现确认提示时, 输入 `Y` 以确认要安装 Nginx. 安装完成后,  Nginx Web 服务器将自行处于活动状态并在服务器上运行.

如果启用了防火墙,  需要开启服务器中 Nginx 程序与外部连接的 80 和 443 端口,  详细查看指南: [常用防火墙设置](../Research/计算机/{8}_linux.md#常用防火墙设置) 或 [云服务器安全组](../Research/计算机/{8}_linux.md#华为云服务器安全组)


测试 Nginx Web 服务器是否启用

```
curl -4 icanhazip.com
http://[服务器 IP 或域名]
```
现在已经启动并运行了 Web 服务器,  并且通过 http 协议简单的访问了此 Web 服务器. 

2. 安装 MySQL

为了更好的存储和管理当前 Web 站点的数据,  而 MySQL 是 PHP 环境中流行的数据库管理系统.

同样,  先通过包管理器 `apt` 获取此软件.

```
sudo apt install mysql-server
```
安装过程会出现确认提示时, 输入 `Y` 以确认要安装 Mysql. 安装完成后,  Mysql 服务器将自行处于活动状态并在服务器上运行.

安装完成后,  建议运行 MySQL 预安装的一个安全脚本,  此脚本会删除一些不安全的默认设置并锁定对数据库系统的访问. 通过运行以下命令可以启动此交互式脚本:

```
sudo mysql_secure_installation
```

之后,  首先会询问是否安装密码验证插件,  此插件安装后,  将会根据你之后提供的密码难度等级,  判断设置的数据库用户密码是否有效,  无效则会重新让你设置. 回答 `y|Y` ,  同意安装即可(或者回答其他任何内容,  都是不启用此插件). 无论是否选择安装插件,  都不会影响后续操作的进行.

如果回答了 `y|Y` , 系统会要求选择密码难度验证级别,  根据需要选择即可,  建议是 `1` (中等难度). 

- `0/LOW` :只检查密码长度; 
- `1/MEDIUM` : 检查长度、数字、大小写、特殊字符.
- `2/STRONG` : 检查长度、数字、大小写、特殊字符、常见密码字典文件.

  
接下来会要求确认并设置 MySQL 数据库的 root 用户的密码. 数据库的 root 用户仅对 MySQL 数据库系统具有完全管理权限,  因此不同于系统的 root 用户. 

> [!bug] 安装失败
> 因为 MySQL 数据库 root 用户的默认身份验证方法免除了使用密码的方式,  因此如果想要为 MySQL 数据库的 root 用户设置密码,  可能会出错. 
> 
> 如果在这里遇到了如下错误提示:  
> ```
> Failed! Error: SET PASSWORD has no significance for user 'root'@'localhost' as the authentication method used doesn't store authentication data in the MySQL server. Please consider using ALTER USER instead if you want to change authentication parameters.
> ```
> 可以通过指令 `sudo mysql` 进入数据库命令行,  执行以下指令来解决. 注意,  这里的密码可以任意设置,  后面还需要更改. 
> ```
> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
> ``` 
> 最后通过 `quit` 指令退出当前命令行,  然后重新执行 `sudo mysql_secure_installation ` 指令,  输入刚设置的密码,  重复以上操作,  即可解决问题.


如果启用了密码验证,  你将看到刚刚输入的 root 用户的密码的密码强度,  以及对是否要继续使用该密码的询问. 如果对当前密码满意,  输入 `Y` 表示确认,  否则会重新请你输入新密码.

对于剩下的操作,  建议在每次出现提示时按 `Y` 并按 `ENTER` 键,  确认执行. 这将删除一些匿名用户和测试用的数据库,  禁用远程登录数据库 root 用户的方式, 并使得 MySQL 重新加载新定义的规则. 当然,  也可以根据需要保留一些操作,  不过要注意,  以上的操作都是为了让你的数据库更安全!

安装和配置完成后, 可以通过键入以下内容测试是否可以通过登录到 MySQL 控制台: 

```bash
sudo mysql
```

请注意,  因为 MySQL 数据库 root 用户的默认身份验证方法免除了使用密码的方式,  因此,  正常情况下,  即使你在运行 mysql_secure_installation 脚本时,  为 root 用户定义了一个密码,  但也无需以提供密码的方式登录 root 用户. 也就是上述的简单连接指令: `sudo mysql` .

但是如果安装过程中,  遇到了上面展示的错误,  并使用了相同的问题解决办法,  这会使得 MySQL 数据库 root 用户的默认身份验证方法更换为使用密码登录的方式. 因此在连接数据库时,  需要指定用户,  并使用其密码登录. 即: 
```bash
sudo mysql -u root -p
```

连接成功后,  会进入数据库的命令行模式.

如果想要重新开启默认身份验证方法,  可以在进入数据库的命令行模式以后,  使用以下指令还原:

```mysql
select user,  host,  plugin from mysql.user;
update user set plugin="auth_socket" where user='root';
```

> [!info] MySQL 默认无密码身份验证
> 管理 MySQL 用户的默认身份验证方法是 "unix_socket" 而不是"密码". 可能 "无密码" 乍一听起来,  觉得不安全,  但其实它会使得数据库服务器更加安全. 因为 "unix_socket" 验证方式,  唯一只允许具有 sudo 权限的系统用户使用 MySQL root 用户身份登录数据库. 这意味着无法使用 PHP 应用程序等,  通过 MySQL root 用户,  进行远程连接和管理数据库. 为 MySQL root 帐户设置密码可以作为一种额外的保护措施,  以防止默认身份验证方法被不小心从 "unix_socket" 更改为"密码"验证方式. 为了提高安全性,  最好为每个数据库设置具有较少扩展权限的专用用户帐户,  特别是如果计划在服务器上托管多个数据库.

您的 MySQL 数据库现在已安装并受到保护. 接下来继续安装 PHP, 这是 LEMP 软件组中的最后一个组件了.

3. 安装 PHP

到目前为止,  已经安装了 Nginx 来服务内容,  安装了 MySQL 来存储和管理数据. 现在, 通过安装 PHP 来编写代码, 并为 web 服务器生成动态内容. 虽然 Apache 在每个请求中嵌入了 PHP 解释器, 但 Nginx 仍然需要外部程序来处理 PHP , 并充当 PHP 解释器本身和 web 服务器之间的桥梁. 这可以使得大多数基于 PHP 的网站获得更好的性能, 不过多了点额外的配置. 

1. 安装 `php-fpm` , “php fastCGI 进程管理器”, 并告诉 Nginx 将 php 请求传递给该软件进行处理. 
2. 安装 `php-mysql` , 一个允许 php 与基于 mysql 数据库通信的 php 模块. 核心 PHP 包将作为依赖项自动安装. 

```bash
sudo apt install php-fpm php-mysql
```
现在已经安装了 PHP 组件. 接下来, 需要配置 Nginx 并使用它们。


4. 配置 Nginx 以使用 PHP 组件

当使用 Nginx Web 服务器时，我们可以创建服务器 block（类似于 Apache 中的虚拟主机）来封装配置细节，并在单个服务器上托管多个站点。在本指南中，我们以域名 `your_domain` 作为示例。在 Ubuntu 20.04 上, Nginx 默认启用了一个服务器 block, 并默认配置为从 `/var/www/html` 目录中提供服务. 虽然这对于单一站点很有效，但如果您在此服务器托管了多个站点，则可能会变得很难管理。因此我们将在 `/var/www` 中为 `your_domain` 网站创建一个额外的目录结构，只有当客户端请求与此站点不匹配时，才会使用 `/var/www/html` 作为默认站点目录。

首先为当前站点创建根 web 目录，如下所示: 

```
sudo mkdir /var/www/blog
```

接下来，使用 `$USER` 环境变量引用当前系统用户, 然后分配目录的所有权到当前用户:

```
sudo chown -R $USER:$USER /var/www/your_domain
```

然后，使用文本编辑器在 Nginx 的 `sites available` 目录中新建和打开一个配置文件。在这里使用的 “nano” 编辑器：

```
sudo nano /etc/nginx/sites-available/your_domain
```

这将创建一个新的空文件, 请为此配置文件粘贴以下预设配置参数:
```nginx
server {
    listen 80;
    server_name your_domain blog.your_domain;
    root /var/www/blog;
    index index.html index.htm index.php;
    location / {
        try_files $uri $uri/ =404;
    }
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
     }
    location ~ /\.ht {
        deny all;
    }
}
```
以下是上述参数的作用:

- `listen` : 定义 Nginx 服务监听的服务器端口。默认侦听端口 80，即 HTTP 的默认端口。

- `root` : 定义存储此网站提供的文件内容的站点根目录路径。

- `index` : 定义 Nginx 提供服务时, 此网站的索引文件的优先检测顺序。通常的做法是列出比 index.php 文件优先级更高的 index.html 文件，以便在 php 应用程序中快速设置维护登录页。

- `server_name` : 定义此服务器 block 响应的域名和/或 IP 地址。

- `location/` : 此参数块包含 try_files 指令，用于检查是否存在与 URI 请求匹配的文件或目录. 如果 Nginx 找不到合适的资源，它将返回 404 错误。

- `location~\.php$` : 此参数块通过将 Nginx 指向 `fastcgi-hp.conf` 程序配置文件和 `php7.4-fpm.sock` 文件来处理实际的 php 请求，该文件声明了与 php-fpm 关联的 socket 。

- `location~/\.ht` : 最后一个参数块处理 `.htaccess` 文件，Nginx 不处理这些文件。通过添加 deny all 指令，如果任何 `.htaccess` 文件恰好进入站点根目录，则不会向访问者提供这些文件。

完成编辑后，保存并关闭文件。如果使用的是 “nano”，则可以通过键入 `CTRL+X` ，然后键入 `y` 和 `ENTER` 进行确认.


通过从 Nginx 的  `sites-enabled`  目录链接到已创建的配置文件来激活配置: 

```
sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled/
```

然后，取消默认配置文件与`sites-enabled`目录的链接：

```
sudo unlink /etc/nginx/sites-enabled/default
```

> [!tip] 提示
> 如果需要恢复默认配置，可以通过重新创建符号链接来恢复，如下所示：
> ```
>  sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/ 
> ```

这将告诉 Nginx 下次重新加载时使用该配置。您可以键入以下命令来测试配置的语法错误：

```
sudo nginx -t
```

如果报告了任何错误，请返回配置文件以改正其内容，然后再继续。

准备就绪后，重新加载 Nginx 以应用更改：

```
sudo systemctl reload nginx
```

您的新网站现在处于活动状态，但 web 根目录`/var/www/blog`仍然为空。在该位置创建一个`index.html`文件，以便我们可以测试您的新服务器块是否按预期工作: 

```
nano /var/www/blog/index.html
```

网站页面里面包含以下内容
```
<html>
	<head>
		<title>your_domain website</title>
	</head>
	<body>
		<h1>Hello World!</h1>
		<p>This is the landing page of <strong>your_domain</strong>.</p>
	</body>
</html>
```

Now go to your browser and ac


> [!Quote] 论文信息
>1. [How to Install WordPress with LEMP on Ubuntu 20.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lemp-on-ubuntu-20-04)
>2. [基于Ubuntu20.4搭建WordPress个人博客-CSDN博客](https://blog.csdn.net/TM2022/article/details/124386462)
