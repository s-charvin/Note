---
title: "Multimodal Cross- and Self-Attention Network for Speech Emotion Recognition"
description: ""
citekey: sunMultimodalCrossSelfAttention2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:33:05
lastmod: 2023-04-11 11:57:43
---

> [!info] 论文信息
>1. Title：Multimodal Cross- and Self-Attention Network for Speech Emotion Recognition
>2. Author：Licai Sun, Bin Liu, Jianhua Tao, Zheng Lian
>3. Entry：[Zotero link](zotero://select/items/@sunMultimodalCrossSelfAttention2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Sun et al_2021_Multimodal Cross- and Self-Attention Network for Speech Emotion Recognition.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现： https://github.com/david-yoon/attentive-modality-hopping-for-SER, https://github.com/SysCV/pcan
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 语音文本双模态任务引入跨模态交互注意力机制, 并于自注意力机制相结合, 在模态间传播信息。

## 摘要

> [!abstract] Speech Emotion Recognition (SER) requires a thorough understanding of both the linguistic content of an utterance (i.e., textual information) and how the speaker utters it (i.e., acoustic information). The one vital challenge in SER is how to effectively fuse these two kinds of information. In this paper, we propose a novel Multimodal Cross- and Self-Attention Network (MCSAN) to tackle this problem. The core of MCSAN is to employ the parallel cross- and self-attention modules to explicitly model both inter- and intra-modal interactions of audio and text. Specifically, the cross-attention module utilizes the cross-attention mechanism to guide one modality to attend to the other modality and update the features accordingly. Similarly, the self-attention module employs the self-attention mechanism to propagate information within each modality. We evaluate MCSAN on two benchmark datasets, IEMOCAP and MELD. Experimental results demonstrate that our proposed model achieves state-of-the-art performance on both datasets.

> 语音情感识别(SER)需要对话语的语言内容(即文本信息)和说话人如何说出(即声学信息)进行深入的理解。SER面临的一个重要挑战是如何有效地融合这两种信息。在本文中，我们提出了一种新的多模式交叉和自我注意网络(MCSAN)来解决这一问题。MCSAN的核心是使用并行的交叉和自我注意模块来显式地建模音频和文本的模式间和模式内的交互。具体地说，交叉注意模块利用交叉注意机制来引导一个模态关注另一个模态并相应地更新特征。同样，自我注意模块使用自我注意机制在每个模态内传播信息。我们在IEMOCAP和MELD两个基准数据集上对MCSAN进行了评估。实验结果表明，我们提出的模型在两个数据集上都达到了最好的性能。

## 预处理

## 概述

## 结果

IEMOCAP 按照[20,14]进行10倍交叉验证，其中8:1:1分别用于训练，验证和测试。采用加权准确度（WA，即总体准确度）和未加权准确度（UA，即所有情绪类别的平均准确度）作为评估指标。MELD[21]整个数据集分为三部分：训练（9989），验证（1109）和测试（2610）。在[21,22]之后，我们报告了该数据集上的加权平均 F1分数。

我们从语音信号中提取40维Mel频率Cepstral系数（MFCC）。窗口大小和帧移大小分别设置为25毫秒和10毫秒。MFCC特征序列的最大长度设置为1000。我们在将它们输入音频编码器之前执行z-normalization。

对于文本特征，我们首先将word-tokenizer应用于数据集提供的transcripts。然后使用预先训练的GloVe模型将话语中的每个单词嵌入到300维矢量中[23]。我们在PyTorch框架内实现了我们的模型。模型中隐藏的神经元数量是128个。交叉和自我注意模块中的堆叠层数为1。头数设置为8。音频编码器中卷积层和最大池层的内核大小为3。为了训练模型，我们使用Adam优化器[24]，IEMOCAP的学习率为0.001，MELD的学习率为0.0005。批量大小为256。我们在IEMOCAP上训练最多30个epoch，在MELD上训练20个epoch。

## 精读

情绪在人类交流中起着重要作用。言语情绪识别（SER）旨在赋予机器感知情绪的能力。SER在人机交互领域具有广泛的应用[1]。以无处不在的语音助理（如亚马逊的Alexa和Apple的Siri）为例。他们有必要推断用户的情绪并做出适当的回应以增强用户体验。最近关于SER的研究仅关注声学信息。已经开发了各种深度学习模型来从手工声学特征或原始语音信号中提取与情绪相关的信息。如卷积神经网络（CNN）[2,3]，递归神经网络（RNN）[4,5]，自我注意机制[6]及其组合[7,8,9]。嵌入语音中的文本信息较少被利用。这些信息对于SER也是至关重要的，因为在某些情况下，话语的情绪可以由语言语义决定。例如，“这真的是一个不幸的日子？”表示说话者情绪悲伤。然而，融合声学和文本信息并不是微不足道的。在融合多模态信息时，通常需要考虑两种交互，即模态内交互和模态间交互[10]。模态内交互是指单一模态内的细粒度特征交互。例如声学特征中的帧-帧关系和文本特征中的单词-单词关系。通过对模态内相互作用进行建模，我们可以捕捉情绪预测的模态特定模式。由于以不同音调说出句子可能会产生完全不同的情绪，因此有必要对音频和文本之间的帧字关系进行建模。这些是所谓的模态间相互作用。模态间交互是同步的（例如，强调特定的单词）或异步的（例如，说一些有趣的东西后的笑声）。最近，一些工作已经探索融合SER的声学和文本信息。一般来说，这些作品可以分为三种类型。第一类为每种模态建立独立模型，并将其输出结合起来进行最终情绪分类[11,12,13,14]。每种模式都可以采用不同的架构来最好地适应不同的输入。

例如，Yoon等[11]采用两个长短期记忆（LSTM）网络对音频和文本进行编码。

Tripathi等[13]将1D-CNN用于词嵌入，将2D-CNN用于光谱特征。尽管可以捕获模态内交互，但是没有探索模态间交互。

第二种类型利用对齐的音频和文本作为输入[15]。对齐的特征首先被融合，然后被馈送到用于顺序学习的时间模型中。因此，可以在整个过程中捕获模态间交互。但是，成本是提供对齐信息。为了克服这个问题，

第三种类型利用注意机制来推断音频和文本之间的潜在跨模态关系。

Yoon等[16]提出了一种新颖的多跳机制，通过调节另一种模态迭代地选择和聚合来自一种模态的信息。

Xu等人[17]利用注意机制学习每个单词的潜在对齐语音帧。然而，它们都没有明确地模拟音频和文本的模态内和模态间交互。

我们在本文中提出了一种新颖的多模式交叉和自我关注网络（MCSAN）。MCSAN主要由交叉注意模块和两个自我注意模块组成。交叉注意模块利用交叉注意机制在音频和文本之间传播信息，而自我注意模块采用自我注意机制在每种模态内传播信息。由于这些模块，MCSAN可以显式地模拟音频和文本的模型间和模型内交互。为了验证MCSAN的有效性，我们对两个数据集进行了实验。结果表明，它优于最先进的方法。我们还进行消融研究来证明我们模型的设计选择是正确的。

如图1所示，MCSAN首先使用音频编码器和文本编码器分别对声学和文本特征进行编码。然后，编码后的特征序列被送入交叉注意和自我注意模块，以学习音频和文本的模式间和模式内交互。最后，这些模块的输出被连接起来，并发送到一个完全连接的分类器中进行情感预测。具体内容介绍如下。

![]({31}_Multimodal%20Cross-%20and%20Self-Attention%20Network%20for%20Speech%20Emotion%20Recognition@sunMultimodalCrossSelfAttention2021.assets/image-20220603194955.png)

2.1. 音频编码器

假设语音的输入声学特征序列表示为 $\mathbf{X}_{a}=\left\{\mathbf{x}_{a}^{1}, \mathbf{x}_{a}^{2}, \ldots, \mathbf{x}_{a}^{T_{a}^{\prime}}\right\}^{T} \in \mathbb{R}^{T_{a}^{\prime} \times d_{a}}\left(T_{a}^{\prime}\right.$ 是声学帧的数量, $d_{a}$ 是特征数量). 我们采用CNN的体系结构，并采用LSTM作为音频编码器。具体地说，使用两个一维时间卷积层来捕获局部特征。由于 $T_{a}^{\prime}$ 通常较大，因此每个卷积层之后是一个最大合并层，以降低时间分辨率并便于后续学习。然后使用双向LSTM(BiLSTM)层来捕获序列内的时间相关性。对BiLSTM层的前向和后向隐藏特征向量进行平均，得到编码后的声学特征。整个过程可以概括为：
$$
\begin{aligned}
\mathbf{X}^{a} &=\operatorname{ConvBlock}\left(\operatorname{ConvBlock}\left(\mathbf{X}^{a}\right)\right) \\
\overleftarrow{\mathbf{h}}{ }_{a}^{t}, \overrightarrow{\mathbf{h}}_{a}^{t} &=\operatorname{BiLSTM}\left(\mathbf{x}_{a}^{t}, \overleftarrow{\mathbf{h}}_{a}^{t+1}, \overrightarrow{\mathbf{h}}_{a}^{t-1}\right), t=1,2, \ldots, T_{a} \\
\mathbf{h}_{a}^{t} &=\frac{1}{2}\left(\overleftarrow{\mathbf{h}}_{a}^{t}+\overrightarrow{\mathbf{h}}_{a}^{t}\right), t=1,2, \ldots, T_{a}
\end{aligned}
$$
其中， ConvBlock $(\cdot)=\operatorname{Max} \operatorname{Pool}(\operatorname{Conv} 1 D(\cdot)), T_{a}$ 是第二个池层之后的声学帧的数量。 我们将 $\mathbf{H}_{a}=\left\{\mathbf{h}_{a}^{1}, \mathbf{h}_{a}^{2}, \ldots, \mathbf{h}_{a}^{T_{a}}\right\}^{T} \in \mathbb{R}^{T_{a} \times d}$ ( $d$ 是统一的特征维度) 表示为编码的声学特征序列。

2.2. Text Encoder

假设语音对应的的输入文本特征序列表示为 $\mathbf{X}_{l}=\left\{\mathbf{x}_{l}^{1}, \mathbf{x}_{l}^{2}, \ldots, \mathbf{x}_{l}^{T_{l}}\right\}^{T} \in \mathbb{R}^{T_{l} \times d_{l}}$ (T $T_{l}$ 是字数, $d_{l}$ 是特征尺寸). 考虑到 $T_{l}$ 通常很小，我们只使用双向LSTM层来编码词级文本特征。编码后的文本特征序列 $\mathbf{H}_{l}=$ $\left\{\mathbf{h}_{l}^{1}, \mathbf{h}_{l}^{2}, \ldots, \mathbf{h}_{l}^{T_{l}}\right\}^{T} \in \mathbb{R}^{T_{l} \times d}$ 可以通过如下计算得到:
$$
\begin{aligned}
\overleftarrow{\mathbf{h}}_{a}^{t}, \overrightarrow{\mathbf{h}}_{a}^{t} &=\operatorname{BiLSTM}\left(\mathbf{x}_{a}^{t}, \overleftarrow{\mathbf{h}}_{a}^{t+1}, \overrightarrow{\mathbf{h}}_{a}^{t-1}\right), t=1,2, \ldots, T_{a} \\
\mathbf{h}_{l}^{t} &=\frac{1}{2}\left(\overleftarrow{\mathbf{h}}_{l}^{t}+\overrightarrow{\mathbf{h}}_{l}^{t}\right), t=1,2, \ldots, T_{l}
\end{aligned}
$$

2.3. Cross-Attention Module

交叉注意模块旨在捕捉每对声学框架和文本单词之间的跨模式交互。该模块由一个位置嵌入层(为了简单起见，我们没有在图1中描述它)和N个堆叠的交叉注意力层和前馈层组成。位置嵌入层用于将时间信息注入特征序列[18]。该模块的主要观点是利用交叉注意机制来学习两个模态之间的关联，然后根据学习到的关联将信息从一个模态传播到另一个模态。在接下来的部分中，我们详细介绍了交叉注意机制。要了解音频和文本之间的关联，我们首先需要使用线性投影将每个特征序列转换为三个术语，即query, key, 和value：
$$
\begin{gathered}
\mathbf{Q}_{a}, \mathbf{Q}_{l}=\mathbf{W}_{a}^{Q} \mathbf{H}_{a}, \mathbf{W}_{l}^{Q} \mathbf{H}_{l} \\
\mathbf{K}_{a}, \mathbf{K}_{l}=\mathbf{W}_{a}^{K} \mathbf{H}_{a}, \mathbf{W}_{l}^{K} \mathbf{H}_{l} \\
\mathbf{V}_{a}, \mathbf{V}_{l}=\mathbf{W}_{a}^{V} \mathbf{H}_{a}, \mathbf{W}_{l}^{V} \mathbf{H}_{l}
\end{gathered}
$$
其中 $\mathbf{Q}_{m}, \mathbf{K}_{m}, \mathbf{V}_{m} \in \mathbb{R}^{T_{m} \times d}$ 是第m模态特征序列的query, key, 和value $m \in\{a, l\}$. $\mathbf{W}_{m}^{Q}, \mathbf{W}_{m}^{K}, \mathbf{W}_{m}^{V} \in$ $\mathbb{R}^{d \times d}$ 是相应的投影矩阵。

在[18]的基础上，我们以交叉的方式计算音频和文本的query和key的点积，以估计两个模态之间的关联。然后通过Softmax函数对结果进行缩放和逐行归一化，以获得关注度权重。在那之后,。我们使用相应的权重聚合每个特征序列的值项，以获得两个模态之间的传播信息：

$$
\begin{aligned}
&\Delta \mathbf{H}_{a \rightarrow l}=\operatorname{softmax}\left(\mathbf{Q}_{l} \mathbf{K}_{a}^{T} / \sqrt{d}\right) \mathbf{V}_{a} \\
&\Delta \mathbf{H}_{l \rightarrow a}=\operatorname{softmax}\left(\mathbf{Q}_{a} \mathbf{K}_{l}^{T} / \sqrt{d}\right) \mathbf{V}_{l}
\end{aligned}
$$
其中 $\Delta \mathbf{H}_{a \rightarrow l} \in \mathbf{H}^{T_{l} \times d}, \Delta \mathbf{H}_{l \rightarrow a} \in \mathbb{R}^{T_{a} \times d}$ 分别表示从音频到文本和文本到音频的传播信息。

上面描述的过程是单头注意力。在实践中，我们使用多头注意，这可以通过多次做单头注意，然后结合每个头的结果来完成。详情见[18]。

最后，我们用来自另一个模态的传播信息来更新另一个模态的特征。

$$
\begin{aligned}
\mathbf{H}_{a} &=\operatorname{Layer} \operatorname{Norm}\left(\mathbf{H}_{a}+\Delta \mathbf{H}_{l \rightarrow a}\right) \\
\mathbf{H}_{l} &=\operatorname{Layer} \operatorname{Norm}\left(\mathbf{H}_{l}+\Delta \mathbf{H}_{a \rightarrow l}\right)
\end{aligned}
$$
为了进一步增加表示能力，在交叉注意力层之后增加了完全连接的前馈层[18]：
$$
\begin{aligned}
\mathbf{H}_{a} &=\operatorname{Layer} \operatorname{Norm}\left(\mathbf{H}_{a}+F e e d F \operatorname{orward}\left(\mathbf{H}_{a}\right)\right) \\
\mathbf{H}_{l} &=\operatorname{Layer} \operatorname{Norm}\left(\mathbf{H}_{l}+F \text { eedForward }\left(\mathbf{H}_{l}\right)\right)
\end{aligned}
$$
我们将模块中最后一个堆叠层的输出分别表示为$\mathbf{H}_{a}^{c}$ and $\mathbf{H}_{l}^{c}$。

2.4. Self-Attention Module

与交叉注意模块平行，自我注意模块旨在捕获音频和文本中的模态内交互。这个模块与交叉注意模块相似，只是使用了自我注意机制。自我注意机制与交叉注意机制有着相同的精神。唯一的区别是查询、键和值来自相同的模态。因此，在自我注意模块中，一个堆叠层的整个过程可以总结如下：

$$
\begin{aligned}
\Delta \mathbf{H}_{m} &=\operatorname{softmax}\left(\mathbf{Q}_{m} \mathbf{K}_{m}^{T} / \sqrt{d}\right) \mathbf{V}_{m} \\
\mathbf{H}_{m} &=\text { Layer } \operatorname{Norm}\left(\mathbf{H}_{m}+\Delta \mathbf{H}_{m}\right) \\
\mathbf{H}_{m} &=\text { Layer } \operatorname{Norm}\left(\mathbf{H}_{m}+\text { FeedForward }\left(\mathbf{H}_{m}\right)\right)
\end{aligned}
$$
其中 $\Delta \mathbf{H}_{m} \in \mathbb{R}^{T_{m} \times d}$ 模态m内的传播信息， $m \in\{a, l\}$. 我们将图1中两个自我注意模块中最后一层的输出分别表示 $\mathbf{H}_{a}^{s}$ and $\mathbf{H}_{l}^{s}$.

为了执行最终分类，我们首先使用全局最大池层来总结交叉和自我注意模块的每个输出。假设$\mathbf{H}_{a}^{c}, \mathbf{H}_{l}^{c}, \mathbf{H}_{a}^{s}, \mathbf{H}_{l}^{s}$ 的汇总特征分别为 $\mathbf{h}_{a}^{c}, \mathbf{h}_{l}^{c}, \mathbf{h}_{a}^{s}, \mathbf{h}_{l}^{s} \in \mathbb{R}^{d}$. 然后，我们将它们连接起来，以获得语音级的表示。最后，遵循完全连接的网络和Softmax层来预测潜在的情感。利用交叉熵损失对模型进行优化。上述过程概括如下：

$$
\begin{aligned}
&\mathbf{h}=\operatorname{Concat}\left(\mathbf{h}_{a}^{c}, \mathbf{h}_{l}^{c}, \mathbf{h}_{a}^{s}, \mathbf{h}_{l}^{s}\right) \\
&\hat{\mathbf{y}}=\operatorname{Softmax}\left(f_{\theta}(\mathbf{h})\right) \\
&\mathcal{L}=-\sum_{i} y_{i} \log \left(\hat{y}_{i}\right)
\end{aligned}
$$
其中 $\mathbf{y}=\left\{y_{1}, y_{2}, \ldots, y_{n}\right\}^{T}$ 是情感标签的 one-hot 向量, $\hat{\mathbf{y}}=\left\{\hat{y}_{1}, \hat{y}_{2}, \ldots, \hat{y}_{n}\right\}^{T}$ 是预测的概率分布, $n$ 是情感类别的个数, $f_{\theta}$ 是参数为 $\theta$ 的全连接网络。


3.3. 基线

在IEMOCAP数据集上，以下基线用于比较：
1. MDRE[11]采用双递归神经网络对音频和文本进行编码，然后使用完全连接的神经网络将两种模态的结果组合起来用于最终情绪分类。
2. MHA[16]基于MDRE，它另外利用新颖的多跳注意机制自动推断音频和文本之间的相关性。
3. Xu等人[17]提出使用注意机制来学习音频和文本之间的潜在对齐。
4. CAN[14]通过以正常和交叉的方式使用每种模态的注意权重来聚合来自对齐音频和文本的顺序信息。

在MELD数据集上，我们使用两个基线进行比较：
1. cMKL[25]采用CNN进行特征提取，并使用多核学习来融合多模态特征。
2. Liang 等人[22]采用两种深度自动编码器来学习音频和文本的潜在表示，并将它们连接起来进行分类。

### 引文

## 摘录
