---
title: "Deepemocluster: A Semi-Supervised Framework for Latent Cluster Representation of Speech Emotions"
description: ""
citekey: linDeepemoclusterSemiSupervisedFramework2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:31:46
lastmod: 2023-04-11 11:26:34
---

> [!info] 论文信息
>1. Title：Deepemocluster: A Semi-Supervised Framework for Latent Cluster Representation of Speech Emotions
>2. Author：Wei-Cheng Lin, Kusha Sridhar, Carlos Busso
>3. Entry：[Zotero link](zotero://select/items/@linDeepemoclusterSemiSupervisedFramework2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Lin et al_2021_Deepemocluster.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 

## 摘要

> [!abstract] Semi-supervised learning (SSL) is an appealing approach to resolve generalization problem for speech emotion recognition (SER) systems. By utilizing large amounts of unlabeled data, SSL is able to gain extra information about the prior distribution of the data. Typically, it can lead to better and robust recognition performance. Existing SSL approaches for SER include variations of encoder-decoder model structures such as autoencoder (AE) and variational autoecoders (VAEs), where it is difficult to interpret the learning mechanism behind the latent space. In this study, we introduce a new SSL framework, which we refer to as the DeepEmoCluster framework, for attribute-based SER tasks. The DeepEmoCluster framework is an end-to-end model with mel-spectrogram inputs, which combines a self-supervised pseudo labeling classification network with a supervised emotional attribute regressor. The approach encourages the model to learn latent representations by maximizing the emotional separation of K-means clusters. Our experimental results based on the MSP-Podcast corpus indicate that the DeepEmoCluster framework achieves competitive prediction performances in fully supervised scheme, outperforming baseline methods in most of the conditions. The approach can be further improved by incorporating extra unlabeled set. Moreover, our experimental results explicitly show that the latent clusters have emotional dependencies, enriching the geometric interpretation of the clusters.

> 半监督学习Semi-supervised learning（SSL）是解决语音情感识别系统泛化问题的一种有效方法，通过利用大量未标记的数据，SSL能够获得这些数据先前分布的额外信息，通常，它可以带来更好的和健壮的识别性能。现有的利用SSL的语音情感识别方法包括不同的编解码器模型结构，如自动编码器autoencoder(AE)和变分自动编码器variational autoecoders(VAES)，其中很难解释潜在特征空间背后的学习机制。在这项研究中，我们为基于属性的attribute-based语音情感识别任务引入了一个新的SSL框架，我们称之为DeepEmoCluster框架。DeepEmoCluster框架是一个以MEL谱图为输入的端到端模型，，它结合了一个自我监督的伪标记分类网络self-supervised pseudo labeling classification network和一个监督的情感属性回归supervised emotional attribute regressor。该方法通过最大化K-Means聚类的情感分离emotional separatio来加强模型学习潜在表征。我们在MSP-Podcast语料库上的实验结果表明，DeepEmoCluster框架在完全监督方案下取得了非常好的预测性能，在大多数情况下都优于基线方法。通过加入额外的未标记unlabeled数据集，可以进一步改进该方法。此外，我们的实验结果明确地表明，潜在簇latent clusters具有情感依赖性，丰富了对clusters的几何解释。

## 预处理

## 概述

## 结果

## 精读

识别人类的情绪状态对于现代人机交互 (HCI) 系统至关重要 [1]。语音情感识别 (SER) 在教育 [2] 和医疗保健 [3] 等各个领域也发挥着重要作用。尽管深度学习方法的最新进展已经在图像分类 [4] 和自动语音识别 (ASR) [5] 等领域带来了高性能，但 SER 仍然是一个具有挑战性的问题，在不同条件下（例如，环境、录音设置或扬声器）[6, 7]。导致性能低下的主要因素之一是训练数据量的可用性。与图像或语音识别任务相比，语音情感语料库的大小相对较小（例如，用于 SER [8] 的 IEMOCAP 语料库约为 12 小时，而用于 ASR [9] 的 LibriSpeech 语料库约为 1,000 小时）。

为了缓解这一限制，一些研究探索了利用来自多个语料库的信息的领域对抗技术domain adversarial techniques。目前已经探索的方向有，采用具有反向梯度层 reverse gradient layers[10] 的附加域分类器additional domain classifier和批评网络critic network [11] 来获得更通用的中间表征，从而减少来自不同域的不匹配现象。

其他研究也探索了数据增强方法以提高 SER 模型的稳健性，比如利用已被应用于人工合成情绪样本的生成对抗网络 (GAN) ，减少训练集分布的稀疏性 [12, 13]。然而，这些对抗性训练方法可能会遇到不稳定的收敛问题或受到数据集大小的限制。

另一种吸引人的方法是半监督学习（SSL）。 SSL 的关键概念是利用大量未标记的数据来提高监督任务的鲁棒性和性能 [14]。与标记数据不同，未标记资源的收集通常既简单又便宜。因此，很容易获得大量未标记数据的数据集，以扩充数据量很少的标记集。 SSL 方法通过使用这些未标记的数据 [15] 来学习输入分布的附加结构。在 SSL 中利用未标记数据的一种方法是利用集群假设cluster assumption，即如果输入空间中的两个数据样本属于同一个集群，那么它们很可能属于目标中的同一类或区域空间。 DeepCluster [16] 遵循这一假设，在从完全无监督的表征学习中提取判别特征方面取得了巨大成功。它利用自监督训练技术来学习基于集群cluster的伪类标签，与监督学习模型相比，它实现了具有竞争力的性能。

受 DeepCluster 框架的启发，本研究提出了一种新的 SER 方法，我们将原始的无监督结构修改为半监督框架。该方法导出情感语音簇，即-DeepEmoCluster。具体来说，我们实现了一个额外的基于监督情感属性的回归器（即唤醒、支配和效价）与无监督聚类分类器联合训练，鼓励模型在最大潜在聚类分离约束下学习情感区分内容。所提出的模型是端到端 (E2E) 卷积神经网络 (CNN) 架构（即 VGG-16 [17]），其中输入特征是 128D-mel 频谱图。我们使用 MSP-Podcast 语料库 [18] 评估我们提出的框架，使用一致性相关系数 (CCC) 作为评估模型性能的指标。结果表明，DeepEmoCluster 框架在完全监督的唤醒、效价和优势方案下实现了有竞争力的预测性能，在大多数情况下优于基线模型。我们发现 DeepEmoCluster 框架可以在使用半监督设置时进一步提高预测性能，其中加强未标记数据的信息增益有助于监督任务。作为评估的一部分，我们探索了 DeepEmoCluster 框架中所需的最佳集群数量。结果表明，应根据未标记集的大小和情感属性来微调聚类的数量。最后，我们的潜在聚类分析表明，DeepEmoCluster 方法创建了依赖于情感内容的潜在聚类，丰富了聚类的几何解释。

本文的主要贡献是用于 SER 任务的新 SSL DeepEmoCluster 框架，它是 DeepCluster 框架 [16] 的半监督变体。通过利用未标记数据并与监督网络联合训练，DeepEmoCluster 方法通过潜在表示中的显式几何解释提高了基于属性的 SER 模型性能。

SER 最近流行的趋势之一是构建 E2E 学习系统。 E2E 模型不需要预定义的手工特征，可以直接从时域波形 [19] 或频域原始频谱图 [20] 中提取情感相关特征。这些方法通常依赖于深度神经网络 (DNN)。萨特等人[20]证明了具有原始频谱图输入的 E2E SER 模型可以轻松地与降噪解决方案（例如谐波滤波）相结合，使 SER 系统能够抵抗低 SNR 环境。李等人[21]提出了一种基于频谱图特征的具有自注意力机制的多任务模型。他们的方法在 IEMOCAP 数据集 [8] 上实现了最先进的性能。 Trigeorgis 等人[19]使用 CNN-BLSTM 结构从原始波形构建了他们的 E2E 模型。关键组件是在离散时域波形上运行的一维卷积，可以将其视为去除背景噪声的特征细化系统。他们的结果表明，源自 E2E 模型的特征优于手工制作的声学特征（例如，eGeMAPS [22]）。在这项研究中，我们还采用了带有梅尔谱图输入的 E2E 模型来更好地表示情绪线索。各种研究已经探索了 SSL 和潜在表示学习方法，以将未标记的数据用于 SER 任务。邓等人[23]提出了半监督自动编码器（SSAE），它将无监督深度去噪自动编码器（DDAE）与监督学习目标相结合。他们为未标记的数据引入了一个额外的类标签，迫使模型通过结合未标记数据的先验信息来学习瓶颈潜在表示。遵循类似的概念，Latif 等人 [24]提出了一种变分自动编码器（VAE）框架，用于从语音信号中获取潜在表示。与 DDAE 相比，VAE 学习表示潜在空间中输入的概率分布，而不是在瓶颈层中压缩它们。 Parthasarathy 和 Busso [25, 26] 采用梯形网络框架（Rasmus 等人 [27] 中的Γ-model）来提高基于属性的 SER 性能。 Γ 模型对噪声编码器和解码器之间的跳跃连接进行一致性正则化，旨在获得针对噪声扰动的不变中间表示。这些方法依赖于编码器-解码器结构，其中瓶颈潜在表示没有经过训练，通过分离具有不同情感内容的数据来明确涉及强几何特性。因此，很难理解潜在空间或瓶颈层背后的机制。本研究旨在使用基于 DeepCluster 框架 [16] 的 SSL 方法创建有意义的潜在表示，该方法在不需要解码器网络的情况下强加了强大的几何约束（即集群之间的最大情感分离）。

本研究使用 MSP-Podcast 语料库 [18]，该语料库由在知识共享许可下从公开可用的播客中收集的情感丰富的自发语音录音组成。录音内容涵盖采访、体育、学术讲座、娱乐、政治等多个话题。我们通过扬声器分类工具处理这些录音，将播客分割成持续时间在 2.75 到 11 秒之间的较小的说话轮次。我们采用了许多预处理步骤来选择具有高信噪比 (SNR) 和没有重叠语音的单说话者内容的说话轮次。我们消除了带有背景噪音、音乐和电话质量语音的转弯。为了平衡语料库的情感内容并拥有情感丰富的句子，我们根据 Mariooryad 等人 [28] 建议的策略，通过情感检索算法运行语音片段。本研究使用 1.6 版的语料库，包含 50,362 个句子（83h 29m）。我们使用 amazon Mechanical turk (AMT) 使用 Burmania 等人 [29] 中讨论的众包协议的变体来注释语料库中的句子。句子被注释为它们的主要和次要情感内容（分类类别），以及情感属性唤醒（平静与活跃）、效价（消极与积极）和支配（弱与强）。本研究使用情感属性，将 SER 任务制定为回归问题。每个注释者使用自我评估模型 (SAM) 以 7 点 Likerttype 量表评估情感内容。语料库中的每个句子都有五个或更多注释，并且通过对主题的分数进行平均来获得真实标签。测试集有来自 50 个说话者的 10,124 个样本，开发集有来自 40 个说话者的 5,958 个样本，训练集有来自其余说话者的 34,280 个样本。此分区旨在保持扬声器独立集。大约有 500、000 个额外的语音片段尚未检索或注释。这些说话轮流形成了我们在语料库中未标记的数据。

### 引文

## 摘录
