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
data: 2022-06-02 14:56:46
lastmod: 2022-06-03 21:53:26
---

# 重点

- [开源代码](https://github.com/winston-lin-wei-cheng/DeepEmoClusters)
- 

# 摘要

Semi-supervised learning (SSL) is an appealing approach to resolve generalization problem for speech emotion recognition (SER) systems. By utilizing large amounts of unlabeled data, SSL is able to gain extra information about the prior distribution of the data. Typically, it can lead to better and robust recognition performance. Existing SSL approaches for SER include variations of encoder-decoder model structures such as autoencoder (AE) and variational autoecoders (VAEs), where it is difficult to interpret the learning mechanism behind the latent space. In this study, we introduce a new SSL framework, which we refer to as the DeepEmoCluster framework, for attribute-based SER tasks. The DeepEmoCluster framework is an end-to-end model with mel-spectrogram inputs, which combines a self-supervised pseudo labeling classification network with a supervised emotional attribute regressor. The approach encourages the model to learn latent representations by maximizing the emotional separation of K-means clusters. Our experimental results based on the MSP-Podcast corpus indicate that the DeepEmoCluster framework achieves competitive prediction performances in fully supervised scheme, outperforming baseline methods in most of the conditions. The approach can be further improved by incorporating extra unlabeled set. Moreover, our experimental results explicitly show that the latent clusters have emotional dependencies, enriching the geometric interpretation of the clusters.

半监督学习(Semi-supervised learning， SSL)是解决语音情感识别系统泛化问题的一种有效方法。通过利用大量未标记的数据，SSL能够获得有关数据先前分布的额外信息。通常，它可以带来更好的和健壮的识别性能。现有的SSLSER方法包括不同的编解码器模型结构，如自动编码器(AE)和变分自动编码器(VAES)，其中很难解释潜在空间背后的学习机制。在这项研究中，我们为基于属性的SER任务引入了一个新的SSL框架，我们称之为DeepEmoCluster框架。DeepEmoCluster框架是一个端到端模型，具有MEL谱图输入，它结合了一个自我监督的伪标记分类网络和一个监督的情感属性回归。该方法通过最大化K-Means聚类的情感分离来鼓励模型学习潜在表征。我们在MSP-Podcast语料库上的实验结果表明，DeepEmoCluster框架在完全监督方案下取得了竞争性预测性能，在大多数情况下都优于基线方法。通过加入额外的未标记集合，可以进一步改进该方法。此外，我们的实验结果明确地表明，潜在簇具有情感依赖性，丰富了对簇的几何解释。

# 结果

# 词汇记录

# 精读

## 引文
