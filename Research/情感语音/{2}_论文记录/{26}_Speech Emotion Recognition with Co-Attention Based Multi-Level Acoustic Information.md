---
title: ""
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: "笔记"
draft: true
layout: 
data: 2022-06-02 14:56:08
lastmod: 2023-04-11 11:31:05
date: 2022-06-02 14:56:08
---

# 重点

- [开源代码](https://github.com/vincent-zhq/ca-mser)
- 利用注意力机制, 将多级特征融合

# 摘要

Speech Emotion Recognition (SER) aims to help the machine to understand human’s subjective emotion from only audio information. However, extracting and utilizing comprehensive in-depth audio information is still a challenging task. In this paper, we propose an end-to-end speech emotion recognition system using multi-level acoustic information with a newly designed co-attention module. We firstly extract multi-level acoustic information, including MFCC, spectrogram, and the embedded high-level acoustic information with CNN, BiLSTM and wav2vec2, respectively. Then these extracted features are treated as multimodal inputs and fused by the proposed co-attention mechanism. Experiments are carried on the IEMOCAP dataset, and our model achieves competitive performance with two different speaker-independent crossvalidation strategies. 

语音情感识别的目的是帮助机器仅从音频信息中理解人的主观情感。然而，提取和利用全面的深度音频信息仍然是一项具有挑战性的任务。在本文中，我们提出了一种端到端的语音情感识别系统，该系统使用了多级声学信息，并设计了一个新的共同注意模块。首先分别用CNN、BiLSTM和Wave2ve2提取多层声学信息，包括MFCC、频谱图和嵌入的高层声学信息。然后将提取的特征作为多通道输入，并利用所提出的共同注意机制进行融合。在IEMOCAP数据集上进行了实验，与两种不同的说话人无关交叉验证策略相比，我们的模型获得了与之相当的性能。

# 结果

![]({26}_Speech%20Emotion%20Recognition%20with%20Co-Attention%20Based%20Multi-Level%20Acoustic%20Information@zouSpeechEmotionRecognition2022.assets/image-20220602163947.png)

![]({26}_Speech%20Emotion%20Recognition%20with%20Co-Attention%20Based%20Multi-Level%20Acoustic%20Information@zouSpeechEmotionRecognition2022.assets/image-20220602163959.png)

# 词汇记录

# 精读

情绪的自动识别有几个应用，如人机交互[1]和监视[2]。一些研究人员建议将声音信息和文本信息结合起来，并学习高级上下文信息来帮助做出最终的情绪预测[3]。然而，相应的转录并不总是可用于大多数情感识别应用。此外，当前的自动语音识别(ASR)系统生成的文本还会引入单词识别错误，干扰情感识别任务。与附加文本和视觉信号的多模式情感识别相比，仅从音频信号进行情感感知要容易得多，因为单音频数据更容易获得。

在本文中，我们介绍了三种不同的用于多级声学信息的编码器：用于频谱图的CNN，用于MFCC的BiLSTM和用于原始音频信号的基于变压器的声学提取网络Wav2ve2[11]。在所设计的协同注意模块中，我们利用从MFCC提取的有效信息和频谱特征对每一帧进行加权后进行优化，得到最终的W2E嵌入。我们将提取的三个特征连接在一起，并用最终融合的信息做出最终的情感预测。在广泛使用的IEMOCAP数据集上，该模型采用了去掉一位说话人和去掉一次会话的交叉验证策略，优于现有的竞争模型。

![]({26}_Speech%20Emotion%20Recognition%20with%20Co-Attention%20Based%20Multi-Level%20Acoustic%20Information@zouSpeechEmotionRecognition2022.assets/image-20220602154158.png)

我们将来自同一音频段的MFCC、语谱图和Wav2ve2分别表示为$x_{m}\in\mathbf{R}^{T_{m}\times D_{m}}$，$x_{s}\in\mathbf{R}^{T_{s}\times D_{s}}$和$x_{w}\in\mathbf{R}^{T_{w}\times 1}$。将提取的MFCC特征$x_{m}^{\prime}$和谱图特征$x_{s}^{\prime}$连接并与线性层变换，得到wav2vec输出$x_{w}^{\prime}$的不同帧的权重。与这些生成的权重相乘后，我们从原始的WAV2vec输出中获得最终的W2E向量。将最终得到的W2E$x_{w}^{\prime\prime}$与之前的MFCC特征$x_{m}^{\prime}$和语谱图特征$x_{s}^{\prime}$连接起来，用于最终的情绪识别任务。由MFCC和频谱图特征生成的Wav2vec帧的权重和最终特征组合分别表示为$x_{\text{COATT}}^{\prime}$和$x^{\prime}$。数据的目标用$y$表示，最终预测用$\hat{y}$表示。

这里我们将多层声学信息定义为基于人类知识的低层MFCC、基于深度学习的高层谱图和W2E的组合，从而涵盖了语音信号在频域和时间域的特征。MFCC序列由双向LSTM处理，该双向LSTM具有0.5的差错和平坦化。平坦化的矢量被输入到具有RELU的线性层，作为具有0.1的丢失值的激活函数，以获得

$$

x_{m}^{\prime}=f_{m}\left(B i \operatorname{TSSM}\left(x_{m}\right)\right), \text{ 

 where  } x_{m}^{\prime} \in \mathbf{R}^{D_{m}^{\prime}}
$$
首先用预先训练的Alexnet重塑谱图图像。对AlexNet提取的特征进行与MFCC特征类似的操作以获得

$$

x_{s}^{\prime}=f_{s}\left(A l e x N e t\left(x_{s}\right)\right)\text{ 

 where  } x_{s}^{\prime} \in \mathbf{R}^{D_{s}^{\prime}}
$$

原始音频片段被直接发送到相应的Wave2ve2处理器和Wav2Vec2模型，以获得原始Wav2Vec2输出

$$

x_{w}^{\prime}=W a v 2 \operatorname{Vec} 2\left(x_{w}\right), \text{  where  } x_{w}^{\prime} \in \mathbf{R}^{T_{w}^{\prime} \times D_{w}^{\prime}}

$$

考虑到三种声学信息源在最终情感预测中的作用相似，我们利用它们之间的相关性来指导特征自适应。通常，波2ve2输出的最后一帧或平均值被用来表示波2ve2特征。显然，我们在序列维度中丢失了一些有效信息。在这里，我们引入了一种共同注意模块，将W2E的不同帧组合在一起，并利用MFCC特征和谱图特征生成帧权重。

先，我们从MFCC特征$x_{m}^{\prime}$和谱图特征$x_{s}^{\prime}$创建一维矩阵，其变换层由

$$x_{a t}^{\prime}=f_{a t}\left(x_{m}^{\prime}\oplus x_{s}^{\prime}\right)$$

给出, 其中 $x_{att}^{\prime} \in \mathbf{R}^{1\times T_{w}^{\prime}}$

将WAV2ve2输出与先前生成的权重相乘，得到最终加权的WAV2ve2特征，如$$x_{w}^{\prime\prime}=\left(x_{a t t}^{\prime}\cdot x_{w}^{\prime}\right)^{T}$$其中$x_{w}^{\prime\prime}\in\mathbf{R}^{D_{w}^{\prime}}$。

将最终的MFCC、语谱图特征和加权的W2E连接起来，并将语音情感预测写为$$\hat{y}=f\left(x_{m}^{\prime}\oplus x_{s}^{\prime}\oplus x_{w}^{\prime\prime}\right)$$

## 引文

SER问题特征方法: 

- 绝大多数的涉及提取关键的音频特征，如Mel频率倒谱系数(MFCC)、恒定Q变换(CQT)或构造相应的频谱图来将问题作为图像分类问题来处理[4]。MFCC和语谱图都反映了语音信号在频域中的更多信息。MFCC可以看作是一种基于人类知识的低层特征。谱图可以通过深度神经网络进行进一步处理，获得高层信息。
- 将语音情感识别(SER)问题转化为多个声学信息的多层次融合问题是一种潜在的利用完整音频信息的有效方法。


针对不同的声学信号，设计具有不同体系结构细节的各种编码器，如用于频谱图的CNN和用于MFCC的CNN/LSTM。

在[3]中，利用一系列具有不同核大小的CNN来挖掘声学信息。

一些方法提出引入网络的组合来提取声学信息，例如[5]结合LSTM和门控多特征单元(GMU)来提取静态和动态语音信号。

在[6]中，Gao等人提出了一种领域对抗性自动编码器，利用预先训练的谱图信息来提取区分表示。从不同来源提取特征需要对应的来源特定的神经网络。

已经提出了不同类型的注意机制来处理提取的特征，如常用的自我注意[5，7]和跨通道注意[8]。

对于输入组合比较复杂的模型，引入了新的注意机制。[9]融合两个通道，然后使用所提出的注意通道-跳跃机制将结果与另一个通道合并。

在[10]中，设计了一种基于注意力的分层时间卷积网络来融合谱图图像的通道间和通道内特征。
