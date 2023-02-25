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
lastmod: 2023-02-25 21:56:29
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



具体来说，考虑序列长度为 $L=T \times H \times W$ 的 $D$ 维输入张量 $X$ ,  $X \in \mathbb{R}^{L \times D}$ . 与 MHA [25]一样, MHPA 首先使用线性运算将输入 $X$ 投影到中间查询向量矩阵 $\hat{Q} \in \mathbb{R}^{L \times D}$ , key 向量矩阵 $\hat{K} \in \mathbb{R}^{L \times D}$ 和 value 向量矩阵 $\hat{V} \in$ $\mathbb{R}^{L \times D}$ ,
$$
\hat{Q}=X W_Q \quad \hat{K}=X W_K \quad \hat{V}=X W_V
$$
计算参数矩阵分别为 $W_Q, W_K, W_V$ 的维度均为 $D \times D$  . 然后将获得的中间张量按输入序列的长度进行池化, 池化操作符设为 $\mathcal{P}$ .

Pooling Operator. 在作为下一层输入之前, 中间向量矩阵 $\hat{Q}, \hat{K}, \hat{V}$ 进行的池化操作 $\mathcal{P}(\cdot ; \Theta)$ 进行池化, 这是 MHPA 整体思想的基石, 以及本文多尺度 Transformer 架构的扩展.

池化操作 $\mathcal{P}(\cdot ; \Theta)$ 会沿每个维度对输入张量执行池化计算. 将 $\Theta$ 分解为 $\Theta:=(\mathbf{k}, \mathbf{s}, \mathbf{p})$ , 池化操作会使用维度为 $k_T \times k_H \times k_W$ 的池化核 $\mathbf{k}$   , 每个维度移动大小为 $s_T \times s_H \times s_W$ 的移动步幅 $\mathbf{s}$  和维度为 $p_T \times p_H \times p_W$ 的数值填充矩阵 $\mathbf{p}$ , 将维度为 $\mathbf{L}=T \times H \times W$ 的输入降维到 $\tilde{\mathbf{L}}$ , 坐标计算公式如下所示
$$
\tilde{\mathbf{L}}=\left\lfloor\frac{\mathbf{L}+2 \mathbf{p}-\mathbf{k}}{\mathbf{s}}\right\rfloor+1
$$
最终得到池化后的输出矩阵 $\mathcal{P}(Y ; \Theta) \in \mathbb{R}^{\tilde{L} \times D}$ , 缩小后的序列长度为, $\tilde{L}=\tilde{T} \times \tilde{H} \times \tilde{W}$ .


By default we use overlapping kernels $\mathrm{k}$ with shapepreserving padding $\mathbf{p}$ in our pooling attention operators, so that $\tilde{L}$ , the sequence length of the output tensor $\mathcal{P}(Y ; \Theta)$ , experiences an overall reduction by a factor of $s_T s_H s_W$ .
Pooling Attention. The pooling operator $P(\cdot ; \Theta)$ is applied to all the intermediate tensors $\hat{Q}, \hat{K}$ and $\hat{V}$ independently with chosen pooling kernels $\mathbf{k}$ , stride $\mathbf{s}$ and padding $\mathbf{p}$ . Denoting $\theta$ yielding the pre-attention vectors $Q=\mathcal{P}\left(\hat{Q} ; \Theta_Q\right)$ , $K=\mathcal{P}\left(\hat{K} ; \Theta_K\right)$ and $V=\mathcal{P}\left(\hat{V} ; \Theta_V\right)$ with reduced sequence lengths. Attention is now computed on these shortened vectors, with the operation,
$$
\operatorname{Attention}(Q, K, V)=\operatorname{Softmax}\left(Q K^T / \sqrt{D}\right) V .
$$
Naturally, the operation induces the constraints $\mathbf{s}_K \equiv \mathbf{s}_V$ on the pooling operators. In summary, pooling attention is computed as,
$$
\operatorname{PA}(\cdot)=\operatorname{Softmax}\left(\mathcal{P}\left(Q ; \Theta_Q\right) \mathcal{P}\left(K ; \Theta_K\right)^T / \sqrt{d}\right) \mathcal{P}\left(V ; \Theta_V\right)
$$
where $\sqrt{d}$ is normalizing the inner product matrix row-wise. The output of the Pooling attention operation thus has its sequence length reduced by a stride factor of $s_T^Q s_H^Q s_W^Q$ following the shortening of the query vector $Q$ in $\mathcal{P}(\cdot)$ .

### 引文

## 摘录
