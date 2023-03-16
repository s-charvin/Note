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
lastmod: 2023-03-16 10:24:01
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

- :fas_question:   超参数选择问题和**训练数据库小样本问题**
- :obs_pdf_file:   在这篇文章中，作者提出了两种不同的方法来帮助 DL 网络更有效地收敛，即添加智能训练样本和参考样本方法。
- :obs_graph_glyph:   在这篇文章中, 作者使用了一种贪心算法来选择智能训练样本和参考样本. 这种算法可以应用于训练和参考样本的选择. 通过比较随机选择和基于贪心算法的选择策略, 作者发现基于贪心算法的选择策略对于训练样本和参考样本都具有显著优势.
- :obs_wand_glyph:   通过选择最具代表性, 信息量更丰富的训练样本和参考样本来提高模型的效率和准确性。

## 摘要

> [!abstract] Deep learning (DL) has attracted more and more attention in computational electromagnetism. Particularly, the convolutional neural network (CNN) is one of the most popular learning models in DL due to its excellent capacity for feature extraction and convergence. The efficiency of CNN mainly depends on how many training samples are needed to effectively converge the network. The sample preparation process often involves a lot of numerical computations, which can be very expensive and time-consuming. In this article, based on the traditional DL network training procedure, two different approaches, namely adding smart training samples and reference samples, are proposed to help the DL network converge. The smart sample selection is based on a greedy algorithm, which can be applied for both training and reference samples. The influences of these two approaches on the CNN training process are investigated by an example of the coupled magneto-thermal computation applied to a transformer. Numerical results show that the two proposed approaches can significantly help the network to converge and improve the efficiency of the DL model.

> 深度学习 (DL) 在电磁学计算领域引起了越来越多的关注。特别是，卷积神经网络 (CNN) 是深度学习中最流行的学习模型之一，因为它具有出色的特征提取和收敛能力。 CNN 的效率主要取决于网络收敛需要多少有效训练样本。这些样本的制作过程通常涉及大量数值计算，这可能非常昂贵且耗时。在本文中，基于传统的深度学习网络训练过程，提出了两种不同的方法，即在训练过程中添加智能选择的训练样本和参考样本，以帮助深度学习网络更好的收敛。智能样本选择基于贪心算法，可应用于获取训练样本和参考样本。本文通过变压器耦合磁热计算任务研究了这两种方法对 CNN 训练过程的影响。数值结果表明，本文所提出的两种方法可以显著的帮助网络收敛并提高深度学习模型的训练效率。

## 预处理

## 概述

## 结果

## 精读

### 引言

在过去的十年中，虽然目前还没有针对深度学习的坚实理论框架，但随着其理论和基础的不断进步，它已经发展成为了一种非常强大的工具，可以从根本上提高我们开展科学研究的能力 [1]，[2]。特别是，卷积神经网络 (CNN) 因其优秀的特征建模能力, 而获得了极大广泛的应用，尤其是在计算机视觉领域 [3]。此外, 在电磁学计算领域，通过引入 CNN 与图像处理相结合的理论, 也取得了一些不错的效果。正如最近在 [4] 中报道的那样，贝叶斯 CNN 可以被用来评估电磁设备的磁场计算。 [5] 报道了 CNN 在加速内置式永磁电机拓扑优化方面的另一种应用。尽管到目前为止，深度学习在很多领域都取得了不错的成绩，但是，深度学习网络要获得优秀的准确性和可重复性，仍然有两个重要的前提常常被忽视，即一组合适的超参数和足够大的训练数据库。研究人员往往重点关注网络在收敛后能获得多好的学习效果，而很少对这两个对网络训练过程至关重要的先决条件进行详细研究。通过将 CNN 应用于耦合磁热计算，我们之前的工作 [6] 已经详细讨论了网络超参数问题并提出了一组基线模型。本文的工作通过采用与 [6] 中所示相同的 CNN 架构和超参数，集中研究训练样本选择策略对训练过程的影响。众所周知，深度学习模型往往需要一定数量的训练样本才能训练出理想的网络。一般来说，正如我们之前的工作所观察到的，CNN 网络通常需要大约 30%–40% 的数据库来有效地训练深度学习模型，这对于复杂的数值模型来说, 数据成本非常高。

一般来说，在深度学习网络训练过程中最繁琐、最耗时、最费力的部分是获取足够大的数据库。我们这里的动机就是让深度学习的网络所需的数据集尽可能小，这是进一步提高深度学习效率的关键。为此，我们提出了两种不同的方法来帮助深度学习网络在提供的小型数据库中更好的收敛，即添加智能训练样本和参考样本。受[7]和[8]中这些想法的启发，引入了一种贪心算法来控制训练样本和参考样本的选择过程。保持数据库和 CNN 模型的超参数和架构不变，研究了不同样本选择方法对模型训练效果的影响。以变压器耦合磁热计算任务为例进行了效果验证实验。结果表明，本文所提出的方法可以在训练数据集尽可能小的情况下显着提高 CNN U-net 的性能，从而提高深度学习的效率。

### 理论与方法

CNN U-Net

不同于人脸识别、卫星识别等传统计算机视觉问题, 无法制定和概括具体的规则，电气工程领域的问题均是基于自然中的物理规则的，这意味着它们的表现也受制于严格的物理规则。物理参数与相应的场分布之间存在密切关系。因此，在结果出来之前，我们往往可以有一个粗略的模糊预期作为先验信息。所有这些先验信息都可以帮助我们更高效地完成网络训练。我们采用 CNN U-net 来估计耦合磁热问题，工作流程如下图所示。下面讨论磁场分布的学习过程，而温度场基本相同分配。


![]({54}_Training%20Sample%20Selection%20Strategy%20Applied%20to%20CNN%20in%20Magneto-Thermal%20Coupled%20Analysis@gongTrainingSampleSelection2021.assets/image-20230313150837.png)





首先，通过有限元法 (FEM) 计算获得了 900 个磁通密度分布样本，这些样本以 256×256×3（RGB）图像的形式展示，并用作深度学习训练的数据库。根据它们的几何参数(变压器的参数等)为这些样本进行标记，以备接下来的监督学习任务。这 900 个标记样本被分成了十组，编号为 `#0` 至 `#9` ，每组有 90 个样本。我们随机选择一组作为目标样本( target sample )，该组样本不会在训练过程中作为输入, 只会被用于在训练过程中验证网络效果，并根据梯度下降算法和误差反向传播更新网络的权重。此外，引入测试样本 (test sample) 以验证训练后的网络。值得注意的是，当测试样本在目标样本 ( target sample ) 内部时，将评估插值的能力()。另一方面，当测试样本在目标样本 ( target sample ) 外部时，将评估外推的能力。

在我们之前的工作[6]中，训练过程中只使用训练样本。输入是包含标签信息的高斯分布，输出是对应的场分布。在这项工作中，首先，提出了一种通过增加一些智能训练样本来提高网络性能的方法。此外，引入了一个名为参考样本的新概念。顾名思义，就是深度学习过程中引入模型的参考信息，也就是我们对目标输出的大概分布的模糊预期。它与训练样本一起参与网络训练过程，对输入图像进行改造。

但是，与常规训练样本在整个 epoch 中只计算一次不同，参考样本将在每个 batch 中计算一次，并且在一个 epoch 中可能有很多 batches。并且，仅将训练样本中的标签信息作为网络的输入，对于参考样本，将考虑整个场分布并结合训练样本标签信息作为网络的新输入。此外，参考样本的引入需要我们改变架构，因为它们会改变输入信息的结构。具体来说，在训练过程中，将参考样本和训练样本结合起来构成输入图像，并将其输入到 CNN 模型中进行训练。
另一方面，无论我们使用多少训练样本，网络的架构都保持不变。采用[6]中获得的网络架构和基线超参数集；调整了网络，使其可以接受更多参考样本作为输入。此外，更加注意调整输入图像的结构，如图所示，它由包含训练样本标签信息的高斯分布和参考样本的整个场分布组成。

Greedy Algorithm

上述提到的智能样本选择策略是通过贪心算法实现的。贪心算法是一种遵循问题解决启发式的方法，即在尝试找到整个问题的整体最优解时，在每一步做出最优选择。它不能保证最优解，但可以提供可能的“最佳”选择[7]。

让我们用 $\mathbf{v}$ 表示一个向量，其中包含对应于不同物理特征的几个分量， $f(\mathbf{v})$ 是 FEM 得到的对应输出场分布，可以理解为 ground truth，那么术语 $[\mathbf{v}, f(\mathbf{v})]$ 可以作为深度学习的一个数据样本。在 $N$ 种不同配置下，标签 $\mathbb{L}_N$ 的集合和 ground truth 字段分布 $\mathbb{F}_N$ 的集合分别定义为 $$\mathbb{L}_N =\left\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_N\right\}, \quad \mathbb{F}_N=\left\{f\left( \mathbf{v}_1\right), f\left(\mathbf{v}_2\right), \ldots, f\left(\mathbf{v}_N\right)\right\} $$ 有监督的任务深度学习是基于 $\left(\mathbb{L}_N, \mathbb{F}_N\right)$ 得到一个近似泛函 $g$ 使得 $g(\mathbb{L})\approx \mathbb{F }$ 当 $N$ 趋于无穷时，即 $\mathbb{L}=\lim _{N \rightarrow \infty} \mathbb{L}_N$ 。决定是否需要添加训练样本的一种方法是使用给定的标签信息来估计当前深度学习模型的误差。一旦深度学习模型经过训练，就可以构建一个方便的误差指标 $\eta$ 作为深度学习模型给出的预测结果与给定标签集的基本事实之间的差异。

![]({54}_Training%20Sample%20Selection%20Strategy%20Applied%20to%20CNN%20in%20Magneto-Thermal%20Coupled%20Analysis@gongTrainingSampleSelection2021.assets/image-20230313171926.png)


我们将算法 1 中描述的选择策略应用到 CNN U-net 中，以确定训练网络的重要样本。智能选择策略可以应用于训练样本和参考样本。这里需要说明的是，在没有先验信息的情况下，统一选择测试集 $\mathbb{V}$ 中的元素。在实践中，在验证模型的外推能力时，新加入的样本 $\mathbf{v}^{k+1}$ 通常与测试样本接近但不应重合。此外， $\mathbf{v}^{k+1}$ 可以表示要添加到网络中的一组样本。

### 数值实验和结果

为了保持本文的完整性，下面回顾一下我们之前的工作[6]中描述的所考虑问题的简要介绍。

Considered Problem

对于以 $50 \mathrm{~Hz}$ 运行的变压器，仅考虑静磁学问题 $$ \begin{aligned} \nabla \times \mathbf{H} & =\mathbf{J}_{\mathbf{s} } \\ \nabla \cdot \mathbf{B} & =0 \\ \mathbf{B} & =\mu \mathbf{H} \end{aligned} $$ 其中 $\mu$ 表示磁导率， $\ mathbf{H}$ 代表磁场强度， $\mathbf{B}$ 代表磁通密度， $\mathbf{J}_{\mathbf{s}}$ 代表电流密度向量。绕组中的热源 $q$ 可以通过磁场计算得到，主要来自于直流损耗和涡流损耗。直流损耗 $p$ 可以通过 $$ p=\mathbf{J}_{\mathrm{s}}^2 / \sigma $$计算，其中 $\sigma$ 是电导率。涡流损耗与磁场分布之间的关系是非线性的，可用以下工程经验公式来描述： $$ k_w=k\left(\frac{\alpha B_m}{\delta} \frac{f}{ 50}\right)^2 \times 100 \% $$ 其中 $k_w$ 是绕组在漏场中的涡流损耗占绕组直流损耗的百分比， $k=2.99$ 当绕组由铜和温度为 $75^{\circ} \mathrm{C}$ [9]， $\alpha$ 表示平均线厚， $\delta$ 为电流密度， $B_m$ 表示主要漏电流的峰值磁通密度信道， $f$ 是频率。关于热部分，由于我们只对绕组和附近绝缘层的温度感兴趣，因此温度分布可以描述为 $$ \begin{aligned} \nabla \cdot(\lambda \nabla T)+q & =0 \\ q & =p\left(1+k_w\right) \end{aligned} $$ 其中 $\lambda$ 为导热系数， $T$ 表示温度。对于温度场的边界条件，绕组上的热量主要通过外绝缘层与空气之间的对流散热 $$ q_{\mathrm{conv}}=h S\left(T_{\mathrm{s} }-T_{\mathrm{f}}\right) $$ 其中 $q_{\mathrm{conv}}$ 是表面单位面积的对流传热率， $h$ 代表对流热- 传递系数，主要由风管的几何形状决定， $S$ 表示散热面积， $T_{\mathrm{s}}$ 表示保温层外侧的温度， $T_{\mathrm{ f}}$ 代表环境温度，设置为 $20^{\circ} \mathrm{C}$ 。

Results and Discussion

上述变压器耦合磁热问题由 FEM 求解，由免费的科学计算软件 Freefem++ [10]、[11] 实现。 这些 FEM 结果构成了即将到来的深度学习过程中的数据库。 训练样本太少可能会导致网络发散，如图 2 中针对磁场和温度场绘制的黑线。 提出了两种帮助网络收敛的方法：增加网络的训练样本（分别在网络中加入特殊参考样本）以提高网络的稳定性和收敛性。 训练样本和参考样本由我们提出的贪婪算法选择。 为了清楚地表示样本选择策略的影响，对每种方法进行随机选择进行比较，如图2所示。可以看出，对于训练样本和参考样本，基于贪心算法的选择策略具有 显着优势。 这里需要说明的是，训练样本的每个数字代表一组，每组包含90个训练样本。 另一方面，对于参考样本，每个数字仅代表一个参考样本。 与我们以往的研究经验一致，由于磁通密度分布的连续性，磁场图像中像素之间存在很强的连通性，这使得磁通密度分布更容易学习。 另一方面，由于我们只关心绕组和绝缘附近的温度，绝缘与空气之间存在较大的梯度间隙，这使得温度场的分布更难学习。 对于磁场和温度场预测，增加训练样本可以大大提高模型的准确性和收敛性，但相应地，需要更多的训练样本。 具体来说，还需要为磁场和温度场准备 90 个以上的训练样本。 相比之下，在网络中引入参考样本也可以提高收敛性，虽然其效果可能不如训练样本，但代价要小得多。 与原始情况相比，即使使用多个参考样本也可以更快地实现收敛。 在实践中，需要在模型性能和计算负担之间进行权衡。

成功训练的 CNN 模型可用于预测具有不同几何参数的磁场和温度场的分布，分别如图 3（a）和（b）所示。一旦模型训练成功，一组即 90 个样本可以在 NVIDIA GTX 1080 8-GB GPU 上在 20 秒内在线输出。

本文的目的是探讨使用深度学习解决训练样本集尽可能小的耦合磁热问题的可行性，这是提高深度学习效率的关键。为了实现这一目标，基于传统的深度学习网络训练过程，提出了两种不同的方法，即添加智能训练样本和参考样本，以帮助深度学习网络收敛。此外，提出了一种基于贪心算法的智能样本选择策略来控制训练样本和参考样本的选择过程。保持数据库和 CNN 模型的超参数和架构不变，研究了不同样本选择方法的影响。以典型变压器为例，进行了数值实验。结果表明，所提出的方法可以有效地帮助网络收敛并显着提高深度学习网络的效率。训练过程中涉及更多的训练样本；模型收敛更稳定和更快，但它带来了更多的计算负担。相比之下，引入参考样本可以帮助网络以更低的成本收敛。

### 引文

## 摘录
