---
title: ""
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-04-17 14:17:18
lastmod: 2022-06-07 10:34:20
---

# 重点

- 论文源文件
- [开源代码](https://github.com/AmirSh15/Compact_SER)
- 第一个将图分类方法用于SER的工作。
- 利用图信号处理的理论，提出了一种基于GCN的图分类方法，该方法可以有效地执行精确的图卷积。
- 模型可训练参数显著减少(仅为30K)。
- IEMOCAP 自带 spontaneity 特征

思考：
- 图结构可以捕捉语音情感的动态特性吗？

# 摘要

We propose a deep graph approach to address the task of speech emotion recognition. A compact, efficient and scalable way to represent data is in the form of graphs. Following the theory of graph signal processing, we propose to model speech signal as a cycle graph or a line graph. Such graph structure enables us to construct a Graph Convolution Network (GCN)-based architecture that can perform an accurate graph convolution in contrast to the approximate convolution used in standard GCNs. We evaluated the performance of our model for speech emotion recognition on the popular IEMOCAP and MSP-IMPROV databases. Our model outperforms standard GCN and other relevant deep graph architectures indicating the effectiveness of our approach. When compared with existing speech emotion recognition methods, our model achieves comparable performance to the state-of-the-art with significantly fewer learnable parameters (∼30K) indicating its applicability in resource-constrained devices.

我们提出了一种深度图方法来解决语音情感识别问题。以图表的形式表示数据是一种紧凑、高效和可伸缩的方式。遵循图信号处理的理论，我们提出将语音信号建模为循环图或折线图。这种图结构使我们能够构建一个基于图卷积网络(GCN)的体系结构，与标准GCN中使用的近似卷积相比，它可以执行精确的图卷积。我们在流行的IEMOCAP和MSP-Improv数据库上对我们的语音情感识别模型的性能进行了评估。我们的模型的性能优于标准GCN和其他相关的深图体系结构，表明了我们方法的有效性。与现有的语音情感识别方法相比，我们的模型在可学习参数(∼30K)显著减少的情况下获得了与最先进水平相当的性能，表明其在资源受限的设备中的适用性。

# 词汇记录

# 结果

MSP-IMPROV

![]({12}_Compact%20Graph%20Architecture%20for%20Speech%20Emotion%20Recognition@shirianCompactGraphArchitecture2021.assets/image-20220417162601.png)

# 精读

大部分SER方法都是遵循两种处理过程，首先从原始音频中提取一组特征，然后将特征输入到深度学习模型中，以生成离散(或连续)的情感标签[1,2,3,4]。在SER领域，模型训练常将LLDs(Low-Level descriptor，手工设计的一些低水平特征)，lexical 特征[5,6]和 Log Mel spectrograms 作为输入[7]。其中 spectrogram 通常与卷积神经网络(CNNs)一起使用[7]，但 CNNs 无法捕捉语音动态变化，而这种时间动态在SER中具有重要意义，因为它反映了情绪的动态变化。为了捕捉情绪的动态变化，Recurrent 模型，特别是长短时记忆网络(LSTMs)[2,3,4]，在SER中占据了主导地位，但其常常产生具有数百万可训练参数的复杂体系结构。目前，以图的形式表示数据，是一种紧凑、高效和可扩展的方式，并且GCNs目前已经在部分领域中实现应用，因此本文将SER问题归结为一个图分类问题，提出采用深度图的方法来进行SER。

本文的工作基于spectral GCNS，它在图形信号处理方面有很好的应用[14]。考虑到卷积核(对角线矩阵)是可学习的，spectral GCNs 在图的拉普拉斯矩阵的谱上执行卷积运算[15]。这涉及到图的拉普拉斯矩阵的特征分解，这在计算上是昂贵的。为了减少计算量，ChebNet用Chebyshev多项式逼近卷积运算(包括可学习的卷积核)[16]。最流行的GCN形式使用切比雪夫多项式的一阶近似，将卷积运算进一步简化为线性投影[9]。这样的GCN模型易于实现，并已成功地用于社交媒体网络和引文网络中的各种节点分类任务[9]。

我们将语音信号建模为一个简单的图，由于这种特殊的图结构，我们利用图信号处理[17]中的某些结果来执行精确的图形卷积(与流行的GCN中使用的approximations 不同)，提出了一个轻量级的GCN架构，在IEMOCAP[18]和MSP-Improv[19]数据库上具有优异的情感识别性能。

**图结构**

首先，从每个语音样本中构造对应的图结构 G=(V,E)，其中 $V$ 是 $M$ 个节点{ $v_{i}$ }的集合，$E$ 是节点之间所有边的集合。$G$ 的邻接矩阵表示为 $A$ ，其中元素 ($A_{ij}$) 表示连接{ $v_{i}$ }和{ $v_{j}$ }的边界权值，权值为零时表示没有边连接两点，其中邻接矩阵 $A$ 的对角线元素为0。

![]({12}_Compact%20Graph%20Architecture%20for%20Speech%20Emotion%20Recognition@shirianCompactGraphArchitecture2021.assets/image-20220304010332.png)

1. **语音图节点的构造策略**遵循一个简单的帧到节点转换，每个节点对应于语音信号的一个 short windowed segment。即 $M$ 帧语音信号(短的、重叠的片段)构成 $G$ 中的 $M$ 个节点。

2. **构建语音信号图结构**，我们研究两个无向图结构:(1)由邻接矩阵 $A_{c}$ 定义的圆形图结构和(2)由邻接矩阵 $A_{l}$ 定义的线形图结构。![]({12}_Compact%20Graph%20Architecture%20for%20Speech%20Emotion%20Recognition@shirianCompactGraphArchitecture2021.assets/image-20220304010347.png)
    由上图可知，每个节点仅连接到两个相邻节点，从而可以将信号转换为折线图或循环图。并且这两种图结构的图拉普拉斯算子具有特殊的结构，可以极大地简化 spectral GCN 计算。

3. **关联节点特征**，每个节点{$v_i$}与节点特征向量{ $x_{i} \in R^P$ }相关联。一个节点特征向量包含了从对应的语音片段中提取的LLDs。特一个特征矩阵$X=[x_1，···x_M] \in R^{M×P}$，包含了所有节点的特征向量。

**图分类**

设计GCN架构，给定一组由语音转换来的图 {$G_1，…，G_N$}和对应的真实标签 {$y_1，…y_{N}$}，能够识别语音情感。本文架构包括两个图卷积层；一个池化层，生成图嵌入向量；一个全连接层，生成离散的情感标签。

![]({12}_Compact%20Graph%20Architecture%20for%20Speech%20Emotion%20Recognition@shirianCompactGraphArchitecture2021.assets/image-20220304010243.png)

1. **图卷积层**。本文模型基于 spectral GCN，在谱域中执行图卷积操作[14]：$h=x_i∗w$，其中 $w$ 为图卷积核(可学习)，$x_i$ 为输入节点特征，其等价于图谱域中的乘积：$\hat{\mathbf{h}}=\hat{\mathbf{x}}_{i} \odot \hat{\mathbf{w}}$，其中$\hat{\mathbf{h}}$、$\hat{\mathbf{x_i}}$ 和 $\hat{\mathbf{w}}$ 表示输出、节点特征和卷积滤波器经由图傅里叶变换(GFT)的谱域表示。由此扩展到输入特征矩阵，便可得到矩阵表示法：$\hat{\mathbf{H}}=\hat{\mathbf{X}} \hat{\mathbf{W}}$。

    为了得到 $\hat{\mathbf{X}}$ 和 $\hat{\mathbf{W}}$ ，我们通常计算归一化的图拉普拉斯矩阵 $\mathcal{L}=\mathbf{D}^{-\frac{1}{2}} \mathbf{L D}^{-\frac{1}{2}}$，其中$\mathbf{D}$为度矩阵(记录每个节点邻点数量的对角矩阵)，$\mathbf{L}=\mathbf{D}−\mathbf{A}$ 为原拉普拉斯矩阵， $\mathbf{A}$ 为图的邻接矩阵。

    又因$\mathbf{L}$ 的特征分解可以写成$\mathcal{L}=\mathbf{U} \Lambda \mathbf{U}^{T}=\sum_{i=1}^{M} \lambda_{i} \mathbf{u}_{i} \mathbf{u}_{i}{ }^{T}$ 形式，其中 $\lambda_{i}$ 是L的第i个特征值，$\mathbf{u}_{i}$ 是对应于 $\lambda_{i}$ 的特征向量，$Λ=diag(\lambda_{i})$ 为对角矩阵， $\mathbf{U}=[\mathbf{u}_1,\mathbf{u}_{2,}\cdots , \mathbf{u}_N]$，可得精确的图卷积运算公式：$$\begin{aligned}&\hat{\mathbf{H}}=\hat{\mathbf{X}} \hat{\mathbf{W}}= \left(\mathbf{U}^{T} \mathbf{X}\right)\left(\mathbf{U}^{T} \mathbf{W}\right) \\ &\mathbf{H}=\mathbf{U} \hat{\mathbf{H}}\end{aligned}$$
    如果进行多次卷积操作，则可扩展得到第k层的图卷积公式：$$\mathbf{H}^{k+1}=\mathbf{U} \left(\mathbf{U}^{T} \mathbf{H}^{k}\right)\left(\mathbf{U}^{T} \mathbf{W}^{k}\right)$$，其中 $\mathbf{H}^{0}=\mathbf{X}$，且 $\mathbf{W}$ 是可学习的。

    特殊的，若令 $A=A_c$ (循环图)，可得 $L$ 的形式为：$$\mathbf{L}=\left[\begin{array}{ccccc}2 & -1 & 0 & \cdots & -1 \\-1 & 2 & -1 & \cdots & 0 \\0 & -1 & 2 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ -1 & 0 & \cdots & -1 & 2 \end{array}\right]$$在此情况下，GFT等价于离散傅里叶变换(DFT)[17]。类似地，对于 $A=A_l$ (线形图)，GFT等价于离散余弦变换(DCT)。这使得卷积操作更加方便且计算效率高，因为我们可以避免对于任意图结构而言计算量大的特征分解。

    根据最近一篇关于GCN[20]的工作，可知公式中的卷积核 $\left(\mathbf{U}^{T} \mathbf{W}^{k}\right)$ 能通过多层感知器(MLP)来学习得到，最后得到以下形式的卷积运算$$\mathbf{H}^{(k+1)}=\mathbf{U}\left(\operatorname{MLP}\left(\mathbf{U}^{T} \mathbf{H}^{(k)}\right)\right)$$ 其中，只有MLP参数是可学习的。

2. **汇聚层**。我们的目标是对整个图结构进行分类(与一般图节点分类任务相反)。因此，我们需要一个函数来从节点的嵌入向量中获得图级表征 $h_G \in R^Q$。

    通过在将所有节点卷积运算得到的嵌入向量矩阵 $H_(k)$ 传递到分类层之前，在最后一层通过汇聚层池化，可以获得 $h_G \in R^Q$。图域中常用的池化方法有mean, max和sum[9,21]三种，但 Max 和 Mean 两种方法通常不能保存有关图结构的基本信息，而Sum池已被证明是很好的选择[20]。因此本文中使用 Sum 方法来获得图表示（对每一维度的所有节点的嵌入特征求和）：$$\mathbf{h}_{G}=\operatorname{sumpool}\left(\mathbf{H}^{(K)}\right)=\sum_{i=1}^{M} \mathbf{h}_{i}^{(K)}$$

    池化层之后是一个全连接的层，用来生成分类标签，最后用交叉熵损失函数 loss =$=-\sum_{n} \mathbf{y}_{n} \log \tilde{\mathbf{y}}_{n}$ 训练。

**实验结果和分析**
我们使用 OpenSMILE 工具包[28]从为InterSpeech 2009情感挑战[27]建议的语音话语中提取一组低层表征(LLD)构建特征集，其中包括Mel频率倒谱系数(MFCCs)、过零率、语音概率、基频(F0)和帧能量。对于每个样本，我们使用一个长度为25ms(步长为10ms)的滑动窗口来局部提取LLDs。然后使用移动平均滤波器对每个特征进行平滑，并且使用平滑后的特征来计算它们各自的一阶 delta 系数。此外，我们还为IEMOCAP 添加了spontaneity 作为 binary feature，因为这一特征有助于SER[29]，spontaneity 数据随数据库一起提供。综上，在IEMOCAP数据库生成了维度P=35的节点特征向量，对于MSPIMPROV，生成了维度P=34的节点特征向量(无 spontaneity 特征)。

## 引用

- 图卷积网络(GCNs)[9]已成功地用于解决计算机vi快速流和自然语言处理中的各种问题，如动作识别[10]、对象跟踪[11]和文本分类[12]。

- 在con Fast streams文本音频分析中，我们知道只有一个最近的工作提出了一个基于注意的图神经网络架构，用于少量音频分类[13]。
