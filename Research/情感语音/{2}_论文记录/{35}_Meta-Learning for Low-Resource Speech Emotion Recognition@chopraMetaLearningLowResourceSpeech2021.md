---
title: "Meta-Learning for Low-Resource Speech Emotion Recognition"
description: ""
citekey: chopraMetaLearningLowResourceSpeech2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
---

> [!info] 论文信息
>1. Title：Meta-Learning for Low-Resource Speech Emotion Recognition
>2. Author：Suransh Chopra, Puneet Mathur, Ramit Sawhney, Rajiv Ratn Shah
>3. Entry：[Zotero link](zotero://select/items/@chopraMetaLearningLowResourceSpeech2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Chopra et al_2021_Meta-Learning for Low-Resource Speech Emotion Recognition.pdf>)
>4. Other：2021 - ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)     -   

>- :luc_github: 论文实现：https://github.com/pmathur5k10/Meta-learning-for-Low-Resource-Speech-Emotion-Recognition
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***


## ⭐ 重点

- 使用 Meta-Learning 方法从高资源语言数据库学习网络参数设置，然后在低资源语言数据库中微调训练，缓解低资源问题。
- 比较了迁移学习，多任务学习，元学习三者在本文结构中的效果- 使用 Meta-Learning 方法从高资源语言数据库学习网络参数设置，然后在低资源语言数据库中微调训练，缓解低资源问题。
- 比较了迁移学习，多任务学习，元学习三者在本文结构中的效果

## 摘要

> [!abstract] While emotion recognition is a well-studied task, it remains unexplored to a large extent in cross-lingual settings. Speech Emotion Recognition (SER) in low-resource languages poses difficulties as existing approaches for knowledge transfer do not generalize seamlessly. Probing the learning process of generalized representations across languages, we propose a meta-learning approach for low-resource speech emotion recognition. The proposed approach achieves fast adaptation on a number of unseen target languages simultaneously. We evaluate the Model Agnostic Meta-Learning (MAML) algorithm on three low-resource target languages -Persian, Italian, and Urdu. We empirically demonstrate that our proposed method - MetaSER1, considerably outperforms multitask and transfer learning-based methods for speech emotion recognition task, and discuss the benefits, efficiency, and challenges of MetaSER on limited data settings.

> 虽然情绪识别是一项已经研究得很好的任务，但在很大程度上，它在跨语言环境中仍未被探索。低资源语言中的语音情感识别(SER)带来了困难，因为现有的知识转移方法不能无缝地推广。探讨了跨语言广义表征的学习过程，提出了一种用于低资源语音情感识别的元学习方法。该方法同时实现了对多种不可见目标语言的快速适应。我们在三种低资源目标语言波斯语、意大利语和乌尔都语上对模型不可知元学习(MAML)算法进行了评估。实验证明，我们提出的方法MetaSER1在语音情感识别任务中的性能明显优于基于多任务和迁移学习的方法，并讨论了MetaSER在有限数据环境下的优势、效率和挑战。

## 预处理

## 概述

## 结果

在这项工作中，我们使用了四个流行的英语数据集(TESS[13]，RAVEDESS[14]，SAVEE[15]，IEMOCAP[16])和一个德语数据集(EMODB[17])作为预训练的来源。我们选择了三个低资源语言数据集进行适应-意大利语(EMOVO[18])、波斯语(SHEMO[19])和乌尔都语(乌尔都语[20])。表1列出了源数据集和目标数据集的语料库统计数据。每个数据集具有不同数量的情感类别，最小类别为4个，最大类别为8个。为了能够在所有数据集之间进行对称比较，我们限制了我们在四个主要情绪类别上的实验-快乐、悲伤、愤怒和中性，这四个情绪类别通常存在于所有源和目标数据集中。剩余类的剩余数据样本不在范围内。每个语料库中的数据按70：30的比例分为训练和测试。此外，以分层方式选择的训练数据的20%用于模型验证。MFCC特征的选择：Mel频率倒谱系数(MFCC)是通过对由在MEL频率尺度上线性间隔的三角滤波器组成的滤波器组的输出对数能量去相关来获得的。这有助于提取编码说话风格信息的声学特征，这些特征表现出比韵律特征更好和更稳健的性能。在过去SER[21]研究的基础上，我们的所有实验都基于话语的MFCC特征。对于每个话语，我们从最多120帧的输入中提取特征。较短的发音被零填充，较长发音的额外信号被裁剪，以每个发音的(120，20)特征矩阵结束。

![]({35}_Meta-Learning%20for%20Low-Resource%20Speech%20Emotion%20Recognition@chopraMetaLearningLowResourceSpeech2021.assets/image-20220605122440.png)

## 精读

语音情绪识别（SER）是指从音频中识别主要的说话者情绪。任务很复杂，因为情绪无法明确定义，更不用说准确检测了。大多数关于SER的工作都集中在高资源语言上，例如英语，普通话，法语和德语，这些语言具有广泛的数据资源。相比之下，低资源语言很少受到研究界的关注。大多数SER数据集专门设计用于训练人类在不同情绪状态下记录语音。这些数据集根据年龄，性别和说话者的类型有明显的区别，因此为学习概括技术提供了各种各样的训练实例。构建这样的端到端SER系统需要大量带注释的语音数据，这既繁琐又昂贵。有限的数据和各种缺陷在为低资源语言构建强大的SER分类器方面造成严重缺陷。[1] 假设情绪识别是一项与语言无关的任务。它表明，相同情绪的声音线索应该在语言中很常见。在多语言转移学习和多任务学习方法[2]中可以看出，在其他语言源上进行预训练，因为初始化后对目标语言进行微调成为这种低资源设置中的主要方法。已知该技术通过利用特定于每个情绪类别的特征来提高语音情绪分类器的性能[3]。但是，这是一种依赖语料库的方法，专注于语言拟合，而不是跨各种语言家族进行概括。表征学习语音中情绪的目的不应该专门针对特定语言，而应该在有限的监督下学习广义表征。

在本文中，我们研究了SER多语言元学习的一个新的研究方向，它能够同时快速适应几个不同任务的看不见的数据。我们认为每个语料库都是一个要优化的独立任务。元学习遵循“学习到学习”范式，其中从高资源语音语料库学习的参数更新在多个低资源语言目标数据集上以一次性学习策略进行微调，如图1所示。我们使用模型不可知元学习（MAML）算法[5]。我们的主要贡献包括使用简单的LSTM backbone架构评估所提出的元学习算法-MetaSER，使用三种低资源语言-意大利语，波斯语和乌尔都语。当在类似的训练环境中对多个英语和德语数据集进行预训练时，MetaSER的表现与比较转移学习（TransSER）和多任务学习（MultiSER）等价物形成对比。我们将元学习应用于低资源语音情绪识别任务的工作是第一次。

SER中基于多任务和迁移学习的方法

[6]中的基于多任务和迁移学习的方法是第一批分析跨语言情感识别的方法之一，并报告说它无意中导致了性能的下降。
[1]认为在不同语言中，每种情绪都有一些共同的声音线索。
[7]探索了与标准归一化技术相结合的多任务学习策略，用于英语和日语多语言情感识别。
[8]对四种不同语言的迁移学习和多任务学习方法进行了全面的评估，但注意到在辅助任务上的多任务联合学习的成绩不如迁移学习。

元学习在语音中的应用：一些文献报道了元学习在自动语音识别(ASR)中的有效性。
[9]演示了使用元学习调整声学模型所有权重的原则性方法。
基于MAML的元学习方法是ASR中多任务迁移学习方法的竞争性选择[10]。
最近，[11]分别探索了文本到语音和情感歧义的元学习。

元学习的目标是从一组任务中学习模型的初始化参数，以便模型能够快速适应几个数据点中的新任务。在本文中，我们的方法通过MAML[5]来优化基础神经结构。对高级资源语言$\mathcal{T}=\left\{T_{1}, T_{2}, T_{3} \ldots T_{k}\right\}$的分布进行了参数优化，该模型适用于一种称为目标任务的低资源语言。MAML是一个两步过程：

(I)通过共享编码器从$\mathcal{T}$学习良好的初始化参数$\theta^{*}$(称为MetaLearn步骤)；
(II)在$T_{l}$(称为微调步骤)上进行特定于任务的学习，获得公式1所给出的微调参数$\theta_{t}^{*}$。将模型暴露在各种任务中使其能够在几个步骤和较少的数据量内学习新任务。
$$\theta_{t}^{*}=\operatorname{Learn}\left(T_{l}，\theta^{*}\right)=\operatorname{Learn}\left(T_{l}；\operatorname{MetaLearn}(\mathcal{T})\right) $$训练范例元学习和微调分别在第$3.2$节和第3.3节中介绍。

MetaLearn: Learning to Learn

假设有一个模型$f(\theta)$，它具有随机初始化的参数$\theta$，并从任务分配$p(\mathcal{T})$中学习。元学习更新包括从$p(\mathcal{T})$采样一批任务$\left\{T_{2}，\ldots T_{i}\right\}$。对于每个任务$T_{i}$，我们将其拆分为训练集和验证集，分别表示为$T_{i}^{\text{Train}}$和$T_{i}^{\text{val}}$。元学习过程从随机初始化的参数$\theta$开始，在$T_{i}^{\text{Train}}$上模拟特定于语言的训练过程，以获得中间参数$\theta_{i}^{\prime}$(公式2)，然后在$T_{i}^{\text{val}}$上对其求值。
$$\begin{gathered}

\theta_{i}^{\prime}=\text { MetaLearn }\left(T_{i}^{\text {train }}, \theta\right) \\

\mathcal{L}_{\mathcal{T}}^{m}(f)=\sum_{\mathcal{T}_{i}} y^{(k)} \log \left(f\left(x^{(k)}\right)+\left(1-y^{(k)}\right) \log \left(1-f\left(x^{(k)}\right)\right)\right. \\

\theta^{*}=M e t a \operatorname{Learn}(\mathcal{T})=\arg \min _{\theta} \sum_{\mathcal{T}_{i} \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{T}_{i}}^{m}\left(f\left(\theta_{i}^{\prime}\right)\right) \\

\theta \leftarrow \theta-\eta \sum_{\mathcal{T}_{i} \sim p(\mathcal{T})} \nabla_{\theta} \mathcal{L}_{T_{i}^{\text {val }}}^{m}\left(f\left(\theta_{i}^{\prime}\right)\right)

\end{gathered}
$$公式3突出显示了任何数据集$\mathcal{T}_{i}$的损失函数，其中梯度是在所有源任务上计算的。它由$\mathcal{L}_{\mathcal{T}_{i}}^{m}$表示，它是数据集中所有样本$\left(x^{(K)}，y^{(K)}\right)$的交叉熵损失准则。公式4示出了公式3中表示的损失函数的最小化，其通过给出更新用于语音情感识别任务的模型的所有源数据集元梯度的值来结束元学习过程。公式5在数学上描述了元梯度更新步骤，其中$\eta$是元学习率。在公式5的总和中展开内部损耗项得到$\theta$的二阶导数。计算二阶导数项的计算代价很高，并且占用大量内存。受一阶MAML(通常称为FOMAML[12])的启发，我们忽略了vanilla MAML的二阶导数部分，而不会对性能造成任何显著的损失。

Language Specific Fine-tuning

$$

\begin{gathered}

\theta_{l}^{*}=\operatorname{Learn}\left(\mathcal{T}_{l}, f\left(\theta^{*}\right)\right)=\arg \min _{\theta} \mathcal{L}_{\mathcal{T}}\left(f\left(\theta^{*}\right)\right) \\

\theta_{l}^{*}=\min _{\theta} \sum_{(X, C) \in \mathcal{T}}-\log \left(P\left(C \mid X, f\left(\theta^{*}\right)\right)\right)

\end{gathered}

$$共享编码器是通过元学习过程由参数$\theta^{*}$初始化的。为了对目标语言任务之一进行分类，我们需要微调次优模型参数，以在目标数据集$\mathcal{T}_{l}$上实现最佳性能。设低资源语言任务$T_{l}$的数据和标签对表示为$(X，C)$，其中$X=\left\{x_{1}，x_{2}，\ldots x_{n}\right\}$是$n$数据样本的集合，$C=\left\{c_{1}，c_{2}，\ldots c_{l}\right\}$是$l$类标签的集合。特定语言的学习通过对特定任务$T_{l}$的梯度下降来进行，以最小化公式6和7中总结的交叉熵损失。


我们打算通过尝试在所有学习范例中保持训练设置的一致性，对MetSER与MultiSER和TransSER进行比较分析。我们为元学习和转移学习实验采用共同的基础模型来比较和对比类似设置中的性能。基本模型是双层LSTM模型，最后是两个密集层。每个LSTM单元都有128个维度的隐藏状态。完全连接的层分别具有128和4个神经元。

TransSER的训练设置：在转移学习的情况下，模型在源中的每个数据集上按顺序进行预训练。然后冻结LSTM参数并微调目标数据集之一的训练部分上的致密层。

MultiSER的训练设置：多任务学习的训练设置涉及对所有源数据集进行交替的课堂预训练。然后在目标数据集的完整训练部分上微调模型的密集层。通过这种方式，该模型避免了灾难性的遗忘，因为它以循环方式从所有类中学习特征。在我们的实验中执行的多任务学习的形式导致跨所有层的软参数共享。

多任务和转移学习基线的超参数：我们对所有实验使用循环学习速率计划，基本学习速率为2e− 5，最高学习率为1 e− 4.发现最佳批量为64。转移学习的预训练和微调阶段的最大时期数分别保持为1000和2500，直到验证损失收敛。

元学习的训练设置：由于过度拟合的显着缺点，从头开始训练MAML体系结构是一项具有挑战性的任务。其主要原因是在微调[22]步骤中仅在几个数据点上更新了整个网络。我们调查了元学习对源数据集的五种不同组合的影响。元学习的超参数：元学习过程有两个优化过程元更新和特定于任务的微调。两种方法都有自己的学习率：meta-LR和task-LR。MetaLR在MetaLearn阶段进行了优化，然后在调整任务LR时在特定于语言的微调期间保持恒定。我们在两个预训练集上的实验中，meta-LR和微调LR的最优值均为1e− 6和2e− 4，分别。我们用Adam优化了元情节，任务特定学习使用随机梯度下降（SGD）。更新元参数的每次迭代都称为情节。每个模型运行中的最大剧集数保持为1e+4。每个元情节都有内部步骤更新，这被称为内部任务。根据经验，内部任务在设置为8时实现收敛。我们通过限制任何给定批次中可用的样本数量来调查MetaSER对未见数据的普遍性。因此，元学习器的批量大小b由k-shot学习参数k和不同类的数量c（b=k∗ c） 。我们保持c=4不变，同时改变k以根据宏F1分数评估模型性能。

MultiSER和Ranser与MetaSER的性能比较：表2中F1分数的比较清楚地表明，MetaSER在所有目标语言的预训练集的所有组合上均显着优于多任务学习（MultiSER）和转移学习（TransSER）对应物。，其中一个源集中的乌尔都语除外。结果强化了我们的假设，即基于多任务和转移学习的方法更多地关注源语言，而不是概括跨语言培训。鉴于源语言主要属于日耳曼语家族，因此从经验上证明，MAML培训可用于从高资源语言家族推广到低资源语言家族。数据大小对学习能力的影响：为了研究MetaSER在数据稀缺环境中的普遍性，我们在一小部分目标训练数据上微调模型，并测试TransSER，MultiSER和MetaSER的模型性能。对于TransSER和MultiSER，模型在完整的源数据集上进行预训练，并在目标数据集的分数训练部分以0.1的间隔进行微调。对于MetaSER，我们将少数镜头参数k的值作为可用训练数据的一部分进行改变，使得k∈ {0.1, 0.2, 0.3, . . . , 1}. 在所有情况下，目标数据集的测试部分在推理期间保持相同。由此产生的模型F1分数被绘制出来，在TESS，EMODB和RAVEDESS的源集中给出图2，这表明TransSER和MultiSER在早期阶段都饱和，而MetaSER随着更多的训练数据可用而稳步提高，直到它开始胜过它们的拐点。然而，MAML培训的陡坡也揭示了培训MAML架构的复杂性，而不是转移学习。尽管MAML训练在所有目标数据集中提供了更好的F1得分结果，但它需要足够的数据才能超过其性能阈值。

### 引文

## 摘录
