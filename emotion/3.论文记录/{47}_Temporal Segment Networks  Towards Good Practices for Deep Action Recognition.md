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
lastmod: 2022-11-12 14:02:32
---

# 重点

- [开源代码](https://github.com/yjxiong/tsn-pytorch)

# 摘要

Deep convolutional networks have achieved great success for visual recognition in still images. However, for action recognition in videos, the advantage over traditional methods is not so evident. This paper aims to discover the principles to design effective ConvNet architectures for action recognition in videos and learn these models given limited training samples. Our first contribution is temporal segment network (TSN), a novel framework for video-based action recognition. which is based on the idea of long-range temporal structure modeling. It combines a sparse temporal sampling strategy and video-level supervision to enable efficient and effective learning using the whole action video. The other contribution is our study on a series of good practices in learning ConvNets on video data with the help of temporal segment network. Our approach obtains the state-the-of-art performance on the datasets of HMDB51 (69.4%) and UCF101 (94.2%). We also visualize the learned ConvNet models, which qualitatively demonstrates the effectiveness of temporal segment network and the proposed good practices. 1

深度卷积网络在静止图像的视觉识别领域取得了巨大成功。然而，对于视频中的动作识别，这些传统方法的优势并不明显。本文旨在研究(discover the principles)如何为视频动作识别设计高效的 ConvNet 架构，并在有限的训练样本下学习这些模型。我们的第一个贡献是 temporal segment network（TSN），一种用于视频动作识别的新框架。其基于长时间结构建模(long-range temporal structure modeling)的思想。它结合了稀疏时间采样策略和视频级监控，以实现使用整个动作视频的高效学习。另一个贡献是我们对借助时间段网络在视频数据上学习 ConvNets 的一系列良好实践的研究。我们的方法在 HMDB51（69.4%）和 UCF101（94.2%）的数据集上获得了最先进的性能。我们还将学习到的 ConvNet 模型可视化，定性地证明了时间段网络的有效性和提出的良好实践。

# 结果

# 词汇记录

# 精读

## 引文
