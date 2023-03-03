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
data: 2022-04-17 14:16:11
lastmod: 2022-04-17 14:53:23
---

# 重点

- 论文源文件
- 创建了一个大型的自然情感语音数据库（多说话人、情感均衡且自然，领域广泛）
- 使用机器学习算法来检索具有稳定情感内容的语音。
- 情感语音评估标准相对完善（属性评估：每个属性分七个等级且均有其对应的直观的人体模型；主要情绪分类评估：愤怒、悲伤、快乐、惊讶、恐惧、厌恶、蔑视、中性，其他；次要情绪分类评估：）


# 摘要


# 词汇记录

# 精读

**传统方案**

![]({7}_Building%20Naturalistic%20Emotionally%20Balanced%20Speech%20Corpus%20by%20Retrieving%20Emotional%20Speech%20from%20Existing%20Podcast%20Recordings@lotfianBuildingNaturalisticEmotionally2019.assets/image-20220304005928.png)

1. 演员阅读预先设定好的包含目标情绪的句子：过度强调表达，与日常不同。

	Emo-DB, CREMA-D, Chen Bimodal

2. 模拟说话人对话，收集即兴的语音（创建情景、视频会议协作、选择情绪敏感的听众）：昂贵耗时

	IEMOCAP, MSP-IMPROV

3. 社会中的记录（呼叫中心、儿童互动、电视脱口秀、自媒体、采访、视频博客）：情感易受实际环境和说话上下文影响，需要规范化

	VAM, TUM-AVIC, SEMAINE, FAU-AIBO, RECOLA

总体特点：数据库小，容易过拟合；说话人少，限制泛化能力；

**本文方案**

	音频来源：播客
	
		类型：（对话、采访、脱口秀、新闻、讨论、教育、讲故事和辩论）
	
		主题：科学、技术、政治、经济、商业、艺术、文化、医学、生活方式和体育。

**实现方法**

1. 选择播客后，首先是将它们转换为一致的格式（单声道，采样率为 16 kHz，16 位 PCM）并分割成短片段，得到输出段的开始时间、段的持续时间和与段相关联的说话者 ID 号的信息。

2. 通过语音活动检测 (VAD)、说话人分类、音乐/语音识别和噪声水平估计算法实现自动化将播客被分割成干净的、单个扬声器的，去除无声、含背景音乐、嘈杂或重叠的语音，并分类作为候选。

3. 依靠用现有语料库训练的机器学习模型来检索具有目标情绪行为的样本，如arousal（calm versus active）和valence（negative versus positive）属性。

4. 通过在众包平台上进行的情感评估进行情感注释。

评估方法：1. 实时跟踪工人的表现，当他们的表现低于可接受的阈值时停止评估。2. 每五个句句子中包含随机包含一个参考句。

使用 Sound eXchange (SoX) 软件转换

使用 Speaker Attribution Intelligent Service 的在线云应用程序识别和跟踪说话者。

手动分割了 105 个播客，用于训练分类器，该分类器可以检测带有背景音乐的片段。
