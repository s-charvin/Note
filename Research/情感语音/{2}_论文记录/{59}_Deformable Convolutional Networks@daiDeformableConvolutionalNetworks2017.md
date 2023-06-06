---
title: "Deformable Convolutional Networks"
description: ""
citekey: daiDeformableConvolutionalNetworks2017
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-06-06 12:02:07
lastmod: 2023-06-06 12:09:00
---

> [!info] 论文信息
>1. Title：Deformable Convolutional Networks
>2. Author：Jifeng Dai, Haozhi Qi, Yuwen Xiong, Yi Li, Guodong Zhang, Han Hu, Yichen Wei
>3. Entry：[Zotero link](zotero://select/items/@daiDeformableConvolutionalNetworks2017) [URL link](http://arxiv.org/abs/1703.06211) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Dai et al_2017_Deformable Convolutional Networks.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\PAK9RILS\\1703.html>)
>4. Other：2017 - arxiv:1703.06211     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- :fas_question:   
- :obs_pdf_file:   
- :obs_graph_glyph:   
- :obs_wand_glyph:   

## 摘要

> [!abstract] Convolutional neural networks (CNNs) are inherently limited to model geometric transformations due to the fixed geometric structures in its building modules. In this work, we introduce two new modules to enhance the transformation modeling capacity of CNNs, namely, deformable convolution and deformable RoI pooling. Both are based on the idea of augmenting the spatial sampling locations in the modules with additional offsets and learning the offsets from target tasks, without additional supervision. The new modules can readily replace their plain counterparts in existing CNNs and can be easily trained end-to-end by standard back-propagation, giving rise to deformable convolutional networks. Extensive experiments validate the effectiveness of our approach on sophisticated vision tasks of object detection and semantic segmentation. The code would be released.

> 由于其构建模块中的固定几何结构，卷积神经网络 (CNN) 本质上仅限于模拟几何变换。在这项工作中，我们引入了两个新模块来增强 CNN 的转换建模能力，即可变形卷积和可变形 RoI 池化。两者都是基于这样的想法，即在没有额外监督的情况下，使用额外的偏移量来增加模块中的空间采样位置，并从目标任务中学习偏移量。新模块可以很容易地替换现有 CNN 中的普通模块，并且可以通过标准反向传播轻松地进行端到端训练，从而产生可变形的卷积网络。广泛的实验验证了我们方法的性能。我们首次表明，在深度 CNN 中学习密集空间变换对于复杂的视觉任务（例如对象检测和语义分割）是有效的。代码发布在 https://github.com/msracver/Deformable-ConvNets。

## 预处理

## 概述

## 结果

## 精读

视觉识别中的一个关键挑战是如何适应对象尺度、姿势、视点和零件变形的几何变化或模型几何变换。一般来说，有两种方式。首先是构建具有足够所需变化的训练数据集。这通常通过增加现有数据样本来实现，例如，通过仿射变换。可以从数据中学习到稳健的表示，但通常以昂贵的训练和复杂的模型参数为代价。第二种是使用变换不变的特征和算法。此类别包含许多众所周知的技术，例如 SIFT（尺度不变特征变换）[42] 和基于滑动窗口的对象检测范例。

上述方式有两个缺点。 首先，假定几何变换是固定的和已知的。 此类先验知识用于扩充数据，并设计特征和算法。 这个假设阻止了对具有未知几何变换的新任务的泛化，这些任务没有被正确建模。 其次，不变特征和算法的手工设计对于过于复杂的转换可能是困难的或不可行的，即使它们是已知的。

最近，卷积神经网络 (CNN) [35] 在图像分类 [31]、语义分割 [41] 和目标检测 [16] 等视觉识别任务中取得了重大成功。尽管如此，它们仍然存在上述两个缺点。他们对几何变换建模的能力主要来自广泛的数据增强、大模型容量和一些简单的手工制作模块（例如，用于小平移不变性的最大池 [1]）。

简而言之，CNN 本质上仅限于模拟大型、未知的转换。局限性源于 CNN 模块的固定几何结构：卷积单元在固定位置对输入特征图进行采样；池化层以固定比例降低空间分辨率； RoI（感兴趣区域）池化层将 RoI 分成固定的空间箱等。缺乏处理几何变换的内部机制。这会导致明显的问题。例如，同一 CNN 层中所有激活单元的感受野大小相同。这对于在空间位置上编码语义的高级 CNN 层来说是不可取的。因为不同的位置可能对应于具有不同尺度或变形的对象，所以尺度或感受野大小的自适应确定对于具有精细定位的视觉识别是可取的，例如，使用完全卷积网络的语义分割 [41]。再举一个例子，虽然最近物体检测取得了重大而快速的进展 [16、52、15、47、46、40、7]，但所有方法仍然依赖于基于原始边界框的特征提取。这显然是次优的，特别是对于非刚性物体。

在这项工作中，我们引入了两个新模块，它们极大地增强了 CNN 建模几何变换的能力。 第一个是可变形卷积。 它将 2D 偏移量添加到标准卷积中的常规网格采样位置。 它可以使采样网格自由变形。 如图 1 所示。偏移量是通过额外的卷积层从前面的特征图中学习的。 因此，变形以局部、密集和自适应的方式以输入特征为条件。

第二种是可变形的 RoI 池化。它为先前 RoI 池 [15、7] 的常规 bin 分区中的每个 bin 位置添加一个偏移量。类似地，偏移量是从前面的特征图和 RoIs 中学习的，从而可以对具有不同形状的对象进行自适应部分定位。

两个模块都很轻。他们为偏移学习添加少量参数和计算。它们可以很容易地替换深度 CNN 中的普通对应物，并且可以通过标准反向传播轻松地进行端到端训练。由此产生的 CNN 称为可变形卷积网络或可变形 ConvNet。

我们的方法与空间变换网络 [26] 和可变形部件模型 [11] 具有相似的高级精神。它们都有内部转换参数，并且纯粹从数据中学习这些参数。可变形卷积网络的一个关键区别在于它们以简单、高效、深入和端到端的方式处理密集的空间变换。在第 3.1 节中，我们详细讨论了我们的工作与以前工作的关系，并分析了可变形 ConvNets 的优越性。


Deformable Convolutional Networks

CNN 中的特征图和卷积是 3D 的。可变形卷积和 RoI 池化模块都在 2D 空间域上运行。该操作在整个通道维度上保持不变。在不失一般性的情况下，为了符号清晰起见，此处以 2D 形式描述模块。扩展到 3D 很简单。

Deformable Convolution

2D 卷积包括两个步骤：1）在输入特征图 $\mathrm{x}$ 上使用规则网格 $\mathcal{R}$ 进行采样； 2) 由 $\mathbf{w}$ 加权的采样值的总和。网格 $\mathcal{R}$ 定义感受野大小和膨胀。例如， $$ \mathcal{R}=\{(-1,-1),(-1,0), \ldots,(0,1),(1,1)\} $$ 定义 $3 \ 乘以 3$ 核，膨胀为 1 。对于输出特征图 $\mathbf{y}$ 上的每个位置 $\mathbf{p}_0$ ，我们有 $$ \mathbf{y}\left(\mathbf{p}_0\right)=\sum_{\ mathbf{p}_n \in \mathcal{R}} \mathbf{w}\left(\mathbf{p}_n\right) \cdot \mathbf{x}\left(\mathbf{p}_0+\mathbf{p }_n\right), $$ 其中 $\mathbf{p}_n$ 列举了 $\mathcal{R}$ 中的位置。在可变形卷积中，规则网格 $\mathcal{R}$ 增加了偏移量 $\left\{\Delta \mathbf{p}_n \mid n=1, \ldots, N\right\}$ ，其中 $N=|\mathbf{R}|$ 。当量。 (1) 变为 $$ \mathbf{y}\left(\mathbf{p}_0\right)=\sum_{\mathbf{p}_n \in \mathcal{R}} \mathbf{w}\left(\ mathbf{p}_n\right) \cdot \mathbf{x}\left(\mathbf{p}_0+\mathbf{p}_n+\Delta \mathbf{p}_n\right) 。$$ 现在，采样在不规则和偏移位置 $\mathbf{p}_n+\Delta \mathbf{p}_n$ 。由于偏移 $\Delta \mathbf{p}_n$ 通常是小数，Eq. (2) 通过双线性插值实现为 $$ \mathbf{x}(\mathbf{p})=\sum_{\mathbf{q}} G(\mathbf{q}, \mathbf{p}) \cdot \ mathbf{x}(\mathbf{q}), $$ 其中 $\mathbf{p}$ 表示任意（小数）位置 ( $\mathbf{p}=$ $\mathbf{p}_0+\mathbf{p} _n+\Delta \mathbf{p}_n$ for Eq. (2)), $\mathbf{q}$ 枚举了特征图 $\mathbf{x}$ 中的所有积分空间位置，而 $G(\cdot, \ cdot)$ 是双线性插值内核。请注意 $G$ 是二维的。它被分成两个一维内核 $G(\mathbf{q}, \mathbf{p})=g\left(q_x, p_x\right) \cdot g\left(q_y, p_y\right)$ , 其中 $g(a, b)=\max (0,1-|a-b|)$ 。当量。 (3) 的计算速度很快，因为 $G(\mathbf{q}, \mathbf{p})$ 仅在少数 $\mathbf{q}$ 时不为零。


如图 2 所示，偏移量是通过在同一输入特征图上应用卷积层获得的。卷积核与当前卷积层具有相同的空间分辨率和膨胀（例如，图 2 中也是 3 × 3，膨胀为 1）。输出偏移字段与输入特征图具有相同的空间分辨率。通道维度 2N 对应于 N 个 2D 偏移量。在训练期间，同时学习用于生成输出特征和偏移量的卷积核。为了学习偏移量，梯度通过方程式中的双线性运算反向传播。 （3）和方程式。 (4).详见附录 A。

Deformable RoI Pooling

RoI 池化用于所有基于区域建议的目标检测方法 [16、15、47、7]。它将任意大小的输入矩形区域转换为固定大小的特征。

RoI Pooling [15] 给定输入特征图 x 和大小为 w×h 和左上角 p0 的 RoI，RoI 池将 RoI 分成 k × k（k 是一个自由参数）个 bin 并输出 k × k 特征图y。对于 (i, j)-th bin (0 ≤ i, j < k)，我们有





### 引文

## 摘录
