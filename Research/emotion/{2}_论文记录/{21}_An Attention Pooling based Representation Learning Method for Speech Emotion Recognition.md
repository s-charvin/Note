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
data: 2022-05-01 11:46:33
lastmod: 2022-05-07 19:33:40
---

# 重点

- 分析了时域和频域不同卷积核对应的不同感受域对语音情感识别的影响
- 新思想：将语音分成重叠片段增加数据量
- 新方法：使用u率压扩减少特征最大值与最小值之间的差距
- 引用了新的Pooling池化方法及其矩阵分解解释、注意力机制解释

# 摘要

This paper proposes an attention pooling based representation learning method for speech emotion recognition (SER). The emotional representation is learned in an end-to-end fashion by applying a deep convolutional neural network (CNN) directly to spectrograms extracted from speech utterances. Motivated by the success of GoogleNet, two groups of filters with different shapes are designed to capture both temporal and frequency domain context information from the input spectrogram. The learned features are concatenated and fed into the subsequent convolutional layers. To learn the final emotional representation, a novel attention pooling method is further proposed. Compared with the existing pooling methods, such as max-pooling and average-pooling, the proposed attention pooling can effectively incorporate class-agnostic bottom-up, and class-specific top-down, attention maps. We conduct extensive evaluations on benchmark IEMOCAP data to assess the effectiveness of the proposed representation. Results demonstrate a recognition performance of 71.8% weighted accuracy (WA) and 68% unweighted accuracy (UA) over four emotions, which outperforms the state-of-the-art method by about 3% absolute for WA and 4% for UA.

针对语音情感识别，提出了一种基于注意力池化的表征学习方法。首先通过将深度卷积神经网络(CNN)直接应用于语音，从中提取特征谱图，以端到端的方式学习情感表征。并且受GoogLeNet的启发，设计了两组不同形状的滤波器，从输入的语谱图中同时捕获时间域和频域的上下文信息，并将最后学习到的特征通过级联，馈送到随后的卷积层中。为了学习最终的情感表征，本文进一步提出了一种新的注意力池池化方法。与现有的最大池化和平均池化方法相比，所提出的注意力池化方法能够有效地融合 class-agnostic bottom-up,class-specific top-down, 和 attention maps方法。我们对基准IEMOCAP数据进行了广泛的评估，以评估模型提取的特征的有效性。实验结果表明，该方法对四种情感的识别率分别为71.8%和68%，比现有方法提高了约3%和4%。

> Top-down 方法确定特征对对象的贡献度。
> Bottom-up 方法是将对象每个区域的一些重要特征提取出来，构成特征向量。
> class-agnostic 不可知类方法
> class-specifi 可知类方法

# 结果

# 词汇记录

# 精读

简单的平均池化或最大池化可能不足以为需要分析更高阶统计量的复杂情感表达得出有效的表示。最近的一些工作显示了引入注意机制的表征学习的好处[12，13，10]。然而，它们通常以自下而上（bottomup）的方式从特征获得显著区域。为了解决这些问题，我们提出了一种基于注意力池的SER表征学习方法，如下图所示。CNN被直接应用于语音语谱图，其中设计了两组不同形状的卷积滤波器来分别捕获时间域和频域的上下文信息。在GoogLeNet[17]的启发下，学习的特征被进一步串联并馈送到后面的卷积层中。并且为了有效地进行表征学习，本文提出了一种新的注意力池方法。第一个注意图是以自下而上的方式得出的，而第二个注意图与情绪类型直接相关。

**数据处理**

数据扩充： 

CNN的输入是从语音中提取的语谱图。给定一个语音，将其分割成2s的片段进行训练，其中训练集的分割间隔1s，测试集的分割间隔0.4s。

数据归类：

每个片段被分配到原语音对应的标签，最后会通过平均每个片段的分数来获得语音最终预测。

**频谱处理**

对每个2s的语音片段，使用40ms的汉明窗，以10ms的帧移得到一系列的语音帧。然后对每个语音帧进行DFT变换（根据论文[11]结论，可知较高频率分辨率可以增强识别性能，因此选择参数NFFT=1600），得到每帧的频谱。将所有帧的频谱进行合并得到对应语音片段的频谱图（帧数x(NFFT/2+1)）。选择0到4 kHz的频率范围(去除了频率较高的一部分)，得到199x400的谱图，然后再经转置和padding（补零）可以得到最终的400×200的频谱矩阵。

频谱处理：

先将频谱矩阵中所有数据归一化到[-1, 1]，然后对其做一个μ为255的u率压扩。u率压扩通过增大数值较小的元素，人为的改变数据的分布，减少矩阵中最大值与最小值之间的差距，在信号处理领域认为可以改善信噪比率而不需要增添更多的数据。

$$

F(x)=\operatorname{sgn}(x) \frac{\ln (1+\mu|x|)}{\ln (1+\mu)},-1 \leq x \leq 1

$$
![]({21}_An%20Attention%20Pooling%20based%20Representation%20Learning%20Method%20for%20Speech%20Emotion%20Recognition@liAttentionPoolingBased2018.assets/image-20220501184932.png)

**论文模型**

论文的模型如下图，输入声谱图$(features × frames × 1）$，先通过有着不同的卷积核的两个CNN，分别提取时域特征和频域特征，concat后喂给后面的CNN，在最后一层使用attention pooling的技术。

标准的CNN结构可以通过多个卷积层对输入的声谱图进行处理，其中第k个卷积层计算输出特征图 $C_{o u t_{k}}$

$$

C_{o u t_{k}}=b_{i}+\sum_{i=1}^{C_{i n}} \omega\left(C_{o u t_{k}}, i\right) * i n p u t\left(C_{i n_{i}}\right)

$$
其中$b$是偏置，$ω$是卷积权重矩阵，$∗$是卷积运算。CNN每个卷积层的Filter，在各个通道对输入的特征图进行卷积，最终对每个通道求和得到输出特征图。

![]({21}_An%20Attention%20Pooling%20based%20Representation%20Learning%20Method%20for%20Speech%20Emotion%20Recognition@liAttentionPoolingBased2018.assets/image-20220501123211.png)

对于第一块的两个卷积层，可以通过改变卷积核的接受域，从原始语谱图中分别提取时频信息特征，并且分析感受野对系统识别性能的影响。如图所示，Conv1a中的Filter，频率轴上的卷积域设置为最小值2，然后时间轴上的卷积域可以自定义设置。Conv1b中的Filter，时间轴上的卷积域设置为最小值2，然后频率轴上的卷积域可以自定义设置。上述过程的目的是找出在限制时间/频率跨度的条件下，
在[17]中INSTIMATION模块的启发下，将得到的两种特征通过级联，作为后续的4个标准卷积层（3×3）的输入，然后最终通过2×2的最大Poolling提取时域和频域的高维特征信息。

通常，CNN使用几个全连接(FC)层来计算目标标签上的概率分布。然而，如果直接将卷积后的特征处理后送入FC层可能会导致过度参数化，这会使得训练变得困难，特别是对于小规模数据集。因此使用一个能够对特征图进行下采样，并保持高维特征表征能力的池化函数非常重要，本文中引入的是 [全局Attentional 池化](obsidian://open?vault=%E7%AC%94%E8%AE%B0&file=emotion%2F3.%E8%AE%BA%E6%96%87%E8%AE%B0%E5%BD%95%2F22.Attentional%20Pooling%20for%20Action%20Recognition)[19]。在实现上，我们在Conv5之后使用1×1卷积层来生成一个自上而下的注意图(大小为H×W×4，对应于4个情感标签)，并使用另一个1×1卷积层来生成自下而上的注意图(大小为H×W×1)。然后对自下而上的注意图应用Softmax操作。最后，将两种类型的注意图按元素相乘并进行空间平均，得到所有4种情绪类别的预测分数。

采用前人工作[10，11，23，24]的方法，采用留一策略（leave-oneout）进行10倍交叉验证。在每个训练过程中，使用9个说话人作为训练数据，剩下的一个用于测试数据。对于CNN的培训，我们使用了PyTorch[25]深度学习框架。优化方法是标准随机梯度下降法(SGD)，小批量为64。我们使用的Nesterov momentum为0.9，权重衰减率为0.0001。CNN经过50多个epoch的训练。初始学习率为0.05，在第21、31和41个epoch减少10倍。我们在每一卷积层之后采用batch normalization[26]层，所用的激活函数是校正线性单元(REU)。优化目标函数采用交叉熵(CE)准则。

**filter大小对系统的影响**

更改频率维度
![]({21}_An%20Attention%20Pooling%20based%20Representation%20Learning%20Method%20for%20Speech%20Emotion%20Recognition@liAttentionPoolingBased2018.assets/image-20220503115559.png)

随着高度(频率)的增加，Wa和中性类的精度也增加。然而，这一趋势在大约10(100赫兹)的高度趋于平缓，超过这一高度后，感受场频率范围的进一步增加不会带来显着改善。

**更改时间维度**

![]({21}_An%20Attention%20Pooling%20based%20Representation%20Learning%20Method%20for%20Speech%20Emotion%20Recognition@liAttentionPoolingBased2018.assets/image-20220503115616.png)

当增加宽度(时间)时，Wa在8(80ms)左右的宽度处先增加到一个峰值，然后逐渐减小。有趣的是，当接受域的时间跨度变大时，愤怒类的准确率迅速下降，这表明愤怒情绪是通过短时间表征来表达的。

在这些实验中，Happy类的准确率最低，与filter形状无关。这可能表明，happy需要从更高级别的表征中学习。

根据上文所述，本文filter的大小选用了10×2和2×8。

## 引文

- 斯兰尼等人。应用具有Mel频率倒谱系数的高斯混合模型(GMM)进行SER[1]。
- 在文献[2，3]中，提取韵律特征来训练支持向量机分类器。
- 在[6，7]中，采用了多阶段的方法，训练DNN和CNN网络进行前端特征提取，然后使用后端情感识别器，如支持向量机和极限学习机(ELM)。
- Trigorgis et.。Al[9]将原始音频送入CNN进行前端特征提取，然后使用长短期记忆(LSTM)层进行情绪表征学习。模型参数可与反向传播算法联合优化。
- 在[8，10]中，随着时间的推移应用最大合并运算以从显著区域获得话语表示。
- 诺伊曼·艾尔。Al[12]在最大池化操作后进一步引入了注意机制。
- 而Mirsamadi et.。Al[13]将加权池化应用于RNN输出。
- 在[14，15]中，人们提出了2D时频LSTM和Grid-LSTM来建模大规模自动语音识别(ASR)中随时间和频率的变化。然而，复杂的模型体系结构容易在诸如IEMOCAP[16]这样的小规模数据集上过度拟合。
