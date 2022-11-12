---
title: "Temporal Segment Networks: Towards Good Practices for Deep Action Recognition"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: "笔记"
draft: true
layout: 
data: 2022-08-26 22:01:02
lastmod: 2022-11-12 14:41:38
---

# 重点

- [开源代码](https://github.com/yjxiong/tsn-pytorch)

# 摘要

Deep convolutional networks have achieved great success for visual recognition in still images. However, for action recognition in videos, the advantage over traditional methods is not so evident. This paper aims to discover the principles to design effective 卷积网络 architectures for action recognition in videos and learn these models given limited training samples. Our first contribution is temporal segment network (TSN), a novel framework for video-based action recognition. which is based on the idea of long-range temporal structure modeling. It combines a sparse temporal sampling strategy and video-level supervision to enable efficient and effective learning using the whole action video. The other contribution is our study on a series of good practices in learning 卷积网络s on video data with the help of temporal segment network. Our approach obtains the state-the-of-art performance on the datasets of HMDB51 (69.4%) and UCF101 (94.2%). We also visualize the learned 卷积网络 models, which qualitatively demonstrates the effectiveness of temporal segment network and the proposed good practices. 1

深度卷积网络在静止图像的视觉识别领域取得了巨大成功。然而，对于视频中的动作识别，这些传统方法的优势并不明显。本文旨在研究(discover the principles)如何为视频动作识别设计高效的卷积网络架构，并在有限的训练样本下学习这些模型。我们的第一个贡献是 temporal segment network（TSN），一种基于长时间结构建模(long-range temporal structure modeling)的思想, 用于视频动作识别的新框架。它结合了稀疏时间采样(sparse temporal sampling)策略和视频层级监督，以实现使用整个动作视频的高效学习。另一个贡献是我们在 TSN 网络的帮助下, 对视频数据上学习卷积网络 s 的一系列优秀的实践研究。我们的方法在 HMDB51（69.4%）和 UCF101（94.2%）的数据集上获得了最先进的性能。同时, 我们还将学习到的卷积网络模型进行了可视化，定性地证明了 TSN 网络的有效性和实践结果。

# 结果

# 词汇记录

# 精读

现有形式的双流卷积网络的一个明显问题是它们不能对远距时间结构进行建模。这主要是因为它们被设计为仅在单个帧(spatial networks)或连续帧堆叠的短片段(temporal network)上操作, 从而对时序上下文的访问有限。然而，对于一种复杂的动作，如体育动作，都横跨相对较长时间, 由多个片段组成。因此如果不能将这些动作中的远距时间结构参与到卷积网络训练中，那将是相当大的损失。

而本文提出的 TSN 网络就能够对整个视频中的动态变化进行建模。

具体来说，我们提出的 TSN 网络框架也是由 spatial stream 卷积网络和 temporal stream 卷积网络组成，并且其能够利用整个视频的视觉信息来实现视频层面的预测。TSN 网络并不是在单个帧或连续帧堆叠的短片段上学习，而是在从整个视频中经过稀疏采样得到的一系列短片段上学习。该序列中的每个代码片断都将生成其自己的操作类的初步预测。然后，将推导出片段之间的共识作为视频级预测。在学习过程中，通过迭代更新模型参数来优化视频级别预测的损失值，而不是两个流卷积网络中使用的摘录级别预测的损失值。 

给定一个视频 V，我们将其分成 K 个时长相等的段{S1，S2，···，SK}。然后，TSN 网络对此序列的建模如下：

$$
\operatorname{TSN}\left(T_1, T_2, \cdots, T_K\right)=\mathcal{H}\left(\mathcal{G}\left(\mathcal{F}\left(T_1 ; \mathbf{W}\right), \mathcal{F}\left(T_2 ; \mathbf{W}\right), \cdots, \mathcal{F}\left(T_K ; \mathbf{W}\right)\right)\right)
$$

## 引文
