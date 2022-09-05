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
data: 2022-06-02 14:56:41
lastmod: 2022-06-05 18:15:21
---

# 重点

- [开源代码](https://github.com/smartcameras/SelfCrossAttn)
- 讨论了注意力机制对不同模态间特征融合的影响
- 通过将两个不同模态的输入分别分配给注意力机制的Q和KV，实现多模态运算之间的数据交互。
- 结论：多模态特征融合过程中，使用自注意力机制和使用跨模态交互注意力机制都有用，但是效果类似。

# 摘要

Humans express their emotions via facial expressions, voice intonation and word choices. To infer the nature of the underlying emotion, recognition models may use a single modality, such as vision, audio, and text, or a combination of modalities. Generally, models that fuse complementary information from multiple modalities outperform their uni-modal counterparts. However, a successful model that fuses modalities requires components that can effectively aggregate task-relevant information from each modality. As crossmodal attention is seen as an effective mechanism for multi-modal fusion, in this paper we quantify the gain that such a mechanism brings compared to the corresponding self-attention mechanism. To this end, we implement and compare a cross-attention and a selfattention model. In addition to attention, each model uses convolutional layers for local feature extraction and recurrent layers for global sequential modelling. We compare the models using different modality combinations for a 7-class emotion classification task using the IEMOCAP dataset. Experimental results indicate that albeit both models improve upon the state-of-the-art in terms of weighted and unweighted accuracy for tri- and bi-modal configurations, their performance is generally statistically comparable.

人类通过面部表情、语调和用词来表达自己的情感。为了推断潜在情绪的性质，识别模型可以使用单个通道，例如视觉、音频和文本，或通道的组合。一般来说，融合来自多个通道的互补信息的模型表现优于单通道对应的模型。然而，融合通道的成功模型需要能够有效地聚合来自每个通道的与任务相关的信息的组件。由于跨通道注意被认为是一种有效的多通道融合机制，本文量化了这种机制与相应的自我注意机制相比所带来的收益。为此，我们实施并比较了交叉注意模型和自我注意模型。除了注意力外，每个模型都使用卷积层来进行局部特征提取，并使用递归层来进行全局顺序建模。我们使用IEMOCAP数据集对7类情绪分类任务中使用不同通道组合的模型进行了比较。实验结果表明，尽管这两个模型在加权和未加权精度方面都优于最先进的三模和双模配置，但它们的性能通常在统计上是可比较的。

# 结果

在本节中，我们将讨论使用交叉自我注意模型进行7类双模态和三模态情绪识别的数据集和结果。

我们还讨论了与两种模型的最新方法和具有附加模型配置的实验的比较。

## 数据集设置

交互式情绪二元运动捕捉（IEMOCAP）[18]数据集，有些人通过合并不同的类（快乐和兴奋，愤怒和沮丧）将其用于4级分类[13]，而其他人[3,7,19,16]则进行7级分类。我们跟随后者，使用与[3,7,19]相同的数据集分区和功能。最终的数据集总共包含7487个话语（1103个愤怒，1041个兴奋，595个快乐，1084个悲伤，1849个沮丧，107个惊喜和1708个中立）。类规模小于100个话语的（恐惧，厌恶，其他）被消除[3]。

## 训练设置

5折交叉验证来评估模型性能。每折中的数据分为训练，开发和测试集（8:0.5:1.5）。每折叠训练和评估模型10次（具有10个不同的随机种子），并且根据加权准确度（WA）和未加权准确度（UWA）度量来评估性能。

对于音频模态，提取40维 MFCC特征（帧大小为25ms，帧移速率为10ms，窗类型为汉明窗）及其其一阶和二阶导数连接以获得120维的最终声学特征维度。通过减去均值，缩放到单位方差，来标准化音频特征。

对于视觉模态，裁剪后的说话人面部图像被馈送到ResNet101[20]中，以3Hz的帧移获得2048维的特征。

对于文本模态，话语中的每个单词都由300维的GloVe[10]嵌入表征。

请注意，模态以不同的速率采样，音频，视觉和文本模态的最大序列长度分别设置为1000,32和128。这些模型是使用PyTorch实现的[21]。



三模态模型的双模态和单模态版本是通过删除与未使用的模态/模态相对应的组件来创建的。


我们使用Adam[22]Optimizer，学习率为0.001。当验证损失连续10个时期停止减少时，学习率降低0.1倍。批量大小为32，所有模型都使用分类交叉熵损失进行训练。音频和视觉编码器每个都包含一个1D卷积层。内核大小和步长都设置为1。音频卷积层的输入和输出通道数分别为1000和500，而视觉则分别为32和25。所有3种模式的bi-GRU层数为1。每个bi-GRU层中隐藏的神经元数量为60个。所有MHA模块中的注意头数量为6，并且应用0.1的辍学率以减少过度拟合。第一和第二完全连接的输出层中的神经元数量分别为60（与bi-GRU神经元的数量相同）和7（输出类的数量）。

当UWA在连续10个时期的验证集中没有改善时停止训练，并且使用具有最佳验证UWA的模型进行测试。

所有参数都是根据验证集的性能选择的。表1显示了自我和交叉注意模型在7类单模态，双模态和三模态情绪识别任务中的表现。我们报告了每个模型在50次运行中获得的平均值和标准偏差（5折×10次重复）。我们还应用了具有零假设的two-tailed t-test，即自我和交叉注意模型的准确度值具有相同的平均（预期）值。单模态性能的比较表明，文本优于视觉和音频模式。这个结果与以前的工作一致[13,19]。由于使用跨模态模型无法进行单模态性能评估，因此我们使用单模态版本的自我关注模型报告结果。在双模态模型中，视觉和文本模态的组合为两种模型提供了最佳性能。这些结果与以前的工作一致[7,19]。总体而言，这两种模型都为双模态和三模态情况提供了可比的性能。仅对于T+A（文本和音频）和T+V+A（文本，视频和音频）的WA，自我注意显着优于交叉注意（P值<.05）。

## 基线模型比较

将三模态模型与AMH[3]进行比较，AMH[3]是当前最先进的模型，它使用单模态GRU层和迭代注意机制的组合1。请注意，就WA和UWA而言，自我关注模型分别超过AMH的表现4.0和2.5个百分点（pp）。交叉注意模型的类似数字是3.1 pp和1.9 pp。

我们还与MDRE[19]进行了比较，MDRE[19]使用递归层对单模态信号进行建模，然后使用完全连接的层进行聚合和分类。与MDRE相比，自我和交叉注意模型以及AMH的更好表现可归因于注意机制的有效性。

对于双模态模型，我们与称为MHA[7]和MDRE的AMH双模态版本进行比较。同样，这两种型号在所有3种双模态情况下都优于MHA和MDRE。请注意，我们通过消除三模态模型而不是针对单个双模态情况进行微调来获得双模态结果。此外，AMH，MHA和MDRE除了MFCC特征外还使用韵律特征进行音频处理，而我们仅使用MFCC特征。通过[16]（0.560 WA和0.612 UWA）获得文本+音频案例的最新结果，该结果显着高于双模态T+A（文本和音频）结果。我们假设有两个原因：（1）与[16]不同，双模态模型没有针对双模态情况进行微调；（2） [16]使用包含其他参数的变压器编码器，这些参数可能有助于学习更复杂的模态间关系，而我们仅使用多头注意机制。尽管如此，这两种模型都改善了AMH的最新三模式结果。图3显示了自我和交叉注意模型的混淆矩阵。对于这两种模式，我们可以观察到，愤怒和沮丧的类经常彼此混淆，类快乐与兴奋混淆（这两个类本质上是相似的）。两种模型在训练中的表现都很差，这可以归因于它在数据集中具有最小的样本量。这些观察结果与以前的文献一致[3]。除了两种描述的模型配置外，我们还尝试了三模态模型的不同变化。我们从两个模型中删除了统计池层以评估其重要性。来自所有时间平均模块（参见图1和2）的输出被连接并传递给分类器模块。这些模型在表2中显示为Cross-noSP和Self-noSP。我们可以做两个观察。首先，即使在消除统计池之后，自我注意模型也优于交叉注意模型（WA的P值<.05）。其次，如果没有统计池层，两个模型的性能都会下降。我们还评估了通过合并自我和交叉关注模型（cross+self）创建的组合模型的性能。将来自两个模型的统计池输出连接并馈送到公共分类器模块。我们可以看到，表现类似于自我关注模型。这可能表明，与自我关注模型相比，交叉关注模型不会提供任何额外的相关信息。

被交叉注意机制在多通道融合中的流行所吸引，我们使用IEMOCAP数据集对基于自我注意和交叉注意的模型进行了三通道和双通道七类分类的比较。结果表明，两种模型的结果没有显著差异。因此，在我们使用的数据集和体系结构的背景下，我们得出结论，在多通道情绪识别中，交叉注意并不优于自我注意。此外，自我注意模型和交叉注意模型都提高了识别任务的最新水平。未来的工作包括研究交叉注意和自我注意模型对其他多通道任务和通道的有效性。致谢。我们感谢[3，7，19]的作者提供了经过处理和分区的IEMOCAP数据集。我们承认使用了ESPRC资助的Tier 2设施Jade。

![]({27}_Is%20Cross-Attention%20Preferable%20to%20Self-Attention%20for%20Multi-Modal%20Emotion%20Recognition.assets/image-20220602164542.png)

![]({27}_Is%20Cross-Attention%20Preferable%20to%20Self-Attention%20for%20Multi-Modal%20Emotion%20Recognition.assets/image-20220602164602.png)

# 词汇记录

# 精读

情绪识别(Emotion recognition, ER)模型使用一种或多种模式，如音频(语言和副语言)、图像(面部表情和肢体姿势)和文本(语言)来推断潜在的情感类别[1]。多模式模型被设计为有效地融合来自不同模式的相关信息，并且通常优于单模式模型[2，3]。

ER模型可以使用原始信号(语音或面部图像)[4、5、6]或手工制作的特征[3、7]作为输入。

- 常用的语音特征是低级描述符，例如共振峰、基音、对数能量、过零率和梅尔倒谱系数(MFCC)[3，7]。
- 面部表情可以由基于始终存在于面部的实体(如眼睛、嘴巴和眉毛)的固定特征和/或基于临时实体(如皱纹和凸起)的临时特征来表示[8]。
- 可以使用单词嵌入算法(如word2vec[9]或Glove[10])将标记化的单词映射为语言特征。


基于深度神经网络(DNN)的ER模型可以包含卷积层，以从输入层和递归层提取局部任务相关分量，从而促进全局序贯建模[4，5]。DNN体系结构中集成的注意机制[11]鼓励ER模型关注与任务相关的时刻[3，6]。注意机制的一般目的是为序列中的不同时间步长提供不同水平的权重。注意机制有两种，即自我(或通道内)注意和跨(或通道间)注意。自我注意机制通过关联相同序列的不同位置来计算单模态序列的表示[6，12]。跨通道注意机制使用一种通道来估计每个位置在另一通道中的相关性[13]。例如，可以使用2个递归层之间的自我注意机制来强调输入语音信号中的任务相关时间步骤[6]，而迭代多跳交叉注意机制可以从利用门控递归单元(GRU)层获得的多模式特征中选择和聚集信息[3，7]。包含多头注意(MHA)模块的Transformers[14]在建模单模和多模情感数据[15，13，16，17]中也变得流行起来。跨模式转换器使用交叉注意来计算使用不同源模式的目标模式表征中的每个时间步长的相关性[13，17]。交叉和自我注意变压器的串联[13，17]或并行[16]组合旨在捕获用于多模式融合的跨模式和模式内关系。


考虑到对基于自我注意和交叉注意的变压器编码者结合模型的兴趣[13，16，17]，我们进行了第一个研究，比较了两种类型的注意机制(不包括其他变压器组件)。为了了解两种类型的注意机制之间的差异，我们广泛地比较了一个只基于交叉注意的模型和一个只基于自我注意的双模式和三模式组合的模型。我们在IEMOCAP[18]的7类情绪分类数据集上对这两种模型进行了比较，结果表明，交叉注意模型并不优于自我注意模型。然而，这两个模型都在加权和未加权准确度方面改善了三通道和双通道情绪识别任务的最新结果。

自我注意和交叉注意模型首先使用特定于模态的编码器处理单个模态的数据。然后，经过编码后的特征分别被馈送到多头自注意力模块或多头交叉注意力模块(Multi-Head Attention, MHA)[14]中。在每个注意力模块的输出端生成话语片段的全局表征作为时间平均值。然后，将得到的特征连接起来，并使用统计汇聚层获得它们的平均值和标准差。然后，将串联的平均和标准偏差向量馈送到全连接层。最终的情感类预测通过Softmax运算获得。具体说明如下：

![]({27}_Is%20Cross-Attention%20Preferable%20to%20Self-Attention%20for%20Multi-Modal%20Emotion%20Recognition.assets/image-20220602181045.png)

1. 设$X_{a} \in \mathbb{R}^{t_{a}}\times d_{a}$是对应于一个音频片段的音频特征，其中$t_{a}$是序列长度，$d_{a}$是特征维度。音频编码器由一个$1 \mathbb{D}$卷积层和一个双向GRU组成。

- 卷积层通过查找与任务相关的特征来优化输入要素序列，其操作如下：$$X_{a}^{\prime}\left(t^{\prime}\right)=b\left(t^{\prime}\right)+\sum_{k=0}^{t_{a}-1}\left(W\left(t^{\prime}，K\right)*X_{a}(K)\right)$$其中$X_{a}^{\prime}\in\mathbb{R}^{t_{a}^{\prime}\times d_{a}^{\prime}}$是长度为$t_{a}^{\prime}$的输出，维度为$d_{a}^{\prime}$的输出，$t^{\prime}\in\left[0, t_{a}^{\prime}-1\right]$，\*是卷积运算符，$W$是权重，$b$是与层关联的偏差。因此，卷积层修改序列长度以及特征尺寸。

- 双向GRU层模拟特征随时间变化的上下文相互依赖关系。对于序列中的每个元素，Bi-GRU层计算以下函数：
$$ \left\{\begin{array}{l} r_{t}=\sigma\left(W_{i r} X_{a}^{\prime}(t)+b_{i r}+W_{h r} h_{t-1}+b_{h r}\right) \\ z_{t}=\sigma\left(W_{i z} X_{a}^{\prime}(t)+b_{i z}+W_{h z} h_{t-1}+b_{h z}\right) \\ n_{t}=\phi_{h}\left(W_{i n} X_{a}^{\prime}(t)+b_{i n}+r_{t} \odot\left(W_{h n} h_{t-1}+b_{h n}\right)\right) \\ h_{t}=\left(1-z_{t}\right) \odot n_{t}+z_{t} \odot\left(h_{t-1}\right) \end{array}\right.
$$
其中$h_{t}$和$h_{t-1}$是时间$t$和$t-1$的隐藏状态向量，$X_{a}^{\prime}(T)$是时间$t$的输入。$R_{t}、z_{t}$和$n_{t}$是重置门、更新门和新门，$W$和$b$是相应的权重和偏差，$\sigma$和$\Phi_{h}$是Sigmoid和双曲正切函数，$\odot$是Hadamard乘积。在bi-GRU的输出端，每个时间步长的前向和后向隐藏状态被串联，并且改进的音频特征可以表示为$e_{a}\in\mathbb{R}^{t_{a}^{\prime}\times d^{\prime\prime}}$，其中$d^{\prime\prime}$是GRU中隐藏神经元数目的两倍。

2. 与音频类似，视觉编码器由一个$1\mathbb{D}$卷积层和一个双GRU层组成。如果$X_{v}\in\mathbb{R}^{t_{v}\times d_{v}}$表示与话语对应的视觉特征，则在视觉编码器的输出处，这些特征被细化为$e_{v}\in\mathbb{R}^{t_{v}^{\prime}\times d^{\prime\prime}}$。

3. 对于文本通道，编码器仅由一个bi-GRU层组成。文本编码器的输入和输出可以分别用$X_{l}\in\mathbb{R}^{t_{l}\times d_{l}}$和$e_{l}\in\mathbb{R}^{t_{l}\times d^{\prime\prime}}$表示。

- 我们使用多头注意力模块[14]进行自我和交叉注意力建模。

多头注意力模块由多个注意操作组成，以捕获对序列的更丰富的解释。每个多头注意力模块需要3个输入，即查询$(Q)$、Кey$(K)$和值$(V)$，每个输入首先使用线性映射层, 投影到$H$个不同的子空间，即令多头注意力模块的Head数目为$H$。每个子空间的投影特征$h \in\{0, \ldots, H-1\}$ ，可计算为

$$
\begin{aligned}

Q_{h} &=W_{h}^{Q} e_{m} \\

K_{h} &=W_{h}^{K} e_{m} \\

V_{h} &=W_{h}^{V} e_{m}

\end{aligned}
$$

其中，$m \in\{a, v, l\}$表示哪种模态。在这些子空间中，通过scaled dot-product attention方法对映射特征进行运算。对子空间$h$，运算过程如下所示

$$
\operatorname{Att}_{h}\left(Q_{h}, K_{h}, V_{h}\right)=\operatorname{Softmax}\left(\frac{Q_{h} K_{h}^{T}}{\sqrt{d_{k}}}\right) V_{h}
$$


其中$A t t_{h}(\cdot)$和$d_{k}$分别指子空间$h$中的中的注意力运算和特征维度。多头注意模块的所有$H$个输出，被串联并通过线性映射层以获得多头注意模块的最终输出。

在交叉注意模型中，源模态使用源自身的输入数据通过线性映射，得到$K$和$V$向量矩阵，然后使用其他模态的数据，再得到$Q$向量矩阵(见图1)。这种方法背后的直觉是通过使源模态适应目标模态来实现跨模态交互[13]。

将音频作为目标通道，而视觉作为源通道举例：

![]({27}_Is%20Cross-Attention%20Preferable%20to%20Self-Attention%20for%20Multi-Modal%20Emotion%20Recognition.assets/image-20220602200508.png)

将精炼的音频特征($e_{a}\in\mathbb{R}^{t_{a}^{\prime}\times d^{\prime\prime}}$)通过线性映射转换为$Q$，然后再将精炼的视频特征($e_{v}\in\mathbb{R}^{t_{v}^{\prime}\times d^{\prime\prime}}$)通过线性映射转换为$K$和$V$。跨模态的多头注意力模块会将视频映射到音频模态，并输出与音频相适应的视觉特征$e_{a v}^{w}\in\mathbb{R}^{t_{a}^{\prime}\times d^{\prime\prime}}$。注意，交叉注意加权输出的序列长度与目标通道音频相同。

对于3个模态，总共有6个源-目标模态的组合，因此我们使用了6个MHA模块。

- 而在自我注意模型的情况下，同一模态的输入序列才会被用作计算$Q、K$和$V$(见图2)，这有助于捕获每个模态中的模态内交互特征。

统计池化方法statistical pooling，在交叉注意模型中，是跨6个模态组合序列的时间平均的级联计算的，而对于自我注意模型，是跨所有3个模态的自注意序列的时间平均的级联计算的。
这两种模型的分类器都是：
$$
\hat{y}=\operatorname{Softmax}\left(f_{\theta_{2}}\left(f_{\theta_{1}}([\mu \| \sigma])\right)\right)
$$
其中，$\mu$和$\sigma$是统计汇聚层输出的均值和标准差，$||$表示串联操作，$f_{\theta_{1}}$和$f_{\theta_{2}}$分别表示参数为$\theta_{1}$和$\theta_{2}$的两个全连接层，$\hat{y}$表示情绪预测的onehot向量。

## 引文
