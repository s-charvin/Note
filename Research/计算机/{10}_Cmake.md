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
lastmod: 2023-04-23 13:39:17
---

# Cmake

CMake 是一个跨平台的构建系统，用于自动生成用于编译和构建软件项目的构建脚本。具体的项目构建规则，由纯文本文件 CMakeLists.txt 控制，其通常位于项目的根目录下，包含了构建项目所需的环境配置、目标配置、编译选项、链接库等构建规则和一系列的 CMake 指令。

CMake 支持将一个或多个 CMakeLists.txt 文件作为输入，这意味着一个项目可以分为多个子项目目录，并在每个子目录下放置一个 CMakeLists.txt 文件，从而实现对子目录的单独构建配置。然后通过根目录的主 CMakeLists.txt 文件定义完整项目的全局构建配置、子项目构建规则、全局编译选项和链接库等即可。

## CMake 基本用法

### 单文件构建过程

CMake 的单文件构建过程是通过在一个单独的 CMakeLists.txt 文件中定义构建规则和配置信息来完成的。这种方式适用于简单的项目或者构建过程较小的项目。


```cmake

# 设置最低的 CMake 版本要求
cmake_minimum_required(VERSION 3.10)

# 设置项目名称
project(MyProject)

# 设置源文件
set(SOURCES main.cpp)

# 添加可执行目标
add_executable(my_executable ${SOURCES})

# 设置编译选项
target_compile_options(my_executable PRIVATE -Wall -Wextra)

# 设置链接库
target_link_libraries(my_executable PRIVATE my_library)

```

## CMakeLists 文件
