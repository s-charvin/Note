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
lastmod: 2023-02-25 22:41:42
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

- 在这篇文章中，作者提出了两种不同的方法来帮助 DL 网络更有效地收敛，即添加智能训练样本和参考样本方法 。
- 在这篇文章中，作者使用了一种贪心算法来选择智能训练样本和参考样本。这种算法可以应用于训练和参考样本的选择。通过比较随机选择和基于贪心算法的选择策略，作者发现基于贪心算法的选择策略对于训练样本和参考样本都具有显著优势。 
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



具体来说，考虑序列长度为 $L=T \times H \times W$ 的 $D$ 维输入张量 $X$ ,  $X \in \mathbb{R}^{L \times D}$ . 与 MHA [25]一样, MHPA 首先使用线性运算将输入 $X$ 投影到中间查询张量 $\hat{Q} \in \mathbb{R}^{L \times D}$ , key 张量 $\hat{K} \in \mathbb{R}^{L \times D}$ 和 value 张量 $\hat{V} \in$ $\mathbb{R}^{L \times D}$ ,
$$
\hat{Q}=X W_Q \quad \hat{K}=X W_K \quad \hat{V}=X W_V
$$
计算参数矩阵分别为 $W_Q, W_K, W_V$ 的维度均为 $D \times D$  . 然后将获得的中间张量 $\hat{Q}, \hat{K}, \hat{V}$ 按输入序列的长度进行池化, 池化操作符设为 $\mathcal{P}$ .

在作为下一层输入之前, 中间向量矩阵 $\hat{Q}, \hat{K}, \hat{V}$ 进行的池化操作 $\mathcal{P}(\cdot ; \Theta)$ 是 MHPA 整体思想的基石, 以及本文多尺度 Transformer 架构的扩展.

池化操作 $\mathcal{P}(\cdot ; \Theta)$ 会沿每个维度对输入张量使用池化核  $\Theta$  执行计算.  $\Theta$ 可以进一步分解为 $\Theta:=(\mathbf{k}, \mathbf{s}, \mathbf{p})$ , 即池化操作会使用维度为 $k_T \times k_H \times k_W$ 的池化窗口 $\mathbf{k}$   , 每个维度移动大小为 $s_T \times s_H \times s_W$ 的移动步幅 $\mathbf{s}$  和维度为 $p_T \times p_H \times p_W$ 的数值填充矩阵 $\mathbf{p}$ , 将维度为 $\mathbf{L}=T \times H \times W$ 的输入降维到 $\tilde{\mathbf{L}}$ , 坐标计算公式如下所示
$$
\tilde{\mathbf{L}}=\left\lfloor\frac{\mathbf{L}+2 \mathbf{p}-\mathbf{k}}{\mathbf{s}}\right\rfloor+1
$$
最终得到池化后的输出矩阵 $\mathcal{P}(Y ; \Theta) \in \mathbb{R}^{\tilde{L} \times D}$ , 缩小后的序列长度为, $\tilde{L}=\tilde{T} \times \tilde{H} \times \tilde{W}$ . 默认情况下，在池化操作中会使用带有方便输出保持形状的填充 $\mathbf{p}$ 的池化核 $\mathrm{k}$ ，因此 $\tilde{L}$ 的输出张量 $\mathcal{ P}(Y ; \Theta)$ 中的序列长度 $\tilde{\mathbf{L}}$ 整体刚好减少了 $s_T s_H s_W$ 步幅倍。


The pooling operator $P(\cdot ; \Theta)$ is applied to all the intermediate tensors $\hat{Q}, \hat{K}$ and $\hat{V}$ independently with chosen pooling kernels $\mathbf{k}$ , stride $\mathbf{s}$ and padding $\mathbf{p}$ . Denoting $\theta$ yielding the pre-attention vectors $Q=\mathcal{P}\left(\hat{Q} ; \Theta_Q\right)$ , $K=\mathcal{P}\left(\hat{K} ; \Theta_K\right)$ and $V=\mathcal{P}\left(\hat{V} ; \Theta_V\right)$ with reduced sequence lengths. Attention is now computed on these shortened vectors, with the operation,

通过池化操作 $P(\cdot ; \Theta)$ , 使用指定的池核 $\mathbf{ k}$ ，步长 $\mathbf{s}$ 和填充 $\mathbf{p}$ 处理过所有中间张量 $\hat{Q}, \hat{K}$ 和 $\hat{V}$ 后, 会得到预注意张量 $Q=\mathcal{P}\left(\hat{Q} ; \Theta_Q\right)$ , $K=\mathcal{P}\left(\hat{K } ; \Theta_K\right)$ 和 $V=\mathcal{P}\left(\hat{V} ; \Theta_V\right)$ , 这样减少了张量的序列长度。然后在这些缩小后的张量上计算注意力，通过如下操作，
$$
\operatorname{Attention}(Q, K, V)=\operatorname{Softmax}\left(Q K^T / \sqrt{D}\right) V .
$$

自然地，该操作会在前面池化操作上引入参数约束 $\mathbf{s}_K \equiv \mathbf{s}_V$ , 完整的池化注意力操作, 可用如下公式表述:
$$
\operatorname{PA}(\cdot)=\operatorname{Softmax}\left(\mathcal{P}\left(Q ; \Theta_Q\right) \mathcal{P}\left(K ; \Theta_K\right)^T / \sqrt{d}\right) \mathcal{P}\left(V ; \Theta_V\right)
$$
其中 $\sqrt{d}$ 是按行规范化内积矩阵。因此，在使用池化操作 $\mathcal{P}(\cdot)$ 后, 查询张量 $Q$ 被缩短，后面的注意操作后的输出的序列长度, 同样的也减少了步幅因子 $s_T^Q s_H^Q s_W^Q$ 倍数。

与 [98] 中一样，可以通过考虑 $h$ 个注意力操作头来并行化计算，其中每个注意力头都仅在 $D$ 维输入张量 $X$ 中的 $D/h$ 维的非重叠通道子集上执行注意力操作。

由于池化注意力计算, 池化了 key, query 和 value 张量, 缩小了 w.r.t. 的序列长度, 这样对多尺度 Transformer 模型的基本计算和内存需求具有非常明显好处。用 $f_Q、f_K$ 和 $f_V$ 表示序列长度缩减因子， $$ f_j=s_T^j \cdot s_H^j \cdot s_W^j, \forall j \in\{Q, K, V\} 。 $$ 考虑到 $\mathcal{P}(; \Theta)$ 的输入张量具有维度 $D \times T \times H \times W$ ，MHPA 的运行时复杂度为 
$O\left(T H W D / h\left(D+T H W / f_Q f_K\right)\right)$ 每个头，内存复杂度为 $O\left(T H W h\left(D / h+T H W / f_Q f_K\right)\right)$ 。通道数 $D$ 和序列长度项 $T H W / f_Q f_K$ 之间的这种权衡告知我们关于架构参数的设计选择，例如头数和层宽。我们建议读者参阅补充资料，了解有关时间记忆复杂性权衡的详细分析和讨论。

Vision Transformer (ViT) 架构 [25] 首先将分辨率为 $T × H × W$ 的输入视频切割成大小为 1×16×16 的非重叠块，其中 $T$ 是帧数, $H$ 是高度， $W$ 是宽度，然后在扁平图像块上逐点应用线性层，以将它们投射到 Transformer 的潜在维度 $D$ 中。这等效于具有内核大小和步长大小为 1×16×16 的卷积。

接下来，将位置张量 $E ∈ R^{L×D}$ 添加到被投影后的每个序列长度为 L , 特征维度大小为 D 的元素中, 编码位置信息并打破置换不变性。


本文的关键思想是逐步增加通道分辨率（即维度），同时降低整个网络的时空分辨率（即序列长度）。通过设计，我们的 MViT 架构在早期层具有良好的时空（和粗通道）分辨率，在后期层中被上/下采样为粗时空（和细通道）分辨率。 MViT 如表 2 所示。


Scale stages。一个尺度级被定义为一组 N 个变换器块，它们在相同的尺度上运行，跨通道和时空维度 D×T ×H×W 具有相同的分辨率。在输入端（表 2 中的立方体 1），我们将补丁（或立方体，如果它们具有时间范围）投影到较小的通道维度（例如，比典型的 ViT 模型小 8 倍），但长序列（例如 4×4 =比典型的 ViT 模型密度高 16 倍；参见表 1）。

在阶段转换（例如表 2 中的 scale1 到 scale2 到 scale2），处理序列的通道维度被上采样，而序列的长度被下采样。这有效地降低了底层视觉数据的时空分辨率，同时允许网络将处理后的信息吸收到更复杂的特征中。


Channel expansion. 当从一个阶段过渡到下一个阶段时，我们通过将前一阶段中最终 MLP 层的输出增加一个与该阶段引入的分辨率变化相关的因子来扩展通道维度。具体来说，如果我们将时空分辨率下采样 4 倍，我们就会将通道维度增加 2 倍。例如，scale3 到 scale4 将分辨率从 2D× T sT × H 8 ×T 8 更改为表 2 中的 4D× T sT × H 16 × T 16。这大致保留了跨阶段的计算复杂度，类似于 ConvNet 设计原则[87, 45]。

Query pooling. 集中注意操作不仅在键和值向量的长度方面而且在查询的长度方面提供了灵活性，从而在输出序列方面提供了灵活性。将查询向量 P(Q; k; p; s) 与内核 s ≡ (sQ T , sQ H , sQ W ) 合并会导致序列缩减 sQ T · sQ H · sQ W 倍数。因为，我们的目的是在一个阶段的开始降低分辨率，然后在整个阶段保持这个分辨率，所以只有每个阶段的第一个池注意力操作符以非退化查询步幅 sQ > 1 运行，所有其他操作符都被限制为 sQ ≡ (1, 1, 1)。

Key-Value pooling.  与查询池不同，改变键 K 和值 V 张量的序列长度，不会改变输出序列长度，因此不会改变时空分辨率。然而，它们在集中注意算子的整体计算要求中起着关键作用。我们分离了 K、V 和 Q 池化的使用，Q 池化用于每个阶段的第一层，K、V 池化用于所有其他层。由于键和值张量的序列长度需要相同才能计算注意力权重，因此用于 K 和值 V 张量的池化步长需要相同。在我们的默认设置中，我们将所有池化参数 (k; p; s) 约束为相同，即 ΘK ≡ ΘV 在一个阶段内，但自适应地改变 s w.r.t.到跨阶段的规模。

Skip connections.   由于通道维度和序列长度在残差块内发生变化，我们池化跳跃连接以适应其两端之间的维度不匹配。 MHPA 通过将查询池运算符 P(·; ΘQ) 添加到残差路径来处理这种不匹配。如图 3 所示，我们不是直接将 MHPA 的输入 X 添加到输出，而是将池化的输入 X 添加到输出，从而将分辨率与参与查询 Q 相匹配。为了处理阶段变化之间的通道维度不匹配，我们使用一个额外的线性层，该层对我们的 MHPA 操作的层归一化输出进行操作。请注意，这与对非标准化信号进行操作的其他（保留分辨率）跳过连接不同。

表 3 显示了 Vision Transformers [25] 和我们的多尺度 Vision Transformers 基本模型的具体实例。 ViT-Base [25]（表 3b）最初将输入投射到形状为 1×16×16 且尺寸为 D = 768 的贴片，然后堆叠 N = 12 个变压器块。对于 8×224×224 输入，所有层的分辨率固定为 768×8×14×14。序列长度（时空分辨率 + 类标记）为 8 · 14 · 14 + 1 = 1569。我们的 MViT-Base（表 3b）由 4 个尺度阶段组成，每个阶段都有几个通道维度一致的变换器块。 MViT-B 最初将输入投影到 D = 96 的通道维度，具有形状为 3×7×7 的重叠时空立方体。对于每个附加阶段，长度为 8 * 56 * 56 + 1 = 25089 的结果序列减少了 4 倍，最终序列长度为 8 * 7 * 7 + 1 = 393 在 scale4。同时，通道维度在每个阶段被上采样 2 倍，在 scale4 增加到 768。请注意，所有池化操作以及分辨率下采样仅在数据序列上执行，而不涉及已处理的类标记嵌入。我们在 scale1 阶段将 MHPA 头数设置为 h = 1，并随着通道尺寸增加头数（每头 D/h 的通道数保持在 96）。在每个阶段转换中，前一阶段的输出 MLP 维度增加 2 倍，并且 MHPA 池化在 Q 张量上，其中 sQ = (1, 2, 2) 在下一阶段的输入。


我们在所有 MHPA 块中使用 K、V 池化，其中 ΘK ≡ ΘV 和 sQ = (1, 8, 8) in scale1 并自适应地衰减此步幅 w.r.t.跨阶段的比例，使得 K、V 张量在所有块中具有一致的比例。

### 引文

## 摘录
