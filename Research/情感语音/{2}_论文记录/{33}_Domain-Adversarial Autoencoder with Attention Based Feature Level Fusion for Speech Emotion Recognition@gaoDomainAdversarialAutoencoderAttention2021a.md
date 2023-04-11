---
title: "Domain-Adversarial Autoencoder with Attention Based Feature Level Fusion for Speech Emotion Recognition"
description: ""
citekey: gaoDomainAdversarialAutoencoderAttention2021a
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:33:25
lastmod: 2023-04-11 11:58:32
---

> [!info] 论文信息
>1. Title：Domain-Adversarial Autoencoder with Attention Based Feature Level Fusion for Speech Emotion Recognition
>2. Author：Yuan Gao, JiaXing Liu, Longbiao Wang, Jianwu Dang
>3. Entry：[Zotero link](zotero://select/items/@gaoDomainAdversarialAutoencoderAttention2021a) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Gao et al_2021_Domain-Adversarial Autoencoder with Attention Based Feature Level Fusion for2.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 使用迁移学习，由预训练网络从其他大型数据库学习先验知识，以此补偿情感数据库小的问题
- 使用领域对抗神经网络，包括情感预测、说话人分类、语料库分类等任务，通过消除先验知识中的非情感信息。
- 研究[13]已经确定，特征压缩后情绪信息可能会丢失。因此，引入多头注意（MHA）以减少特征融合阶段的信息丢失
- 引入了 valence 和 arousal 作为情感映射的两个标准，将不同数据库的不同标签，映射统一。

## 摘要

> [!abstract] Over the past two decades, although speech emotion recognition (SER) has garnered considerable attention, the problem of insufficient training data has been unresolved. A potential solution for this problem is to pre-train a model and transfer knowledge from large amounts of audio data. However, the data used for pre-training and testing originate from different domains, resulting in the latent representations to contain non-affective information. In this paper, we propose a domain-adversarial autoencoder to extract discriminative representations for SER. Through domain-adversarial learning, we can reduce the mismatch between domains while retaining discriminative information for emotion recognition. We also introduce multi-head attention to capture emotion information from different subspaces of input utterances. Experiments on IEMOCAP show that the proposed model outperforms the state-of-the-art systems by improving the unweighted accuracy by 4.15%, thereby demonstrating the effectiveness of the proposed model.

> 在过去的二十年里，尽管语音情感识别(SER)引起了相当大的关注，但训练数据不足的问题一直没有得到解决。这个问题的一个潜在解决方案是预先训练模型并从大量音频数据中迁移知识。然而，用于预训练和测试的数据来自不同的领域，导致潜在表征包含非情感信息。在本文中，我们提出了一种领域对抗的自动编码器来提取SER的区分表征。通过领域对抗性学习，我们可以减少领域之间的不匹配，同时保留用于情感识别的区分信息。我们还引入了多头注意，从输入话语的不同子空间中捕捉情感信息。在IEMOCAP上的实验表明，该模型比现有的系统提高了4.15%的未加权准确率，从而证明了该模型的有效性。

## 预处理

## 概述

## 结果

使用IEMOCAP中的脚本数据和临时数据对所提出的模型进行了评估。我们实施了将“happy”和“excited”合并为一个情感类别“happy”的普遍做法，产生了5531个话语[15]。

在DAE的预训练中，我们使用了三个社区可用的流行情感数据集：

萨里视听表达情感(SAVEE)[17]，包含四个男性受试者的录音，其中120个是中性的，60个是其他六种情绪的。
柏林情感语音数据库(EMO-DB)[18]，由七种情绪组成，由10名专业演员在录音环境中表演。整个数据集由535个话语组成。
情感声音数据库(EmoV-DB)[19]，包含来自四名男性说话者的7000个样本。这项研究使用了其中的四种情绪，共5256次。

输入信号的采样频率为16 kHz。我们将所有语音分割成265毫秒的片段。为每个片段计算输入频谱图，帧大小为25ms。输入语谱图的维度为32×129（Time × frequency）。批次大小设置为128。我们使用adadelta作为优化器，使用交叉熵作为损失函数。在本研究中，我们随机抽取了IEMOCAP中80%的数据用于训练，20%用于测试。为了解决不同语料库中情感标注不一致的问题，我们引入了valence和arousal作为情感映射的统一标准。Schuller等人。[20]将情绪映射到二元价和唤醒。在这项研究中，我们将这些情绪进一步归类为四类。如表1所示，P(X)中的情绪可以与快乐、中性、愤怒和悲伤共享相同的特征分布。

进行了可视化分析，以验证所提议的DAE的有效性。引入t分布随机邻近嵌入(t-SNE)[21]来可视化预先训练的自动编码器和DAE的特征表示。

![]({33}_Domain-Adversarial%20Autoencoder%20with%20Attention%20Based%20Feature%20Level%20Fusion%20for%20Speech%20Emotion%20Recognition@gaoDomainAdversarialAutoencoderAttention2021a.assets/image-20220604104136.png)

如图2所示，自动编码器和DAE ProForm对于愤怒(绿点)和悲伤(蓝点)和愤怒的分离都很好。在DAE的特征分布中，蓝点之间的距离较近。此外，DAE对于幸福(粉点)的表现相对较好。中性用白点表示，它散布在两个地块上。同样的情况在[7]中也有报道。

![]({33}_Domain-Adversarial%20Autoencoder%20with%20Attention%20Based%20Feature%20Level%20Fusion%20for%20Speech%20Emotion%20Recognition@gaoDomainAdversarialAutoencoderAttention2021a.assets/image-20220604104207.png)

使用IEMOCAP中的脚本数据和临时数据对所提出的模型进行了评估。我们实施了将“happy”和“excited”合并为一个情感类别“happy”的普遍做法，产生了5531个话语[15]。

在DAE的预训练中，我们使用了三个社区可用的流行情感数据集：

萨里视听表达情感(SAVEE)[17]，包含四个男性受试者的录音，其中120个是中性的，60个是其他六种情绪的。
柏林情感语音数据库(EMO-DB)[18]，由七种情绪组成，由10名专业演员在录音环境中表演。整个数据集由535个话语组成。
情感声音数据库(EmoV-DB)[19]，包含来自四名男性说话者的7000个样本。这项研究使用了其中的四种情绪，共5256次。

输入信号的采样频率为16 kHz。我们将所有语音分割成265毫秒的片段。为每个片段计算输入频谱图，帧大小为25ms。输入语谱图的维度为32×129（Time × frequency）。批次大小设置为128。我们使用adadelta作为优化器，使用交叉熵作为损失函数。在本研究中，我们随机抽取了IEMOCAP中80%的数据用于训练，20%用于测试。为了解决不同语料库中情感标注不一致的问题，我们引入了valence和arousal作为情感映射的统一标准。Schuller等人。[20]将情绪映射到二元价和唤醒。在这项研究中，我们将这些情绪进一步归类为四类。如表1所示，P(X)中的情绪可以与快乐、中性、愤怒和悲伤共享相同的特征分布。

进行了可视化分析，以验证所提议的DAE的有效性。引入t分布随机邻近嵌入(t-SNE)[21]来可视化预先训练的自动编码器和DAE的特征表示。

![]({33}_Domain-Adversarial%20Autoencoder%20with%20Attention%20Based%20Feature%20Level%20Fusion%20for%20Speech%20Emotion%20Recognition@gaoDomainAdversarialAutoencoderAttention2021a.assets/image-20220604104136.png)

如图2所示，自动编码器和DAE ProForm对于愤怒(绿点)和悲伤(蓝点)和愤怒的分离都很好。在DAE的特征分布中，蓝点之间的距离较近。此外，DAE对于幸福(粉点)的表现相对较好。中性用白点表示，它散布在两个地块上。同样的情况在[7]中也有报道。

![]({33}_Domain-Adversarial%20Autoencoder%20with%20Attention%20Based%20Feature%20Level%20Fusion%20for%20Speech%20Emotion%20Recognition@gaoDomainAdversarialAutoencoderAttention2021a.assets/image-20220604104207.png)

## 精读

### 引文

## 摘录
