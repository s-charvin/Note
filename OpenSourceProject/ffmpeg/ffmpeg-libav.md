---
title: "{{ffmpeg-libav}}"
description: ""
author: ""
tags: [""]
categories: ""
keywords:  [""]
draft: true
layout: ""
date: 2023-05-14 20:14:43
lastmod: 2023-05-14 20:38:01
---



`ffmpeg` 作为一个通用的媒体转换器, 其功能实现主要是通过几个基本的 libav 系列库来实现的. 首先, 其整个转换过程可以大致抽象为以下过程

```
 _______              ______________
|       |            |              |
| input |  demuxer   | encoded data |   decoder
|  输入  | ---------> | packets      | -----+
|_______|            |______________|      |
                                           v
                                       _________
                                      |         |
                                      | decoded |
                                      | frames  |
                                      |_________|
 ________             ______________       |
|        |           |              |      |
| output | <-------- | encoded data | <----+
|  输出   |   muxer   | packets      |   encoder
|________|           |______________|

```
