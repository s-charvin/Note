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
data: 2022-04-17 14:16:59
lastmod: 2022-06-06 20:01:37
---

# 重点

- 论文源文件
- 为了提升情感识别效果，使用 Contrastive Predictive Coding(CPC) 无监督学习方法，预先在无标签的大型语音数据库训练一个特征提取器，最终改善了小数据量问题。
- 遇见了两个新的损失函数：infoNCE 损失函数，源自于 CPC 无监督方法；concordance correlation coefficient(CCC), 基于一致性相关系数的损失函数,测量两个随机变量的对齐度（相关程度）。

# 摘要

Speech emotion recognition (SER) is a key technology to enable more natural human-machine communication. However, SER has long suffered from a lack of public large-scale labeled datasets. To circumvent this problem, we investigate how unsupervised representation learning on unlabeled datasets can benefit SER. We show that the contrastive predictive coding (CPC) method can learn salient representations from unlabeled datasets, which improves emotion recognition performance. In our experiments, this method achieved state-of-the-art concordance correlation coefficient (CCC) performance for all emotion primitives (activation, valence, and dominance) on IEMOCAP. Additionally, on the MSPPodcast dataset, our method obtained considerable performance improvements compared to baselines.

语音情绪识别（SER）是实现更自然的人机通信的关键技术。但是，SER长期以来一直缺乏公共的大规模标签数据集。为了避免这个问题，我们研究了未标记数据集上的无监督表示学习如何使SER受益。我们表明，对比预测编码（CPC）方法可以从未标记的数据集中学习显着表示，从而提高情绪识别性能。在我们的实验中，该方法在IEMOCAP上实现了所有情绪原语（激活，效价和优势）的最新一致性相关系数（CCC）性能。此外，在MSPPodcast数据集上，与基线相比，我们的方法获得了相当大的性能改进。

# 词汇记录

# 结果

使用系数

![]({11}_Contrastive%20Unsupervised%20Learning%20for%20Speech%20Emotion%20Recognition.assets/image-20220417162513.png)

IEMOCAP

![]({11}_Contrastive%20Unsupervised%20Learning%20for%20Speech%20Emotion%20Recognition.assets/image-20220417162339.png)

# 精读

无监督学习方法提出背景在于，虽然深度学习(dl)方法在多个领域能实现最先进的结果，但这些方法往往是需要大量数据支撑的。

维度情绪指标通常包括激活(又名激发，非常平静或非常活跃) ，效价(积极或消极水平)和支配(非常弱或非常强)。

**基于CPC的特征提取**

Contrastive predictive coding（对比预测编码），属于对比学习范畴，通过损失函数构建和分离正反例，具体实现步骤如下。

对于在上述设置中使用的 cpc 模型，我们使用一个带有步长[5,4,4,2] ，滤波器尺寸[10,8,8,4]和128个隐藏单元的带有关联激活的4层 cnn 来编码16khz 音频波形输入。

采用一个具有256个隐含维数的单向门控递归单元(gru)网络作为自回归模型。对于 gru 的每个输出，我们预测未来的12个时间步，使用50个负样本，从同一序列中取样，在每个预测中。

我们用10s固定长度的话语训练 cpc 模型。较长的话语在10s时被切断，较短的话语通过重复来填充。

在情感识别器中，使用了一个具有512维隐藏状态的8头注意层。注意层的输出与输入维数相同。两个完全相连的层有128个隐藏单元。退出的可能性被设置为0.2的辍学层。

我们的模型在 pytorch 上实现，所有的方法都在8个 gpu 上进行，每个 gpu 的小批量大小为8个样本进行 cpc 预训练。我们使用 adam 优化器，重量衰减0.00001，学习率0.0002。我们使用50个时代的训练和保存模型，执行最好的验证集测试。

为了评估 iemocap 数据集，我们配置了5个交叉验证来评估模型。所有的实验都进行了五次，得到了平均值和标准差。

1. 在 LibriSpeech dataset 预训练 CPC模型，使用非线性编码器 $f$ 将语音序列 $x_{t}$ 映射到隐式表征 $z_{t}$。
2. 使用自回归模型 $g$ 将过去时间上连续的隐层表征转化为上下文相关的特征 $c_{t}$，上下文相关意味着包含了过去的信息，亦即 $c_{t}$ 能够通过未来的观察值 $x_{t+k}$ 预测 $z_{t+k}$。$$\hat{z}_{t+k}=h_{k}\left(c_{t}\right)=h_{k}\left(g\left(z_{\leq t}\right)\right)$$
3. 从同一序列或其他序列中随机抽取样本（即其他观察值 $x$ ），计算其隐式表征 $z_{t}$，以形成对比问题。假设每个语境的 N个样本中，含有随机抽样的 N-1 个 negative 样本和一个positive 样本。
4. 利用 infoNCE 损失函数 $\mathcal{L}$( $\tau$ 是特征聚集程度的比例因子，$k$ 是预测时间上限，$i$ 为随机抽取的 negative 样本)，学习区分 negative 样本和 positive 样本，归结为一个 N 分类问题。$\mathcal{L}=-\sum_{m=1}^{k}\left[\log \frac{\exp \left(\hat{z}_{t+m}^{\top} z_{t+m}\right) / \tau}{\exp \left(\hat{z}_{t+m}^{\top} z_{t+m}\right) / \tau+\sum_{i=1}^{N-1} \exp \left(\hat{z}_{t+m}^{\top} z_{i}\right) / \tau}\right]$

显然，在不同的音频段和时间步骤中，损失是累加的，因此在训练中，损失通常是针对批量的音频段和这些段中所有可能的时间步骤计算的，以利用基于小批量的 adam 优化器。优化结果在隐层表征和其预测对应之间产生更大的内积，比任何 negative 样本匹配的隐层表征和预测。优化目标函数的理论证明可以在[11]和[18]中找到。

基于注意力机制的情感识别

由于话语的某些部分往往在情感上比其他部分更加突出，因此我们采用一种自我注意机制来关注这些时段，以利用相关特征，进行句子级别的嵌入。具体步骤：将CPC输出的 $C^{L*D_{c}}$ 作为输入，使用多头 dot-product 注意力机制，得到多方面考虑上下文信息权重的$H_{j}^{L × D_{attn}}$ 特征, 并经过简单的串联和线性变换得到$U^{L × D_{u}} = Conat(H^{1},H^{2},\cdot\cdot\cdot,H^{n}) W_{o}^{nD_{attn}×D_{u}}$作为序列特征。

沿着时间维度计算 $U$ 的平均值和标准差，并将它们连接成序列表示，然后经过两个全连接层（Relu+dropout）以及一个隐藏层单元为最终输出数量的全连接层，得到最终输出结果。

最终使用损失函数更新参数，其中$\rho = \frac{\sigma_{XY}}{\sigma_{X}\sigma_{Y}}$ 是皮尔森相关系数，用来反映两个变量X(模型预测)和Y(数据标签)的线性相关程度；$μ$ 和 $σ$是均值和标准差; 

$\mathcal{L}=1-\alpha \mathrm{CCC}_{a c t}-\beta \mathrm{CCC}_{v a l}-\gamma \mathrm{CCC}_{d o m}$

$\mathrm{CCC}(X, Y)=\rho \frac{2 \sigma_{X} \sigma_{Y}}{\sigma_{X}^{2}+\sigma_{Y}^{2}+\left(\mu_{X}-\mu_{Y}\right)^{2}}$

实验设置

1. 基线方法：使用MFCC40维特征的单独的受监督模型
2. 采用端到端的方式，从原始音频中训练 CPC 模型直接学习特征和情感识别器。加入基线方法，采用手工特征进行监控任务，以测试当特征提取部分知道下游任务时，是否有可能学到更好的特征。
3. minicpc 在相同的数据集上分两个阶段训练 cpc 模型和情感识别器。
4. 在 LibriSpeech dataset上预训练CPC，在 MSP-Podcast 和 IEMOCAP上训练含CPC的情感识别器。

## 引用

- 虽然利用非监督式学习对 ser 的研究相对较少，但之前使用自动编码器的尝试已经成功[12,13]。

- 最近，有研究表明，学习在一个时间序列中预测未来的信息是一种有用的训练前机制[14]。

- 例如，对比预测编码(cpc)[11]能够从顺序数据中提取有用的表示，并在各种任务中取得竞争性的表现，包括语音中的电话和说话人分类。

- 一般来说，有两种广泛使用的方法来表示情绪: 通过情绪类别(快乐、悲伤、愤怒等)或者通过维度情绪度量(又名情绪原语)[3,4,15]。

- 由于情绪表征是一个活跃的研究课题，我们建议感兴趣的读者参阅[15,16]。
