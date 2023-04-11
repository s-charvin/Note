---
title: "Speech Emotion Recognition with Multiscale Area Attention and Data Augmentation"
description: ""
citekey: xuSpeechEmotionRecognition2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:30:19
lastmod: 2023-04-11 11:16:13
---

> [!info] 论文信息
>1. Title：Speech Emotion Recognition with Multiscale Area Attention and Data Augmentation
>2. Author：Mingke Xu, Fan Zhang, Xiaodong Cui, Wei Zhang
>3. Entry：[Zotero link](zotero://select/items/@xuSpeechEmotionRecognition2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Xu et al_2021_Speech Emotion Recognition with Multiscale Area Attention and Data Augmentation.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：https://github.com/lessonxmk/Optimized_attention_for_SER
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 第一次引入多尺度区域注意力机制，从不同尺度处理需要 attention 数据
- 引入nlpaug library中的Vocal Tract Length Perturbation (VTLP)，利用VTLP，在语音特征层面上施加一个随机的扭曲因子，对原始数据进行处理，生成新的数据。
- 使用长方形卷积核，从时间和频域维度提取特征

思考：
- 不同注意力机制总结
	- 通道注意力
	- 空间注意力
	- 残差注意力
	- 混合注意力
	- 双重注意力
	- 自注意力
	- 类别注意力
	- 时间注意力
	- 频率注意力
	- 全局注意力
	- 高阶注意力

> [注意力机制研究现状综述（Attention mechanism） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/361893386)
>[一文看尽深度学习中的各种注意力机制 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/379501097)
>[14 - 第五节 Transformer （2022：各式各样的自注意力机制变型） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/488632024)

## 摘要

> [!abstract] In Speech Emotion Recognition (SER), emotional characteristics often appear in diverse forms of energy patterns in spectrograms. Typical attention neural network classifiers of SER are usually optimized on a fixed attention granularity. In this paper, we apply multiscale area attention in a deep convolutional neural network to attend emotional characteristics with varied granularities and therefore the classifier can benefit from an ensemble of attentions with different scales. To deal with data sparsity, we conduct data augmentation with vocal tract length perturbation (VTLP) to improve the generalization capability of the classifier. Experiments are carried out on the Interactive Emotional Dyadic Motion Capture (IEMOCAP) dataset. We achieved 79.34% weighted accuracy (WA) and 77.54% unweighted accuracy (UA), which, to the best of our knowledge, is the state of the art on this dataset.

> 在语音情感识别(SER)中，情感特征往往以不同形式的能量模式出现在谱图中。SER中经典的基于注意力的神经网络分类器通常是在固定的注意力粒度（attention granularity）上进行优化的。本文将多尺度区域注意力机制（multiscale area attention）应用于深度卷积神经网络中，以适应不同粒度的情感特征，从而使分类器能够从不同尺度的注意集合中获益。针对数据稀疏性问题，采用声道长度扰动(VTLP)进行数据增强，提高了分类器的泛化能力。在(IEMOCAP)数据集上进行实验获得了79.34%的加权准确率(WA)和77.54%的未加权准确率(UA)。

## 预处理

## 概述

## 结果

IEMOCAP

![]({15}_Speech%20Emotion%20Recognition%20with%20Multiscale%20Area%20Attention%20and%20Data%20Augmentation@xuSpeechEmotionRecognition2021.assets/image-20220417181906.png)

原始数据和基于VTLP的扩展增强数据上最大区域大小的选择。
> 当在原始数据集上训练时，最大区域大小为4x4的模型获得了最高的ACC，其次是3x3。在扩充后的数据集上训练时，最大面积为3x3的模型获得了最高的ACC。在大多数情况下，增强数据的使用带来了超过0.5%的绝对精度提升。因此，我们建议使用3x3的最大区域大小，并使用VTLP进行数据增强。

VTLP下扩充数据量对SER性能的影响。

> 随着训练中加入更多扩充数据的副本，准确率提高

使用不同 area features特征的。
> Max、Mean和Sample三种选择, Max达到最大值,Mean和Sample三种选择最小值

## 精读

![]({15}_Speech%20Emotion%20Recognition%20with%20Multiscale%20Area%20Attention%20and%20Data%20Augmentation@xuSpeechEmotionRecognition2021.assets/image-20220417182945.png)

如上图所示，本文网络结构由5个卷积层、一个attention层和一个全连接层构成。本文使用Librosa[19]提取logMel谱图作为特征，并将其送入两个平行的卷积层中，分别从时间轴和频率轴提取纹理。其中每个卷积层之后都应用了 Batch normalization。

在这一部分中，我们扩展了李彦宏等人对这一领域的关注。[13]至SER。注意机制可以看作是一种软寻址操作，它使用key-value对来表示存储在存储器中的内容，元素由地址(key)和值(value)组成。query可以匹配到根据query和key之间的相关程度从存储器中检索到的对应value的key。Query、Key、Value通常先乘以一个参数矩阵W，得到Q、K、V。公式1表示注意力分数的计算，其中DK是K[20]的维度，以防止结果太大。

![]({15}_Speech%20Emotion%20Recognition%20with%20Multiscale%20Area%20Attention%20and%20Data%20Augmentation@xuSpeechEmotionRecognition2021.assets/image-20220607171540.png)

在self-attention中，query、key和value来自同一个输入X。通过计算自我注意，模型可以关注输入不同部分之间的联系。在SER中，情感特征的分布往往跨越更大的尺度，在语音情感识别中使用自我注意提高了准确率。

然而，在常规 attention 机制下，该模型只使用预设的粒度作为计算的基本单位，例如，单词用于词级翻译模型， 网格单元用于基于图像的模型等。然而，很难知道哪种粒度最适合复杂的任务。区域注意允许模型以多个尺度和粒度进行注意，并学习最合适的粒度。如图2所示，对于连续的存储块，可以创建多个区域以适应不同的粒度，例如1x2、2x1、2x2等。为了以区域为单位计算attention，我们需要定义区域的key和value。例如，我们可以将一个area的平均值定义为key，将一个area的sum定义为value，这样就可以用一种类似于普通注意力的方式来评估注意力。(公式1)。

对大的内存块的注意力进行详尽的评估在计算上可能是令人望而却步的。对调查区域设置最大长度和最大宽度。

使用nlpaug库中的声道长度扰动(VTLP)[14]作为数据增强的手段，生成了原始数据的另外7个副本[21]，增加 IEMOCAP 的数据量。然后数据集随机分为训练集(80%的数据)和测试集(20%的数据)进行5次交叉验证。每个话语被分成2秒的片段，片段之间有1秒(训练中)或1.6秒(测试中)的重叠。以同一话语所有片段的平均预测结果作为最终结果。

### 引文

- 2014年，由han等人提出了第一个基于深度学习的SER模型。[4]。
- 最近，为了同样的目的，M.Chen等人提出了自己的观点。[5]组合卷积神经网络(CNN)和长短期记忆(LSTM)；
- X.Wu等人。[6]用胶囊网络(CapsNet)取代了CNN；
- Y.Xu等人。[7]使用GRU(Gate Recurn Unit)从帧和语音级计算特征
- S.Parthasarathy[11]使用梯形网络将无监督辅助任务和预测情绪属性的主要任务结合起来。
- 最近，人们对基于注意力的SER模型感兴趣，以获得更高的精度[8，9，12]。
- Y.Li等人。[13]建议的区域注意力，允许模型同时计算多个粒度的注意力，这一想法在SER中尚未探索。
- 数据不足阻碍了SER的进展。数据扩充已成为自动语音识别(ASR)相关领域中增加训练数据的一种流行方法[14-17]。
- 然而，它并没有受到SER的广泛关注。它用于平衡情绪类别[18]，而不是增加训练数据的总量。

## 摘录
