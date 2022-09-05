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
data: 2022-06-02 14:56:57
lastmod: 2022-06-13 17:42:02
---

# 重点

- [开源代码](https://github.com/iiscleap/multimodal_emotion_recognition)
- 引入了一个可学习的前端语音特征提取器
- 

# 摘要

In this work, we propose a novel approach for multi-modal emotion recognition from conversations using speech and text. The audio representations are learned jointly with a learnable audio front-end (LEAF) model feeding to a CNN based classifier. The text representations are derived from pre-trained bidirectional encoder representations from transformer (BERT) along with a gated recurrent network (GRU). Both the textual and audio representations are separately processed using a bidirectional GRU network with self-attention. Further, the multi-modal information extraction is achieved using a transformer that is input with the textual and audio embeddings at the utterance level. The experiments are performed on the IEMOCAP database, where we show that the proposed framework improves over the current state-of-the-art results under all the common test settings. This is primarily due to the improved emotion recognition performance achieved in the audio domain. Further, we also show that the model is more robust to textual errors caused by an automatic speech recognition (ASR) system.

在这项工作中，我们提出了一种新的基于语音和文本的多模态情感识别方法。音频表示与馈送到基于CNN的分类器的可学习音频前端(叶)模型联合学习。文本表示是从来自变压器的预先训练的双向编码器表示(BERT)和门控递归网络(GRU)导出的。使用具有自我注意的双向GRU网络分别处理文本和音频表示。此外，多模态信息提取是使用在发声级别与文本和音频嵌入一起输入的转换器来实现的。实验在IEMOCAP数据库上进行，实验表明，在所有常见测试设置下，所提出的框架比目前最先进的结果有所改善。这主要是由于在音频域中实现了改进的情感识别性能。此外，我们还表明，该模型对自动语音识别(ASR)系统引起的文本错误具有更强的鲁棒性。

# 结果

音频分类器的Leaf-CNN模型在其基本实现中是内存密集型的。为了避免这个问题，叶子特征的步长增加到30ms，而不是缺省值10ms。Leaf-cnn特征抽取器的训练批大小为16，学习率为1×10−5。检查来自cnn分类器的音频表示的维度是否有3个不同的值50、100和200值(表1)。基于对验证数据的性能，来自Leaf-CNN分类器的音频表示维度被固定为100。同样，文本特征抽取器的BERT-GRU模型被训练成32批大小和相同的学习率。对于这个发音级别的嵌入抽取器，发现维度100在验证集上给出了最好的准确率。对于文本和音频，具有自我注意的BiGRU的训练批次为32，学习率为1×10−3。BiGRU层中有自我注意和无自我注意的通道的准确率如表1所示。这对于文本和音频形态来说都是一致的。模型的最后一个部分，即多模式转换器，训练的批次为32，学习率为1×10−4。在不同的隐含层数和隐含层维度的组合下进行了多次实验，如表2所示。结果发现，结果随注意头数的变化可以忽略不计，因此将其固定为12。最终的多模式转换器配置被选择为隐含层维度为120，有12个注意头和3个隐含层。

# 词汇记录

# 精读

随着对会话代理和个人助理的需求不断增长，人类情感的自动识别已经成为增强用户体验的关键任务。利用文本、语音和视频的多模态数据进行人类情感识别，对智能手机、可穿戴设备、智能扬声器、自动驾驶监控、情绪分析和心理健康等各种应用都有重要影响。开发情商的这一领域将使机器在交互中更像人类[1]。情感识别的问题具有挑战性，主要是因为情感的复杂表达是高度个人化的。人类互动中的情绪可以通过面部表情[2]、言语[3]、手势[4]和呼吸等生理信号来检测。此外，不同的模态包含与情感相关的不同程度的信息，因此，设计一种联合的多模态情感识别方法被认为是为了提高这些系统的性能[6]。虽然需要以一种多通道的方式感知情绪的能力，但也需要以一种健壮的方式通过每一种通道感知情绪。在本文中，我们探索了一种语音和文本的情感识别任务。

对于多模态情感识别，Sikka等人探索了Logistic回归和支持向量机分类器。[7]和Castellano et.。Al[8].。

深度学习方面的进展也有利于从语音[9]、视听情感识别[10]以及从联合文本、语音和视觉形式[11]进行情感识别。

Yoon等人的作品。[12]和Lee et.。艾尔。[13]专注于基于语音和文本的情感识别，

Majumder等人。[14]探索使用文本、语音和视频功能的三模态融合进行情感识别。Log-Mel滤波器组特征与其他声学指标一起在与语音中的情感识别相关的工作中被广泛使用[15，16，17]。这些特征是知识驱动的，这意味着数据集中的任何可变性都不会对从音频文件中提取的特征起到明确的作用。这促使研究人员开发可学习的音频特征提取程序[18，19，20]。

在这项工作中，我们提出了一种对话中的情感识别方法，其中我们首先分别使用Leaf[19]和Bert[21]从音频和文本中提取可学习的特征。我们提出了一种跨话语的信息融合方法，该方法针对两种模态中的每一种都使用自我注意网络。这两个模态被组合在多模态转换器中，以便使用长期多模态上下文信息进行更好的分类。我们的模型在广泛使用的IEMOCAP数据集[22]上进行了评估。

对于音频情感识别，已经研究了韵律特征和其他声学特征[23，24]。这里，MEL频率倒谱系数(MFCC)与基于基音的特征一起使用。OpenSMALL[25]是一个被广泛使用的音频特征提取工具包，已经被用于像[15，16]这样的几个作品中。

Wu et.。Al[17]除了音调特征外，还使用了帧长度为250ms的长期对数-梅尔滤波器组特征。

在过去的几年里，随着双向编码表示从转换器(BERT)[21]的迁移学习能力的增强，从文本中提取特征已经有了长足的进步。这在[17]中已经被用于文本特征提取。在另一项工作中，对单词2vec表示[26]训练的卷积神经网络已用于基于文本的情感识别[15，16]。单词表示的全局向量(手套)[27]也被Tripari et应用于情感识别。
艾尔。[28]和Pepino et.。Al[29]。文献[30]利用双向LSTM(bi-LSTM)网络实现了多模态信息的融合。这一点得到了Poria et的进一步改进。
艾尔。[15]其中以分层方式执行融合。
在[12，13]中已经探索了使用注意机制来保持长期背景。自我注意网络的体系结构也被应用于多模态情感识别。模型体系结构的主要组件的示意图如图1所示。

![]({39}_Multimodal%20Transformer%20with%20Learnable%20Frontend%20and%20Self%20Attention%20for%20Emotion%20Recognition.assets/image-20220613162838.png)

音频特征提取


使用可学习的音频分类前端(LEAF)[19]模型来提取音频特征，该模型使用filtering,、pooling、compression和normalization等组件来学习特征。此外，考虑到模型的小参数优点，可学习的前端可以集成到更大的情感识别网络中，并且可以联合学习。LEAF模型对原始音频文件采用一维卷积网络，生成区分语谱图的音频表示。LEAF输出在CNN网络中使用，平均池之后是完全连接的输出层。Leaf-CNN网络与发声级别标签（utterance level labels）联合训练，并且来自后续全连接层的100维特征被用作每个音频发声的嵌入。为了后续模型的学习，冻结了这个叶子-CNN网络，并将来自这一层的嵌入特征用作发声级别的音频特征。

我们使用基于BERT的特征来表示文本[21]。在每个发声文本通过BERT模型之后，来自编码器的最后四个隐藏层被拼接在一起。为了向表征添加更多上下文，BERT输出通过具有隐藏维度100的两层双向门控循环单元(GRU)模型[31]。BERT-GRU模型与发音级别标签联合训练，并将GRU模型输出端的表征作为后续带有自我注意块的BiGRU的发音级别文本嵌入。与音频的Leaf-CNN模型一样，BERT-GRU网络在随后的学习阶段被冻结，嵌入内容被用作发声级别的文本特征。

3.3. 多话语自我关注

对话中的每个话语都有一个情感标签。目的是利用前一时间实例u(t−1)、u(t−2)、...的嵌入表征有条件地预测话语u（t）的嵌入表征输出... 以及未来的时间实例，u（t+1），u（t+2）...的嵌入表征输出。Poria等[15]启发了这项工作中提出的背景信息的增加。有注意力的Bi-GRU网络输入用于音频模态的LEAF-CNN话语嵌入和用于文本的BERT-GRU话语嵌入。注意网络的目标是从先前和未来的话语中选择性地结合上下文，以便能够预测当前话语中的情绪标签。

设从BiGRU到自我关注层的输入的维度为$(B\times S\times H)$。这里，$B$表示批大小，$S$表示对话中的发声数量，$H=$$\left[H_{f}；H_{b}\right]$是发声级别的前向$\left(H_{f}\right)$和后向$\left(H_{b}\right)$输出维度的串联。为简单起见，在这些计算中假定批大小为1。当$B>1$时，矩阵乘积将被张量积代替。

设$O_{f}$和$O_{b}$表示输入到自我注意网络的BiGRU的输出。设$W_{f}^{a}$和$W_{b}^{a}$这两个权重矩阵表示关注层参数。向前方向的注意力计算为，

$$
\begin{aligned}

A_{f} &=\left(O_{f} W_{f}^{a}\right)\left(O_{f} W_{f}^{a}\right)^{T} \\

A_{f}^{i j} &=\frac{\exp \left(A_{f}^{i j}\right)}{\sum_{j=1}^{S} \exp \left(A_{f}^{i j}\right)} \forall i, j \in\{1,2, \ldots, S\} \\

O_{f}^{a} &=A_{f} O_{f}

\end{aligned}
$$

向后方向的注意力是相同的。具有自我注意块的Bi GRU被训练来共同预测视频中所有话语的标签。该输出$\left[O_{f}^{a} ; O_{b}^{a}\right]$用作后续多模变压器的每个话语的嵌入。与特征提取器一样，具有自我注意网络的Bi-GRU在训练后续多模态变压器时被冻结。

具有注意力的BiGRU为语音和文本生成发声级别的表征。这些嵌入是拼接的。采用transformer encoder[32]来融合音频和文本信息以改进情感识别。假设具有自我关注层的转换器能够处理长期依赖关系，并且能够比LSTM或GRU模型更有效地组合模态。


使用语音和文本进行情感识别的深度学习模型使用数据集中提供的音频文件及其文本转录进行训练。在实践中，我们很少遇到带有转录的音频。当用提供的抄本训练模型并在ASR输出上测试时，该测试设置评估模型对文本通道中的噪声的稳健性。为了获得ASR文本，我们使用了Google Speech to Text2 on IEMOCAP音频文件。表4显示了此测试设置下的结果。结果表明，即使有ASR输出，在所有三个测试设置下，模型的性能也不会急剧下降。在CV-5测试策略下，我们的模型的性能比[17]中报告的结果有了相当大的改善(相对改善了31%)。这项工作的主要改进主要是在音频域。如表4所示，该模型对文本通道中的噪声的稳健性进一步证实了仅使用语音输入时性能的改善。精度的提高可以归因于所提出的系统中的许多因素。Leaf的可学习前端功能使模型能够捕获音频的本地时频模式。将GRU与BiGRU层的注意力相结合，有助于模型描述音频信号中的长期信息。此外，多模式转换器有助于文本和音频模式的融合，并允许在音频域中观察到的改进以增强多模式情感识别性能。

## 引文
