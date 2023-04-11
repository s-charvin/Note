---
title: "Is Cross-Attention Preferable to Self-Attention for Multi-Modal Emotion Recognition?"
description: ""
citekey: rajanCrossAttentionPreferableSelfAttention2022
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:32:24
lastmod: 2023-04-11 11:32:00
---

> [!info] 论文信息
>1. Title：Is Cross-Attention Preferable to Self-Attention for Multi-Modal Emotion Recognition?
>2. Author：Vandana Rajan, Alessio Brutti, Andrea Cavallaro
>3. Entry：[Zotero link](zotero://select/items/@rajanCrossAttentionPreferableSelfAttention2022) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Rajan et al_2022_Is Cross-Attention Preferable to Self-Attention for Multi-Modal Emotion.pdf>)
>4. Other：2022 - ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：https://github.com/smartcameras/SelfCrossAttn
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 讨论了注意力机制对不同模态间特征融合的影响
- 通过将两个不同模态的输入分别分配给注意力机制的Q和KV，实现多模态运算之间的数据交互。
- 结论：多模态特征融合过程中，使用自注意力机制和使用跨模态交互注意力机制都有用，但是效果类似。

## 摘要

> [!abstract] Humans express their emotions via facial expressions, voice intonation and word choices. To infer the nature of the underlying emotion, recognition models may use a single modality, such as vision, audio, and text, or a combination of modalities. Generally, models that fuse complementary information from multiple modalities outperform their uni-modal counterparts. However, a successful model that fuses modalities requires components that can effectively aggregate task-relevant information from each modality. As cross-modal attention is seen as an effective mechanism for multi-modal fusion, in this paper we quantify the gain that such a mechanism brings compared to the corresponding self-attention mechanism. To this end, we implement and compare a cross-attention and a self-attention model. In addition to attention, each model uses convolutional layers for local feature extraction and recurrent layers for global sequential modelling. We compare the models using different modality combinations for a 7-class emotion classification task using the IEMOCAP dataset. Experimental results indicate that albeit both models improve upon the state-of-the-art in terms of weighted and unweighted accuracy for tri- and bi-modal configurations, their performance is generally statistically comparable. The code to replicate the experiments is available at https://github.com/smartcameras/SelfCrossAttn

> 

## 预处理

## 概述

## 结果

## 精读

### 引文

## 摘录
