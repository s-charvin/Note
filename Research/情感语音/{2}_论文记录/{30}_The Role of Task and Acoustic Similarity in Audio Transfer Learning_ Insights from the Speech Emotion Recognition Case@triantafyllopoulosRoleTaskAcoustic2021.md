---
title: "The Role of Task and Acoustic Similarity in Audio Transfer Learning: Insights from the Speech Emotion Recognition Case"
description: ""
citekey: triantafyllopoulosRoleTaskAcoustic2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:32:56
lastmod: 2023-04-11 11:55:52
---

> [!info] 论文信息
>1. Title：The Role of Task and Acoustic Similarity in Audio Transfer Learning: Insights from the Speech Emotion Recognition Case
>2. Author：Andreas Triantafyllopoulos, Björn W. Schuller
>3. Entry：[Zotero link](zotero://select/items/@triantafyllopoulosRoleTaskAcoustic2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Triantafyllopoulos_Schuller_2021_The Role of Task and Acoustic Similarity in Audio Transfer Learning.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 使用迁移学习时，越相关的任务，迁移效果会更好
- 最终微调过程，靠近输入的层比仅微调输出分类层有更多的适应
- 为了处理目标标签的不平衡问题，我们使用了一种平衡的非负似然损失(NLLoss)
- arousal、valence、dominance 三个情感维度并不是完全无关的，可以通过一定方式找出其相关性。- 使用迁移学习时，越相关的任务，迁移效果会更好
- 最终微调过程，靠近输入的层比仅微调输出分类层有更多的适应
- 为了处理目标标签的不平衡问题，我们使用了一种平衡的非负似然损失(NLLoss)
- arousal、valence、dominance三个情感维度并不是完全无关的，可以通过一定方式找出其相关性。

## 摘要

> [!abstract] With the rise of deep learning, deep knowledge transfer has emerged as one of the most effective techniques for getting state-of-the-art performance using deep neural networks. A lot of recent research has focused on understanding the mechanisms of transfer learning in the image and language domains. We perform a similar investigation for the case of speech emotion recognition (SER), and conclude that transfer learning for SER is influenced both by the choice of pre-training task and by the differences in acoustic conditions between the upstream and downstream data sets, with the former having a bigger impact. The effect of each factor is isolated by first transferring knowledge between different tasks on the same data, and then from the original data to corrupted versions of it but for the same task. We also demonstrate that layers closer to the input see more adaptation than ones closer to the output in both cases, a finding which explains why previous works often found it necessary to fine-tune all layers during transfer learning.

> 随着深度学习的兴起，深度知识迁移已经成为利用深度神经网络获得最先进性能的最有效技术之一。最近的许多研究都集中在理解意象和语言领域的迁移学习机制。我们对语音情感识别(SER)进行了类似的研究，得出结论：语音情感识别的迁移学习既受预训练任务选择的影响，也受上下游数据集声学条件差异的影响，其中前者影响更大。通过首先在相同数据的不同任务之间传输知识，然后将原始数据传输到其损坏的版本，但对于相同的任务，每个因素的影响是隔离的。我们还证明，在这两种情况下，靠近输入的层比靠近输出的层有更多的适应，这一发现解释了为什么以前的研究经常发现在迁移学习过程中有必要微调所有层。

## 预处理

## 概述

## 结果

作为迁移学习的下游数据集，我们使用了最近推出的SER数据集MSPPodcast(v1.7)[29]。它被分成了不同于说话人的分区：
·一个由38179个片段组成的训练集
·一个由7538个片段组成的开发集，从44个说话者(22名男性-22名女性)中收集
·12 902个片段组成的测试集，由60名说话者(30名男性-30名女性)组成，MSP-Podcast已经为arousal、valence、dominance以及8个情绪类别的情感维度加上一个额外的其他类别进行了注释。

在目前的工作中，我们将重点放在情感方面。这些已经在发声层面上以7-point 李克特量表（Likert scale）进行了注解，个别注释者的分数被平均以获得一致投票。与文献[30，31]中的其他方法类似，我们将连续值归入3分标度。我们使用以下映射：

低：[1-3]·中：(3-5)·高：(5-7)


这会导致了严重的不平衡分布，9%的数据在低范围内，67%在中范围内，24%在高范围内。

这些维度是能够用来定义影响，并且经过充分验证的结构[32]，其已经被证明通过不同的声学提示（acoustic cues）来表现[33]。虽然它们量化了情感表达的不同方面，但它们并不是彼此完全无关的。他们的相似性可以通过三个情绪维度之间的皮尔逊相关性Pearson correlation来衡量。在MSP-Podcast训练集上，arousal与valence的相关性为0.2412，与dominance的相关性为0.7953。这表明了这三个方案之间的任务相似程度，这是我们在迁移学习实验中利用的一个事实。

我们还利用三个额外的数据集进行预训练，我们将把它们称为上游数据集：AudioSet[27]，原始作者表明它有助于SER，VoxCeleb1[34]，我们预训练说话人识别，因为它被证明转换成SER[26]，以及IEMOCAP[35]，它被注释为相同的情感维度。由于篇幅所限，我们参考原始出版物了解每个数据集的详细说明。

我们进行了三组实验：
·在不同的数据集上进行预训练；在MSPPodcast上针对arousal任务进行微调
·在MSP-Podcast上针对不同的任务进行训练；在arousal上进行微调
·在干净的arousal数据上进行训练；在带宽受限的arousal数据上进行微调。

## 精读

深度学习（DL）方法在后几年获得了显着的突出地位。对其有效性最常被接受的解释之一是深度神经网络（DNN）体系结构可以学习在不同任务之间进行迁移的通用表征[1,2]。最近随着自我监督学习的出现，这引出了大量关于利用过去信息提高性能和增加新任务和/或数据集收敛性的文献研究[3,4]。然而，这种技术并不总是能产生更好的性能，会导致“负迁移”的良好记录效应[5,6]。这就提出了迁移学习何时成功的问题，特别是它在多大程度上受到预训练、下游任务、输入特征、体系结构类型以及不同数据集之间并置的影响。

为此，Neyshabur等[7]研究了视觉领域的迁移学习，并假设下游任务受益于预训练，因为模型正在学习可迁移的高级特征，并且因为他们学习低级统计。这些观察结果可归因于在视觉领域广泛研究的组合性概念[8]。许多先前的工作都集中在学习音频域中的一般表征，无论是使用监督[9,10,11]，无监督[12,13,14]还是自我监督方法[15,16,17,18]]。随着数据稀缺的众多应用程序的兴起，例如在医疗领域[19]，该主题变得越来越相关。在这项工作中，我们将语音情绪识别（SER）作为下游应用，这是一个在社区中受到相当关注但大数据尚未广泛应用的领域[20]。虽然DNN已经超越了传统方法[21]，但并非所有任务和数据集都如此[22]。这导致社区采用迁移学习方法，从基于特征的[23]开始，最近转向DL方法[24,25,26]。因此，了解迁移学习的工作原理可能会设计更强大的算法，释放DL对SER和其他低资源音频任务的全部潜力。我们的主要贡献在于将预训练任务的影响与各个数据集之间的声学不匹配的影响区分开来；我们期望在成功迁移中发挥重要作用的两个因素。为此，我们首先利用三种不同的数据集和任务进行预训练，以说明这两种因素在实际应用中的相对重要性。然后，我们利用这样一个事实，即我们的SER数据集已被注释为多个不同的情绪方案，它们之间具有不同程度的相似性。这使我们能够通过训练一个方案并将知识迁移到同一数据集上的另一个方案来隔离任务相似性的影响。最后，我们通过将知识从相同数据的干净版本迁移到损坏版本来隔离声学相似性的影响。我们的实验表明，虽然这两个因素都很重要，但主要是缺乏任务相似性导致负迁移，而即使是极端的声发散也可以克服。此外，我们做出了令人惊讶的观察，即更接近输入的层更容易适应，这一发现可以解释为什么之前作品中的作者发现有必要对所有层进行微调而不是最后一层[10,17]。这是一个重要发现，因为微调更多层会增加优化的开销，因为需要调整更多参数。


我们的实验是使用Kong等人最近引入的Cnn14架构进行的[10]。它已经过培训，可以在AudioSet上进行音频标记[27]。作者开放了他们的代码和训练有素的权重1。我们使用16 kHz变体，因为我们使用的数据集也来自16 kHz。作为特征，我们使用了使用64个Mel bins，32 ms的窗口大小和10 ms的帧移，计算的log-Mel频谱图.C nn14遵循VGG架构设计[28]。在最后一个卷积层之后，使用最大和平均池将特征汇集到特征维度上，随后馈入两个线性层。在每第二个卷积层之后应用概率为0.2的辍学。

![]({30}_The%20Role%20of%20Task%20and%20Acoustic%20Similarity%20in%20Audio%20Transfer%20Learning_%20Insights%20from%20the%20Speech%20Emotion%20Recognition%20Case@triantafyllopoulosRoleTaskAcoustic2021.assets/image-20220603181014.png)

除非另有说明，所有的实验都是使用标准的随机梯度下降优化器进行的，恒定学习率为0.001，Nesterov momentum设置为0.9[36]，批次大小为8。这些网络总共训练了60个epoch。我们只显示在验证集上产生最佳性能的epoch的结果。

为了处理目标标签的不平衡问题，我们使用了一种平衡的非负似然损失(NLLoss)，该损失是通过将每一项与训练集中对应类别的频率的倒数相乘而得到的。我们首先通过从随机初始化训练模型来训练标准基线。经过58个时代的训练，我们的UAR达到了68.76%。我们将这种模型称为Cnn14-Baseline。


对于所有迁移学习实验，我们尝试两个变体：

·微调所有层：通过这个实验，我们有兴趣了解网络如何适应新数据。
·仅微调线性层：通过此实验，我们有兴趣了解网络如何能够利用在预培训中学到的特征。

为了衡量模型对新任务的适应情况，一个好的指标是训练前和训练后各层权重之间的距离，如Neyshabur等人所示。[7]。为此，我们使用余弦距离：

$$

d(x, y)=1-\frac{x \cdot y}{\|x\|\|y\|}

$$

我们的第一个实验是使用在第三节提到的上游数据集上预先训练的模型进行的。

- 对于AudioSet我们使用孔等人发布的权重。[10]并将该预训练模型称为Cnn14 AudioSet。
- 对于VoxCeleb1我们使用标准NLLoss对网络进行100个epoch的训练，并选择在验证集上提供最佳准确性的检查点(在epoch92上为64%)，我们将该模型称为Cnn14 VoxCeleb。
- 最后，对于IEMOCAP我们训练网络60个epoch，并选择在验证集上给出最佳UAR的检查点(在epoch33上为64%)。我们使用与张等人相同的装箱和训练/开发/测试拆分。[31][中英文摘要]。我们将这种模型称为Cnn14 IEMOCAP。


为了理清任务的影响和上下游任务之间的声学差异，我们利用了MSP Podcast被注释为三种不同情绪属性的事实，如第三节所述。因此，我们预训练了一个关于Valence的模型和另一个关于dominance能力的模型，我们分别称之为Cnn14-Valence和Cnn14-Dominance，并为arousal对它们进行了微调。在原始任务的预训练过程中，Valence模型在第52时段达到峰值，UAR为63.56%，dominance模型在第33时段达到54.87%。最后，我们有兴趣系统地研究从影响任务相似性中分离出来的声学相似性的影响。我们通过将数据通过窄带通滤波器来模拟不同程度的声学相似性  去除大部分频谱，而通过将知识迁移到arousal分类任务和从arousal分类任务迁移来保持任务相似性不变。我们使用中心频率为500 Hz的四阶Butterworth滤波器，并测试出以下频带宽度：[20,40,60,80,100,200,300,400]。

关于迁移学习的有效性，结果好坏参半：尽管在使用原始数据时，我们无法超过基线表现，但表1和图2a都表明，预培训加速了收敛。此外，微调所有层总是更有利于仅微调线性层，这一发现与以前的工作一致[10，17]。这也与图3a中LayerWise余弦距离显示的趋势一致。较早的层在初始化方面比后一层有更多的适应，除了CNN14-VoxCeleb之外的所有模型的进一步训练加剧了这一趋势。我们的主要关注点是区分任务和声学相似性的影响。使用表1中所示的不同上游数据集进行的初步实验表明，这两种影响都在发挥作用。对于arousal分类，Cnn14-AudioSet的表现不如Cnn14-IEMOCAP和Cnn14-VoxCeleb，这表明任务相似性比声学相似性更重要；虽然AudioSet比其他两个数据集更大，呈现更多的声学多样性，但音频标记任务也与arousal分类有本质的不同。在MSP-Podcast上对不同标注方案到觉醒的知识迁移实验进一步说明了任务相似性的重要性。与dominance能力相比，Valence训练与arousal的相关性要小得多，这也会导致更糟糕的表现，并需要更长的时间才能收敛。Cnn14-Valence和Cnn14-IEMOCAP之间的直接比较也突显了任务相似性与声学相似性的相对重要性。后者是针对总体较少的数据进行预训练的，这些数据来自记录在非常狭窄的一组条件中的不同数据集，但针对相同的任务。然而，它的表现比前者要好得多，前者是在相同的数据上进行预训练的，但任务不同。最后，我们关于将知识迁移到相同数据的损坏版本但用于相同任务(arousal)的实验表明，成功的知识迁移是可能的，虽然取决于声学失配的程度。图2B中的UAR结果表明，从预先训练的网络开始会导致更好的性能、更快的收敛和更好的初始化，即使被破坏的声音信号与原始的声音信号根本不同。正如预期的那样，更宽的带宽会带来整体更好的性能，无论是在进行预培训的情况下，还是在没有预培训的情况下。图3b所示的权重空间距离表明，微调主要影响较早的层，这表明这些层还负责适应上行和下行数据集之间的声学条件变化。

我们已经通过实验证明，SER 的迁移学习取决于声学和任务相似性，后者是决定因素。结果表明，错误选择任务可能不利于迁移学习成绩。另外，我们已经确定，靠近输入的层比接近输出的层更适应；这一事实解释了为什么许多以前的作品在微调所有层而不是简单的最后层时表现出更好的性能。这些发现应该指导 SER 的体系结构设计和预培训策略。如图所示，不同的情感维度可能导致根本不同的表征，这一事实使得寻求通用表征非常具有挑战性。为了获得语音片段的整体情感表征，我们需要能够概括几个不同任务的表征，这些表征应该反映在训练前的团中。

### 引文

## 摘录
