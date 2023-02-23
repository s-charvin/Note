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
lastmod: 2023-02-23 12:50:45
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

提出 Reversible Vision Transformer (Rev-ViT) 和 Reversible Multiscale Vision Transformers (Rev-MViT)，这是最先进的视觉识别主干的内存高效可逆适应。

观察到 Reversible Transformer 比普通网络具有更强的内在正则化。因此，我们通过使用不同的重复增强、增强幅度和下降路径率来调整原始方法来开发新的训练方法，以匹配其 non-reversible 对应物的性能。

在多项任务中对模型进行基准测试：图像分类、对象检测和动作识别，以及准确性、内存、最大训练批次大小和模型复杂性。特别是，在匹配的复杂性（FLOPs/参数）和最终精度下，Rev-ViT-B 和 Rev-ViT-L 训练时每张图像的内存占用分别比 ViT-B 和 ViT-L 轻 8.2 倍和 15.5 倍。此外，我们还展示了深度 reversible 网络如何实现比普通网络高 2-4 倍的吞吐量。

## 结果

## 精读

计算机视觉领域的深度学习革命以高性能硬件加速器为基础。在专用 AI 加速器的推动下，对最先进模型的计算要求呈指数级增长。然而，计算只是故事的一半。另一个经常被忽视的一半是内存带宽瓶颈，与峰值加速器 FLOPs 相比，它很难按比例扩展 [54]。特别是，峰值加速器 FLOPs 以每 2 年约 3.1 倍的速度增加 [21, 62]。然而，峰值带宽仅以每 2 年约 1.4 倍的速度增长。这种差异在 transformer 中加剧，它们已经在过去的三年里翻了一番, 在过去的三年里，大约每三个月需要计算一次，这导致了所谓的内存墙 [21]，其中整体模型性能和训练速度都受到内存的严格限制 [34]。因此，对于带宽限制模型，通过重新计算以计算换取内存实际上可能比使用工作最优算法更有效 [70,71]。在训练神经网络模型的情况下，这可以通过重新计算激活而不是存储然后从 DRAM [31] 加载它们来实现。除了训练速度之外，scaling vision transformers 自然会影响 GPU 内存容量，尤其是在视频识别等内存匮乏的情况下，由于中间激活的内存占用量大，最先进的模型通常仅限于批量大小 1。我们提出 Reversible Vision Transformers，这是一系列富有表现力的视觉识别架构，与其不可逆变体相比，具有非常有利的激活记忆足迹![]({52}_Reversible%20Vision%20Transformers@mangalamReversibleVisionTransformers2022.assets/image-20230223111716.png)

。通过权衡 GPU 激活缓存与高效的即时激活重新计算，可逆视觉变换器有效地将激活内存增长与模型深度分离。

虽然自然语言处理社区已经对用于机器翻译的 reversible transformers 进行了一些早期探索 [38]，但这些技术侧重于更长的序列长度而不是深度。我们的实验表明，由于内部子块残差连接导致训练收敛不稳定，vision transformers 直接适应 reversible architectures 无法扩展到更深的模型。在这项工作中，我们重新配置 Vision Transformers (ViT) [15] 和 Multiscale Vision Transformers (MViT) [18] 中的残差路径来克服这个问题。我们进一步发现可逆结构具有更强的固有正则化，因此，我们使用更轻的增强配方（重复增强、增强幅度和随机深度）和残差块之间的横向连接。我们对图像分类和目标检测以及视频分类等图像识别任务进行了广泛的基准测试，在所有这些任务中，reversible vision transformers 与 non-reversible vision transformers 相比具有竞争力的性能，性能衰减可以忽略不计甚至没有。此外，可逆模型具有非常有利的每图像内存占用，在可逆训练的 ViT-Large 模型上节省 15.5 倍，在 MViTLarge 模型上节省 4.5 倍。

Transformers 是一种流行的网络结构，最初被提出用于自然语言应用 [68]，现在广泛应用于深度学习的所有领域，例如强化学习 [7]、语音 [41]、音乐 [32]、多模态学习[35] 最近，在传统视觉任务 [15] 中也是如此。自推出以来，Vision Transformers 得到了热烈的采用，并且被应用于多个视觉识别任务 [15、63、64]，使用先验，例如多尺度特征层次结构 [18、24、49、69、76] 和局部结构建模 [9、14、49]。此外，视觉转换器也被推广用于视频中的动作识别和检测 [1、3、18、49、52、53]。

然而，增大 transformer 模型的一个关键问题是所需的 GPU 内存随深度的增长而增长。内存的这种线性增长阻碍了非常深的模型的开发，因为需要大大减少批量大小才能适应在 GPU 上存储中间激活。这个问题在处理非常大的输入张量的视频模型中更加严重，并且即使对于较浅的深度也经常使用批量大小 1 进行训练。扩展传统变压器架构的潜在系统级解决方案是模型并行性 [10]，它将模型的不同部分放在不同的 GPU 上。然而在实践中，由于巨大的跨设备流量，它非常慢并且需要特殊的高带宽网络基础设施。

在这项工作中，我们使用 Vision Transformers [15] 和 Multiscale Vision Transformers [18] 作为我们的基础模型，并提出了它们的 reversible transformer 版本，将内存需求与模型的深度分离。这有助于节省 GPU 内存，并允许以更高的批次大小进行训练，从而保持甚至增加深度不可逆模型的训练吞吐量。

Reversible Architectures 是一系列基于 NICE [12, 13] reversible transformation 模型的神经网络架构，它们是现代基于生成流的图像生成架构 [30, 37] 的先驱。基于 NICE 的 invertible 变换，Gomez 等人。 [22] 提出了一种 Reversible ResNet 架构，该架构采用 reversible 变换 [12] 在 ResNets [27] 中进行内存高效图像分类。一项有趣的工作建立在可逆 ResNets 思想的基础上，使用 ODE 特征 [6、39、59]、动量 [39、59]、逐层反演 [25]、基于傅里叶变换的反演 [20] 和基于定点迭代的反演 [2, 60]。Reversible CNN 已应用于多种传统图像任务，例如压缩 [46]、重建 [43]、检索 [42] 和去噪 [33、47] 以及压缩感知 [61]、紧凑分辨率 [75]、图像到图像的转换 [67]、遥感 [56]、医学图像分割 [55、74] 和 MRI 重建 [57]。Reversible 变换也适用于其他网络，例如 RNN [51]、Unet [4、16]、Masked 卷积网络 [60] 和 1000 层深度图神经网络 [40]。由 Kiatev 等人发起的一些早期尝试也使 Reversible 转换适应 NLP 领域。 [38] 并在 [78、79] 的基础上进行机器翻译。

然而，词级输入分区包含比补丁级图像分区更丰富的语义内容，并且 NLP transformers 往往深度较浅但通道维度较宽。例如，Kiatev 等人。 [38] 专注于扩展输入序列维度而不是模型深度，并且没有对最大批量大小、峰值 GPU 内存和训练吞吐量进行基准测试。

我们的实验表明，reversible vision transformers 的简单适应对于更深的（≥8 个块）模型表现不佳。这项工作是第一个提出 reversible vision transformers，使其适用于两个最先进的变压器网络，即 ViT 和 MViT。此外，这项工作首次将可逆主干用于对象检测和视频分类，这往往是视觉识别中内存最匮乏的领域之一。


reversible transformer 由一堆可逆块组成，这些可逆块遵循可逆变换的结构，以允许输出的解析可逆性。








考虑一个变换 $T_1$ ，它将输入张量 $I$ 中划分的两个 $d$ 维张量 $\left[I_1 ; I_2\right]$ , 转换为输出张量 $O$ 中划分的两个张量 $\left[O_1 ; O_2\right]$ , 具有任意可微函数 $F(\cdot): \mathbb{R}^d \rightarrow \mathbb{R}^d$ , 如下所示：
$$
\mathbf{I}=\left[\begin{array}{l}
I_1 \\
I_2
\end{array}\right] \underset{T_1}{\longrightarrow}\left[\begin{array}{l}
O_1 \\
O_2
\end{array}\right]=\left[\begin{array}{c}
I_1 \\
I_2+F\left(I_1\right)
\end{array}\right]=\mathbf{O}

\tag{1}
$$
注意，上述变换 $T_1$ 允许逆变换 $T_1^{\prime}$ 使得 $T_1^{\prime} \circ T_1$ 是恒等变换. 

此外，考虑一个使用函数 $G(\cdot): \mathbb{R}^d \rightarrow \mathbb{R}^d$ 的类似转置变换 $T_2$ , 如下所示：
$$
\mathbf{I}=\left[\begin{array}{c}
I_1 \\
I_2
\end{array}\right] \underset{T_2}{\longrightarrow}\left[\begin{array}{l}
O_1 \\
O_2
\end{array}\right]=\left[\begin{array}{c}
I_1+G\left(I_2\right) \\
I_2
\end{array}\right]=\mathbf{O}\tag{2}
$$
与 $T_1$ 类似,  $T_2$ 也允许逆变换 $T_2^{\prime}$ . 现在考虑组合 $T=T_2 \circ T_1$ 它对输入向量 $\mathbf{I}$ 的两个分区进行变换, 获得
$$
\mathbf{I}=\left[\begin{array}{c}
I_1 \\
I_2
\end{array}\right] \underset{T}{\longrightarrow}\left[\begin{array}{l}
O_1 \\
O_2
\end{array}\right]=\left[\begin{array}{c}
I_1+G\left(I_2+F\left(I_1\right)\right) \\
I_2+F\left(I_1\right)
\end{array}\right]=\mathbf{O}\tag{3}
$$
自然地， $T$ 提供逆变换 $T^{\prime}=T_1^{\prime} \circ T_2^{\prime}$ 遵循 $T^{\prime}(T(I))= I$ 。请注意，逆变换 $T^{\prime}$ 仅使用了函数 F 和 G 一次，因此具有相同的作为正向变换 $T$ 的计算成本。



考虑反向传播机制. 给定一个计算图节点 $\mathcal{M}$ , 它的子节点 $\left\{\mathcal{N}_j\right\}$ , 以及子节点相对于最终损失的梯度 $\left\{\frac{d \mathcal{L}}{d \mathcal{N}_j}\right\}$ , 反向传播算法使用链式法则计算关于 $\mathcal{M}$ 的梯度为,
$$
\frac{d \mathcal{L}}{d \mathcal{M}}=\sum_{\mathcal{N}_j}\left(\frac{\partial f_j}{\partial \mathcal{M}}\right)^T \frac{d \mathcal{L}}{d \mathcal{N}_j}\tag{4}
$$
其中 $f_j$ 表示来自其父节点的函数计算节点 $\mathcal{N}_j$ , $\mathcal{M}$ 是其中之一. 雅可比矩阵 $\frac{\partial f_j}{\partial \mathcal{M}}$ , 需要计算 $f_j$ 输出相对于当前节点 $\mathcal{M}$ 的部分梯度.

现在考虑最简单的神经网络层 $f(X)=W^T X$ , 其中 $X$ 是网络内部的中间激活(非输入层的网络输入). 应用上述反向传播算法计算关于父节点的导数, 并使用输出 $Y$ 作为唯一的子节点 $\mathcal{N}_j$ , 我们得到,

$$
\frac{d \mathcal{L}}{d W} =\left(\frac{d \mathcal{L}}{d Y}\right)\left(\frac{d Y}{d W}\right)=\left(\frac{d \mathcal{L}}{d Y}\right) X^T \quad ; \quad\frac{d \mathcal{L}}{d X}=W \frac{d \mathcal{L}}{d Y}\tag{5}
$$
因此，由于函数 jacobian，反向传播算法需要前向传递期间的中间激活，以便在反向传递中可用，以计算相对于权重的梯度。

通常，这是通过在 GPU 内存上缓存中间激活以用于反向传播来实现的。这允许以额外内存为代价进行快速梯度计算。此外，网络的顺序性质要求在计算损失梯度和释放缓存内存之前缓存所有层的激活。这种依赖性会显着影响峰值内存使用量，从而使其与网络深度 $D$ 线性相关。

如上所述，使用可逆变换 T 变换的输入允许根据变换的输出重新计算输入。因此，由这种可逆转换组成的网络不需要存储中间激活，因为它们可以很容易地在输出的反向传递中重新计算。然而，可逆变换 T 对学习函数的属性施加了重要的约束。


Equidimensional Constraint: 函数 $F$ 和 $G$ 在输入和输出空间中需要是等维的。因此，特征维度需要在 $T$ 下保持不变。虽然此约束是其他视觉架构的障碍，例如 ResNets [27] 需要更改特征维度，但它在 Vision Transformer 架构 [15] 中很容易满足，它在整个层中保持恒定的特征维度。

![]({52}_Reversible%20Vision%20Transformers@mangalamReversibleVisionTransformers2022.assets/image-20230223124305.png)



上图显示了适用于 Vision Transformer 架构的可逆转换 $T$ [15]。输入由两个分区张量 $I_1$ 和 $I_2$ 组成，它们根据方程 $(3)$ 进行变换以保持可逆性。这会产生一个双残差流架构，其中每个输入 $I_1$ 和 $I_2$ 都维护自己的残差流，同时使用函数 $F$ 和 $G$ 将信息相互混合。遵循 ViT [15]，我们使用多头注意力和 MLP 分别子锁定为函数 $F$ 和 $G$。


由于 ViT 架构仅使用单个残差流，因此需要修改架构以支持双残差流设计（§3.2.1）。我们提出以下建议：
1. Initiation. 我们保持主干完好无损，并将修补后的输出激活保存到到 I1 和 I2。请注意，此设计选择不同于 [23]，后者建议沿通道尺寸分成两半。
2. Termination. 这两个残差路径需要在最终分类器头之前融合以保留信息。我们建议首先对输入进行层归一化，然后进行连接，以减少融合计算开销。

残余连接在深度网络中的信号传播中起着关键作用 [27]。可逆变换 $T$ 本身也关键地取决于两个流之间的剩余连接以保持可逆性。有趣的是，我们观察到 Reversible Vision Transformer 中残差连接和信号传播之间的关键关系。

### 引文

## 摘录
