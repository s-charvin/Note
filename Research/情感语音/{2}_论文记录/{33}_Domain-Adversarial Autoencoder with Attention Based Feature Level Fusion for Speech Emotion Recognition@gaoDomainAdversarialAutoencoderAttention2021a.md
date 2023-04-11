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
lastmod: 2023-04-11 11:59:27
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

由于语音是人类交流中最常见的形式，因此人工智能从语音中学习情绪信息至关重要。言语情绪识别（SER）的发展显着促进了自然和社交的人机通信。因此，这个研究课题引起了工业界和学术界越来越多的兴趣。然而，两个主要瓶颈限制了SER系统的识别能力。首先是缺乏大型自然标记数据集[1]，因为记录和注释情绪相关数据集非常耗时。其次是如何从语音信号中提取最佳特征。随着语音处理和图像分类深度学习的快速发展，深度学习方法在SER领域也取得了显着的进步[2,3]。与传统的手工制作特征相比，深度表征特征在没有任何专业知识的情况下显示出有希望的识别结果[4]。然而，由于人类情绪模棱两可，如何为SER提取最佳特征仍需要持续关注[5]。

训练数据的不足可以通过迁移学习产生额外的特征来补偿[6]，迁移学习可以通过来自不同领域的数据学习先验知识。对于SER任务，一些研究人员通过预先训练模型以无监督的方式学习其他特征来完成这种知识迁移[7,8]。自动编码器[9]在图像重建方面提供了良好的性能，并在许多领域得到广泛应用[10]。我们结合了卷积自动编码器，它是特征建模的最优化结构，作为所提出的SER系统的预训练组件。

但是，只需对自动编码器进行预训练就会产生某些问题。由于无监督学习的自发性[11]，在早期的研究中，预先训练的自动编码器还学习了各种非情感信息，如说话者和录音环境。为了解决这个问题，我们专注于领域对抗神经网络（DANN）[12]。梯度反转层可以防止模型学习域信息。我们使用DANN作为潜在表征的约束，目的是减少源域和目标域之间的不匹配。在所提出的方法中，DANN的域分类器被修改为具有说话者和语料库识别的多任务监督学习。在领域对抗训练的帮助下，我们可以通过消除非情感信息来提取更好的最佳表征。

此外，之前的研究已经确定，特征压缩后情绪信息可能会丢失[13]。因此，引入多头注意（MHA）以减少特征融合阶段的信息丢失[14]。

在本文中，我们提出了一种新的SER表征提取模型。这项研究的主要贡献可以总结如下。
1） 为了克服数据稀缺的问题，对自动编码器进行预训练以从其他情感语料库中提取潜在表征。
2） 域对抗训练被纳入以实现域独立表征。
3） MHA确保我们的模型将有效利用来自不同特征分布的情绪信息。

![]({33}_Domain-Adversarial%20Autoencoder%20with%20Attention%20Based%20Feature%20Level%20Fusion%20for%20Speech%20Emotion%20Recognition@gaoDomainAdversarialAutoencoderAttention2021a.assets/image-20220604100107.png)

2.1. Domain-adversarial autoencoder

为了解决上述瓶颈，我们提出了一种新的表征提取模型，该模型结合了深度CNN体系结构来提供一个有效的SER系统。如图所示，所提出的表征提取模型是通过领域对抗自动编码器(DAAE)实现的。DAAE主要由两部分组成：

(1)预先训练的卷积自动编码器

(2)域对抗神经网络(DANN)。

为了解决情感识别任务中数据不足的问题，我们对卷积自动编码器进行了预训练以提取额外的特征。这种预训练模型可以从额外的数据中迁移知识，以帮助SER任务。然而，自动编码器学习的这种先验知识也包含非情感信息，如说话人和录音环境等。

为了获得更优的潜在特征，我们将DANN直接加入到潜在表征$R_l$中。使用DANN的主要目的是消除$R_l$中的非情感信息。DANN有两个分类器和一个共享特征提取器。考虑到上述目的，Ganin等人。[12]在域分类器和特征提取器之间引入了梯度反转层。这一层通过在反向传播期间乘以某个负常数λ来反转梯度的符号。在我们提出的模型中，Dann可以对RL施加约束，以使该潜在表征的分布与源域保持一致。我们进一步修改了DANN，加入了三个有监督的分类任务，包括作为标签预测者的情感，作为领域分类器的说话人和语料库。典型的预训练模型会自发地从P(X)中学习领域信息，通过DANN可以确保情感识别的区分表征，同时使来自源数据和目标数据的样本无法区分。通过这种方式，所提出的表征提取模型可以实现情感识别的领域无关的表征。DAE的目标函数定义如下：
$$
\begin{gathered}

L_{D A A E}=L_{A E}+\alpha L_{D} \\

L_{D}=L_{e}-\lambda\left(\beta L_{s}+(1-\beta) L_{c}\right)

\end{gathered}
$$

其中$L_{AE}$是预先训练的自动编码器的重构损失，$L_{e}、L_{s}$和$L_{c}$是DANN中情感、说话人和语料库分类任务的损失函数。我们使用$α$和$\beta$作为权衡参数来控制每个损失项的权重。

对于输入数据$x$，该模型分两个阶段进行训练
(1)预训练
(2)特征提取。

在预训练阶段，该模型通过将$P(X)$重构为$P^{\prime}(X)$来更新自动编码器权重。DANN进行了更新，加入了净化特征。自动编码器的目标函数定义为$$L_{A E}=\operatorname{argmin}\left\|P(X)-P^{\prime}(X)\right\|^{2}$$
在特征提取阶段，我们首先使用来自目标数据X的样本对DAE进行微调。这是通过保持DAN的固定权重和偏差并将重建误差反向传播到自动编码器来完成的。以这种方式，潜在表征$R_l$的生成利用了先验知识并从监督DANN中获益，同时保留了用于情感识别的区别性信息。此外，深层表征$R_d$由深层CNN结构提取，这与SATT等人使用的结构类似。[15]。这两种类型的表征连接在一起，然后是一个完全连接的层。输出是公共表征RC，它包含从表征提取模型和深层CNN体系结构中学习的信息。


注意机制允许神经网络捕获输入序列的情绪显著部分。因此，上述两种类型的表示及其串联RC通过MHA融合在一起[14]。因此，我们可以增强输入序列的显著情感部分，并联合处理来自不同表示子空间的信息。实现了对输入特征的降维。每个头部的注意力分数计算如下

$$
\operatorname{Head}_{i}=\operatorname{Softmax}\left(\frac{Q K^{T}}{\sqrt{d_{i}}}\right) V
$$

注意的输入是分别对应于查询、关键字和值的潜在表示RD、RL和Rf。我们没有直接给分类器喂食，而是执行了一个线性项目，然后是一个按比例排列的点积注意力。MHA的最终输出是通过连接每个Headi生成的，如下式所示。(8)。

$$
\begin{gathered}

Q_{i}=R_{d} * W_{i}^{Q} \\

K_{i}=R_{l} * W_{i}^{K} \\

V_{i}=R_{f} * W_{i}^{V} \\

M_{h}(Q, K, V)=\text { Concat }\left(H e a d_{1}, \text { Head }_{2}, \ldots, \text { Head }_{n}\right)

\end{gathered}
$$

基于注意力的特征级融合方法的结构细节如图1的右侧所示。由于MHA允许系统对输入序列元素之间的相对依赖关系进行建模，因此该融合方法被用于为双向长期短期记忆(BLSTM)分类器获得稳定而有效的输入。

### 引文

## 摘录
