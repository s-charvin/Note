---
title: "Speech Emotion Recognition with Multi-Task Learning"
description: ""
citekey: caiSpeechEmotionRecognition2021a
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:27:21
lastmod: 2023-04-11 10:58:46
---

> [!info] 论文信息
>1. Title：Speech Emotion Recognition with Multi-Task Learning
>2. Author：Xingyu Cai, Jiahong Yuan, Renjie Zheng, Liang Huang, Kenneth Church
>3. Entry：[Zotero link](zotero://select/items/@caiSpeechEmotionRecognition2021a) [URL link](https://www.isca-speech.org/archive/interspeech_2021/cai21b_interspeech.html) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Cai et al_2021_Speech Emotion Recognition with Multi-Task Learning.pdf>)
>4. Other：2021 - Interspeech 2021  ISCA   -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 利用预先训练好的Wave2vec-2.0进行语音特征提取，通过情感分类(Ser)和语音识别(ASR)两个任务对SER数据进行微调。
- 改进了训练时的loss值，额外添加了文本识别损失（CTC，忽略文本和语音长度差异，有效反向传播梯度）
- 语音识别(ASR)可以作为副产品获得。
- 最终预测时，将 Softmax 算子替换成 argmax 算子。- 论文源文件

## 摘要

> [!abstract] 
> Speech emotion recognition (SER) classifies speech into emotion categories such as: Happy, Angry, Sad and Neutral. Recently, deep learning has been applied to the SER task. This paper proposes a multi-task learning (MTL) framework to simultaneously perform speech-to-text recognition and emotion classification, with an end-to-end deep neural model based on wav2vec-2.0. Experiments on the IEMOCAP benchmark show that the proposed method achieves the state-of-the-art performance on the SER task. In addition, an ablation study establishes the effectiveness of the proposed MTL framework.

> 语音情感识别(SER)将语音分为快乐、愤怒、悲伤和中性等情感类别。最近，深度学习被应用到 SER 任务中。提出了一种同时进行语音到文本识别和情感分类的多任务学习(MTL)框架，并基于 Wav2vec-2.0建立了端到端的深度神经模型。在 IEMOCAP 基准测试平台上的实验表明，该方法在 SER 任务上达到了最好的性能。此外，一项消融研究确定了拟议的 MTL 框架的有效性。

## 预处理

## 概述

## 结果

IEMOCAP

![]({4}_Speech%20Emotion%20Recognition%20with%20Multi-Task%20Learning@caiSpeechEmotionRecognition2021a.assets/image-20220417160641.png)

## 精读

IEMOCAP

![]({4}_Speech%20Emotion%20Recognition%20with%20Multi-Task%20Learning@caiSpeechEmotionRecognition2021a.assets/image-20220304005708.png)

许多识别模型使用的频谱特征，以及韵律特征的显式表示、音质特征和基于Teager能量算子的特征[5]。这些方法需要很强的领域知识和对语音的深入理解。

**Multi-task Learning**

多任务学习使用共享架构模型，同时优化不同任务的多个目标，其优势是辅助信息和不同任务之间的能够交叉正则化(隐含地，任务 a 可以是任务 b 目标的调节器 )。同时，联合优化带来了挑战[18]。

**Wav2Vec-2.0: Pretraining with Fine-Tuning for Speech**

预训练阶段通常在无监督的情况，使用一个大数据集训练一个模型，比如 bert，让模型学习数据的有意义表示，预训练完成后，该模型就可以通过使用相对较少的带有标签的受监督的训练数据对特定的下行任务数据进行微调训练。预训练阶段所获得的信息，可以帮助训练针对下行特定任务数据的模型且不容易过拟此类特定任务的数据。

wav2vec-2.0 ，使用类似于 bert 所采用的无监督方法，通过对大量的音频数据进行预先训练来学习语音表达，试图恢复编码音频特征的随机掩码部分。经过训练之后，可以针对不同的下游任务上进行了微调。

**Model Architecture**

我们提出了一种端到端模型，输入原始语音波形，并输出预测的情感标签。

我们将预先训练的 Wav2vec-2.0模型表示为 $f(·)$ ，假设输入波形为 $x$ ，其长度为 $L$ (样本数量： $L$ )，从 Wav2vec-2.0中最后一个隐藏层得到的输出作为特征 $z$ ，即 $z=f(X)$ ，对应灰色块部分。后面 ASR 路径（使用由 V=32个字符组成的词汇表，其中有26个英文字母和几个标点符号），以 $z$ 为输入，通过一个完全连接层(FC 块) $g$ ，获得对字符的预测： $y=g(f(X))$ 。后面的另一个的 SER 路径，以 $z$ 为输入，通过池化层 P 和全连接层 h，获得对情感类的预测： $C=h(ΣP(z_{i}))$ 。在两条路径的末端，我们对 $y$ 和 $c$ 应用 Softmax 算子，以将它们转换为概率向量，然后通过 CTC 和 CrossEntropy 分别求取 ASR 和 SER 的损失，并最终联合为最终损失值 $\mathcal{L}=\mathcal{L}_{\mathrm{CE}}+\alpha \mathcal{L}_{\mathrm{CTC}}$ 。最终预测时，将 Softmax 算子替换成 argmax 算子。

### 引文

- 在早期的工作[4]中，发现支持在向量机、LDA、QDA和HMM中，支持向量机和隐马尔可夫模型的表现相对较好。人们经常发现组合方法更有效[9，10，11]，分类准确性更高。

- 作者在[12]中对CNN和LSTM结构进行了评估，发现3层卷积层加上一个双LSTM层的级联得到了最好的结果。

- 在[13]中，骨干卷积网络ResNet-101来提供更强的特征提取。

- 在文献[14]中，作者提出了一个由注意力滑动递归神经网络(ASRNN)组成的模型。

- 在文献[15]中，作者结合了编码的语言特征和声学特征，建立了一个多头自我注意模型来研究这两个特征对SER任务的影响。

- 在[16]中，作者利用了基于深度注意力的语言模型，并将停顿作为检测情绪的关键特征。

- 在[17]中，从几个方面对CNN+注意和biLSTM+注意两种模式进行了评估和比较。

- 在计算机视觉领域，[19]，同时在12个不同数据集上使用 MTL 模型，在其中的11个数据集上取得了最先进的结果。

- 在语音识别领域，[20,21]将Connectionist Temporal Classification (CTC)[22]映射层与基于注意力的解码器结合，在一个shared attention encoder（共享注意力编码器）上，执行端到端的语音识别(ASR 任务)。

- text-to-speech(TTS)模型FastSpeech-2 [23]联合使用 mel 语谱图以及韵律：音高、持续时间和能量。

- 众所周知的深度语言模型 BERT [24]在训练前阶段采用了两个任务: 掩蔽令牌预测和下一句预测。

- 对于编码任务，[25]同时根据性别和情绪对输入话语进行分类; 这种方法表现得比只预测情绪的模型更好。

- 此外，MTL与其他技术密切相关，例如迁移学习[26]和持续学习[27]。

- 深度语言模型 ERNIE-2.0 [28]在 MTL 框架中结合了持续学习框架并并在 GLUE 任务上取得了最佳结果。

## 摘录
