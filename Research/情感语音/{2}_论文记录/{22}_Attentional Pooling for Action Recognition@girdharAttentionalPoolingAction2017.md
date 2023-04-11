---
title: "Attentional Pooling for Action Recognition"
description: ""
citekey: girdharAttentionalPoolingAction2017
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
---

> [!info] 论文信息
>1. Title：Attentional Pooling for Action Recognition
>2. Author：Rohit Girdhar, Deva Ramanan
>3. Entry：[Zotero link](zotero://select/items/@girdharAttentionalPoolingAction2017) [URL link](http://arxiv.org/abs/1711.01467) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Girdhar_Ramanan_2017_Attentional Pooling for Action Recognition.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\SSC5EGTH\\1711.html>)
>4. Other：2017 - arxiv:1711.01467 [cs]     -   

>- :luc_github: 论文实现：https://github.com/rohitgirdhar/AttentionalPoolingAction
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***


## ⭐ 重点

- 提出了一种 Pooling 方法: Attentional Pooling

## 摘要

> [!abstract] We introduce a simple yet surprisingly powerful model to incorporate attention in action recognition and human object interaction tasks. Our proposed attention module can be trained with or without extra supervision, and gives a sizable boost in accuracy while keeping the network size and computational cost nearly the same. It leads to significant improvements over state of the art base architecture on three standard action recognition benchmarks across still images and videos, and establishes new state of the art on MPII dataset with 12.5% relative improvement. We also perform an extensive analysis of our attention module both empirically and analytically. In terms of the latter, we introduce a novel derivation of bottom-up and top-down attention as low-rank approximations of bilinear pooling methods (typically used for fine-grained classification). From this perspective, our attention formulation suggests a novel characterization of action recognition as a fine-grained recognition problem.

> 

## 预处理

## 概述

## 结果

## 精读

人类动作识别是热门研究问题，涉及图像[7，13，34，36，58]和视频[24，27，41，45]两个方面。较新的基于图像的数据集，有HICO[7]和MPII[34]，两个数据库都很大，并且高度多样化，分别包含600个和393个类别。但与图像集相比，收集如此多样化的视频动作数据集是非常困难的，因此现有流行的数据库，如UCF101[45]或HMDB51[27]分别只包含101和51个类别。这反过来导致了很高的视频基线模型性能，例如，在视频数据集UCF101上的分类准确率为大约为94%[54]，在图像数据集MPII的平均精度(mAP)大约为32%[30]。




此外，我们的方法不受姿势标签的限制，正如我们在实验中所表明的那样，在现有方法[4]预测的姿势甚至不使用姿势的情况下，我们的方法都可以显示出有效的性能。

我们的方法摆脱了边界框检测步骤，并通过自动学习关注任务中图像中信息最丰富的部分来改进这两种方法。

然而，我们的方法使用单个帧来预测和应用空间注意力，使得它同时适用于基于单个图像和视频的用例。[44]还使用3D视频中标记的姿势关键点将注意力吸引到身体部分。学习了一种不受约束的注意力模型，它经常学习环顾人体，寻找能够更容易地对动作进行分类的对象。

特点：基于视频的动作识别方法主要解决两个问题：动作分类和(时空)时间检测。虽然基于图像的识别问题，包括动作识别，随着深度学习的进步(例如，MPII性能从5%的mAP[34]上升到27%的mAP[18])有了很大的提升，但基于视频的识别仍然依赖于手工制作的特征，如iDT[53]。这些特征是通过沿视频中密集采样点轨迹提取外观和运动特征来计算的，通过使用fisher vectors[32]汇聚到固定长度表示。基于卷积神经网络(CNN)的视频动作识别方法大体上遵循两个主要范例：(1)Multi-stream 网络[42，54]，其将输入视频分割成诸如RGB、光流（optical flow）、翘曲流（warped flow）等多个形态，在这些形态之上训练基于标准图像的CNN，并对来自每个CNN的预测进行后期融合；(2)3D卷积网络[47，49]，其将视频表示为时间点，并训练3D卷积模型用于动作预测。在性能方面，基于3D 卷积的方法更难扩展，而Multi-stream 方法[54]目前保持着最先进的性能。

Pose：之前也有将人体姿势融入到动作识别的工作[8，10，60]。特别是，P-CNN[8]可以计算沿姿势关键点的局部外观和运动特征，并在视频上聚合这些特征以进行动作预测，但不是端到端可训练的。最近的工作[60]在chained multi-stream方式中添加了作为附加流（additional stream）的人体姿势，得到了优秀的结果。

Hard attention：之前在基于图像的动作识别方面的工作已经表现出令人印象深刻的性能，它结合了来自human, context和pose关键点边界框（bounding box）的证据[8，18，30]。Gkioxari等人。[18]修改R-CNN pipeline以提出R\*CNN，其中他们选择一个辅助框(auxiliary box)来编码context部分，而不是人类边界框。Mallya和Lazebnik[30]通过使用完整图像作为context并使用多实例学习(MIL，multiple instance learning)对图像中存在的所有人类进行推理来预测图像的动作标签，从而对其进行了改进。

软注意：除了[39，44]对spatio-temporal attention和[40]temporal attention的研究外，探索动作识别的不受限制的“软”注意的工作相对较少。重要的是，所有这些都考虑了视频设置，其中LSTM网络预测当前帧的空间注意力图。

二阶池：因为我们的模型使用一组外观特征来预测和应用注意力图，这将使特征中的输出为二次(SEC。3.1)。这种观察允许我们通过二阶或双线性合并操作[28]来实现注意，这些操作通过低阶近似[16，25，26]来提高效率。我们的工作主要与[26]有关，他们指出，当有效地实现时，低阶近似避免了显式地计算二阶特征。我们指出，二阶特征的秩1近似等价于有时被表示为“自我注意”的注意模型[50]。揭示这种联系使我们能够探索几个扩展，包括自下而上和自上而下注意力的变化，以及利用额外监督的注意图的规律化注意图。

**全局池化**

全局池化是使用大小与特征图相等的池窗口，作用于特征图$X$。假设要被池化的特征图为 $X \in R^{n \times f}$,  $n$ 是特征图的特征数量 (例如, $n=H × W=16 \times 16=256$，显然，二维特征图在计算时应该是被展平了 ) ，$f$ 是特征通道数 (例如, 2048)。传统的求和或最大池化会将其减小到 $R^{f \times 1}$, 然后再通过一层全连接 $\mathbf{w} \in R^{f \times 1}$ 得到最终的预测分数。 例如，对于多分类问题，其中第$k$个预测分数可以使用下式表示

$$
\begin{aligned}
\operatorname{score}(k)&=\mathbf{1}^{T} X \mathbf{w}_{k}, \quad \text { where } \quad X \in R^{n \times f}, \mathbf{1} \in R^{n \times 1}, \mathbf{w} \in R^{f \times 1}\\
&=\left[\begin{array}{c}
1 \\
1 \\
\vdots
\end{array}\right]_{\text {n }}^{T} \times\left[\begin{array}{ccc}

x_{11} & x_{12} & \cdots \\

x_{21} & \ddots & \cdots \\

\vdots & \vdots & \ddots
\end{array}\right] \times\left[\begin{array}{c}

w_{1 k} \\

w_{2 k} \\

\vdots
\end{array}\right]_{\text {f }}
\end{aligned}
$$

其中，$1^{T} X_k$可以理解为对每个通道的特征进行求和，然后再对这些结果利用权值矩阵继续加权求和，就得到了最终的pooling结果。这种全局池化方法可以有效地将多通道特征图映射下采样到标量，但此方法对所有输入数据都一视同仁，这意味着没有考虑特征间的差异性，即在频谱图中，许多区域可能与情绪信息几乎没有关系。因此，需要一种更好的池化方法来提高SER性能。注意到由Girdhar等人[19]提出的注意力池化，我们在Conv5之后引入了一个注意力池化层。

**二阶池化**

首先由输入特征图构造 $X^{T} X \in R^{f \times f}$，这样做对细粒度（fine-grained）分类任务很有用 [20，21]。通常情况下可以通过向量化"vectorizes"此特征，然后通过学习一个大小为 $f^{2}$ 的权重矩阵获得预测分数。又因为两个矩阵的内积可以由求迹公式$\operatorname{Tr}\left(A B^{T}\right)=\operatorname{dot}(A(:), B(:))$来表示 ，可以得到第$k$个预测分数的简单矩阵表示

$$
\operatorname{score}(k)=\operatorname{Tr}\left(X^{T} X W_k^{T}\right), \quad \text { where } \quad X \in R^{n \times f}, W_k \in R^{f \times f}
$$


一般计算过程中，$W_k$通常是高维的，当数据集大小不足时，会产生过拟合问题，因此可以通过低秩分解，将权重矩阵$W_k$分解为两个向量的乘积：

$$

\operatorname{score}(k)=\operatorname{Tr}\left(X^{T} X \mathbf{b}_k \mathbf{a}_k^{T}\right), \quad \text { where } \quad X \in R^{n \times f}, \mathbf{a}_k, \mathbf{b}_k \in R^{f \times 1}
$$

根据求迹运算的两种性质： $\operatorname{Tr}(A B C)=\operatorname{Tr}(C A B)$ 和标量的迹是其本身。上述公式可以改写为：


$$
\begin{aligned}
\operatorname{score}(k)
&=\operatorname{Tr}\left(\mathbf{a}_k^{T} X^{T} X \mathbf{b}_k\right) \\
&=\mathbf{a}_k^{T} X^{T} X \mathbf{b}_k \\
&=\mathbf{a}_k^{T}\left(X^{T}(X \mathbf{b}_k)\right) , \quad \text { where } \quad X \in R^{n \times f}, \mathbf{a}_k, \mathbf{b}_k \in R^{f \times 1}
\end{aligned}
$$

即，在具体计算过程中，首先计算给定特征图 $X$中 $n$ 个特征值的注意力权重 $\mathbf{h}=$ $X \mathbf{b}_k \in R^{n \times 1}$，然后对特征图中的特征值进行加权得到 $\mathbf{x}=X^{T} \mathbf{h} \in R^{f \times 1}$。最后将每个通道得到的加权特征通过线性计算，产生预测分数 $\mathbf{a}_k^{T} \mathbf{x}$ 。

同时，预测分数计算公式也可以写成下述计算形式

$$
\begin{aligned}
\operatorname{score}(k)
&=\left((X \mathbf{a}_k)^{T} X\right) \mathbf{b}_k\\
&=\left(X \mathbf{a}_k\right)^{T}\left(X \mathbf{b}_k\right)\\
\end{aligned}

$$

第一行表示$X \mathbf{a}_k \in R^{n \times 1}$也可以看作是注意力权重，而$\mathbf{b}_k$是最终的分类器。第k个类别的预测分数可以看作是两个注意图$X \mathbf{a}_k$ 和 $X \mathbf{b}_k$的组合。第二行说明计算过程是对称的，最终的预测分数可以看作是两个注意力权重的内积。

对于不同的类别所对应的 $\mathbf{a}_k,\mathbf{b}_k$，他们每一个都能产生特定于类（class-specific）的注意力权重，即均与类相关，称为 “top-down” attention。因此，可以将两者中的$\mathbf{b}_k$假设为与类无关（class-agnostic）的"botom-up"，即所有类别的预测分数计算共用一个$\mathbf{b}_k=\mathbf{b}$。

$$
\text { score }(k)=\mathbf{t}_{k}^{T} \mathbf{h}, \quad \text { where } \quad \mathbf{t}_{k}=X \mathbf{a}_{k}, \mathbf{h}=X \mathbf{b}
$$

相当于“top-down”(与类别相关)$\mathbf{t}_{k}$和"botom-up"(基于特征)的注意力权重之间的内积。“top-down” 和"botom-up" 方法的组合来源于论文biological vision[22]，表明此处的“top-down” 和"botom-up" 权重内积也可以简单地通过元素相乘和全局池化来实现：

$$
\operatorname{score}(k)=\mathbf{1}^{T} \mathbf{c}_{k}, \quad \text { where } \quad \mathbf{c}_{k}=\mathbf{t}_{k} \circ \mathbf{h}
$$

同时，回顾全局平均池化公式，可以发现它能表示成以下形式

$$
\text { score }(k)=\mathbf{1}^{T} X \mathbf{w}_{k}=\mathbf{1}^{T} \mathbf{t}_{k} \quad \text { where } \quad \mathbf{t}_{k}=X \mathbf{w}_{k}
$$


从这个角度来看，上面的推导给出了传统全局平均池化生成“top-down” 注意力权重的能力，即二阶池化的一种特殊情况。
### 引文

## 摘录
