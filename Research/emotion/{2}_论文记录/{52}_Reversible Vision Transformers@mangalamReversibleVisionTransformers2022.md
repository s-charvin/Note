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
lastmod: 2023-02-23 11:04:29
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

### 引文

## 摘录
