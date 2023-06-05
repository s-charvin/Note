---
title: "Multimodal Language Analysis in the Wild: CMU-MOSEI Dataset and Interpretable Dynamic Fusion Graph"
description: ""
citekey: bagherzadehMultimodalLanguageAnalysis2018
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-06-04 18:21:02
lastmod: 2023-06-05 16:55:28
---

> [!info] 论文信息
>1. Title：Multimodal Language Analysis in the Wild: CMU-MOSEI Dataset and Interpretable Dynamic Fusion Graph
>2. Author：AmirAli Bagher Zadeh, Paul Pu Liang, Soujanya Poria, Erik Cambria, Louis-Philippe Morency
>3. Entry：[Zotero link](zotero://select/items/@bagherzadehMultimodalLanguageAnalysis2018) [URL link](https://aclanthology.org/P18-1208) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Bagher Zadeh et al_2018_Multimodal Language Analysis in the Wild.pdf>)
>4. Other：2018 - Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)  Association for Computational Linguistics Melbourne, Australia  -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- :fas_question:   
- :obs_pdf_file:   
- :obs_graph_glyph:   
- :obs_wand_glyph:   

## 摘要

> [!abstract] Analyzing human multimodal language is an emerging area of research in NLP. Intrinsically this language is multimodal (heterogeneous), sequential and asynchronous; it consists of the language (words), visual (expressions) and acoustic (paralinguistic) modalities all in the form of asynchronous coordinated sequences. From a resource perspective, there is a genuine need for large scale datasets that allow for in-depth studies of this form of language. In this paper we introduce CMU Multimodal Opinion Sentiment and Emotion Intensity (CMU-MOSEI), the largest dataset of sentiment analysis and emotion recognition to date. Using data from CMU-MOSEI and a novel multimodal fusion technique called the Dynamic Fusion Graph (DFG), we conduct experimentation to exploit how modalities interact with each other in human multimodal language. Unlike previously proposed fusion techniques, DFG is highly interpretable and achieves competative performance when compared to the previous state of the art.

> 分析人类多模态语言是 NLP 的一个新兴研究领域。从本质上讲，人类的沟通是多模态的（异质的）、时间性的和异步的；它由语言（文字）、视觉（表情）和听觉（副语言）三种模态组成，并形成了异步协调的序列表现形式。从资源的角度来看，需要大规模的数据集，以便深入研究多模态语言。在本文中，我们设计和构建了一个多模态意见情感和情绪强度数据集(CMU-MOSEI)，这是迄今为止规模最大的情感分析和情绪识别数据集。同时，我们利用 CMU-MOSEI 的数据和一种称为动态融合图 (DFG) 的新型多模态融合技术进行实验，以探究各模态如何在人类多模态语言中的相互作用。与之前提出的融合技术不同，DFG 具有高度可解释性，并且在性能上与当前的最新技术相媲美。

## 预处理

## 概述

## 结果

## 精读

在自然语言处理中，这种语言形式被视为人类多模态语言。多模态语言建模最近成为 NLP 和多模态机器学习的中心研究方向。然而，从资源的角度来看，以往的多模态语言数据集在以下几个方面存在严重不足：数据集大小，模态丰富度。，演讲者数量，单样本的注释数量。

我们在本文中的第一个贡献是介绍了最大的多模态情绪和情绪识别数据集，称为 CMU 多模态意见情绪和情绪强度 (CMUMOSEI)。 CMU-MOSEI 包含来自 1,000 位不同演讲者的 23,453 个带注释的视频片段和 2237,250 个主题。每个视频片段都包含与音频对齐到音素级别的手动转录。所有视频均来自在线视频共享网站 1. 该数据集目前是 CMU Multimodal Data SDK 的一部分，可通过 Github 免费提供给科学界。

我们的第二个贡献是一种称为动态融合图 (DFG) 的可解释融合模型，用于研究多模态语言中跨模态动力学的性质。 DFG 包含与模态如何交互直接相关的内置功效。这些功效在我们的实验中得到了可视化和详细研究。除了可解释性之外，与之前提出的 CMU-MOSEI 多模态情感和情感识别模型相比，DFG 实现了卓越的性能。


我们将 CMU-MOSEI 与用于情感分析和情感识别的大量数据集进行比较。以下数据集包括语言、视觉和听觉模式的组合作为其输入数据。

CMU-MOSI (Zadeh et al., 2016b) 是 2199 个意见视频剪辑的集合，每个视频剪辑都用 [-3,3] 范围内的情感注释。 CMU-MOSEI 是 CMU-MOSI 的下一代。

ICT-MMMO (W ̈ ollmer et al., 2013) 由在视频级别注释的在线社交评论视频组成，用于情感。

YouTube (Morency et al., 2011) 包含来自社交媒体网站 YouTube 的视频，涵盖范围广泛的产品评论和意见视频。

MOUD（Perez-Rosas 等人，2013 年）包含西班牙语的产品评论视频。每个视频都包含多个标记为显示正面、负面或中性情绪的片段。

IEMOCAP（Busso 等人，2008 年）包含 151 个对话录制视频，每个会话有 2 个演讲者，整个数据集中共有 302 个视频。每个片段被注释为存在 9 种情绪（愤怒、兴奋、恐惧、悲伤、惊讶、沮丧、快乐、失望和中性）以及效价、唤醒和支配。

Stanford Sentiment Treebank (SST)（Socher 等人，2013 年）在从电影评论数据中收集的句子解析树中包含短语的细粒度情感标签。虽然 SST 有更大的注释池，但我们只考虑根级注释进行比较。

Cornell Movie Review (Pang et al., 2002) 是 2000 份电影评论文档和句子的集合，这些文档和句子根据整体情感极性或主观评分进行了标记。

大型电影评论数据集 (Maas et al., 2011) 包含来自极端电影评论的文本。

Sanders Tweets Sentiment (STS) 包含 5513 条手工分类的推文，每条推文都根据 Microsoft、Apple、Twitter 和 Google 的四个主题之一进行分类。

Vera am Mittag (VAM) 语料库包含德国电视谈话 2238 节目“Vera am Mittag”的 12 小时录音（Grimm 等人，2008 年）。此视听数据被标记为三种情感基元的连续值标度：效价、激活和支配。 VAM-Audio 和 VAMFaces 是分别包含声学和视觉输入的子集。

RECOLA（Ringeval 等人，2013 年）包含 9.5 小时的在线二元交互的音频、视觉和生理（心电图和皮肤电活动）记录。

Mimicry (Bilakhia et al., 2015) 包含两种情况下人类互动的视听记录：讨论政治话题时和玩角色扮演游戏时。

AFEW (Dhall et al., 2012, 2015) 是一个动态的时间面部表情数据语料库，由从电影中提取的接近真实世界的环境组成。

![]({57}_Multimodal%20Language%20Analysis%20in%20the%20Wild_%20CMU-MOSEI%20Dataset%20and%20Interpretable%20Dynamic%20Fusion%20Graph@bagherzadehMultimodalLanguageAnalysis2018.assets/image-20230605164842.png)


CMU-MOSEI 与本节数据集的详细比较如表 1 所示。CMU-MOSEI 具有更长的总持续时间以及更多的数据点总数。此外，CMU-MOSEI 的演讲嘉宾和主题也更加多样化。它提供了所有三种模式，以及情绪和情绪的注释。


CMU-MOSEI Dataset 

理解表达的情感和情绪是人类多模态语言中的两个关键因素。我们介绍了一种用于多模态情绪和情绪识别的新型数据集，称为 CMU 多模态意见情绪和情绪强度 (CMU-MOSEI)。在下面的小节中，我们首先解释 CMU-MOSEI 数据采集的细节，然后是注释和特征提取的细节。

CMU-MOSEI Dataset 数据采集过程

社交多媒体提供了一个独特的机会，可以从各种演讲者和主题中获取大量数据。这些社交多媒体网站的用户经常以独白视频的形式发表意见；只有一个人在镜头前讨论某个感兴趣话题的视频。每个视频本质上包含三种形式：口头文本形式的语言，通过感知手势和面部表情的视觉形式，以及通过语调和韵律形式的声学形式。

在我们的自动数据采集过程中，来自 YouTube 的视频使用面部检测来分析帧中是否存在一个说话者，以确保视频是独白。我们通过拒绝具有移动摄像头的视频（例如自行车上的摄像头或步行时录制的自拍），将视频限制为演讲者的注意力完全集中在摄像头上的设置。我们使用在线视频中 250 个经常使用的主题作为采集的种子。


严格限制从每个频道获取的视频数量最多为 10 个。这导致从 YouTube 发现了 1,000 个身份。身份的定义代表通道的数量，因为准确的识别需要二次手动注释，这对于大量说话者来说是不可行的。此外，我们限制视频具有上传者提供的手动和正确标点的转录。最终获得的视频库包括 5,000 个视频，然后由 14 位专家评委在三个月内手动检查视频、音频和文字记录的质量。评委们还为每个视频添加了性别注释，并确认每个视频都是可以接受的独白。经过人工质量检查后，剩下一组 3228 个视频。我们还使用面部特征提取置信度和强制对齐置信度对视频和文字记录的质量进行了自动检查，这在第 3.3 节中进行了讨论。此外，我们使用评委提供的数据（57% 男性对 43% 女性）平衡数据集中的性别。这构成了 CMU-MOSEI 中的最后一组原始视频。最后一组视频中涵盖的主题在图 1 中显示为维恩式词云（Coppersmith 和 Kelly，2014 年），其大小与为该主题收集的视频数量成正比。最常见的 3 个主题是评论 (16.2%)、辩论 (2.9%) 和咨询 (1.8%)。其余主题几乎均匀分布 3.

然后将最终的视频集标记为使用成绩单手动提供的标点符号的句子。由于转录本的质量很高，使用标点符号比使用 Stanford CoreNLP 分词器表现出更好的句子质量（Manning 等人，2014 年）。两位专家对一组 20 个随机视频进行了验证。标记化后，一组 23,453 个句子被选为数据集中的最终句子。这是通过限制每个身份为数据集贡献至少 10 个和最多 50 个句子来实现的。表 2 显示了 CMU-MOSEI 数据集的高级汇总统计数据。


CMU-MOSEI Dataset 注释过程

CMU-MOSEI 的注释紧跟 CMU-MOSI (Zadeh et al., 2016a) 和 Stanford Sentiment Treebank (Socher et al., 2013) 的注释。每个句子都在 [-3,3] Likert 量表上标注了情绪：[-3：高度消极，-2 消极，-1 弱消极，0 中性，+1 弱积极，+2 积极，+3 高度积极]. {快乐、悲伤、愤怒、恐惧、厌恶、惊讶}的 Ekman 情绪 (Ekman et al., 1980) 在 [0,3] Likert 量表上注释了情绪 x 的存在：[0: 没有 x 的证据，1 : 弱 x, 2: x, 3: 高度 x]。标注由 Amazon Mechanical Turk 平台的 3 位众包评委完成。为了避免对评委产生隐性偏见并捕捉人群的原始看法，我们避免了极端的注释培训，而是为评委提供了一段 5 分钟的培训视频，介绍如何使用注释系统。所有标注均由师傅完成，通过率高于98%，保证标注质量. 

![]({57}_Multimodal%20Language%20Analysis%20in%20the%20Wild_%20CMU-MOSEI%20Dataset%20and%20Interpretable%20Dynamic%20Fusion%20Graph@bagherzadehMultimodalLanguageAnalysis2018.assets/image-20230605165524.png)

图 2 显示了 CMU-MOSEI 数据集中情绪和情绪的分布。分布显示有利于积极情绪的轻微转变，这类似于 CMU-MOSI 和 SST 的分布。我们认为这是在线意见略微转向正面的隐含偏见，因为这也存在于 CMU-MOSI 中。情绪直方图显示了不同情绪的不同流行程度。最常见的类别是快乐，有超过 12,000 个正样本点。最不普遍的情绪是恐惧，几乎有 1900 个正样本点，这对于机器学习研究来说是一个可接受的数字。


CMU-MOSEI Dataset 手动特征提取过程

CMU-MOSEI 中的数据点以视频格式出现，摄像头前有一个扬声器。每种模态提取的特征如下（对于其他基准，我们提取相同的特征）：


语言：所有视频都有手动转录。Glove 词嵌入 (Pennington et al., 2014) 用于从转录本中提取词向量。使用 P2FA 强制对齐模型（Yuan 和 Liberman，2008）在音素级别对齐单词和音频。在此之后，视觉和听觉模态通过插值与单词对齐。由于英语单词的发音持续时间通常很短，因此这种插值不会导致大量信息丢失。

视觉：以 30Hz 的频率从完整视频中提取帧。使用 MTCNN 人脸检测算法（Zhang et al., 2016）提取人脸的边界框。我们通过面部动作编码系统 (FACS) (Ekman et al., 1980) 提取面部动作单元。提取这些动作单元可以准确跟踪和理解面部表情（Baltruˇ saitis 等人，2016）。我们还使用 Emotient FACET (iMotions, 2017) 从静态面孔中提取了一组六种基本情绪。 MultiComp OpenFace (Baltruˇ saitis et al., 2016) 用于提取一组 68 个面部标志、20 个面部形状参数、面部 HoG 特征、头部姿势、头部方向和眼睛注视 (Baltruˇ saitis et al., 2016)。最后，我们从 DeepFace (Taigman et al., 2014)、FaceNet (Schroff et al., 2015) 和 SphereFace (Liu et al., 2017) 等常用人脸识别模型中提取人脸嵌入。

声学：我们使用 COVAREP 软件 (Degottex et al., 2014) 提取声学特征，包括 12 Mel 倒谱系数、音高、浊音/清音分割特征 (Drugman and Alwan, 2011)、声门源参数 (Drugman et al. , 2012; Alku et al., 1997, 2002), peak slope parameters and maxima dispersion quotients (Kane and Gobl, 2013).所有提取的特征都与情绪和语调有关。


### 引文

## 摘录
