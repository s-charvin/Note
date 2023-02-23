---
title: "Reversible Vision Transformers"
description: ""
citekey: mangalamReversibleVisionTransformers2022
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-23 10:58:38
lastmod: 2023-02-23 11:20:27
---

> [!info] 论文信息
>1. Title：Reversible Vision Transformers
>2. Author：Karttikeya Mangalam, Haoqi Fan, Yanghao Li, Chao-Yuan Wu, Bo Xiong, Christoph Feichtenhofer, Jitendra Malik
>3. Entry：[Zotero link](zotero://select/items/@mangalamReversibleVisionTransformers2022) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Mangalam et al_2023_Reversible Vision Transformers.pdf>)
>4. Other：2022 - 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)     -   

>- :luc_github: 论文实现：[https://github.com/karttikeya/minREV/](https://github.com/karttikeya/minREV/)
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 

## 摘要

> [!abstract] We present Reversible Vision Transformers, a memory efficient architecture design for visual recognition. By decoupling the GPU memory footprint from the depth of the model, Reversible Vision Transformers enable memory efficient scaling of transformer architectures. We adapt two popular models, namely Vision Transformer and Multiscale Vision Transformers, to reversible variants and benchmark extensively across both model sizes and tasks of image classification, object detection and video classification. Reversible Vision Transformers achieve a reduced memory footprint of up to 15.5× at identical model complexity, parameters and accuracy, demonstrating the promise of reversible vision transformers as an efficient backbone for resource limited training regimes. Finally, we find that the additional computational burden of recomputing activations is more than overcome for deeper models, where throughput can increase up to 3.9 × over their non-reversible counterparts. Code and models are available at https://github.com/facebookresearch/mvit.

> 我们介绍了 Reversible Vision Transformers，这是一种用于视觉识别的内存高效架构设计。通过将 GPU 内存需求与模型的深度分离，Reversible Vision Transformers 可以通过高效的内存使用来扩展架构。我们将两种流行的模型（即 Vision Transformer 和 Multiscale Vision Transformers）应用于 reversible 变体，并在模型大小和图像分类、对象检测和视频分类任务中广泛进行基准测试。 Reversible Vision Transformers 在大致相同的模型复杂度、参数和准确性下实现了高达 15.5 倍的内存占用减少，证明了 Reversible Vision Transformers 作为硬件资源有限训练条件下的的有效解决方案。最后，我们发现重新计算 activations 的额外计算负担对于更深的模型来说是可以克服的，其中吞吐量可以比不可逆模型增加 2.3 倍。

## 预处理

## 概述

## 结果

## 精读

计算机视觉领域的深度学习革命以高性能硬件加速器为基础。在专用 AI 加速器的推动下，对最先进模型的计算要求呈指数级增长。然而，计算只是故事的一半。另一个经常被忽视的一半是内存带宽瓶颈，与峰值加速器 FLOPs 相比，它很难按比例扩展 [54]。特别是，峰值加速器 FLOPs 以每 2 年约 3.1 倍的速度增加 [21, 62]。然而，峰值带宽仅以每 2 年约 1.4 倍的速度增长。这种差异在 transformer 中加剧，它们已经在过去的三年里翻了一番, 在过去的三年里，大约每三个月需要计算一次，这导致了所谓的内存墙 [21]，其中整体模型性能和训练速度都受到内存的严格限制 [34]。因此，对于带宽限制模型，通过重新计算以计算换取内存实际上可能比使用工作最优算法更有效 [70,71]。在训练神经网络模型的情况下，这可以通过重新计算激活而不是存储然后从 DRAM [31] 加载它们来实现。除了训练速度之外，scaling vision transformers 自然会影响 GPU 内存容量，尤其是在视频识别等内存匮乏的情况下，由于中间激活的内存占用量大，最先进的模型通常仅限于批量大小 1。我们提出 Reversible Vision Transformers，这是一系列富有表现力的视觉识别架构，与其不可逆变体相比，具有非常有利的激活记忆足迹![]({52}_Reversible%20Vision%20Transformers@mangalamReversibleVisionTransformers2022.assets/image-20230223111716.png)

。通过权衡 GPU 激活缓存与高效的即时激活重新计算，可逆视觉变换器有效地将激活内存增长与模型深度分离。

虽然自然语言处理社区已经对用于机器翻译的 reversible transformers 进行了一些早期探索 [38]，但这些技术侧重于更长的序列长度而不是深度。我们的实验表明，由于内部子块残差连接导致训练收敛不稳定，vision transformers 直接适应 reversible architectures 无法扩展到更深的模型。在这项工作中，我们重新配置 Vision Transformers (ViT) [15] 和 Multiscale Vision Transformers (MViT) [18] 中的残差路径来克服这个问题。我们进一步发现可逆结构具有更强的固有正则化，因此，我们使用更轻的增强配方（重复增强、增强幅度和随机深度）和残差块之间的横向连接。我们对图像分类和目标检测以及视频分类等图像识别任务进行了广泛的基准测试，在所有这些任务中，reversible vision transformers 与 non-reversible vision transformers 相比具有竞争力的性能，性能衰减可以忽略不计甚至没有。此外，可逆模型具有非常有利的每图像内存占用，在可逆训练的 ViT-Large 模型上节省 15.5 倍，在 MViTLarge 模型上节省 4.5 倍。




### 引文

## 摘录
