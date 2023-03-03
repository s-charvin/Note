---
title: ""
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-04-17 14:17:29
lastmod: 2022-06-07 10:34:56
---

# 重点

- 论文原文件
- [开源代码](https://github.com/ekazakos/auditory-slow-fast)
- 场景音频识别论文，从音频中识别物体、交互和活动需要识别发出声音的物体(如闹钟、咖啡机)、与物体交互产生的声音(如放下玻璃、关闭抽屉)和活动(如洗涤、油炸)。
- 单网络，双stream结构，分别重点分析时域和频域的特征。
- 使用可分离卷积分别关注输入信号的时间和频率。
- 在卷积层、残差链接模块处的结束处使用横向链接，把 Fast stream的特征融合到了Slow stream中。

# 摘要

We propose a two-stream convolutional network for audio recognition, that operates on time-frequency spectrogram inputs. Following similar success in visual recognition, we learn Slow-Fast auditory streams with separable convolutions and multi-level lateral connections. The Slow pathway has high channel capacity while the Fast pathway operates at a fine-grained temporal resolution. We showcase the importance of our two-stream proposal on two diverse datasets: VGG-Sound and EPIC-KITCHENS-100, and achieve stateof-the-art results on both.

我们提出了一种用于音频识别的双流卷积网络，该网络操作于时频谱图输入。在视觉识别方面取得类似的成功之后，我们学习了具有可分离的卷曲和多层侧向连接的慢-快听觉流。慢路径具有高的信道容量，而快路径以细粒度的时间分辨率运行。我们在两个不同的数据集上展示了我们的两流建议的重要性：VGG-Sound和EPIC-Kitchens-100，并在这两个数据集上取得了最先进的结果。

# 词汇记录

# 结果

# 精读

与之前的场景音频识别不同，从音频中识别物体、交互和活动需要识别发出声音的物体(如闹钟、咖啡机)、与物体交互产生的声音(如放下玻璃、关闭抽屉)和活动(如洗涤、油炸)。这就带来了与这些活动相关的可变长度音频的挑战。有些可能是短暂的(如靠近)，而另一些则在较长的时间内重复(如油炸)，此外还有许多表现出类内的变化(如切洋葱和切奶酪)。通常背景或无关的声音活动经常被捕捉到。我们使用了两个分别从YouTube和egocentric 的视频中捕获的基于活动的数据集：VGG-Sound[1]和EPIC-KITCHENS[2]，，并仅从与这些视频相关的音频信号中识别目标活动。神经科学有强有力的证据表明，在人类听觉系统中存在两种听觉流，一种是用于识别发出声音的物体的 the ventral stream，另一种是用于定位这些物体的 the dorsal streams。研究[3,4]表明 the ventral stream 相应地表现出高声谱分辨率，用于目标识别，而 the ventral stream 具有高时间分辨率以及更高的工作采样率。

这一证据是我们设计此结构的动力，并受到类似的基于视觉的结构[5]的启发，我们提出了两种听觉识别流: Slow and Fast stream，它们分别实现了ventral 和 dorsal 听觉通道的一些属性。我们的 stream 是残差网络的变体，并使用二维可分离卷积，它分别在频率和时间上独立运行。通过从 Fast streams 到 Slow streams 的横向连接，将流融合到多个表示级别，并通过连接全局平均池化表示获得最终表示，以进行动作识别。本文的贡献如下:i)我们提出了一种新的基于神经科学证据的听觉识别双流结构;ii)我们在epic - kitchen和VGGSound上都取得了最先进的效果;最后iii)我们通过消融分析来展示融合我们的特殊流的重要性。

![]({13}_Slow-Fast%20Auditory%20Streams%20for%20Audio%20Recognition@kazakosSlowFastAuditoryStreams2021.assets/image-20220304010406.png)

![]({13}_Slow-Fast%20Auditory%20Streams%20for%20Audio%20Recognition@kazakosSlowFastAuditoryStreams2021.assets/image-20220304010424.png)

我们提出的方法使用考虑相同输入的 two-streams 结构：Slow stream 和 Fast stream。

两种 stream 的输入相同的音频，并从中提取出 log-mel-spectrogram。Slow streams 以限制低采样率和保持高通道容量来捕获频率特征，在输入的对数mel频谱图上使用的时间跨度 stride=α，其中a≥1；而 Fast streams 以保持高采样率和限制小通道容量来捕获时间特征，以整个对数mel频谱图作为输入，没有任何时间跨度stride。

两种 stream 结构都是ResNet50[26]网络的变体。每个 stream 前置部分由一个初始卷积块conv1和一个池化层pool1组成，池化层后面是4个 residual 过程，其中每个过程包含多个 residual 块。Slow streams 信道容量高，为Fast的β=8倍，输入谱图的时间跨度为α=4，因此时间分辨率（采样率）低。此外，由图可知， Slow streams 仅在res4和res5中在时间维度上有卷积(见右侧图1中的棕色和绿色块)。另一方面，Fast stream 输入谱图无时间跨度，为完整mel谱，并且在整个流中都有时间卷积，对特征通道有所限制。网络结构中的卷积过程，使用的可分离卷积，将原3×3内核分成两个内核，3×1和1×3，分别关注输入信号的时间和频率。遵循[5]中的方法，我们在 pool1 和每个 residual 过程后通过 lateral connections 将 Fast streams 信息融合到 Slow streams中 。首先将 Fast stream 的输出通过一个卷积核为7×1，时间跨度stride=α=4的二维时域卷积和来匹配 Slow streams 的采样率。然后我们将此Fast stream下采样得到的特征图与 Slow streams 特征图连接起来。**为了补偿原始音频的高采样率**，我们在两个stream的conv1和pool1中使用时间 stride=2，对两个stream的特征图进行了4倍的时间下采样，其余阶段不执行任何时间下采样。

在 Slow streams 和 Fast streams 的最后一个卷积层之后，应用 time-frequency 全局平均池化层，并将池化得到的特征连接后输入到分类器中，通过FC层获得最终的表示。

## 引用

Single-stream architectures. 

- 这些算法将频谱图作为输入，使用二维卷积和k×k方形滤波器，同时处理频率和时间，类似于图像卷积网络[6,7,9,10,11,12,13,14]。

- 在音频识别中，场景和活动识别的一种常见方法是使用 single-stream 卷积体系结构[6,7,8]。

- SoundNet[8]使用了以 teacher-student 方式训练的1D ConvNet，并对声学场景分类进行了微调。

- Single-stream 2D ConvNets 已广泛应用于DCASE挑战的高星参赛作品中，并用于声场景分类[9,10,11,12,13,14]。

- 然而，由于频谱图的统计量不均匀，在频率和时间上的对称滤波可能不是最优的。

- 一种选择是使用矩形 k×m滤波器，如[15,16]。

- 另一种方法是使用1 × k和k × 1滤波器的可分离卷积网络，最近已在[17,18]中使用。

Multi-stream architectures. 

- 在[19,20,21,22,23,24,25]中采用了 Late fusion of multiple streams 进行音频识别。

- 大多数方法使用的 modality-specific streams [19, 20, 21, 22]. 

- 除了late fusion 之外, 在[20, 21] 中注意力机制结构中集成了 multi-level fusion. 

- 在 [23, 24, 25]中, 所有 streams 融合为相同的输入 。

- In [23], 一个 stream 以低频为输入，另一个以高频为输入。

- [24] applies median filtering with different kernels at the input of each stream to model long duration sound events, medium, and short duration impulses separately. 

- [24]在每个输入 stream 处采用不同内核的中值滤波，分别对长时声音、中等持续脉冲和短时脉冲建模。

- In [25] , 1D convolutions are used with different dilation rates at each stream to model convolutional streams that operate on different temporal resolutions. 

- 在[25]中，使用在每个输入 stream 上具有不同空洞卷积率的一维卷积，来模拟运行在不同时间分辨率上的卷积 stream 。
