---
title: "Speech Emotion Recognition Using Semantic Information"
description: ""
citekey: tzirakisSpeechEmotionRecognition2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:27:40
lastmod: 2023-04-11 10:59:51
---

> [!info] 论文信息
>1. Title：Speech Emotion Recognition Using Semantic Information
>2. Author：Panagiotis Tzirakis, Anh Nguyen, Stefanos Zafeiriou, Björn W. Schuller
>3. Entry：[Zotero link](zotero://select/items/@tzirakisSpeechEmotionRecognition2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Tzirakis et al_2021_Speech Emotion Recognition Using Semantic Information.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 

## 摘要

> [!abstract] Speech emotion recognition is a crucial problem manifesting in a multitude of applications such as human computer interaction and education. Although several advancements have been made in the recent years, especially with the advent of Deep Neural Networks (DNN), most of the studies in the literature fail to consider the semantic information in the speech signal. In this paper, we propose a novel framework that can capture both the semantic and the paralinguistic information in the signal. In particular, our framework is comprised of a semantic feature extractor, that captures the semantic information, and a paralinguistic feature extractor, that captures the paralinguistic information. Both semantic and paraliguistic features are then combined to a unified representation using a novel attention mechanism. The unified feature vector is passed through a LSTM to capture the temporal dynamics in the signal, before the final prediction. To validate the effectiveness of our framework, we use the popular SEWA dataset of the AVEC challenge series and compare with the three winning papers. Our model provides state-of-the-art results in the valence and liking dimensions.1

> 语音情感识别是人机交互、教育等众多应用中的一个关键问题。尽管近年来取得了一些进展，特别是随着深度神经网络(DNN)的出现，但文献中的大多数研究都没有考虑语音信号中的语义信息。在本文中，我们提出了一种新的框架，可以同时捕捉信号中的语义信息和副语言信息。特别是，我们的框架由一个捕获语义信息的语义特征抽取器和一个捕获副语言信息的副语言特征抽取器组成。然后，使用一种新的注意机制将语义特征和并列特征组合成统一的表示。在最终预测之前，统一的特征向量通过 LSTM 来捕获信号中的时间动态。为了验证我们的框架的有效性，我们使用了 AVEC 挑战系列中流行的 SEWA 数据集，并与三篇获奖论文进行了比较。我们的模型在价位和喜好维度上提供了最先进的结果。

## 预处理

## 概述

## 结果

Speech2Vec

计算结果系数

![]({5}_Speech%20Emotion%20Recognition%20Using%20Semantic%20Information@tzirakisSpeechEmotionRecognition2021.assets/image-20220417161416.png)

![]({5}_Speech%20Emotion%20Recognition%20Using%20Semantic%20Information@tzirakisSpeechEmotionRecognition2021.assets/image-20220417161252.png)

![]({5}_Speech%20Emotion%20Recognition%20Using%20Semantic%20Information@tzirakisSpeechEmotionRecognition2021.assets/image-20220417161340.png)

![]({5}_Speech%20Emotion%20Recognition%20Using%20Semantic%20Information@tzirakisSpeechEmotionRecognition2021.assets/image-20220417161312.png)

## 精读

语音情感识别是人机交互和教育等众多应用中的一个关键问题。尽管近年来取得了一些进展，特别是随着深度神经网络（DNN）的出现，文献中的大多数研究都没有考虑语音信号中的语义信息。

![]({5}_Speech%20Emotion%20Recognition%20Using%20Semantic%20Information@tzirakisSpeechEmotionRecognition2021.assets/image-20220304005759.png)

我们的跨模式框架可以利用语义(高级)信息(SEC。3.1)和语音信号中的副语言(低级)动态(Sec.。3.2)。使用一种新的注意力融合策略(SEC)将低级别和高级特征集融合在一起。3.3)在将它们馈送到单层LSTM模块之前，捕获信号中的时间动态，用于最终的帧级预测。

1. 第一步捕获语音信号中的 semantic information

	训练了 Speech2Vec 和 Word2Vec 模型（可以分别使用语音数据和文本信息获得含语义信息的 Speech embedding  spaces 和 Word embedding  spaces）得到特征矩阵，然后使用[15]的方法(将得到的 embedding  spaces 通过域对抗方法[^Adversarialtraining]得到对齐后的 embedding  spaces )。即通过领域对抗性训练来学习。其中鉴别器试图最小化$L_{D}\left(\theta_{D} \mid W\right)=-\frac{1}{n} \sum_{i=1}^{n} \log P_{\theta_{D}}\left(\text { speech }=1 \mid W s_{i}\right)-\frac{1}{m} \sum_{i=1}^{m} \log P_{\theta_{D}}\left(\text { speech }=0 \mid t_{i}\right)$，其中$θ$是鉴别器的参数，$P_{\theta_{D}}(speech=1/0|z)$是特征矩阵$z$源自语音特征矩阵或文本特征矩阵的概率，使其能准确识别特征矩阵$z$的来源。而生成器试图最小化$L_{G}\left(W \mid \theta_{D}\right)=-\frac{1}{n} \sum_{i=1}^{n} \log P_{\theta_{D}}\left(\text { speech }=0 \mid W s_{i}\right) -\frac{1}{m} \sum_{i=1}^{m} \log P_{\theta_{D}}\left(\text { speech }=1 \mid t_{i}\right)$，持续优化$W$来欺骗鉴别器，使$T'=WS$和$T$尽可能相似，最终使$W$将得到的特征向量矩阵对齐。

2. 上述公式平等对待所有嵌入向量，而频率较高的词在向量空间中的嵌入质量会比频率较低的词更好。

	为此，我们使用频繁词来创建自定字典，该字典指定哪些语音嵌入向量{$S_{k}$}对应于哪些文本嵌入向量{$T_{k}$}，继续改善映射矩阵$W$。最终优化出$W^{∗}= \mathop{argmin}\limits_{W}||WS_{k}−T_{r}||_{F}$，公式解可由$S_{r} T_{r}^{T}$的奇异值分解得到的，即$S V D\left(S_{r} T_{r}^{T}\right)=$ $U \Sigma V^{T}$。**并最终得到想要的 Speech Semantic Features：$X_{s}$** 

3. 第三步为了得到语音信号中的 paralinguistic information
	使用原始波形作为输入，通过一个三层的一维卷积神经网络得到 Paralinguistic Features $X_{p}$ ![]({5}_Speech%20Emotion%20Recognition%20Using%20Semantic%20Information@tzirakisSpeechEmotionRecognition2021.assets/image-20220304012843.png)

4. 融合两个特征（简单串联或注意力机制融合）

    - 将 $X_{s}$和 $X_{p}$  简单的串联得到$X_{fusion}=[X_{s},X_{p}]$。
    - 每个特征集点乘线性映射矩阵$W_{s},W_{p}$，使其位于相同的向量空间（相同纬度），第一层使用注意力机制融合这两种特征得到$\tilde{\mathbf{x}}_{sp}=\text {Attention}\left(\tilde{\mathbf{x}}_{s}, \tilde{\mathbf{x}}_{p}\right)$，通过三个具有相同维度的全连接层(FC)，得到三种信息流$a,v,l$，刚好对应arousal, valence, liking 情感维度。然后再通过两个注意力机制一步步融合三种特征得$X_{fusion}=\text {Attention}\left(\text {Attention}\left(a, l\right), v\right)$

5. 在最终预测之前，$X_{fusion}$**通过 ==LSTM== 来捕获信号中的时间动态。**

6. 模型设置

Adam优化方法[27]、固定学习速率为10−4、小batch 大小25，序列长度为300，dropout[28]率为0.5、LSTM网络的 gradient norm clipping为5.0、原始波形长10秒、采样率22050 Hz、目标损失函数Concordance Correlation Coefficient (ρc)

### 引文

- 已经广泛用于情绪识别任务的两种模式是语音和文本[11,12]。为此，几个系统已经表明，整合这两种模式，可以获得强大的性能收益[11]。

- Word2Vec [13]、 Speech2Vec [14]对齐它们的两个嵌入空间，使得Speech2Vec功能尽可能接近Word2Vec功能[15]

- 虽然在模型的训练阶段，唤醒和效价维度很容易整合到单个网络中，但可喜性维度可能会导致收敛和泛化困难[16,17]。

- 例如，Trigeorgis等[22]利用卷积神经网络捕获信号中的空间信息，并利用时间信息的递归神经网络。

- 在一项类似的研究中，Tzirakis等[23]表明，使用更深的架构和更长的输入窗口可以产生更好的结果。

- 在另一项研究中，Neumann等[25]提出了一种将CNN与注意力相结合的注意卷积神经网络（ACNN）。

- 特别是，Tzirakis等[8]使用音频和视觉信息进行连续情绪识别。虽然这项研究取得了良好的结果，但它利用这两种模式进行模型的培训和评估。在最近的一项研究中，Albanie等人。

- 将知识从视觉信息（面部表情）转移到语音模型。

## 摘录
