---
title: "Audio-Visual Domain Adaptation Feature Fusion for Speech Emotion Recognition"
description: ""
citekey: weiAudioVisualDomainAdaptation2022
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-04-12 13:32:26
lastmod: 2023-04-12 13:50:44
---

> [!info] 论文信息
>1. Title：Audio-Visual Domain Adaptation Feature Fusion for Speech Emotion Recognition
>2. Author：Jie Wei, Guanyu Hu, Xinyu Yang, Anh Tuan Luu, Yizhuo Dong
>3. Entry：[Zotero link](zotero://select/items/@weiAudioVisualDomainAdaptation2022) [URL link](https://www.isca-speech.org/archive/interspeech_2022/wei22b_interspeech.html) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Wei et al_2022_Audio-Visual Domain Adaptation Feature Fusion for Speech Emotion Recognition.pdf>)
>4. Other：2022 - Interspeech 2022  ISCA   -   

>- :luc_github: 论文实现：https://github.com/Janie1996/AV4SER
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：

## ⭐ 重点

- :fas_question:   
- :obs_pdf_file:   
- :obs_graph_glyph:   
- :obs_wand_glyph:   

## 摘要

> [!abstract] 
> Speech emotion recognition has made significant progress in recent years, in which feature representation learning has been paid more attention, but discriminative emotional features extraction has remained unresolved. In this paper, we propose MDSCM - a Multi-attention based Depthwise Separable Convolutional Model for speech emotional feature extraction that can reduce the feature redundancy through separating spatialwise convolution and channel-wise convolution. MDSCM also enhances the feature discriminability by the multi-attention module that focuses on learning features with more emotional information. In addition, we propose an Audio-Visual Domain Adaptation Learning paradigm (AVDAL) to learn an audiovisual emotion-identity space. A shared audio-visual representation encoder is built to transfer the emotional knowledge learned from the visual domain to complement and enhance the emotional features that only extracted from speech. Domain classifier and emotion classifier are used for encoder training to reduce the mismatching of domain features, and enhance the discriminability of features for emotion recognition. The experimental results on the IEMOCAP dataset demonstrate that our proposed method outperforms other state-of-the-art speech emotion recognition systems, achieving 72.43% on weighted accuracy and 73.22% on unweighted accuracy. The code is available at https://github.com/Janie1996/AV4SER.

> 语音情感识别近年来取得了重大进展，其中特征表示学习受到更多关注，但判别性情感特征提取仍未解决。在本文中，我们提出了 MDSCM——一种用于语音情感特征提取的基于多注意力的深度可分离卷积模型，它可以通过分离空间卷积和通道卷积来减少特征冗余。 MDSCM 还通过多注意力模块增强了特征可辨别性，该模块侧重于学习具有更多情感信息的特征。此外，我们提出了一种视听域适应学习范式 (AVDAL) 来学习视听情感身份空间。构建了一个共享的视听表示编码器来传输从视觉领域学习的情感知识，以补充和增强仅从语音中提取的情感特征。领域分类器和情感分类器用于编码器训练，以减少领域特征的不匹配，增强情感识别的特征可辨别性。 IEMOCAP 数据集上的实验结果表明，我们提出的方法优于其他最先进的语音情感识别系统，加权准确率达到 72.43%，未加权准确率达到 73.22%。代码可在 https://github.com/Janie1996/AV4SER 获得。

## 预处理

## 概述

## 结果

## 精读

语音情感识别（SER）旨在从语音中自动识别人类的情绪状态。它是下一代人机交互的重要技术，在安全驾驶监控、社交机器人和推荐系统等方面具有潜在应用[1,2,3]。在本文中，我们专注于利用有区别的情感特征来提高 SER 系统的性能。

从语音中提取有区别的情感特征并非易事。随着卷积神经网络 (CNN) 在图像和语音分类中的应用，从语音中提取深层情感特征引起了研究人员的兴趣 [4, 5, 6, 7]。权等人。 [6] 提出了一种双流特征提取模型，其中每个流都与 CNN 架构相关联。 Sajjad 等人。 [7] 提出使用更大的 CNN 作为显着特征提取的骨干网络。然而，一些研究 [8, 9] 表明，多层 CNN 叠加后获得的特征往往存在大量冗余，这可能会影响特征的可辨性。

为了解决上述问题，我们提出了一种基于多注意力的深度可分离卷积模型 (MDSCM) 用于语音情感特征提取，该模型基于空间方向和通道方向卷积可以完全解耦的假设 [10]。首先，使用独特的卷积核为每个输入通道学习空间相关性，以在减少冗余的同时保留各个通道的独立特征。其次，采用逐点卷积来学习跨通道相关性并增强特征多样性。第三，MDSCM 从通道、空间和时间因素考虑特征差异，利用多注意模块学习情感相关性较高的信息，最大限度地发挥重要特征的优势，获得具有判别力的情感特征。

SER 任务前提下的另一个挑战是单一语音模态作为推理阶段输入的限制。因此，大多数 SER 研究只关注训练阶段的语音情感特征提取 [11, 12, 13]，而忽略了在训练阶段可以使用多模态数据来丰富情感特征学习的事实。最近的多模态情绪识别研究表明，从多模态数据中提取的情绪特征具有更好的可辨别性 [14,15,16]。然而，这些系统受到同时存在的相关模态的严重限制，并且缺少特定模态可能会对系统造成损害。最近，Albanie 等人。 [17] 使用跨模态学习通过联合特征学习和跨模态关系建模来转移知识来解决该问题。具体来说，他们提出通过面部情绪识别网络的跨模态知识蒸馏来学习语音特征表示。然而，这种方法首先需要一个强大的教师网络，这也是一个复杂的挑战。此外，学生网络的性能低于教师网络，在推理阶段可能无法达到预期的性能。

基于上述见解，在本文中，我们还提出了一种视听域适应学习范式 (AVDAL)，用于构建视听情感身份空间 (ave)，以实现从视频到音频模态的情感知识迁移。具体来说，我们构建了一个音频-视觉表示编码器 (AVRE) 来联合训练语音和视频数据，将语音和视频信息嵌入到一个紧凑的特征编码空间中。由于这个空间可以学习额外的领域知识，我们借用领域适应的思想[18]通过梯度反转层消除语音和视频域之间的差异，同时强制语音和视频嵌入共享相同的分布。此外，为了获得 ave 空间，我们添加了情感分类器以使 AVRE 能够共享情感信息。值得注意的是，由于音频和视频模态在此范例中共享相同的编码器，因此可以通过仅输入单模态数据来将数据映射到平均空间。在我们实验的推理阶段，我们只能使用语音作为 AVRE 的输入来获得从语音到 ave 空间的情感特征映射，其中包含互补的视觉知识。

### 引文

## 摘录
