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
lastmod: 2022-11-19 14:44:51
---

# 重点

- [开源代码](https://github.com/IntelVCL/MultiObjectiveOptimization)

# 摘要 

In multi-task learning, multiple tasks are solved jointly, sharing inductive bias between them. Multi-task learning is inherently a multi-objective problem because different tasks may conflict, necessitating a trade-off. A common compromise is to optimize a proxy objective that minimizes a weighted linear combination of pertask losses. However, this workaround is only valid when the tasks do not compete, which is rarely the case. In this paper, we explicitly cast multi-task learning as multi-objective optimization, with the overall objective of finding a Pareto optimal solution. To this end, we use algorithms developed in the gradient-based multiobjective optimization literature. These algorithms are not directly applicable to large-scale learning problems since they scale poorly with the dimensionality of the gradients and the number of tasks. We therefore propose an upper bound for the multi-objective loss and show that it can be optimized efficiently. We further prove that optimizing this upper bound yields a Pareto optimal solution under realistic assumptions. We apply our method to a variety of multi-task deep learning problems including digit classification, scene understanding (joint semantic segmentation, instance segmentation, and depth estimation), and multilabel classification. Our method produces higher-performing models than recent multi-task learning formulations or per-task training.

在多任务学习中，多任务联合求解，多任务之间共享归纳==偏置==。多任务学习本质上是一个多目标问题，因为不同的任务可能会发生冲突，需要进行权衡取舍。一个常见的折衷方案是优化一个间接的目标函数（proxy objective），以最大限度地减少所有任务损失的加权和。但是，这种解决方案只有在任务不竞争时才有效，这种情况很少发生。本文将多任务学习明确地归结为多目标优化问题，其总体目标是寻找一个帕累托最优解（Pareto Optimality，一种理想状态，假定在固定资源的条件下，多个需优化目标, 虽然从一种资源分配状态到另一种分配状态的变化中，没有使任何人境况变坏的前提下，使得至少一个人变得更好）。为此，我们使用基于梯度的多目标优化文献中开发的算法。这些算法不能直接应用于大规模的学习问题，因为它们与梯度的维数和任务的数量规模很小。因此，我们提出了一个多目标损失的上界，并表明它可以被有效地优化。我们进一步证明了在现实假设下优化这个上界可以得到一个帕累托最优解。我们将该方法应用于多任务深度学习问题，包括数字分类、场景理解(联合语义分割、实例分割和深度估计)和多标签分类。我们的方法产生了比最近的多任务学习公式或每任务训练更高性能的模型。

# 结果

# 词汇记录

# 精读

## 引文
