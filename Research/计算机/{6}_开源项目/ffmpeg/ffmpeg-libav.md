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
lastmod: 2023-05-20 20:33:46
---



`ffmpeg` 作为一个通用的媒体转换器,  其功能实现主要是通过几个基本的 libav 系列库来实现的,  其整个转换过程可以大致抽象为以下过程

![](ffmpeg-libav.assets/ffmpeg.svg)

首先在了解具体的转换过程前,  需要先介绍部分上图包含的以及与其相关的抽象术语.

- 封装(Muxer): 又称容器,  用于按照某种规则组合,  传输和存储多种编码后的媒体流(音频、视频、字幕、章节信息等),  方便对这些元素的统一管理. 常见封装格式有 AVI, FLV, MKV, MP4 等.
- 解封装(Demuxer): 封装的反操作,  用于从输入数据中解析分离出不同类型的媒体流数据.
- 流(Stream): 流是媒体数据信息的一种传输方式,  一般的媒体传输会包含视频流(Video Stream)、音频流(Audio Stream)、字幕(Subtitle)、附件(t)、数据(d)等信息.
- 数据包(Packet): 将所有的媒体流分割为一段段进行处理,  这些分段数据解析后会存放在各自类型的数据包(Packet)中. (一般一个 Packet 会存放一个视频帧或多个音频帧).
- 解码(Decoder): 一般的媒体数据均是经过压缩处理的,  因此这里是将输入数据还原为原始数据的过程.
- 帧(Frame): 编解码器真正处理的数据最小处理单元
- 编码(Encoder): 对原始数据进行加工或压缩,  然后输出的过程. (视频: H263、H264、H265、MPEG)


`ffmpeg` 的封装(Muxer)和解封装(Demuxer)操作是通过调用 `libavformat` 库来实现的. `libavformat` 库提供了丰富的协议处理及封装格式处理功能,  可以在打开输入(输出)时,  根据输入(输出)的格式,  选择合适的协议和封装格式,  完成媒体流数据到文件的读写(I/O)操作或媒体流协议的数据解析. 其中,  媒体流数据会被分割为数据包(Packet)一段段进行处理,  具体存储结构由 `libavformat` 库中的 `AVPacket` 结构体定义. 

由于媒体数据是时间序列类型的,  因此每个输入文件可能包含多个流, 每个输入流都会包含一系列的数据包（Packet）,  同时每个数据包都会有一个时间戳, 用于表示该数据包在时间轴上的位置. 时间戳可以是以时间单位（例如秒、毫秒）表示的具体时间值, 或者是以时间基准（例如帧号）表示的相对时间值. 

当有多个输入文件时,  `ffmpeg` 会尝试通过跟踪任何活动输入流上的最低时间戳,  选择具有最小时间戳的数据包作为当前处理的数据包,  来确保多个输入文件之间的数据在时间上保持同步, 避免数据错位或乱序. 

如果使用 ffmpeg 时采用 `streamcopy` 方法, 则可以直接略过编码数据包的解码处理阶段直接将数据包传递给封装过程, 一般用于媒体封装格式的直接转换. 

如果需要对其中的媒体数据进行处理, 则需要利用到 `libavcodec` 库中提供的编解码器, 通过解码器可以将编码的数据包还原为原始未压缩的帧数据（原始视频/PCM 音频/...）. 帧数据被处理完毕后被传递给编码器, 编码器对它们进行编码并输出编码数据包. 最后, 这些被传递给封装(Muxer)过程, 它将编码的数据包写入输出文件或协议流. 

# 通过官方样例代码学习 ffmpeg

## 解码音频流

```
const char *outfilename, *filename;


```


> [!cite]
> https://www.longqi.cf/tools/2015/02/13/ffmpegcn/
> https://ffmpeg.org/doxygen/trunk/index.html
> https://leixiaohua1020.github.io/
> https://blog.csdn.net/friend_gank/category_1072727.html
> https://blog.csdn.net/hustbin/category_1113443.html
> https://blog.csdn.net/leixiaohua1020/article/details/44220151
> [0voice/ffmpeg_develop_doc](https://github.com/0voice/ffmpeg_develop_doc)
