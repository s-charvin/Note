---
title: "{{Cmake}}"
description: ""
author: ""
tags: [""]
categories: ""
keywords:  [""]
draft: true
layout: ""
date: 2023-03-11 14:10:34
lastmod: 2023-04-23 13:18:20
---





CMake 是一个跨平台的构建系统，用于自动生成用于编译和构建软件项目的构建脚本。具体的项目构建规则，由纯文本文件 CMakeLists.txt 控制，其中包含了构建项目所需的构建规则和一系列的 CMake 指令。CMakeLists.txt 文件通常位于项目的根目录下，用于定义项目的构建配置、目标和构建规则等。CMakeLists.txt 文件使用 CMake 的脚本语言，其中包含了一系列的 CMake 指令，用于设置项目的构建环境、编译选项、链接库、生成可执行文件、安装目标等。

## Cmake 构建目录结构

CMake 在构建项目时使用两个主要目录：源目录和二进制目录。源目录是项目源代码所在的位置。这也是可以找到 CMakeLists 文件的地方。二进制目录有时称为构建目录，CMake 将在其中放置生成的目标文件、库和可执行文件。CMake 不会将任何文件写入源目录，只会写入二进制目录，因此强烈建议使用区域隔离的源目录和二进制目录。

## CMake 基本用法

将一个或多个 CMakeLists 文件作为输入并生成项目文件或 Makefile 以用于各种本机开发工具。

## CMakeLists 文件

CMakeLists 文件是纯文本文件，其中包含 CMake 语言中的项目描述。这[`cmake-language`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#manual:cmake-language(7) "（在 CMake v3.26.0 中）")表示为一系列注释、命令和变量。您可能想知道为什么 CMake 决定拥有自己的语言而不是使用现有的语言，例如 Python、Java 或 Tcl。主要原因是 CMake 开发人员不想让 CMake 需要额外的工具才能运行。通过要求其中一种其他语言，CMake 的所有用户都需要安装该语言，并且可能需要安装该语言的特定版本。出于性能和功能原因，这是执行某些 CMake 工作所需的语言扩展之上的。

### CMake 的 Hello World
