---
title: "UniFormerV2: Spatiotemporal Learning by Arming Image ViTs with Video UniFormer"
description: ""
citekey: liUniFormerV2SpatiotemporalLearning2022
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-12-09 16:43:30
lastmod: 2023-12-09 22:56:02
---

> [!info] 论文信息
>1. Title：UniFormerV2: Spatiotemporal Learning by Arming Image ViTs with Video UniFormer
>2. Author：Kunchang Li, Yali Wang, Yinan He, Yizhuo Li, Yi Wang, Limin Wang, Yu Qiao
>3. Entry：[Zotero link](zotero://select/items/@liUniFormerV2SpatiotemporalLearning2022) [URL link](http://arxiv.org/abs/2211.09552) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Li et al_2022_UniFormerV2.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\3H34AYMS\\2211.html>)
>4. Other：2022 - arxiv:2211.09552     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- :fas_question:   
- :obs_pdf_file:   
- :obs_graph_glyph:   
- :obs_wand_glyph:   

## 摘要

> [!abstract] Learning discriminative spatiotemporal representation is the key problem of video understanding. Recently, Vision Transformers (ViTs) have shown their power in learning long-term video dependency with self-attention. Unfortunately, they exhibit limitations in tackling local video redundancy, due to the blind global comparison among tokens. UniFormer has successfully alleviated this issue, by unifying convolution and self-attention as a relation aggregator in the transformer format. However, this model has to require a tiresome and complicated image-pretraining phrase, before being finetuned on videos. This blocks its wide usage in practice. On the contrary, open-sourced ViTs are readily available and well-pretrained with rich image supervision. Based on these observations, we propose a generic paradigm to build a powerful family of video networks, by arming the pretrained ViTs with efficient UniFormer designs. We call this family UniFormerV2, since it inherits the concise style of the UniFormer block. But it contains brand-new local and global relation aggregators, which allow for preferable accuracy-computation balance by seamlessly integrating advantages from both ViTs and UniFormer. Without any bells and whistles, our UniFormerV2 gets the state-of-the-art recognition performance on 8 popular video benchmarks, including scene-related Kinetics-400/600/700 and Moments in Time, temporal-related Something-Something V1/V2, untrimmed ActivityNet and HACS. In particular, it is the first model to achieve 90% top-1 accuracy on Kinetics-400, to our best knowledge. Code will be available at https://github.com/OpenGVLab/UniFormerV2.

> 学习判别性时空表示是视频理解的关键问题。最近，视觉变换器（ViTs）已经展示了他们在通过自注意力学习长期视频依赖方面的能力。不幸的是，由于在令牌之间进行盲目的全局比较，它们在解决局部视频冗余方面存在局限性。相反，UniFormer 成功地通过将卷积和自注意力统一为 transformer 格式的关系聚合器来缓解了这个问题。然而，在在视频上进行微调之前，这个模型必须需要一段繁琐和复杂的图像预训练阶段，这阻碍了它在实践中的广泛使用。相反，开源的 ViT 已经可以使用，并且在图像监督下进行了充分的预训练。基于这些观察结果，我们提出了一种通用的范例，通过为预训练的 ViTs 配备高效的 UniFormer 设计，来构建一个强大的视频网络系列。我们称之为 UniFormerV 2 系列，因为它继承了 UniFormer 块的简洁风格。但是它包含了全新的局部和全局关系聚合器，通过无缝集成 ViTs 和 UniFormer 的优点，可以实现更适合的准确性计算平衡。没有任何花哨的东西，我们的 UniFormerV 2 在包括与场景相关的 Kinetics-400/600/700 和 Moments in Time，与时间相关的 Something-Something V 1/V 2，未剪辑的 ActivityNet 和 HACS 在内的 8 个流行视频基准上获得了最新的识别性能。特别地，据我们所知，它是第一个在 Kinetics-400 上达到 90% top-1 准确率的模型。代码可在 https://github.com/OpenGVLab/UniFormerV2上获取。

## 预处理

## 概述

## 结果

## 精读

时空表示学习是视频理解中的一个基本任务。最近，视觉变压器（ViTs）在图像领域取得了显著的成功（Dosovitskiy 等，2021 年；Wang 等，2021 b 年；Liu 等，2021 年；Li 等，2022 a 年）。因此，研究者们努力将基于图像的 ViTs 转化为视频建模（Bertasius 等，2021 年；Arnab 等，2021 年；Yan 等，2022 年），通过在时间维度上扩展多头自注意力（MHSA）。然而，这些方法中的时空注意机制主要集中在捕捉全局视频依赖性上，而缺乏处理局部视频冗余的能力。结果就是，在浅层中，这些模型承载了大量的计算负担来编码局部视频表示，导致时空学习中的准确性和效率平衡不尽人意。

为了解决这些问题，研究人员引入了一种简洁的 UniFormer (Li et al., 2022 a)，它以 transformer 的方式将卷积和自注意力统一为多头关系聚合器（MHRA）。
通过分别在浅层和深层模型中建模局部和全局关系，它既可以学习有判别性的时空表示，又可以大大减少计算负担。然而，作为一种新的视频建模架构，UniFormer 在开始阶段没有任何基于图像的预训练。为了获得稳健的视觉表示，它必须经过繁琐的监督预训练阶段，从零开始学习图像，然后再对视频进行微调。或者，我们注意到有各种开源的图像 ViT（Wightman, 2019；Touvron et al., 2021）已经在大规模网络数据集上以丰富的监督形式进行了良好的预训练，例如图像-文本对比学习（Radford et al., 2021）和掩码图像建模（He et al., 2022；Bao et al., 2021）。这些模型在各种视觉任务上具有很强的泛化能力（Luo et al., 2022；Chen et al., 2022；Shen et al., 2021）。因此，我们受到一个自然的问题的启发：我们是否可以将 ViTs 和 UniFormer 的优势整合到视频建模中？

在本文中，我们提出了一种通用的范式来构建一组强大的视频网络，通过将图像预训练的 ViTs 与 UniFormer 的高效视频设计相结合。我们将结果模型称为 UniFormerV 2（图 1），因为它继承了 UniFormer 的简洁风格，但为本地和全局 UniBlocks 配备了新的多头相对位置编码器（MHRA）。在本地 UniBlock 中，我们可以在空间 ViT 块之前灵活地插入一个局部时间 MHRA。在这种情况下，我们既能大大减少时间冗余，又能利用预训练良好的 ViT 块，有效地学习本地时空表示。在全局 UniBlock 中，我们引入了一个基于查询的跨 MHRA。与原始 UniFormer 中昂贵的全局 MHRA 不同，我们的跨 MHRA 可以将所有时空令牌总结为一个视频令牌，以有效地学习全局时空表示。最后，我们将本地和全局的 UniBlocks 重新组织为一个多阶段的融合架构。它可以自适应地整合多尺度时空表示，以捕捉视频中的复杂动态。

我们将我们的范式应用在预训练的 ViTs 上，包括有监督学习、对比学习和掩码图像建模。所有改进的模型在视频分类上表现出良好的性能，展示了我们 UniFormerV 2 的通用属性。此外，我们开发了一个紧凑的 Kinetics-710 基准，将 Kinetics 400/600/700 的动作类别集成在一起，并删除了这些基准的训练集中重复和/或泄漏的视频，以实现公平性（即将训练视频总数从 1.14 M 减少到 0.66 M）。在 K 710 上训练后，我们的模型可以通过仅进行 5 轮微调，在 K 400/600/700 上简单地实现更高的准确性。最后，大量实验证明，我们的 UniFormerV 2 在 8 个流行视频基准上达到了最先进的性能，包括与场景相关的数据集（即 Kinetics-400/600/700 和 Moments in Time），与时间相关的数据集（即 Something-Something V 1/V 2）和未修剪的数据集（即 ActivityNet 和 HACS）。据我们所知，这是第一个在 Kinetics-400 上达到 90.0% top-1准确率的模型。

2 RELATED WORK

Vision Transformer。继自然语言处理中的 Transformer（Vaswani et al.，2017）之后，Vision Transformer（ViT）（Dosovitskiy et al.，2021）在各种视觉任务中取得了巨大的成功，包括目标检测 Carion 等人（2020）；Zhu 等人（2021），语义分割 Xie 等人（2021）；Cheng 等人（2021），低层次图像处理 Liang 等人（2021）；Cui 等人（2022），动作识别 Bertasius 等人（2021）；Arnab 等人（2021），时间定位 Zhang 等人（2022）和多模态学习 Radford 等人（2021）；Wang 等人（2022）。为了使 ViT 更加高效和有效，研究人员以不同的方式引入了尺度和局部建模，例如多尺度架构（Wang 等人，2021 b）；Fan 等人（2021），本地窗口（Liu 等人，2021），早期卷积嵌入（Xiao 等人，2021）；Yuan 等人，2021 a）和卷积位置编码（Chu 等人，2021）；Dong 等人，2022）。或者，UniFormer（Li 等人，2022 a）将卷积和自注意力作为关系聚合器以转换方式统一，从而减少了大规模本地冗余。

视频学习。三维卷积神经网络（CNNs）曾在视频理解中起到主导作用（Tran 等人，2015 年; Carreira＆Zisserman，2017 年）。由于三维 CNN 的困难优化问题，已经做出了很大努力来将三维卷积分解在时空维度（Tran 等人，2018 年; Qiu 等人，2017 年; Feichtenhofer 等人，2019 年）或通道维度（Tran 等人，2019 年; Feichtenhofer，2020 年; Kondratyuk 等人，2021 年）。然而局部感受野限制了三维卷积对长距离依赖关系的捕捉。全局注意力激发了研究人员将图像预训练的 ViTs 转移到视频任务中（Bertasius 等人，2021 年; Neimark 等人，2021年; Zhang, et al., 2021 b; Arnab et al., 2021; Bulat et al., 2021; Patrick et al., 2021). 为了使视频转换器更加高效，之前的研究引入了具有汇聚自我注意力（Fan 等，2021）、本地自我注意力（Liu 等，2022）或统一注意力（Li 等，2022 a）的分层结构。虽然这些新的模型在时间建模方面表现出色，但它们依赖于繁琐的图像预训练。相比之下，各种精心预训练的 ViTs（Wightman，2019）已经开源。在本文中，我们的目标是将高效的 UniFormer 设计扩展到 ViT，将其装备为强大的视频学习者。

3 METHOD

总体框架。我们提出将图像 ViT 与 UniFormer(Li 等人，2022 a)的视频设计相结合，形成 UniFormerV 2。一方面，可以充分利用和保留预训练良好的 ViT 中的空间交互作用以增强空间建模。另一方面，可以灵活地采用高效的 UniFormer 中的分层时间交互作用，以增强时间建模。我们的整体架构如图 2 所示。首先将输入视频投影为令牌，然后通过相应的 UniBlocks 进行局部和全局建模。最后，多阶段融合块将自适应地整合不同阶段的全局令牌，进一步增强视频表示。

![]({61}_UniFormerV2_%20Spatiotemporal%20Learning%20by%20Arming%20Image%20ViTs%20with%20Video%20UniFormer@liUniFormerV2SpatiotemporalLearning2022.assets/image-20231209221700.png)


具体来说，我们首先使用3D 卷积（即3×16×16）将输入视频投影为 L 个时空令牌 $X_{in} \in \mathbb{R}^{L \times C}$ ，其中 L = T × H × W（T，H 和 W 分别表示时间、高度和宽度）。按照原始的 ViT 设计（Dosovitskiy 等，2021），我们进行 16 倍的空间下采样。为了更好地进行时间建模，我们进行 2 倍的时间下采样。接下来，我们构建本地和全局 UniBlocks。对于我们的本地块，我们通过在其之前插入本地时间 MHRA（Li 等，2022 a）来改写基于图像预训练的 ViT 块。在这种情况下，我们既可以有效利用 ViT 的强大空间表示，又可以有效地降低本地时间冗余。此外，我们在每个本地 UniBlock 的顶部引入一个全局 UniBlock，用于捕捉完整的时空依赖关系。为了提高计算效率，我们设计了一种基于查询的交叉 MHRA，用于聚合所有的时空令牌作为全局视频令牌。所有这些具有不同级别全局语义的令牌都进一步融合，用于区分性视频表示。

为了有效地对已经学习到的空间表示进行时间依赖建模，我们提出了一种新的本地 UniBlock，在标准 ViT 块之前插入了一个本地时间 MHRA。

$XT = LT \cdot MHRA (\text{Norm}(X_{\text{in}})) + X_{\text{in}}, \quad (1)$

$XS = GS \cdot MHRA (\text{Norm}(XT)) + XT, \quad (2)$

$XL = FFN (\text{Norm}(XS)) + XS. \quad (3)$

LT MHRA 和 GS MHRA 分别指具有局部时间亲和性和全局空间亲和性的 MHRA。FFN 由两个线性投影组成，中间由 GeLU 分隔（Hendrycks＆Gimpel，2016）。此，在 UniFormer 中进行归一化后（Li 等，2022 a），我们在局部 MHRA 之前采用批量归一化（BN）（Ioffe＆Szegedy，2015），在全局 MHRA 和 FFN 之前采用层归一化（LN）（Ba 等，2016）。请注意，GS MHRAFFN 来自图像预训练的 ViT 块。总体而言，MHRA（Li 等，2022a）通过多头融合学习令牌关系：

$Rn(X) = AnVn(X), \quad (4)$

$MHRA(X) = \text{Concat}(R1(X); R2(X); \dots ; RN(X)) \cup U, \quad (5)$


其中，Rn（·）表示第 n 个头部中的关系聚合器。 An 是描述令牌关系的亲和矩阵，Vn（·）是线性投影，而 U∈RC×C 是可学习的融合矩阵。对于我们的本地 UniBlock，我们插入 LT MHRA 来减少本地时间冗余，与原始 UniFormer（Li 等，2022 a）具有类似的设计思路。因此，LT MHRA 中的亲和性是局部的，具有可学习的参数矩阵 an∈Rt×1×1在时间管 t×1×1中。


$ALT_n(X_i, X_j) = a_{i-j}^n$ , where $j \in \Omega_{t \times 1 \times 1}^i$ .

这样可以有效地学习管中一个标记 Xi 与其他标记 Xj 之间的局部时间关系。或者，GS MHRA 属于原始的 ViT 块。因此，GS MHRA 中的亲和性指的是单帧 1×H×W 中的全局空间自注意。

$AGS_n(X_i, X_j) = \exp\{Q_n(X_i)^T K_n(X_j)\} \sum_{j' \in \Omega_{1 \times H \times W}} \exp\{Q_n(X_i)^T K_n(X_{j'})\}$

其中 Qn(·)和 Kn(·) ∈ RL× C N 是第 n 个头部的不同线性投影。

讨论。 (I) 注意我们本地 UniBlock 中的时空亲和性可以分解为本地时间亲和性 AnLT（公式 6）和全局空间亲和性 AnGS（公式 7）。在这种情况下，我们不仅可以利用 UniFormer 的高效视频处理设计，还可以继承 ViT 有效图像预训练。或者，原始的 UniFormer（Li 等，2022 a）中的本地亲和性是联合时空的，即 Alocaln（Xi，Xj）= ain−j，其中 j 属于一个三维管道 Ωt×h×wi。参数矩阵必须从零开始学习，这不可避免地增加了训练成本。(II) 与 UniFormer 相比，我们在本地 UniBlock 中放弃了其动态位置编码（DPE），因为 ViT 块中的位置编码已经表征了令牌的位置。表 9 b 还显示，本地 UniBlock 的额外 DPE 没有起到帮助作用。（III）我们采用本地亲和力进行时间特征化，而不是像 TimeSformer（Bertasius 等人，2021）那样应用全局时间建模，从而大大减少了 UniFormer 风格中的计算负担，处理了时间冗余。

3.2 GLOBAL UNIBLOCK

为了在时空尺度上明确进行长程依赖性建模，我们在我们的 UniFormerV 2 中引入了一个全局 UniBlock。具体而言，这个全局 UniBlock 包括以下三个基本组件：DPE、MHRA 和 FFN，如下所示。

$XC = DPE(XL) + XL, \quad (8)$

$XST = C \cdot MHRA(\text{Norm}(q), \text{Norm}(XC)), \quad (9)$

$XG = FFN(\text{Norm}(XST)) + XST, \quad (10)$
DPE 被实例化为深度级的时空卷积（Li 等人，2022 a）。我们以交叉注意力的方式设计了全局 C MHRA，以高效地构建视频表示。

$RC_n(q, X) = AC_n(q, X) \cdot V_n(X), \quad (11)$

$CMHRA(q, X) = \text{Concat}(RC_1(q, X); RC_2(q, X); \dots ; RC_N(q, X)) \cup U. \quad (12)$

RnC(q, ·) 是交叉关系聚合器，它可以将可学习的查询 q ∈ R 1×C 转换为视频表征，通过建模该查询 q 与所有时空标记 X 之间的依赖关系。先，它计算交叉亲和矩阵 AnC(q, X) 来学习 q 和 X 之间的关系。
$AC_n(q, X_j) = \frac{\exp\{Q_n(q)^T K_n(X_j)\}}{\sum_{j' \in \Omega_{T \times H \times W}} \exp\{Q_n(q)^T K_n(X_{j'})\}}.$

然后，它使用线性投影将 X 转化为时空上下文 Vn(X)。随后，它将这样的上下文 Vn(X)聚合到可学习的查询中，通过它们之间的关联性 AnC(q, X)进行引导。最后，通过线性投影 U ∈ RC×C，将所有头部的增强查询标记进一步融合为最终的视频表示。注意，查询标记在训练过程中是零初始化的，以确保稳定性。

讨论。我们进一步讨论了我们的全局 UniBlock 与原始 UniFormer（Li 等人，2022 a）的不同设计。（I）我们在本地 UniBlock 之上添加了全局 UniBlock，以令牌形式提取多尺度时空表示。这种设计有助于增强有区别的视频表示，而不会损害预训练架构。（II）典型的全局时空注意力由于其二次复杂度而计算复杂。为了追求更好的准确性-计算平衡，我们在 UniFormerV 2 中引入了一种跨注意力风格的全局 MHRA，从而将计算复杂度从 O(L 2)大幅降低到 O(L)，其中 L 是令牌数量。更重要的是，由于查询 q 是可学习的，它可以自适应地整合来自所有 L 个令牌的时空上下文，以提升视频识别能力。（III）全局 UniBlock 继承了 UniFormer 的 DPE 设计，我们发现它在表9c 中也有帮助。

3.3 MULTI-STAGE FUSION BLOCK

我们提出了一个多阶段融合块，将每个全局 UniBlock 的所有视频令牌集成在一起，如图3所示。为简单起见，我们将第 $i$ 个全局块表示为 $\mathbf{X}_i^G=\mathrm{G}_i\left(\mathbf{q}_i, \mathbf{X}_i^L\right)$ 。给定来自本地 UniBlock 的令牌 $\mathbf{X}_i^L$ ，全局块将可学习查询 $\mathbf{q}$ 转换为视频令牌 $\mathbf{X}_i^G$ 。在本文中，我们探索了四种融合策略来整合所有全局块的视频令牌 $\left\{\mathbf{X}_i^G\right\}_{i=1}^N$ 到最终的视频表示 $\mathbf{F}$ 中，并采用顺序方式进行融合以考虑效果和效率。

![]({61}_UniFormerV2_%20Spatiotemporal%20Learning%20by%20Arming%20Image%20ViTs%20with%20Video%20UniFormer@liUniFormerV2SpatiotemporalLearning2022.assets/image-20231209225104.png)


研究过的融合方法如下：(a) 顺序：我们按顺序使用前一个全局块的视频令牌 $\mathbf{X}_{i-1}^G$ 作为当前全局块 $\mathrm G_i(\cdot)$ 的查询令牌 $\mathbf q_i$ , 其中 $\mathrm G_i(\cdot)= \mathrm G_i (\cdot,\cdot)$ . (b) 并行：我们并行连接所有全局令牌 $\left\{\mathbf X_i ^ G \right\}_{ i = 1 } ^ N$ ，并使用线性投影 $\in R^{N\times C}$ 来获取最终令牌, 其中 $F = Concat(X_1 ^ G,..., X_N ^ G ) U_F$ . (c) 分层 KV: 我们将上一个全球模型生成器（global generator）产生的视觉特征向量作为当前模型生成器（model generator）输入时候上下文信息之一. 即 $X _ i ^ { g } = g _ i ([ x _ { i - 1 } , x _ { l }] )$. (d) 分层 Q: 我们将上一个模型生成器产生的视觉特征向量作为当前模型生成器输入时候查询信息之一. 即 $X _ i ^ { g } = g _ i ([x_{l}, q])$.

最后，我们从本地和全局块中动态地整合最终的标记，从而有效地提高实证研究中的识别性能（表 12）。具体而言，我们从最终的本地 UniBlock 中提取类标记 FC，并通过加权和与视频标记 F 相加，即 Z = αF + (1 − α)FC，其中α是通过 Sigmoid 函数处理可学习参数。

5 CONCLUSION

在本文中，我们提出了一种强大的视频模型，即 UniFormerV 2。它利用图像预训练的 ViTs 和高效的 UniFormer 设计来进行视频学习。通过新颖的局部和全局视频关系聚合器它能够以可控制的复杂度进行有效的时空建模。除了无缝集成 ViTs 和 UniFormer 的优势外，我们还引入了多尺度令牌融合，进一步增强视频表示。根据我们的最佳知识，我们的 UniFormerV 2 在 8 个流行的视频基准上实现了最先进的性能，并首次在 Kinetics-400 上达到了 90%的 top-1 准确率。可重现性。为了确保所有结果可以复现，我们在实验中提供了数据集、模型和训练超参数的详细信息（参见表 10 和表 11）。对于 Kinetics 710，我们在表 20 中提供了其标签列表供复现。所有代码都基于 UniFormer（Li et al., 2022b）存储库。

### 引文

## 摘录
