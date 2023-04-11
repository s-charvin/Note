---
title: "Multitask Learning and Multistage Fusion for Dimensional Audiovisual Emotion Recognition"
description: ""
citekey: atmajaMultitaskLearningMultistage2020
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:34:19
lastmod: 2023-04-11 12:02:59
---

> [!info] 论文信息
>1. Title：Multitask Learning and Multistage Fusion for Dimensional Audiovisual Emotion Recognition
>2. Author：Bagus Tris Atmaja, Masato Akagi
>3. Entry：[Zotero link](zotero://select/items/@atmajaMultitaskLearningMultistage2020) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Atmaja_Akagi_2020_Multitask Learning and Multistage Fusion for Dimensional Audiovisual Emotion.pdf>)
>4. Other：2020 - ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：https://github.com/bagustris/multistage-ser
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 本文目标是增强CCC，因此使用CCC损耗代替MSE损失函数
- 比较了多任务学习（计算多个维度损失值的总损失）、单任务学习（计算单一维度损失值的损失）在单模态、多模态模型中的效果，得出了多任务学习更好些。
- 比较了早期融合方法和晚期融合方法。
- 在多任务学习中，提出了一种多阶段融合的方法，提升了最终效果。- 本文目标是增强 CCC，因此使用 CCC 损耗代替 MSE 损失函数
- 比较了多任务学习（计算多个维度损失值的总损失）、单任务学习（计算单一维度损失值的损失）在单模态、多模态模型中的效果，得出了多任务学习更好些。
- 比较了早期融合方法和晚期融合方法。
- 在多任务学习中，提出了一种多阶段融合的方法，提升了最终效果。

## 摘要

> [!abstract] Due to its ability to accurately predict emotional state using multimodal features, audiovisual emotion recognition has recently gained more interest from researchers. This paper proposes two methods to predict emotional attributes from audio and visual data using a multitask learning and a fusion strategy. First, multitask learning is employed by adjusting three parameters for each attribute to improve the recognition rate. Second, a multistage fusion is proposed to combine results from various modalities' final prediction. Our approach used multitask learning, employed at unimodal and early fusion methods, shows improvement over single-task learning with an average CCC score of 0.431 compared to 0.297. A multistage method, employed at the late fusion approach, significantly improved the agreement score between true and predicted values on the development set of data (from [0.537, 0.565, 0.083] to [0.68, 0.656, 0.443]) for arousal, valence, and liking.

> 视听情绪识别由于能够利用多模态特征准确预测情绪状态，近年来受到研究者的广泛关注。本文提出了两种基于多任务学习和融合策略的基于视听数据的情感属性预测方法。首先，通过调整每个属性的三个参数来进行多任务学习，以提高识别率。其次，提出了一种多阶段融合的方法，将不同模态的最终预测结果进行融合。我们的方法使用了多任务学习，在单峰unimodal（单模态）和早期融合方法中使用，显示出比单任务学习更好的结果，平均Ccc得分为0.431分，而单任务学习方法为0.297分。在晚期融合方法中采用的多阶段方法显著提高了发展数据集上的真实值和预测值之间的一致性分数(从[0.537，0.565，0.083]提高到[0.68，0.656，0.443])，包括性唤醒、效价和喜好。

## 预处理

## 概述

## 结果

本研究使用了[3]中提供的 SEWA 数据集[12]。该数据集包含来自汉语、英语、德语、希腊语、匈牙利语和塞尔维亚语的视听记录，但在这项工作中仅使用德语(DE)和匈牙利语(HU)，因为它们没有提供其他语言的测试标签。提供三个属性来表示情绪状态，即：唤醒、价位和喜好。这些属性的分数是从几个母语人士的注释中获得的：六个德国人和五个匈牙利人。在96名受试者中，68名受试者(每名34名)用于培训，其余28名受试者(每名14名)用于验证/发展。除了数据集，文[3]的作者还提供了表1所示的基线特征。我们没有生成新的特征集，而是将多任务学习和多模式视听融合应用于这些特征集。对于音频和视觉特征，使用相同的处理块，即4.0s 的窗口长度和100ms 的跳跃大小，其中还为每0.1s 给出标签。然后，通过为低于该数字的其他序列填充零，将最长的1768序列(标签号)用于所有对象。对于双峰特征融合，音频和视觉特征在被送入分类器之前被连接起来。

## 精读

已经使用两种观点来实现自动情绪识别：分类视图和维度视图。虽然大多数研究人员试图将人类情绪分为不同的类别（例如幸福，愤怒等），但维度情绪识别是更具挑战性的任务，因为它试图将情绪标记为程度而不是类别。从维度的角度来看，情感被描述为2或3个属性[1]。

- Valence (pleasantness)和arousal (emotion intensity)是2D情绪模型中两个最常见的维度。
- 在3D模型中，使用dominance (degree of control)或liking。
- 其他属性，如expectancy，可以作为第四维（4D）添加[2]。

在本文中，我们评估了三个情绪维度/属性：arousal, valence, 和 liking，这些都是从[3]中的数据集中获得的。此任务是在特定指标上获得最准确的预测。作为回归任务（分类任务），最常见的指标是真实值和预测情绪程度（值）之间的误差。然而，最近的研究人员[3]引入了相关性(correlation)测量来确定真实值与预测情绪程度之间的一致性。

通常使用两种方法来最小化学习过程特征的损失并获得预测情绪维度的最佳模型，即单任务学习（STL）和多任务学习（MTL）。
- 单任务学习仅在多输出学习中最小化单个损失函数。例如，当学习预测维度情绪中的唤醒，效价和喜好时，只有唤醒被最小化。其他维度，效价和喜好，在学习过程中被忽略。通过最小化唤醒误差，学习过程的结果可用于预测一维（唤醒）或所有三个维度（唤醒，效价和喜好）。
- 单任务学习的问题在于，当它用于预测多个输出时，使用单个损失函数预测三个分数。一个维度的高分通常导致另一个维度的得分较低。为了解决这个问题，我们引入了在使用最小化所有情绪维度的真实情绪和预测情绪程度之间的误差情况下的多任务学习。多任务学习中的常用方法是对学习过程中的每个损失函数使用相同的加权因子。因此，损失总和是来自每个情绪维度的三个每个损失函数的总和。我们在本文中提出的方法旨在通过为每个情绪维度的每个损失函数分配不同的加权因子来获得平衡分数。

由于情绪来自多种形式，因此创建融合策略以适应这些模态也是一项挑战。标准方法是通过在相同或不同网络中组合不同模态之间的特征。这被称为早期融合策略。然后训练这两个或多个融合特征以将这些输入映射到标签上。另一个策略是使用后期融合。在这个策略中，每种模态都使用其标签在其相应网络中进行训练。然后将每种模态的识别结果分组以找到对应于标签的最高概率。早期融合和晚期融合的结果也可以通过将这些结果组合在支持向量回归（SVR）中来融合。最后一步的结果可以多阶段重复，以提高识别率。

我们对本文的贡献可以概括如下：
（1）使用多任务学习来最小化损失函数，使用三个参数来处理来自视听特征的三个情绪属性；
（2） 融合策略通过分析早期融合和晚期融合的单峰unimodal（单模态）和双峰bimodal（双模态）特征，结合早期-晚期融合使用多级SVR来提高视听情绪识别率。

Multitask learning

机器学习中的问题之一是获得适当的成本函数或损失函数来对数据进行建模。回归分析（分类任务）中的大多数问题的损失函数都使用真实值和预测值之间的误差计算。损失函数的选择通常由用于评估的指标决定。在维度情感识别的情况下，
- Ringeval 等人建议使用一致性相关系数 (CCC) 来对预测情绪属性的性能进行评分 [3]。
- Parthasarathy 和 Busso 使用多任务学习来最小化维度情感识别中的均方误差 (MSE) [4]。作者使用两个参数来衡量三个情绪属性的损失函数：唤醒、效价和支配。并确定了唤醒和效价的加权因子，以及优势的加权因子（唤醒和效价的加权因子中减去 1 来获得）。所有权重因子都在 0-1 的范围内，其中一个值为 0 的可能性为 33.3%。还发现唤醒和效价的最佳参数是 0.7 和 0.3。在这种情况下，学习过程中忽略了优势，可以将其视为类似于单任务学习的两任务学习。
- 使用共享层和独立层等两种多任务学习方法，与基线单任务学习相比，作者实现了 CCC 分数的提高 [4]。由于系统在较大的网络上比在较小的网络上学习得更好，因此使用的网络越大，获得的改进就越大。
- Chen 等人还使用以 MSE 作为损失函数的多任务学习 [5]。尽管从给定的基线上实现了 CCC 分数的提高，但没有指定与单任务学习的性能比较。这可能会导致难以确定改进是来自多任务学习还是其他使用的策略。

Multimodal Fusion

由于可以从许多模态中识别情感，例如语音、面部图像、运动和语言信息，因此在此类系统中通常考虑使用多模态技术来适应许多特征。 
- [ ] 中描述的数据集包括来自音频和视觉的多模态情感特征。
- 布索等人 [6]提供了来自语音和手势的情感数据集，包括面部表情和手部动作。
- 该数据集的改进版本[7]提供了一个带有视听信息的情感数据库，从而促进了（表演）录音中的自然性。

为了处理从多模态数据集中提取的各种特征，研究人员开发了几类特征融合方法[5,8,9,10,11]。大多数策略可以分为早期融合和晚期融合。
- 在早期融合方法中，也称为特征级融合，在进行分类之前将来自不同模态的特征组合起来。
- 在后期融合方法中，也称为决策层融合，最终的决策概率由每个单峰unimodal（单模态）模型结果通过SVR等方法给出。 Ringeval 等人。为来自 SEWA 数据集的后期融合策略提供基线融合方法 [3, 12]。可以使用静态回归器（即 SVR）将每个模态或特征集的结果组合起来，以根据几种模态的给定结果做出预测的情感属性分数的最终决定。

Multitask learning based on CCC loss

CCC是维度情绪识别中用来衡量真实情绪维度与预测情绪程度一致性的常用度量标准。《CCC》的公式

$$C C C=\frac{2 \rho_{x y} \sigma_{x} \sigma_{y}}{\sigma_{x}^{2}+\sigma_{y}^{2}+\left(\mu_{x}-\mu_{y}\right)^{2}}$$ 


式中，$\rho_{x y}$是$x$与$y$之间的皮尔逊系数相关系数，$\sigma$为标准差，$\mu$为平均值。这是基于林的计算[20]。CCC的范围从$-1$(完全不一致)到$1$(完全一致)。因此，使真实值和预测情感之间的一致性最大化的CCC损失函数(CCCL)可以定义为$$CCCL=1-CCC$$
在单任务学习中，损失函数是来自唤醒$\left(CL_{\text{aro}}\right)$、价值$\left(CL_{\text{val}}\right)$或喜欢$\left(CL_{l Ik}\right)$的损失函数之一。在多任务学习中，当CCC损失用作所有唤醒、价位和喜好的单一度量时，$C L_{\text{Total}}$是这三个CCC损失函数的组合：
$$。

C L_{t o t}=\alpha C L_{a r o}+\beta C L_{v a l}+\gamma C L_{l i k}，

$$
其中，$\alpha、\beta$和$\gamma$是每个情感维度损失函数的权重因子。在常见的方法中，$\alpha、\beta$和$\Gamma$被设置为1，而在[4]中，$\Gamma$被设置为$1-(\alpha+\beta)$以最小化MSE。在该方法中，所有权重系数都在0-1的范围内。

在本文中，我们使用了所有这三个参数，并且这些加权因子的和并不限于仅0-1。由于目标是加强CCC，因此使用CCC损耗代替MSE。

![]({37}_Multitask%20Learning%20and%20Multistage%20Fusion%20for%20Dimensional%20Audiovisual%20Emotion%20Recognition@atmajaMultitaskLearningMultistage2020.assets/image-20220605203900.png)

如图1所示，视听情感识别系统由3个LSTM层组成，分别为256、128和64个单元。在每个LSTM层之后添加系数为0.4的丢弃层。在一次实验中使用了RMSprop优化器，学习率为0.0005，批次大小为34，持续50个时期。为了补偿在进行注释时的延迟，标签在训练过程中被移到前面0.1，并且在写预测时被移回。

在图1中，该系统从双峰bimodal（双模态）音频和视觉特征集中产生对唤醒、价位和喜好程度的预测。这一结果可以与使用SVR(来自不同特征集)的单峰unimodal（单模态）或双峰bimodal（双模态）(早期)融合的其他结果相结合，并且从SVR得到的预测也可以输入到相同的SVR系统(使用SCRKIT-LINE工具实现[21])。

![]({37}_Multitask%20Learning%20and%20Multistage%20Fusion%20for%20Dimensional%20Audiovisual%20Emotion%20Recognition@atmajaMultitaskLearningMultistage2020.assets/image-20220605203950.png)

在图2中，这种早期融合和晚期融合的组合分三个阶段进行了说明。首先，使用支持向量机方法对单峰unimodal（单模态）结果(称为结果#1)和多峰(双峰bimodal（双模态）)结果(称为结果#2)或单峰unimodal（单模态）和单峰unimodal（单模态）进行训练。这个学习过程产生一个新的结果(即该图中的结果#3)。将后期融合的结果#3再次馈送到SVR方法结果#4。结果#4再次馈送到SVR方法结果#5。这种多阶段融合可以进行n次以获得CCC评分的改善。为了评估所提出的MTL方法与STL和以前的MTL方法的有效性，我们比较了这些方法之间的CCC分数。表2显示了不同属性的CCC分数及其平均值。我们提出的MTL2的性能优于STL和先前提出的MTL1。

为了找到α，β和γ的最佳参数，我们在0-1的范围内对这些参数进行了随机搜索。表2中使用的参数是最优的，即α，β和γ分别为0.7、0.2和1.0。我们提出的具有三个参数的MTL学习优于STL和以前的MTL[4]。对于STL方法，唤醒和配价在其属性优化时都获得了最高的CCC分数。虽然喜好在STL3中得到了优化，但它仍然是最难估计的。这一问题应在今后的研究中加以解决。


为了获得多级融合结果，执行以下步骤，1。单峰unimodal（单模态）情绪识别：执行此步骤以研究双峰bimodal（双模态）或多峰融合的重要性特征集。2.双峰bimodal（双模态）融合：通过连接来自不同或相同模态的两个特征集来执行该步骤。3.多模态融合：前两步使用DNN进行，第三步使用SVR进行，结合单峰unimodal（单模态）或双峰bimodal（双模态）情绪识别的结果。4.多阶段融合：多模式SVR的输出可以使用相同的SVR进行组合，以提高情绪识别的识别率。我们通过将一个特征集输入到系统中来运行单峰unimodal（单模态）特征集的实验，以找到哪些特征集提供更好的性能。为此，我们使用具有先前解释的LSTM层的小型网络（在Keras[22]中实现）。从12个功能集中，我们通过最高平均CCC分数选择7个功能集。七个特征集的组合产生了21对双峰bimodal（双模态）特征集。请注意，这里双峰bimodal（双模态）的定义不是音频和视觉模态，而是一对两个特征集。从单峰unimodal（单模态）和双峰bimodal（双模态）结果中，我们选择11个最高CCC分数，并将这11个结果输入SVR，以通过后期融合执行多模式视听情绪识别。使用SVR的最后多模态融合可以被认为是1阶段特征融合。通过将SVR的结果输入到相同的SVR系统，可以执行两阶段多模态融合。我们将这种多级多模式融合限制为5次重复。图3显示了CCC评分从1到5个阶段的唤醒，效价和喜好的结果。该图显示，随着阶段数量的增加，CCC分数有所提高。与单峰unimodal（单模态），双峰bimodal（双模态）和多峰融合（1阶段）相比，多级融合获得了显着改善。所提出的多级融合可以将喜欢属性的CCC得分从0.083（基线单峰unimodal（单模态））提高到0.443，这是该任务中最具挑战性的属性。其他两个属性获得相对改善的基线结果分别为26.63%和16.11%的唤醒和效价。

### 引文

## 摘录
