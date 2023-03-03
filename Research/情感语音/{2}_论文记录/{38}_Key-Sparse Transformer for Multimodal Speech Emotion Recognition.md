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
data: 2022-06-02 14:56:55
lastmod: 2022-06-12 19:17:07
---

# 重点

- 开源代码

# 摘要

Speech emotion recognition is a challenging research topic that plays a critical role in human-computer interaction. Multimodal inputs further improve the performance as more emotional information is used. However, existing studies learn all the information in the sample while only a small portion of it is about emotion. The redundant information will become noises and limit the system performance. In this paper, a keysparse Transformer is proposed for efficient emotion recognition by focusing more on emotion related information. The proposed method is evaluated on the IEMOCAP and LSSED. Experimental results show that the proposed method achieves better performance than the state-of-the-art approaches.

语音情感识别是一个极具挑战性的研究课题，在人机交互中起着至关重要的作用。随着更多的情感信息被使用，多通道输入进一步改善了性能。然而，现有的研究学习了样本中的所有信息，而只有一小部分是关于情绪的。冗余信息会成为噪声，限制系统的性能。本文通过更多地关注情感相关信息，提出了一种基于密钥稀疏变换的情感识别算法。在IEMOCAP和LSSED上对该方法进行了评估。实验结果表明，该方法取得了比现有方法更好的性能。

# 结果

数据集：IEMOCAP和LSSED

Experimental setup：

预训练的wav2vec 和 RoBERTa取自[https://github.com/pytorch/fairseq](https://github.com/pytorch/fairseq)

音频和文本特征序列的最大长度分别被设置为460和20。

SGD优化器学习速率设置为5×10−4和1×10−4对模型进行优化。

每30个epoch，学习率下降到原来的50%。利用p=0.5的Dropout来减小过拟合度。
批次大小为32。

特征提取模块中的Vanilla Transformers个数为5个，深度融合模块中的KS-Transformers个数为2个。多头注意采用8个注意力头部。通道交互模块中使用的CCAB数量使用0-4个，其中3为最好，如图所示。

![]({38}_Key-Sparse%20Transformer%20for%20Multimodal%20Speech%20Emotion%20Recognition@chenKeySparseTransformerMultimodal2022.assets/image-20220612184405.png)

# 词汇记录

# 精读

语音情感识别(SER)正迅速成为人机交互(HCI)的重要工具[1]。Ser还揭示了自闭症和老年人护理等统称为医疗保健的问题[2]。例如，患有严重言语和语言障碍的人难以表达自己的情绪。情感识别系统可以帮助患者进行治疗，提高他们的情感交流技能。语音是多模式的，因为它本质上包含文本信息。最新的研究[3，4]也证明了多模方法优于单模方法。因此，多式联运SER成为近年来的研究热点

在本文中，我们使用Transformer作为基本结构来实现情感识别。然而，很少有作品注意到，音频或文本中并不是所有的信息都与情感有关。例如，考虑一篇文章“好吧，看，这是一个美丽的一天。我们为什么要争论呢？“。在IEMOCAP[16]中，Vanilla Transformer中的注意力权重如图1所示。我们可以看到Transformer中的注意力权重被分配给所有单词。然而，“美丽”和“争论”这两个词在这句话中包含了大部分的情感信息。而与情感无关的单词，如it、a、Look等，对于SER任务来说是不必要的，成为噪声，导致系统性能的限制。为了解决这个问题，我们提出了一种新的方法，称为键稀疏转换器(KS-Transformer)，来判断样本中每个单词或语音帧的重要性，帮助模型更多地关注与情感相关的信息。在KS-Transformer的基础上，进一步设计了级联交叉注意块，实现了不同模式的高效融合。

·我们提出了KS-Transformer来判断每个帧或词的重要性，从而帮助模型更加关注情感信息。在KS-Transformer的基础上，我们进一步设计了级联交叉注意块来实现不同通道之间的交互。
·我们在IEMOCAP和LSSED上对该方法进行了评估，结果表明该方法比现有的最新方法取得了更好的结果。


建议的模型，如图所示，主要由三个模块组成。其中，特征提取模块用于学习输入特征，通道交互模块用于学习交互信息，深度融合模块旨在将音频和文本中的信息进一步结合。具体地说，第一个模块(灰色部分)基于Vanilla Transformer，后两个模块(黄色部分)基于KS-Transformer。

![]({38}_Key-Sparse%20Transformer%20for%20Multimodal%20Speech%20Emotion%20Recognition@chenKeySparseTransformerMultimodal2022.assets/image-20220612184832.png)

Vanilla Transformer

vanilla transformer最初由编码器和解码器组成。在本文中，我们使用Transformer来表示编码器部分，因为它是实现我们所提出的体系结构所需的部分。Transformer的输入分为Q、K和V，分别由Query, Key 和 Value组成。具体表现形式如下：

$$
\boldsymbol{W}=\operatorname{softmax}\left(\frac{\boldsymbol{Q} \boldsymbol{K}^{T}}{\sqrt{d_{Q}}}\right)
$$
$$
\boldsymbol{a t t n}=W \times V
$$

Key-Sparse attention mechanism

key-sparse Transformer的目标是自动发现情感信息。假设Q中的查询向量个数为i，而K中的键向量个数为j，则键稀疏注意机制如图所示。需要注意的是，Transformer中的K和V总是相同的。

![]({38}_Key-Sparse%20Transformer%20for%20Multimodal%20Speech%20Emotion%20Recognition@chenKeySparseTransformerMultimodal2022.assets/image-20220612185158.png)

KSTransformer中使用的key-sparse注意机制能够自动判断每个语音帧或单词的重要性。如图所示，权重矩阵W是通过将Q和K相乘得到的，W中的每一行都是V中值向量的权重。由于值向量表示音频中的帧或文本中的单词，所以我们将相同值向量的所有权重相加，并将求和用作语音帧或单词在样本中的重要性的判别器。我们选择前k个求和最大的k个值向量，并保持它们在权重矩阵中的关注度不变，而将其余的重置为零。这种操作使得权重矩阵从稠密到稀疏，减少了冗余度，这就是为什么我们将这里使用的Transformer称为KS-Transformer。通过如下公式计算top-k掩码。

$$
\boldsymbol{M}_{\mathbf{z}}= \begin{cases}0 & \text { if } s_{z}<\text { threshold } \\ 1 & \text { if } s_{z} \geq \text { threshold }\end{cases}
$$

Modality interaction module

由于通道交互模块是基于级联交叉注意块(CCAB)的，因此我们首先介绍了CCAB的结构。

![]({38}_Key-Sparse%20Transformer%20for%20Multimodal%20Speech%20Emotion%20Recognition@chenKeySparseTransformerMultimodal2022.assets/image-20220612185801.png)

如图左侧所示，CCAB是两个KS转换器的级联，其中，第一个KS转换器从通道A创建Q，从通道B创建K、V。使用这种特殊的输入方法，键稀疏注意机制将找出B中与A最相关的部分，并产生组合了A和B信息的输出。由于不同通道之间的情绪信息往往是互补的[3，17，18]，A和B都不能代表准确的情绪。因此，CCAB中的第二个KSTransformer将融合的特征作为输入，并在应用键稀疏注意时考虑来自通道A和通道B的信息。得益于CCAB，A和B被更全面和准确地融合。

如图右侧所示，通道交互模块由一堆CCAB组成，其中后者将前一个CCAB的输出作为Q输入，而K和V输入始终来自通道B。来自B的信息经过一个CCAB被视为一次交互，因为来自B的信息通过key-sparse注意流入A。多个CCAB应用于多次交互。为了保证特征的稳定性，采用了跳跃连接。

Deep fusion module

大多数研究采用融合特征来预测互动后的情绪[12，19]。然而，我们认为融合的特征可能并不是最好的，可以深度融合以进一步提高系统的性能。具体而言，深度融合模块由多个KS-Transformers组成，它们以融合后的特征为输入，利用键稀疏注意力来增强音频和文本之间的交互，实现深度融合。

![]({38}_Key-Sparse%20Transformer%20for%20Multimodal%20Speech%20Emotion%20Recognition@chenKeySparseTransformerMultimodal2022.assets/image-20220612190651.png)

为了验证关键稀疏注意的有效性，我们以IEMOCAP中的一个样本为例，通过可视化的方式比较了Vanilla Transformer和KS-Transformer中的注意力权重。如图所示，Vanilla Transformer记录了所有单词，包括与情感无关的嘈杂单词，并有过度适应的趋势。然而，KS-Transformer使连接从密集变为稀疏，它能够忽略大多数噪声，更多地关注情感信息。同时，KS-Transformer的稀疏性可以降低模型的复杂性，减少过拟合度。

为了探索KS-Transformer中的最佳稀疏性，我们将k从0.1变化到0.9。我们设置的k越大，重置为零的关注度权重就越少，稀疏性也就越小。由于LSSED存在样本不平衡的问题，我们使用未加权准确度(UA)作为衡量标准。结果如图6所示。由于IEMOCAP是一个相对较小的语料库，当k大于0.5时，模型容易过度拟合，导致UA分数保持不变。然而，在大规模数据集LSSED上，由于冗余信息的存在，当k>0.5时，会出现显著的下降。相反，当k小于0.5时，模型使用的信息量太少，并且可能收敛到不满意的局部最小值。考虑到IEMOCAP和LSSED语料库上的UA性能曲线，k被设置为0.5，这意味着每个KS-Transformer中默认为50%的关注度权重被重置为零。

通道交互对于多通道系统是至关重要的。为了研究CCAB堆栈的有效性，我们将使用的CCAB数量从0更改为4，其中0表示移除了通道交互模块，结果如表1所示。加权准确度(WA)和UA作为标准。应当指出的是，所使用的CCAB数量代表进行互动的次数。从表1中我们可以看出，当只应用一种CCAB时，不同模式之间的相互作用是肤浅和不足的。性能随着CCAB数量的增加而提高。当数目为3时，性能最好，这证实了CCAB的有效性和多次交互的必要性。

## 引文

Yoon等人。[5]利用双递归神经网络对音频和文本信息进行融合。

以同样的方式，Krishna等人。[6]使用原始音频波形作为音频特征，将手套词嵌入作为文本特征进行多模式学习。
此外，

Peri et al.。[7]结合音视频信息，利用多任务设置进行情感识别。

预训练的自监督学习在自然语言处理[8，9]和语音识别[10]等领域都取得了巨大的成功。

同时，最近的工作[11，12]使用了SSL模型，在SER中取得了令人振奋的结果。

目前，Wav2vec[10]和Roberta[9]是文献中最常用的预训练的SSL模型。

受注意力机制的启发，Transformer[13]在长序列建模方面表现突出，并在自然语言处理方面取得了巨大的成功[11]。

Tarantino等人。[14]在Transformer中使用全局窗口系统来捕捉话语中的深层关系。

此外，Huang et al.。[15]使用Transformer融合不同的情感分析模式。
