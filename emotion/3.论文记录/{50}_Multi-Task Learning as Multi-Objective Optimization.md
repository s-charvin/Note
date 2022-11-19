---
title: "Multi-Task Learning as Multi-Objective Optimization"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: "笔记"
draft: true
layout: 
data: 2022-08-26 22:01:04
lastmod: 2022-11-19 20:15:22
---

# 重点

- [开源代码](https://github.com/IntelVCL/MultiObjectiveOptimization)

# 摘要 

In multi-task learning, multiple tasks are solved jointly, sharing inductive bias between them. Multi-task learning is inherently a multi-objective problem because different tasks may conflict, necessitating a trade-off. A common compromise is to optimize a proxy objective that minimizes a weighted linear combination of pertask losses. However, this workaround is only valid when the tasks do not compete, which is rarely the case. In this paper, we explicitly cast multi-task learning as multi-objective optimization, with the overall objective of finding a Pareto optimal solution. To this end, we use algorithms developed in the gradient-based multiobjective optimization literature. These algorithms are not directly applicable to large-scale learning problems since they scale poorly with the dimensionality of the gradients and the number of tasks. We therefore propose an upper bound for the multi-objective loss and show that it can be optimized efficiently. We further prove that optimizing this upper bound yields a Pareto optimal solution under realistic assumptions. We apply our method to a variety of multi-task deep learning problems including digit classification, scene understanding (joint semantic segmentation, instance segmentation, and depth estimation), and multilabel classification. Our method produces higher-performing models than recent multi-task learning formulations or per-task training.

原目标：在多任务学习中，多任务联合求解，多任务之间共享[归纳性偏好](https://blog.csdn.net/qq_39478403/article/details/121107057)（inductive bias ，让算法优先解决某种解决方案，如分布约束，正则项惩罚，预先假设等）。多任务学习本质上是一个多目标问题，因为不同的任务可能会发生冲突，需要进行权衡取舍。一个常见的折衷方案是优化一个间接的目标函数（proxy objective），以最大限度地减少所有任务损失的加权和。

原目标的问题：但是，这种解决方案只有在多个任务互相不竞争时才更有效。

优化目标：所以本文将多任务学习明确地归结为多目标优化问题，其总体目标是寻找一个帕累托最优解（Pareto Optimality，一种理想状态，假设在固定资源的条件下，无法继续通过调整资源分配方案，使得所有目标境况都不变坏的情况下，令至少一个目标变得更好）。

具体方法：为了达成这一目的，我们使用了多目标优化文献中提出的基于梯度的算法。但是这些算法并不能直接应用于大规模的学习问题中，因为它们会随着任务模型梯度的维度和任务数量的增加而变得很差。因此，我们又提出了一个多目标损失的上界，并进一步证明了在现实的假设条件下，可以通过优化这个上界，最终得到一个帕累托最优解。

方法证明：我们将该方法应用到了一些深度学习多任务问题中，包括数字分类、场景理解(联合语义分割、实例分割和深度估计)和多标签分类，并最终得到了比最近的多任务学习方法或单任务训练更高性能的模型。

# 结果

# 词汇记录

# 精读

斯坦因悖论（Stein’s paradox）是统计学中最令人惊讶的结果之一。 Stein (1956) 表明，最好使用所有样本的数据来估计其中三个或更多高斯随机变量的均值，而不是单独的去估计它们，即使这些变量的分布是独立的（类似于用总体估计的结果对单个估计的结果做修正）。

[举例](http://bayes-stat.github.io/download/stein.pdf)：如果有 3 个以上的运动员在打棒球，现在有了他们各自的击球结果记录。在估计他们各自的命中率时，不要直接求他们各自的极大似然估计（即使这些运动员是相互独立的），因为这样不准。最好的办法是在估计任何一个人的命中率时，把其他人的击球结果记录也用起来。

![]({50}_Multi-Task%20Learning%20as%20Multi-Objective%20Optimization.assets/image-20221119184932.png)

斯坦因悖论是探索多任务学习 (MTL) (Caruana, 1997) 的早期启发。多任务学习是一种学习范式，通过使用来自多个任务的数据，寄希望于获得优于独立学习每个任务的性能。多任务学习的潜在优势超出了斯坦因悖论的直接影响，因为现实世界中即使看似无关的任务也由于数据产生的共享过程而存在很强的依赖性。例如，虽然自动驾驶任务和对象操纵任务看似无关，但其底层数据都受相同的光学规律、材料特性和动力学定律影响。这启发了人们将多项任务作为学习系统中的归纳偏置（inductive bias）。

典型的多任务学习系统的输入通常为一组输入点集合以及每点在不同任务中的目标集。多任务联合求解，然后共享归纳偏置。常见的一种跨任务共享归纳偏置（inductive bias）的设置方法为设计一个参数化的假设类，让其在不同任务之间共享一些参数。一般而言，可以通过最小化每个任务的经验风险的加权和，来学习到这些参数。然而，这种线性加权的方式仅在共享参数对所有任务都有效时才有意义。换言之，最小化经验风险加权和的方式仅在这些任务的学习不存在竞争关系时才有效，而这种情况很少见。任务目标存在冲突的多任务学习，需要对不同任务之间的权衡进行建模，而这超出了线性组合的能力。

多任务学习的另一个目标是找到一个不受任何其它方案主导的解决方案。在本文中，我们将多任务学习的目标定为寻找帕累托最优解。在给定多个条件的情况下寻找帕累托最优解的问题称为多目标优化。目前已有多种用于多目标优化的算法。

一种方法是多梯度下降算法 (MGDA)，该算法基于梯度下降的方法，并证明了帕累托集合上的点是收敛的(Désidéri, 2012)。 MGDA 非常适合深层网络的多任务学习。它可以使用每个任务的梯度并解决优化问题来更新共享参数。然而，有两个技术性问题阻碍了 MGDA 的大规模应用。(i) 底层优化问题不能很好地扩展到深度网络中自然出现的高维梯度。 (ii) 该算法需要显式计算每个任务的梯度，这会导致向后传递次数的线性缩放，并粗略地将训练时间乘以任务数。在本文中，我们开发了一种基于 Frank-Wolfe 的优化器，可扩展到高维问题。此外，我们为 MGDA 优化目标提供了一个上限，并表明它可以通过单个向后传递计算而无需明确的特定于任务的梯度，从而使该方法的计算开销可以忽略不计。我们证明，在现实假设下，使用我们的上限会产生帕累托最优解。结果是一种用于深度网络多目标优化的精确算法，计算开销可忽略不计。我们在三个不同的问题上对所提出的方法进行了实证评估。首先，我们使用 MultiMNIST (Sabour et al., 2017) 对多位分类进行了广泛的评估。其次，我们将多标签分类转换为 MTL，并使用 CelebA 数据集进行实验 (Liu et al., 2015b)。最后，我们将提出的方法应用于场景理解；具体来说，我们对 Cityscapes 数据集执行联合语义分割、实例分割和深度估计 (Cordts et al., 2016)。我们评估中的任务数量从 2 到 40 不等。我们的方法明显优于所有基线。

多任务学习：我们总结了与我们最密切相关的工作，并向感兴趣的读者推荐 Ruder (2017) 和 Zhou 等人的评论。 (2011b) 了解更多背景信息。多任务学习 (MTL) 通常通过硬或软参数共享进行。在硬参数共享中，参数的一个子集在任务之间共享，而其他参数是特定于任务的。在软参数共享中，所有参数都是特定于任务的，但它们通过贝叶斯先验 (Xue et al., 2007; Bakker and Heskes, 2003) 或联合字典 (Argyriou et al., 2007; Long and Wang, 2015) 共同约束；Yang 和 Hospedales，2016 年；罗德，2017 年）。继深度 MTL 在计算机视觉领域取得成功后，我们专注于基于梯度优化的硬参数共享（Bilen 和 Vedaldi，2016 年；Misra 等人，2016 年；Rudd 等人，2016 年；Yang 和 Hospedales，2016 年；Kokkinos， 2017 年；Zamir 等人，2018 年），自然语言处理（Collobert 和 Weston，2008 年；Dong 等人，2015 年；Liu 等人，2015a；Luong 等人，2015 年；Hashimoto 等人，2017 年），语音处理（Huang 等人，2013 年；Seltzer 和 Droppo，2013 年；Huang 等人，2015 年），甚至在多种模式上看似不相关的领域（Kaiser 等人，2017 年）。Baxter (2000) 从理论上将 MTL 问题分析为个体学习者与元算法之间的交互。每个学习者负责一项任务，元算法决定共享参数的更新方式。所有上述 MTL 算法都使用加权求和作为元算法。还探索了超越加权求和的元算法。李等。 (2014) 考虑每个学习者都基于内核学习并利用多目标优化的情况。 Zhang 和 Yeung (2010) 考虑每个学习者都是线性模型并使用任务亲和矩阵的情况。周等。 (2011a) 和 Bagherjeiran 等人。 (2005) 使用任务共享字典的假设并开发类似期望最大化的元算法。德米兰达等人。 (2012) 和 Zhou 等人。 (2017b) 使用群体优化。这些方法都不适用于现代深度网络等高容量模型的基于梯度的学习。肯德尔等人。 (2018) 和 Chen 等人。 (2018) 分别提出基于不确定性和梯度幅度的启发式方法，并将其方法应用于卷积神经网络。最近的另一项工作使用多智能体强化学习（Rosenbaum 等人，2017 年）。

多目标优化：多目标优化解决了优化一组可能对比目标的问题。我们推荐 Miettinen (1998) 和 Ehrgott (2005) 对该领域的调查。与我们的工作特别相关的是基于梯度的多目标优化，由 Fliege 和 Svaiter (2000)、Schäffler 等人开发。 (2002) 和德西德里 (2012)。这些方法使用多目标 Karush-Kuhn-Tucker (KKT) 条件（Kuhn 和 Tucker，1951 年）并找到降低所有目标的下降方向。 Peitz 和 Dellnitz（2018 年）以及 Poirion 等人将这种方法扩展到随机梯度下降。 (2017)。在机器学习中，这些方法已应用于多智能体学习（Ghosh 等人，2013 年；Pirotta 和 Restelli，2016 年；Parisi 等人，2014 年）、内核学习（Li 等人，2014 年）、顺序决策制定 （Roijers 等人，2013 年）和贝叶斯优化（Shah 和 Ghahramani，2016 年；Hernández-Lobato 等人，2016 年）。我们的工作将基于梯度的多目标优化应用于多任务学习。

## 引文
