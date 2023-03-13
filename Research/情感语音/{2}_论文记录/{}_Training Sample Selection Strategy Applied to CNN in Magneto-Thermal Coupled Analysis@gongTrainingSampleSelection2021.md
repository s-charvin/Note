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
lastmod: 2023-03-13 17:05:41
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

### 引言

在过去的十年中，虽然目前还没有针对深度学习的坚实理论框架，但随着其理论和基础的不断进步，它已经发展成为了一种非常强大的工具，可以从根本上提高我们开展科学研究的能力 [1]，[2]。特别是，卷积神经网络 (CNN) 因其优秀的特征建模能力, 而获得了极大广泛的应用，尤其是在计算机视觉领域 [3]。此外, 在电磁学计算领域，通过引入 CNN 与图像处理相结合的理论, 也取得了一些不错的效果。正如最近在 [4] 中报道的那样，贝叶斯 CNN 可以被用来评估电磁设备的磁场计算。 [5] 报道了 CNN 在加速内置式永磁电机拓扑优化方面的另一种应用。尽管到目前为止，深度学习在很多领域都取得了不错的成绩，但是，深度学习网络要获得优秀的准确性和可重复性，仍然有两个重要的前提常常被忽视，即一组合适的超参数和足够大的训练数据库。研究人员往往重点关注网络在收敛后能获得多好的学习效果，而很少对这两个对网络训练过程至关重要的先决条件进行详细研究。通过将 CNN 应用于耦合磁热计算，我们之前的工作 [6] 已经详细讨论了网络超参数问题并提出了一组基线模型。本文的工作通过采用与 [6] 中所示相同的 CNN 架构和超参数，集中研究训练样本选择策略对训练过程的影响。众所周知，深度学习模型往往需要一定数量的训练样本才能训练出理想的网络。一般来说，正如我们之前的工作所观察到的，CNN 网络通常需要大约 30%–40% 的数据库来有效地训练深度学习模型，这对于复杂的数值模型来说, 数据成本非常高。一般来说，在深度学习网络训练过程中最繁琐、最耗时、最费力的部分是获取足够大的数据库。我们这里的动机就是让深度学习的网络所需的数据集尽可能小，这是进一步提高深度学习效率的关键。为此，我们提出了两种不同的方法来帮助深度学习网络在提供的小型数据库中更好的收敛，即添加智能训练样本和参考样本。受[7]和[8]中这些想法的启发，引入了一种贪心算法来控制训练样本和参考样本的选择过程。保持数据库和 CNN 模型的超参数和架构不变，研究了不同样本选择方法对模型训练效果的影响。以基于 transformer 的耦合磁热计算任务为例进行了效果验证实验。结果表明，本文所提出的方法可以在训练数据集尽可能小的情况下显着提高 CNN U-net 的性能，从而提高深度学习的效率。

### 理论与方法

CNN U-Net

Unlike traditional computer vision problems that have no rules that can be formulated and summarized such as face recognition, satellite identification, etc. Problems in the field of electrical engineering are physics-based, which means that their behaviors are subject to strict physical rules. There are close relationships between the physical parameters and the corresponding field distribution. Hence, we can often have a rough vague expectation as a priori information before the result comes out. All these aprioriinformation can help us to complete the network training more efficiently. We adopt the CNN U-net to estimate the coupled magneto-thermal problem, the workflow is described in Fig. 1. In the following, the learning procedure is discussed for the magnetic field distribution, while it is basically the same for the temperature field distribution.
不同于人脸识别、卫星识别等传统计算机视觉问题, 无法制定和概括具体的规则，电气工程领域的问题均是基于自然中的物理规则的，这意味着它们的表现也受制于严格的物理规则。物理参数与相应的场分布之间存在密切关系。因此，在结果出来之前，我们往往可以有一个粗略的模糊预期作为先验信息。所有这些先验信息都可以帮助我们更高效地完成网络训练。我们采用 CNN U-net 来估计耦合磁热问题，工作流程如下图所示。下面讨论磁场分布的学习过程，而温度场基本相同分配。


![]({}_Training%20Sample%20Selection%20Strategy%20Applied%20to%20CNN%20in%20Magneto-Thermal%20Coupled%20Analysis@gongTrainingSampleSelection2021.assets/image-20230313150837.png)



To begin with, 900 samples of magnetic flux density distributions are obtained through finite element method (FEM) computations, which are displayed via 256 × 256 × 3redgreen-blue (RGB) images, and employed as the database for DL. Label these samples according to their geometric parameters for the up-coming supervised learning. The 900 labeled samples were divided into ten groups from #0 to #9, with 90 samples in each group. We randomly choose one group as the target sample, which will not be adopted as the input in the training process. Target samples are employed to validate the network during the training process and update the weight of the network according to the gradient descent algorithm and backpropagation of the error. In addition, test samples are introduced to verify the trained network posteriorly. It should be mentioned here that the capability of the interpolation is evaluated when the test samples are inside the target samples. On the other hand, the capacity of extrapolation is evaluated when the test samples are outside the target.

首先，通过有限元法 (FEM) 计算获得了900个磁通密度分布样本，这些样本以 256×256×3（RGB）图像的形式展示，并用作深度学习训练的数据库。根据它们的几何参数为这些样本进行标记，以备接下来的监督学习任务。这 900 个标记样本被分成了十组，编号为 `#0` 至 `#9` ，每组有 90 个样本。我们随机选择一组作为目标样本( target sample )，该组样本不会在训练过程中作为输入, 只会被用于在训练过程中验证网络效果，并根据梯度下降算法和误差反向传播更新网络的权重。此外，引入测试样本 (test sample) 以验证训练后的网络。值得注意的是，当测试样本在目标样本 ( target sample ) 内部时，将评估插值的能力。另一方面，当测试样本在目标样本 ( target sample ) 外部时，将评估外推的能力。

In our previous work [6], only the training samples are utilized in the training process. The input is the Gaussian distribution that contains the label information and the output is the corresponding field distribution. In this work, firstly, an approach is proposed to improve the network performance by increasing some smart training samples. Besides, a new concept named reference samples is introduced. As the name implies, it is the reference information introduced to the model during the深度学习process, which is our vague expectation of the approximate distribution of the target output. It participates in the process of network training together with training samples to reform the input image. But, different from regular training samples, which are only computed once in a whole epoch, the references will be computed once in each batch, and there may be lots of batches in one epoch. What is more, only the label information are taken from training samples as the input for the network, as for reference samples, the whole field distribution will be taken into consideration and combined with training sample label information as the new input for the network. In addition, the introduction of reference requires us to change the architecture because they will change the structure of input information. On the other hand, no matter how many training samples we use, the architecture of the network remains the same. Adopt the network architecture and the baseline set of hyperparameters obtained in [6]; the network was adjusted so that it can accept more reference samples as input. Besides, more attention has been paid to adjusting the structure of the input image, as shown in Fig. 1, which is composed of the Gaussian distribution containing the training sample label information and the entire field distribution of the reference sample.

在我们之前的工作[6]中，训练过程中只使用训练样本。输入是包含标签信息的高斯分布，输出是对应的场分布。在这项工作中，首先，提出了一种通过增加一些智能训练样本来提高网络性能的方法。此外，引入了一个名为参考样本的新概念。顾名思义，就是深度学习过程中引入模型的参考信息，也就是我们对目标输出的大概分布的模糊预期。它与训练样本一起参与网络训练过程，对输入图像进行改造。但是，与常规训练样本在整个 epoch 中只计算一次不同，参考样本将在每个 batch 中计算一次，并且在一个 epoch 中可能有很多 batches。并且，仅将训练样本中的标签信息作为网络的输入，对于参考样本，将考虑整个场分布并结合训练样本标签信息作为网络的新输入。此外，参考样本的引入需要我们改变架构，因为它们会改变输入信息的结构。另一方面，无论我们使用多少训练样本，网络的架构都保持不变。采用[6]中获得的网络架构和基线超参数集；调整了网络，使其可以接受更多参考样本作为输入。此外，更加注意调整输入图像的结构，如图所示，它由包含训练样本标签信息的高斯分布和参考样本的整个场分布组成。


Greedy Algorithm

上述样本选择策略是通过贪心算法实现的。贪心算法是一种遵循问题解决启发式的方法，即在尝试找到整个问题的整体最优解时，在每一步做出最优选择。它不能保证最优解，但可以提供可能的“最佳”选择[7]。

Let us denote $\mathbf{v}$ a vector which contains several components corresponding to different physical features, $f(\mathbf{v})$ the corresponding output field distribution obtained by FEM, which can be understood as the ground truth, then the term $[\mathbf{v}, f(\mathbf{v})]$ can server as one data sample for the DL. With $N$ different configurations, the set for the label $\mathbb{L}_N$ and the set of ground truth field distribution $\mathbb{F}_N$ are defined, respectively, as
$$
\mathbb{L}_N=\left\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_N\right\}, \quad \mathbb{F}_N=\left\{f\left(\mathbf{v}_1\right), f\left(\mathbf{v}_2\right), \ldots, f\left(\mathbf{v}_N\right)\right\}
$$
The task of supervised DL is to obtain an approximated functional $g$ based on $\left(\mathbb{L}_N, \mathbb{F}_N\right)$ such that $g(\mathbb{L}) \approx \mathbb{F}$ when $N$ tends to infinity, that is $\mathbb{L}=\lim _{N \rightarrow \infty} \mathbb{L}_N$. One way of deciding whether the training samples need to be added is to estimate the error of the current DL model with the given label information. Once the DL models are trained, a convenient error indicator $\eta$ can be constructed as the difference between the prediction results given by the DL model and the ground truth with the given label set.

We applied the selection strategy as described in Algorithm 1 into the CNN U-net to determine the significant samples to train the network. The smart selection strategy can be applied to both training samples and reference samples.
It should be mentioned here that in the case of without a priori information, the elements in test set $\mathbb{V}$ are chosen uniformly. In practice, the newly added sample $\mathbf{v}^{k+1}$ usually close to but should not coincide with the test samples when verifying the extrapolation capacity of the model. Moreover, $\mathbf{v}^{k+1}$ can represent a set of samples to be added to the network.











### 数值实验和结果

为了保持本文的完整性，下面回顾一下我们之前的工作[6]中描述的所考虑问题的简要介绍。

Considered Problem

For a transformer operating at $50 \mathrm{~Hz}$ , only the magnetostatics problem is considered
$$
\begin{aligned}
\nabla \times \mathbf{H} & =\mathbf{J}_{\mathbf{s}} \\
\nabla \cdot \mathbf{B} & =0 \\
\mathbf{B} & =\mu \mathbf{H}
\end{aligned}
$$
where $\mu$ denotes the magnetic permeability, $\mathbf{H}$ stands for the magnetic field strength, $\mathbf{B}$ is the magnetic flux density, $\mathbf{J}_{\mathbf{s}}$ represents the current density vector.

The heat source $q$ in windings can be obtained from the magnetic field computation, which mainly comes from the dc loss and the eddy current loss. The dc loss $p$ can be calculated by
$$
p=\mathbf{J}_{\mathrm{s}}^2 / \sigma
$$
where $\sigma$ is the electrical conductivity. The relationship between the eddy current loss and magnetic field distribution is nonlinear, which can be described by the following engineering empirical formula:
$$
k_w=k\left(\frac{\alpha B_m}{\delta} \frac{f}{50}\right)^2 \times 100 \%
$$
where $k_w$ is the percentage of the eddy current loss of the winding in the leakage field in the winding dc loss, $k=2.99$ when the winding is made of copper and temperature is $75^{\circ} \mathrm{C}$ [9], $\alpha$ denotes the average of wire thickness, $\delta$ is current density, $B_m$ represents the peak flux density of main leakage channel, and $f$ is the frequency.

About the thermal part, since we only interested in the temperature of the winding and the nearby insulation layer, the distribution of temperature can be described by
$$
\begin{aligned}
\nabla \cdot(\lambda \nabla T)+q & =0 \\
q & =p\left(1+k_w\right)
\end{aligned}
$$
where $\lambda$ is heat conductivity, $T$ denotes temperature. For the boundary condition of the temperature field, the heat on the winding is mainly dissipated by convection between the outside insulating layer and the air
$$
q_{\mathrm{conv}}=h S\left(T_{\mathrm{s}}-T_{\mathrm{f}}\right)
$$
where $q_{\mathrm{conv}}$ is the heat-transfer rates per unit area at the surface by convection, $h$ stands for the convective heat-transfer coefficient, which is mainly determined by the geometry of air duct, $S$ denotes the heat-dissipating area, $T_{\mathrm{s}}$ represents the temperature of the outside of insulation layer, $T_{\mathrm{f}}$ stands for the ambient temperature, which is set to be $20^{\circ} \mathrm{C}$.


Results and Discussion

上述变压器耦合磁热问题由 FEM 求解，由免费的科学计算软件 Freefem++ [10]、[11] 实现。 这些 FEM 结果构成了即将到来的深度学习过程中的数据库。 训练样本太少可能会导致网络发散，如图 2 中针对磁场和温度场绘制的黑线。 提出了两种帮助网络收敛的方法：增加网络的训练样本（分别在网络中加入特殊参考样本）以提高网络的稳定性和收敛性。 训练样本和参考样本由我们提出的贪婪算法选择。 为了清楚地表示样本选择策略的影响，对每种方法进行随机选择进行比较，如图2所示。可以看出，对于训练样本和参考样本，基于贪心算法的选择策略具有 显着优势。 这里需要说明的是，训练样本的每个数字代表一组，每组包含90个训练样本。 另一方面，对于参考样本，每个数字仅代表一个参考样本。 与我们以往的研究经验一致，由于磁通密度分布的连续性，磁场图像中像素之间存在很强的连通性，这使得磁通密度分布更容易学习。 另一方面，由于我们只关心绕组和绝缘附近的温度，绝缘与空气之间存在较大的梯度间隙，这使得温度场的分布更难学习。 对于磁场和温度场预测，增加训练样本可以大大提高模型的准确性和收敛性，但相应地，需要更多的训练样本。 具体来说，还需要为磁场和温度场准备 90 个以上的训练样本。 相比之下，在网络中引入参考样本也可以提高收敛性，虽然其效果可能不如训练样本，但代价要小得多。 与原始情况相比，即使使用多个参考样本也可以更快地实现收敛。 在实践中，需要在模型性能和计算负担之间进行权衡。


成功训练的 CNN 模型可用于预测具有不同几何参数的磁场和温度场的分布，分别如图 3（a）和（b）所示。一旦模型训练成功，一组即 90 个样本可以在 NVIDIA GTX 1080 8-GB GPU 上在 20 秒内在线输出。

本文的目的是探讨使用深度学习解决训练样本集尽可能小的耦合磁热问题的可行性，这是提高深度学习效率的关键。为了实现这一目标，基于传统的深度学习网络训练过程，提出了两种不同的方法，即添加智能训练样本和参考样本，以帮助深度学习网络收敛。此外，提出了一种基于贪心算法的智能样本选择策略来控制训练样本和参考样本的选择过程。保持数据库和 CNN 模型的超参数和架构不变，研究了不同样本选择方法的影响。以典型变压器为例，进行了数值实验。结果表明，所提出的方法可以有效地帮助网络收敛并显着提高深度学习网络的效率。训练过程中涉及更多的训练样本；模型收敛更稳定和更快，但它带来了更多的计算负担。相比之下，引入参考样本可以帮助网络以更低的成本收敛。

### 引文

## 摘录
