---
title: "CopyPaste: An Augmentation Method for Speech Emotion Recognition"
description: ""
citekey: pappagariCopyPasteAugmentationMethod2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
---

> [!info] 论文信息
>1. Title：CopyPaste: An Augmentation Method for Speech Emotion Recognition
>2. Author：Raghavendra Pappagari, Jesús Villalba, Piotr Żelasko, Laureano Moro-Velazquez, Najim Dehak
>3. Entry：[Zotero link](zotero://select/items/@pappagariCopyPasteAugmentationMethod2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Pappagari et al_2021_CopyPaste.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***


## ⭐ 重点

- 与只用干净的数据训练的模型相比，用噪声增强的数据训练的模型表现得更好，但在噪声环境下噪声增强的性能更好
- 预训练可以显著提高所有数据集上的模型性能
- 引入声纹识别领域的 x-vector 模型进行迁移学习。- 与只用干净的数据训练的模型相比，用噪声增强的数据训练的模型表现得更好，但在噪声环境下噪声增强的性能更好
- 预训练可以显著提高所有数据集上的模型性能
- 引入声纹识别领域的x-vector模型进行迁移学习。

## 摘要

> [!abstract] Data augmentation is a widely used strategy for training robust machine learning models. It partially alleviates the problem of limited data for tasks like speech emotion recognition (SER), where collecting data is expensive and challenging. This study proposes CopyPaste, a perceptually motivated novel augmentation procedure for SER. Assuming that the presence of emotions other than neutral dictates a speaker's overall perceived emotion in a recording, concatenation of an emotional (emotion E) and a neutral utterance can still be labeled with emotion E. We hypothesize that SER performance can be improved using these concatenated utterances in model training. To verify this, three CopyPaste schemes are tested on two deep learning models: one trained independently and another using transfer learning from an x-vector model, a speaker recognition model. We observed that all three CopyPaste schemes improve SER performance on all the three datasets considered: MSP-Podcast, Crema-D, and IEMOCAP. Additionally, CopyPaste performs better than noise augmentation and, using them together improves the SER performance further. Our experiments on noisy test sets suggested that CopyPaste is effective even in noisy test conditions.

> 

## 预处理

## 概述

## 结果

## 精读

### 引文

## 摘录
