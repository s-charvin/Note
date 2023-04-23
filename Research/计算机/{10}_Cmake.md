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
lastmod: 2023-04-23 19:32:07
---

# Cmake

CMake 是一个跨平台的构建系统，用于自动生成用于编译和构建软件项目的构建脚本。具体的项目构建规则，由纯文本文件 CMakeLists.txt 控制，其通常位于项目的根目录下，包含了构建项目所需的环境配置、目标配置、编译选项、链接库等构建规则和一系列的 CMake 指令。

CMake 支持将一个或多个 CMakeLists.txt 文件作为输入，这意味着一个项目可以分为多个子项目目录，并在每个子目录下放置一个 CMakeLists.txt 文件，从而实现对子目录的单独构建配置。然后通过根目录的主 CMakeLists.txt 文件定义完整项目的全局构建配置、子项目构建规则、全局编译选项和链接库等即可。

## CMake 基本用法

```CMake
cmake_minimum_required(VERSION 3.10)
project(MultiProjectBuild VERSION 1.0)
```
