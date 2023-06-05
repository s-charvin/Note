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
date: 2023-06-05 19:22:39
lastmod: 2023-06-05 22:31:18
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

> 与近年来大规模视觉转换器 (ViTs) 的巨大进步相比，基于卷积神经网络 (CNN) 的大规模模型仍处于早期状态。这项工作提出了一种新的基于 CNN 的大规模基础模型，称为 InternImage，它可以从增加参数和训练数据（如 ViTs）中获得收益。不同于最近关注大密集核的 CNN，InternImage 以**可变形卷积**为核心算子，使我们的模型不仅具有检测和分割等下游任务所需的大有效感受野，而且具有自适应空间聚合以输入和任务信息为条件。因此，所提出的 InternImage 减少了传统 CNN 的严格归纳偏差，并使得从 ViT 等海量数据中学习具有大规模参数的更强、更鲁棒的模式成为可能。我们模型的有效性在具有挑战性的基准测试中得到了证明，包括 ImageNet、COCO 和 ADE20K。值得一提的是，InternImage-H 在 COCO test-dev 上取得了 65.4 mAP 的新纪录，在 ADE20K 上取得了 62.9 mIoU 的新纪录，优于当前领先的 CNN 和 ViT。

## 预处理

## 概述

基于可变形卷积, 设计了一个

## 结果

## 精读

随着 transformers 在大规模语言模型[3-8]中取得的显著成功，vision transformers（ViTs）[2, 9-15]也席卷了计算机视觉领域，正成为大规模语言模型研究和实践的首选。视觉基础模型。一些先驱 [16–20] 已经尝试将 ViT 扩展到具有超过 10 亿个参数的超大型模型，击败卷积神经网络 (CNN) 并显着推动各种计算机视觉任务的性能限制，包括基本的分类、检测和分割。虽然这些结果表明 CNN 在海量参数和数据时代不如 ViT，但我们认为基于 CNN 的基础模型在配备了类似的操作员/架构级设计、扩展参数和海量数据情况下也可以实现与 ViT 相当甚至更好的性能。

为了弥合 CNN 和 ViT 之间的差距，我们首先从两个方面总结它们的差异：(1) 从算子级别 [9, 21, 22]，ViT 的多头自注意力 (MHSA) 具有长程依赖性和自适应空间聚合（见图1（a））。受益于灵活的 MHSA，ViT 可以从海量数据中学习比 CNN 更强大、更稳健的表征。 (2) 从体系结构的角度来看[9,22,23]，除了MHSA，ViTs还包含一系列标准CNNs中没有的高级组件，如层归一化(LN)[24]、前馈网络(FFN) ) [1]、GELU [25] 等。尽管最近的工作 [21, 22] 通过使用具有非常大内核（例如 31×31）的密集卷积对将长程依赖性引入 CNN 进行了有意义的尝试，如中所示图 1（c），在性能和模型规模方面与最先进的大规模 ViTs [16, 18-20, 26] 仍有相当大的差距。

在这项工作中，我们专注于设计一个基于 CNN 的基础模型，该模型可以有效地扩展到大规模参数和数据。具体来说，我们从灵活的卷积变体开始——可变形卷积 (DCN) [27, 28]。通过将其与一系列类似于 transformer 的定制块级和架构级设计相结合，我们设计了一个全新的卷积骨干网络，称为 InternImage。

![]({58}_InternImage_%20Exploring%20Large-Scale%20Vision%20Foundation%20Models%20with%20Deformable%20Convolutions@wangInternImageExploringLargeScale2023.assets/image-20230605193829.png)


如图所示，与最近改进的具有非常大内核（例如 31×31 [22]）的 CNN 不同，InternImage 的核心运算符是一个动态稀疏卷积，其公共窗口大小为 3×3，（1）其采样偏移量可以灵活地从给定数据中动态学习适当的接受域（可以是长程或短程）； (2) 采样偏移量和调制标量根据输入数据自适应调整，可以像ViTs一样实现自适应空间聚合，减少正则卷积的过度归纳偏差； (3) 卷积窗口是一个普通的 3×3，避免了大密集内核带来的优化问题和昂贵的成本 [22, 29]。

通过上述设计，所提出的 InternImage 可以有效地扩展到大参数大小并从大规模训练数据中学习更强的表示，在广泛的视觉范围内实现与大规模 ViTs [2、11、30] 相当甚至更好的性能任务。总之，我们的主要贡献如下：

(1) 我们提出了一种新的基于 CNN 的大规模基础模型——InternImage。据我们所知，它是第一个有效扩展到超过 10 亿个参数和 4 亿张训练图像的 CNN，并实现了与最先进的 ViTs 相当甚至更好的性能，表明卷积模型也是一个值得探索的模型大尺度模型研究方向。

(2) 我们成功地通过使用改进的 3×3 DCN 算子引入远程依赖和自适应空间聚合将 CNN 扩展到大规模设置，并探索以算子为中心的定制基本块、堆叠规则和缩放策略。这些设计有效地利用了运算符，使我们的模型能够从大规模参数和数据中获得收益。

(3) 我们在图像分类、目标检测、实例和语义分割等代表性视觉任务上评估了所提出的模型，并通过将模型大小从 3000 万扩展到最先进的 CNN 和大规模 ViT 进行了比较到10亿，数据从100万到4亿不等。具体来说，我们具有不同参数大小的模型可以始终优于 ImageNet [31] 上的现有技术。 InternImageB 仅在 ImageNet-1K 数据集上训练就达到了 84.9% 的 top-1 准确率，比基于 CNN 的对应 [21、22] 至少高出 1.1 个百分点。借助大规模参数（即 10 亿）和训练数据（即 4.27 亿），InternImage-H 的 top-1 准确率进一步提升至 89.6%，接近良好工程 ViTs [2, 30]和混合 ViTs [20]。此外，在具有挑战性的下游基准 COCO [32] 上，我们最好的模型 InternImage-H 以 21.8 亿个参数实现了最先进的 65.4% box mAP，比 SwinV2-G [16] 高 2.3 个百分点（65.4 比. 63.1) 参数减少了 27%，如图 所示。

相关工作

在大规模数据集和计算资源可用之后，卷积神经网络（CNN）成为视觉识别的主流。受 AlexNet [33] 的影响，许多更深更有效的神经网络架构被提出，例如 VGG [34]、GoogleNet [35]、ResNet [36]、ResNeXt [37]、EfficientNet [38、39] 等. 除了架构设计之外，还制定了更复杂的卷积操作，例如深度卷积 [40] 和可变形卷积 [27, 28]。通过考虑变压器的先进设计，现代 CNN 通过在宏观/微观设计中发现更好的组件并引入具有长程依赖性 [21、41-43] 或动态权重 [44] 的改进卷积，在视觉任务上表现出了良好的性能。近年来，一种新的视野基础模型侧重于基于变压器的架构。 ViT [9] 是最具代表性的模型，由于全局感受野和动态空间聚合，它在视觉任务中取得了巨大成功。然而，ViT 中的全局注意力受到昂贵的计算/内存复杂性的影响，尤其是在大型特征图上，这限制了它在下游任务中的应用。为了解决这个问题，PVT [10, 11] 和 Linformer [45] 对下采样的键和值映射进行了全局关注，DAT [46] 使用可变形的注意力来从值映射中稀疏采样信息，而 HaloNet [47] 和 Swin transformer [2] 开发了局部注意力机制，并使用晕轮和移位操作在相邻局部区域之间传递信息。大型模型。放大模型是提高特征表示质量的重要策略，这在自然语言处理 (NLP) 领域已得到充分研究 [48]。受到 NLP 领域成功的启发，Zhai 等人。 [19] 首先将 ViT 扩展到 20 亿个参数。刘等人。 [16] 将层次结构 Swin transformer 扩大到更深更宽的模型，有 30 亿个参数。一些研究人员通过结合 ViTs 和 CNNs 在不同层次的优势，开发了大规模混合 ViTs [20, 49]。最近，BEiT-3 [17] 使用多模态预训练进一步探索了基于 ViT 的具有大规模参数的更强表示。这些方法显着提高了基本视觉任务的上限。然而，基于 CNN 的大规模模型的研究在参数总数和性能方面落后于基于 Transformer 的架构。尽管新提出的 CNN [21, 41–43] 通过使用具有非常大内核的卷积或递归门控内核引入了长程依赖性，但与最先进的 ViT 仍然存在相当大的差距。在这项工作中，我们的目标是开发一个基于 CNN 的基础模型，该模型可以有效地扩展到与 ViT 相当的大规模。


方法介绍

为了设计一个大规模的基于 CNN 的基础模型，我们从一个灵活的卷积变体开始，即可变形卷积 v2 (DCNv2) [28] 并做一些在此基础上进行调整，以更好地适应大型基础模型的要求。然后，我们通过将调谐卷积运算符(tuned convolution operator)与现代骨干网中使用的 advanced block 设计相结合来构建 basic block [16, 19]。最后，我们探索基于 DCN 的块的堆叠和缩放原理，以构建一个可以从海量数据中学习强表示的大规模卷积模型。

方法介绍: 可变形卷积 v3

卷积(CNN)与多头自注意力(MHSA)。以前的作品 [21、22、50] 已经广泛讨论了 CNN 和 ViT 之间的差异。在决定 InternImage 的核心算子之前，我们先总结一下标准 convolution 和 MHSA 的主要区别。

(1) 远程依赖建模能力(Long-range dependencies)。尽管人们早就认识到具有较大有效感受野（长程依赖性）的模型通常在下游视觉任务上表现更好 [51–53]，但实际上 CNN 的有效感受野 [34, 36] 通常堆叠的 3×3 大小的标准卷积核大小很小, 即使使用非常深的模型，基于 CNN 的模型仍然无法获得像 ViTs 这样的远程依赖构建能力，这限制了它的性能。

(2) 自适应空间聚合能力(Adaptive spatial aggregation). 与权重由输入动态调节的 MHSA 相比，常规卷积 [54] 是一种具有静态权重和强归纳偏差（例如 2D 局部性、邻域结构、平移等价性等）的算子(常规卷积假设输入数据中的局部性、邻域结构和平移等价性等特征是重要的，并且使用静态的权重进行特征提取。)。凭借高度归纳的特性，由常规卷积组成的模型可能比 ViT 收敛得更快并且需要更少的训练数据，但它也限制了 CNN 从网络规模数据中学习更通用和更稳健的模式。

可变形卷积 DCN v2. 

为了弥补卷积和 MHSA 之间差距的一种直接方法是将远程依赖和自适应空间聚合引入常规卷积中。DCNv2 [28] 是常规卷积的一般变体, 给定输入 $x ∈ R^{C×H×W}$ 和当前像素 $p_0$，DCNv2 可以表示为：

![]({58}_InternImage_%20Exploring%20Large-Scale%20Vision%20Foundation%20Models%20with%20Deformable%20Convolutions@wangInternImageExploringLargeScale2023.assets/image-20230605194425.png)


其中 K 表示采样点总数，k 为采样点枚举。 $w_{k}∈R^{C×C}$ 表示第 k 个采样点的投影权重， $m_k∈R$ 表示第 k 个采样点的调制标量，用 sigmoid 函数归一化。 $p_k$ 表示预定义网格采样的第 k 个位置 {(−1, −1), (−1, 0), ..., (0, +1), ..., (+1, + 1)} 与常规卷积一样， $Δp_k$ 是对应于第 k 个网格采样位置的偏移量。我们从等式中看到 (1) 对于长程依赖，采样偏移量 $Δp_k$ 是灵活的并且能够与短程或远程特征交互； (2) 对于自适应空间聚合，采样偏移量 $Δp_k$ 和调制标量 $m_k$ 都是可学习的，并由输入 x 调节。因此可以发现 DCNv2 与 MHSA 具有相似的有利特性，这促使我们在此算子的基础上开发基于 CNN 的大规模基础模型。

为 Vision Foundation 模型扩展 DCNv2。在通常的实践中，DCNv2通常被用作常规卷积的扩展，加载常规卷积的预训练权重并进行微调以获得更好的性能，这并不完全适合需要从头开始训练的大规模视觉基础模型.在这项工作中，为了解决这个问题，我们从以下几个方面扩展了 DCNv2：

(1) 在卷积神经元之间共享权重。与常规卷积类似，原始 DCNv2 中的不同卷积神经元 1 具有独立的线性投影权重，因此其参数和内存复杂度与采样点总数成线性关系，这极大地限制了模型的效率，尤其是在大规模模型中。为了解决这个问题，我们借鉴了可分离卷积 [55] 的思想，并将原始卷积权重 wk 分离为深度部分和点部分，其中深度部分由原始位置感知调制标量 mk 负责，逐点部分是采样点之间共享的投影权重 w。

(2)引入多组机制。多组（头）设计最早出现在组卷积[33]中，广泛应用于 transformer 的 MHSA[1]中，与自适应空间聚合一起有效地从不同位置的不同表示子空间中学习更丰富的信息。受此启发，我们将空间聚合过程分成 G 个组，每个组都有单独的采样偏移量 Δpgk 和调制尺度 mgk，因此单个卷积层上的不同组可以有不同的空间聚合模式，从而为下游提供更强的特征任务。

(3) 沿采样点归一化调制标量。原始 DCNv2 中的调制标量由 sigmoid 函数按元素归一化。因此，每个调制标量都在[0, 1]范围内，所有样本点的调制标量之和不稳定，在0到 K 之间变化。这导致在大规模训练时 DCNv2层的梯度不稳定参数和数据。为了缓解不稳定问题，我们将 element-wise sigmoid 归一化更改为沿样本点的 softmax 归一化。这样，调制标量的和被约束为1，使得模型在不同尺度下的训练过程更加稳定。

结合上述修改，扩展的 DCNv2，标记为 DCNv3，可以表示为 Eqn。 (2).

![]({58}_InternImage_%20Exploring%20Large-Scale%20Vision%20Foundation%20Models%20with%20Deformable%20Convolutions@wangInternImageExploringLargeScale2023.assets/image-20230605194558.png)

其中 G 表示聚合组的总数。对于第g组，wg∈RC×C′表示组的位置无关投影权重，其中C′=C/G表示组维度。 mgk ∈ R 表示第 g 组中第 k 个采样点的调制标量，由 softmax 函数沿维度 K 归一化。 xg ∈ RC′×H×W 表示切片输入特征图。 Δpgk 为第 g 组中网格采样位置 pk 对应的偏移量。


总的来说，DCNv3作为DCN系列的扩展，具有以下三个优点：（1）该算子弥补了常规卷积在长程依赖和自适应空间聚合方面的不足； (2) 与常见的 MHSA 和密切相关的可变形注意力 [46, 56] 等基于注意力的算子相比，该算子继承了卷积的归纳偏差，使我们的模型更高效，训练数据更少，训练时间更短； (3) 该算子基于稀疏采样，比以前的方法如 MHSA [1] 和重新参数化大内核 [22] 具有更高的计算和内存效率。 此外，由于采样稀疏，DCNv3只需要一个3×3的核来学习长程依赖，更容易优化，避免了大核中使用的重新参数化[22]等额外的辅助技术。

方法介绍: InternImage Model

使用 DCNv3作为核心算子带来了一个新的问题：如何构建一个能够有效利用核心算子的模型？在本节中，我们首先介绍模型的基本块和其他整体层的细节，然后通过探索为这些基本块量身定制的堆叠策略，构建一个名为 InternImage 的新的基于 CNN 的基础模型。最后，我们研究了所提出模型的放大规则，以获得增加参数的增益。

使用 DCNv3作为核心算子带来了一个新的问题：如何构建一个能够有效利用核心算子的模型？在本节中，我们首先介绍模型的基本块和其他整体层的细节，然后通过探索为这些基本块量身定制的堆叠策略，构建一个名为 InternImage 的新的基于 CNN 的基础模型。最后，我们研究了所提出模型的放大规则，以获得增加参数的增益。

Basic block. 

与传统 CNN [36] 中广泛使用的瓶颈不同，我们的基本块的设计更接近 ViTs，它配备了更高级的组件，包括 LN [24]、前馈网络 (FFN) [1] 和 GELU [ 25]。这种设计在各种视觉任务中被证明是有效的 [2, 10, 11, 21, 22]。我们的基本块的细节如图 3 所示，其中核心运算符是 DCNv3，通过将输入特征 x 通过可分离卷积（3×3 深度卷积，然后是线性投影）。对于其他组件，我们默认使用后归一化设置 [57]，并遵循与普通变压器 [1、9] 相同的设计。

Stem & downsampling layers.

为了获得分层特征图，我们使用卷积干和下采样层将特征图调整为不同的比例。如图 3 所示，stem 层放置在第一阶段之前，将输入分辨率降低 4 倍。它由两个卷积、两个LN层和一个GELU层组成，其中两个卷积的核大小为3，步幅为2，填充为1，第一个卷积的输出通道是第二个的一半.类似地，下采样层由步幅为 2、填充为 1 的 3×3 卷积组成，后面是一个 LN 层。它位于两个阶段之间，用于将输入特征图下采样 2 倍。

Stacking rules.

为了阐明块堆叠过程，我们首先列出 InternImage 的积分超参数: Ci：第 i 级的通道号； Gi：第 i 阶段 DCNv3的组号； Li：第 i 阶段的基本块数。

由于我们的模型有 4 个阶段，一个变体由 12 个超参数决定，其搜索空间太大而无法穷举并找到最佳变体。为了减少搜索空间，我们将现有技术[2,21,36]的设计经验总结为4条规则，如图3所示，其中第一条规则使后三级的通道数由通道数C1决定第一阶段的，第二个规则让组号对应于阶段的通道数。对于不同阶段的堆叠块数，我们将堆叠模式简化为“AABA”，即第1、2、4阶段的块数相同，且不大于第3阶段的块数，如图所示最后两条规则。使用这些规则，可以仅使用 4 个超参数（C1、C'、L1、L3）来定义一个 InternImage 变体。

让我们选择一个具有 3000 万个参数的模型作为原点，并将 C1 离散化为 {48, 64, 80}，将 L1 离散化为 {1, 2, 3, 4, 5}，将 C' 离散化为 {16, 32}。这样，原来巨大的搜索空间减少到 30 个，我们可以在 ImageNet [31] 中通过训练和评估从这 30 个变体中找到最好的模型。在实践中，我们使用最佳超参数设置（64、16、4、18）来定义原始模型并将其缩放到不同的尺度。

Scaling rules.

基于上述约束下的最优原点模型，我们进一步探索受[38]启发的参数缩放规则。具体来说，我们考虑两个缩放维度：深度 D（即 3L1 +L3）和宽度 C1，并使用 α、β 和复合因子 φ 缩放这两个维度。缩放规则可以写为：D′ = αφD 和 C′ 1 = βφC1，其中 α ≥ 1，β ≥ 1，αβ1.99 ≈ 2。这里，1.99 是 InternImage 特有的，通过将模型宽度和保持深度不变。我们通过实验发现最佳缩放设置为α = 1.09和β = 1.36，然后我们以此为基础构建具有不同参数尺度的 InternImage 变体，即 InternImage-T/S/B/L/XL，其复杂度相似到 ConvNeXt [21] 的那些。为了进一步测试能力，我们用 10 亿构建了一个更大的 InternImage-H 参数，并且为了适应非常大的模型宽度，我们还将组维度 C' 更改为 32。配置总结在表 1 中。

### 引文

## 摘录
