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
data: 2022-04-17 14:13:05
lastmod: 2022-04-17 16:08:17
---

# 重点

- 论文源文件
- 语音识别困难的损失值的均值和方差会很大。
- 语音识别困难的数据会对最终训练后的系统产生负面影响。
- 课程式学习（由简到难学习）
- Co-teaching（两个深度学习网络相互传播和学习）解决单一简单网络可能导致的偏见问题。

# 摘要

Speech emotion recognition is a challenging task due to the ambiguity of emotion, which makes it difficult to learn the features of emotion data using machine learning algorithms. However, previous studies conventionally ignore the ambiguity of emotion and treat the emotion data as the same difficulty level, which results in low recognition accuracy. Motivated by human and animal learning studies, we propose a novel method named Progressive Co-teaching (PCT) to learn speech emotion features from simple to difficult. PCT method automatically identifies the difficulty level of data by itself using loss values, and then each network exchanges easy instances with small loss to peer network for early training. The rest instances with large loss are added gradually for later training. The experiment results demonstrate that our method achieves an improvement of 3.8% and 1.27% on MAS and IEMOCAP database than the state-of-the-arts, respectively.

由于情感的模糊性，语音情感识别是一项具有挑战性的任务，这使得使用机器学习算法学习情感数据的特征变得困难。然而，以往的研究忽略了情感的模糊性，将情感数据等同于难度水平，导致识别准确率较低。受人类和动物学习研究的启发，我们提出了一种从简单到困难学习语音情感特征的渐进式协同教学(PCT)方法。PCT方法利用损失值自动识别数据的难易程度，然后每个网络将损失较小的简单实例交换给对等网络进行早期训练。其余损失较大的实例将逐步添加，以供后续训练。实验结果表明，我们的方法在MAS和IEMOCAP数据库上分别比现有的方法提高了3.8%和1.27%。

# 词汇记录

# 结果

IEMOCAP&&MAS

![]({1}_Progressive%20Co-Teaching%20for%20Ambiguous%20Speech%20Emotion%20Recognition.assets/image-20220417160506.png)

![]({1}_Progressive%20Co-Teaching%20for%20Ambiguous%20Speech%20Emotion%20Recognition.assets/image-20220417160513.png)

# 精读

![image-20220124145043099]({1}_Progressive%20Co-Teaching%20for%20Ambiguous%20Speech%20Emotion%20Recognition.assets/image-20220124145043099.png)

**参考方法：Co-teaching**

Co-teaching方法[15]最初用来在网络训练过程中排除那些标签错误的噪声数据。在Co-teaching方法中，噪声数据的数量由R(T)%控制。如图2(A)所示，Co-teaching方法同时训练两个网络，每个小批量的数据按照损失值进行排序，丢弃R(T)%的损失值较大的实例。然后，两个网络交换剩余的实例以训练更新参数。

**改进方法：Progressive Co-teaching**

1. 解决随机数据间数据差异可能很大，会遗失有用数据。

	由于每个小批次的数据都是从已打乱数据中随机抽取的，因此数据的难度差异很大。为了解决这个问题，我们首先让每个网络计算所有训练数据的loss值，以识别每次迭代开始时所有数据的难易程度，然后得到分割后的小批量数据。

2. 模糊情感数据分割

	因为语音情感识别困难的数据，其损失值的均值和方差会很大。我们设置了损失阈值λ，对于损失值大于λ的实例会被视为hard数据，暂时不会使用。其余损失值小于λ的实例作为易处理数据回放到各个网络的小批量中。

3. 模糊数据（识别困难的数据）仍然包含有用的信息，应该在训练过程中包括在内。

	每个网络将这挑选后的小loss值的数据交换到对等网络进行训练。在网络训练过程中，网络逐渐变强，hard实例的损失值也会逐渐变小，这意味着这些实例都会被纳入到后面的训练中来训练网络。因此简单数据和hard数据都会参与网络参数的更新，这与Co-teaching方法是背道而驰的。

**Database and spectrogram**

为了验证PCT方法的有效性，我们使用了两个数据库来评估我们的方法，MAS数据库和IEMOCAP数据库[16]。

使用MATLAB频谱分析功能，利用35ms汉明窗口和四分之三窗口长度的短时傅立叶变换，将每个发音转换成语谱图。光谱图的尺寸为550×550像素。

为了验证PCT在模糊数据中的有效性，我们选择了MAS和IEMOCAP中都是相对模糊数据的30%的数据作为测试集，其余的数据作为训练集。模糊数据是基于专家的投票和数据库描述获取。

此外，我们通过测试集的整体准确率来评估每个网络的性能。

学习率：0.0001，

损失函数：交叉熵损失函数

优化函数：ADAM优化器(动量=0.9)。

batch大小：32

epoch：200

损失阈值λ：0.8

## 引文
