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
lastmod: 2022-11-20 12:55:57
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

斯坦因悖论是探索多任务学习 (MTL) (Caruana, 1997) 的早期启发。多任务学习是一种学习范式，通过使用来自多个任务的数据，寄希望于获得优于独立学习每个任务的性能。多任务学习的潜在优势超出了斯坦因悖论的直接影响，因为现实世界中即使看似无关的任务也由于数据产生的共享过程而存在很强的依赖性。例如，虽然自动驾驶任务和对象操纵任务看似无关，但其底层数据都受相同的光学规律、材料特性和动力学定律影响。这启发了人们将多项任务作为学习系统中的归纳偏置（inductive bias）。

典型的多任务学习系统的输入通常为一组输入点集合以及每点在不同任务中的目标集。多任务联合求解，然后共享归纳偏置。常见的一种跨任务共享归纳偏置（inductive bias）的设置方法为设计一个参数化的假设类，让其在不同任务之间共享一些参数。一般而言，可以通过最小化每个任务的经验风险的加权和，来学习到这些参数。然而，这种线性加权的方式仅在共享参数对所有任务都有效时才有意义。换言之，最小化经验风险加权和的方式仅在这些任务的学习不存在竞争关系时才有效，而这种情况很少见。对于任务目标存在冲突的多任务学习，需要对不同任务之间的权衡进行建模，而这超出了线性组合的能力范畴。

多任务学习的另一个目标是找到一个不受任何其它方案主导的解决方案。在本文中，本文将多任务学习的目标定为寻找帕累托最优解。在给定多个条件的情况下寻找帕累托最优解的问题称为多目标优化。目前已有多种用于多目标优化的算法。

一种方法是多梯度下降算法 (MGDA)，该算法基于梯度下降的方法，通过使用每个任务的梯度并解决优化问题来更新共享参数，并可证明帕累托集合上的点是收敛的(Désidéri, 2012)。 MGDA 非常适合深层网络的多任务学习，然而，有两个技术性问题阻碍了 MGDA 的大规模应用。(i) 随着任务数量和梯度维度的增加，传统的底层优化方法会存在问题，导致模型的扩展性很差。 (ii) 该算法需要计算每个任务的梯度，从而导致反向传播的计算次数随任务数而线性增加，增加了训练时间。

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

或者（Alternatively），将多任务学习转换为多目标优化 ：optimizing a collection of possibly conflicting objectives. This is the approach we take. We specify the multi-objective optimization formulation of MTL using a vector-valued loss $\mathbf{L}$ :

$$
\min _{\substack{\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}, \ldots, \boldsymbol{\theta}^{T}}} \mathbf{L}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}, \ldots, \boldsymbol{\theta}^{T}\right)=\min _{\substack{\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}, \ldots, \boldsymbol{\theta}^{T}}}\left(\hat{\mathcal{L}}^{1}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}\right), \ldots, \hat{\mathcal{L}}^{T}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{T}\right)\right)^{\top}
$$

The goal of multi-objective optimization is achieving Pareto optimality.

Definition 1 (Pareto optimality for MTL)

(a) A solution $\boldsymbol{\theta}$ dominates a solution $\overline{\boldsymbol{\theta}}$ if $\hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{\text {sh }}, \boldsymbol{\theta}^{t}\right) \leq \hat{\mathcal{L}}^{t}\left(\overline{\boldsymbol{\theta}}^{\text {sh }}, \overline{\boldsymbol{\theta}}^{t}\right)$ for all tasks $t$ and $\mathbf{L}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}, \ldots, \boldsymbol{\theta}^{T}\right) \neq \mathbf{L}\left(\overline{\boldsymbol{\theta}}^{s h}, \overline{\boldsymbol{\theta}}^{1}, \ldots, \overline{\boldsymbol{\theta}}^{T}\right)$

(b) A solution $\boldsymbol{\theta}^{\star}$ is called Pareto optimal if there exists no solution $\boldsymbol{\theta}$ that dominates $\boldsymbol{\theta}^{\star}$ .

The set of Pareto optimal solutions is called the Pareto set $\left(\mathcal{P}_{\boldsymbol{\theta}}\right)$ and its image is called the Pareto front $\left(\mathcal{P}_{\mathbf{L}}=\{\mathbf{L}(\boldsymbol{\theta})\}_{\boldsymbol{\theta} \in \mathcal{P}_{\boldsymbol{\theta}}}\right)$ . In this paper, we focus on gradient-based multi-objective optimization due to its direct relevance to gradient-based MTL.

In the rest of this section, we first summarize in Section $3.1$ how multi-objective optimization can be performed with gradient descent. Then, we suggest in Section 3.2 a practical algorithm for performing multi-objective optimization over very large parameter spaces. Finally, in Section $3.3$ we propose an efficient solution for multi-objective optimization designed directly for high-capacity deep networks. Our method scales to very large models and a high number of tasks with negligible overhead.

${ }^{1}$ This definition can be extended to the partially-labelled case by extending $\mathcal{Y}^{t}$ with a null label. 

Multiple Gradient Descent Algorithm

As in the single-objective case, multi-objective optimization can be solved to local optimality via gradient descent. In this section, we summarize one such approach, called the multiple gradient descent algorithm (MGDA) (Désidéri, 2012). MGDA leverages the Karush-Kuhn-Tucker (KKT) conditions, which are necessary for optimality (Fliege and Svaiter, 2000; Schäffler et al. 2002; Désidéri, 2012). We now state the KKT conditions for both task-specific and shared parameters:

- There exist $\alpha^{1}, \ldots, \alpha^{T} \geq 0$ such that $\sum_{t=1}^{T} \alpha^{t}=1$ and $\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)=0$

- For all tasks $t, \nabla_{\boldsymbol{\theta}^{t}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)=0$

Any solution that satisfies these conditions is called a Pareto stationary point. Although every Pareto optimal point is Pareto stationary, the reverse may not be true. Consider the optimization problem

$$
\min _{\alpha^{1}, \ldots, \alpha^{T}}\left\{\left\|\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)\right\|_{2}^{2} \mid \sum_{t=1}^{T} \alpha^{t}=1, \alpha^{t} \geq 0 \quad \forall t\right\}
$$

Désidéri (2012) showed that either the solution to this optimization problem is 0 and the resulting point satisfies the KKT conditions, or the solution gives a descent direction that improves all tasks. Hence, the resulting MTL algorithm would be gradient descent on the task-specific parameters followed by solving 3 and applying the solution $\left(\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}}\right)$ as a gradient update to shared parameters. We discuss how to solve 33 for an arbitrary model in Section $3.2$ and present an efficient solution when the underlying model is an encoder-decoder in Section $3.3$

Solving the Optimization Problem

The optimization problem defined in 3 is equivalent to finding a minimum-norm point in the convex hull of the set of input points. This problem arises naturally in computational geometry: it is equivalent to finding the closest point within a convex hull to a given query point. It has been studied extensively (Makimoto et al. 1994 Wolfe 1976 Sekitani and Yamamoto 1993). Although many algorithms have been proposed, they do not apply in our setting because the assumptions they make do not hold. Algorithms proposed in the computational geometry literature address the problem of finding minimum-norm points in the convex hull of a large number of points in a low-dimensional space (typically of dimensionality 2 or 3 ). In our setting, the number of points is the number of tasks and is typically low; in contrast, the dimensionality is the number of shared parameters and can be in the millions. We therefore use a different approach based on convex optimization, since $\sqrt{3}]$ is a convex quadratic problem with linear constraints.

Before we tackle the general case, let's consider the case of two tasks. The optimization problem can be defined as $\min _{\alpha \in[0,1]}\left\|\alpha \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{1}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}\right)+(1-\alpha) \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{2}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{2}\right)\right\|_{2}^{2}$ , which is a onedimensional quadratic function of $\alpha$ with an analytical solution:

$$
\hat{\alpha}=\left[\frac{\left(\nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{2}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{2}\right)-\nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{1}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}\right)\right)^{\top} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{2}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{2}\right)}{\left\|\nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{1}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{1}\right)-\nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{2}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{2}\right)\right\|_{2}^{2}}\right]_{+, \underset{T}{1}}
$$

where $[\cdot]_{+,{ }_{T}^{1}}$ represents clipping to $[0,1]$ as $[a]_{+,{ }_{T}^{1}}=\max (\min (a, 1), 0)$ . We further visualize this solution in Figure 1. Although this is only applicable when $T=2$ , this enables efficient application of the Frank-Wolfe algorithm (Jaggi, 2013) since the line search can be solved analytically. Hence, we use Frank-Wolfe to solve the constrained optimization problem, using (4) as a subroutine for the line search. We give all the update equations for the Frank-Wolfe solver in Algorithm 2 

![](https://cdn.mathpix.com/cropped/2022_11_19_76f32b82e44c9de424c3g-3.jpg?height=312&width=918&top_left_y=240&top_left_x=365)

Figure 1: Visualisation of the min-norm point in the convex hull 6 : of two points $\left(\min _{\gamma \in[0,1]}\|\gamma \boldsymbol{\theta}+(1-\gamma) \overline{\boldsymbol{\theta}}\|_{2}^{2}\right)$ . As the geometry suggests, the solution is either an edge case or a perpendicular vector.

![](https://cdn.mathpix.com/cropped/2022_11_19_76f32b82e44c9de424c3g-3.jpg?height=400&width=428&top_left_y=256&top_left_x=1308)

![](https://cdn.mathpix.com/cropped/2022_11_19_76f32b82e44c9de424c3g-3.jpg?height=711&width=1397&top_left_y=720&top_left_x=362)

Efficient Optimization for Encoder-Decoder Architectures

The MTL update described in Algorithm 2 is applicable to any problem that uses optimization based on gradient descent. Our experiments also suggest that the Frank-Wolfe solver is efficient and accurate as it typically converges in a modest number of iterations with negligible effect on training time. However, the algorithm we described needs to compute $\nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{\text {sh }}, \boldsymbol{\theta}^{t}\right)$ for each task $t$ , which requires a backward pass over the shared parameters for each task. Hence, the resulting gradient computation would be the forward pass followed by $T$ backward passes. Considering the fact that computation of the backward pass is typically more expensive than the forward pass, this results in linear scaling of the training time and can be prohibitive for problems with more than a few tasks.

We now propose an efficient method that optimizes an upper bound of the objective and requires only a single backward pass. We further show that optimizing this upper bound yields a Pareto optimal solution under realistic assumptions. The architectures we address conjoin a shared representation function with task-specific decision functions. This class of architectures covers most of the existing deep MTL models and can be formally defined by constraining the hypothesis class as

$$
f^{t}\left(\mathbf{x} ; \boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)=\left(f^{t}\left(\cdot ; \boldsymbol{\theta}^{t}\right) \circ g\left(\cdot ; \boldsymbol{\theta}^{s h}\right)\right)(\mathbf{x})=f^{t}\left(g\left(\mathbf{x} ; \boldsymbol{\theta}^{s h}\right) ; \boldsymbol{\theta}^{t}\right)
$$

where $g$ is the representation function shared by all tasks and $f^{t}$ are the task-specific functions that take this representation as input. If we denote the representations as $\mathbf{Z}=\left(\mathbf{z}_{1}, \ldots, \mathbf{z}_{N}\right)$ , where $\mathbf{z}_{i}=g\left(\mathbf{x}_{i} ; \boldsymbol{\theta}^{s h}\right)$ , we can state the following upper bound as a direct consequence of the chain rule:

$$
\left\|\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)\right\|_{2}^{2} \leq\left\|\frac{\partial \mathbf{Z}}{\partial \boldsymbol{\theta}^{s h}}\right\|_{2}^{2}\left\|\sum_{t=1}^{T} \alpha^{t} \nabla_{\mathbf{Z}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)\right\|_{2}^{2}
$$

where $\left\|\frac{\partial \mathbf{Z}}{\partial \boldsymbol{\theta}^{s h}}\right\|_{2}$ is the matrix norm of the Jacobian of $\mathbf{Z}$ with respect to $\boldsymbol{\theta}^{\text {sh }}$ . Two desirable properties of this upper bound are that (i) $\nabla_{\mathbf{Z}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)$ can be computed in a single backward pass for all tasks and (ii) $\left\|\frac{\partial \mathbf{Z}}{\partial \boldsymbol{\theta}^{s h}}\right\|_{2}^{2}$ is not a function of $\alpha^{1}, \ldots, \alpha^{T}$ , hence it can be removed when it is used as an optimization objective. We replace the $\left\|\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)\right\|_{2}^{2}$ term with the upper bound we have just derived in order to obtain the approximate optimization problem and drop the $\left\|\frac{\partial \mathbf{Z}}{\partial \theta^{s h}}\right\|_{2}^{2}$ term since it does not affect the optimization. The resulting optimization problem is

$$
\min _{\alpha^{1}, \ldots, \alpha^{T}}\left\{\left\|\sum_{t=1}^{T} \alpha^{t} \nabla_{\mathbf{Z}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)\right\|_{2}^{2} \mid \sum_{t=1}^{T} \alpha^{t}=1, \alpha^{t} \geq 0 \quad \forall t\right\}
$$

We refer to this problem as MGDA-UB (Multiple Gradient Descent Algorithm - Upper Bound). In practice, MGDA-UB corresponds to using the gradients of the task losses with respect to the representations instead of the shared parameters. We use Algorithm 2 with only this change as the final method.

Although MGDA-UB is an approximation of the original optimization problem, we now state a theorem that shows that our method produces a Pareto optimal solution under mild assumptions. The proof is given in the supplement.

Theorem 1 Assume $\frac{\partial \mathrm{Z}}{\partial \theta^{\text {sh }}}$ is full-rank. If $\alpha^{1, \ldots, T}$ is the solution of MGDA-UB, one of the following is true:

(a) $\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)=0$ and the current parameters are Pareto stationary.

(b) $\sum_{t=1}^{T} \alpha^{t} \nabla_{\boldsymbol{\theta}^{s h}} \hat{\mathcal{L}}^{t}\left(\boldsymbol{\theta}^{s h}, \boldsymbol{\theta}^{t}\right)$ is a descent direction that decreases all objectives.

This result follows from the fact that as long as $\frac{\partial \mathbf{Z}}{\partial \theta \text { sh }}$ is full rank, optimizing the upper bound corresponds to minimizing the norm of the convex combination of the gradients using the Mahalonobis norm defined by $\frac{\partial Z}{\partial \theta^{s h}}{ }^{\top} \frac{\partial Z}{\partial \theta^{s h}}$ . The non-singularity assumption is reasonable as singularity implies that tasks are linearly related and a trade-off is not necessary. In summary, our method provably finds a Pareto stationary point with negligible computational overhead and can be applied to any deep multi-objective problem with an encoder-decoder model.

## 引文

多任务学习：本文总结了与本文最密切相关的工作，并向感兴趣的读者推荐 Ruder (2017) 和 Zhou 等人的评论。 (2011b) 了解更多背景信息。多任务学习 (MTL) 通常通过硬或软参数共享进行。在硬参数共享中，参数的一个子集在任务之间共享，而其他参数是特定于任务的。在软参数共享中，所有参数都是特定于任务的，但它们通过贝叶斯先验 (Xue et al., 2007; Bakker and Heskes, 2003) 或联合字典 (Argyriou et al., 2007; Long and Wang, 2015) 共同约束；Yang 和 Hospedales，2016 年；罗德，2017 年）。继深度 MTL 在计算机视觉领域取得成功后，本文专注于基于梯度优化的硬参数共享（Bilen 和 Vedaldi，2016 年；Misra 等人，2016 年；Rudd 等人，2016 年；Yang 和 Hospedales，2016 年；Kokkinos， 2017 年；Zamir 等人，2018 年），自然语言处理（Collobert 和 Weston，2008 年；Dong 等人，2015 年；Liu 等人，2015a；Luong 等人，2015 年；Hashimoto 等人，2017 年），语音处理（Huang 等人，2013 年；Seltzer 和 Droppo，2013 年；Huang 等人，2015 年），甚至在多种模式上看似不相关的领域（Kaiser 等人，2017 年）。Baxter (2000) 从理论上将 MTL 问题分析为个体学习者与元算法之间的交互。每个学习者负责一项任务，元算法决定共享参数的更新方式。所有上述 MTL 算法都使用加权求和作为元算法。还探索了超越加权求和的元算法。李等。 (2014) 考虑每个学习者都基于内核学习并利用多目标优化的情况。 Zhang 和 Yeung (2010) 考虑每个学习者都是线性模型并使用任务亲和矩阵的情况。周等。 (2011a) 和 Bagherjeiran 等人。 (2005) 使用任务共享字典的假设并开发类似期望最大化的元算法。德米兰达等人。 (2012) 和 Zhou 等人。 (2017b) 使用群体优化。这些方法都不适用于现代深度网络等高容量模型的基于梯度的学习。肯德尔等人。 (2018) 和 Chen 等人。 (2018) 分别提出基于不确定性和梯度幅度的启发式方法，并将其方法应用于卷积神经网络。最近的另一项工作使用多智能体强化学习（Rosenbaum 等人，2017 年）。

多目标优化：多目标优化解决了优化一组可能对比目标的问题。本文推荐 Miettinen (1998) 和 Ehrgott (2005) 对该领域的调查。与本文的工作特别相关的是基于梯度的多目标优化，由 Fliege 和 Svaiter (2000)、Schäffler 等人开发。 (2002) 和德西德里 (2012)。这些方法使用多目标 Karush-Kuhn-Tucker (KKT) 条件（Kuhn 和 Tucker，1951 年）并找到降低所有目标的下降方向。 Peitz 和 Dellnitz（2018 年）以及 Poirion 等人将这种方法扩展到随机梯度下降。 (2017)。在机器学习中，这些方法已应用于多智能体学习（Ghosh 等人，2013 年；Pirotta 和 Restelli，2016 年；Parisi 等人，2014 年）、内核学习（Li 等人，2014 年）、顺序决策制定 （Roijers 等人，2013 年）和贝叶斯优化（Shah 和 Ghahramani，2016 年；Hernández-Lobato 等人，2016 年）。本文的工作将基于梯度的多目标优化应用于多任务学习。

[(40条消息) 精读论文：Multi-Task Learning as Multi-Objective Optimization(附翻译)_菜菜的小孙同学的博客-CSDN博客](https://blog.csdn.net/m0_38088084/article/details/108009616)

[论文笔记：Multi-Task Learning as Multi-Objective Optimization | Just for Life. (muyuuuu.github.io)](https://muyuuuu.github.io/2020/12/05/MTL-to-MOO/)
