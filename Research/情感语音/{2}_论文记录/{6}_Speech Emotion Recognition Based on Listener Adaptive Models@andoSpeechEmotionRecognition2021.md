---
title: "Speech Emotion Recognition Based on Listener Adaptive Models"
description: ""
citekey: andoSpeechEmotionRecognition2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:28:36
lastmod: 2023-04-11 11:01:11
---

> [!info] 论文信息
>1. Title：Speech Emotion Recognition Based on Listener Adaptive Models
>2. Author：Atsushi Ando, Ryo Masumura, Hiroshi Sato, Takafumi Moriya, Takanori Ashihara, Yusuke Ijima, Tomoki Toda
>3. Entry：[Zotero link](zotero://select/items/@andoSpeechEmotionRecognition2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Ando et al_2021_Speech Emotion Recognition Based on Listener Adaptive Models.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 缓解传统方法没有考虑到不同听众的个性化情感感知。
- 最终结果可以转换为传统的情绪感知结果（求平均）
- 采用的方法是自适应方法（自适应全连接（AFC），自适应LSTM（ALSTM）和自适应CNN（ACNN）
- 采用了一个更大型的、持续更新的开源库MSP-Podcast。

思考：
- 把所有听众都考虑了，每个听众都是不同的，那么这些听众是否可以进一步分类，即不同类人有不同的情感判别特性，然后根据类别设计不同模型？
- 优点：计算次数变少，把人分类后，可扩展性也更好。

## 摘要

> [!abstract] This paper presents a novel speech emotion recognition scheme that can deal with the individuality of emotion perception. Most conventional methods directly model the majority decision of multiple listener's perceived emotions. However, emotion perception varies with the listener, which means the conventional methods can mismatch the recognition results to human perception. In order to mitigate this problem, we propose a Listener Adaptive (LA) model that reflects emotion recognition criteria of each listener. One-hot listener codes with several adaptation layers are employed in the LA model. The LA model yields the posterior probabilities of the listener-specific perceived emotions. Majority-voted emotion can be also estimated by averaging, in the LA model, the posterior probabilities for all listeners. Experiments on two emotional speech datasets demonstrate that the proposed approach offers improved listener-wise perceived emotion recognition performance in natural speech.

> 提出了一种新的能够处理情感感知个性化的语音情感识别方案。大多数传统方法直接对多个听者的感知情绪的多数决策进行建模。然而，情感感知随着听者的不同而不同，这意味着传统的识别方法可能会使识别结果与人的感知不匹配。为了缓解这一问题，我们提出了一种反映每个听者情感识别标准的听者自适应(LA)模型。LA模型采用具有多个适配层的One-HotLister编码。LA模型产生特定于听者的感知情绪的后验概率。在LA模型中，多数人投票的情绪也可以通过平均所有听众的后验概率来估计。在两个情感语音数据集上的实验表明，该方法在自然语音中具有更好的听者感知情感识别性能。

## 预处理

## 概述

## 结果

IEMOCAP&&MSP-Podcast

![]({6}_Speech%20Emotion%20Recognition%20Based%20on%20Listener%20Adaptive%20Models@andoSpeechEmotionRecognition2021.assets/image-20220417161651.png)

## 精读

![]({6}_Speech%20Emotion%20Recognition%20Based%20on%20Listener%20Adaptive%20Models@andoSpeechEmotionRecognition2021.assets/image-20220304005823.png)

![]({6}_Speech%20Emotion%20Recognition%20Based%20on%20Listener%20Adaptive%20Models@andoSpeechEmotionRecognition2021.assets/image-20220304005857.png)

大多数传统情感识别方法，将声音特征输入模型后，经由解码器和编码器得到后验概率，最终从中选出最大概率对应的标签，即为情感预测标签。而在此方式中所使用的训练集中的真实标签，是由一组参与情感标签标注的人，对声音序列进行标注，并取出投票数最多的情感标签作为其真实标签得到的，即 the majority decision of multiple listener’s perceived emotions 方法。然而现实情况是情绪感知会因听者而异（听众依赖问题），这意味着传统方法可能会使识别结果与人类个体的个性化感知不匹配。为了缓解传统方法没有考虑到不同听众的个性化情感感知特征，本文提出了一个 Listener Adaptive模型 (LA，听众自适应模型) ，它可以反映每个听众的情绪感知标准。

本文所提出的方法假定每个注释训练集语音的听众都是已知的，并且包括在了训练数据中，然后用一个模型来学习每个听众的情绪感知标准，以此解决听众依赖性问题。

本文中的LA模型将 One-hot listener code **v (l)** 输入到  listener embedding layer中，得到 Listener embedding 向量 **e (l)**，然后将之作为辅助信息与声学特征 **x** 共同输入到多个adaptation layers （自适应全连接层（AFC），自适应LSTM层（ALSTM）和自适应CNN层（ACNN））中。通过切换 listener code ，用单一模型估计依赖于听众的情绪感知后验概率，最终产生每个特定听众的情绪感知的后验概率。对于传统的 Majority-voted 情绪感知结果可以通过在 LA 模型中对所有听众的后验概率进行平均来估计特定标签的概率。 

==声学特征：400维对数功率谱图，其中帧长和帧移分别为40ms 和10ms。Dft长度为1600(10hz 网格分辨率) ，使用0-4千赫兹频率范围。所有的功率谱都使用训练数据集的均值和方差进行了 z 标准化$^{[7, 19]}$。==

本文使用了两个情感语音数据集: Msp-podcast和Iemocap。Msp-podcast有非常自然的语音、大量听众以及语音标注，每个语音都至少有3个听众(平均每个语音有6-7个听众)标注。这个数据集有两种情绪标注，主要情绪和次要情绪，文中只使用了主要情绪构成训练集。 其中开放数据集中的60名发言者的8215个片段用于测试，44名发言者的4418个片段用于验证，其余的25332个片段用于训练。在训练集中，标注少于100条的听众被归类为“其他听众”，因为这些听众会使得学习依赖于听者的情绪感知特征变得困难。Iemocap 是一个被广泛使用的数据集，其中包含了一些听众标注的演讲。它包含10个专业演员(5个男性和5个女性)的视听数据。本文只使用了即兴发挥的语音，并将快乐和兴奋的标签组合成 hap 类。在这个语料库中共有6个学生听众，其中每个语音会得到3个标注，因此我们统一了每个听众的多个情绪标注，规则如下: 优先选择标注中情绪标签出现次数最多的，否则选择第一个标注。对于标注少于500条的听众被归类为“其他听众”，和 msp-podcast 一样。评估表现采用一个说话人缺失交叉验证进行比较，一个说话人用于测试，另一个用于验证，其他8个说话人用于训练。

为了阐明情绪感知中听者依赖性的存在，我们首先使用Cohen’s kappa 系数来研究听者注释的相似性。通过5级匹配((4 targets + Oth)计算相似度。我们选择 msp-podcast/iemocap 中的前10名/前3名的听众来评估两个听众对的相似性，在这些听众对中，两个听众都注释了超过20个相同的话语(结果中小于20个是“-”)。结果表明，MSP-Podcast中相当数量的听众对相似度较低。听众1与听众4,9,10表现出高度相似性，但与其他听众相似性低。另一方面，iemocap 中听众对的相似度均大于0.4(中度匹配) ，而听众1和听众3的相似度相对较低。这些表明情绪感知取决于听众，至少对于 MSP-Podcast。

基线是 majority-voted 情绪识别模型和那些受过 soft-target 目标训练的模型。在依赖听者的情绪识别任务中，基线模型的输出被看作是听者的个体估计结果。由于该方法统一了 la 模型的多个输出，因此在多数情感识别中也比较了不同初始参数情感模型的集成。听众人数为每个语音的平均听众人数，即 msp 播客和 iemocap 中的平均听众人数分别为7和3。在基线模型中，

输入 batch 的大小为8（iemocap）和16（MSPPodcast），结构包含3层 cnn（16,24,32+batch normalization+ReLu激活函数+2 × 2 max-pooling 层）、1层双向 lstm（128个隐藏单元+0.2 Dropout 率）、4-head 结构注意力层（0.2 Dropout 率）和2层 fc（64个隐藏单元+0.2 Dropout 率）。最终的损失优化方法使用的是Adam（学习率为0.0001）。

==在训练步骤中，以 inverse values of the class frequencies 作为 class weights ，以 mitigate the class imbalance problem（缓解类不平衡问题）。==采用 Speed perturbation 方法进行数据增强，其因子分别设置为0.9、0.95、1.05和1.1。SpecAugment（针对ASR的数据增强方法）也应用了两个 time and frequency masking（时频掩蔽方法）。这些方法是基于LA模型的。

单独使用 afc、 alstm 和 acnn 层，并将这些适应层组合作为 LA 模型进行评估。La 模型的结构和超参数与基线相同。在 MSP-Podcast和 iemocap 中，听者嵌入向量维数分别为32和8。在 ld 模型训练中，计算每个listener的类权重，并将 listener 权重与listener注释频率的反比值相乘，得到最终的损失权重。其他的训练条件与基线相符。

评价指标为加权准确度(wa：所有语音的分类准确度)和未加权准确度(ua：个体情绪类准确度的宏观平均值)。![]({6}_Speech%20Emotion%20Recognition%20Based%20on%20Listener%20Adaptive%20Models@andoSpeechEmotionRecognition2021.assets/image-20220304012859.png)

符号(ens.)是指模型的整体结果。

在 msp-podcast 中，在听者依赖任务中，具有 afc 层的 la 模型的宏观平均值显著高于软标签模型和具有comparable UAs(p  .05)的 majority-voted 模型(配对 t 检验 p < 0.05)。在多数人投票的情感识别中也出现了类似的结果;

具有相似 UA 的基线及其集合的 WA 高出 10% 以上。从这些结果和表3可以看出，在听者的情绪感知差异很 大的情况下，例如自然语言，所提出的LA模型是有效的。

在 IEMOCAP 中，基于 AFC 分层的 LA 模型在依赖于听者和多数投票的情绪任务中分别表现出略好于基线的表现和几乎相同的表现。这些都表明，在情感感知不太依赖于听者的情况下，所提出的方法不会恶化估计性能。最后，对 LA 模型中的适配层进行了比较。AFC 适应层比 ALSTM 和 ACNN 有更好的效果。一种可能性是，个性化情绪感知的出现在对情绪线索的感知做出决定的编码器中，而不是从音频信号中提取情绪线索的解码器中。结果还表明，听众和说话人的个性应该在评估模型的不同部分进行建模；

### 引文

- 在口头对话系统中生成类似人类的响应[1]

- 联系中心呼叫中客户分析的声音[2]

- 最近的研究通过使用深度神经网络（DNN）取得了显着的效果[3-8]，该框架的主要优点是，通过组合不同类型的图层，可以自动学习感知情绪的复杂线索。

- 注意机制也被用来关注话语识别的局部特征[5]。

- 基于DNN的模型可以利用低级特征，例如对数功率谱图或原始波形，这些特征具有丰富但复杂的信息[6,7]。

- 卷积神经网络 (CNN) 和长短期记忆循环神经网络 (LSTM-RNN) 已被用于捕获话语中的局部和上下文特征 [3,4,8]。

- 情绪表达和情绪感知两个方面的研究：情绪呈现的方式取决于说话者，他们无意识地设定了话语的声学特征[9]。情绪的感知方式取决于听者的年龄，性别和文化[10,11]。

- 鉴于情绪表达方面的问题，说话者依赖性通常在SER中考虑。为了减轻对不同说话者的依赖性，提出了说话者适应[12]或通过多任务学习区分说话者性别[8,13]。

- 利用听众依赖的情绪感知做SER：一种方法是通过软标签[14]或多变量高斯[15]来模拟听众的情绪感知分布。但是，它不能区分听众。另一个结构个别听众模型来描述情绪感知的可变性[16]。这个框架的问题之一是模型大小；它需要与听众相同数量的隔离模型，这在大量听众的情况下是不切实际的。

- 受到语音处理中domain adaptation的启发[17,18]

- 多数票情绪识别模型直接评价多数票情绪的后验概率。该模型由编码器和解码器组成[8,19]。
- 基线是 majority-voted 情感识别模型和那些与软目标训练 [24] 。

## 摘录
