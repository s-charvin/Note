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
lastmod: 2023-06-05 16:42:43
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

### 引文

## 摘录
