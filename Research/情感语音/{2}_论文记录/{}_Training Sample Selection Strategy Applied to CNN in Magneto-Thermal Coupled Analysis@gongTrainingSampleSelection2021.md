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
lastmod: 2023-03-13 14:36:33
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

OVER the last decade, although there is still no solid theoretical framework for深度学习right now, it has become an unprecedented tool that can essentially improve our capability to carry out scientific research due to advances in theory and infrastructure [1], [2]. Particularly, convolutional neural network (CNN) has gained tremendous popularity and has been widely used because of its capacity to automatically execute feature engineering on its own, especially when it comes to computer vision [3]. In the field of computational electromagnetic, CNN combined with image processing has attracted lots of attention and achieved some good results. As recently reported in [4], Bayesian CNN is used to evaluate the magnetic field computation of electromagnetic devices. Another application of CNN to accelerate the topology optimization of interior permanent magnet motor is reported in [5]. Even though深度学习has achieved some good performances in lots of fields so far, however, there are still two important premises for a深度学习network to achieve good accuracy and reproducibility that are often overlooked, namely a proper set of hyperparameters and a sufficient training database. Researchers often tend to pay attention to what kind of learning effect a network can get after convergence, but rarely conduct detailed studies on these two prerequisites that are crucial to the network training procedure. The hyperparameter issue has been detailed discussed and a set of baseline model has been proposed in our previous work [6] via the application of CNN in the coupled magneto-thermal computation. This work concentrates on the impact of sample selection strategy on the training process by adopting the same CNN architecture and hyperparameters as illustrated in [6]. It is well known that深度学习needs a certain amount of training samples to obtain the ideal trained network. Generally speaking, as observed in our previous work, the CNN usually takes about 30%–40% of the database to effectively train the深度学习model, which is still expensive when it comes to a complex numerical model. In general, in comparison with the深度学习network training process, the most tedious, time-consuming, and laborious part of the深度学习procedure is to obtain a sufficient database. Our motivation here is to have a data set as small as possible, which is the key to further improve the efficiency of DL. For this purpose, we propose two different approaches to help the深度学习network converge with a small database, namely adding smart training samples and reference samples. Inspired by these ideas in [7] and [8], a greedy algorithm is introduced to govern the selection procedure for the training samples and reference samples. Keeping the database and the hyperparameters and architecture of the CNN model remain unchanged, the influence of different sample selection approaches is investigated. The numerical experiments are conducted using the transformer coupled magnetic-thermal problem as an example. Results illustrate that proposed approaches can significantly improve the performance of the CNN U-net with a training data set as small as possible, hence improve the efficiency of the DL.


在过去的十年中，虽然目前还没有针对深度学习的坚实理论框架，但随着其理论和基础的不断进步，它已经发展成为了一种非常强大的工具，可以从根本上提高我们开展科学研究的能力 [1]，[2]。特别是，卷积神经网络 (CNN) 因其优秀的特征建模能力, 而获得了极大广泛的应用，尤其是在计算机视觉领域 [3]。此外, 在电磁学计算领域，通过引入 CNN 与图像处理相结合的理论, 也取得了一些不错的效果。正如最近在 [4] 中报道的那样，贝叶斯 CNN 可以被用来评估电磁设备的磁场计算。 [5] 报道了 CNN 在加速内置式永磁电机拓扑优化方面的另一种应用。尽管到目前为止，深度学习在很多领域都取得了不错的成绩，但是，深度学习网络要获得优秀的准确性和可重复性，仍然有两个重要的前提常常被忽视，即一组合适的超参数和足够大的训练数据库。研究人员往往重点关注网络在收敛后能获得多好的学习效果，而很少对这两个对网络训练过程至关重要的先决条件进行详细研究。通过将 CNN 应用于耦合磁热计算，我们之前的工作 [6] 已经详细讨论了网络超参数问题并提出了一组基线模型。本文的工作通过采用与 [6] 中所示相同的 CNN 架构和超参数，集中研究训练样本选择策略对训练过程的影响。众所周知，深度学习模型往往需要一定数量的训练样本才能训练出理想的网络。一般来说，正如我们之前的工作所观察到的，CNN 网络通常需要大约 30%–40% 的数据库来有效地训练深度学习模型，这对于复杂的数值模型来说, 数据成本非常高。一般来说，在深度学习网络训练过程中最繁琐、最耗时、最费力的部分是获取足够大的数据库。我们这里的动机就是让深度学习的网络所需的数据集尽可能小，这是进一步提高深度学习效率的关键。为此，我们提出了两种不同的方法来帮助深度学习网络在提供的小型数据库中更好的收敛，即添加智能训练样本和参考样本。受[7]和[8]中这些想法的启发，引入了一种贪心算法来控制训练样本和参考样本的选择过程。保持数据库和 CNN 模型的超参数和架构不变，研究了不同样本选择方法对模型训练效果的影响。以基于 transformer 的耦合磁热ji问题为例进行了数值实验。结果表明，所提出的方法可以在训练数据集尽可能小的情况下显着提高 CNN U-net 的性能，从而提高深度学习的效率。


CNN U-Net


Unlike traditional computer vision problems that have no rules that can be formulated and summarized such as face recognition, satellite identification, etc. Problems in the field of electrical engineering are physics-based, which means that their behaviors are subject to strict physical rules. There are close relationships between the physical parameters and the corresponding field distribution. Hence, we can often have a rough vague expectation as a priori information before the result comes out. All these aprioriinformation can help us to complete the network training more efficiently. We adopt the CNN U-net to estimate the coupled magneto-thermal problem, the workflow is described in Fig. 1. In the following, the learning procedure is discussed for the magnetic field distribution, while it is basically the same for the temperature field distribution.

To begin with, 900 samples of magnetic flux density distributions are obtained through finite element method (FEM) computations, which are displayed via 256 × 256 × 3redgreen-blue (RGB) images, and employed as the database for DL. Label these samples according to their geometric parameters for the up-coming supervised learning. The 900 labeled samples were divided into ten groups from #0 to #9, with 90 samples in each group. We randomly choose one group as the target sample, which will not be adopted as the input in the training process. Target samples are employed to validate the network during the training process and update the weight of the network according to the gradient descent algorithm and backpropagation of the error. In addition, test samples are introduced to verify the trained network posteriorly. It should be mentioned here that the capability of the interpolation is evaluated when the test samples are inside the target samples. On the other hand, the capacity of extrapolation is evaluated when the test samples are outside the target.

In our previous work [6], only the training samples are utilized in the training process. The input is the Gaussian distribution that contains the label information and the output is the corresponding field distribution. In this work, firstly, an approach is proposed to improve the network performance by increasing some smart training samples. Besides, a new concept named reference samples is introduced. As the name implies, it is the reference information introduced to the model during the深度学习process, which is our vague expectation of the approximate distribution of the target output. It participates in the process of network training together with training samples to reform the input image. But, different from regular training samples, which are only computed once in a whole epoch, the references will be computed once in each batch, and there may be lots of batches in one epoch. What is more, only the label information are taken from training samples as the input for the network, as for reference samples, the whole field distribution will be taken into consideration and combined with training sample label information as the new input for the network. In addition, the introduction of reference requires us to change the architecture because they will change the structure of input information. On the other hand, no matter how many training samples we use, the architecture of the network remains the same. Adopt the network architecture and the baseline set of hyperparameters obtained in [6]; the network was adjusted so that it can accept more reference samples as input. Besides, more attention has been paid to adjusting the structure of the input image, as shown in Fig. 1, which is composed of the Gaussian distribution containing the training sample label information and the entire field distribution of the reference sample.

Greedy Algorithm


The above sample selection strategy is realized via a greedy algorithm. A greedy algorithm is an approach that follows the problem-solving heuristic of making the optimal choice at each step as it tries to find the overall optimal solution to the entire problem. It cannot guarantee the optimal solution, but can provide a possible “best” choice [7].


Results and Discussion


The above-mentioned transformer coupled magneto-thermal problem is solved by the FEM, which is realized by the free scientific computing software of Freefem++ [10], [11]. These FEM results constitute the database in the upcoming深度学习process. Too few training samples may cause the network to diverge, as the black lines plotted in Fig. 2 for both magnetic and temperature fields. Two proposed approaches are put forward to help the network converge: increase training samples to the network (respectively, add the special reference samples in the network) to improve the stability as well as the convergence of the network. The training and reference samples are selected by our presented greedy algorithm. To clearly represent the influence of sample selection strategy, a random selection is performed to each approach for comparison, as shown in Fig. 2. It can be observed that for both training samples and reference samples, the selection strategy based on the greedy algorithm has significant advantages. It should be mentioned here, each number for training samples stands for a group, which contains 90 training samples. On the other hand, for reference samples, each number stands for only one single reference sample. Consistent with our previous research experience, due to the continuity of the magnetic flux density distribution, there are strong connectivities between pixels in the magnetic field images, which makes the magnetic flux density distribution easier to learn. On the other hand, since we are only concerned about the temperature nearby the windings and insulations, there are relatively large gradient gaps between insulation and air, which makes the distribution of the temperature field more difficult to learn. For both magnetic field and temperature field prediction, increasing training samples can greatly improve the accuracy and convergence of the model, but correspondingly, more training samples are required. Specifically, 90 more training samples should be prepared for both magnetic and temperature fields. By contrast, the introduction of reference samples in the network can also improve the convergence, although its effect may not be as good as training samples, the cost is much less. The convergence can be achieved much faster even with several reference samples in comparison with the original case. In practice, a trade-off needs to be considered between model performance and computational burden.

The successfully trained CNN model can be used to predict the distribution of the magnetic field and temperature field with different geometry parameters, as, respectively, shown in Fig. 3(a) and (b). One group, that is, 90 samples can be output online within 20 s on NVIDIA GTX 1080 8-GB GPU once the model has been successfully trained.

The purpose of this article is to explore the feasibility of using深度学习to solve the coupled magneto-thermal problem with a training sample set as small as possible, which is the key to improve the efficiency of DL. To achieve this goal, based on the conventional深度学习network training procedure, two different approaches, namely adding smart training samples and reference samples, are proposed to help the深度学习network converge. Besides, a smart sample selection strategy based on the greedy algorithm is put forward to govern the selection process of both training samples and reference samples. Keeping the database and the hyperparameters and architecture of the CNN model remain unchanged, the influence of different sample selection approaches are investigated. Taking a typical transformer as an example, numerical experiments are performed. The results illustrate that the proposed method can effectively help the network converge and significantly improve the efficiency of the深度学习network. More training samples were involved in the training process; more stable and faster the model converges, but it comes with more computational burdens. By contrast, the introduction of reference samples can help the network to converge with much less cost.

### 引文

## 摘录
