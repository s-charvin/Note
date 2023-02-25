---
title: "Multiscale Vision Transformers"
description: ""
citekey: fanMultiscaleVisionTransformers2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-25 20:57:22
lastmod: 2023-02-25 21:26:30
---

> [!info] 论文信息
>1. Title：Multiscale Vision Transformers
>2. Author：Haoqi Fan, Bo Xiong, Karttikeya Mangalam, Yanghao Li, Zhicheng Yan, Jitendra Malik, Christoph Feichtenhofer
>3. Entry：[Zotero link](zotero://select/items/@fanMultiscaleVisionTransformers2021) [URL link](http://arxiv.org/abs/2104.11227) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Fan et al_2021_Multiscale Vision Transformers.pdf>)
>4. Other：2021 - arxiv:2104.11227 [cs]  arXiv   -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 

## 摘要

> [!abstract] We present Multiscale Vision Transformers (MViT) for video and image recognition, by connecting the seminal idea of multiscale feature hierarchies with transformer models. Multiscale Transformers have several channel-resolution scale stages. Starting from the input resolution and a small channel dimension, the stages hierarchically expand the channel capacity while reducing the spatial resolution. This creates a multiscale pyramid of features with early layers operating at high spatial resolution to model simple low-level visual information, and deeper layers at spatially coarse, but complex, high-dimensional features. We evaluate this fundamental architectural prior for modeling the dense nature of visual signals for a variety of video recognition tasks where it outperforms concurrent vision transformers that rely on large scale external pre-training and are 5-10x more costly in computation and parameters. We further remove the temporal dimension and apply our model for image classification where it outperforms prior work on vision transformers. Code is available at: https://github.com/facebookresearch/SlowFast

> 我们通过将多尺度特征层次结构的开创性思想与 Transformer 模型联系起来，展示了用于视频和图像识别的 Multiscale Vision Transformers (MViT)。多尺度 Transformer 有几个 channel-resolution 尺度的 stages。其从输入分辨率和小维度 channel 开始，阶段分层扩展通道维度，同时降低空间分辨率。这创建了一个多尺度特征金字塔，早期层在高空间分辨率下运行以模拟简单的低级视觉信息，而更深层在空间粗糙但复杂的高维特征上运行。我们评估了这种先验基础架构，用于为各种视频识别任务建模视觉信号的密集性质，它优于依赖大规模外部预训练的 concurrent vision transformer，并且在计算和参数方面的成本高出 5-10 倍。我们进一步删除了时间维度并将我们的模型应用于图像分类，它优于先前在视觉 transformer 上的工作。代码位于：https://github.com/facebookresearch/SlowFast。

## 预处理

## 概述

## 结果

## 精读

Multiscale Vision Transformer (MViT)

我们的通用 Multiscale Transformer 架构建立在分阶段的核心概念之上。每个阶段由多个具有特定 space-time 分辨率和通道维度的 transformer 块组成。 Multiscale Transformers 的主要思想是逐步扩展通道容量，同时池化(pooling, 降低)网络的输入到输出的特征图分辨率。

我们首先描述了多头池注意力机制 (MHPA, Multi Head Pooling Attention)，这是一种自注意运算，可以在 transformer 块中实现灵活的对特征图建模，从而使得多尺度 transformer 可以在逐渐变化的 space-time 分辨率下运行。与原始的多头注意力机制 (MHA, Multi Head Attention)  [98] 相比, 不像 MHA 那样, 通道维度和 space-time 分辨率保持固定，而是会池化潜在特征张量序列以减少参与输入的序列长度（分辨率）, 如下图所示。
![]({53}_Multiscale%20Vision%20Transformers@fanMultiscaleVisionTransformers2021.assets/image-20230225212421.png)




### 引文

## 摘录
