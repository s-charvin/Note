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
lastmod: 2023-04-12 20:36:43
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

在本节中，介绍了所提出的方法。如图1所示，整个框架包括三个模块：语音情感特征提取、音视频情感表征提取和情感识别。 1）语音情感特征提取：我们提出了一种基于多注意的深度可分离卷积模型（MDSCM）来从语音中提取有区别的情感特征； 2) 视听情感表征提取：我们基于提出的 AVDAL 范式学习视听情感识别空间，从视频中传输情感信息以增强语音情感特征提取； 3) 情绪识别：我们融合了从 MDSCM 和 AVRE 中提取的两个特征，并将其输入 LSTM 以识别情绪。

语音情感特征提取是 SER 的核心。在本文中，我们提出了一种基于多注意力的深度可分离卷积模型 (MDSCM)，用于从语音中提取有区别的情感特征。 MDSCM 由卷积模块和注意力模块构成。

准确地说，卷积模块由两个卷积层和四个 Depthwise Separable Convolutional (DSC) 层组成；注意模块由三个注意层组成。我们从语音中提取 log Mel-filterbank 声谱图 S ∈ RM×t，其中 M 表示滤波器的数量，t 表示帧的数量。添加滑动窗口将 S 划分为子序列 {S1, S2, . . . , Sn}，其中 Si ∈ RM×T 作为 MDSCM 的输入，T 是窗口长度。这些子序列是按时间顺序排列的。

卷积模块。每个子序列 Si 被送入卷积模块。通过两个卷积层得到特征Fi，经过四个DSC层得到特征F D i 。值得注意的是，与传统的卷积相反，DSC 是基于空间卷积和通道卷积可以完全解耦的假设 [10]。输入的每个通道都用唯一的卷积核进行卷积；然后将得到的特征通过逐点卷积进行卷积，即1×1卷积核。具体来说，第一个DSC层的操作如图2所示，输入特征Fi∈RC×H×W的每个通道Ci与核K1∈RC×h×w的对应通道进行卷积运算，得到feature FSi ∈ RC×H1×W1 保留了每个通道的独立特性也减少了冗余。其次，FSi的所有元素乘以1×1卷积核K2∈RC1×1×1得到FCi∈RC1×H1×W1，学习了跨通道相关性并增强了特征多样性。其他三个DSC层的操作与上述一致，得到最终特征F D i ∈ RC′×H′×W′。

注意模块。考虑到不同特征的贡献可能不同，注意力模块被提出来更加关注具有显着情感信息的特征。特征F D i用于通过通道、空间和时间注意层序列计算情感显着值以获得判别特征fsi∈Rd，其中d是特征维度。详情如下： 1) Channel attention layer。 F D i 的空间维度首先通过PooL操作进行压缩，得到Cp i ∈ RC′。然后计算每个通道的注意力权重 M p i ∈ RC′。输入 F D i 乘以 M p i 得到输出 FC i ∈ RC′×H′×W ′：

其中(W0, b0, W1, b1)分别表示全连接层的权重和偏置，⊙表示矩阵乘法。 2）空间注意层。 F C i 的通道维度通过 PooL 操作压缩得到 Sp i ∈ RH′×W ′ 。并针对不同区域计算注意力权重 M s i ∈ RH′×W ′。然后我们使用输入 F C i 乘以 M s i 得到 F S i ∈ RC′×H′×W ′：

其中 Convk1×k2 表示卷积运算，k1×k2 是内核大小。 3）时间注意层。由于频谱图 Si ∈ RM×T 具有牢固的时间关系，我们将更多注意力放在不同帧的贡献上。 F S i 沿T轴展开得到F T i = [F 1 i ,F2 i ,...,FW′ i ]，使用transformer[19]的自注意力机制计算注意力权重wt i 。然后，经加权求和后得到fsi ∈ Rd。注意力权重计算公式如下：

其中 Q、K、V 分别用作查询、键和值。 (WQ, WK , WV ) 是参数矩阵，dk 是比例因子。



在训练阶段，为了增强从语音中提取的情感特征的丰富性，我们考虑学习和迁移视频模态的情感知识。我们提出了 AVDAL 范式来学习联合视听嵌入空间 ave，它探索模态之间的相关性，AVDAL 的细节如图 3 所示。

具体来说，我们对视频进行统一采样，得到序列 {V1, V2, . . . , Vn}，其中 Vi 代表视频帧。我们构建了一个视听表示编码器 AVRE。语音频谱图Si和视频帧Vi作为输入联合训练AVRE，编码过程数学描述如下：

情感分类器 De 遵循 AVRE 以将提取的语音特征限制为接近具有相同情感类别的提取视频特征，强制这些特征表示在平均空间中共享相同的分布。经过探索语音和视频模态之间的相关性，编码器 AVRE 消除了 Si 和 Vi 之间的视听差距，并传输训练视频数据的情感信息以辅助 SER 任务。然而，不可忽视的是，AVRE 还学习了其他非情感信息，尤其是两种模态之间的域属性，这可能会影响平均空间的优化。因此，我们借用领域适应的思想[18]。添加域分类器 Dd 以消除域信息以获得更紧凑的特征表示。

域分类器 Dd 以 eis 和 eiv 作为输入，使用全连接层解决区分输入是语音还是视频的二元分类任务。请注意，我们的最终目标是消除域信息的特征表示，这与 Dd 的目的相反。因此，在 AVRE 和 Dd 之间增加了一个梯度反转层，旨在通过在反向传播过程中乘以一个负常数来反转梯度符号。它可以约束从语音和视频中提取的特征表示是紧凑的，防止 AVRE 区分语音和视频。因此，我们获得了消除域信息的特征表示。

总之，编码器 AVRE、情感分类器 De 和领域分类器 Dd 是联合训练的。损失函数 L 可以写成：

Le 和 Ld 是 De 和 Dd 的损失函数，其中 pi 表示输入被正确分类的概率，yi 和 y'i 表示域标签和输入数据的预测概率，N 是训练数据的数量。


在 MDSCM 和 AVRE 提取情感特征后，我们将两种类型的特征连接起来，表示为 {X1, X2, . . . , Xn}。由于说话者的情绪状态是连续的，结合相邻的时刻信息有助于准确识别情绪，我们使用 LSTM 网络来学习连续帧之间的时间关系。此外，考虑到某些片段可以强烈反映情绪状态，而其他片段（例如噪声）表现力较弱，因此在学习时间关系期间使用自我注意机制[19]来捕获显着的情绪片段。

### 引文

## 摘录
