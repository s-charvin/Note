---
title: "Training Sample Selection Strategy Applied to CNN in Magneto-Thermal Coupled Analysis"
description: ""
citekey: gongTrainingSampleSelection2021
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-03-12 15:50:47
lastmod: 2023-03-13 15:34:14
---

> [!info] 论文信息
>1. Title：Training Sample Selection Strategy Applied to CNN in Magneto-Thermal Coupled Analysis
>2. Author：Ruohan Gong, Zuqi Tang
>3. Entry：[Zotero link](zotero://select/items/@gongTrainingSampleSelection2021) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Gong_Tang_2021_Training Sample Selection Strategy Applied to CNN in Magneto-Thermal Coupled.pdf>)
>4. Other：2021 - IEEE Transactions on Magnetics     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 

## 摘要

> [!abstract] Deep learning (DL) has attracted more and more attention in computational electromagnetism. Particularly, the convolutional neural network (CNN) is one of the most popular learning models in深度学习due to its excellent capacity for feature extraction and convergence. The efficiency of CNN mainly depends on how many training samples are needed to effectively converge the network. The sample preparation process often involves a lot of numerical computations, which can be very expensive and time-consuming. In this article, based on the traditional深度学习network training procedure, two different approaches, namely adding smart training samples and reference samples, are proposed to help the深度学习network converge. The smart sample selection is based on a greedy algorithm, which can be applied for both training and reference samples. The influences of these two approaches on the CNN training process are investigated by an example of the coupled magneto-thermal computation applied to a transformer. Numerical results show that the two proposed approaches can significantly help the network to converge and improve the efficiency of the深度学习model.

> 深度学习 (DL) 在电磁学计算领域引起了越来越多的关注。特别是，卷积神经网络 (CNN) 是深度学习中最流行的学习模型之一，因为它具有出色的特征提取和收敛能力。 CNN 的效率主要取决于有效收敛网络需要多少训练样本。这些样本的制作过程通常涉及大量数值计算，这可能非常昂贵且耗时。在本文中，基于传统的深度学习网络训练过程，提出了两种不同的方法，即添加智能训练样本和参考样本，以帮助深度学习网络更好的收敛。智能样本选择基于贪心算法，可应用于训练样本和参考样本。本文通过基于 transformer 的耦合磁热计算任务, 研究了这两种方法对 CNN 训练过程的影响。数值结果表明，所提出的两种方法可以显著的帮助网络收敛并提高深度学习模型的训练效率。

## 预处理

## 概述

## 结果

## 精读

在过去的十年中，虽然目前还没有针对深度学习的坚实理论框架，但随着其理论和基础的不断进步，它已经发展成为了一种非常强大的工具，可以从根本上提高我们开展科学研究的能力 [1]，[2]。特别是，卷积神经网络 (CNN) 因其优秀的特征建模能力, 而获得了极大广泛的应用，尤其是在计算机视觉领域 [3]。此外, 在电磁学计算领域，通过引入 CNN 与图像处理相结合的理论, 也取得了一些不错的效果。正如最近在 [4] 中报道的那样，贝叶斯 CNN 可以被用来评估电磁设备的磁场计算。 [5] 报道了 CNN 在加速内置式永磁电机拓扑优化方面的另一种应用。尽管到目前为止，深度学习在很多领域都取得了不错的成绩，但是，深度学习网络要获得优秀的准确性和可重复性，仍然有两个重要的前提常常被忽视，即一组合适的超参数和足够大的训练数据库。研究人员往往重点关注网络在收敛后能获得多好的学习效果，而很少对这两个对网络训练过程至关重要的先决条件进行详细研究。通过将 CNN 应用于耦合磁热计算，我们之前的工作 [6] 已经详细讨论了网络超参数问题并提出了一组基线模型。本文的工作通过采用与 [6] 中所示相同的 CNN 架构和超参数，集中研究训练样本选择策略对训练过程的影响。众所周知，深度学习模型往往需要一定数量的训练样本才能训练出理想的网络。一般来说，正如我们之前的工作所观察到的，CNN 网络通常需要大约 30%–40% 的数据库来有效地训练深度学习模型，这对于复杂的数值模型来说, 数据成本非常高。一般来说，在深度学习网络训练过程中最繁琐、最耗时、最费力的部分是获取足够大的数据库。我们这里的动机就是让深度学习的网络所需的数据集尽可能小，这是进一步提高深度学习效率的关键。为此，我们提出了两种不同的方法来帮助深度学习网络在提供的小型数据库中更好的收敛，即添加智能训练样本和参考样本。受[7]和[8]中这些想法的启发，引入了一种贪心算法来控制训练样本和参考样本的选择过程。保持数据库和 CNN 模型的超参数和架构不变，研究了不同样本选择方法对模型训练效果的影响。以基于 transformer 的耦合磁热计算任务为例进行了效果验证实验。结果表明，本文所提出的方法可以在训练数据集尽可能小的情况下显着提高 CNN U-net 的性能，从而提高深度学习的效率。


CNN U-Net


Unlike traditional computer vision problems that have no rules that can be formulated and summarized such as face recognition, satellite identification, etc. Problems in the field of electrical engineering are physics-based, which means that their behaviors are subject to strict physical rules. There are close relationships between the physical parameters and the corresponding field distribution. Hence, we can often have a rough vague expectation as a priori information before the result comes out. All these aprioriinformation can help us to complete the network training more efficiently. We adopt the CNN U-net to estimate the coupled magneto-thermal problem, the workflow is described in Fig. 1. In the following, the learning procedure is discussed for the magnetic field distribution, while it is basically the same for the temperature field distribution.
不同于人脸识别、卫星识别等传统计算机视觉问题, 无法制定和概括具体的规则，电气工程领域的问题均是基于自然中的物理规则的，这意味着它们的表现也受制于严格的物理规则。物理参数与相应的场分布之间存在密切关系。因此，在结果出来之前，我们往往可以有一个粗略的模糊预期作为先验信息。所有这些先验信息都可以帮助我们更高效地完成网络训练。我们采用 CNN U-net 来估计耦合磁热问题，工作流程如下图所示。下面讨论磁场分布的学习过程，而温度场基本相同分配。


![]({}_Training%20Sample%20Selection%20Strategy%20Applied%20to%20CNN%20in%20Magneto-Thermal%20Coupled%20Analysis@gongTrainingSampleSelection2021.assets/image-20230313150837.png)



To begin with, 900 samples of magnetic flux density distributions are obtained through finite element method (FEM) computations, which are displayed via 256 × 256 × 3redgreen-blue (RGB) images, and employed as the database for DL. Label these samples according to their geometric parameters for the up-coming supervised learning. The 900 labeled samples were divided into ten groups from #0 to #9, with 90 samples in each group. We randomly choose one group as the target sample, which will not be adopted as the input in the training process. Target samples are employed to validate the network during the training process and update the weight of the network according to the gradient descent algorithm and backpropagation of the error. In addition, test samples are introduced to verify the trained network posteriorly. It should be mentioned here that the capability of the interpolation is evaluated when the test samples are inside the target samples. On the other hand, the capacity of extrapolation is evaluated when the test samples are outside the target.

首先，通过有限元法 (FEM) 计算获得了900个磁通密度分布样本，这些样本以 256×256×3（RGB）图像的形式展示，并用作深度学习训练的数据库。根据它们的几何参数为这些样本进行标记，以备接下来的监督学习任务。这 900 个标记样本被分成了十组，编号为 `#0` 至 `#9` ，每组有 90 个样本。我们随机选择一组作为目标样本( target sample )，该组样本不会在训练过程中作为输入, 只会被用于在训练过程中验证网络效果，并根据梯度下降算法和误差反向传播更新网络的权重。此外，引入测试样本 (test sample) 以验证训练后的网络。值得注意的是，当测试样本在目标样本 ( target sample ) 内部时，将评估插值的能力。另一方面，当测试样本在目标样本 ( target sample ) 外部时，将评估外推的能力。

In our previous work [6], only the training samples are utilized in the training process. The input is the Gaussian distribution that contains the label information and the output is the corresponding field distribution. In this work, firstly, an approach is proposed to improve the network performance by increasing some smart training samples. Besides, a new concept named reference samples is introduced. As the name implies, it is the reference information introduced to the model during the DL process, which is our vague expectation of the approximate distribution of the target output. It participates in the process of network training together with training samples to reform the input image. But, different from regular training samples, which are only computed once in a whole epoch, the references will be computed once in each batch, and there may be lots of batches in one epoch. What is more, only the label information are taken from training samples as the input for the network, as for reference samples, the whole field distribution will be taken into consideration and combined with training sample label information as the new input for the network. In addition, the introduction of reference requires us to change the architecture because they will change the structure of input information. On the other hand, no matter how many training samples we use, the architecture of the network remains the same. Adopt the network architecture and the baseline set of hyperparameters obtained in [6]; the network was adjusted so that it can accept more reference samples as input. Besides, more attention has been paid to adjusting the structure of the input image, as shown in Fig. 1, which is composed of the Gaussian distribution containing the training sample label information and the entire field distribution of the reference sample.

在我们之前的工作[6]中，训练过程中只使用训练样本。输入是包含标签信息的高斯分布，输出是对应的场分布。在这项工作中，首先，提出了一种通过增加一些智能训练样本来提高网络性能的方法。此外，引入了一个名为参考样本的新概念。顾名思义，就是深度学习过程中引入模型的参考信息，也就是我们对目标输出的大概分布的模糊预期。它与训练样本一起参与网络训练过程，对输入图像进行改造。但是，与常规训练样本在整个 epoch 中只计算一次不同，参考样本将在每个 batch 中计算一次，并且在一个 epoch 中可能有很多 batches。并且，仅将训练样本中的标签信息作为网络的输入，对于参考样本，将考虑整个场分布并结合训练样本标签信息作为网络的新输入。此外，参考样本的引入需要我们改变架构，因为它们会改变输入信息的结构。另一方面，无论我们使用多少训练样本，网络的架构都保持不变。采用[6]中获得的网络架构和基线超参数集；调整了网络，使其可以接受更多参考样本作为输入。此外，更加注意调整输入图像的结构，如图所示，它由包含训练样本标签信息的高斯分布和参考样本的整个场分布组成。


Greedy Algorithm


The above sample selection strategy is realized via a greedy algorithm. A greedy algorithm is an approach that follows the problem-solving heuristic of making the optimal choice at each step as it tries to find the overall optimal solution to the entire problem. It cannot guarantee the optimal solution, but can provide a possible “best” choice [7].


Results and Discussion


The above-mentioned transformer coupled magneto-thermal problem is solved by the FEM, which is realized by the free scientific computing software of Freefem++ [10], [11]. These FEM results constitute the database in the upcoming深度学习process. Too few training samples may cause the network to diverge, as the black lines plotted in Fig. 2 for both magnetic and temperature fields. Two proposed approaches are put forward to help the network converge: increase training samples to the network (respectively, add the special reference samples in the network) to improve the stability as well as the convergence of the network. The training and reference samples are selected by our presented greedy algorithm. To clearly represent the influence of sample selection strategy, a random selection is performed to each approach for comparison, as shown in Fig. 2. It can be observed that for both training samples and reference samples, the selection strategy based on the greedy algorithm has significant advantages. It should be mentioned here, each number for training samples stands for a group, which contains 90 training samples. On the other hand, for reference samples, each number stands for only one single reference sample. Consistent with our previous research experience, due to the continuity of the magnetic flux density distribution, there are strong connectivities between pixels in the magnetic field images, which makes the magnetic flux density distribution easier to learn. On the other hand, since we are only concerned about the temperature nearby the windings and insulations, there are relatively large gradient gaps between insulation and air, which makes the distribution of the temperature field more difficult to learn. For both magnetic field and temperature field prediction, increasing training samples can greatly improve the accuracy and convergence of the model, but correspondingly, more training samples are required. Specifically, 90 more training samples should be prepared for both magnetic and temperature fields. By contrast, the introduction of reference samples in the network can also improve the convergence, although its effect may not be as good as training samples, the cost is much less. The convergence can be achieved much faster even with several reference samples in comparison with the original case. In practice, a trade-off needs to be considered between model performance and computational burden.

The successfully trained CNN model can be used to predict the distribution of the magnetic field and temperature field with different geometry parameters, as, respectively, shown in Fig. 3(a) and (b). One group, that is, 90 samples can be output online within 20 s on NVIDIA GTX 1080 8-GB GPU once the model has been successfully trained.

The purpose of this article is to explore the feasibility of using深度学习to solve the coupled magneto-thermal problem with a training sample set as small as possible, which is the key to improve the efficiency of DL. To achieve this goal, based on the conventional深度学习network training procedure, two different approaches, namely adding smart training samples and reference samples, are proposed to help the深度学习network converge. Besides, a smart sample selection strategy based on the greedy algorithm is put forward to govern the selection process of both training samples and reference samples. Keeping the database and the hyperparameters and architecture of the CNN model remain unchanged, the influence of different sample selection approaches are investigated. Taking a typical transformer as an example, numerical experiments are performed. The results illustrate that the proposed method can effectively help the network converge and significantly improve the efficiency of the深度学习network. More training samples were involved in the training process; more stable and faster the model converges, but it comes with more computational burdens. By contrast, the introduction of reference samples can help the network to converge with much less cost.

### 引文

## 摘录
