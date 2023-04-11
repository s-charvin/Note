---
title: "Decentralizing Feature Extraction with Quantum Convolutional Neural Network for Automatic Speech Recognition"
description: ""
citekey: yangDecentralizingFeatureExtraction2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
---

> [!info] 论文信息
>1. Title：Decentralizing Feature Extraction with Quantum Convolutional Neural Network for Automatic Speech Recognition
>2. Author：Chao-Han Huck Yang, Jun Qi, Samuel Yen-Chi Chen, Pin-Yu Chen, Sabato Marco Siniscalchi, Xiaoli Ma, Chin-Hui Lee
>3. Entry：[Zotero link](zotero://select/items/@yangDecentralizingFeatureExtraction2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Yang et al_2021_Decentralizing Feature Extraction with Quantum Convolutional Neural Network for.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：https://github.com/huckiyang/QuantumSpeech-QCNN
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***


## ⭐ 重点

- 

## 摘要

> [!abstract] We propose a novel decentralized feature extraction approach in federated learning to address privacy-preservation issues for speech recognition. It is built upon a quantum convolutional neural network (QCNN) composed of a quantum circuit encoder for feature extraction, and a recurrent neural network (RNN) based end-to-end acoustic model (AM). To enhance model parameter protection in a decentralized architecture, an input speech is first up-streamed to a quantum computing server to extract Mel-spectrogram, and the corresponding convolutional features are encoded using a quantum circuit algorithm with random parameters. The encoded features are then down-streamed to the local RNN model for the final recognition. The proposed decentralized framework takes advantage of the quantum learning progress to secure models and to avoid privacy leakage attacks. Testing on the Google Speech Commands Dataset, the proposed QCNN encoder attains a competitive accuracy of 95.12% in a decentralized model, which is better than the previous architectures using centralized RNN models with convolutional features. We conduct an in-depth study of different quantum circuit encoder architectures to provide insights into designing QCNN-based feature extractors. Neural saliency analyses demonstrate a high correlation between the proposed QCNN features, class activation maps, and the input Mel-spectrogram. We provide an implementation1 for future studies.

> 我们提出了一种新的联合学习（federated learning）中的分散特征提取方法，用来解决语音识别中的隐私保护问题。它建立在量子卷积神经网络(QCNN)的基础上，该网络由用于特征提取的量子电路编码器（quantum circuit encoder）和基于端到端声学模型(AM)的递归神经网络(RNN)组成。为了增强分布式体系结构中的模型参数保护，首先将输入的语音上行到量子计算服务器（quantum computing server）以提取Mel谱图，然后使用带有随机参数的量子电路算法（quantum circuit algorithm）对相应的卷积特征进行编码。然后将编码的特征向下传输到本地RNN模型以进行最终识别。提出的去中心化框架利用量子学习过程来保护模型，避免隐私泄露攻击。在Google语音命令数据集上进行测试，所提出的QCNN编码器在去中心化模型下获得了95.12%的竞争准确率，优于以往使用集中式卷积特征的RNN模型的结构。我们对不同的量子电路编码器体系结构进行了深入的研究，为设计基于QCNN的特征抽取器提供了见解。神经显著分析表明，所提出的QCNN特征、类激活图和输入的MEL谱图之间具有高度的相关性。

## 预处理

## 概述

## 结果

## 精读

![]({29}_Decentralizing%20Feature%20Extraction%20with%20Quantum%20Convolutional%20Neural%20Network%20for%20Automatic%20Speech%20Recognition@yangDecentralizingFeatureExtraction2021.assets/image-20220603150559.png)


随着对声学数据隐私问题的日益关注[1]，设计满足新隐私保护法规要求的新型自动语音识别（ASR）架构至关重要，例如GDPR[2]。垂直联合学习（VFL）[3]是一种潜在的数据保护策略，通过分散端到端深度学习[4]框架并将特征提取与ASR推理引擎分开。随着商业量子技术的最新进展[5]，量子机器学习（QML）[6]由于其在参数加密和隔离方面的优势而成为VFL的理想构建模块。为此，通常由经典位表示的QML输入需要首先基于量子位编码为量子状态。接下来，将近似算法（例如，量子分支程序[7]）应用于基于具有噪声容限的量子电路[8]的量子器件。为了实现我们提出的方法，我们利用最先进的嘈杂中间尺度量子（NISQ）[9]平台（5到50量子比特）进行学术和商业应用[10]。它可以在基于云的计算提供商的可访问量子服务器上设置[5]。如图1所示，我们提出了一种分散声学建模（AM）方案，通过结合变分量子电路（VQC）学习范式[6]和深度神经网络来设计量子卷积神经网络（QCNN）[13][14]（DNN）。VQC是指一种量子算法，具有灵活的设计可访问性，耐噪声[6,8]，适用于NISQ硬件，光照或不需要量子纠错。基于VFL下VQC的优势，可以用较少的纠缠编码量子比特实现量子增强数据处理方案[15,7]，以确保模型参数保护和较低的计算复杂度。如表1所示，据作者所知，这是第一项将量子电路和DNN结合起来并为ASR构建新QCNN[13]的工作。为了提供安全的数据流水线和可靠的量子计算，我们引入了分散式ASR任务的VFL架构，其中使用远程NISQ云服务器生成基于量子的特征，并使用本地模型执行ASR解码[11]。我们将分散的基于量子的ASR系统称为QCNN-ASR。在量子计算机产生的机器噪声的Google语音命令数据集上进行评估，所提出的QCNN-ASR框架在单词识别方面达到了95.12%的竞争准确率。.



### 引文

## 摘录
