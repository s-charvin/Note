---
title: "Dynamic Snake Convolution based on Topological Geometric Constraints for Tubular Structure Segmentation"
description: ""
citekey: qiDynamicSnakeConvolution2023
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-10-23 21:06:39
lastmod: 2023-10-24 10:11:17
---

> [!info] 论文信息
>1. Title：Dynamic Snake Convolution based on Topological Geometric Constraints for Tubular Structure Segmentation
>2. Author：Yaolei Qi, Yuting He, Xiaoming Qi, Yuan Zhang, Guanyu Yang
>3. Entry：[Zotero link](zotero://select/items/@qiDynamicSnakeConvolution2023) [URL link](http://arxiv.org/abs/2307.08388) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Qi et al_2023_Dynamic Snake Convolution based on Topological Geometric Constraints for.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\LHFXHBSE\\2307.html>)
>4. Other：2023 - arxiv:2307.08388     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- :fas_question:   
- :obs_pdf_file:   
- :obs_graph_glyph:   
- :obs_wand_glyph:   

## 摘要

> [!abstract] Accurate segmentation of topological tubular structures, such as blood vessels and roads, is crucial in various fields, ensuring accuracy and efficiency in downstream tasks. However, many factors complicate the task, including thin local structures and variable global morphologies. In this work, we note the specificity of tubular structures and use this knowledge to guide our DSCNet to simultaneously enhance perception in three stages: feature extraction, feature fusion, and loss constraint. First, we propose a dynamic snake convolution to accurately capture the features of tubular structures by adaptively focusing on slender and tortuous local structures. Subsequently, we propose a multi-view feature fusion strategy to complement the attention to features from multiple perspectives during feature fusion, ensuring the retention of important information from different global morphologies. Finally, a continuity constraint loss function, based on persistent homology, is proposed to constrain the topological continuity of the segmentation better. Experiments on 2D and 3D datasets show that our DSCNet provides better accuracy and continuity on the tubular structure segmentation task compared with several methods. Our codes will be publicly available.

> 血管、道路等拓扑管状结构的精确分割在各个领域都至关重要，可确保下游任务的准确性和效率。然而，许多因素使任务变得复杂，包括薄的局部结构和可变的全局形态。在这项工作中，我们注意到管状结构的特殊性，并利用这些知识来指导我们的 DSCNet 在三个阶段同时增强感知：特征提取、特征融合和损失约束。首先，我们提出了一种动态蛇卷积，通过自适应地关注细长和曲折的局部结构来准确捕获管状结构的特征。随后，我们提出了一种多视图特征融合策略，以补充特征融合过程中多角度对特征的关注，确保保留来自不同全局形态的重要信息。最后，提出了一种基于持久同源性的连续性约束损失函数，以更好地约束分割的拓扑连续性。 2D 和 3D 数据集上的实验表明，与多种方法相比，我们的 DSCNet 在管状结构分割任务上提供了更好的准确性和连续性。我们的代码是公开可用的1。

## 预处理

## 概述

## 结果

## 精读

对拓扑管状结构的准确分割在多个领域都至关重要，以确保下游任务的精度和效率。在临床应用中，良好界定的血管是计算流体动力学的关键前提，并协助放射科医生定位和诊断病变 [13, 16]。在遥感应用中，完整的道路分割为路线规划提供了坚实的基础。不论在哪个领域，这些结构都共同具有薄弱和弯曲的特点，由于它们在图像中的比例小，因此难以捕捉。因此，迫切需要增强对细小管状结构的感知。

但由于以下困难，这仍然是一个挑战：(1) 薄弱和脆弱的局部结构。如图1所示，细小结构只占总体图像的很小一部分，且像素组成有限。此外，这些结构容易受到复杂背景的干扰，使模型难以精确区分微妙的目标变化。因此，模型可能难以区分这些结构，导致分割的断裂。(2) 复杂和变化的全局形态。图1显示了细小管状结构的复杂和变化的形态，即使在同一图像内。位于不同区域的目标观察到形态变化，这取决于分支数量、分叉位置和路径长度。当数据展现出前所未有的形态结构时，模型可能倾向于过拟合已经看到的特征，导致弱化的泛化。

最近，许多研究提议结合领域知识（例如几何拓扑和树结构）来更好地指导模型感知管状结构的独特特征，从而集中于提高局部分割的准确性并维持全局形态的连续性。现有方法可以大致分为三类：(1) 基于网络的方法[7, 12, 31, 28, 14, 8] 根据管状结构的特性设计特定的网络架构，指导模型关注关键特性。但考虑到管状结构的小比例，网络可能不可避免地失去对应结构的感知。(2) 基于特征的方法[21, 33, 15, 35, 20] 通过为模型提供额外的特征表示来增强对管状结构特定几何和拓扑特征的理解。然而，一些多余的特征表示增加了计算负担，而没有对模型产生积极的影响。(3) 基于损失的方法[24, 29, 1, 30] 在训练过程中引入测量方法来补充约束，通常通过损失函数。这些方法加强了对分割的严格约束。基于此基础，从拓扑角度结合连续性约束的结构化损失可能进一步提高管状分割的准确性。

为了应对上述障碍，我们提出了一个新颖的框架，DSCNet，涉及到一个**管状感知的卷积核**、**多视图特征融合策略**和**拓扑连续性约束损失函数**。
(1) 为了应对模型难以关注的细小和脆弱的局部结构的小比例的挑战，我们提出动态蛇形卷积(DSConv) 来增强对几何结构的感知，通过自适应地关注管状结构的细小和曲线局部特征。
(2) 为了应对复杂和变化的全局形态的挑战，我们提出了一种多视图特征融合策略。在此方法中，我们基于 DSConv 生成多个形态核模板，从多个角度查看目标的结构特征，并通过总结典型的关键特征实现有效的特征融合。
(3) 为了应对管状结构分割容易断裂的问题，我们提出了基于持续同胚(TCLoss)的拓扑连续性约束损失函数。PH[9, 19, 5] 对拓扑特征从出现到消失的过程进行响应。它从嘈杂的高维数据中获取充足的拓扑信息。相关的 Betti 数是描述拓扑空间中连通性的一种方式。与[30, 10]不同，我们的 TCLoss 结合了 PH 与点集相似性，引导网络关注于异常像素/体素分布的断裂区域，从拓扑角度实现连续性约束。

总之，我们的工作提出了一个知识融合的新颖框架，解决了细小管状结构的难题，具体的贡献有三个方面：(1) 我们提出了动态蛇形卷积，自适应地关注瘦长和曲折的局部特征，在2D 和3D 数据集上实现准确的管状结构分割。我们的模型已经通过内部和外部测试数据进行了全面验证。(2) 我们提出了一种多视角特征融合策略，补充了对多视角的关键特征的注意力。(3) 我们提出了基于持续同胚的拓扑连续性约束损失函数，更好地约束了分割的连续性。

2. 相关工作
2.1 基于网络设计的方法
为了更好地根据管状结构的形态设计特定的网络架构和模块，提出了各种方法来实现更好的性能。 (1) 基于卷积核设计的方法，代表性的有著名的扩张卷积[32]和可变形卷积[6]，它们被提出来处理CNNs中固有的有限几何变换，这些方法在复杂的检测和分割任务上表现出色。这些方法[7, 34, 12, 31]也被设计来动态地感知对象的几何特征，以适应形态可变的结构。例如，在[12]中提出的DUNet将可变形卷积集成到U形结构中，并根据血管的规模和形状自适应地调整感受野。(2) 基于网络架构设计的方法被提出来学习管状结构的特殊几何拓扑特征。PointScatter[28]被提出来以点集来表示管状结构，这是对提取管状结构的分割模型的一个替代方法。[14]提出了一种树形结构的卷积门控循环单元来明确地模拟冠状动脉的拓扑结构。与上述完全自由地让模型学习几何变化的思想不同，考虑到过多的随机性导致的收敛困难的局限性和模型可能会关注目标的意外区域的可能性。我们的工作整合了管状结构形态的领域知识，以稳定地增强在特征提取过程中对管状结构的感知。

2.2 基于特征融合的方法
基于特征融合的方法[35, 15, 33, 21, 20]通过向模型补充额外的特征信息来增强对管状结构的表示。考虑到管状结构的拓扑和稀疏性，[35]提出了一个跨网络的多尺度特征融合方法，该方法在两个网络之间进行，有效地支持高质量的血管分割。在[15]中，研究了一个全局变换器和双局部注意力网络，通过深浅层次特征融合来同时捕获全局和局部特性。[33]提议融合上下文解剖信息和血管拓扑来实现准确的管状结构分割。在我们的工作中，我们提出了一种多角度特征融合策略，以补充对来自多个视角的关键特征的注意力。在这种策略中，我们基于我们的DSConv生成大量的形态核模板，从多个角度观察目标的结构特性，并通过总结基本的标准特征来实现特征融合，从而提高我们模型的性能。

2.3 基于损失函数的方法
基于损失函数的方法[24, 29, 1]引入测量方法在训练过程中补充约束。这些方法加强了对管状结构分割的严格约束。[24]引入了一个称为中心线骰子的相似性测量，该测量是基于分割掩码和骨架的交集计算的。[29]提出了一个几何感知的管状结构分割方法，深度距离变换(DDT)，该方法结合了来自经典距离变换的骨架化和管状结构分割的直觉。这些方法关注管状结构分割的连续性，但骨架的不准确性和偏移会影响约束的精度。[1]提出了一个相似性指数，该指数捕获了预测分割的拓扑一致性，并设计了一个基于形态闭合运算符的管状结构分割的损失函数。在[30]中，将拓扑数据分析方法与几何深度学习模型结合，用于3D对象的细粒度分割。这些方法将捕获拓扑对象的特征。从中得到启示，我们的工作提出了一个拓扑连续性约束损失函数(TCLoss)，该函数从拓扑角度更好地约束分割的连续性。我们的TCLoss在训练过程中逐渐引入基于持续同胚[27, 2]的约束，以引导网络关注断裂区域并实现连续性。

3. 方法学
我们的方法旨在同时处理2D 和3D 特征图的细管状结构。为了简化，我们的模块在2D 中描述，并在我们的开源中也提供了详细的扩展到3D 的方法。

3.1.动态蛇卷积

在本节中，我们讨论如何执行动态蛇形卷积（DSConv）来提取管状结构的局部特征。给定标准的2D卷积坐标为 $K$，中心坐标为 $K_i=\left(x_i, y_i\right)$。具有膨胀度为1的 $3 \times 3$ 核 $K$ 表示为：
$$
K=\{(x-1, y-1),(x-1, y), \cdots,(x+1, y+1)\}
$$

为了让卷积核更有灵活性地关注目标的复杂几何特征，受到[6]的启发，我们引入了变形偏移量 $\Delta$。但是，如果模型自由学习变形偏移，感知场往往会偏离目标，尤其是在细管状结构的情况下。因此，我们使用迭代策略（见图[3]），轮流选择要处理的每个目标中要观察的下一个位置，从而确保注意力的连续性，并且由于大的变形偏移而不使感知场扩散得过远。

![]({60}_Dynamic%20Snake%20Convolution%20based%20on%20Topological%20Geometric%20Constraints%20for%20Tubular%20Structure%20Segmentation@qiDynamicSnakeConvolution2023.assets/image-20231024095610.png)

图 3. 左： DSConv 坐标计算的图示。右：DSConv 的感受野。


在DSConv中，我们在 $\mathrm{x}$-轴和 $\mathrm{y}$-轴的方向上直线化标准卷积核。我们考虑一个大小为9的卷积核，并以$x$轴方向为例，$K$中每个网格的具体位置表示为：$K_{i \pm c}=\left(x_{i \pm c}, y_{i \pm c}\right)$，其中 $c=\{0,1,2,3,4\}$ 表示从中心网格到水平距离。卷积核 $K$ 中每个网格位置 $K_{i \pm c}$ 的选择是一个累积过程。从中心位置 $K_i$ 开始，离中心网格的位置取决于前一个网格的位置：与 $K_i$ 相比，$K_{i+1}$ 增加了一个偏移量 $\Delta=\{\delta \mid \delta \in[-1,1]\}$。因此，偏移需要为 $\Sigma$，从而确保卷积核符合线性形态结构。在 $\mathrm{x}$-轴的方向上的图 3 变为：
$$
K_{i \pm c}=\left\{\begin{array}{l}
\left(x_{i+c}, y_{i+c}\right)=\left(x_i+c, y_i+\Sigma_i^{i+c} \Delta y\right), \\
\left(x_{i-c}, y_{i-c}\right)=\left(x_i-c, y_i+\Sigma_{i-c}^i \Delta y\right),
\end{array}\right.
$$
而在 $y$-轴方向的方程2变为：
$$
K_{j \pm c}=\left\{\begin{array}{l}
\left(x_{j+c}, y_{j+c}\right)=\left(x_j+\Sigma_j^{j+c} \Delta x, y_j+c\right), \\
\left(x_{j-c}, y_{j-c}\right)=\left(x_j+\Sigma_{j-c}^j \Delta x, y_j-c\right),
\end{array}\right.
$$

由于偏移 $\Delta$ 通常是小数，所以实施了双线性插值：
$$
K=\Sigma_{K^{\prime}} B\left(K^{\prime}, K\right) \cdot K^{\prime}
$$

其中 $K$ 表示方程 2 和方程 $3$ 的分数位置，$K^{\prime}$ 列举所有整数空间位置，$B$ 是双线性插值核，并且它被分为两个一维核，如下所示：
$$
B\left(K, K^{\prime}\right)=b\left(K_x, K_x^{\prime}\right) \cdot b\left(K_y, K_y^{\prime}\right)
$$

如图 3 所示，由于二维（x轴，y轴）变化，我们的 DSConv 在变形过程中覆盖了一个 $9 \times 9$ 的范围。DSConv 旨在根据动态结构更好地适应纤细的管状结构，从而更好地感知关键特征。

3.2. 多视角特征融合策略

本节讨论实施多视角特征融合策略，以指导模型从多个视角补充关注关键特征。对于每个 $K$，从层 $l$ 提取两个特征图 $f^l\left(K_x\right)$ 和 $f^l\left(K_y\right)$ 从x轴和y轴，表示为：
$$
f^l(K)=\{\underbrace{\Sigma_i w\left(K_i\right) \cdot f^l\left(K_i\right)}_{f^l\left(K_x\right)}, \underbrace{\Sigma_j w\left(K_j\right) \cdot f^l\left(K_j\right)}_{f^l\left(K_y\right)}\}
$$
其中 $w\left(K_i\right)$ 表示位置 $K_i$ 的权重，由 $l$-th 层卷积核 $K$ 提取的特征使用累积方法计算。

基于方程 6 ，我们提取 $m$ 组特征作为 $T^l$，其中包含 DSConv 的不同形态：
$$
T^l=(\underbrace{f^l\left(K_x\right), f^l\left(K_y\right)}_{T_1^l}, \underbrace{f^l\left(K_x\right), f^l\left(K_y\right)}_{T_2^l}, \cdots \underbrace{f^l\left(K_x\right), f^l\left(K_y\right)}_{T_m^l})
$$

多模板的特征融合必然会带来冗余噪声。因此，在训练阶段引入了随机丢弃策略 $r^l$（见图 &），以提高我们模型的性能，并在不增加额外计算负担的情况下防止过拟合，然后方程 7 变为：
$$
\left\{\begin{array}{l}
r^l \sim \operatorname{Bernoulli}(p) \\
\hat{T}^l=r^l \cdot T^l \\
f^{l+1}(K)=\Sigma^{\lfloor m \times p\rfloor} \hat{T}_t^l
\end{array}\right.
$$
其中 $p$ 是随机丢弃的概率，且 $r^l$ 满足 Bernoulli 分布。在训练阶段保存最佳的丢弃策略，并指导模型在测试阶段融合关键特征。






3.3.拓扑连续性约束损失

在本节中，我们讨论如何实现基于持久同调的拓扑连续性约束损失（TCLoss）来约束分割的连续性。复杂结构中的几何和拓扑信息是帮助模型理解连续结构的关键线索。采用拓扑数据分析工具来提取隐藏在复杂管状结构中的基本特征。

我们的目标是构建数据的拓扑并提取复杂管状结构中的高维关系，表示为持久性条形码和持久性同源性 (PH)，如图 5 所示。

给定 G，其 N 维拓扑结构，同调类 [9, 19] 是 N 流形的等价类，可以在 G 内相互变形，其中 0 维和 1 维是连通分量和句柄。 PH用于计算拓扑特征的演化，并保持拓扑特征的出现时间b和消失时间d之间的周期[30]。这些时期总结为

这种格式称为持久图 (PD)，它由一组点 (b, d) 组成。每个点 (b, d) 代表在 b 处出现并在 d 处消失的第 d 个同源类。令 P D = dgm(·) 表示从真实值 L 和输出 O 获得的持久同源性。我们考虑复杂管状结构中的拓扑信息，其中包含确定裂缝是否存在的关键线索，在同伦特征中很明显0维和1维同调特征。现有方法[30,5,10]使用修正的Wasserstein距离来计算输出生成的点与groundtruth生成的点之间的最佳匹配，而没有最佳配对的离群点被匹配到对角线并且不参与在损失计算中。然而，在我们的任务中，离群点代表异常出现或消失的时间，并暗示错误的拓扑关系发挥了重要作用。因此，我们使用Hausdorff距离来衡量两组点之间的相似度[26]：


其中 PO ∈ Dgm(O) 、 PL ∈ Dgm(L) 和 d* H 表示双向 Hausdorff 距离，以 n 维点计算。我们使用的豪斯多夫距离对异常值很敏感。如式9所示，如果两组点相似，除了PO中只有一个点远离PH中的任何点外，所有点都完美叠加，则豪斯多夫距离由该点决定，并且很大[11 ]。


然后对所有维度（n=0,1,2,····,N）求和得到LP H，并将整个TCLoss与交叉熵损失LCE积分作为最终损失函数LT C = LCE + PN n=0 d* H。

最后，拓扑和精度受到两个损失函数的综合作用的约束，有助于连续的管状分割。






4. 实验配置
4.1. 数据集
我们使用三个数据集，包括两个公开数据集和一个内部数据集，以验证我们的框架。在2D上，我们评估DRIVE视网膜数据集[25]和马萨诸塞州道路数据集[17]。在3D上，我们使用名为Cardiac CCTA Data的数据集。关于实验设置的详细信息可以在补充材料中找到。

4.2. 评估
我们进行了比较实验和消融研究，以展示我们提议的框架的优势。为了验证准确性，我们比较了经典的分割网络U-Net[4]和2021年提出的用于血管分割的CS2-Net[18]。为了验证网络设计的性能，我们比较了2022年提出的用于视网膜血管分割的DCU-net[31]。为了验证特征融合的优势，我们比较了2021年提出的用于医学图像分割的Transunet[3]。为了验证损失函数的约束，我们比较了2021年提出的clDice[24]和基于Wasserstein距离的TCLoss LW T C[30]。所有这些模型都在相同的数据集上训练，并使用以下度量标准进行评估。所有指标都是针对每张图片计算的，然后取平均。

1. 体积得分：使用Mean Dice Coefficient (Dice)、Relative-Dice coefficient (RDice)[22]、CenterlineDice (clDice)[24]、Accuracy (ACC) 和 AUC 来评估结果的性能。
2. 拓扑错误：我们遵循[24, 28]的方法，计算基于拓扑的得分，包括Betti Errors用于Betti numbers β0和β1。同时，为了客观地验证冠状动脉分割的连续性，使用overlap until first error (OF) [23]来评估提取的中心线的完整性。
3. 距离错误：Hausdorff Distance (HD) [26]也被广泛用于描述两组点之间的相似性，推荐用于评估细管状结构。

5. 结果与讨论
在这一段中，我们将从三个方面评估和分析我们提议的框架的有效性：(1) 我们提议的方法在细管状结构分割任务上的性能通过以下指标进行比较和验证。同时展示了不同方法的视觉效果。 (2) 我们分析了我们提议的DSConv引导模型关注管状结构的有效性，以及TCLoss限制分割的拓扑结构的帮助。 (3) 我们为DRIVE数据集提供了全面的实验，包括消融研究。此外，由于空间限制，我们突出显示了在其他数据集上的一些最重要的比较实验。结果显示，我们的方法在2D和3D领域都表现出色。

5.1. 定量评估
我们的方法在每个指标上的优势在表1中得到了展示，结果显示我们提议的DSCNet在2D和3D数据集上都取得了更好的结果。

在DRIVE上的评估。在DRIVE数据集上，我们的DSCNet在分割精度和拓扑连续性方面均优于其他模型。在表1中，从体积精度的角度看，我们提出的DSCNet与其他方法相比，取得了最好的分割结果，Dice为82.06%，RDice为90.17%，clDice为82.07%，ACC为96.87%，AUC为90.27%。同时，从拓扑的角度看，与其他方法相比，我们的DSCNet在β0错误为0.998和β1错误为0.803方面取得了最好

的结果。此外，在OF指标上，我们的DSCNet也达到了89.13%，显然高于其他方法。

这种性能的优势部分归因于我们提出的DSConv和TCLoss的组合。DSConv强制模型关注管状结构，从而提高了细节的捕获能力。同时，TCLoss能够限制分割的拓扑结构，从而进一步提高分割的连续性。这些因素共同作用，使得我们的方法能够在分割任务中达到出色的性能。

在其他数据集上的评估。我们还在其他数据集上进行了评估，结果显示我们的方法在各个指标上均优于其他方法。这进一步证明了我们提出的方法的鲁棒性和广泛的应用性。

6. 结论
我们提出了一个专门针对细管状结构的分割任务的新型深度学习框架。我们引入了DSConv，能够引导模型关注管状结构。此外，我们还提出了一个基于Wasserstein距离的新型损失函数，称为TCLoss，它能够限制分割结果的拓扑结构。实验结果表明，我们的方法在多个数据集上均取得了出色的性能，明显优于现有的方法。这为未来的细管状结构分割研究提供了一个有力的工具。

感谢您阅读此文，如有任何疑问，请与我们联系。

### 引文

## 摘录
