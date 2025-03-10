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
data: 2022-06-02 14:56:50
lastmod: 2022-06-04 18:08:14
---

# 重点

- [开源代码](https://github.com/tobefans/LSSED)
- 提出了一个具有挑战性的大规模英语语音情感识别数据库LSSED
- 上游预训练的数据如果含有更多的信息，会使得下游任务更好训练，得到良好的泛化能力。
- 如果使用较宽的窗口大小，则每帧的频率信息更丰富，频率分辨率更高，并且较高的频率分辨率有利于提取声学特征

# 摘要

Speech emotion recognition is a vital contributor to the next generation of human-computer interaction (HCI). However, current existing small-scale databases have limited the development of related research. In this paper, we present LSSED, a challenging large-scale english speech emotion dataset, which has data collected from 820 subjects to simulate realworld distribution. In addition, we release some pre-trained models based on LSSED, which can not only promote the development of speech emotion recognition, but can also be transferred to related downstream tasks such as mental health analysis where data is extremely difficult to collect. Finally, our experiments show the necessity of large-scale datasets and the effectiveness of pre-trained models.

语音情感识别是下一代人机交互的重要组成部分。然而，现有的小型数据库限制了相关研究的发展。在本文中，我们提出了一个具有挑战性的大规模英语语音情感数据集LSSED，它收集了820名受试者的数据来模拟真实世界的分布。此外，我们发布了一些基于LSSED的预训练模型，这些模型不仅可以促进语音情感识别的发展，还可以移植到数据收集极其困难的相关下游任务，如心理健康分析。最后，我们的实验证明了大规模数据集的必要性和预训练模型的有效性。

# 结果

# 词汇记录

# 精读

语音情感识别是人机交互系统的重要组成部分。虽然情感本身非常抽象，但它仍然具有一些明显的语调特征。直觉上，悲伤的声音通常低沉而缓慢，而快乐的声音通常相反。到目前为止，已经出现了许多针对现有数据集的算法。人们对SER进行了大量的研究。在文献[1]中，Schuller et al.。应用连续隐马尔可夫模型(HMM)对自收集的语音语料库进行SER。自2004年以来，一些标准化的语音情感数据库相继发布。AiBO[2]、EMODB[3]、ENTERFACE[4]、RML[5]、IEMOCAP[6]、AFEW[7]和MELD[8]。其中，IEMOCAP[6]和MELD[8]是数据最多的数据库。IEMOCAP[6]收集了10个人的7433个句子(总共13小时40分钟)。MELD[8]包含来自407人的13,708个句子(约12小时)。在[9]中，使用决策树来缓解AIBO[2]和IEMOCAP[6]上的错误传播。在[10]中，将RBM应用于学习EMODB[3]和ENTERFACE[4]上的区分特征。随着深度学习的快速发展，张等人提出了自己的观点。[11]利用DCNN在EMODB[3]、RML[5]、ENTERFACE[4]上弥合语音信号中的情感间隙。同时，萨特等人也提出了自己的观点。[12]介绍了一种基于端到端LSTM-CNN的系统，该系统具有IEMOCAP[6]上的原始光谱图。最近，Yeh et al.。[13]提出了一种对话式情感解码算法，对IEMOCAP[6]和MELD[8]上的每个话语的情感状态进行连续解码。

虽然SER已经取得了一定程度的进展，但仍然存在潜在的严重的过适应问题，这可能会限制SER的发展。如[1417]所示，即使在某个数据库上实现了很高的精度，但在转移到另一个数据库时，它们的性能可能会很差。这是因为现有的数据库普遍规模较小，导致多样性不足，与现实场景相去甚远，从而导致模型过度拟合的趋势。因此，迫切需要一个能够更全面地反映真实分布的大规模情感数据集来提高现有算法的泛化能力。一般来说，迁移学习可以在一定程度上提高算法的性能。Boigne et al.。[18]指出了在小数据集上识别情绪的任务相关迁移学习。对于与情感识别相关的任务，由于数据收集非常困难，一个好的预训练模型是当务之急。以抑郁症检测任务为例，到目前为止，最多只有100个左右的受试者。我们认为，SER任务中的预训练模型更适合于抑郁症的检测，因为它更倾向于提取声学特征，而ASR任务中的模型更容易提取语言特征。

在本文中，我们提出了一个具有挑战性的大规模英语语音情感识别数据集LSSED。它收录了820人的147,025个句子(总计206小时25分钟)。基于我们的数据集，我们可以模拟更全面、更丰富的真实世界场景的数据分布，以便深度神经网络可以更好地模拟它们的分布。此外，由于目前还没有大规模的非语义预训练模型，我们发布了一些具有语音情感识别任务的预训练模型。


2.1. 收集和标记

参与实验的受试者广泛分布，具有来自不同性别和年龄组的表示。每个受试者将在室内实验室环境中以一个或多个情感视频录制，相机指向他或她。在视频中，主题是由随机问题引起的，因为他们的话语与情感标签相关联。视频的总长度约为10-20分钟。每个视频对话中的话语都由专业的注释团队进行注释。每个话语都附有相应的情绪标签，包括愤怒，快乐，悲伤，失望，无聊，厌恶，兴奋，恐惧，惊讶，正常等。请注意，视频中的某些话语包含两种或多种情绪。此外，每个话语还附有辅助信息，包括受试者的性别和年龄。


2.2. 数据分布

如上所述，我们的数据库涵盖了各种人群。表2显示了年龄和性别的条件分布和联合分布。在LSSED中，性别分布相对均衡。然而，在年龄分布上，老年人较少。

![]({34}_LSSED_%20A%20Large-Scale%20Dataset%20and%20Benchmark%20for%20Speech%20Emotion%20Recognition@fanLSSEDLargeScaleDataset2021.assets/image-20220604175651.png)

情绪标签的数据分布如图1所示。由于受试者是在自发环境中发言，所以较常见的中性样本占较大比例。接下来分别是快乐、悲伤、失望、兴奋和愤怒的样本。这六大类样本占总样本的81%。其次，无聊、恶心、恐惧、惊讶的样本较少，仅占6%。此外，13%的其他不常见样本可以用于任务，以区分它们是否为常见情绪。为了标准化未来的训练基准，我们将LSSED数据集分为训练集和测试集。具体来说，我们首先对所有样本进行排序，然后将20%的样本设置为测试集，其余的作为训练集。应该注意的是，我们确保每个情感类别在训练集和测试集中的分布相同或至少相似。

![]({34}_LSSED_%20A%20Large-Scale%20Dataset%20and%20Benchmark%20for%20Speech%20Emotion%20Recognition@fanLSSEDLargeScaleDataset2021.assets/image-20220604175804.png)

表3显示了情感标签在训练集和测试集中的具体数据分布。

![]({34}_LSSED_%20A%20Large-Scale%20Dataset%20and%20Benchmark%20for%20Speech%20Emotion%20Recognition@fanLSSEDLargeScaleDataset2021.assets/image-20220604175915.png)

2.3. 预处理和特征提取

在获得视频后，我们将其转换为16 kHz的采样率的音频信号。根据每个话语的开始时间和结束时间，我们剔除了147,025个音频话语。对于每个句子，我们使用谱减法[19]来进行音频去噪。它减去短时频谱上的噪声，然后恢复音频。接下来，在获得视频后，我们将其转换为16 kHz的采样率的音频信号。根据每个话语的开始时间和结束时间，我们剔除了147,025个音频话语。对于每个句子，我们使用谱减法[19]来进行音频去噪。它减去短时频谱上的噪声，然后恢复音频。接下来，我们将音量增加2倍，以使声音更响亮。经过预处理后，采用1024点的Hann窗长和512点的窗位移量进行短时傅立叶变换。随后进行平方运算以获得功率谱。然后，功率谱通过具有128-尺度的三角形滤波器组来模拟人类的听觉感知系统。

我们首先选择VGG[20]和ResNet[21]进行预训练，这两种方法在许多场景中都很有用。VGG建立了一个统一而简单的结构来深化网络，而ResNet则提出了剩余学习来简化训练过程。为了更好地适应语音的特殊性，我们提出了一种改进的ResNet模型--PyResNet[21]。由于数据量足够大，所以PyResNet是基于ResNet50、ResNet101或ResNet152的。具体地，将ResNet每层中的第二卷积层替换为能够捕捉多尺度信息的金字塔卷积[22]，以解决有效语音信息的时间位置不确定的问题。此外，为了使模型对时间不敏感，同时也保留了频率信息，仅在时间维度上用平均汇聚层代替了空隙层。

虽然目前的算法在许多小规模的数据集上都取得了很好的效果，但预先训练好的模型往往不能很好地推广到其他数据集。这引发了我们对数据库规模的思考，导致收集和建立了大量的数据库，这些数据库可以提供足够的信息来训练一个具有良好泛化能力的模型。

为了验证不同尺度数据集的有效性，我们基于ResNet152计算了性能降级，如表4所示。我们选择的度量标准是加权准确率(Wa，总体分类准确率)和未加权准确率(UA，每类平均准确率)。结果表明，从小规模IEMOCAP[6]训练的模型在大规模LSSED上测试时，性能下降很大，而从大规模到小规模测试时，性能下降较小。这证明了LSSED的有效性，因为它模拟了真实世界的分布。

3.2. 语音情感识别基准

在实验中，所有算法都使用了来自LSSED的训练集和测试集。我们的模型通过sgd优化器迭代了60个时期，批处理大小为256，权重衰减率为0.001。学习率(初始为0.01)每20个历元下降到原来的10%。与当前主流的SER实验相一致，我们使用了四种情绪类别，包括愤怒、中性、快乐和悲伤。结果如表5所示。这表明现有算法在大规模LSSED上的性能并不令人满意。更重要的是，这些算法的精度(加权和未加权)甚至低于基本的VGG和ResNet模型。此外，值得注意的是，我们的PyResNet取得了比基本主干模型更好的结果。这说明基于金字塔卷积的改进在大规模数据库上是有效的。由于这些算法在大规模数据库上的整体性能不是很好，应该指出LSSED仍然有很大的挑战，这意味着语音情感识别距离完美的广泛应用还有很长的路要走。使用ResNet152作为主干的MTS-3分支和PyResNet的混淆矩阵如下所示。虽然它们都使用多尺度卷积核，但前者使用源自一个核的多尺度核，而后者直接使用多个不同的核，具有更强大的建模能力。如图2所示，我们可以观察到，中性样本被正确预测的概率很高，这也是最常见的情绪。但我们也应该注意到，这两个模型都存在对中性类别的预测偏差问题。我们推测，这是因为每个人都有不同的中立标准。在我们今后的工作中，我们还将考虑每个人的休息(中立)状态。相比之下，我们的PyResNet在更难预测的愤怒、快乐和悲伤类别上有显著的改进。

通过以上预先训练的模型，我们希望进一步探索其对下游任务的适用性。我们选择基于语音的抑郁检测作为我们的下游任务。由于专业要求很高，收集抑郁症患者的数据非常困难。这导致目前的抑郁症自动检测效果不尽如人意。因此，使用具有足够先验知识的预训练模型来提高检测精度是很自然的想法。这一系列实验是在DAICWOZ抑郁症数据库上进行的，该数据库是痛苦分析访谈语料库(DAIC)的子集[26]。我们选择SER任务和ASR任务进行传输。对于SER，我们使用预先训练的带有ResNet152的PyResNet作为主干。对于ASR，我们使用ESPNet[27]，这是一个端到端的编解码器结构网络。

如表6所示，基于SER的传输性能优于基于ASR的传输性能。这是因为ASR提取的特征偏向于语义，而SER提取的特征偏向于声学。抑郁症检测更注重与SER任务差距较小的声学特征。此外，在成帧时，我们还考虑了SER和ASR在带宽上的差异。ASR通常使用大约25ms的窄窗口长度。这意味着它更注重时间上的变化，具有更高的时间分辨率。对于SER，我们使用了65ms左右的宽窗口长度，这意味着每帧的频率信息更丰富，频率分辨率更高。由于较高的频率分辨率有利于提取声学特征，因此SER预训练模型可能是一些下游任务的较好选择，如抑郁检测。

在这项工作中，我们提出了一个具有挑战性的大规模英语语音情感识别数据库LSSED，它可以模拟真实的分布。我们指出，现有的算法往往会过度适应小规模的数据库，因此不能很好地推广到真实场景中。此外，我们还发布了一些基于LSSED的预训练模型。这些模型不仅可以促进SER的发展，还可以转移到类似的下游任务，如心理健康分析，在这些任务中，数据收集起来极其困难。

## 引文
