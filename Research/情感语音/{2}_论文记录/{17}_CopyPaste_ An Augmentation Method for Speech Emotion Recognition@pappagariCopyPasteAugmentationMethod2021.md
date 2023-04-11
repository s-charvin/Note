---
title: "CopyPaste: An Augmentation Method for Speech Emotion Recognition"
description: ""
citekey: pappagariCopyPasteAugmentationMethod2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:30:37
lastmod: 2023-04-11 11:20:12
---

> [!info] 论文信息
>1. Title：CopyPaste: An Augmentation Method for Speech Emotion Recognition
>2. Author：Raghavendra Pappagari, Jesús Villalba, Piotr Żelasko, Laureano Moro-Velazquez, Najim Dehak
>3. Entry：[Zotero link](zotero://select/items/@pappagariCopyPasteAugmentationMethod2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Pappagari et al_2021_CopyPaste.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 与只用干净的数据训练的模型相比，用噪声增强的数据训练的模型表现得更好，但在噪声环境下噪声增强的性能更好
- 预训练可以显著提高所有数据集上的模型性能
- 引入声纹识别领域的 x-vector 模型进行迁移学习。- 与只用干净的数据训练的模型相比，用噪声增强的数据训练的模型表现得更好，但在噪声环境下噪声增强的性能更好
- 预训练可以显著提高所有数据集上的模型性能
- 引入声纹识别领域的x-vector模型进行迁移学习。

## 摘要

> [!abstract] Data augmentation is a widely used strategy for training robust machine learning models. It partially alleviates the problem of limited data for tasks like speech emotion recognition (SER), where collecting data is expensive and challenging. This study proposes CopyPaste, a perceptually motivated novel augmentation procedure for SER. Assuming that the presence of emotions other than neutral dictates a speaker's overall perceived emotion in a recording, concatenation of an emotional (emotion E) and a neutral utterance can still be labeled with emotion E. We hypothesize that SER performance can be improved using these concatenated utterances in model training. To verify this, three CopyPaste schemes are tested on two deep learning models: one trained independently and another using transfer learning from an x-vector model, a speaker recognition model. We observed that all three CopyPaste schemes improve SER performance on all the three datasets considered: MSP-Podcast, Crema-D, and IEMOCAP. Additionally, CopyPaste performs better than noise augmentation and, using them together improves the SER performance further. Our experiments on noisy test sets suggested that CopyPaste is effective even in noisy test conditions.

> Data augmentation 是训练稳健的机器学习模型的一种广泛使用的策略。它部分缓解了语音情感识别(SER)等任务数据有限的问题，在这些任务中，收集数据既昂贵又具有挑战性。本文提出的 CopyPaste，假设非中性情绪的存在决定了说话人在录音中的总体感知情绪，因此含某情绪的语音和其他中性话语的串联，仍是此情绪。通过在两个深度学习模型上测试了三种 CopyPaste 方案：一个是独立训练的，另一个是从 x 向量模型(说话人识别模型)进行迁移学习的。在 MSP-Podcast、CREMA-D 和 IEMOCAP 这三个数据集上，所有三种 CopyPaste 方案都提高了 SER 性能。此外，CopyPaste 的性能比噪声增强更好，而且即使在噪声测试条件下，CopyPaste 也是有效的。

## 预处理

## 概述

## 结果

CopyPaste 方案对干净数据和噪声增强数据都是有效的。但与预先训练的 ResNet 模型相比，CopyPaste 方案在随机初始化的 ResNet 模型上获得的改进相对更高。

Clean+Noise：SER模型训练针对干净和噪声增强数据进行训练

Clean：SER模型训练仅针对CLEAN数据进行训练

括号内数据：显示与不使用CopyPaste(无CP)训练的模型相比的提高值。

No CP：表示没有CopyPaste训练的模型

## 不同数据库中不同方案得到的情感分类平均结果

表2：使用随机初始化ResNet模型得到的结果(加权F1-分数)。

![]({17}_CopyPaste_%20An%20Augmentation%20Method%20for%20Speech%20Emotion%20Recognition@pappagariCopyPasteAugmentationMethod2021.assets/image-20220419153233.png)

表3：使用针对说话人分类预训练的ResNet模型得到的结果(加权F1分数)。

![]({17}_CopyPaste_%20An%20Augmentation%20Method%20for%20Speech%20Emotion%20Recognition@pappagariCopyPasteAugmentationMethod2021.assets/image-20220419153243.png)

## 精读

在本文中假设，除了中性情绪外，其他情绪的存在决定了录音中说话人的整体感知情绪。换句话说，如果说话者在较长的发声中表达了一种非中性的情绪，即使是很短的持续时间，那么该说话者就被认为是在表达这种情绪。因此，在SER模型训练中，可以将新的串联话语（有情绪语句与中性语串联）与原始话语一起使用将提高SER性能。本文使用两个模型来评估上述假设：一个是独立训练的模型，另一个是从说话人识别模型中进行迁移学习的模型。我们遵循[14]中提出的框架来构建模型。

CopyPaste数据增强方案：

- Neutral CopyPaste (N-CP)：将有情感语音(比方说情感E)和中性语音连接起来，以产生另一种带有情感E的话语。
- Same Emotion CopyPaste (SE-CP)：将具有相同情感的两个E情感语音连接在一起以产生另一个具有情感E的语音。
- N+SE-CP：在模型训练中同时使用N-CP和SE-CP。

![]({17}_CopyPaste_%20An%20Augmentation%20Method%20for%20Speech%20Emotion%20Recognition@pappagariCopyPasteAugmentationMethod2021.assets/image-20220418213738.png)

本文 ResNet 模型由三个模块组成：帧级表征学习网络、pooling网络和语音级分类器。帧级表征学习网络对输入的帧级特征进行操作，例如Mel频率倒谱系数(MFCC)和滤波器组系数。

使用的ResNet-34[22]结构，由一系列具有残差链接的2D卷积层组成。pooling网络包括多头注意力机制，对ResNet的输出进行操作。每个头部$h$的归一化注意力权重$w_{h,t}=\frac{\exp \left(-s_{h}\left\|\mathbf{x}_{t}-\boldsymbol{\mu}_{h}\right\|\right)}{\sum_{t=1}^{T} \exp \left(-s_{h}\left\|\mathbf{x}_{t}-\boldsymbol{\mu}_{h}\right\|\right)}$，头$h$的输出嵌入向量是其输入沿时间轴的加权平均值

不同的头被设计来捕捉输入信号的不同语音方面。我们将注意力头部的输出连接起来，并将其通过一个完全连通的层，以获得总结输入的单个向量嵌入。然后，将完全连接层的输出通过语音级分类器来获得模型判决。

为了使用ResNet结构实现SER，我们训练了两个模型：一个是用随机初始化训练的模型，另一个是用预先训练好的说话人分类模型初始化的模型。我们使用23维MFCC表示作为ResNet模型的输入，并且在通过ResNet之前，应用了基于能量的语音活动检测（energy-based voice activity detection）和平均归一化（mean normalization）。在训练过程中，我们使用带有默认参数的ADAM优化器来最小化交叉熵损失函数。选择在development集上具有最佳加权F1分数的纪元在测试集上进行评估。记录测试集上3次运行的加权F1分数的平均值。

在预训练中使用了几个带有说话人标签的数据集：VoxCeleb1、VoxCeleb2、NISTSRE4-10和Switchboard数据集，总共包含大约12000名说话人。然后使用噪声和音乐增强来提高说话人的分类性能。在说话人识别领域，这种模型通常被称为x向量模型。更多详情，请参考[21]。

为了将在该模型中学习到的知识转移到SER中，我们遵循了[14]中描述的微调过程，即用一个情感鉴别层替换最终的说话人鉴别层，并进行微调以最大限度地减少情感损失。换言之，我们将预训练中学习到的权重用于除最后一层之外的所有层，然后对所有权重进行优化以进行情感分类。

在训练过程中，随机抽取128个语料，并根据情感类别标签进行了CopyPaste，并且在每个时期只对80%的batch执行CopyPaste增强。在相同的前提下，在N+SE-CP方案中，对每个时期中40%的批次遵循N-CP和SE-CP方案，相当于80%的批次具有CopyPaste增强。为了避免过度匹配，我们从每个记录中随机选取4个用于串联，而不是整个记录。我们注意到，在我们的数据集中，训练记录的平均长度不到6s。因此，我们的假设只受到可以忽略不计的可能性的影响，因为只挑选每个记录中的4s进行连接。

并且在本文中，后面通过添加来自MUSAN语料库的噪声和音乐来扩展和增加训练数据[23]，即由训练集分别添加10、5和0分贝的噪声和音乐后得到6个副本。其中由干净和扩充数据组成的数据集训练的模型称为Clean+Noise。由于研究人员表明，与干净的测试数据相比，在有噪声的测试数据上向训练数据添加噪声的有效性更明显[24]，因此本文在有噪声的测试条件下比较了噪声增强和CopyPaste。但由于情感数据集通常是干净的，并且具有较高的信噪比，因此考虑在测试数据中添加噪声。，共创建了两组测试数据，一组信噪比为10分贝，另一组为0分贝，用于与CopyPaste进行比较。

### 引文

- 一些例子，如[5，6，7，8]，探索了标准特征表示，如MFCC和OpenSMILE[9]特征与深度学习模型，如CNN和LSTM的使用。
- 很少有研究使用原始波形或语谱图作为输入，探索联合学习语音表征的情感识别模型[10，11，12]。
- 很少有其他研究小组探索利用具有与情绪无关的注释的大型数据集，如音素和说话人身份标签[13，14]。在这方面，作者在[13]中表明，在训练用于预测音素的ASR模型中学习的知识可以转移到SER。类似地，从诸如X向量模型的说话人识别模型中提取的特征被示出为包含情感信息[14]。
- ResNet34体系结构[14, 21, 22]
- 在[14，16]中表明，在干净的录音中添加噪音有助于模型更好地识别情绪。改变说话速度[16]和声道长度扰动[17]也有助于SER。
- 预训练显著提高了所有数据集上的模型性能，就像在[14]中的情况一样。
- 与只用干净的数据训练的模型相比，用噪声增强的数据训练的模型表现得更好，这与之前的研究证实了[14，16]。
- 很少有研究[18，19]冒险使用先进的技术，如CycleGans和StarGans来产生情感语音特征。
- 在这方面，一些作者观察到，当情绪中立的语音片段和情绪E的情绪片段按顺序播放时，人类听众通常将整个序列归类为情绪E[20]。
- x向量模型[21]。
- 由于研究人员表明，与干净的测试数据相比，在有噪声的测试数据上向训练数据添加噪声的有效性更明显[24]

## 摘录
