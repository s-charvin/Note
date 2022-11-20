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
lastmod: 2022-11-20 21:56:33
---

# 重点

- [开源代码](https://github.com/IntelVCL/MultiObjectiveOptimization)

# 摘要 

In multi-task learning, multiple tasks are solved jointly, sharing inductive bias between them. Multi-task learning is inherently a multi-objective problem because different tasks may conflict, necessitating a trade-off. A common compromise is to optimize a proxy objective that minimizes a weighted linear combination of pertask losses. However, this workaround is only valid when the tasks do not compete, which is rarely the case. In this paper, we explicitly cast multi-task learning as multi-objective optimization, with the overall objective of finding a Pareto optimal solution. To this end, we use algorithms developed in the gradient-based multiobjective optimization literature. These algorithms are not directly applicable to large-scale learning problems since they scale poorly with the dimensionality of the gradients and the number of tasks. We therefore propose an upper bound for the multi-objective loss and show that it can be optimized efficiently. We further prove that optimizing this upper bound yields a Pareto optimal solution under realistic assumptions. We apply our method to a variety of multi-task deep learning problems including digit classification, scene understanding (joint semantic segmentation, instance segmentation, and depth estimation), and multilabel classification. Our method produces higher-performing models than recent multi-task learning formulations or per-task training.

原目标：在多任务学习中，多任务联合求解，多任务之间共享[归纳性偏好](https://blog.csdn.net/qq_39478403/article/details/121107057)（inductive bias ，让算法优先解决某种解决方案，如分布约束，正则项惩罚，预先假设等）。多任务学习本质上是一个多目标问题，因为不同的任务可能会发生冲突，需要进行权衡取舍。一个常见的折衷方案是优化一个间接的目标函数（proxy objective），以最大限度地减少所有任务损失的加权和。

原目标的问题：但是，这种解决方案只有在多个任务互相不竞争时才更有效。

优化目标：所以本文将多任务学习明确地归结为多目标优化问题，其总体目标是寻找一个帕累托最优解（Pareto Optimality，一种理想状态，假设在固定资源的条件下，无法继续通过调整资源分配方案，使得所有目标境况都不变坏的情况下，令至少一个目标变得更好）。

具体方法：为了达成这一目的，本文使用了多目标优化文献中提出的基于梯度的算法。但是这些算法并不能直接应用于大规模的学习问题中，因为它们会随着任务模型梯度的维度和任务数量的增加而变得很差。因此，本文又提出了一个多目标损失的上界，并进一步证明了在现实的假设条件下，可以通过优化这个上界，最终得到一个帕累托最优解。

方法证明：本文将该方法应用到了一些深度学习多任务问题中，包括数字分类、场景理解(联合语义分割、实例分割和深度估计)和多标签分类，并最终得到了比最近的多任务学习方法或单任务训练更高性能的模型。

# 结果

# 词汇记录

# 精读

斯坦因悖论（Stein’s paradox）是统计学中最令人惊讶的结果之一。 Stein (1956) 表明，最好使用所有样本的数据来估计其中三个或更多高斯随机变量的均值，而不是单独的去估计它们，即使这些变量的分布是独立的（类似于用总体估计的结果对单个估计的结果做修正）。

[举例](http://bayes-stat.github.io/download/stein.pdf)：如果有 3 个以上的运动员在打棒球，现在有了他们各自的击球结果记录。在估计他们各自的命中率时，不要直接求他们各自的极大似然估计（即使这些运动员是相互独立的），因为这样不准。最好的办法是在估计任何一个人的命中率时，把其他人的击球结果记录也用起来。

![]({50}_Multi-Task%20Learning%20as%20Multi-Objective%20Optimization.assets/image-20221119184932.png)

斯坦因悖论是探索多任务学习 (多任务学习) (Caruana, 1997) 的早期启发。多任务学习是一种学习范式，通过使用来自多个任务的数据，寄希望于获得优于独立学习每个任务的性能。多任务学习的潜在优势超出了斯坦因悖论的直接影响，因为现实世界中即使看似无关的任务也由于数据产生的共享过程而存在很强的依赖性。例如，虽然自动驾驶任务和对象操纵任务看似无关，但其底层数据都受相同的光学规律、材料特性和动力学定律影响。这启发了人们将多项任务作为学习系统中的归纳偏置（inductive bias）。

典型的多任务学习系统的输入通常为一组输入点集合以及每点在不同任务中的目标集。多任务联合求解，然后共享归纳偏置。常见的一种跨任务共享归纳偏置（inductive bias）的设置方法为设计一个参数化的假设类，让其在不同任务之间共享一些参数。一般而言，可以通过最小化每个任务的经验风险的加权和，来学习到这些参数。然而，这种线性加权的方式仅在共享参数对所有任务都有效时才有意义。换言之，最小化经验风险加权和的方式仅在这些任务的学习不存在竞争关系时才有效，而这种情况很少见。对于任务目标存在冲突的多任务学习，需要对不同任务之间的权衡进行建模，而这超出了线性组合的能力范畴。

多任务学习的另一个目标是找到一个不受任何其它方案主导的解决方案。在本文中，本文将多任务学习的目标定为寻找帕累托最优解。在给定多个条件的情况下寻找帕累托最优解的问题称为多目标优化。目前已有多种用于多目标优化的算法。

一种方法是多梯度下降算法 (MGDA)，该算法基于梯度下降的方法，通过使用每个任务的梯度并解决优化问题来更新共享参数，并可证明帕累托集合上的点是收敛的(Désidéri, 2012)。 MGDA 非常适合深层网络的多任务学习，然而，有两个技术性问题阻碍了 MGDA 的大规模应用。

1. 随着任务数量和梯度维度的增加，传统的底层优化方法会存在问题，导致模型的扩展性很差。 
2. 该算法需要计算每个任务的梯度，从而导致反向传播的计算次数随任务数而线性增加，增加了训练时间。

在本文中，提出了一种基于 Frank-Wolfe 的优化方法，可以扩展到高维问题。此外，本文为 MGDA 的优化目标提供了一个上界，并表明可以在没有明确特定任务梯度的情况下通过单次反向传递计算该优化目标，从而使该方法多余的计算开销可以忽略不计。论文证明，在现实条件的假设下，该算法可以使得神经网络找到多目标优化任务的帕累托最优解。

最终本文得到了一种针对深度网络多目标优化问题的精确算法，并在三个不同的问题上对所提出的方法进行了实证评估。首先，本文在 MultiMNIST (Sabour et al., 2017) 上对多数字分类进行了评估。然后，本文将多标签分类转换为了多任务学习，并在 CelebA 数据集(Liu et al., 2015b)上进行了实验。最后，本文将本文提出的方法应用到了场景理解问题中。具体来说，本文在 Cityscapes 数据集 (Cordts et al., 2016) 上对联合语义分割、实例分割以及深度估计三种任务进行了评估。在本文的评估中的，任务数量从 2 到 40 不等，并且最终结果明显优于所有基线。

假设有一个多任务学习问题，输入空间为 $\mathcal{X}$ ，任务的集合为 $\left\{\mathcal{Y}^{t}\right\}_{t \in[T]}$ ，数据集为独立同分布 (i.i.d.) 的数据点 $\left\{\mathbf{x}_{i}, y_{i}^{1}, \ldots, y_{i}^{T}\right\}_{i \in[N]}$ 组成。其中 $T$ 是任务数量， $N$ 表示数据集的大小， $y_{i}^{t}$ 表示第 $t^{\text {th }}$ 个任务的第 $i^{\text {th }}$ 个数据点的标签。然后进一步将每个任务的参数化假设类（parametric hypothesis class，描述输入与输出关系的参数化函数表达式集合，学习过程就是从中选择一个函数）定义为 $f^{t}\left(\mathbf{x} ; \boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right): \mathcal{X} \rightarrow \mathcal{Y}^{t}$ ，其中 $\left(\boldsymbol{\theta}^{s h}\right)$ 是所有任务共享的参数， $\left(\boldsymbol{\theta}^{t}\right)$ 是每个任务独有的参数。每一个任务的损失函数为 $\mathcal{L}^{t}(\cdot, \cdot): \mathcal{Y}^{t} \times \mathcal{Y}^{t} \rightarrow \mathbb{R}^{+}$ .

多任务学习通常会将损失函数设计为：

$$
\min _{\substack{\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}, \ldots, \boldsymbol{\theta}^{T}}} \sum_{t=1}^{T} c^{t} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)
$$

 $c^{t}$ 是每个任务的静态或动态权重，  $\hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)$ 是每个任务 $t$ 的经验损失，公式为 $\hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right) \triangleq \frac{1}{N} \sum_{i} \mathcal{L}\left(f^{t}\left(\mathbf{x}_{i} ; \boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right), y_{i}^{t}\right)$。

尽管加权求和公式在直觉上很吸引人，但它通常要么需要在各种尺度上进行昂贵的网格搜索，要么需要使用启发式算法

尽管加权求和的公式很直观，但当网络层数和任务数逐步增多时，通常需要为每个超参数进行网格搜索，十分消耗计算资源。要么使用启发式搜索 (heuristic，Kendall et al. 2018, Chen et al. 2018)，但是也很难在多任务学习中找到最优解。假设对任务 $t_{1}$ 和 $t_{2}$ 学习到的两个参数 $\boldsymbol{\theta}$ 和 $\boldsymbol{\overline{\theta}}$ 使得 $\hat{\mathcal{L}}^{t_{1}}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t_{1}}\right)<\hat{\mathcal{L}}^{t_{1}}\left(\overline{\boldsymbol{\theta}}^{s h}, \overline{\boldsymbol{\theta}}^{t_{1}}\right)$ 并且  $\hat{\mathcal{L}}^{t_{2}}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t_{2}}\right)>\hat{\mathcal{L}}^{t_{2}}\left(\overline{\boldsymbol{\theta}}^{s h}, \overline{\boldsymbol{\theta}}^{t_{2}}\right)$ ，此时参数  $\boldsymbol{\theta}$ 更适合于任务 $t_{1}$ ，而参数 $\boldsymbol{\overline{\theta}}$ 更适合于任务 $t_{2}$ 。如果不知道两个任务的重要性，那么就无法比较参数 $\boldsymbol{\theta}$ 和 $\boldsymbol{\overline{\theta}}$ 哪个更好。

或者（Alternatively），将多任务学习转换为多目标优化 ：优化一组可能相互冲突的目标集合。本文选用的方式是利用一个损失值向量 $\mathbf{L}$ 来表示多任务学习的最终损失：

$$
\min _{\substack{\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}, \ldots, \boldsymbol{\theta}^{T}}} \mathbf{L}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}, \ldots, \boldsymbol{\theta}^{T}\right)=\min _{\substack{\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}, \ldots, \boldsymbol{\theta}^{T}}}\left(\hat{\mathcal{L}}^{1}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}\right), \ldots, \hat{\mathcal{L}}^{T}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{T}\right)\right)^{\top}
$$

然后使用基于梯度下降的多目标优化方法（因为它与基于梯度下降的多任务学习直接相关），优化上述公式，最终得到帕累托最优方案。

多任务学习的帕累托最优的定义：

1. 对于所有的任务 $t$ ，如果 $\hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{\text {sh }}, \boldsymbol{\theta}^{t}\right) \leq \hat{\mathcal{L}}^{t}\left(\overline{\boldsymbol{\theta}}^{\text {sh }}, \overline{\boldsymbol{\theta}}^{t}\right)$ 并且 $\mathbf{L}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}, \ldots, \boldsymbol{\theta}^{T}\right) \neq \mathbf{L}\left(\overline{\boldsymbol{\theta}}^{s h}, \overline{\boldsymbol{\theta}}^{1}, \ldots, \overline{\boldsymbol{\theta}}^{T}\right)$ ，那么 $\boldsymbol{\theta}$ 优于 $\overline{\boldsymbol{\theta}}$ 。

2. 如果没有 $\boldsymbol{\theta}$ 优于 $\boldsymbol{\theta}^{\star}$ ，那么称 $\boldsymbol{\theta}^{\star}$ 是最优解。

帕累托最优解的集合被称为 Pareto set $\left(\mathcal{P}_{\boldsymbol{\theta}}\right)$ ，因此其映像为 Pareto front $\left(\mathcal{P}_{\mathbf{L}}=\{\mathbf{L}(\boldsymbol{\theta})\}_{\boldsymbol{\theta} \in \mathcal{P}_{\boldsymbol{\theta}}}\right)$ .。

多梯度下降算法

与单目标任务一样，多目标优化问题也可以通过梯度下降法求解局部最优。这里，本文总结了一种被称为多重梯度下降算法 (MGDA) (Désidéri, 2012) 的方法。MGDA 利用了优化问题中非常重要的 KKT（Karush-Kuhn-Tucker，Fliege and Svaiter, 2000; Schäffler et al. 2002; Désidéri, 2012） 条件。以下是通过特定任务参数和共享参数说明的 KKT 条件：

- 存在 $\alpha^{1}, \ldots, \alpha^{T} \geq 0$ 且 $\sum_{t=1}^{T} \alpha^{t}=1$ ，使得 $\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)=0$ 。（在共享层，没有可行的下降方向，即处于全局最优点，达到了所有任务的最优解。）

- 对于任意的任务 $t$ ，有  $\nabla_{\boldsymbol{\theta}^{t}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)=0$。

任何满足以上这些条件的解都是帕累托平稳点，反之则结论不成立。因此可以将优化问题改写为：

$$
\min _{\alpha^{1}, \ldots, \alpha^{T}}\left\{\left\|\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)\right\|_{2}^{2} \mid \sum_{t=1}^{T} \alpha^{t}=1, \alpha^{t} \geq 0 \quad \forall t\right\}
$$

这个优化问题已经被 Désidéri (2012) 证明，如果该优化问题的结果为 0 ，则可以得出满足 KKT 条件的点；如果不为 0 则该解决方案也能给出改善所有任务的下降方向。因此，最终的多任务学习算法，会针对特定任务参数，执行梯度下降；然后通过求解以上公式，将 $\left(\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}}\right)$ 作为梯度去更新共享参数。

解决优化问题

上述最终定义的优化问题等价于在输入空间的凸包（convex hul）中找到最小范数点。这个问题来源于计算几何（computational geometry）中，因此对此问题已经有了相当广泛的研究(Makimoto et al. 1994 Wolfe 1976 Sekitani and Yamamoto 1993)：它相当于在凸包内找到与给定查询点最接近的点。但是计算几何学文献中提出的算法仅解决了在低维空间（通常为 2 或 3 维）的含有大量点的凸包中，找到最小范数点的问题，这不符合本文假设，也不适用于解决本文问题的环境。在本文的设置中，凸包点数为任务数，通常很小。相反，空间维度为共享参数的数目，可以是数百万。因为上述优化问题是具有线性约束的凸二次问题，因此本文使用了另一种基于凸优化（convex optimization）的方法。 

在处理一般情况之前，先处理只有两个目标任务的情况。首先其优化问题可以被定义为一个关于  $\alpha$ 的一元二次函数： $\min _{\alpha \in[0,1]}\left\|\alpha \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{1}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}\right)+(1-\alpha) \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{2}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{2}\right)\right\|_{2}^{2}$ ，并且可以得到它的解析解为：

$$
\hat{\alpha}=\left[\frac{\left(\nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{2}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{2}\right)-\nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{1}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}\right)\right)^{\top} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{2}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{2}\right)}{\left\|\nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{1}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}\right)-\nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{2}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{2}\right)\right\|_{2}^{2}}\right]_{+, \underset{T}{1}}
$$

其中 $[\cdot]_{+,{ }_{T}^{1}}$ 表示被裁剪到 $[0,1]$ ，例如 $[a]_{+,{ }_{T}^{1}}=\max (\min (a, 1), 0)$ 。此方法的进一步可视化见下图。

![](https://cdn.mathpix.com/cropped/2022_11_19_76f32b82e44c9de424c3g-3.jpg?height=312&width=918&top_left_y=240&top_left_x=365)

Figure 1: Visualisation of the min-norm point in the convex hull of two points $\left(\min _{\gamma \in[0,1]}\|\gamma \boldsymbol{\theta}+(1-\gamma) \overline{\boldsymbol{\theta}}\|_{2}^{2}\right)$ . As the geometry suggests, the solution is either an edge case or a perpendicular vector.

![](https://cdn.mathpix.com/cropped/2022_11_19_76f32b82e44c9de424c3g-3.jpg?height=400&width=428&top_left_y=256&top_left_x=1308)

尽管这只适用于 $T=2$ 的情况，但是由于可以通过解析来解决线搜索问题，因此可以在这里有效地应用 Frank-Wolfe (Jaggi, 2013) 算法来解决上述公式的约束优化问题。求解算法过程如下所示。 

![](https://cdn.mathpix.com/cropped/2022_11_19_76f32b82e44c9de424c3g-3.jpg?height=711&width=1397&top_left_y=720&top_left_x=362)

![]({50}_Multi-Task%20Learning%20as%20Multi-Objective%20Optimization.assets/image-20221120181425.png)

![]({50}_Multi-Task%20Learning%20as%20Multi-Objective%20Optimization.assets/image-20221120181431.png)

在 Encoder 和 Decoder 结构中高效优化

上述提到的多任务学习更新算法可以应用到任何基于梯度下降的优化问题中。本文通过实验还表明，Frank-Wolfe 求解器非常有效且准确，因为它通常会在合适的迭代次数时收敛，而对训练时间的影响可以忽略不计。然而这个算法需要对每个任务 $t$ 都计算 $\nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{\text {sh }}, \boldsymbol{\theta}^{t}\right)$ ，也就说需要对每个任务都对共享参数进行一次反向传播。因此，最终的梯度计算过程中，在前向传播之后，还需要再进行 $T$ 次反向传播。考虑到反向传播通常会比前向传播消耗更多的计算资源，这会导致训练时间的线性增长，这对多任务学习来说是令人望而却步的。

现在，本文提出一种有效的方法来确定优化任务目标的上界，这样就只需要单次反向传播即可。通过进一步证明，在实际假设下，通过优化此上界也可以产生帕累托最优解。本文提出的体系结构将共享表征函数（shared representation function）和特定任务的决策函数（specific-task decision functions）结合在了一起，能够涵盖大多数现有的深层多任务学习模型。具体假设类（参数化的函数表达式集合）约束可以定义为：

$$
f^{t}\left(\mathbf{x} ; \boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)=\left(f^{t}\left(\cdot ; \boldsymbol{\theta}^{t}\right) \circ g\left(\cdot ; \boldsymbol{\theta}^{s h}\right)\right)(\mathbf{x})=f^{t}\left(g\left(\mathbf{x} ; \boldsymbol{\theta}^{s h}\right) ; \boldsymbol{\theta}^{t}\right)
$$

其中 $g$ 是所有任务共享的表征函数， $f^{t}$ 是以共有表征作为输入，作用于特定任务的的决策函数。如果将共有表征表示为 $\mathbf{Z}=\left(\mathbf{z}_{1}, \ldots, \mathbf{z}_{N}\right)$ ，其中 $\mathbf{z}_{i}=g\left(\mathbf{x}_{i} ; \boldsymbol{\theta}^{s h}\right)$ ，那么就可以将上界来代替原有优化目标。

$$
\left\|\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)\right\|_{2}^{2} \leq\left\|\frac{\partial \mathbf{Z}}{\partial \boldsymbol{\theta}^{s h}}\right\|_{2}^{2}\left\|\sum_{t=1}^{T} \alpha^{t} \nabla_{\mathbf{Z}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)\right\|_{2}^{2}
$$

其中 $\left\|\frac{\partial \mathbf{Z}}{\partial \boldsymbol{\theta}^{s h}}\right\|_{2}$ 是 $\mathbf{Z}$ 关于 $\boldsymbol{\theta}^{\text {sh }}$ 的雅可比矩阵范数（matrix norm of the Jacobian）。而在此上界中， $\nabla_{\mathbf{Z}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)$ 对于所有任务而言可以在一次反向传播时就被计算出来。另一方面， $\left\|\frac{\partial \mathbf{Z}}{\partial \boldsymbol{\theta}^{s h}}\right\|_{2}^{2}$ 与 $\alpha^{1}, \ldots, \alpha^{T}$ 无关，不会影响到优化过程，因此可以在优化过程中会被移除。最后将 $\left\|\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)\right\|_{2}^{2}$ 替换换位上界后，可以得到另一个近似优化问题，并可将其内的 $\left\|\frac{\partial \mathbf{Z}}{\partial \theta^{s h}}\right\|_{2}^{2}$  项删除。那么最终的优化问题就变成了：

$$
\min _{\alpha^{1}, \ldots, \alpha^{T}}\left\{\left\|\sum_{t=1}^{T} \alpha^{t} \nabla_{\mathbf{Z}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)\right\|_{2}^{2} \mid \sum_{t=1}^{T} \alpha^{t}=1, \alpha^{t} \geq 0 \quad \forall t\right\}
$$

上述改进的模型称为 MGDA-UB (Multiple Gradient Descent Algorithm - Upper Bound)。在实践中，MGDA-UB 仅使用共享表征而不是共享参数的任务损失的梯度，模型计算复杂度将大大降低。

尽管 MGDA-UB 只是原优化问题的近似解，但是下列定理表明，在一定的假设条件下此方案可以产生帕累托最优解。

定理：假设 $\frac{\partial \mathrm{Z}}{\partial \theta^{\text {sh }}}$ 是满秩的，如果  $\alpha^{1, \ldots, T}$ 是 MGDA-UB 的解，那么下面其中一个则是正确的：

(a) 当 $\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)=0$ 时，目标参数是帕累托平稳点。

(b)  $\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)$ 是降低所有目标的下降方向。

该结果源自以下事实：只要 $\frac{\partial \mathbf{Z}}{\partial \theta \text { sh }}$ 为满秩，则优化上界对应于使用 $\frac{\partial Z}{\partial \theta^{s h}}{ }^{\top} \frac{\partial Z}{\partial \theta^{s h}}$ 定义的 Mahalonobis 范数最小化梯度的凸组合范数。这种非奇异性假设是合理的，因为奇点意味着任务是线性相关的并且不需要权衡。

## 引文

多任务学习：本文总结了与本文最密切相关的工作，并向感兴趣的读者推荐 Ruder (2017) 和 Zhou 等人的评论。 (2011b) 了解更多背景信息。多任务学习 (多任务学习) 通常通过硬或软参数共享进行。在硬参数共享中，参数的一个子集在任务之间共享，而其他参数是特定于任务的。在软参数共享中，所有参数都是特定于任务的，但它们通过贝叶斯先验 (Xue et al., 2007; Bakker and Heskes, 2003) 或联合字典 (Argyriou et al., 2007; Long and Wang, 2015) 共同约束；Yang 和 Hospedales，2016 年；罗德，2017 年）。继深度 多任务学习 在计算机视觉领域取得成功后，本文专注于基于梯度优化的硬参数共享（Bilen 和 Vedaldi，2016 年；Misra 等人，2016 年；Rudd 等人，2016 年；Yang 和 Hospedales，2016 年；Kokkinos， 2017 年；Zamir 等人，2018 年），自然语言处理（Collobert 和 Weston，2008 年；Dong 等人，2015 年；Liu 等人，2015a；Luong 等人，2015 年；Hashimoto 等人，2017 年），语音处理（Huang 等人，2013 年；Seltzer 和 Droppo，2013 年；Huang 等人，2015 年），甚至在多种模式上看似不相关的领域（Kaiser 等人，2017 年）。Baxter (2000) 从理论上将 多任务学习 问题分析为个体学习者与元算法之间的交互。每个学习者负责一项任务，元算法决定共享参数的更新方式。所有上述 多任务学习 算法都使用加权求和作为元算法。还探索了超越加权求和的元算法。李等。 (2014) 考虑每个学习者都基于内核学习并利用多目标优化的情况。 Zhang 和 Yeung (2010) 考虑每个学习者都是线性模型并使用任务亲和矩阵的情况。周等。 (2011a) 和 Bagherjeiran 等人。 (2005) 使用任务共享字典的假设并开发类似期望最大化的元算法。德米兰达等人。 (2012) 和 Zhou 等人。 (2017b) 使用群体优化。这些方法都不适用于现代深度网络等高容量模型的基于梯度的学习。肯德尔等人。 (2018) 和 Chen 等人。 (2018) 分别提出基于不确定性和梯度幅度的启发式方法，并将其方法应用于卷积神经网络。最近的另一项工作使用多智能体强化学习（Rosenbaum 等人，2017 年）。

多目标优化：多目标优化解决了优化一组可能对比目标的问题。本文推荐 Miettinen (1998) 和 Ehrgott (2005) 对该领域的调查。与本文的工作特别相关的是基于梯度的多目标优化，由 Fliege 和 Svaiter (2000)、Schäffler 等人开发。 (2002) 和德西德里 (2012)。这些方法使用多目标 Karush-Kuhn-Tucker (KKT) 条件（Kuhn 和 Tucker，1951 年）并找到降低所有目标的下降方向。 Peitz 和 Dellnitz（2018 年）以及 Poirion 等人将这种方法扩展到随机梯度下降。 (2017)。在机器学习中，这些方法已应用于多智能体学习（Ghosh 等人，2013 年；Pirotta 和 Restelli，2016 年；Parisi 等人，2014 年）、内核学习（Li 等人，2014 年）、顺序决策制定 （Roijers 等人，2013 年）和贝叶斯优化（Shah 和 Ghahramani，2016 年；Hernández-Lobato 等人，2016 年）。本文的工作将基于梯度的多目标优化应用于多任务学习。

[(40条消息) 精读论文：Multi-Task Learning as Multi-Objective Optimization(附翻译)_菜菜的小孙同学的博客-CSDN博客](https://blog.csdn.net/m0_38088084/article/details/108009616)

[论文笔记：Multi-Task Learning as Multi-Objective Optimization | Just for Life. (muyuuuu.github.io)](https://muyuuuu.github.io/2020/12/05/多任务学习-to-MOO/)
