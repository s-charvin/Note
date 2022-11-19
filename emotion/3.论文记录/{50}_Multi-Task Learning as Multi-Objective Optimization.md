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
lastmod: 2022-11-19 17:35:28
---

# 重点

- [开源代码](https://github.com/IntelVCL/MultiObjectiveOptimization)

# 摘要 

In multi-task learning, multiple tasks are solved jointly, sharing inductive bias between them. Multi-task learning is inherently a multi-objective problem because different tasks may conflict, necessitating a trade-off. A common compromise is to optimize a proxy objective that minimizes a weighted linear combination of pertask losses. However, this workaround is only valid when the tasks do not compete, which is rarely the case. In this paper, we explicitly cast multi-task learning as multi-objective optimization, with the overall objective of finding a Pareto optimal solution. To this end, we use algorithms developed in the gradient-based multiobjective optimization literature. These algorithms are not directly applicable to large-scale learning problems since they scale poorly with the dimensionality of the gradients and the number of tasks. We therefore propose an upper bound for the multi-objective loss and show that it can be optimized efficiently. We further prove that optimizing this upper bound yields a Pareto optimal solution under realistic assumptions. We apply our method to a variety of multi-task deep learning problems including digit classification, scene understanding (joint semantic segmentation, instance segmentation, and depth estimation), and multilabel classification. Our method produces higher-performing models than recent multi-task learning formulations or per-task training.

原目标：在多任务学习中，多任务联合求解，多任务之间共享[归纳性偏好](https://blog.csdn.net/qq_39478403/article/details/121107057)（让算法优先解决某种解决方案，如分布约束，正则项惩罚，预先假设等）。多任务学习本质上是一个多目标问题，因为不同的任务可能会发生冲突，需要进行权衡取舍。一个常见的折衷方案是优化一个间接的目标函数（proxy objective），以最大限度地减少所有任务损失的加权和。

原目标的问题：但是，这种解决方案只有在多个任务互相不竞争时才更有效。

优化目标：所以本文将多任务学习明确地归结为多目标优化问题，其总体目标是寻找一个帕累托最优解（Pareto Optimality，一种理想状态，假定在固定资源的条件下，多个需优化目标，虽然从一种资源分配状态变换成了另一种分配状态，但是并不会使任一目标境况变坏，并且还使得至少一个目标变得更好）。

具体方法：为了达成这一目的，我们使用了多目标优化文献中提出的基于梯度的算法。但是这些算法并不能直接应用于大规模的学习问题中，因为它们会随着任务模型梯度的维度和任务数量的增加而变得很差。因此，我们又提出了一个多目标损失的上界，并进一步证明了在现实的假设条件下，可以通过优化这个上界，最终得到一个帕累托最优解。

我们将该方法应用到了一些深度学习多任务问题中，包括数字分类、场景理解(联合语义分割、实例分割和深度估计)和多标签分类，并最终得到了比最近的多任务学习方法或单任务训练更高性能的模型。

# 结果

# 词汇记录

# 精读

斯坦因悖论（Stein’s paradox）是统计学中最令人惊讶的结果之一。 Stein (1956) 表明，最好使用所有样本来估计三个或更多高斯随机变量的均值，而不是分别估计它们，即使高斯分布是独立的。

斯坦因悖论是多任务学习 (MTL) (Caruana, 1997) 的早期动机，这是一种学习范式，其中使用来自多个任务的数据，希望获得优于独立学习每个任务的性能。 MTL 的潜在优势超出了斯坦因悖论的直接影响，因为即使看似无关的现实世界任务也由于产生数据的共享过程而具有很强的依赖性。例如，虽然自动驾驶和物体操纵看似无关，但底层数据受相同的光学、材料特性和动力学定律支配。这促使使用多项任务作为学习系统中的归纳偏差。一个典型的 MTL 系统被赋予输入点的集合和每个点的各种任务的目标集。跨任务设置归纳偏差的一种常见方法是设计一个参数化的假设类，该类在任务之间共享一些参数。通常，这些参数是通过解决优化问题来学习的，该优化问题最小化每个任务的经验风险的加权和。然而，线性组合公式仅在存在对所有任务都有效的参数集时才有意义。换句话说，经验风险加权和的最小化仅在任务不竞争时才有效，而这种情况很少见。具有相互冲突目标的 MTL 需要对任务之间的权衡进行建模，这超出了线性组合所实现的范围。 MTL 的另一个目标是找到不受任何其他人支配的解决方案。这样的解决方案被认为是帕累托最优的。在本文中，我们将 MTL 的目标定为寻找帕累托最优解。

## 引文
