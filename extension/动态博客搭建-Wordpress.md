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
lastmod: 2023-03-04 13:55:07
---


> [!info] 
> 1. 服务器: 华为云 HECS (1vCPUs | 2GiB | 带宽 1 Mbit/s)
> 2. 操作系统: Ubuntu 20.04 64 位

## 软件环境配置

### 1. 登录服务器的(没有就去[创建](../Research/计算机/{8}_linux.md#初始服务器设置))日常使用用户

```bash
ssh charvin@[服务器 IP]
# 示例: ssh charvin@111.222.066
```

### 2. 安装 LEMP 软件环境

> [!info] LEMP
> LEMP 代表由 **L**inux 操作系统,  Nginx (发音像“**E**ngine-X”) Web 服务器,  **M**ySQL 数据库和 **P**HP 脚本语言构成的软件组合, 可用于提供用于编写动态网页和 Web 应用程序的基础环境. 

#### 1. 安装 Nginx Web 服务器

为了向网站访问者显示网页, 这里采用高性能 Web 服务器 Nginx,  通过包管理器 `apt` 可以获取此软件.

```bash
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

#### 2. 安装 MySQL

为了更好的存储和管理当前 Web 站点的数据,  而 MySQL 是 PHP 环境中流行的数据库管理系统.

同样,  先通过包管理器 `apt` 获取此软件.

```bash
sudo apt install mysql-server
```
安装过程会出现确认提示时, 输入 `Y` 以确认要安装 Mysql. 安装完成后,  Mysql 服务器将自行处于活动状态并在服务器上运行.

安装完成后,  建议运行 MySQL 预安装的一个安全脚本, 此脚本会删除一些不安全的默认设置并锁定对数据库系统的访问. 通过运行以下命令可以启动此交互式脚本:

```bash
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
> ```mysql
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

如果想要重新开启默认身份验证方法, 可以在进入数据库的命令行模式以后,  使用以下指令还原:

```mysql
select user,  host,  plugin from mysql.user;
USE database_name;
update user set plugin="auth_socket" where user='root';
```

> [!info] MySQL 默认无密码身份验证
> 管理 MySQL 用户的默认身份验证方法是 "unix_socket" 而不是"密码". 可能 "无密码" 乍一听起来,  觉得不安全,  但其实它会使得数据库服务器更加安全. 因为 "unix_socket" 验证方式,  唯一只允许具有 sudo 权限的系统用户使用 MySQL root 用户身份登录数据库. 这意味着无法使用 PHP 应用程序等,  通过 MySQL root 用户,  进行远程连接和管理数据库. 为 MySQL root 帐户设置密码可以作为一种额外的保护措施,  以防止默认身份验证方法被不小心从 "unix_socket" 更改为"密码"验证方式. 为了提高安全性,  最好为每个数据库设置具有较少扩展权限的专用用户帐户,  特别是如果计划在服务器上托管多个数据库.

您的 MySQL 数据库现在已安装并受到保护. 接下来继续安装 PHP, 这是 LEMP 软件组中的最后一个组件了.

#### 3. 安装 PHP

到目前为止,  已经安装了 Nginx 来服务内容,  安装了 MySQL 来存储和管理数据. 现在, 通过安装 PHP 来编写代码, 并为 web 服务器生成动态内容. 虽然 Apache 在每个请求中嵌入了 PHP 解释器, 但 Nginx 仍然需要外部程序来处理 PHP , 并充当 PHP 解释器本身和 web 服务器之间的桥梁. 这可以使得大多数基于 PHP 的网站获得更好的性能, 不过多了点额外的配置. 

1. 安装 `php-fpm` , “php fastCGI 进程管理器”, 并告诉 Nginx 将 php 请求传递给该软件进行处理. 
2. 安装 `php-mysql` , 一个允许 php 与基于 mysql 数据库通信的 php 模块. 核心 PHP 包将作为依赖项自动安装. 

```bash
sudo apt install php-fpm php-mysql
```
现在已经安装了 PHP 组件. 接下来, 需要配置 Nginx 并使用它们。

#### 4. 配置 Nginx 以使用 PHP 组件

当使用 Nginx Web 服务器时，我们可以创建服务器 block（类似于 Apache 中的虚拟主机）来封装配置细节，并在单个服务器上托管多个站点。在本指南中，我们以域名 `blog` 作为示例。在 Ubuntu 20.04 上, Nginx 默认启用了一个服务器 block, 并默认配置为从 `/var/www/html` 目录中提供服务. 虽然这对于单一站点很有效，但如果您在此服务器托管了多个站点，则可能会变得很难管理。因此我们将在 `/var/www` 中为 `blog` 网站创建一个额外的目录结构，只有当客户端请求与此站点不匹配时，才会使用 `/var/www/html` 作为默认站点目录。

首先为当前站点创建根 web 目录，如下所示: 

```bash
sudo mkdir /var/www/blog
```

接下来，使用 `$USER` 环境变量引用当前系统用户, 然后分配目录的所有权到当前用户:

```bash
sudo chown -R $USER:$USER /var/www/blog
```

然后，使用文本编辑器在 Nginx 的 `sites available` 目录中新建和打开一个配置文件。在这里使用的 “nano” 编辑器：

```bash
sudo nano /etc/nginx/sites-available/blog
```

这将创建一个新的空文件, 请为此配置文件粘贴以下预设配置参数:
```nginx
server {
    listen 80;
    server_name 124.70.208.35:80 124.70.208.35:443;
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

```bash
sudo ln -s /etc/nginx/sites-available/wordpress /etc/nginx/sites-enabled/
```

然后，取消默认配置文件与`sites-enabled`目录的链接：

```bash
sudo unlink /etc/nginx/sites-enabled/default
```

> [!tip] 提示
> 如果需要恢复默认配置，可以通过重新创建符号链接来恢复，如下所示：
> ```bash
>  sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/ 
> ```

这将告诉 Nginx 下次重新加载时使用该配置。您可以键入以下命令来测试配置的语法错误：

```bash
sudo nginx -t
```

如果报告了任何错误，请返回配置文件以改正其内容，然后再继续。

准备就绪后，重新加载 Nginx 以应用更改：

```bash
sudo systemctl reload nginx
```

您的新网站现在处于活动状态，但 web 根目录`/var/www/blog`仍然为空。在该位置创建一个`index.html`文件，以便我们可以测试您的新服务器块是否按预期工作: 

```bash
nano /var/www/blog/index.html
```

网站页面里面包含以下内容
```html
<html>
	<head>
		<title>blog website</title>
	</head>
	<body>
		<h1>Hello World!</h1>
		<p>This is the landing page of <strong>blog</strong>.</p>
	</body>
</html>
```
现在转到浏览器并访问服务器的域名或 IP 地址, 就可以看到效果了.


到此, LEMP 软件组现已完全配置完成。

#### 5. 使用 Nginx 测试 PHP

您的 LEMP 堆栈现在应该已完全设置。 您可以测试它以验证 Nginx 是否可以正确地将 `.php` 文件交给您的 PHP 处理器。


您可以通过在文档根目录中创建一个测试 PHP 文件来完成此操作。 在文本编辑器的文档根目录中打开一个名为 `info.php` 的新文件：

```bash
nano /var/www/blog/info.php
```

将以下行键入或粘贴到新文件中。 这是将返回有关您的服务器的信息的有效 PHP 代码：

```php
<?php
phpinfo();
```

完成后，通过键入 `CTRL` + `X` 保存并关闭文件，然后键入 `y` 和 `ENTER` 进行确认.

您现在可以通过访问您在 Nginx 配置文件中设置的域名或公共 IP 地址, 然后访问 `/info.php` ，在网络浏览器中访问此页面: 

```bash
http://[服务器 IP 或域名]/info.php
```

您将看到一个网页，其中包含有关您的服务器的详细信息.

通过该页面检查了有关您的 PHP 服务器的相关信息后，最好删除您创建的文件，因为它包含有关您的 PHP 环境和 Ubuntu 服务器的敏感信息。 您可以使用 `rm` 删除该文件：

```bash
sudo rm /var/www/blog/info.php
```



如果以后需要，您可以随时重新生成此文件。

#### 6. 从 PHP 测试数据库连接（可选）

如果您想测试 PHP 是否能够连接到 MySQL 并执行数据库查询，您可以创建一个包含虚拟数据的测试表并从 PHP 脚本查询其内容。 在我们这样做之前，我们需要创建一个测试数据库和一个正确配置的新 MySQL 用户来访问它。

At the time of this writing, the native MySQL PHP library `mysqlnd` [doesn’t support](https://www.php.net/manual/en/ref.pdo-mysql.php) `caching_sha2_authentication`, the default authentication method for MySQL 8. We’ll need to create a new user with the `mysql_native_password` authentication method in order to be able to connect to the MySQL database from PHP.

We’ll create a database named **example_database** and a user named **example_user**, but you can replace these names with different values.

First, connect to the MySQL console using the **root** account:

```bash
sudo mysql
```



To create a new database, run the following command from your MySQL console:

```mysql
CREATE DATABASE example_database;
```



Now you can create a new user and grant them full privileges on the custom database you’ve just created.

The following command creates a new user named `example_user`, using `mysql_native_password` as default authentication method. We’re defining this user’s password as `password`, but you should replace this value with a secure password of your own choosing.

```mysql
CREATE USER 'example_user'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
```



Now we need to give this user permission over the `example_database` database:

```mysql
GRANT ALL ON example_database.* TO 'example_user'@'%';
```



This will give the **example_user** user full privileges over the **example_database** database, while preventing this user from creating or modifying other databases on your server.

Now exit the MySQL shell with:

```mysql
exit
```



You can test if the new user has the proper permissions by logging in to the MySQL console again, this time using the custom user credentials:

```bash
mysql -u example_user -p
```



Notice the `-p` flag in this command, which will prompt you for the password used when creating the **example_user** user. After logging in to the MySQL console, confirm that you have access to the **example_database** database:

```mysql
SHOW DATABASES;
```



This will give you the following output:

```
Output+--------------------+
| Database           |
+--------------------+
| example_database   |
| information_schema |
+--------------------+
2 rows in set (0.000 sec)
```

Next, we’ll create a test table named **todo_list**. From the MySQL console, run the following statement:

```mysql
CREATE TABLE example_database.todo_list (
	item_id INT AUTO_INCREMENT,
	content VARCHAR(255),
	PRIMARY KEY(item_id)
);
```



Insert a few rows of content in the test table. You might want to repeat the next command a few times, using different values:

```mysql
INSERT INTO example_database.todo_list (content) VALUES ("My first important item");
```



To confirm that the data was successfully saved to your table, run:

```mysql
SELECT * FROM example_database.todo_list;
```



You’ll see the following output:

```
Output+---------+--------------------------+
| item_id | content                  |
+---------+--------------------------+
|       1 | My first important item  |
|       2 | My second important item |
|       3 | My third important item  |
|       4 | and this one more thing  |
+---------+--------------------------+
4 rows in set (0.000 sec)

```

After confirming that you have valid data in your test table, you can exit the MySQL console:

```mysql
exit
```



Now you can create the PHP script that will connect to MySQL and query for your content. Create a new PHP file in your custom web root directory using your preferred editor. We’ll use `nano` for that:

```bash
nano /var/www/your_domain/todo_list.php
```



The following PHP script connects to the MySQL database and queries for the content of the **todo_list** table, exhibiting the results in a list. If there’s a problem with the database connection, it will throw an exception.  this content into your `todo_list.php` script:
```php
<?php
$user = "example_user";
$password = "password";
$database = "example_database";
$table = "todo_list";

try {
  $db = new PDO("mysql:host=localhost;dbname=$database", $user, $password);
  echo "<h2>TODO</h2><ol>"; 
  foreach($db->query("SELECT content FROM $table") as $row) {
    echo "<li>" . $row['content'] . "</li>";
  }
  echo "</ol>";
} catch (PDOException $e) {
    print "Error!: " . $e->getMessage() . "<br/>";
    die();
}
```



Save and close the file when you’re done editing.

You can now access this page in your web browser by visiting the domain name or public IP address configured for your website, followed by `/todo_list.php`:

```
http://server_domain_or_IP/todo_list.php
```

You should see a page like this, showing the content you’ve inserted in your test table:

### 3. 为 WordPress 创建 MySQL 数据库和用户

WordPress 使用 MySQL 来管理和存储站点和用户信息。虽然您已经安装了 MySQL，但让我们创建一个数据库和一个用户供 WordPress 使用。

首先，登录到 MySQL root（管理）帐户。如果 MySQL 配置为使用 `auth_socket` 身份验证插件（默认），您可以使用以下命令登录 MySQL 管理帐户 `sudo` ：

```bash
sudo mysql
```

如果您已将身份验证方法更改为使用 MySQL root 帐户的密码，请改用以下命令：

```bash
mysql -u root -p
```

系统将提示您输入为 MySQL root 帐户设置的密码。

登录后，创建一个 WordPress 可以控制的单独数据库。您可以随意调用它，但我们将使用 `wordpress` 在本指南中使用它以保持简单。您可以通过输入以下内容为 WordPress 创建数据库：

```mysql
CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
```

> [!tip] 提示
> 每个 MySQL 语句必须以分号 ( `;` ) 结尾。如果遇到错误，请检查以确保分号存在。

接下来，让我们创建一个单独的 MySQL 用户帐户，我们将专门使用它来操作我们的新数据库。从管理和安全的角度来看，创建单一用途的数据库和帐户是一个好主意。我们将在本指南中使用该名称 `wordpressuser` - 如果您愿意，可以随意更改。


在以下命令中，您将创建一个帐户、设置密码并授予对您创建的数据库的访问权限。记得在这里选择一个强密码：

```mysql
CREATE USER '[自定义用户名]'@'localhost' IDENTIFIED BY '[自定义密码]';
# 示例: CREATE USER 'wordpressuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON wordpress.* TO '[用户名]'@'localhost';
# 示例: GRANT ALL ON wordpress.* TO 'wordpressuser'@'localhost';
```

您现在拥有一个数据库和用户帐户，每个都是专门为 WordPress 制作的。

数据库任务完成后，让我们通过键入以下命令退出 MySQL：

```mysql
EXIT;
```

MySQL 会话将退出，返回到常规 Linux shell。

### 4. 安装额外的 PHP 扩展

在设置 LEMP 堆栈时，需要极少的扩展集才能使 PHP 与 MySQL 进行通信。WordPress 及其许多插件利用了额外的 PHP 扩展，您将在本教程中使用更多扩展。

让我们通过键入以下命令下载并安装一些最流行的 PHP 扩展以用于 WordPress：

```bash
sudo apt update
```

```bash
sudo apt install php-curl php-gd php-intl php-mbstring php-soap php-xml php-xmlrpc php-zip
```

> [!tip] 提示
> 注意：每个 WordPress 插件都有自己的一套要求。有些可能需要安装额外的 PHP 扩展包。检查您的插件文档以发现其 PHP 要求。如果它们可用，则可以 `apt` 按照上面的说明安装它们。

完成扩展安装后，重新启动 PHP-FPM 进程，以便正在运行的 PHP 处理器可以利用新安装的功能：

```bash
sudo systemctl restart php8.1-fpm
```

您现在已经在服务器上安装了所有需要的 PHP 扩展。

### 5. 为 WordPress 配置 Nginx

接下来，让我们对我们的 Nginx 服务器块文件进行一些调整。根据先决条件教程，您应该在 `/etc/nginx/sites-available/` 为响应服务器域名或 IP 地址并受 TLS/SSL 证书保护的目录中配置站点配置文件。我们将在此处用作示例 `/etc/nginx/sites-available/wordpress`，但您应该在适当的地方将路径替换为您的配置文件。 

此外，我们将在本指南中用作 `/var/www/wordpress` 为 WordPress 安装的根目录。同样，您应该使用您自己的配置中指定的 Web 根目录。

> [!tip] 提示
> 注意：您可能正在使用 `/etc/nginx/sites-available/default` 默认配置（ `/var/www/html` 作为您的网络根目录）。如果您只打算在此服务器上托管一个网站，则可以使用它。如果没有，最好将必要的配置拆分成逻辑块，每个站点一个文件夹。

使用`sudo`权限打开您站点的服务器块文件以开始：

```
sudo nano /etc/nginx/sites-available/wordpress
```

在主`server`块中，让我们添加几个`location`块。

`/favicon.ico`首先为对和 的请求创建完全匹配的位置块`/robots.txt`，您不想记录对这两个请求的请求。

使用正则表达式位置来匹配对静态文件的任何请求。我们将再次关闭这些请求的日志记录，并将它们标记为高度可缓存的，因为这些通常是昂贵的服务资源。您可以调整此静态文件列表以包含您的站点可能使用的任何其他文件扩展名.

在现有 `location /` 块内，让我们调整 `try_files` 列表。通过在行前加上井号 ( ) 来注释掉默认设置 `#` ，然后添加突出显示的行。这样，不是返回 404 错误作为默认选项，而是将控制权传递给 `index.php` 带有请求参数的文件。

这应该是这个样子：
```
server {
    listen 80;
    server_name 124.70.208.35:80 124.70.208.35:443;
    root /var/www/wordpress;
    index index.html index.htm index.php;
    
	location = /favicon.ico { log_not_found off; access_log off; }
    location = /robots.txt { log_not_found off; access_log off; allow all; }
    location / {
        #try_files $uri $uri/ =404;
        try_files $uri $uri/ /index.php$is_args$args;
    }
    location ~* \.(css|gif|ico|jpeg|jpg|js|png)$ {
        expires max;
        log_not_found off;
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

完成后，保存并关闭文件。

现在，让我们通过键入以下内容来检查我们的配置是否存在语法错误：

```
sudo nginx -t
```


如果没有报告错误，请键入以下命令重新加载 Nginx：

```
sudo systemctl reload nginx
```

### 6. 下载和配置 WordPress

现在您的服务器软件已配置完毕，让我们下载并设置 WordPress。出于安全原因，始终建议直接从项目网站获取最新版本的 WordPress。

更改为可写目录，然后通过键入以下内容下载压缩版本：

```
cd /tmp
```

这会将您的目录更改为临时文件夹。然后，输入以下命令以压缩文件形式下载最新版本的 WordPress：

```
curl -LO https://wordpress.org/latest.tar.gz
```

**注意：** 该`-LO`标志用于直接获取压缩文件的源。`-L`确保在重定向的情况下成功获取文件，并`-O`使用具有相同名称的本地文件写入远程文件的输出。要了解有关`curl`命令的更多信息，请访问[如何使用 cURL 下载文件](https://www.digitalocean.com/community/tutorials/workflow-downloading-files-curl)

提取压缩文件以创建 WordPress 目录结构：

```
tar xzvf latest.tar.gz
```



您将暂时将这些文件移动到我们的文档根目录中，但在您这样做之前，让我们将示例配置文件到 WordPress 实际读取的文件名中：

```
cp /tmp/wordpress/wp-config-sample.php /tmp/wordpress/wp-config.php
```



现在，让我们将目录的全部内容到我们的文档根目录中。我们使用`-a`标志来确保我们的权限得到维护，并在我们的源目录末尾使用一个点来指示应该目录中的所有内容（包括隐藏文件）：

```
sudo cp -a /tmp/wordpress/. /var/www/wordpress
```



现在我们的文件已准备就绪，您可以将所有权分配给**www-data**用户和组。这是 Nginx 运行的用户和组，Nginx 需要能够读取和写入 WordPress 文件才能为网站提供服务并执行自动更新：

```
sudo chown -R www-data:www-data /var/www/wordpress
```



文件现在位于服务器的文档根目录中并具有正确的所有权，但您仍然需要完成一些额外的配置。接下来，让我们对主要的 WordPress 配置文件进行一些更改。

当您打开该文件时，您将首先调整一些密钥来为我们的安装提供一些安全性。WordPress 为这些值提供了一个安全的生成器，因此您不必自己想出值。这些仅在内部使用，因此在此处具有复杂、安全的值不会损害可用性。

要从 WordPress 密钥生成器获取安全值，请键入：

```
curl -s https://api.wordpress.org/secret-key/1.1/salt/
```

> [!warning] 警告
> 每次请求唯一值很重要。不要**复制**下面显示的值！

```
Outputdefine('AUTH_KEY',         '1jl/vqfs<XhdXoAPz9 DO NOT COPY THESE VALUES c_j{iwqD^<+c9.k<J@4H');
define('SECURE_AUTH_KEY',  'E2N-h2]Dcvp+aS/p7X DO NOT COPY THESE VALUES {Ka(f;rv?Pxf})CgLi-3');
define('LOGGED_IN_KEY',    'W(50,{W^,OPB%PB<JF DO NOT COPY THESE VALUES 2;y&,2m%3]R6DUth[;88');
define('NONCE_KEY',        'll,4UC)7ua+8<!4VM+ DO NOT COPY THESE VALUES #`DXF+[$atzM7 o^-C7g');
define('AUTH_SALT',        'koMrurzOA+|L_lG}kf DO NOT COPY THESE VALUES  07VC*Lj*lD&?3w!BT#-');
define('SECURE_AUTH_SALT', 'p32*p,]z%LZ+pAu:VY DO NOT COPY THESE VALUES C-?y+K0DK_+F|0h{!_xY');
define('LOGGED_IN_SALT',   'i^/G2W7!-1H2OQ+t$3 DO NOT COPY THESE VALUES t6**bRVFSD[Hi])-qS`|');
define('NONCE_SALT',       'Q6]U:K?j4L%Z]}h^q7 DO NOT COPY THESE VALUES 1% ^qUswWgn+6&xqHN&%');
```

这些是您可以直接粘贴到配置文件中以设置安全密钥的配置行。复制您现在收到的输出。

现在，打开 WordPress 配置文件：

```
sudo nano /var/www/wordpress/wp-config.php
```

找到包含这些设置的虚拟值的部分。它看起来像这样：

> [!example] 示例
> 
> ```
> ... 
> define('AUTH_KEY',         'put your unique phrase here');
> define('SECURE_AUTH_KEY',  'put your unique phrase here');
> define('LOGGED_IN_KEY',    'put your unique phrase here');
> define('NONCE_KEY',        'put your unique phrase here');
> define('AUTH_SALT',        'put your unique phrase here');
> define('SECURE_AUTH_SALT', 'put your unique phrase here');
> define('LOGGED_IN_SALT',   'put your unique phrase here');
> define('NONCE_SALT',       'put your unique phrase here');
> ... 
> ```

删除这些行并粘贴您从命令行复制的值：

接下来，让我们修改文件开头的一些数据库连接设置。您必须调整数据库名称、数据库用户以及在 MySQL 中配置的关联密码。

您应该进行的另一项更改是设置 WordPress 用于写入文件系统的方法。由于您已授予 Web 服务器写入所需位置的权限，因此您可以明确地将文件系统方法设置为“direct”。未能使用我们当前的设置进行设置将导致 WordPress 在我们执行某些操作时提示输入 FTP 凭据。在数据库连接设置下方或文件中的任何其他位置添加此设置：
```
. . .

define( 'DB_NAME', 'wordpress' );

/** MySQL database username */
define( 'DB_USER', 'wordpressuser' );

/** MySQL database password */
define( 'DB_PASSWORD', 'password' );

. . .

define( 'FS_METHOD', 'direct' );
```

完成后保存并关闭文件。

# root

> [!Quote] 论文信息
>1. [How to Install WordPress with LEMP on Ubuntu 20.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lemp-on-ubuntu-20-04)
>2. [基于Ubuntu20.4搭建WordPress个人博客-CSDN博客](https://blog.csdn.net/TM2022/article/details/124386462)
