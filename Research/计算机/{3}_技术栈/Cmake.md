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
lastmod: 2023-04-23 19:46:51
---

# Cmake

CMake 是一个跨平台的构建系统，用于自动生成用于编译和构建软件项目的构建脚本。具体的项目构建规则，由纯文本文件 CMakeLists.txt 控制，其通常位于项目的根目录下，包含了构建项目所需的环境配置、目标配置、编译选项、链接库等构建规则和一系列的 CMake 指令。

CMake 支持将一个或多个 CMakeLists.txt 文件作为输入，这意味着一个项目可以分为多个子项目目录，并在每个子目录下放置一个 CMakeLists.txt 文件，从而实现对子目录的单独构建配置。然后通过根目录的主 CMakeLists.txt 文件定义完整项目的全局构建配置、子项目构建规则、全局编译选项和链接库等即可。

## CMake 基本用法

脚本命令

```CMake
# 控制变量的值
set
if
else
elseif
endif

# 循环
while
endforeach
endforeach
foreach

# 定义函数和宏
function
macro

# 包含文件
include

# 查找包
find_package

# 获取属性
get_property

# 输出消息
message

# 选项
option

# 配置文件生成
configure_file

# 获取文件名组件
get_filename_component

# 获取目录属性
get_directory_property

# 设置最低版本要求
cmake_minimum_required

# 设置项目名称
site_name

# 设置属性
set_property

# 标记属性为高级选项
mark_as_advanced

# 文件操作
file
find_file
find_library
find_path
find_program

# 获取 CMake 属性
get_cmake_property

# 数学运算
math

# 字符串操作
string

# 列表操作
list

# 设置目录属性
set_directory_properties

# CMake 语言相关
cmake_language

# 取消变量的值
unset

# 执行外部进程
execute_process

# 获取系统信息
cmake_host_system_information

# 变量观察
variable_watch

# 解析命令行参数
cmake_parse_arguments

# 控制循环
continue
break

# CMake 策略
cmake_policy

# 包含守卫
include_guard

# 结束函数和宏
endfunction
endmacro

# 结束循环
endwhile

# 返回值
return

# 解析参数
separate_arguments

# 定义块
block
endblock

```

项目命令


```
project
add_executable
add_library
target_link_libraries
include_directories
target_include_directories
add_subdirectory
add_dependencies
install
enable_testing
add_test
target_sources
set_target_properties
add_custom_command
add_custom_target
link_directories
target_link_directories
set_tests_properties
add_definitions
target_compile_definitions
target_compile_options
add_compile_definitions
add_compile_options
define_property
target_compile_features
source_group
try_compile
try_run
create_test_sourcelist
get_target_property
set_source_files_properties
get_source_file_property
get_test_property
load_cache
add_link_options
target_link_options
remove_definitions
fltk_wrap_ui
aux_source_directory
build_command
include_regular_expression
link_libraries
add_subdirectory
enable_language
export
include_external_msproject
target_precompile_headers
target_sources
```
