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
data: 2022-04-17 14:16:26
lastmod: 2022-06-06 19:33:41
---

# 重点

- 论文源文件
- 通过静态 Log-Mel Filter bank 特征（Mel滤波器组）和其动态一阶导数和二阶导数特征进行互补学习，逐步了解高层次的情绪表示。 
- 利用了一种 gate-based 的多特征融合单元，用于在帧级上有效地将不同特征整合在一起。
- 使用了 Bahdanau 可微分注意力模型计算情绪
- 使用 z-score标准化 消除说话人之间的差异

# 摘要

Many studies on automatic speech emotion recognition (SER) have been devoted to extracting meaningful emotional features for generating emotion-relevant representations. However, they generally ignore the complementary learning of static and dynamic features, leading to limited performances. In this paper, we propose a novel hierarchical network called HNSD that can efficiently integrate the static and dynamic features for SER. Specifically, the proposed HNSD framework consists of three different modules. To capture the discriminative features, an effective encoding module is firstly designed to simultaneously encode both static and dynamic features. By taking the obtained features as inputs, the Gated Multi-features Unit (GMU) is conducted to explicitly determine the emotional intermediate representations for framelevel features fusion, instead of directly fusing these acoustic features. In this way, the learned static and dynamic features can jointly and comprehensively generate the unified feature representations. Benefiting from a well-designed attention mechanism, the last classification module is applied to predict the emotional states at the utterance level. Extensive experiments on the IEMOCAP benchmark dataset demonstrate the superiority of our method in comparison with state-of-the-art baselines.

许多自动语音情感识别(SER)的研究致力于提取有意义的情感特征以生成与情感相关的表征。然而，它们普遍忽略了静态和动态特征的互补学习，导致了性能的限制。在本文中，我们提出了一种新的层次化网络HNSD，它能有效地集成SER的静态和动态特征。具体地说，拟议的HNSD框架由三个不同的模块组成。为了获取可区分的特征，首先设计了一个有效的编码模块，同时对静态和动态特征进行编码。将获得的特征作为输入，通过门控多特征单元(GMU)明确地确定帧特征融合的情感中间表征，而不是直接融合这些声学特征。这样，学习到的静态特征和动态特征可以联合、综合地生成统一的特征表示。得益于精心设计的注意机制，最后一个分类模块用于预测话语层面的情绪状态。在IEMOCAP基准数据集上的广泛实验表明，与最先进的基线相比，我们的方法具有优越性。

# 词汇记录

# 结果

IEMOCAP

![]({8}_Hierarchical%20Network%20Based%20on%20the%20Fusion%20of%20Static%20and%20Dynamic%20Features%20for%20Speech%20Emotion%20Recognition@caoHierarchicalNetworkBased2021.assets/image-20220417161851.png)

![]({8}_Hierarchical%20Network%20Based%20on%20the%20Fusion%20of%20Static%20and%20Dynamic%20Features%20for%20Speech%20Emotion%20Recognition@caoHierarchicalNetworkBased2021.assets/image-20220417161903.png)

# 精读

![]({8}_Hierarchical%20Network%20Based%20on%20the%20Fusion%20of%20Static%20and%20Dynamic%20Features%20for%20Speech%20Emotion%20Recognition@caoHierarchicalNetworkBased2021.assets/image-20220304005951.png)

静态特征中包含了足够的频域信息。 

1. 使用汉明窗将语音信号分割成25ms 窗宽、10ms 移位的短帧。
2. 利用短时距傅里叶变换信号将信号从时域转换到频域。
3. 对 mel 滤波器组（26个）的能谱进行了对数运算。将Log-Mel 特征作为静态特征，由矩阵$X^{S}∈R^{T×N}$表示，其中 $T$ 是帧数，$N$ 是 Mel滤波器的数量。 $x^{S}_{i}∈ X^{S}$是含 $N$ 个滤波器的第 $i$ 帧（i∈[1，t]）。

动态特征描述了帧间的频谱变化，并反映了情绪的变化过程，可以使用一阶差分方程获得，并由$X^{d} = [Y, Z]$表示，$x^{d}_{i}∈ X^{d}$, i 为第 i 帧（i∈[1，t]）。

1. $y_{i} =\sum_{n=1}^{M} n\left(x_{i+n}^{s}-x_{i-n}^{s}\right) / 2 \sum_{n=1}^{M} n^{2}$
2. $z_{i} =\sum_{n=1}^{M} n\left(y_{i+n}-y_{i-n}\right) / 2 \sum_{n=1}^{M} n^{2}$

第一层是一个有效编码模块。为了防止不同的特征之间彼此干扰，通过使用长短期记忆单元(LSTM，隐藏单元512)，把$X^{S}$和$X^{d}$ 进行编码，用$f^{s}_{i}$ 和 $f^{d}_{i}$ 表示。在这个模块中可以分别学习静态特征和动态特征在时间尺度上的上下文信息，并将静态和动态特征嵌入到高维特征表示中。

第二层中引入门控多特征单元（GMU），将所获得的特征$f^{s}_{i}$ 和 $f^{d}_{i}$作为输入，通过以Tanh为激活函数的神经元$（h_{d/S}=\tanh \left(W_{d/s}\left(f^{d/s}\right)^{T}\right)）$得到 $h^{S}$和$h^{d}$ 。同时定义了一个门神经元控制$f^{s}$ 和 $f^{d}$的权重，表示为$z=\sigma\left(W_{c}\left[f^{s}, f^{d}\right]^{T}\right) ∈ R^{1×T}$，最终得到协同融合特征$h=h_{s}*z+h_{d}*(1-z)∈ R^{hs×T}$

第三层采用 Bahdanau 的注意力机制模型通过前馈神经网络计算权重，每一帧的情绪分数$s_{t}=V^{T} \tanh \left(W h_{t}+b\right)$，其反映了每个帧的情感贡献。其中 $h_{t}$ 表示 $h$ 第$t$帧的融合特征， $V∈R^{d×1}$（本文中d选用的16）和$W≥R^{d×Hs}$是权重矩阵，$b∈R^{d×1}$是偏置向量。然后将情绪分数标准化得到是 t-th 帧的$\alpha_{t}=\frac{\exp \left(s_{t}\right)}{\sum_{i=1}^{T} \exp \left(s_{i}\right)}$。而话语层次的特征就可以通过对每一帧按其贡献加权得到   $u=\sum_{t=1}^{T} \alpha_{t} h_{t}$

通过全连接层（神经元个数：128）和sorftmax层得到最终的情感识别结果。训练过程中使用Adam（学习率：0.0001，weight decay ：0.001）进行反馈优化参数

通过WA（（神经元个数：128））和UA对测试结果进行评估。

## 引用

- 许多研究已经采用了基于卷积神经网络（CNN）和经常性神经网络（RNN）的模型，以产生更多辨别性声学特征，以提高SER [2,3,4,5,6]的性能。

- “例如，李等人。 [4]设计了两个不同的卷积核，用于分别从频谱图分别捕获时间和频域特性。 李等人。''

- [5]提出了一种具有多头自注意的扩展神经网络，用于从 mel frequency 倒谱系数(mfccs)研究情绪相关特征。

- 近年来，注意机制在提高注意效果方面取得了很大进展[7,8,9]。

- [7]应用RNN以检测MFCC的时间上下文信息，并引入了可靠的关注机制，专注于语音信号的情绪相关区域。

- 陈等人。 [10]和Lee等人。 [11]考虑了语音的动态特征作为网络的输入，它们将连接的静态和动态特征转移到深层神经网络中。然而，这种策略忽略了静态和动态特征将相互干扰，这导致表现不令人满意[12]。 

- [13],给出了通过门控多特征单元(gmu)寻找情绪中间表示的灵感。

- Bahdanau注意机制[14,15]致力于在最后一个模块计算情绪突出框架。

- Bi-LSTM [11]：输入为32种特征的Bi-LSTM网络（包括F0，语音概率，过零率，12维MFCC的log energy系数，以及一阶时间导数）。  

- LSTM+CTC [9]：输入为40维的log Mel-filter bank 特征的 attention-based BI-LSTM网络，与连接主义时间分类（CTC）组合。   

- CNN+ Attention[4]：基于声谱图，使用含两组 filter的CNN提取 time-specific and frequency-specific 特征，然后将其连接起来输入到后续的卷积层中，使用 Attention pooling 方法学习  the final emotional representation.。  

- Transformer[20]：基于IS09特征集（统计功能集），结合 self-attention 研究情感语音识别。 

- CNN + RNN + Attention [10]：输入为一阶和二阶动态特征的基于attention的三维CNN 模型判别信息  

- CNN-GRU-SEQCAP [21]：考虑声谱中activities的spatial relationship的基于 capsule networks (CapsNets) 的架构，the spatial relationship of activities in spectrograms  

- Transformer + auxiliary learning [22]: 输入为log Mel-Filter Bank 特征的一种基于多任务学习的多头注意力机制的深度学习网络。
