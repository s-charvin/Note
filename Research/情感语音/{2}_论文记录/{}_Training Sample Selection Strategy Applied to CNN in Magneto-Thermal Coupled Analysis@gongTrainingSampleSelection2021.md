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
lastmod: 2023-03-13 14:28:57
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

> [!abstract] Deep learning (DL) has attracted more and more attention in computational electromagnetism. Particularly, the convolutional neural network (CNN) is one of the most popular learning models in DL due to its excellent capacity for feature extraction and convergence. The efficiency of CNN mainly depends on how many training samples are needed to effectively converge the network. The sample preparation process often involves a lot of numerical computations, which can be very expensive and time-consuming. In this article, based on the traditional DL network training procedure, two different approaches, namely adding smart training samples and reference samples, are proposed to help the DL network converge. The smart sample selection is based on a greedy algorithm, which can be applied for both training and reference samples. The influences of these two approaches on the CNN training process are investigated by an example of the coupled magneto-thermal computation applied to a transformer. Numerical results show that the two proposed approaches can significantly help the network to converge and improve the efficiency of the DL model.

> 深度学习 (DL) 在电磁学计算领域引起了越来越多的关注。特别是，卷积神经网络 (CNN) 是深度学习中最流行的学习模型之一，因为它具有出色的特征提取和收敛能力。 CNN 的效率主要取决于有效收敛网络需要多少训练样本。这些样本的制作过程通常涉及大量数值计算，这可能非常昂贵且耗时。在本文中，基于传统的深度学习网络训练过程，提出了两种不同的方法，即添加智能训练样本和参考样本，以帮助深度学习网络更好的收敛。智能样本选择基于贪心算法，可应用于训练样本和参考样本。本文通过基于 transformer 的耦合磁热计算任务, 研究了这两种方法对 CNN 训练过程的影响。数值结果表明，所提出的两种方法可以显著的帮助网络收敛并提高深度学习模型的训练效率。


## 预处理

## 概述

## 结果

## 精读

OVER the last decade, although there is still no solid theoretical framework for DL right now, it has become an unprecedented tool that can essentially improve our capability to carry out scientific research due to advances in theory and infrastructure [1], [2]. Particularly, convolutional neural network (CNN) has gained tremendous popularity and has been widely used because of its capacity to automatically execute feature engineering on its own, especially when it comes to computer vision [3]. In the field of computational electromagnetic, CNN combined with image processing has attracted lots of attention and achieved some good results. As recently reported in [4], Bayesian CNN is used to evaluate the magnetic field computation of electromagnetic devices. Another application of CNN to accelerate the topology optimization of interior permanent magnet motor is reported in [5]. Even though DL has achieved some good performances in lots of fields so far, however, there are still two important premises for a DL network to achieve good accuracy and reproducibility that are often overlooked, namely a proper set of hyperparameters and a sufficient training database. Researchers often tend to pay attention to what kind of learning effect a network can get after convergence, but rarely conduct detailed studies on these two prerequisites that are crucial to the network training procedure. The hyperparameter issue has been detailed discussed and a set of baseline model has been proposed in our previous work [6] via the application of CNN in the coupled magneto-thermal computation. This work concentrates on the impact of sample selection strategy on the training process by adopting the same CNN architecture and hyperparameters as illustrated in [6]. It is well known that DL needs a certain amount of training samples to obtain the ideal trained network. Generally speaking, as observed in our previous work, the CNN usually takes about 30%–40% of the database to effectively train the DL model, which is still expensive when it comes to a complex numerical model. In general, in comparison with the DL network training process, the most tedious, time-consuming, and laborious part of the DL procedure is to obtain a sufficient database. Our motivation here is to have a data set as small as possible, which is the key to further improve the efficiency of DL. For this purpose, we propose two different approaches to help the DL network converge with a small database, namely adding smart training samples and reference samples. Inspired by these ideas in [7] and [8], a greedy algorithm is introduced to govern the selection procedure for the training samples and reference samples. Keeping the database and the hyperparameters and architecture of the CNN model remain unchanged, the influence of different sample selection approaches is investigated. The numerical experiments are conducted using the transformer coupled magnetic-thermal problem as an example. Results illustrate that proposed approaches can significantly improve the performance of the CNN U-net with a training data set as small as possible, hence improve the efficiency of the DL.

CNN U-Net


Unlike traditional computer vision problems that have no rules that can be formulated and summarized such as face recognition, satellite identification, etc. Problems in the field of electrical engineering are physics-based, which means that their behaviors are subject to strict physical rules. There are close relationships between the physical parameters and the corresponding field distribution. Hence, we can often have a rough vague expectation as a priori information before the result comes out. All these aprioriinformation can help us to complete the network training more efficiently. We adopt the CNN U-net to estimate the coupled magneto-thermal problem, the workflow is described in Fig. 1. In the following, the learning procedure is discussed for the magnetic field distribution, while it is basically the same for the temperature field distribution.

To begin with, 900 samples of magnetic flux density distributions are obtained through finite element method (FEM) computations, which are displayed via 256 × 256 × 3redgreen-blue (RGB) images, and employed as the database for DL. Label these samples according to their geometric parameters for the up-coming supervised learning. The 900 labeled samples were divided into ten groups from #0 to #9, with 90 samples in each group. We randomly choose one group as the target sample, which will not be adopted as the input in the training process. Target samples are employed to validate the network during the training process and update the weight of the network according to the gradient descent algorithm and backpropagation of the error. In addition, test samples are introduced to verify the trained network posteriorly. It should be mentioned here that the capability of the interpolation is evaluated when the test samples are inside the target samples. On the other hand, the capacity of extrapolation is evaluated when the test samples are outside the target.

In our previous work [6], only the training samples are utilized in the training process. The input is the Gaussian distribution that contains the label information and the output is the corresponding field distribution. In this work, firstly, an approach is proposed to improve the network performance by increasing some smart training samples. Besides, a new concept named reference samples is introduced. As the name implies, it is the reference information introduced to the model during the DL process, which is our vague expectation of the approximate distribution of the target output. It participates in the process of network training together with training samples to reform the input image. But, different from regular training samples, which are only computed once in a whole epoch, the references will be computed once in each batch, and there may be lots of batches in one epoch. What is more, only the label information are taken from training samples as the input for the network, as for reference samples, the whole field distribution will be taken into consideration and combined with training sample label information as the new input for the network. In addition, the introduction of reference requires us to change the architecture because they will change the structure of input information. On the other hand, no matter how many training samples we use, the architecture of the network remains the same. Adopt the network architecture and the baseline set of hyperparameters obtained in [6]; the network was adjusted so that it can accept more reference samples as input. Besides, more attention has been paid to adjusting the structure of the input image, as shown in Fig. 1, which is composed of the Gaussian distribution containing the training sample label information and the entire field distribution of the reference sample.

Greedy Algorithm


The above sample selection strategy is realized via a greedy algorithm. A greedy algorithm is an approach that follows the problem-solving heuristic of making the optimal choice at each step as it tries to find the overall optimal solution to the entire problem. It cannot guarantee the optimal solution, but can provide a possible “best” choice [7].








### 引文

## 摘录
