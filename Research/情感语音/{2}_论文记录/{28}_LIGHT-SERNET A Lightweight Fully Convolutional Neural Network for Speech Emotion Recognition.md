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
data: 2022-06-02 14:56:38
lastmod: 2023-04-11 11:53:15
date: 2022-06-02 14:56:38
---

# 重点

- [开源代码](https://github.com/AryaAftab/LIGHT-SERNET)
- 对多维数据，分路径使用特定于某维度的接受野进行卷积计算。可以减少卷积参数量， 例如分别提取时间 维度的依赖关系，频域维度的依赖关系。
- F-LOSS有时候会比CE-Loss有更高的精度，

# 摘要

Detecting emotions directly from a speech signal plays an important role in effective human-computer interactions. Existing speech emotion recognition models require massive computational and storage resources, making them hard to implement concurrently with other machine-interactive tasks in embedded systems. In this paper, we propose an efficient and lightweight fully convolutional neural network for speech emotion recognition in systems with limited hardware resources. In the proposed FCNN model, various feature maps are extracted via three parallel paths with different filter sizes. This helps deep convolution blocks to extract high-level features, while ensuring sufficient separability. The extracted features are used to classify the emotion of the input speech segment. While our model has a smaller size than that of the state-of-the-art models, it achieves a higher performance on the IEMOCAP and EMO-DB datasets.

直接从语音信号中检测情感在有效的人机交互中起着重要的作用。现有的语音情感识别模型需要大量的计算和存储资源，使得它们很难与嵌入式系统中的其他机器交互任务并行执行。本文针对硬件资源有限的语音情感识别问题，提出了一种高效、轻量级的全卷积神经网络。在所提出的FCNN模型中，通过三条具有不同滤波器大小的并行路径来提取各种特征映射。这有助于深度卷积块提取高级特征，同时确保足够的可分性。提取的特征被用于对输入语音片段的情感进行分类。虽然我们的模型比最先进的模型具有更小的尺寸，但它在IEMOCAP和EMO-DB数据集上实现了更高的性能。

# 结果

## 实验设置

在对−1和1之间的音频信号进行归一化之后，计算信号的MFCC。为此，我们使用汉明窗口将音频信号分割成具有16ms重叠的64ms帧大小，这些帧可以被认为是准平稳段。在对每一帧应用1024点快速傅立叶变换(FFT)之后，信号在40赫兹到7600赫兹的范围内接受梅尔尺度滤波器组分析。然后使用反离散余弦变换计算每一帧的MFCC，其中选择前40个系数来训练模型。

## 训练设置

基于10次交叉验证，每折经历300个历元的训练，批次大小为32。使用初始学习速率为10−4的ADAM优化器。从时段50及以上开始的学习速率每20个时段以e−0.15的速率下降。

由于缺乏足够的数据来训练模型，可能会遇到过拟合的问题，所以我们引入了正则化来解决这个问题。我们在每个卷积层之后使用批归一化，在Softmax层之前以0.3%的速率丢弃，并且对于LFLB以10−6的速率进行加权衰减(L2正则化)。

模型权值在训练时具有32位浮点精度。在对模型进行训练后，我们将训练后的模型权值的精度改为16位浮点数，将模型的规模缩小了一半。所有报告的结果都是针对具有此精度的权重。

损失函数的影响：

我们选择两个损失函数来训练所提出的模型：焦点损失（F损失）和交叉熵损失（CE损失）。提出了F损失来解决类别不平衡和具有挑战性的样本[20]。在实验中，使用γ=2的F-损耗。表1显示了EMO-DB和IEMOCAP数据集上两个损失函数的结果。与表1中的UAR相比，显示FLoss在IEMOCAP（即兴+脚本）上实现了比CE损失更高的准确度，而对于IEMOCAP（即兴）和EMO-DB数据集，CE损失表现更好。这些结果表明，模型的UAR可以提高性能，在某些情况下，CE损失简单（表1）。

并行路径的影响：在这里，我们评估并行路径对CE损失的IEMOCAP和EMO-DB数据集的影响。与单独使用每条路径相比，同时使用这三条路径分别使IEMOCAP（脚本+即兴）数据集上的WA，UAR和F1分别增加了1.38%，0.91%和1.06%。在EMO-DB数据集上，这一改进分别为1.86%，1.35%和1.57%。为了公平比较，在同时使用三条路径和单独使用每条路径时都采用了相同数量的滤波器。

输入长度的影响：由于IEMOCAP数据集话语的长度可变（即在0.58到34.13秒的范围内），我们评估了所提出的输入长度为3秒和7秒的模型。输入长度越长的主要问题是计算成本和峰值内存使用量（PMU）。输入长度为3秒和7秒的计算成本分别为322和7.6亿浮点操作（mfLOP），输入长度为3秒和7秒的PMU分别为1610和3797千字节。还发现使用7秒输入长度而不是3秒输入长度将IEMOCAP（即兴）上的评估指标增加超过2.13%，IEMOCAP（脚本+即兴）上的评估指标增加超过3.69%（表1）。

# 词汇记录

# 精读

直接从语音信号检测情绪在有效的人机交互中起着重要作用[1]。自动情绪识别可以用于各种智能设备，特别是智能对话系统和语音助理，如Apple Siri，Amazon Alexa和Google Assistant。最近，从他们的言语中识别说话者的情绪状态受到了相当大的关注[2-8]。现有的语音情绪识别（SER）方法基准主要由特征提取器和分类器组成，以获得情绪状态[2]。最近，基于深度学习（DL）的技术彻底改变了语音处理领域，并且在许多情况下优于经典方法[2,9]。基于DL的方法成功的主要原因之一是深度神经网络（DNN）通过学习过程从数据中提取复杂特征的能力[10]。特别是，与传统方法相比，卷积神经网络（CNN）在SER方面取得了显着进步[11-13]。CNN对于忽视输入信号传递的可能与目标任务无关的信息特别强大[14]。当输入是复杂的非结构化信号（例如图像或语音信号）时，此特征特别有用。


在本文中，我们提出了一种新的SER模型，它可以从Mel频率cepstral系数（MFCC）中学习频谱时间信息，该模型仅利用CNN。首先，开发了分层DL模型来自动化和替换手部工程特征的过程。事实上，我们利用三个并行CNN块从MFCC能量图中提取具有不同属性的特征。然后将提取的特征连接并馈送到深度CNN以捕获最终用softmax层分类的高级表示。所提出的模型非常轻，这使其适用于在线SER应用程序以及在资源有限的小型嵌入式系统和物联网设备上实施。与基准方法相比，CNN的使用不仅降低了模型的复杂性，而且提供了更好的泛化。我们在IEMOCAP和EMO-DB数据集上评估所提出的SER模型的实验证实，我们的模型需要相当少的参数，同时实现与现有技术模型相同或更好的性能。

在正文第一部分，将三个并行的CNN应用于MFCC，以提取时间和频谱特征。这种结构可以在其特征提取器1中实现光谱信息和时间信息之间的平衡。

![]({28}_LIGHT-SERNET_%20A%20Lightweight%20Fully%20Convolutional%20Neural%20Network%20for%20Speech%20Emotion%20Recognition@aftabLIGHTSERNETLightweightFully2022.assets/image-20220603143834.png)

在文献[15]中，分类精度与接收野大小之间存在直接关系，即接收野越大，分类精度越高。因此，我们使用以下技术来增加卷积网络的接受场：
1. 增加层数(更深的网络)，
2. 使用子采样块，例如合并或更高的步长，
3. 使用膨胀卷积，以及
4. 执行深度卷积。越深的网络有更高的感受野，因为每增加一层，感受野就增加核大小[16]。但是，增加层数会增加模型参数的数量，从而导致模型过度拟合。

对于多维信号，可以分别考虑每个维度来计算接受场[15]。因此，我们使用大小为9×1、1×11和3×3的核分别提取频谱、时间和频谱-时间依赖关系，如图2所示。与只有一条接收野大小相同的路径相比，使用这种技术的优点是将模型的这一部分的参数数量和计算成本减少了9×11(9×1+1×11+3×3)。最后，将提取的每条路径的特征拼接并馈送到主体II中。图1中的第二个框说明了主体部分I的结构。

Body Part II由几个LFLB组成，它们具有不同的配置，应用于Body Part I中串联的低级特征，以捕获高级特征。LFLB是受赵等人的工作启发的连续层的集合。[17]。该算法由卷积层、批归一化层(BN)、指数线性单元(ELU)和最大合并层组成。在我们的工作中，ELU层和最大池层分别被一个校正的线性单元(REU)和平均池所取代。最后一个LFLB使用全局平均池(GAP)，而不是平均池，使得我们的模型能够在不改变体系结构的情况下对不同长度的数据集进行训练。主体部分II的规格如图1所示。

![]({28}_LIGHT-SERNET_%20A%20Lightweight%20Fully%20Convolutional%20Neural%20Network%20for%20Speech%20Emotion%20Recognition@aftabLIGHTSERNETLightweightFully2022.assets/image-20220603143850.png)

## 引文

Yenigalla等[6]通过使用具有大卷积滤波器和音素嵌入的几个并行路径来提高识别率。

Chen等[5]使用Mel谱图，delta和delta-delta作为输入，并提出了一种基于三维注意力的卷积递归神经网络，以保持有效的情绪信息并减少无关情绪因素的影响。

Li等[3]提出了扩张残差网络和多头自我注意的组合，以减轻渐进分辨率降低中语音时间结构的损失，同时忽略超分割特征序列中元素之间的相对依赖性。

为了减少模型大小和计算成本，Zhong等[8]将神经网络的权重从原始全精度值量化为二进制值，然后可以更容易地存储和处理。

Zhong等[4]将注意力机制和焦点损失相结合，将训练过程集中在学习硬样本和减重易样本上，以解决具有挑战性的样本问题。
