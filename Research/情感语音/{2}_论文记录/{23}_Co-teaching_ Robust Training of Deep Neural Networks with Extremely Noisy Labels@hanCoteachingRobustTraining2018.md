---
title: "Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels"
description: ""
citekey: hanCoteachingRobustTraining2018
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:31:33
lastmod: 2023-04-11 11:26:05
---

> [!info] 论文信息
>1. Title：Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels
>2. Author：Bo Han, Quanming Yao, Xingrui Yu, Gang Niu, Miao Xu, Weihua Hu, Ivor Tsang, Masashi Sugiyama
>3. Entry：[Zotero link](zotero://select/items/@hanCoteachingRobustTraining2018) [URL link](http://arxiv.org/abs/1804.06872) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Han et al_2018_Co-teaching.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\AQULTHKY\\1804.html>)
>4. Other：2018 - arxiv:1804.06872 [cs, stat]     -   

>- :luc_github: 论文实现：https://paperswithcode.com/paper/co-teaching-robust-training-of-deep-neural
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 提出了一种 Co-teaching 方法, 多模型联合学习

## 摘要

> [!abstract] Deep learning with noisy labels is practically challenging, as the capacity of deep models is so high that they can totally memorize these noisy labels sooner or later during training. Nonetheless, recent studies on the memorization effects of deep neural networks show that they would first memorize training data of clean labels and then those of noisy labels. Therefore in this paper, we propose a new deep learning paradigm called Co-teaching for combating with noisy labels. Namely, we train two deep neural networks simultaneously, and let them teach each other given every mini-batch: firstly, each network feeds forward all data and selects some data of possibly clean labels; secondly, two networks communicate with each other what data in this mini-batch should be used for training; finally, each network back propagates the data selected by its peer network and updates itself. Empirical results on noisy versions of MNIST, CIFAR-10 and CIFAR-100 demonstrate that Co-teaching is much superior to the state-of-the-art methods in the robustness of trained deep models.

> 带噪声标签的深度学习实际上是具有挑战性的，因为深度模型的容量如此之高，以至于他们迟早可以在训练过程中完全记住这些噪声标签。尽管如此，最近关于深度神经网络记忆效果的研究表明，它们会首先记忆干净标签的训练数据，然后记忆噪声标签的训练数据。因此，在本文中，我们提出了一种新的深度学习范式，称为“Co-teaching”，用于对抗噪声标签。也就是说，我们**同时训练两个深层神经网络，让它们在每个小批次中相互传授：首先，每个网络前馈所有数据，并选择一些可能干净的标签数据；然后，两个网络相互沟通，这个小批次中的哪些数据应该用于训练；最后，每个网络反向传播其对等网络选择的数据并进行自我更新**。在MNIST、CIFAR-10和CIFAR-100的噪声版本上的实验结果表明，Co-teaching在训练的深度模型的稳健性方面远远优于最新的方法。

## 预处理

## 概述

## 结果

## 精读

从噪声的标签中学习可以追溯到三十年前[1]，并在最近几年仍然保持活力[13，31]。从本质上讲，噪声标签从实际的真实标签中被破坏，因此它们不可避免地退化了学习模型的健壮性，特别是对于深度神经网络[2，45]。不幸的是，噪声标签在现实世界中随处可见。例如，在线查询[4]和众包[42，44]每天都会在世界各地产生大量噪声标签。由于深度神经网络具有很高的适应噪声标签的能力[45]，因此用噪声标签稳健地训练深度网络是一项具有挑战性的工作。目前的方法主要集中在估计噪声转移矩阵。

例如Goldberger等人。[13]，在Softmax层的顶部，添加了额外的Softmax层来模拟噪波过渡矩阵。

Patrini等人。[31]利用两步解决方案启发式地估计噪声转移矩阵。

噪声转移矩阵不容易被准确估计，尤其是当类别数较大时。为了摆脱对噪声转移矩阵的估计，一个有希望的方向是对选定的样本进行训练[17，26，34]。这些工作试图从含噪声的实例中挑选出干净的实例，然后使用它们来更新网络。直观地说，随着训练数据的噪声变得更少，可以获得更好的性能。在这些工作中，具有代表性的方法有MentorNet[17]和Decoupling[26]。

MentorNet[17]预先训练一个额外的网络，然后使用额外的网络来选择干净的实例来指导训练。当没有干净的验证数据时，MentorNet必须使用预定义的课程(curriculum, 指导)(例如，self-paced curriculum)。然而，self-paced MentorNet的想法类似于self-training方法[6]，它继承了由于样本选择偏差而导致的累积误差的相同劣势。

Decoupling[26]同时训练两个网络，然后只使用从这两个网络具有不同预测的实例来更新模型。尽管如此，噪声标签均匀地分布在整个示例空间中。因此，不一致区域包括多个噪声标签，其中Decoupling方法不能显式地处理噪声标签。虽然MentorNet和Decoupling是这一方向的代表性方法，但仍然存在上述讨论的问题，这自然促使我们在研究中对其进行改进。

同时，对深层模型的一个有趣的观察是，它们可以首先记忆容易的实例，并随着训练周期的增加而逐渐适应困难的实例[2]。当存在噪声标签时，深度学习模型最终会记住这些错误给定的标签[45]，从而导致泛化性能较差。此外，这种现象不会随着训练优化(例如Adagrad[9]和Adam[18])或网络体系结构(例如MLP[15]、Alexnet[20]和Inception[37])[17、45]的选择而改变。

在本文中，我们提出了一种简单但有效的学习范式，称为“Co-teaching”，它允许我们在具有极高噪声的标签(例如，45%的噪声标签出现在具有多个类的细粒度分类(fine-grained classification)中[8])的情况下稳健地训练深层网络。我们的想法源于Co-training方法[5]。与Decoupling类似，我们的联合教学也同时维持两个网络。尽管如此，值得注意的是，在每个小批量数据中，每个网络都将其小损失实例(像self-paced MentorNet)视为有用的知识，并将这些有用的实例传授给其对等网络以更新参数。

以下简要解释了为什么Co-teaching可以更强大的直觉想法。在图1中，假设错误流来自对第一个小批量数据中的训练实例的偏向选择。在MentorNet或Decoupling中，来自一个网络的误差会在第二个小批量数据中直接传递到自己身上，并且误差应该越来越累积。然而，在Co-teaching中，由于两个网络具有不同的学习能力，它们可以过滤由噪声标签引入的不同类型的错误。在该交换过程中，可以通过对等网络相互减少误码流。此外，我们使用带动量的stochastic optimization来训练深层网络，而非线性深层网络可以首先记忆干净的数据以变得健壮[2]。当来自噪声数据的错误流进入对等网络时，由于其健壮性，它将减弱这种错误。我们在噪声版本的MNIST、CIFAR-10和CIFAR-100数据集上进行了实验。实验结果表明，在极端噪声环境下(即45%的噪声标签)，Co-teaching方法训练的深度学习模型的稳健性远远优于最新的基线。在低水平噪声环境下(即20%的噪声标签)，通过训练深度学习模型的稳健性.

统计学习方法。

统计学习对噪声标签问题的解决起到了很大作用，尤其是在理论方面。该方法可以分为三个方面：代理损失(surrogate loss)、噪声率估计(noise rate estimation)和概率建模(probabilistic modeling)。

在代理损失(surrogate losses)类别中，Natarajan等人。[30]提出了一种无偏估计器，以提供噪声校正损失方法。

Masnadi-Shirazi等人。[27]给出了一类稳健非凸损失，这是一类稳健损失的特例。

在噪声率估计类别中，两个Menon等人。[28]和刘等人。[23]提出了一种基于分数区间顺序统计量的类概率估计器。

Sanderson等人的研究成果。[36]使用ROC曲线的斜率给出了相同的估计值。

在概率建模类别中，Raykar等人。[32]提出了一种two-coin模型来处理来自多个注释器的噪声标签。

严等人。[42]通过设置与实例相关联的动态翻转概率，扩展了该two-coin模型。

其他深度学习方法。此外，还有一些其他深度学习解决方案来处理噪音标签[24，41]。

Li等人。[22]提出了一个从干净标签和知识图中提取知识的统一框架，该框架可用于从噪声标签中学习更好的模型。Veit等人。

[40]利用一组清洁标签训练了一个标签清洗网络，并利用该网络降低了大规模噪声标签中的噪声。Tanaka等人。

[38]提出了一种同时学习参数和估计真实标签的联合优化框架。勒恩等人。

[34]利用额外的验证集自适应地为每次迭代中的训练样本分配权重。

Rodrigues et al.。[35]在来自多个注释器的噪波标签的输出层之后添加了群组层。但是，所有方法都需要额外的资源或更复杂的网络。

Learning to teach 方法。Learning-to-teach也是一个热门话题。受[16]启发，这些方法由teacher和student网络组成。教师网络的职责是选择更多的信息实例，以便更好地训练student网络。最近，这种思想被应用于为训练数据[10]学习适当的课程，并处理多标签[14]。然而，这些工作没有考虑噪声标签，MentorNet[17]将这一想法引入了这一领域。

Co-teaching

![]({23}_Co-teaching_%20Robust%20Training%20of%20Deep%20Neural%20Networks%20with%20Extremely%20Noisy%20Labels@hanCoteachingRobustTraining2018.assets/image-20220531124714.png)

我们的想法是**同时**训练两个深层网络。如上图所示，在每个小批量数据中，每个网络选择自己的小损失实例作为有用的知识，并将这些有用的实例传授给其对等网络以供进一步训练。因此，该算法被命名为Co-teaching(算法1)。由于所有深度学习训练方法都是基于随机梯度下降的，所以我们的Co-teaching是以小批量的方式进行的。具体地说，我们维护两个网络f(参数为wf)和g(参数为wg)。当形成小批量数据$\overline{\mathcal{D}}$时(步骤3)，我们首先让网络f(或g)在此小批量数据$\overline{\mathcal{D}}$中选择出训练损失较小的一小部分实例$\overline{\mathcal{D}}_{f}$(或$\overline{\mathcal{D}}_{g}$)(步骤4和5)。实例数由R(T)和网络f(g)控制, 即仅从小批量中选择这个网络中计算得到的损失小于R(T)的实例。然后，将选择出的实例作为用于参数更新的有用知识, 馈送到其另一个网络中(步骤6和7)。

设计上述算法有两个重要的问题：

Q1。为什么基于动态R(T)的抽样小损失实例可以帮助我们找到干净的实例？

Q2.。为什么我们需要两个网络并交叉更新参数？

要回答第一个问题，我们首先需要说明小损失和干净实例之间的联系。直观地说，当标签正确时，小损失实例更有可能是正确标签的实例。因此，如果我们只使用每个Mini-Bach数据中的小损失实例来训练我们的分类器，它应该对噪声标签具有抵抗力。然而，以上要求分类器足够可靠，以便小损失实例确实是干净的。深层网络的“记忆”效应正好可以帮助我们解决这个问题[2]。也就是说，在有噪声的数据集上，即使存在有噪声的标签，深度网络也会在初始迭代[45，2]中学习干净而容易的数据。因此，它们有能力在训练开始时使用它们的损失值来过滤噪声实例。然而，问题是，当纪元的数量变得很大时，它们最终会超出噪声标签。为了纠正这个问题，我们希望在开始时在小批量中保留更多的实例，即R(T)很大。然后，我们逐渐提高丢失率，即R(T)变得更小，这样我们就可以保持干净的实例，并在我们的网络记住它们之前丢弃那些有噪声的实例(R(T)的细节将在4.2节讨论)。基于这种思想，我们可以在算法1中只使用一个网络，让分类器自动进化。这个过程类似于boosting[11]和active learning[7]。然而，众所周知，boosting和active learning对离群点和噪声很敏感，少数错误选择的实例会恶化整个模型的学习性能[12，3]。这与我们的第二个问题有关，其中两个量词可以提供帮助。直观地说，不同的分类器可以产生不同的决策边界，从而具有不同的学习能力。因此，在对噪声标签进行训练时，我们也期望它们能够具有不同的过滤标签噪声的能力。这促使我们交换所选的小损失实例，即使用选自g(f)的数据更新f(g)。这个过程类似于Co-training[5]，如果选择的实例不是完全干净的，这两个网络将自适应地纠正对等网络的训练错误。以“同行评议”为例予以支持。当学生检查自己的试卷时，他们很难发现任何错误或错误，因为他们对答案有一些个人偏见。幸运的是，他们可以要求同班同学复习他们的论文。然后，他们就更容易找到自己的潜在缺陷了。综上所述，由于来自一个网络的错误本身不会被直接传回，我们可以预期我们的Co-teaching方法比自我进化的方法可以处理更大的噪声。

与Co-training的关系。虽然Co-teaching是由Co-training推动的，但唯一的相似之处是训练了两个分类器。它们之间存在着根本性的区别。(I)。Co-training需要两个观点(两套独立的特征集)，而联合教学需要一个单一的观点。(2)Co-training没有利用深层神经网络的记忆，而联合教学则利用了深层神经网络的记忆。(Iii)Co-training是为半监督学习而设计的，Co-teaching是为有噪音标签的学习而设计的；由于噪音标签学习并不是半监督学习的特例，我们不能简单地将协同训练从一个问题背景转换到另一个问题背景。


为了进行公平的比较，我们用PyTorch实现了所有带有默认参数的方法，并在NIVIDIA K80图形处理器上进行了所有的实验。CNN与Leaky-relu(LReLU)主动函数一起使用[25]，详细结构如表所示。

![]({23}_Co-teaching_%20Robust%20Training%20of%20Deep%20Neural%20Networks%20with%20Extremely%20Noisy%20Labels@hanCoteachingRobustTraining2018.assets/image-20220531154133.png)

也就是说，本文中的9层CNN结构遵循“时间集成(Temporal Ensembling)”[21]和“虚拟对抗训练(Virtual Adversarial Training)[29]，因为我们使用的网络结构是弱监督学习的标准试验床。对于所有实验，ADAM优化器(Momentum=0.9)的初始学习率为0.001，batch大小设置为128，我们运行200个epoch。此外，还使用了dropout和batchNormal方法。由于深层网络是高度非凸的，即使采用相同的网络和优化方法，不同的初始化也会导致不同的局部最优。因此，与[26]相似，我们还将具有相同体系结构但不同初始化的两个网络作为两个分类器。

这里，我们假设噪声限制是已知的，并且设置R(T)=1−τ·min(T/Tk，1)，其中Tk=10，τ=。如果在高级时未知，可以使用验证集[23，43]来推断。第4.2节分析了R(T)和τ的选择。


基于上述原理，为了说明R（T）的衰变如何影响共同教学，首先，我们令$R(T) = 1-\tau \cdot \min \left\{T^{c} / T_{k}, 1\right\}\text { with } \tau=\epsilon$，其中c有三个选择，即$c=\{0.5,1,2\}$,以及三个Tk值，即$T_{k}=\{5,10,15\}$。如果$\epsilon$在advanced中未知，则可以使用验证集推断[23,43]。为了显示τ的影响，我们改变$\tau=\{0.5,0.75,1,1.25,1.5\} \epsilon$。请注意，τ不能为零。在这种情况下，不会反向传播，优化将停止。

### 引文

## 摘录
