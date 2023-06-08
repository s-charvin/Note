---
title: "InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions"
description: ""
citekey: wangInternImageExploringLargeScale2023
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-06-08 15:29:52
lastmod: 2023-06-08 15:30:10
---

> [!info] 论文信息
>1. Title：InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions
>2. Author：Wenhai Wang, Jifeng Dai, Zhe Chen, Zhenhang Huang, Zhiqi Li, Xizhou Zhu, Xiaowei Hu, Tong Lu, Lewei Lu, Hongsheng Li, Xiaogang Wang, Yu Qiao
>3. Entry：[Zotero link](zotero://select/items/@wangInternImageExploringLargeScale2023) [URL link](http://arxiv.org/abs/2211.05778) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Wang et al_2023_InternImage.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\FCU8FYKI\\2211.html>)
>4. Other：2023 - arxiv:2211.05778     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- :fas_question:   
- :obs_pdf_file:   
- :obs_graph_glyph:   
- :obs_wand_glyph:   

## 摘要

> [!abstract] Compared to the great progress of large-scale vision transformers (ViTs) in recent years, large-scale models based on convolutional neural networks (CNNs) are still in an early state. This work presents a new large-scale CNN-based foundation model, termed InternImage, which can obtain the gain from increasing parameters and training data like ViTs. Different from the recent CNNs that focus on large dense kernels, InternImage takes deformable convolution as the core operator, so that our model not only has the large effective receptive field required for downstream tasks such as detection and segmentation, but also has the adaptive spatial aggregation conditioned by input and task information. As a result, the proposed InternImage reduces the strict inductive bias of traditional CNNs and makes it possible to learn stronger and more robust patterns with large-scale parameters from massive data like ViTs. The effectiveness of our model is proven on challenging benchmarks including ImageNet, COCO, and ADE20K. It is worth mentioning that InternImage-H achieved a new record 65.4 mAP on COCO test-dev and 62.9 mIoU on ADE20K, outperforming current leading CNNs and ViTs. The code will be released at https://github.com/OpenGVLab/InternImage.

>  与近年来大规模视觉转换器 (ViTs) 的巨大进步相比，基于卷积神经网络 (CNN) 的大规模模型仍处于早期状态。这项工作提出了一种新的基于 CNN 的大规模基础模型，称为 InternImage，它可以从增加参数和训练数据（如 ViTs）中获得收益。不同于最近关注大密集核的 CNN，InternImage 以可变形卷积为核心算子，使我们的模型不仅具有检测和分割等下游任务所需的大有效感受野，而且具有自适应空间聚合以输入和任务信息为条件。因此，所提出的 InternImage 减少了传统 CNN 的严格归纳偏差，并使得从 ViT 等海量数据中学习具有大规模参数的更强、更鲁棒的模式成为可能。我们模型的有效性在具有挑战性的基准测试中得到了证明，包括 ImageNet、COCO 和 ADE20K。值得一提的是，InternImage-H 在 COCO test-dev 上取得了 65.4 mAP 的新纪录，在 ADE20K 上取得了 62.9 mIoU 的新纪录，优于当前领先的 CNN 和 ViT。该代码将在 https://github.com/OpenGVLab/InternImage 上发布。

## 预处理

## 概述

## 结果

## 精读

### 引文

## 摘录
