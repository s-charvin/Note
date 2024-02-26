---
title: "CNN(卷积神经网络)"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-03-19 14:32:35
lastmod: 2023-11-13 21:42:14
date: 2022-03-19 14:32:35
---

# CNN 卷积神经网络

![img](CNN(卷积神经网络).assets/v2-a35a29688a764b9ec5e438d53bc1d35a_720w.jpg)

CNN 在图像识别等任务中具有重要作用，主要是因为 CNN 利用了图片（信号）在其域中的「局部平移不变性（local translational invariance）」,能够挖掘数据局部结构。

对于 CNN 来说，其核心在于使用了基于卷积核的卷积操作，对「计算区域内的中心节点和相邻节点进行加权求和」，进而提取出来图像（信号）的特征。上述的计算区域通常是个二维或者三维的特征矩阵，无论卷积核平移到图像（信号）中的哪个位置都可以保证其运算方式的一致性，。

## 特点：

- 局部感知(连接)

	在卷积神经网络中，通过设置一个 Kernel size 大小的卷积核(Filter)，在输入的图像或特征数据上扫描局部区域，进行特征提取，被感知的区域被称为 Receptive Field(接受域)，每感知完一个 Receptive Field(接受域) 后都会得到一个由 Field 内部参数(黄色细线箭头)加权计算(局部连接)的数据(蓝色)。然后通过不断移动 Stride 步长进行下一次感知，对于超过边界的范围使用 Padding 规则填充多余部分，直到扫描完输入的所有数据；![img](CNN(卷积神经网络).assets/v2-4fd0400ccebc8adb2dffe24aac163e70_b.gif)

- 权值共享

	每一个 Filter 都有自己的参数，当 使用一个 Kernel size 大小比输入特征维度小很多的 Filter 进行卷积卷积操作时，会感知到数量大小由输入特征维度和移动 Stride 步长决定的多个 Receptive Fields，也就是说这些 Field 共享了此 Kernel 的参数。Kernel size 小的好处就是对于输入特征维度非常大的数据，小Kernel size 的参数量会少很多。![img](CNN(卷积神经网络).assets/v2-15fea61b768f7561648dbea164fcb75f_b.gif)

- 多核卷积

	定义多个 Filter ，通常这些 Filter 的参数也是不同的，每个 Filter 都会在感知完所有的 Receptive Fields 后产生一组特征数据，因此多个 Filter 也就可以得到不同数量的特征数据组，亦即计算得到的特征维度。![img](CNN(卷积神经网络).assets/v2-8788fbbe3e65e01bfac0e01914c1809f_b.gif)

- 空间下采样

	卷积层数越深，卷积层每个数据都是由前一个卷积层单个 Receptive Field 得来的，同理此 Receptive Field 中的数据也会是再前一个卷积层的多个 Receptive Fields(不是所有，与 Field 大小对应)得来的。![img](CNN(卷积神经网络).assets/v2-8457d9749836f38431eccf9625bf5636_720w.png)

## 计算实例：

假设输入图像大小为 $5×5$（变量表示：$m×n$），卷积滤波器（也叫Filter、kernel）大小为$3×3$（变量表示：$f×f$），步长（也叫stride）小为1（变量表示：s），最终获得特征图大小为3×3。

![](CNN(卷积神经网络).assets/image-20220314113634.png)

定义元素可通过下标方式来代替，如图像 {$x_{ij}$} ，Filter {$w_{ij}$} ，特征图元素为 {$h_{ij}$}；偏置向量为 b ，激活函数为  Relu()。

第一步卷积由左上角 $x_{00}$ 开始，因此第一个卷积域为 $[[x_{00}:x_{02}],[x_{00}:x_{20}]]$

![](CNN(卷积神经网络).assets/image-20220314115300.png)

卷积完成后，右移 Step=1 步，获得第二个卷积域为$[[x_{01}:x_{03}],[x_{01}:x_{21}]]$

![](CNN(卷积神经网络).assets/image-20220314115347.png)

继续右移，可知在不超出边界的情况下($is+f-1≤m-1, js+f-1≤n-1$)，可以计算出总共需要移动 $j = floor\left(\frac{n-f}{s}\right)=2$ 步。同理可得卷积过程需要下移 $i = floor\left(\frac{m-f}{s}\right)=2$ 步。

每移动一步，就可以通过卷积操作计算出一个值，可以由此推出最终的输出维度为$\left(ceil\left(\frac{n-f}{s}\right), ceil\left(\frac{m-f}{s}\right)\right)= (3,3)$，多了一个维度是因为在 $(0,0)$ 处也是有卷积值的。

		上述 floor(x) 表示取≤x的最大整数值，ceil(x) 表示取≥x的最小整数值。

每一步的卷积过程可由下面公式表示，默认从 $x_{00}$ 作为左上顶点开始，向右下分别移动 $i,j$ 步，到达 $x_{s×i, s×j}$ 顶点处，以顶点为基，在卷积窗口内做运算：

![](CNN(卷积神经网络).assets/image-20220316084110.png)


$$
\begin{aligned}

h_{i, j}=&Relu\left(\sum_{k=0}^{f-1} \sum_{l=0}^{f-1} w_{k, l} x_{s×i+k, s×j+l}+b\right), \\

&i\in \left[0,floor\left(\frac{m-f}{s}\right)\right]\\

&j \in \left[0,floor\left(\frac{n-f}{s}\right)\right]
\end{aligned}
$$

但是考虑到，当步长设置为非1数值的时候，卷积过程会忽略一些图像边界，而造成图边沿数据损失，并且随着层数越多，损失也就会越多，如下图所示，如果设置步长 $s=3$ ，灰色框圈住的部分就被丢弃了。因此一般会通过 Padding（填充）操作，将原图填充为合适的尺寸，再运算。

![](CNN(卷积神经网络).assets/image-20220316084348.png)







假设卷积窗口的可以超出边界（但不可以全部超出，即 $is≤m-1,js≤n-1$），第k次移动后的窗口超出图像边界，则需要填充的部分可以通过公式 $ks+f-1=m(or n)-1+pad$ ，得到两个维度总共需要填充的元素维度。通常卷积核大小选择奇数，因为容易计算$pad=f-1$，且pad为偶数方便两侧添加，即左右(上下)填充大小为$p = \frac{f-1}{2}$。

以奇数卷积窗口为例，在添加 Padding 后，每一步的卷积过程并无太大变化，只是卷积步数通常会增加。

$$
\begin{aligned}

h_{i, j}=&Relu\left(\sum_{k=0}^{f-1=2} \sum_{l=0}^{f-1=2} w_{k, l} x_{s×i+k, s×j+l}+b\right), \\

&i\in \left[0,\frac{m-f+2 p}{s}\right]\\
&j \in \left[0,\frac{n-f+2 p}{s}\right]
\end{aligned}
$$

最终输出维度为：

$$
\left(\frac{m-f+2 p}{s}+1,\frac{n-f+2 p}{s}+1  \right)
$$

前面讲述了深度为1的卷积层计算方法，如果深度大于1（如彩色图，深度为RGB3层），其实只需要再加一层循环即可。

$$

h_{i, j}=Relu\left(\sum_{d=0}^{d-1}\sum_{k=0}^{f-1} \sum_{l=0}^{f-1} w_{d,k, l} x_{d,s×i+k, s×j+l}+b\right)

$$




> [YJango的卷积神经网络——介绍 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/27642620)
> [利用卷积模块，提出了结合图卷积（GCN）与 $1 ×1$ 卷积的全新GRU单元，进一步构建双向循环神经网络，来一体化解决路网级实时交通数据补全与预测问题](https://link.zhihu.com/?target=https%3A//www.sciencedirect.com/science/article/pii/S0968090X21003740)
> [零基础入门深度学习(4) - 卷积神经网络 - 作业部落 Cmd Markdown 编辑阅读器 (zybuluo.com)](https://www.zybuluo.com/hanbingtao/note/485480)
> https://www.tensorflow.org/api_guides/python/nn#Convolution
