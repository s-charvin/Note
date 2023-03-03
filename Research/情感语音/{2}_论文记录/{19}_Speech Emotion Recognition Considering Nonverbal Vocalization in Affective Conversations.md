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
data: 2022-04-26 08:27:26
lastmod: 2022-04-26 11:44:22
---

# 重点

- 开源代码

# 摘要

In real-life communication, nonverbal vocalization such as laughter, cries or other emotion interjections, within an utterance play an important role for emotion expression. In previous studies, only few emotion recognition systems consider nonverbal vocalization, which naturally exists in our daily conversation. In this work, both verbal and nonverbal sounds within an utterance are considered for emotion recognition of real-life affective conversations. Firstly, a support vector machine (SVM)-based verbal and nonverbal sound detector is developed. A prosodic phrase autotagger is further employed to extract the verbal/nonverbal sound segments. For each segment, the emotion and sound feature embeddings are respectively extracted using the deep residual networks (ResNets). Finally, a sequence of the extracted feature embeddings for the entire dialog turn are fed to an attentive long short-term memory (LSTM)-based sequence-to-sequence model to output an emotional sequence as recognition result. The NNIME corpus (The NTHU-NTUA Chinese interactive multimodal emotion corpus), which consists of verbal and nonverbal sounds, was adopted for system training and testing. 4766 single speaker dialogue turns in the audio data of the NNIME corpus were selected for evaluation. The experimental results showed that nonverbal vocalization was helpful for speech emotion recognition. For comparison, the proposed method based on decision-level fusion achieved an accuracy of 61.92% for speech emotion recognition outperforming the traditional methods as well as the feature-level and model-level fusion approaches.

在实际沟通过程中，语音交谈中的非语言发声，如笑声、哭声或其他情感感叹词，在情感表达中起着重要的作用。在以往的研究中，很少有情感识别系统考虑自然存在于我们日常对话中的非语言发声，因此在本文工作中，语音中的语言和非语言声音部分都被用作对现实生活中情感对话的情感识别。本文首先设计了一种基于支持向量机的**语言语音和非语言语音检测器**，然后进一步使用韵律短语自动标记器（prosodic phrase autotagger）来提取语言语音和非语言语音片段。对于每个片段，分别使用深度残差网络(ResNets)提取情感和语音嵌入特征。最后，将从整个对话提取的嵌入特征序列馈送到基于注意力的长短期记忆(LSTM)的序列到序列模型，以输出情感序列作为识别结果。采用NNIME语料库(NTHU-NTUA汉语交互式多通道情感语料库)进行系统训练和测试。在NNIME语料库的音频数据中选取4766个单人对话进行评估。实验结果表明，非语言声音有助于语音情感识别。相比之下，基于决策层融合的语音情感识别方法的准确率达到61.92%，优于传统方法以及特征层和模型层的融合方法。

# 结果

# 词汇记录

# 精读

近年来，随着科学技术的快速进步，使智能设备在我们的日常生活中变得更加流行。聊天机器人、心理诊断助手、智能医疗、销售广告、智能娱乐等智能服务，考虑的不仅仅是服务的完成性，更重要的是人机交互的人性化。如何实现智能化的人机交互平台成为一个重要的研究问题。对于语音交互系统的应用，一些先进的企业会使用聊天机器人来改善他们的客户服务，并为公司增加业务成绩[1]，[2]并且与直接和客户沟通不同的是，与情感相关的共情系统一般会被纳入到语音交互系统的设计中，以改善用户在人机交互中的体验。更重要的是，要让语音交互系统被用户视为一种社会角色，共情是必不可少的一步。基于以上动机，本研究旨在提高情感识别过程的准确率。

随着使用移动设备越来越普及，语音已经成为人与人、人与机器沟通的最常见的方式之一。语音情感识别是实现计算机情感智能的重要技术之一[4]-[9]，因为人们可以通过语音中包含的信息来理解他人的情感[3]。目前，语音情感识别的研究主要集中在情感特征提取和识别建模两个方面。此外，情感语音数据库的选择对于开发稳健的语音情感识别架构也很重要[10]，[11]。目前的情感识别系统受到语音数据资源缺乏的限制，很少关注日常自发交流中的非语言发声。NNIME 和 BAUM-1 语料库中数据的声音类型和情感类别之间的关系如图1所示，例如，大笑很容易被认为是幸福的，而大喊大叫则与惊喜高度相关。现有的关于非语言情绪识别的文献描述了某些非语言声音(如笑声和喊叫)有利于积极情绪(如快乐和惊讶)的识别[12]-[17]。然而，关于其他非语言声音类型以及隐晦或负面情绪(如悲伤和沮丧)的影响的相关实验和讨论并不多。在现实生活中，对话中的非语言声音在人们识别他人情绪方面发挥着重要作用[18]。当人类大脑分析情绪语音时，非语言声音可以有效地帮助大脑获得情绪表达的差异[19]。因此，本研究旨在将非语言声音的特征应用于语音情感识别。

本研究提出了以下有待解决的问题。

- 第一个问题是语音情感识别基本单元的选择。当我们在对话中识别别人的情绪时，我们不需要听别人的整个反应来识别情绪。从文献中的报告来看，句子级别的特征比粗略对应于用于情感识别的几个单词的持续时间的语音片段更差[26]。先前的研究表明，情绪的识别至少需要一秒钟以上的语音信号[33]。文献[28]中的研究表明，离散的韵律动作单位可以代表言语情感。由于停顿在汉语语音中起着韵律边界标记的作用[41]，我们选择韵律短语作为情感识别的基本单位。

- 对于第二个问题，自然语言中有许多非语言的声音，如笑声和哭声，这有助于区分他人的情绪。在我们只听到鼻息声的情况下，我们无法确定他人的情绪。如果我们听到低能量和多次停顿的鼻息声参与对话，我们可以识别它是对话过程中悲伤情绪中的抽泣声。文献[19]中的研究表明，当人们识别他人的情绪时，我们的大脑独立地处理语音表征和情绪，然后通过声音效应更清楚地获得情绪的差异。由于语音发声和非语音发声在语音情感表达上是相辅相成的，本研究采用两种不同的深度残差网络(ResNets)来提取语音发声的情感特征和非语言声音的情感特征，用于语音情感识别。

- 对于最后一个问题，我们认为在一次对话中可能存在多种情感表达。人们在不同的对话中表达不同程度或不同类型的情绪。人们在感兴趣的内容上往往会表现出高度的 arousal 情绪，在描述日常生活事件时会考虑中性的情绪。针对这一问题，我们将音频信号分为语言段和非语言段进行特征提取。然后使用长短期记忆(LSTM)模型来刻画语音信号的连续情感表达。也就是说，构建LSTM模型，从一系列分段的语音信号中获得说话人在对话中的情感变化。

图2显示了建议的系统框架。在训练阶段，主要分为语音/非语音分割、特征嵌入提取和情感模型构建三个阶段。首先，语音信号经过静默检测、语言和非语言的语音片段检测和韵律短语分割过程，得到语音/语音片段。其次，使用语言和非语言的语音/语音片段来训练相应的ResNet模型，以提取情感和声音的嵌入特征。通过去除输出层，将经过情感/语音类型分类训练的ResNet模型用作特征提取器。最后用 ResNet 提取的语音和情感的特征作为每个片段的代表嵌入特征，该特征嵌入序列将用于情感识别，以获得考虑时间上下文中情感变化的每个片段的情感识别结果。

![]({19}_Speech%20Emotion%20Recognition%20Considering%20Nonverbal%20Vocalization%20in%20Affective%20Conversations@hsuSpeechEmotionRecognition2021.assets/image-20220426103153.png)


本研究选取NTHU-NTUA中文互动多通道情绪语料库(NNIME)作为系统评测的资料库。在NNIME中，有愤怒、悲伤、快乐、挫折、中立和惊讶6种情感情绪。NNIME的设计有三个主要要素：(1)第一个要素是采用二元交互作用进行情感行为的自然诱导，(2)第二个要素是同时收集二元组的外部行为和内部生理信息，(3)第三个要素是从不同的角度诠释交互作用的两个组的丰富情绪属性[25]。NNIME语料库包括44名来自台湾艺术大学戏剧系的受试者的录音，其中22名女性，20名男性。NNIME语料库由49名受试者标注，其中包括学生和教授。该数据库包含音频、视频和心电记录。在这项研究中，我们只使用了包含102个二元交互会话的音频数据，大约11个小时(每个会话的持续时间μ=195.35秒，σ=73.26秒)。

由于本研究只使用了NNIME数据库中的音频文件，即整部剧的音频数据，按照指定的分割标准

1. 注释单个发言者的通话开始/结束时间。
2. 注释多个发言者的开始/结束通话时间。
3. 如果被其他发言者打断，请在话轮的上一次停顿时停下来。
4. 纯粹的非语言声音可以看作是一种转折。

将音频文件手工分割为7672个单人对话回合，每个会话的音频文件逐个标注说话人语音信号的开头和结尾，称为会话中的单人对话回合。下图显示了注释文件的一个例子。

![]({19}_Speech%20Emotion%20Recognition%20Considering%20Nonverbal%20Vocalization%20in%20Affective%20Conversations@hsuSpeechEmotionRecognition2021.assets/image-20220426110552.png)

由于NNIME语料库每个会话有一个/两个记录 channel，我们只选择了其中较清晰的一个频道。最后，从7672个单人话轮中选出4766个单人话轮(每个话轮的时长和标准差μ=3.25秒，σ=5.42秒)，并对其进行情感类型和声音类型的标注。

在这项研究中，我们使用了与NNIME中定义的相同的六种情绪，包括愤怒、沮丧、悲伤、惊讶、中立和快乐。由于很难区分说话人的 “silence“ 和 “background noise” 片段，我们增加了一个“background” 标签来代表 silence/background 片段。这项研究总共使用了6个情绪标签来表达情绪，以及一个“background”标签来表征不太可能被贴上特定情绪标签的静音/背景噪音片段。由于演讲者在NNIME的对话回合中不仅表达了一种情绪，我们重新注释了每个片段的情绪和“background”标签。

除了情感类型，本研究还定义了四种声音类型。每个语言片段被分配了一个情感类别，每个非语言片段被分配到四种声音类型中的一种，如表II所示。前三种非语言类声音类型，包括笑声、呼吸和喊叫，第四类是背景音，包括沉默、噪音、观众声音等。由于NNIME的录音环境有来自观众和演员自发行为的噪音，非语言的 “background” 标签不仅包括对话中的沉默，还包括来自录音环境的噪音和观众声音。

音频分割是我们提出的方法中的一个重要步骤，因此我们需要一个边界验证集来测试语音和非语音区间的自动边界检测结果。我们从4766个单人对话语料中随机抽取 300 个对话进行边界标注和情感标注。在选择的300个对话的边界已经被标注之后，使用边界验证集来训练用于语言/非语言语音分割的支持向量机模型。重新标注NNIME语料库有四个步骤。

- 首先，使用Praat软件对选定的300个对话的文本网格文件进行静音检测。
- 其次，使用基于韵律短语现象(phenomena of prosodic phrase，PPH)和如下标准的三个标注器，对音频片段进行标注。
	1. 语句暂停超过 $0.3$ 秒。
	2. Intonation raising(在 raising pitch 轮廓的最高点标注)。
	3. 延长结尾处(Prolonged ending，在延长的起始处标注)。
	4. 下降强度(在下降强度的最低点标注)

	1. 消除Praat对静默间隔的错误检测。
	2. 不要修剪少于$0.1$秒的间隔。
	3. 调整Praat检测到的静默区间的错误边界。

- 第三，标注器对每个片段的情感类型和声音类型进行标注，并将音频文件分类为语言片段和非语言片段。最后，将这些经过标注的音频作为边界验证集。

表四显示了边界验证集合的统计数据

![]({19}_Speech%20Emotion%20Recognition%20Considering%20Nonverbal%20Vocalization%20in%20Affective%20Conversations@hsuSpeechEmotionRecognition2021.assets/image-20220426114306.png)

表五显示了边界验证集合中声音类型的分布。利用该数据集验证了本文提出的自动分割方法的性能。

![]({19}_Speech%20Emotion%20Recognition%20Considering%20Nonverbal%20Vocalization%20in%20Affective%20Conversations@hsuSpeechEmotionRecognition2021.assets/image-20220426114314.png)

在边界标注中，确保每个标签至少由两个标注器标注。重新标注的情感标签和声音类型标签的kappa分数[42]分别为0.63和0.69，均大于0.6，这意味着基本一致。重新标注的数据的一致性足够高，足以证明其可靠性。

## 引文

随着对情感计算的研究越来越多，学者们已经建立了几个**情感数据库**[20]-[24]。这些数据库包含不同格式(如音频、视频、文本和运动)和不同标注(如语言、情感标签和脚本)的数据。为了分析情感语音中的非语言声音，一个合适的情感语音数据库是值得研究的。

与其他剧本类情感语料库或电视剧中的分段音频不同，NTHU-NTUA 汉语交互式多通道情感语料库(**NNIME**)是一个自发的汉语语音情感数据库，包含了各种情感的非语言声音，如笑声、抽泣和叹息[25]等，符合本研究的要求，因此被采用。

在语音情感识别机制中，如何从语音信号中提取情感特征是有效情感识别的关键问题。许多研究都在寻找合适的音频特征或合适的**音频特征集**[26]、[27]来表征情绪特征。其他研究试图用不同的特征单位来表示音频[28]。近年来，随着神经网络(NN)的发展，许多研究人员试图从原始的音频波形或频谱中提取特征用于情感识别[29]-[32]。一些研究认为，现有的声学特征集可能缺乏主观情感特征，因为特征提取算法的参数大多是人工调整的[31]。他们期望基于神经网络的端到端情感特征提取方法能够从语音中获取信息。

基于不同类型的情感特征，语音情感识别模型的选择应考虑所提取特征的属性。长短时记忆(LSTM)是一种能够对连续时间属性[34]、[35]特征的情绪类型进行分类的记忆。**谢等人** 提出了一种基于注意的长短期记忆(LSTM)递归神经网络，用于基于帧水平语音特征的语音情感识别[34]。他们在CASIA、eNTERFACE和GEMEP情感语料库上的实验表明，所提出的方法的性能优于迄今报道的最先进的算法。

卷积神经网络(CNN)可以通过卷积步骤组合局部特征，从而获得更大范围的组合信息的分类结果[33]。**赵等人**。将一维和二维CNN与LSTM网络相结合用于语音情感识别。建立一维CNN是为了从语音中学习与局部和全球情感相关的特征，而二维CNN是用来学习音谱图的[36]。CNN和LSTM的结合被称为**CLDNN**，预计将从两种类型的模型中受益，并通过涉及注意力来获得更好的表现[37]。

随着深层网络结构的逐渐成熟，使用更深层的基于CNN的模型也具有良好的图像识别性能。利用**ResNet**提取语音的幅值谱特征，在语音情感识别中也取得了许多优秀的结果[38][40]。
