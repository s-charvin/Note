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
data: 2022-04-17 19:03:29
lastmod: 2022-04-19 16:44:07
---

# 重点

- [开源代码](https://github.com/julianyulu/icassp2021-mscnn-spu)
- 引入多尺度卷积(MSCNN)，用不同大小的卷积核对某特征图进行卷积操作，得到新的大小不同的特征图，之后经过处理得到下一层的输入特征图。
- 提出了一个统计合并单元(SPU)，它由沿序列方向的三个平行的一维pooling组成：a)全局最大合并；b)全局平均合并；c)全局标准差合并。
- 使用Google的Speech-to-Text API获取文本识别结果输入进模型中，与输入语音实际文本的结果做对比。

思考：
- 不同卷积方式
	- 1×1 卷积（Bottleneck结构）
	- 3D卷积
	- 扩张卷积
	- 转置卷积（反卷积）
	- 分组卷积（混洗分组卷积，逐点分组卷积）
	- 可分离卷积（空间可分卷积，深度可分卷积）
	- 平展卷积
	- 微步卷积
	- 空洞卷积（膨胀卷积）
	- 可变形卷积
	- 图卷积

[A Comprehensive Introduction to Different Types of Convolutions in Deep Learning | by Kunlun Bai | Towards Data Science](https://towardsdatascience.com/a-comprehensive-introduction-to-different-types-of-convolutions-in-deep-learning-669281e58215)

[CNN中千奇百怪的卷积方式大汇总 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/29367273)

[变形卷积核、可分离卷积？卷积神经网络中十大拍案叫绝的操作。 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/28749411)

[一文看尽深度学习中的20种卷积（附源码整理和论文解读） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/381839221)

# 摘要

Emotion recognition from speech is a challenging task. Recent advances in deep learning have led bi-directional recurrent neural network (Bi-RNN) and attention mechanism as a standard method for speech emotion recognition, extracting and attending multi-modal features - audio and text, and then fusing them for downstream emotion classification tasks. In this paper, we propose a simple yet efficient neural network architecture to exploit both acoustic and lexical information from speech. The proposed framework using multi-scale convolutional layers (MSCNN) to obtain both audio and text hidden representations. Then, a statistical pooling unit (SPU) is used to further extract the features in each modality. Besides, an attention module can be built on top of the MSCNNSPU (audio) and MSCNN (text) to further improve the performance. Extensive experiments show that the proposed model outperforms previous state-of-the-art methods on IEMOCAP dataset with four emotion categories (i.e., angry, happy, sad and neutral) in both weighted accuracy (WA) and unweighted accuracy (UA), with an improvement of 5.0% and 5.2% respectively under the ASR setting.

语音情感识别是一项具有挑战性的任务。深度学习的最新进展使双向递归神经网络(bi-RNN)和注意机制成为语音情感识别的标准方法，提取并处理音频和文本的多模式特征，然后将它们融合用于下游情感分类任务。在本文中，我们提出了一种简单而高效的神经网络结构，以利用语音中的声学信息和词汇信息。该框架使用多尺度卷积层(MSCNN)来同时获得音频和文本的隐藏表示。然后，使用统计汇集单元(SPU)进一步提取每个通道的特征。此外，还可以在MSCNNSPU(音频)和MSCNN(文本)的基础上构建注意力模块，以进一步提高性能。大量实验表明，该模型在IEMOCAP数据集上的加权准确率(WA)和未加权准确率(UA)上均优于已有的方法，在ASR环境下分别提高了5.0%和5.2%。

# 结果

IEMOCAP

![]({16}_Efficient%20Speech%20Emotion%20Recognition%20Using%20Multi-Scale%20CNN%20and%20Attention.assets/image-20220418090457.png)

# 词汇记录

# 精读

本文首先提出了一种简单的卷积神经网络(CNN)和pooling-based模型，称为带有statistical pooling units的multi scale CNN(MSCNN-SPU)，该模型能够有效地同时学习语音和文本模式用于情感识别。此外，通过在MSCNN-SPU之上构建注意力模块，从而产生MSCNN-SPU-ATT，可以进一步提高整体性能。

![]({16}_Efficient%20Speech%20Emotion%20Recognition%20Using%20Multi-Scale%20CNN%20and%20Attention.assets/image-20220418092230.png)

使用一组具有不同kernel大小的filters来构建multiple CNN层，分别用于文本和音频这两个独立的路径。

具有ReLU激活的各种单层二维卷积[13]与文本和音频的输入特征并行应用。

设$\Omega^{A, T}=\left\{\left(s, d^{A, T}\right), s \in S^{A, T}\right\}$是音频通道(上标‘A’)和文本通道(上标‘T’)的kernel的集合，其中s是沿输入序列维度的kernel大小，dA和dT分别是mfcc和单词嵌入向量的维度。

$$

\begin{aligned}

&\mathrm{G}_{\alpha}^{\mathrm{MSCNN}}(\boldsymbol{x}, \theta)=\left\{y_{\alpha}^{A, T} \mid \alpha \in \Omega\right\}\\

&y_{\alpha=(s, d) \in \Omega}^{A, T}[i, j]=\sum_{m=\left\lfloor-\frac{s}{2}\right\rfloor}^{\left\lceil\frac{s}{2}\right\rceil} \sum_{n=\left\lfloor-\frac{d}{2}\right\rfloor}^{\left\lceil\frac{d}{2}\right\rceil} \boldsymbol{k}[m, n] \cdot \boldsymbol{x}[i-m, j-n]

\end{aligned}

$$

因此，我们提出了一个统计合并单元(SPU)，它由沿序列建模方向的三个平行的一维合并组成：a)全局最大合并；b)全局平均合并；c)全局标准差合并。

$$

\mathrm{E}=\left\{\mathrm{G}_{\gamma}^{\mathrm{SPU}}\left(\mathrm{G}_{\alpha}^{\mathrm{MSCNN}}(\boldsymbol{x})\right) \mid \alpha \in \Omega, \gamma \in\{\max , \text { avg, std }\}\right\}

$$

受[1，3]中注意机制概念的启发，我们提出了一种建立在Audio MSCNN-SPU和 Text-MSCNN 之上的双通道attention层。与以前的工作不同，我们将前者的输出视为上下文向量$\boldsymbol{e}_{\gamma}$(即来自音频分支的最大池、平均池、标准池特征向量)。根据来自max-pooling、avgpooling和std-pooling的输出，分别将加权系数$s_{k}^{\gamma}$计算自上下文向量$\boldsymbol{e}_{\gamma}$和来自文本MSCNN $\boldsymbol{h}_{k}$的第k个输出特征映射之间的乘积。由此得到的注意力向量S是通过用加权系数$s_{k}^{\gamma}$对$\boldsymbol{h}_{k}$加权得到的。

$$
\begin{gathered}

s_{k}^{\gamma}=\frac{\exp \left(\boldsymbol{e}_{\gamma}^{\mathrm{T}} \boldsymbol{h}_{k}\right)}{\sum_{k} \exp \left(\boldsymbol{e}_{\gamma}^{\mathrm{T}} \boldsymbol{h}_{k}\right)}, \text{ where } \gamma \in\{\text{max}, \text{avg}, \text{std} \}\\

\boldsymbol{S}^{\gamma}=\sum_{k} s_{k}^{\gamma} \boldsymbol{h}_{k} \\

\boldsymbol{S}=\operatorname{concat}\left(\boldsymbol{S}^{\mathrm{max}}, \boldsymbol{S}^{\mathrm{avg}}, \boldsymbol{S}^{\mathrm{std}}\right)

\end{gathered}

$$

此外，在说话人识别任务中，使用Kaldi语音识别工具包[18]，X向量嵌入[16]被用作从VoxCeleb数据集[17]上的预先训练的TDNN模型中提取的互补音频特征。

模型设置：
每个CNN层的filter数量被设置为128；在文本encoder中，SWEM-max和SWEMavg特征[14]是从单词嵌入中获得的，然后被附加到文本SPU的输出中；另一方面，将X-vector嵌入附加到audioSPU的输出中；Adam优化，学习率为0.0005；采用范数为1的梯度剪裁；dropout率为0.3；batch size为64。

其次，我们将我们提出的方法与其他多模式方法进行比较。一种直接的方法是为每种模态训练一个LSTM网络，然后从每个模式连接最后一个隐藏状态，如MDRE[1]所示。学习对齐[2]采用LSTM网络对音频和文本的序列进行建模。然后，使用模型中的注意力执行音频和文本之间的软对齐。在MHA[3]中，提出了一种所谓的多跳注意，使用一种模态的隐藏表示作为上下文向量并将注意方法应用于另一种模态，然后重复这种方案数次。

## 引文

- 近年来，基于深度学习的情感识别方法在情感识别中表现出了很好的性能[1，2，3]。
- [1]通过在文本和音频之间引入注意机制来融合学习特征。
- 在[2]中，注意力网络被用来学习语音和文本之间的对齐，而BiLSTM网络被用来对情感识别中的序列进行建模。
- 此外，文献[3]还提出了一种多跳关注法，选择文本数据的相关部分，然后关注音频特征，用于以后的分类目的。使用Audio-BRE(LSTM)。
- 研究人员已经证明了CNN在具有音频特征[7,8]和文本信息[9]的情绪分类中的有效性。
- 受[9]中使用的文本-CNN架构的激励
- 在[11]中，一种使用WordNet和词性标注的混合方法与标准音频特征相结合，然后使用支持向量机进行分类。
- 使用DNN，[12]从多分辨率CNN中提取文本特征，从BiLSTM中提取音频信息，并使用分类损失和验证损失的加权和来优化任务。
- 使用CNN进行情感识别任务的工作经常使用单层全局最大池或全局平均池，并在[7，8]中被证明是有效的。
- Swem向量，它是直接在学习的单词嵌入上连接各种池的结果[14]
- 使用300维GloVe[19]嵌入作为标记化记录的预训练单词嵌入。
- CNN+LSTM in [20]
- [21]中的TDNN+LSTM
