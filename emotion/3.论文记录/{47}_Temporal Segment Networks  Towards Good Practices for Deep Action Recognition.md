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
lastmod: 2022-11-12 20:39:56
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

给定一个视频 $V$ ，我们将其分成 $K$ 个时长相等的视频段 ${S_1，S_2，···，S_K}$ 。然后，TSN 网络对此视频段序列的建模如下：

$$
\operatorname{TSN}\left(T_1, T_2, \cdots, T_K\right)=\mathcal{H}\left(\mathcal{G}\left(\mathcal{F}\left(T_1 ; \mathbf{W}\right), \mathcal{F}\left(T_2 ; \mathbf{W}\right), \cdots, \mathcal{F}\left(T_K ; \mathbf{W}\right)\right)\right)
$$

这里的 $\left(T_1, T_2, \cdots, T_K\right)$ 是一个视频帧序列，其中每个帧片段 $T_k$ 随机取样自对应的视频段 $S_k$ 。 $\mathcal{F}\left(T_k ; \mathbf{W}\right)$ 是表示带有参数 $\mathbf{W}$ 的卷积网络函数，该函数对视频帧 $T_k$ 进行计算，并生成类别评分。分段共识(Segmental consensus)函数 $\mathcal{G}$ 会将来自多个视频段的输出组合在一起，以获得其中类别预测的共识。基于这一共识，预测函数 $\mathcal{H}$ (如 Softmax 函数)可以计算出整个视频中每个类别的概率。结合标准分类交叉熵 (standard categorical cross-entropy) 损失函数,  通过分段共识 $\mathbf{G}=\mathcal{G}\left(\mathcal{F}\left(T_1 ; \mathbf{W}\right), \mathcal{F}\left(T_2 ; \mathbf{W}\right), \cdots, \mathcal{F}\left(T_K ; \mathbf{W}\right)\right)$ ，可以得到最终损失函数公式为：

$$
\mathcal{L}(y, \mathbf{G})=-\sum_{i=1}^C y_i\left(G_i-\log \sum_{j=1}^C \exp G_j\right),
$$

其中 $C$ 是类别的数量， $y_i$ 是关于类 $i$ 的真实标签。在实际实验中，根据之前 $[16,17]$ 的研究，将视频段的数量 $K$ 设置为 3。而共识函数 $\mathcal{G}$ ，在本文工作中我们使用了最简单的形式：聚合函数 $g$ （平均、最大值、加权平均），即 $G_i=$ $g\left(\mathcal{F}_i\left(T_1\right), \ldots, \mathcal{F}_i\left(T_K\right)\right)$ 。

一些研究表明，更深层的结构可以提高物体识别性能[9,10]。因此在本研究中，我们选择了原始的具有 Batch Normalization 的 Inception (BN-Inception)[23]作为构建块来设计 two-stream 卷积网络，因为它在准确性和效率之间有很好的平衡。与原始的 two-stream 卷积网络[1]一样，spatial stream 卷积网络的输入为单个 RGB 图像，temporal stream 卷积网络的输入为叠加的连续光流（optical flow）。

在这里，我们提出研究两种额外的输入模式，即 RGB difference 和 warped optical flow fields。

采用 RGB difference 的灵感来源于，单个 RGB 图像通常只能编码特定时间点的静态外观，而缺乏前一帧和下一帧的上下文信息（动态信息）。因此我们尝试将 stacked RGB difference 作为另一种输入方式，并研究了其在动作识别中的性能。

warped optical flow fields  的灵感来源于[28]，temporal stream 卷积网络以光流（optical flow）为输入，以捕获运动信息为目标。然而，在现实的视频中，通常存在着摄像机运动，光流（optical flow）可能不只会集中在人的动作上。受改进的 dense trajectories[2]的启发，我们提出了采用弯曲光流（warped optical flow）作为附加输入模态。

## 引文
