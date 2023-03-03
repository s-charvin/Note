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
data: 2022-06-02 14:56:53
lastmod: 2022-06-05 14:51:28
---

# 重点

- [开源代码](https://github.com/david-yoon/attentive-modality-hopping-for-SER)
- 引入音频、文本、视频三模态改进情感识别任务
- 引入注意力机制来融合多模态特征信息
- 提出了一种attentive modality hopping process（注意模态跳跃过程），以其他模态为条件，利用注意力机制和前面计算后的特征向量（或经注意后的特征向量）在当前模态中聚合重要的特征信息。

# 摘要

In this work, we explore the impact of visual modality in addition to speech and text for improving the accuracy of the emotion detection system. The traditional approaches tackle this task by independently fusing the knowledge from the various modalities for performing emotion classification. In contrast to these approaches, we tackle the problem by introducing an attention mechanism to combine the information. In this regard, we first apply a neural network to obtain hidden representations of the modalities. Then, the attention mechanism is defined to select and aggregate important parts of the video data by conditioning on the audio and text data. Furthermore, the attention mechanism is again applied to attend the essential parts of speech and textual data by considering other modalities. Experiments are performed on the standard IEMOCAP dataset using all three modalities (audio, text, and video). The achieved results show a significant improvement of 3.65% in terms of weighted accuracy compared to the baseline system.

在这项工作中，我们探索除了语音和文本之外，还有视觉模态对情绪检测系统的影响，以提高情绪检测系统的准确性。传统的方法通过独立地融合来自各种模态的知识来处理这一任务，以执行情感分类。与这些方法不同，我们通过引入注意力机制来结合信息来解决这个问题。在这一点上，我们首先应用神经网络来获得模态的隐藏表征。然后，定义了注意机制，通过对音频和文本数据的条件化处理来选择和聚合视频数据的重要部分。此外，注意机制再次被应用于通过考虑其他模态来注意基本的词性和文本数据。在标准IEMOCAP数据集上使用所有三种模态(音频、文本和视频)进行了实验。结果表明，与基线系统相比，加权精度有3.65%的显着提高。

# 结果

# 词汇记录

# 精读

情绪识别在所有人类交流中都起着至关重要的作用。我们的反应取决于情绪状态，并且在传达信息时也提供非语言提示。最近，在计算机辅助技术中已经有许多努力来理解情绪[1]。自动客户服务系统通常设计用于对说话人的情绪进行分类以增强用户体验。情绪分类在语旁领域也是有益的。最近，商业数字辅助应用，如Siri，发现副语言信息，如情感，有利于识别说话者的意图[2]。人类通常使用多模态信息来识别情绪。然而，多模态对这一领域的影响尚未得到充分研究。在本文中，我们有兴趣利用文本，言语和视觉模型中的信息来识别情绪。在过去，已经从语音信号中探索了不同的情绪识别方法[3,4]。大多数言语情绪技术都专注于提取低级或高级特征。特别地，应用信号处理技术来提取特征，例如cepstral和韵律prosodic特征。超分割Suprasegmental特征（如cepstral或韵律contours）已被证明可以为这项任务提供良好的表现[5]。此外，统计建模技术，如隐马尔可夫模型（HMM）和高斯混合模型（GMM），已成功用于此任务[6,7]。最近，除了用于情绪分类的语音信号之外，研究人员还探索了文本信息的应用。词汇信息通常用于搜索表达说话者情绪状态的关键字。在[8]中，通过使用消息的单词表征来使用词汇信息。最近的方法利用深度神经网络（DNN）强大的建模功能来融合来自两种模态的信息[9,10,11]。模态的隐藏表征用于组合来自声学和文本数据的知识以用于情绪分类。在我们以前的工作[12]中，我们探索了利用文本信息的注意机制。训练注意机制自动总结词汇内容和言语话语。实验评估表明标准IEMOCAP数据集具有卓越的性能[13]。

在本文中，我们通过将视觉信息纳入框架并提出一种有效利用多模态知识的注意机制来扩展这种方法。这是由于人类通过面部表情，语音信号和词汇内容表达情感这一事实。我们假设除了语音和词汇信息之外，利用视觉知识将导致卓越的表现。

与**独立组合**来自模态的信息相反，我们建议应用一种关注机制，该机制汇总来自以其他两种模态为条件提取的当前模态的知识。所提出的方法首先从三种模态（语音，文本和视觉）获得隐藏表征的序列。
- 通过将注意力权重与隐藏单元线性组合来获得视觉模型的汇总向量。
- 然后应用该矢量以获得声学数据的注意权重。
- 更新的视觉和声学数据连续用于计算文本数据的注意权重以聚合文本模态的显着部分。

随着这个过程持续多次，我们假设该机制将有效地计算每种模态的相关部分。为了评估所提出的方法的性能，我们在标准的IEMOCAP数据集上进行了情绪识别实验。在该语料库上的实验表明，所提出的方法在加权准确度方面优于基线系统3.65%的相对改善。另外，我们通过增加模态的迭代来获得改进的模型性能。实验结果表明，我们提出的模型通过迭代跳跃过程正确地学习了在模态之间聚合必要信息。

近年来，已有几种神经网络方法被成功地应用于情感分类。研究人员提出了基于卷积神经网络(CNN)的模型，该模型对语音话语进行训练以执行识别[14，15]。也有一些使用注意机制的成功方法[16，17]。特别是，[17]中的工作提出了一种将基于注意的建模合并到递归神经网络(RNN)体系结构中的方法。注意力机制被设计为计算每一帧的权重或相关性。通过对这些加权语音特征的时间聚集来获得发声级别表示。注意单元被设计为自动获取用于情感识别的语音片段。使用声学和词汇知识的情感识别也在文献中进行了探索。这些作品的灵感来自于这样一个事实，即情感对话不仅由言语组成，也由文本内容组成。在[18]中，利用情感关键字来有效地识别类别。最近在[9，10，19]中，已经探索了一种基于长短期记忆(LSTM)的网络来编码两种模态的信息。此外，已经有一些尝试使用注意间机制融合各种模态[11，12]。然而，这些方法的设计只考虑了声学和文本信息之间的交互作用。

本节介绍应用于语音情感识别任务的方法。我们首先引入递归编码器来分别对音频、文本和视频模态进行编码。然后，我们提出了一种逐个利用每种模态的方法。在该技术中，提出了一种细心的模态跳跃过程，通过迭代聚合过程获得每个模态的相关部分。

受文献[9，17，20]中所用结构的启发，我们采用递归神经网络对语音信号中的一系列特征进行编码，并将信号分类为情感类别之一。特别是，我们对每个模态(即，声学、文本、视觉)采用门控递归单元(GRU)[21]来编码信息，如图1所示。GRU通过如下更新其隐藏状态来编码每个模态的特征向量序列：

$$ \mathbf{h}_{t}=f_{\theta}\left(\mathbf{h}_{t-1}, \mathbf{x}_{t}\right), $$ 其中$f_{\theta}$是具有权重参数$\theta的GRU网络，\mathbf{h}_{t}$表示在$t$时间步长的隐藏状态，以及$\mathbf{x}_{t}$表示目标模态中的$t$个连续特征。该递归编码器以与独立音频、文本和视频模态相同的方式使用。对于视频数据，我们从预先训练的ResNet[22]获得每一帧的固定维度表示。

我们提出了一种新的迭代注意过程，称为注意力模态跳跃机制(AMH)，它聚集了每个模态上的显著信息来预测语音的情绪。图1显示了建议的AMH模型的体系结构。以前的研究通过融合每个模态上的信息，使用神经网络模型独立使用多模态信息[9，19]。最近，研究人员还研究了模态的注意间机制[11，12]。与这种方法相反，我们提出了一种神经网络体系结构，它通过迭代过程以其他模态为条件，在一种模态中聚合信息。

![]({36}_Attentive%20Modality%20Hopping%20Mechanism%20for%20Speech%20Emotion%20Recognition@yoonAttentiveModalityHopping2020.assets/image-20220605170157.png)



首先，通过公式(1)使用递归编码器对每个模态的序列特征进行编码。然后，音频递归编码器的最后一步隐藏状态$\mathbf{h}_{\text{Last}}^{A}$和文本递归编码器$\mathbf{h}_{\text{Last}}^{T}$融合在一起以形成上下文知识$\mathbf{C}$。然后，我们将注意力机制应用于视频序列$\mathbf{h}_{\mathbf{t}}^{V}$，以聚集视频形态的显著部分。由于该模型是用单一注意方法开发的，我们将该模型称为AMH-1。AMH-1模型的最终结果$\mathbf{H}_{\text{Hop}1}$计算如下：

$$ \begin{aligned} &\mathbf{H}_{\text {hop } 1}=\left[\mathbf{h}_{\text {last }}^{A} ; \mathbf{h}_{\text {last }}^{T} ; \mathbf{H}_{1}^{V}\right] \\ &\mathbf{H}_{1}^{V}=\sum_{i} a_{i} \mathbf{h}_{i}^{V} \\ &a_{i}=\frac{\exp \left((\mathbf{C})^{\top} \mathbf{W} \mathbf{h}_{i}^{V}\right)}{\sum_{i} \exp \left((\mathbf{C})^{\top} \mathbf{W} \mathbf{h}_{i}^{V}\right)},(i=1, \ldots, t), \\ &\mathbf{C}=f\left(\mathbf{h}_{\text {last }}^{A}, \mathbf{h}_{\text {last }}^{T}\right) \end{aligned} $$ 
其中$f$是融合函数(在本研究中我们使用向量连接)，$\mathbf{W}\in\mathbb{R}^{d\times d}$和偏差$\mathbf{b}$是学习的模型参数。整个流程如图1(A)所示。公式(2)中的$\mathbf{H}_{1}^{V}$是一种考虑了音频和文本模态的视觉信息的新模态表示。

利用该信息，我们将称为$\mathbf{A M H}\mathbf{M}$-2的第二注意模态跳跃过程应用于音频序列。AMH-2模型的最终结果$\mathbf{H}_{\text{Hop}2}$计算如下：
$$
\begin{aligned}
&\mathbf{H}_{\mathrm{hop} 2}=\left[\mathbf{H}_{1}^{A} ; \mathbf{h}_{\text {last }}^{T} ; \mathbf{H}_{1}^{V}\right] \\
&\mathbf{H}_{1}^{A}=\sum_{i} a_{i} \mathbf{h}_{i}^{A}, \\
&a_{i}=\frac{\exp \left((\mathbf{C})^{\top} \mathbf{W} \mathbf{h}_{i}^{A}\right)}{\sum_{i} \exp \left((\mathbf{C})^{\top} \mathbf{W} \mathbf{h}_{i}^{A}\right)},(i=1, \ldots, t), \\
&\mathbf{C}=f\left(\mathbf{h}_{\text {last }}^{T}, \mathbf{H}_{1}^{V}\right)
\end{aligned}
$$
其中，$\mathbf{H}_{1}^{A}$是考虑AMH-1过程之后的文本和视觉模态的音频信息的新表示。

我们进一步将第三注意模态跳跃过程应用于文本序列，称为$\mathbf{A}\mathbf{M H}-\mathbf{3}$，具有来自等式(2)和(3)的更新的音频和视觉表示。AMH-3模型的最终结果$\mathbf{H}_{\text{Hop}3}$计算如下：

$$
\begin{aligned}
&\mathbf{H}_{\mathrm{hop} 3}=\left[\mathbf{H}_{1}^{A} ; \mathbf{H}_{1}^{T} ; \mathbf{H}_{1}^{V}\right] \\
&\mathbf{H}_{1}^{T}=\sum_{i} a_{i} \mathbf{h}_{i}^{T} \\
&a_{i}=\frac{\exp \left((\mathbf{C})^{\boldsymbol{\top}} \mathbf{W} \mathbf{h}_{i}^{T}\right)}{\sum_{i} \exp \left((\mathbf{C})^{\top} \mathbf{W} \mathbf{h}_{i}^{T}\right)},(i=1, \ldots, t), \\
&\mathbf{C}=f\left(\mathbf{H}_{1}^{A}, \mathbf{H}_{1}^{V}\right)
\end{aligned}
$$

其中，$\mathbf{H}_{1}^{T}$是考虑到音频和视频形态的文本信息的更新表示。

同样，我们可以重复$\mathbf{A}\mathbf{M H}-\mathbf{1}$过程，更新后的模态为$\mathbf{H}_{1}^{A}、\mathbf{H}_{1}^{T}$和$\mathbf{H}_{1}^{V}$，以定义AMH-4过程并计算$\mathbf{H}_{\mathbf{hop}4}$，如下所示：

$$
\begin{aligned}
&\mathbf{H}_{\mathrm{hop} 4}=\left[\mathbf{H}_{1}^{A} ; \mathbf{H}_{1}^{T} ; \mathbf{H}_{2}^{V}\right], \\
&\mathbf{H}_{2}^{V}=\sum_{i} a_{i} \mathbf{h}_{i}^{V}, \\
&a_{i}=\frac{\exp \left((\mathbf{C})^{\top} \mathbf{W} \mathbf{h}_{i}^{V}\right)}{\sum_{i} \exp \left((\mathbf{C})^{\top} \mathbf{W} \mathbf{h}_{i}^{V}\right)},(i=1, \ldots, t), \\
&\mathbf{C}=f\left(\mathbf{H}_{1}^{A}, \mathbf{H}_{1}^{T}\right) .
\end{aligned}
$$

由于所提出的AMH机制采用迭代的模态跳跃过程，因此我们可以推广$\mathbf{A}\mathbf{M H}-\mathbf{N}$公式，该公式允许模型通过按顺序重复等式$(2)、(3)$和(4)来在模态上跳$N$次。

因为我们的目标是对语音情感进行分类，所以我们通过Softmax函数传递AMH-N的最终结果$\mathbf{H}_{\mathbf{hop}\mathbf{N}}$来预测七类情感类别。我们采用由下式定义的交叉熵损失函数：

$$
\begin{aligned}
\hat{y}_{c} &=\operatorname{softmax}\left(\left(\mathbf{H}_{\mathrm{hopN}}\right)^{\top} \mathbf{W}+\mathbf{b}\right) \\
\mathcal{L} &=\frac{1}{N} \sum_{j=1}^{N} \sum_{c=1}^{C} y_{j, c} \log \left(\hat{y}_{j, c}\right)
\end{aligned}
$$


其中$y_{j，c}$是真实的标签向量，而$\hat{y}_{j，c}$是来自Softmax层的预测概率。$\mathbf{W}$和偏差$\mathbf{b}$是模型参数。$C$是班级总数，$N$是训练中使用的样本总数。

## 引文
