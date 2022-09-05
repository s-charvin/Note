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
data: 2022-04-17 14:13:45
lastmod: 2022-04-17 16:07:40
---

# 重点

- 建立线性投影矩阵获取不同语料库的共有特征子空间
- 使用联合正规化特征分布的MMD距离，缓解原始特征分布差异。
	- 正规化的特征差异，含数据总体平均差异及每类情感的平均差异的联合差异分布。
	- 正规化的区分语音信号中包含的情绪不同投影向量。


# 摘要

In this paper, we focus on the research of cross-corpus speech emotion recognition (SER), in which the training and testing speech signals in cross-corpus SER belong to dierent speech corpus. Due to this fact, mismatched feature distributions may exist between the training and testing speech feature sets degrading the performance of most originally well-performing SER methods. To deal with cross-corpus SER, we propose a novel domain adaptation (DA) method called joint distribution adaptive regression (JDAR). The basic idea of JDAR is to learn a regression matrix by jointly considering the marginal and conditional probability distribution between the training and testing speech signals and hence their feature distribution dierence can be alleviated in the subspace spanned by the learned regression matrix. To evaluate the proposed JDAR, we conduct extensive cross-corpus SER experiments on EmoDB, eNTERFACE, and CASIA speech databases. Experimental results show that the proposed JDAR achieves satisfactory performance and outperforms most of state-of-the-art subspace learning based DA methods.

本文主要研究跨语料库语音情感识别技术，其中跨语料库语音情感识别中的语音信号属于不同的语料库。由于这一事实，在训练和测试语音特征集之间可能存在不匹配的特征分布，从而降低了大多数最初表现良好的SER方法的性能。为了处理跨语料库SER，我们提出了一种新的领域适应(DA)方法，称为联合分布自适应回归(JDAR)。JDAR的基本思想是通过联合考虑训练和测试语音信号之间的边缘概率分布和条件概率分布来学习回归矩阵，从而在学习的回归矩阵所跨越的子空间中缓解它们的特征分布差异。为了评估所提出的JDAR，我们在EmoDB、eNTERFACE和CASIA语音数据库上进行了广泛的跨语料库SER实验。实验结果表明，JDAR取得了令人满意的性能，并优于大多数基于子空间学习的DA方法。

# 词汇记录

# 结果

EmoDB<>eNTERFACE<>CASIA

![]({3}_@Cross-Corpus%20Speech%20Emotion%20Recognition%20Using%20Joint%20Distribution%20Adaptive%20Regression.assets/image-20220417160424.png)

![]({3}_@Cross-Corpus%20Speech%20Emotion%20Recognition%20Using%20Joint%20Distribution%20Adaptive%20Regression.assets/image-20220417160432.png)

# 精读：

domain adaptation (DA) method

1. 不同语料库的情况下,训练和测试语音信号之间可能存在很大的特征分布差距，导致这些SER方法的性能迅速下降。

本文从共有特征子空间学习（不同高维数据的低维子特征空间的重合部分）的角度，提出了一种联合分布自适应回归(JDAR)方法，建立了一个分析不同语料库不变量的线性回归模型，以学习源和目标语音信号的共有回归矩阵，再利用共有回归矩阵，投影的目标语音特征，获取能区分语音信号中的不同情感的区别性信息。
$$\min _{\mathbf{P}}\left\|\mathbf{L}_{s}-\mathbf{P}^{T} \mathbf{X}_{s}\right\|_{F}^{2}+\lambda f_{1}(\mathbf{P})+\mu f_{2}(\mathbf{P})$$
2. 源语音样本和目标语音样本之间的原始不匹配特征分布

更重要的是，学习的回归矩阵由于采用了联合特征分布自适应正则化项，使得源语音样本和目标语音样本之间的原始不匹配特征分布能够在标签空间得到有效缓解。
$$f_{1}(\mathbf{P})=\left\|\frac{1}{N_{s}} \sum_{i=1}^{N_{s}} \mathbf{P}^{T} \mathbf{x}_{s}^{i}-\frac{1}{N_{t}} \sum_{j=1}^{N_{t}} \mathbf{P}^{T} \mathbf{x}_{t}^{j}\right\|_{2}^{2}+\sum_{j=1}^{C}\left\|\frac{1}{N_{s_{j}}} \sum_{i=1}^{D_{s_{j}}} \mathbf{P}^{T} \mathbf{x}_{s_{j}}^{i}-\frac{1}{N_{t_{j}}} \sum_{i=1}^{N_{t_{j}}} \mathbf{P}^{T} \mathbf{x}_{t_{j}}^{i}\right\|_{2}^{2}$$
$$\quad f_{2}(\mathbf{P})=\left\|\mathbf{P}^{T}\right\|_{2,1}$$

使用语料库：EmoDB[8]、eNTERFACE[9]和CASIA[10]






本文研究了跨语料库检索问题，提出了一种简单而有效的方法--JDAR。JDAR的优势主要包括两个方面。首先，通过使用回归矩阵，强制源和目标语音特征在包含语音情感标签信息的子空间中共享相似的特征分布。其次，在对学习的回归矩阵进行投影时，我们还可以提取出对语音有贡献的特征，这些特征不仅有助于区分语音信号中的不同情感，而且有助于对抗源语音信号和目标语音信号之间存在的语料库差异。在三个广泛使用的语音情感语料库上进行了使用不同语音特征集的广泛的跨语料库SER实验。实验结果表明，JDAR方法的整体性能优于现有的DA方法，适用于处理跨语料库的SER问题。



## 引文

- 例如，在[4]中，Schuller等人的工作。使用五种特征归一化方案对现有的大量语音语料库进行了跨语料库的SER研究，这可能是本课题最早的研究。
- 随后，Hassan et al.。[5]提出了一种改进的支持向量机(SVM)，称为重要性加权支持向量机(IW-SVM)，用于处理跨语料SER问题。
- 近年来，邓等人提出了自己的观点。[6，7]设计了一系列基于自动编码器的无监督领域自适应(DA)方法来处理跨语料库SER任务。这些方法的基本思想是学习一个用于训练和测试语音信号的共享子空间，以迫使它们在该子空间中的特征分布差距被缩小。
