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
data: 2022-04-17 14:16:33
lastmod: 2022-06-06 19:48:00
---

# 重点 

- 论文源文件
- 提出了一种使用了增强版激活函数的方法：Attention ReLU GRU，即将attention-based Rectified Linear Unit (AReLU) 作为激活函数的GRU和BiGRU。
- openSMILE工具包[16]提取特征
- 引出了一些重要的激活函数：SELU [18], EELU [19], Mish [20], and learnable activations such as Comb [21] and PAU [22].

# 摘要

Notwithstanding the significant advancements in the field of deep learning, the basic long short-term memory (LSTM) or Gated Recurrent Unit (GRU) units have largely remained unchanged and unexplored. There are several possibilities in advancing the state-of-art by rightly adapting and enhancing the various elements of these units. Activation functions are one such key element. In this work, we explore using diverse activation functions within GRU and bi-directional GRU (BiGRU) cells in the context of speech emotion recognition (SER). We also propose a novel Attention ReLU GRU (AR-GRU) that employs attention-based Rectified Linear Unit (AReLU) activation within GRU and BiGRU cells. We demonstrate the effectiveness of AR-GRU on one exemplary application using the recently proposed network for SER namely Interaction-Aware Attention Network (IAAN). Our proposed method utilising AR-GRU within this network yields significant performance gain and achieves an unweighted accuracy of 68.3% (2% over the baseline) and weighted accuracy of 66.9 % (2.2 % absolute over the baseline) in four class emotion recognition on the IEMOCAP database.

尽管深度学习领域取得了重大进展，但基本的长短期记忆(LSTM)或门控递归单位(GRU)单位在很大程度上保持不变和未被探索。通过正确地调整和加强这些单位的各种要素，有几种可能性来推进最先进的技术。激活功能就是这样的关键要素之一。在这项工作中，我们探索在语音情感识别(SER)的背景下，在GRU和双向GRU(BiGRU)细胞中使用不同的激活函数。我们还提出了一种新的注意力重现GRU(AR-GRU)，它在GRU和BiGRU细胞中使用基于注意的整流线性单元(AReLU)的激活。我们使用最近提出的SER网络，即交互感知注意网络(IAN)，在一个示例性应用上演示了AR-GRU的有效性。我们提出的方法在这个网络中使用AR-GRU获得了显著的性能提升，在IEMOCAP数据库上的四类情感识别中，未加权准确率为68.3%(超过基线2%)，加权准确率为66.9%(绝对准确率为2.2%)。

# 词汇记录

# 结果

IEMOCAP

![]({9}_A%20Novel%20Attention-Based%20Gated%20Recurrent%20Unit%20and%20its%20Efficacy%20in%20Speech%20Emotion%20Recognition.assets/image-20220417162004.png)

# 精读

蕴含在人类声音中的副语言信息揭示了说话者的情感状态。这些信息在人与人之间的互动中至关重要，因为我们人类利用这些信息来调整，例如，我们的信息内容或者我们的声调，目的是使互动更加顺畅，并且使我们对自己的语言产生共鸣。

激活函数是改善LSTM 或 GRU 等Unit的一个关键因素，因此，在本文中，我们探讨了语音情感识别中 GRU 和双向 GRU Unit内不同的激活函数，并提出了一种新的Attention ReLU GRU(AR-GRU)方法，即使用AReLU （Attention-based Rectified Linear Units）作为激活函数的GRU 和 BiGRU 。

AR-GRU有助于在富含情绪的语音间捕捉特征间的长程交互（依赖），并在解决梯度消失问题的同时提高SER系统的性能。

AReLU中是通过使用Alpha为0.01和Beta为-4，使AReLU类似于RELU的激活函数。因为Alpha是控制negative values的比例因子，而值0.01与 clamp function相结合对 negative values影响最小，β是控制 positive values 的比例因子，将其设置为-4会使此比例因子失效。然后不断探索取值效果，最终得到β值为1，Alpha为0.01时，结果最好。

我们使用[13]作为基线模型，它采用了一个BiGRU来处理说话人的当前话语，以及两个GRU来处理前面的话语。基于Emobase 2010的配置，使用openSMILE工具包[16]，提取声学低级描述符（LLDs），包括梅尔-频谱系数（MFCCs）、音调和它们在语料的每个短帧中的统计数据。

使用5折交叉验证（5-fold Cross Validation）和留一法进行验证，通过观察每100个训练周期在验证集上的表现来提前停止。

![]({9}_A%20Novel%20Attention-Based%20Gated%20Recurrent%20Unit%20and%20its%20Efficacy%20in%20Speech%20Emotion%20Recognition.assets/image-20220304010017.png)

## 扩展知识

**GRU**

门控递归单元(GRU)是递归神经网络(RNN)的一种，它使用门控机制(gating mechanisms )来控制和管理神经网络中神经元之间的信息流。GRU的结构允许自适应地从大型数据序列捕获相关性，同时确保不会丢弃来自序列较早部分的信息。这是通过选通机制实现的，该选通机制规定了在每个时间步要保留或丢弃的信息。与LSTM相比，GRU能够克服消失梯度问题，并且由于需要优化的参数数量较少，因此训练速度更快。

传统GRU中的经典激活函数是双曲正切(TANH)。尽管使用tanh函数有其固有的优点，但由于密集的激活计算，它具有很高的计算复杂度，并且容易受到消失梯度问题的影响。

[**AReLU**](https://zhuanlan.zhihu.com/p/158389615)

AReLU一种基于注意力机制的可动态学习的线性整流单元（激活函数）[14]，可以表示为element-wise sign-based attention机制（基于符号的注意力机制：ELSA）和 标准Rectified Linear Unit（ReLU） 的组合，其对梯度消失的抵抗力更强，只有两个额外的可学习参数，可以在较小的学习率下促进快速的网络训练。

$\mathcal{F}\left(x_{i}, \alpha, \beta\right)=\mathcal{R}\left(x_{i}\right)+\mathcal{L}\left(x_{i}, \alpha, \beta\right)\\ \begin{cases}C(\alpha) x_{i} & , x_{i}<0 \\ (1+\sigma(\beta)) x_{i} & , x_{i}=0\end{cases}$

$X = {x_{i}}$,是激活层的输入，${α, β} ∈ R^{2}$是可学习参数，C是剪裁操作，作用是将alpha的值限制在$[0.01, 0.99]$之间，阻止其变为0，$σ$是sigmoid函数。理解：对于大于零的数据梯度进行放大，小于零的则缩小。

## 引用

- 隐马尔可夫模型(hmms)或支持向量机(svms)[3,4]。

- 包括卷积神经网络[5] 

- 回归神经网络[6,7,8] 

- cnns 和 rnns [9]

- 例如长短期记忆(lstm)[10]和门控循环单元(gru)[11] ，可以捕捉序列数据的时间动态，能够捕获的时间依赖性的声学特征。

- 注意力机制可以用来帮助 rnns 关注最突出的情感信息[6,7,8]。

- 此外，上下文信息也可以用来改善服务器系统的性能，如最近的工作[12,13]所示。

- 我们使用交互感知的注意力网络（IAAN）[13]作为基线模型，Yeh et al. [13]通过交互感知注意网络(iaan)成功地利用了语境信息，该网络利用前一个说话者在双人对话场景中的转换来学习注意力分数，以检测一个说话者话语的情绪状态。

- 基于注意力的纠正线性单元(arellu)[14]。

- BiLSTM+ATT[6]: 一个基于帧级特征的注意力池层的 bilstm 网络。

- MDNN[17]: 由多个局部分类器和一个全局分类器组成的多路径深层神经网络。
