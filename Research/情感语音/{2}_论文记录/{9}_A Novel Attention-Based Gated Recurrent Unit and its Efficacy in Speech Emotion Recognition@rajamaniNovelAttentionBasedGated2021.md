---
title: "A Novel Attention-Based Gated Recurrent Unit and its Efficacy in Speech Emotion Recognition"
description: ""
citekey: rajamaniNovelAttentionBasedGated2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:29:22
lastmod: 2023-04-11 17:54:18
---

> [!info] 论文信息
>1. Title：A Novel Attention-Based Gated Recurrent Unit and its Efficacy in Speech Emotion Recognition
>2. Author：Srividya Tirunellai Rajamani, Kumar T. Rajamani, Adria Mallol-Ragolta, Shuo Liu, Björn Schuller
>3. Entry：[Zotero link](zotero://select/items/@rajamaniNovelAttentionBasedGated2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Rajamani et al_2021_A Novel Attention-Based Gated Recurrent Unit and its Efficacy in Speech Emotion.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\TBPVYNJ2\\9414489.html>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 提出了一种使用了增强版激活函数的方法：Attention ReLU GRU，即将attention-based Rectified Linear Unit (AReLU) 作为激活函数的GRU和BiGRU。
- openSMILE工具包[16]提取特征
- 引出了一些重要的激活函数：SELU [18], EELU [19], Mish [20], and learnable activations such as Comb [21] and PAU [22].

## 摘要

> [!abstract] Notwithstanding the significant advancements in the field of deep learning, the basic long short-term memory (LSTM) or Gated Recurrent Unit (GRU) units have largely remained unchanged and unexplored. There are several possibilities in advancing the state-of-art by rightly adapting and enhancing the various elements of these units. Activation functions are one such key element. In this work, we explore using diverse activation functions within GRU and bi-directional GRU (BiGRU) cells in the context of speech emotion recognition (SER). We also propose a novel Attention ReLU GRU (AR-GRU) that employs attention-based Rectified Linear Unit (AReLU) activation within GRU and BiGRU cells. We demonstrate the effectiveness of AR-GRU on one exemplary application using the recently proposed network for SER namely Interaction-Aware Attention Network (IAAN). Our proposed method utilising AR-GRU within this network yields significant performance gain and achieves an unweighted accuracy of 68.3% (2% over the baseline) and weighted accuracy of 66.9 % (2.2 % absolute over the baseline) in four class emotion recognition on the IEMOCAP database.

> 尽管深度学习领域取得了重大进展，但基本的长短期记忆(LSTM)或门控递归单位(GRU)单位在很大程度上保持不变和未被探索。通过正确地调整和加强这些单位的各种要素，有几种可能性来推进最先进的技术。激活功能就是这样的关键要素之一。在这项工作中，我们探索在语音情感识别(SER)的背景下，在 GRU 和双向 GRU(BiGRU)细胞中使用不同的激活函数。我们还提出了一种新的注意力重现 GRU(AR-GRU)，它在 GRU 和 BiGRU 细胞中使用基于注意的整流线性单元(AReLU)的激活。我们使用最近提出的 SER 网络，即交互感知注意网络(IAN)，在一个示例性应用上演示了 AR-GRU 的有效性。我们提出的方法在这个网络中使用 AR-GRU 获得了显著的性能提升，在 IEMOCAP 数据库上的四类情感识别中，未加权准确率为68.3%(超过基线2%)，加权准确率为66.9%(绝对准确率为2.2%)。

## 预处理

## 概述

## 结果

IEMOCAP

![]({9}_A%20Novel%20Attention-Based%20Gated%20Recurrent%20Unit%20and%20its%20Efficacy%20in%20Speech%20Emotion%20Recognition@rajamaniNovelAttentionBasedGated2021.assets/image-20220417162004.png)

## 精读

蕴含在人类声音中的副语言信息揭示了说话者的情感状态。这些信息在人与人之间的互动中至关重要，因为我们人类利用这些信息来调整，例如，我们的信息内容或者我们的声调，目的是使互动更加顺畅，并且使我们对自己的语言产生共鸣。

激活函数是改善 LSTM 或 GRU 等 Unit 的一个关键因素，因此，在本文中，我们探讨了语音情感识别中 GRU 和双向 GRU Unit 内不同的激活函数，并提出了一种新的 Attention ReLU GRU(AR-GRU)方法，即使用 AReLU （Attention-based Rectified Linear Units）作为激活函数的 GRU 和 BiGRU 。

AR-GRU 有助于在富含情绪的语音间捕捉特征间的长程交互（依赖），并在解决梯度消失问题的同时提高 SER 系统的性能。

AReLU 中是通过使用 Alpha 为 0.01 和 Beta 为-4，使 AReLU 类似于 RELU 的激活函数。因为 Alpha 是控制 negative values 的比例因子，而值 0.01 与 clamp function 相结合对 negative values 影响最小，β是控制 positive values 的比例因子，将其设置为-4 会使此比例因子失效。然后不断探索取值效果，最终得到β值为 1，Alpha 为0.01时，结果最好。

我们使用[13]作为基线模型，它采用了一个 BiGRU 来处理说话人的当前话语，以及两个 GRU 来处理前面的话语。基于 Emobase 2010 的配置，使用 openSMILE 工具包[16]，提取声学低级描述符（LLDs），包括梅尔-频谱系数（MFCCs）、音调和它们在语料的每个短帧中的统计数据。

使用 5 折交叉验证（5-fold Cross Validation）和留一法进行验证，通过观察每 100 个训练周期在验证集上的表现来提前停止。

![]({9}_A%20Novel%20Attention-Based%20Gated%20Recurrent%20Unit%20and%20its%20Efficacy%20in%20Speech%20Emotion%20Recognition@rajamaniNovelAttentionBasedGated2021.assets/image-20220304010017.png)

## 扩展知识

**GRU**

门控递归单元(GRU)是递归神经网络(RNN)的一种，它使用门控机制(gating mechanisms )来控制和管理神经网络中神经元之间的信息流。GRU 的结构允许自适应地从大型数据序列捕获相关性，同时确保不会丢弃来自序列较早部分的信息。这是通过选通机制实现的，该选通机制规定了在每个时间步要保留或丢弃的信息。与 LSTM 相比，GRU 能够克服消失梯度问题，并且由于需要优化的参数数量较少，因此训练速度更快。

传统 GRU 中的经典激活函数是双曲正切(TANH)。尽管使用 tanh 函数有其固有的优点，但由于密集的激活计算，它具有很高的计算复杂度，并且容易受到消失梯度问题的影响。

[**AReLU**](https://zhuanlan.zhihu.com/p/158389615)

AReLU 一种基于注意力机制的可动态学习的线性整流单元（激活函数）[14]，可以表示为 element-wise sign-based attention 机制（基于符号的注意力机制：ELSA）和标准 Rectified Linear Unit（ReLU） 的组合，其对梯度消失的抵抗力更强，只有两个额外的可学习参数，可以在较小的学习率下促进快速的网络训练。

$\mathcal{F}\left(x_{i}, \alpha, \beta\right)=\mathcal{R}\left(x_{i}\right)+\mathcal{L}\left(x_{i}, \alpha, \beta\right)\\ \begin{cases}C(\alpha) x_{i} & , x_{i}<0 \\ (1+\sigma(\beta)) x_{i} & , x_{i}=0\end{cases}$

$X = {x_{i}}$ ,是激活层的输入， ${α, β} ∈ R^{2}$ 是可学习参数，C 是剪裁操作，作用是将 alpha 的值限制在 $[0.01, 0.99]$ 之间，阻止其变为 0， $σ$ 是 sigmoid 函数。理解：对于大于零的数据梯度进行放大，小于零的则缩小。

### 引文

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

## 摘录
