---
title: "Deformable Convolutional Networks"
description: ""
citekey: daiDeformableConvolutionalNetworks2017
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-06-06 12:02:07
lastmod: 2023-06-06 12:35:59
---

> [!info] 论文信息
>1. Title：Deformable Convolutional Networks
>2. Author：Jifeng Dai, Haozhi Qi, Yuwen Xiong, Yi Li, Guodong Zhang, Han Hu, Yichen Wei
>3. Entry：[Zotero link](zotero://select/items/@daiDeformableConvolutionalNetworks2017) [URL link](http://arxiv.org/abs/1703.06211) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Dai et al_2017_Deformable Convolutional Networks.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\PAK9RILS\\1703.html>)
>4. Other：2017 - arxiv:1703.06211     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- :fas_question:   
- :obs_pdf_file:   
- :obs_graph_glyph:   
- :obs_wand_glyph:   

## 摘要

> [!abstract] Convolutional neural networks (CNNs) are inherently limited to model geometric transformations due to the fixed geometric structures in its building modules. In this work, we introduce two new modules to enhance the transformation modeling capacity of CNNs, namely, deformable convolution and deformable RoI pooling. Both are based on the idea of augmenting the spatial sampling locations in the modules with additional offsets and learning the offsets from target tasks, without additional supervision. The new modules can readily replace their plain counterparts in existing CNNs and can be easily trained end-to-end by standard back-propagation, giving rise to deformable convolutional networks. Extensive experiments validate the effectiveness of our approach on sophisticated vision tasks of object detection and semantic segmentation. The code would be released.

> 由于其构建模块中的固定几何结构，卷积神经网络 (CNN) 本质上仅限于模拟几何变换。在这项工作中，我们引入了两个新模块来增强 CNN 的转换建模能力，即可变形卷积和可变形 RoI 池化。两者都是基于这样的想法，即在没有额外监督的情况下，使用额外的偏移量来增加模块中的空间采样位置，并从目标任务中学习偏移量。新模块可以很容易地替换现有 CNN 中的普通模块，并且可以通过标准反向传播轻松地进行端到端训练，从而产生可变形的卷积网络。广泛的实验验证了我们方法的性能。我们首次表明，在深度 CNN 中学习密集空间变换对于复杂的视觉任务（例如对象检测和语义分割）是有效的。代码发布在 https://github.com/msracver/Deformable-ConvNets。

## 预处理

## 概述

在视觉识别领域面临以下挑战

1. 如何适应对象几何变化
2. 


## 结果

## 精读

视觉识别中的一个关键挑战是如何适应对象尺度、姿势、视点和零件变形的几何变化或模型几何变换。一般来说，有两种方式。首先是构建具有足够所需变化的训练数据集。这通常通过增加现有数据样本来实现，例如，通过仿射变换。可以从数据中学习到稳健的表示，但通常以昂贵的训练和复杂的模型参数为代价。第二种是使用变换不变(旋转不变性、尺度不变性和平移不变性等属性)的特征和算法。此类别包含许多众所周知的技术，例如 SIFT（尺度不变特征变换）[42] 和基于滑动窗口的对象检测范例。

上述方式有两个缺点。 首先，假定几何变换是固定的和已知的。 此类先验知识用于扩充数据，并设计特征和算法。 这个假设阻止了对具有未知几何变换的新任务的泛化，这些任务没有被正确建模。 其次，不变特征和算法的手工设计对于过于复杂的转换可能是困难的或不可行的，即使它们是已知的。

最近，卷积神经网络 (CNN) [35] 在图像分类 [31]、语义分割 [41] 和目标检测 [16] 等视觉识别任务中取得了重大成功。尽管如此，它们仍然存在上述两个缺点。他们对几何变换建模的能力主要来自广泛的数据增强、大模型容量和一些简单的手工制作模块（例如，用于小平移不变性的最大池 [1]）。

简而言之，CNN 本质上仅限于模拟大型、未知的转换。局限性源于 CNN 模块的固定几何结构：卷积单元在固定位置对输入特征图进行采样；池化层以固定比例降低空间分辨率； RoI（感兴趣区域）池化层将 RoI 分成固定的空间箱等。缺乏处理几何变换的内部机制。这会导致明显的问题。例如，同一 CNN 层中所有激活单元的感受野大小相同。这对于在空间位置上编码语义的高级 CNN 层来说是不可取的。因为不同的位置可能对应于具有不同尺度或变形的对象，所以尺度或感受野大小的自适应确定对于具有精细定位的视觉识别是可取的，例如，使用完全卷积网络的语义分割 [41]。再举一个例子，虽然最近物体检测取得了重大而快速的进展 [16、52、15、47、46、40、7]，但所有方法仍然依赖于基于原始边界框的特征提取。这显然是次优的，特别是对于非刚性物体。

在这项工作中，我们引入了两个新模块，它们极大地增强了 CNN 建模几何变换的能力。 第一个是可变形卷积。 它将 2D 偏移量添加到标准卷积中的常规网格采样位置。 它可以使采样网格自由变形。 如图 1 所示。偏移量是通过额外的卷积层从前面的特征图中学习的。 因此，变形以局部、密集和自适应的方式以输入特征为条件。

第二种是可变形的 RoI 池化。它为先前 RoI 池 [15、7] 的常规 bin 分区中的每个 bin 位置添加一个偏移量。类似地，偏移量是从前面的特征图和 RoIs 中学习的，从而可以对具有不同形状的对象进行自适应部分定位。

两个模块都很轻。他们为偏移学习添加少量参数和计算。它们可以很容易地替换深度 CNN 中的普通对应物，并且可以通过标准反向传播轻松地进行端到端训练。由此产生的 CNN 称为可变形卷积网络或可变形 ConvNet。

我们的方法与空间变换网络 [26] 和可变形部件模型 [11] 具有相似的高级精神。它们都有内部转换参数，并且纯粹从数据中学习这些参数。可变形卷积网络的一个关键区别在于它们以简单、高效、深入和端到端的方式处理密集的空间变换。在第 3.1 节中，我们详细讨论了我们的工作与以前工作的关系，并分析了可变形 ConvNets 的优越性。


Deformable Convolutional Networks

CNN 中的特征图和卷积是 3D 的。可变形卷积和 RoI 池化模块都在 2D 空间域上运行。该操作在整个通道维度上保持不变。在不失一般性的情况下，为了符号清晰起见，此处以 2D 形式描述模块。扩展到 3D 很简单。

Deformable Convolution

2D 卷积包括两个步骤：1）在输入特征图 $\mathrm{x}$ 上使用规则网格 $\mathcal{R}$ 进行采样； 2) 由 $\mathbf{w}$ 加权的采样值的总和。网格 $\mathcal{R}$ 定义感受野大小和膨胀。例如， $$ \mathcal{R}=\{(-1,-1),(-1,0), \ldots,(0,1),(1,1)\} $$ 定义 $3 \ 乘以 3$ 核，膨胀为 1 。对于输出特征图 $\mathbf{y}$ 上的每个位置 $\mathbf{p}_0$ ，我们有 $$ \mathbf{y}\left(\mathbf{p}_0\right)=\sum_{\ mathbf{p}_n \in \mathcal{R}} \mathbf{w}\left(\mathbf{p}_n\right) \cdot \mathbf{x}\left(\mathbf{p}_0+\mathbf{p }_n\right), $$ 其中 $\mathbf{p}_n$ 列举了 $\mathcal{R}$ 中的位置。在可变形卷积中，规则网格 $\mathcal{R}$ 增加了偏移量 $\left\{\Delta \mathbf{p}_n \mid n=1, \ldots, N\right\}$ ，其中 $N=|\mathbf{R}|$ 。当量。 (1) 变为 $$ \mathbf{y}\left(\mathbf{p}_0\right)=\sum_{\mathbf{p}_n \in \mathcal{R}} \mathbf{w}\left(\ mathbf{p}_n\right) \cdot \mathbf{x}\left(\mathbf{p}_0+\mathbf{p}_n+\Delta \mathbf{p}_n\right) 。$$ 现在，采样在不规则和偏移位置 $\mathbf{p}_n+\Delta \mathbf{p}_n$ 。由于偏移 $\Delta \mathbf{p}_n$ 通常是小数，Eq. (2) 通过双线性插值实现为 $$ \mathbf{x}(\mathbf{p})=\sum_{\mathbf{q}} G(\mathbf{q}, \mathbf{p}) \cdot \ mathbf{x}(\mathbf{q}), $$ 其中 $\mathbf{p}$ 表示任意（小数）位置 ( $\mathbf{p}=$ $\mathbf{p}_0+\mathbf{p} _n+\Delta \mathbf{p}_n$ for Eq. (2)), $\mathbf{q}$ 枚举了特征图 $\mathbf{x}$ 中的所有积分空间位置，而 $G(\cdot, \ cdot)$ 是双线性插值内核。请注意 $G$ 是二维的。它被分成两个一维内核 $G(\mathbf{q}, \mathbf{p})=g\left(q_x, p_x\right) \cdot g\left(q_y, p_y\right)$ , 其中 $g(a, b)=\max (0,1-|a-b|)$ 。当量。 (3) 的计算速度很快，因为 $G(\mathbf{q}, \mathbf{p})$ 仅在少数 $\mathbf{q}$ 时不为零。


如图 2 所示，偏移量是通过在同一输入特征图上应用卷积层获得的。卷积核与当前卷积层具有相同的空间分辨率和膨胀（例如，图 2 中也是 3 × 3，膨胀为 1）。输出偏移字段与输入特征图具有相同的空间分辨率。通道维度 2N 对应于 N 个 2D 偏移量。在训练期间，同时学习用于生成输出特征和偏移量的卷积核。为了学习偏移量，梯度通过方程式中的双线性运算反向传播。 （3）和方程式。 (4).详见附录 A。

Deformable RoI Pooling

RoI 池化用于所有基于区域建议的目标检测方法 [16、15、47、7]。它将任意大小的输入矩形区域转换为固定大小的特征。

RoI Pooling [15] 给定输入特征图 x 和大小为 w×h 和左上角 p0 的 RoI，RoI 池将 RoI 分成 k × k（k 是一个自由参数）个 bin 并输出 k × k 特征图y。对于 (i, j)-th bin (0 ≤ i, j < k)，我们有

$$ \mathbf{y}(i, j)=\sum_{\mathbf{p} \in \operatorname{bin}(i, j)} \mathbf{x}\left(\mathbf{p}_0+\mathbf{p}\right) / n_{i j} $$

其中 $n_{i j}$ 是 bin 中的像素数。第 $(i, j)$ 个 bin 跨越 $\left\lfloor i \frac{w}{k}\right\rfloor \leq p_x<\left\lceil(i+1) \frac{w}{k  }\right\rceil$ 和 $\left\lfloor j \frac{h}{k}\right\rfloor \leq p_y<$ $\left\lceil(j+1) \frac{h}{k}\right \rceil$ 。与方程式类似。 (2)、在可变形 RoI pooling 中，偏移量 $\left\{\Delta \mathbf{p}_{i j} \mid 0 \leq i, j<k\right\}$ 被添加到空间 binning 位置。等式（5）变为 $$\mathbf{y}(i, j)=\sum_{\mathbf{p} \in \operatorname{bin}(i, j)} \mathbf{x}\left(\mathbf{p}_0+\mathbf{p }+\Delta \mathbf{p}_{i j}\right) / n_{i j} 。$$ 通常， $\Delta \mathbf{p}_{i j}$ 是小数。当量。 (6) 通过等式通过双线性插值实现。 (3) 和 (4)。图 3 说明了如何获得偏移量。首先，RoI 池化（等式（5））生成池化特征图。从地图中，fc 层生成归一化偏移量 $\Delta \hat{\mathbf{p}}_{i j}$ ，然后将其转换为偏移量 $\Delta \mathbf{p}_{i j}$ 当量。 (6) 按元素与 Rol 的宽度和高度的乘积，如 $\Delta \mathbf{p}_{i j}=\gamma \cdot \Delta \widehat{\mathbf{p}}_{i j} \circ （宽，高）$ 。这里 $\gamma$ 是一个预定义的标量，用于调制偏移量的大小。它根据经验设置为 $\gamma=0.1$ 。偏移归一化对于使偏移学习对 RoI 大小不变是必要的。 fc 层是通过反向传播学习的，详见附录 A。Position-Sensitive (PS) RoI Pooling [7] 它是全卷积的，不同于 RoI pooling。通过一个转换层，所有输入特征图首先被转换为每个对象类的 $k^2$ 个得分图（ $C$ 个对象类总共 $C+1$ 个），如图 4 底部分支所示。无需区分类别，此类分数图表示为 $\left\{\mathbf{x}_{i, j}\right\}$ ，其中 $(i, j)$ 枚举所有 bin。在这些分数图上执行池化。第 $(i, j)$ 个 bin 的输出值是通过从对应于该 bin 的一个分数映射 $\mathbf{x}_{i, j}$ 求和获得的。简而言之，与等式（5）中的 RoI 池的不同之处在于，通用特征图 $x$ 被特定的正敏感分数图 $\mathbf{x}_{i, j}$ 代替。在可变形 PS RoI 池中，方程式的唯一变化。 (6)是 $\mathrm{x}$ 也修改为 $\mathbf{x}_{i, j}$ 。然而，偏移学习是不同的。它遵循 [7] 中的“完全卷积”精神，如图 4 所示。在顶部分支中，一个转换层生成完整的空间分辨率偏移场。对于每个 RoI（也针对每个类），PS RoI pooling 应用于此类字段以获得归一化偏移量 $\Delta \widehat{\mathbf{p}}_{i j}$ ，然后将其转换为实际偏移量 $\Delta \mathbf{p}_{i j}$ 以与上述可变形 RoI 池相同的方式。

Deformable ConvNets

可变形卷积和 RoI 池化模块都具有与其普通版本相同的输入和输出因此，它们可以很容易地替换现有 CNN 中的普通版本。在训练中，这些添加的用于偏移学习的 conv 和 fc 层被初始化为零权重。它们的学习率设置为现有层学习率的 β 倍（默认情况下，β = 1，Faster R-CNN 中的 fc 层，β = 0.01）。他们通过方程式中的双线性插值操作通过反向传播进行训练。 （3）和方程式。 (4).生成的 CNN 称为可变形 ConvNet。

为了将可变形卷积网络与最先进的 CNN 架构相结合，我们注意到这些架构由两个阶段组成。首先，深度全卷积网络在整个输入图像上生成特征图。其次，浅层任务特定网络从特征图生成结果。我们详细说明下面的两个步骤。

用于特征提取的可变形卷积我们采用两种最先进的特征提取架构：ResNet-101 [22] 和 InceptionResNet [51] 的修改版本。两者都在 ImageNet [8] 分类数据集上进行了预训练。

最初的 Inception-ResNet 是为图像识别而设计的。它有一个特征错位问题，并且对于密集的预测任务有问题。它被修改以修复对齐问题[20]。修改后的版本被称为“Aligned-Inception-ResNet”，详见附录 B。

这两个模型都包含几个卷积块、一个平均池和一个用于 ImageNet 分类的 1000 路 fc 层。移除了平均池化层和全连接层。最后添加一个随机初始化的 1×1 卷积以将通道维度减少到 1024。与通常的做法 [4, 7] 一样，最后一个卷积块中的有效步幅从 32 像素减少到 16 像素以增加特征图解决。具体来说，在最后一个块的开头，步幅从 2 更改为 1（ResNet-101 和 Aligned-Inception-ResNet 的“conv5”）。为了补偿，此块中所有卷积滤波器的膨胀（内核大小 > 1）从 1 更改为 2。

可选地，将可变形卷积应用于最后几个卷积层（内核大小 > 1）。我们对不同数量的此类层进行了实验，发现 3 层可以很好地权衡不同的任务，如表 1 所示。

分割和检测网络任务特定网络建立在上述特征提取网络的输出特征图之上。

在下文中，C 表示对象类的数量。 DeepLab [5] 是一种最先进的语义分割方法。它在特征图上添加一个 1×1 卷积层以生成 (C + 1) 个表示每个像素分类分数的图。随后的 softmax 层然后输出每个像素的概率。

Category-Aware RPN 与 [47] 中的区域提议网络几乎相同，只是将 2 类（对象或非对象）卷积分类器替换为 (C + 1) 类卷积分类器。 它可以被认为是 SSD [40] 的简化版本。

Faster R-CNN [47] 是最先进的检测器。在我们的实现中，RPN 分支被添加到 conv4 块的顶部，遵循 [47]。在之前的实践 [22, 24] 中，在 ResNet-101 的 conv4 和 conv5 块之间插入了 RoI 池化层，每个 RoI 保留 10 层。这种设计实现了良好的准确性，但每个 RoI 的计算量很高。相反，我们采用了[38]中的简化设计。 RoI 池化层添加在 last1。在合并的 RoI 特征之上，添加了两个维度为 1024 的 fc 层，然后是边界框回归和分类分支。尽管这种简化（从 10 层 conv5 块到 2 个 fc 层）会略微降低准确性，但它仍然是一个足够强大的基线，并且在这项工作中不是一个问题。

可选地，RoI 池化层可以更改为可变形的 RoI 池化。 R-FCN [7] 是另一种最先进的检测器。它的每个 RoI 计算成本可以忽略不计。我们遵循原来的实现。可选地，其 RoI 池层可以更改为可变形的位置敏感 RoI 池。


理解可变形卷积神经网络

这项工作建立在使用额外的偏移量增加卷积和 RoI 池中的空间采样位置并从目标任务中学习偏移量的想法之上。当堆叠可变形卷积时，复合变形的效果是深远的。图 5 对此进行了举例说明。标准卷积中的感受野和采样位置在整个顶部特征图（左）上都是固定的。它们根据可变形卷积中对象的比例和形状进行自适应调整（右）。更多示例如图 6 所示。表 2 提供了这种自适应变形的定量证据。可变形 RoI pooling 的效果类似，如图 7 所示。标准 RoI pooling 中网格结构的规律性不再成立。相反，部分偏离 RoI 箱并移动到附近的对象前景区域。定位能力得到增强，尤其是对于非刚性物体。

In Context of Related Works

我们的工作在不同方面与以前的工作有关。我们详细讨论了关系和差异。

Spatial Transform Networks (STN)[26] 这是第一个在深度学习框架中从数据中学习空间变换的工作。它通过仿射变换等全局参数变换来扭曲特征图。这种扭曲是昂贵的，并且学习转换参数是众所周知的困难。 STN 在小规模图像分类问题上取得了成功。逆 STN 方法 [37] 通过有效的变换参数传播取代了昂贵的特征变形。可变形卷积中的偏移学习可以被视为 STN [26] 中的极轻量级空间变换器。然而，可变形卷积不采用全局参数变换和特征变形。相反，它以局部和密集的方式对特征图进行采样。为了生成新的特征图，它有一个加权求和步骤，这在 STN 中是不存在的。可变形卷积很容易集成到任何 CNN 架构中。它的训练很容易。对于需要密集（例如，语义分割）或半密集（例如，对象检测）预测的复杂视觉任务，它被证明是有效的。这些任务对于 STN [26, 37] 来说是困难的（如果不是不可行的话）。

Active Convolution [27] 这项工作是当代的。 它还使用偏移量增加卷积中的采样位置，并通过端到端的反向传播学习偏移量。 它被证明对图像分类任务有效。 与可变形卷积的两个关键区别使这项工作的通用性和适应性较差。 首先，它共享所有不同空间位置的偏移量。 其次，偏移量是每个任务或每次训练学习的静态模型参数。 相反，可变形卷积中的偏移量是每个图像位置都不同的动态模型输出。 它们对图像中的密集空间变换进行建模，并且对（半）密集预测任务（例如对象检测和语义分割）有效。

Effective Receptive Field

它发现并非感受野中的所有像素都对输出响应有同等贡献。中心附近的像素具有更大的影响。有效感受野只占理论感受野的一小部分，呈高斯分布。尽管理论上感受野大小随卷积层数线性增加，但令人惊讶的结果是，有效感受野大小随卷积层数的平方根线性增加，因此比我们预期的要慢得多。这一发现表明，即使是深度 CNN 中的顶层单元也可能没有足够大的感受野。这部分解释了为什么空洞卷积 [23] 广泛用于视觉任务（见下文）。它表明了自适应感受野学习的需要。可变形卷积能够自适应地学习感受野，如图 5、6 和表 2 所示。

空洞卷积(Atrous convolution)
它将普通过滤器的步幅增加到大于 1，并将原始权重保持在稀疏采样位置。这增加了接受域的大小，并在参数和计算方面保持相同的复杂性。它已广泛用于语义分割[41、5、54]（在[54]中也称为扩张卷积）、目标检测[7]和图像分类[55]。可变形卷积是空洞卷积的推广，如图 1 (c) 所示。表 3 给出了与空洞卷积的广泛比较。

Deformable Part Models (DPM)

可变形 RoI 池类似于 DPM，因为这两种方法都学习对象部分的空间变形以最大化分类分数。可变形 RoI 池更简单，因为没有考虑部件之间的空间关系。

DPM 是一个浅层模型，对变形建模的能力有限。虽然它的推理算法可以通过将距离变换视为特殊的池化操作来转换为 CNN [17]，但它的训练不是端到端的，并且涉及启发式选择，例如组件和零件尺寸的选择。相比之下，可变形的 ConvNets 是深度的并且执行端到端的训练。当多个可变形模块堆叠时，建模变形的能力变得更强。

DeepID-Net

它引入了变形约束池化层，该池化层还考虑了物体检测的部分变形。因此，它与可变形 RoI 池具有相似的精神，但要复杂得多。这项工作是高度工程化的，基于 RCNN [16]。目前尚不清楚如何以端到端的方式使其适应最近最先进的目标检测方法 [47、7]。

Spatial manipulation in RoI pooling

空间金字塔池化 [34] 在尺度上使用手工制作的池化区域。它是计算机视觉中的主要方法，也用于基于深度学习的对象检测 [21、15]。了解池化区域的空间布局的研究很少。 [28] 中的工作从一个大的超完备集合中学习池化区域的一个稀疏子集。大集合是手工设计的，学习不是端到端的。可变形 RoI 池化是第一个在 CNN 中端到端学习池化区域的方法。虽然这些区域目前大小相同，但扩展到多个大小如空间金字塔池 [34] 是直截了当的。

Transformation invariant features and their learning

在设计变换不变特征方面已经付出了巨大的努力。著名的例子包括尺度不变特征变换 (SIFT) [42] 和 ORB [49]（O 表示方向）。在 CNN 的背景下有大量此类作品。 [36] 研究了 CNN 表示对图像变换的不变性和等价性。一些作品学习关于不同类型变换的不变 CNN 表示，例如 [50]、散射网络 [3]、卷积丛林 [32] 和 TIpooling [33]。一些作品致力于特定的变换，例如对称性 [13、9]、比例 [29] 和旋转 [53]。正如第 1 节中分析的那样，在这些作品中，变换是先验已知的。知识（例如参数化）用于手工制作特征提取算法的结构，或者固定在 SIFT 中，或者使用可学习的参数，例如基于 CNN 的参数。他们无法处理新任务中的未知转换。相比之下，我们的可变形模块概括了各种变换（见图 1）。变换不变性是从目标任务中学习的。

Dynamic Filter [2]

与可变形卷积类似，动态滤波器也以输入特征和样本变化为条件。不同的是，只学习过滤器权重，而不是像我们这样的采样位置。这项工作适用于视频和立体声预测。


Combination of low level filters

高斯滤波器及其平滑导数[30]被广泛用于提取低级图像结构，如角落、边缘、T 形接头等。在特定条件下，此类滤波器形成一组基，它们的线性组合在模型中形成新的滤波器同一组几何变换，例如 Steerable Filters [12] 中的多个方向和 [45] 中的多个尺度。我们注意到，虽然[45]中使用了可变形内核这个术语，但它的含义与我们在这项工作中的含义不同。大多数 CNN 从头开始​​学习所有的卷积滤波器。最近的工作 [25] 表明它可能是不必要的。它通过低级滤波器（高达 4 阶的高斯导数）的加权组合代替自由形式的滤波器并学习权重系数。当训练数据较小时，过滤器函数空间的正则化可以提高泛化能力。上述工作与我们的相关，当组合多个过滤器，尤其是具有不同尺度的过滤器时，生成的过滤器可能具有复杂的权重，类似于我们的可变形卷积过滤器。然而，可变形卷积学习采样位置而不是滤波器权重。

### 引文

## 摘录
