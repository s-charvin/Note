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
lastmod: 2023-02-25 22:25:44
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

基于 Multi Head Pooling Attention（第 3.1 节），我们描述了专门使用 MHPA 和 MLP 层进行视觉表示学习的多尺度 Transformer 模型。首先，我们简要回顾了为我们的设计提供信息的 Vision Transformer 模型。



### 引文

## 摘录
