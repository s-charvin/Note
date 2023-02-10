---
title: "GCN(图网络)"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-03-19 14:34:40
lastmod: 2022-03-22 17:15:11
---

# [GCN 图网络](https://www.zhihu.com/question/54504471/answer/332657604)

 CNN 可以处理[Euclidean Structure](https://blog.csdn.net/imsuhxz/article/details/91361977) 类数据，即数据点与数据点之间的排列是整齐对应的，例如 CNN 在图片（信号）识别等任务中具有重要作用，主要是因为 CNN 利用了图片（信号）在其域中的「局部平移不变性（local translational invariance）」。![img](GCN(图网络).assets/v2-7e9deacb367dfe0d6913cf6f83197650_720w.jpg)

而图网络是不规整的关系型数据，所以其不存在平移不变形（每个节点的周围邻居数不固定），这就使得传统的 CNN 方法无法直接应用于网络中。

![img](GCN(图网络).assets/v2-5cb1a159a2257ae89fdf86d59bbc3036_720w.jpg)

 GCN 处理的是 Non Euclidean Structure 类数据，即不同数据点和不同数据点之间有不同的连接关系，在赋范空间内构成拓扑关联。

## 谱图理论

提取拓扑图的空间特征主要有两种方法，(1) vertex domain (spatial domain)：按照给定的条件把每个顶点相邻的neighbors找出来（确定 receptive field ）。然后按照一定的方式处理包含不同数目neighbors的特征。缺点是：每个顶点提取出来的neighbors不同，使得计算处理必须针对所有顶点；提取特征的效果可能没有卷积好。(2) spectral domain：借助图谱的理论，使用图的拉普拉斯矩阵的特征值和特征向量，来研究图的性质，将空间域中的拓扑图结构通过图傅立叶变换映射到频域中并进行卷积，然后利用逆变换返回空间域，此理论也是 GCN 的理论基础，以下为谱图理论证明。

[首先使用数学中的 laplace 算子 $\Delta$ 引出 laplace 矩阵 $L$ ：](https://zhuanlan.zhihu.com/p/85287578)

对一个函数求完梯度后，再求散度就可以得到 laplace算子 $\Delta$ 的定义： $\Delta=\sum_{i} \frac{\partial^{2}}{\partial x_{i}^{2}}$，即$\Delta f=\nabla^{2} f=\nabla \cdot \nabla f=\operatorname{div}(\operatorname{gradf})$ 。

<video id="laplace">
<source src="./GCN(图网络).assets/拉普拉斯矩阵与拉普拉斯算子的关系 - 知乎.mp4" type="video/mp4">
</video>


以二维离散laplace算子 $\Delta$ 为例 ，可得

$$
\begin{aligned}
\Delta f &=\nabla^{2} f=\nabla \cdot \nabla f=\nabla \cdot \{\frac{\partial f}{\partial x} \vec{i}+\frac{\partial f}{\partial y} \vec{j}\}\\
&=f(x+1, y)+f(x-1, y)+f(x, y+1)+f(x, y-1)-4 f(x, y)
\end{aligned}
$$

由上式可发现 laplace算子 $\Delta$ 计算了 $f(x,y)$ 与其周围点的梯度差之和，而周围临界点可看作 $f(x,y)$ 在( $x,y$ )两个自由度上受到了微小扰动后的结果，即 laplace算子 $\Delta$ 计算得到的是对 $f(x,y)$ 点进行微小扰动后,在所有自由度上可能获得的总增益 （或者说是总变化）。同时，由上面视频可知，在几何意义上，当 $\Delta f>0$ 表示该点为发散源，且函数取到极小值；当 $\Delta f<0$ 表示该点为汇源，且函数取到极大值；$|\Delta f<0|$ 的值越大，则邻域节点流向(或流出)当前节点越流畅。

根据上面的思想，可以将结论推广到图网络中，对图网络中的所有节点定义一个N维向量 $f=(x_{1}, x_{2} , \cdots , x_{N})$ 表示图网络的所处状态，其中 $x_{i}$ 为节点 $i$ 在当前状态的值。
因此可知，当在节点 $i$ 处产生扰动时，节点值可能变为其任意的邻域节点。？

假设图网络节点与节点之间的边界权重为 $W_{ij}$ （理解为经扰动后单个节点和节点间产生的变化对总变化的影响），通过 laplace算子 $\Delta$ 可以求取每个节点 $i$ 变化到所有邻域节点 $j \in N_{i}$ 所带来的总增益，其中因为邻接矩阵 $W$ 可以控制每个节点与邻域节点的关系，因此计算过程中可以直接所有维度上进行矩阵运算。
$$
\begin{aligned}
\Delta f_{i}&= \sum_{j} W_{ij}(f_{i}-f_{j})=\sum_{j} W_{ij}f_{i}-\sum_{j } W_{ij}f_{j}\\
&=f_{i}\sum_{j } W_{ij}-\left(w_{i 1}, \ldots, w_{i N}\right) \left(\begin{array}{c}f_{1} \\ \vdots \\ f_{N}\end{array}\right)\\
&=f_{i}d_{i}-w_{i:}f\quad, d_{i}\text{ 为节点的度：总临邻点数}\\ \\
\Delta f&=\left(\begin{array}{c}
\Delta f_{1} \\
\vdots \\
\Delta f_{N}
\end{array}\right)=\left(\begin{array}{c}

d_{1} f_{1}-w_{1:} f \\

\vdots \\

d_{N} f_{N}-w_{N:} f

\end{array}\right) \\
&=\left(\begin{array}{ccc}

d_{1} & \cdots & 0 \\

\vdots & \ddots & \vdots \\
0 & \cdots & d_{N}
\end{array}\right) f-\left(\begin{array}{c}

w_{1:} \\

\vdots \\

w_{N:}

\end{array}\right) f \\
&=\operatorname{diag}\left(d_{i}\right) f-W f \\
&=(D-W) f
\end{aligned}
$$

定义拉普拉斯矩阵 $L=D-W$ ，可以看出通过拉普拉斯矩阵  $L$ 对图网络向量进行矩阵运算，与 laplace算子 $\Delta$ 的作用相同。其中 $D$ 为由所有节点的度构成的对角阵(每个节点连接的邻接节点数)，$W$ 为由节点边界权重构成的邻接矩阵(表示每个节点间是否相邻和两者的关系权重)。

特殊的，考虑归一化后的拉普拉斯矩阵：$L_{Normal}=I-D^{-1/2}WD^{-1/2}$

性质：

- 由于拉普拉斯矩阵以每行 (列) 元素之和为零，因此拉普拉斯矩阵的至少有一个特征值为 0 ，对 应的特征向量 $u_{0}=[1,1, \cdots , 1 ]^{T} / \sqrt{N}$ ，且满足: $\mathbf{L} u_{0}=0 u_{0}$ 。

- 拉普拉斯矩阵的特征值都大于等于零，归一化的拉普拉斯矩阵的特征值区间为 $[0,2]$;

- 如果有 $n$ 个特征值为 0 ，则表示图有 $n$ 个子图相互无连接；

- 特征值的总和为矩阵的迹，对于归一化的拉普拉斯矩阵，如果没有孤立节点或子图，其特征值为 $\mathrm{N}$ 。

[拉普拉斯矩阵  $L$ 的特征值分解(谱分解)](https://zhuanlan.zhihu.com/p/120311352)

从拉普拉斯矩阵  $L$ 的定义可知，对于无向图(节点之间的联系均是双向的,$w_{ij}=w_{ji}$)来说，  $L$ 是个半正定实对称矩阵，因此  [$L$ 可以进行正交相似对角化](https://blog.csdn.net/universe_1207/article/details/100544529)：

$$
\mathbf{L}=\mathbf{U} \mathbf{\Lambda} \mathbf{U}^{-1}=\mathbf{U} \mathbf{\Lambda} \mathbf{U}^{T}
$$

其中， $\boldsymbol{\Lambda}$ 为特征值构成「对角矩阵」， $\boldsymbol{U}$ 为特征向量构成的「正交矩阵」。

因为 $L$ 是[半正定矩阵](https://baike.baidu.com/item/%E5%8D%8A%E6%AD%A3%E5%AE%9A%E7%9F%A9%E9%98%B5/2152711#:~:text=%E5%8D%8A%E6%AD%A3%E5%AE%9A%E7%9F%A9%E9%98%B5%E6%98%AF%20%E6%AD%A3%E5%AE%9A%E7%9F%A9%E9%98%B5%20%E7%9A%84%E6%8E%A8%E5%B9%BF%E3%80%82%20%E5%AE%9E%E5%AF%B9%E7%A7%B0%E7%9F%A9%E9%98%B5%20A%E7%A7%B0%E4%B8%BA%E5%8D%8A%E6%AD%A3%E5%AE%9A%E7%9A%84%EF%BC%8C%E5%A6%82%E6%9E%9C%E4%BA%8C%E6%AC%A1%E5%9E%8BX%27AX%E5%8D%8A%E6%AD%A3%E5%AE%9A%EF%BC%8C%E5%8D%B3%E5%AF%B9%E4%BA%8E%E4%BB%BB%E6%84%8F%E4%B8%8D%E4%B8%BA0%E7%9A%84%E5%AE%9E%E5%88%97%E5%90%91%E9%87%8FX%EF%BC%8C%E9%83%BD%E6%9C%89X%27AX%20%E2%89%A5%200.%20%5B1%5D,%E4%BA%8C%E6%AC%A1%E5%9E%8B%20%E4%B8%8EHermite%E5%9E%8B%E7%9A%84%E7%A0%94%E7%A9%B6%E4%B8%AD%EF%BC%8C%E8%80%8C%E4%B8%94%E5%8F%AA%E9%99%90%E4%BA%8E%E5%AF%B9%20%E5%AE%9E%E5%AF%B9%E7%A7%B0%E7%9F%A9%E9%98%B5%20%E6%88%96%20Hermite%E7%9F%A9%E9%98%B5%20%E7%9A%84%E4%BD%BF%E7%94%A8%E3%80%82%20%E9%9A%8F%E7%9D%80%E6%95%B0%E5%AD%A6%E6%9C%AC%E8%BA%AB%E5%8F%8A%E5%85%B6%E5%AE%83%E5%AD%A6%E7%A7%91%20%28%E5%A6%82%E6%95%B0%E5%AD%A6%E8%A7%84%E5%88%92%E3%80%81%E6%8A%95%E5%85%A5%E4%BA%A7%E5%87%BA%E7%9A%84%E7%9F%A9%E9%98%B5%E7%90%86%E8%AE%BA%E3%80%81%E7%8E%B0%E4%BB%A3%E6%8E%A7%E5%88%B6%E7%AD%89%29%E7%9A%84%E9%9C%80%E8%A6%81%2C%E6%9C%89%E4%B8%8D%E5%B0%91%E4%BA%BA%E5%BC%80%E5%A7%8B%E7%A0%94%E7%A9%B6%E6%9C%AA%E5%BF%85%E5%AF%B9%E7%A7%B0%E7%9A%84%E8%BE%83%E4%B8%BA%E5%B9%BF%E4%B9%89%E7%9A%84%E6%AD%A3%E5%AE%9A%E7%9F%A9%E9%98%B5%E3%80%82)，即对任何非零向量$X$，都有$X^{T}AX≥0$，因此代入图网络向量后可以得到:

$$
\begin{aligned}

f^{T} \mathbf{L} f &=f^{T} D f-f^{T} W f \\

&=\sum_{i} d_{i} f_{i}^{2}-\sum_{i, j} f_{i} f_{j} w_{i j} \\
&=\frac{1}{2}\left(\sum_{i} d_{i} f_{i}^{2}-2 \sum_{i j} f_{i} f_{j} w_{i j}+\sum_{i} d_{i} f_{i}^{2}\right) \\
&=\frac{1}{2} \sum_{i, j} w_{i j}\left(f_{i}-f_{j}\right)^{2}≥0
\end{aligned}
$$

[可分解矩阵特征值和特征向量的几何意义](https://zhuanlan.zhihu.com/p/80817719)

设 $W$ 为可特征分解(谱分解)的矩阵，$\{u_{i}\}$ 是 $W$ 的一组线性无关特征向量，可知任何向量 $v$ 都可由$\{u_{i}\}$ 线性表出：$v=\alpha_{1} u_{1}+\alpha_{2} u_{2}+\cdots+\alpha_{n} u_{n}$ ，若持续地用 $W$ 去乘以向量 $v$ 做变换，可得 

$$
\begin{aligned}

v^{'}=W^{k}v&=W^{k-1}u^{H} \wedge u u^{H} \alpha=W^{k-1}u^{H} \wedge\alpha=W^{k-2}u^{H} \wedge^{2} \alpha\\

&=\cdots=\mu_{1}^{k} \alpha_{1} u_{1}+\mu_{2}^{k} \alpha_{2} u_{2}+\cdots+\mu_{n}^{k} \alpha_{n} u_{n}
\end{aligned}
$$

由上式可知随着 $k$ 的增加，变换后的向量 $v^{'}$ 会收敛到 $W$ 特征值最大的特征向量上。

假设矩阵 $W$ 为拓扑图的一个标准邻接矩阵，其满足 $W_{ii}=0; W_{ij}=1/0\text{(有无邻边)}$，用其乘向量 $f$ 做变换可得$W f=\left(\sum_{j=1}^{n} w_{1, j} x_{j}, \sum_{j=1}^{n} W_{2, j} x_{j}, \ldots, \sum_{j=1}^{n} W_{n, j} x_{j}\right)^{T}$ ，其中第 $i$ 个节点的值为  $(Wf)_{i}=\sum_{\{j|W_{ij}=1\}} x_{j}$，可推得 $Wf$ 会使得向量 $f$ 的某个节点值变为其相邻节点权值的期望值，刻画局部的平滑度。由此可引申为图网络中向量 $f$ 的一种运动过程(不断与 $W$ 相乘)，此过程最终会使得 $f$ 的方向趋向于邻接矩阵 $W$ 特征值最大的特征向量 $u$ 的方向。

假设矩阵为归一化后的拉普拉斯矩阵 $L=I-D^{-1/2}WD^{-1/2}$ ，同时用 $L$ 乘向量 $f$ 可得第 $i$ 个节点的值为$(L x)_{i}=x_{i}-\frac{1}{d} \sum_{j:\{i, j\} \in E} x_{j}$，显然不同于邻接矩阵 $W$ 描述的运动轨迹，laplace 矩阵描述的是原向量运动的位移或者变化量的强度，即每个节点 $i$ 变化到所有邻域节点 $j \in N_{i}$ 所带来的增益(差值、变化量)。

[图网络的傅里叶正反变换及推广卷积](https://www.zhihu.com/question/54504471/answer/332657604)

**传统傅里叶变换**函数定义为：

$$

F(\omega)=\mathcal{F}[f(t)]=\int f(t) e^{-i \omega t} d t

$$

其中 $e^{-i \omega t}$ 刚好满足条件 $\Delta V=ΛV$，即：

$$
\Delta e^{-i \omega t}=\frac{\partial^{2}}{\partial t^{2}} e^{-i \omega t}=-\omega^{2} e^{-i \omega t}
$$

可知 $e^{-i \omega t}$ 是拉普拉斯算子 $\Delta$ 的特征函数。

又因为拉普拉斯矩阵就是离散拉普拉斯算子，模仿上面可以设 $LU=ΛU$，其中 $U$ 是拉普拉斯矩阵 $L$ 经过特征值分解得来的特征向量矩阵，利用 $U$ 和 图网络向量  $f$ 可根据以上定义得出类似的图网络上的傅里叶变换形式 $\hat{f}$ 及其逆变换 $f$ （离散情况下，积分换成求和 $\sum$）：

$$
\begin{aligned}
\hat{f}
 &=\left(\begin{array}{c}
\hat{f}\left(\lambda_{1}\right) \\
\hat{f}\left(\lambda_{2}\right) \\
\vdots \\
\hat{f}\left(\lambda_{N}\right)
\end{array}\right)

=\left(\begin{array}{c}
\sum_{i=1}^{N} x_{i} u_{1}^{*}\left(i\right)  \\
\sum_{i=1}^{N} x_{i} u_{2}^{*}\left(i\right) \\
\vdots \\
\sum_{i=1}^{N} x_{i} u_{N}^{*}\left(i\right)
\end{array}\right)\\

&=\left(\begin{array}{cccc}

u_{1}(1) & u_{1}(2) & \ldots & u_{1}(N) \\

u_{2}(1) & u_{2}(2) & \ldots & u_{2}(N) \\

\vdots & \vdots & \ddots & \vdots \\

u_{N}(1) & u_{N}(2) & \ldots & u_{N}(N)

\end{array}\right)

\left(\begin{array}{c}

x_{1} \\

x_{2} \\

\vdots \\

x_{N}

\end{array}\right)\\
&=U^{T}f\\

f &=UU^{-1}f=UU^{T}f= U \hat{f}

\end{aligned}
$$

其中$f=(x_{1}, x_{2} , \cdots , x_{N})$ 是图网络上的 $N$ 维向量， $x_{i}$ 与图网络的顶点一一对应，表示图网络顶点的状态值， $u_{l}(i)$ 表示第 $l$ 个特征向量的第 $i$ 个分量。那么特征值 (频率) $\lambda_{l}$ 下的， $f$ 的图网络傅里叶变换就是 $f$ 与 $\lambda_{l}$ 对应的特征向量 $u_{l}$ 进行内积运算。

## Graph Convolution Network(图卷积网络定义)

传统的[函数卷积](https://www.zhihu.com/question/22298352)定义为 $f(t)*h(t)$ ，由卷积操作的性质可知函数卷积结果为其傅里叶变换乘积的逆变换，因此通过类比，假设$f=(x_{1}, x_{2} , \cdots , x_{N})$ 是图网络上的 $N$ 维向量，$h$ 为卷积核(自己定义)，代入上述得到的图网络傅里叶变换公式可以得到

$$
\begin{aligned}
(f * h)_{Graph}&=\mathcal{F}^{-1}(\hat{h} \odot \hat{f})=U \hat{h} \odot \hat{f} \\

&=U
\left(\begin{array}{c}
\hat{h}\left(\lambda_{1}\right) \\
\hat{h}\left(\lambda_{2}\right) \\
\vdots \\
\hat{h}\left(\lambda_{N}\right)
\end{array}\right)

\odot

\left(\begin{array}{c}
\hat{f}\left(\lambda_{1}\right) \\
\hat{f}\left(\lambda_{2}\right) \\
\vdots \\
\hat{f}\left(\lambda_{N}\right)
\end{array}\right)\\

&=U
\left(\begin{array}{c}
\hat{h}\left(\lambda_{1}\right)\hat{f}\left(\lambda_{1}\right) \\
\hat{h}\left(\lambda_{2}\right)\hat{f}\left(\lambda_{2}\right) \\
\vdots \\
\hat{h}\left(\lambda_{N}\right)\hat{f}\left(\lambda_{N}\right)
\end{array}\right)\\

&=U \left(\begin{array}{lll}
\hat{h}\left(\lambda_{1}\right) & & \\
& \ddots & \\
& & \hat{h}\left(\lambda_{n}\right)
\end{array}\right) 

\left(\begin{array}{c}
\hat{f}\left(\lambda_{1}\right) \\
\hat{f}\left(\lambda_{2}\right) \\
\vdots \\
\hat{f}\left(\lambda_{N}\right)
\end{array}\right)\\

&=U \left(\begin{array}{lll}
    \hat{h}\left(\lambda_{1}\right) & & \\
    & \ddots & \\
    & & \hat{h}\left(\lambda_{n}\right)
    \end{array}\right) U^{T} f\\
&=U\left(\left(U^{T} h\right) \odot\left(U^{T} f\right)\right)
\end{aligned}
$$

根据上述得到的图卷积公式

$$
(f * h)_{Graph}=U \left(\begin{array}{lll}
    \hat{h}\left(\lambda_{1}\right) & & \\
    & \ddots & \\
    & & \hat{h}\left(\lambda_{n}\right)
    \end{array}\right) U^{T} f
$$

可知公式中的 $U$ 可由拉普拉斯矩阵 $L$ 得到， $f$ 为表征图网络节点状态的向量。

回顾卷积神经网络CNN中的卷积过程是通过设计含有可训练共享参数的kernel来实现的，从上式看就可以很直观的推测：graph convolution中的卷积参数可以定义为 $diag(\hat{h}(\lambda_{l}))$。具体历史定义方法如下：

- **GCN-1**，将 $diag(\hat{h}(\lambda_{l}))$ 直接变成卷积核 $diag(\theta_{l})$
	$$
	y_{\text {output }}=\sigma\left(U 
	
	\left(\begin{array}{lll}
	\theta_{1} &        & \\
	& \ddots & \\
	& & \theta_{N}
	\end{array}\right)
	
	U^{T} x\right)
	$$
	
	缺点：
	
	(1) 每一次前向传播，都要计算 $U ， \operatorname{diag}\left(\theta_{l}\right)$ 及 $U^{T}$ 三者的矩阵乘积，特别是对于大规模的图网络，计算的代价较高，也就是论文中 $\mathcal{O}\left(n^{3}\right)$ 的计算复杂度
	
	(2) 卷积核不具有 spatial localization(空间定位)
	
	(3) 卷积核需要 $N$ 个参数 $\theta_{l}$，才能构成对角参数阵
	
- **GCN-2**，将 $diag(\hat{h}(\lambda_{l}))$ 变成卷积核 $diag(\sum_{j=0}^{K-1} \alpha_{j} \lambda_{l}^{j}), l=1,\cdots,N$，其中 $\lambda$ 为拉普拉斯矩阵 $L$ 的特征值，
	$$
	\begin{aligned}
	y_{\text {output }}&=\sigma\left(U 
	
	\left(\begin{array}{lll}
	\sum_{j=0}^{K-1} \alpha_{j} \lambda_{1}^{j} &        & \\
	& \ddots & \\
	& & \sum_{j=0}^{K-1} \alpha_{j} \lambda_{N}^{j}
	\end{array}\right)
	
	U^{T} x\right) \\
	&=\sigma\left(\sum_{j=0}^{K-1} \alpha_{j} L^{j}x\right)
	\end{aligned}
	$$
	
	优缺点：

	(1) 卷积核只有 $K$ 个参数，一般 $K$ 远小于 $n$ ，参数的复杂度被大大降低了。

	(2) 矩阵变换后，神奇地发现不需要做特征分解了，直接用拉普拉斯矩阵 $L$ 进行变换。然而由于要计算 $L^{j}$ ，计算复杂度还是 $\mathcal{O}\left(n^{3}\right)$

	(3) 卷积核具有很好的spatial localization，特别地， $K$ 就是卷积核的receptive field，也就是说每次卷积会将中心顶点 K-hop neighbor 上的 feature 进行加权求和，权系数就是 $\alpha_{k}$

	更直观地看， $K=1$ 就是对每个顶点上一阶neighbor的feature进行加权求和，如下图所示:

- [**利用Chebyshev多项式作为卷积核**](https://zhuanlan.zhihu.com/p/106687580)

卷积特性对比

传统CNN的特点：局部感知、权值共享、多核卷积、空间下采样

**第一代GCN**的卷积运算矩阵为 $U \operatorname{diag}\left(\theta_{l}\right)U^{T}$，该卷积核对应的卷积矩阵维度大小与输入相等，其所有内部参数均有可能为非零元素，因此对节点进行卷积操作时，会考虑到所有节点，类似于执行全连接操作的卷积核，不是局部感知。

**第二代GCN **的卷积运算矩阵为$U \operatorname{diag}\left(\sum_{j=0}^{K-1} \alpha_{j} \lambda_{l}^{j}\right)U^{T}$，受 **K** 控制,假设维度$N=6$ ，则有：

当 $K=0$ 时卷积运算矩阵为

$$
\left[\begin{array}{cccccc}
\alpha_{0} & 0 & 0 & 0 & 0 & 0 \\
0 & \alpha_{0} & 0 & 0 & 0 & 0 \\
0 & 0 & \alpha_{0} & 0 & 0 & 0 \\
0 & 0 & 0 & \alpha_{0} & 0 & 0 \\
0 & 0 & 0 & 0 & \alpha_{0} & 0 \\
0 & 0 & 0 & 0 & 0 & \alpha_{0}
\end{array}\right]
$$

当 $K=1$ 时卷积运算矩阵为

$$
\left[\begin{array}{cccccc}
\alpha_{0}+2 \alpha_{1} & -\alpha_{1} & 0 & 0 & -\alpha_{1} & 0 \\
-\alpha_{1} & \alpha_{0}+3 \alpha_{1} & -\alpha_{1} & 0 & -\alpha_{1} & 0 \\
0 & -\alpha_{1} & \alpha_{0}+2 \alpha_{1} & -\alpha_{1} & 0 & 0 \\
0 & 0 & -\alpha_{1} & \alpha_{0}+3 \alpha_{1} & -\alpha_{1} & -\alpha_{1} \\
-\alpha_{1} & -\alpha_{1} & 0 & -\alpha_{1} & \alpha_{0}+3 \alpha_{1} & 0 \\
0 & 0 & 0 & -\alpha_{1} & 0 & \alpha_{0}+\alpha_{1}
\end{array}\right]
$$

当 $K=2$ 时卷积运算矩阵为

$$
\left[\begin{array}{cccccc}
\alpha_{0}+2 \alpha_{1}+6 \alpha_{2} & -\alpha_{1}-4 \alpha_{2} & \alpha_{2} & \alpha_{2} & -\alpha_{1}-4 \alpha_{2} & 0 \\
-\alpha_{1}-4 \alpha_{2} & \alpha_{0}+3 \alpha_{1} \dashv 12 \alpha_{2} & -\alpha_{1}-5 \alpha_{2} & 2 \alpha_{2} & -\alpha_{1}-5 \alpha_{2} & 0 \\
\alpha_{2} & -\alpha_{1}-5 \alpha_{2} & \alpha_{0}+2 \alpha_{1}+6 \alpha_{2} & -\alpha_{1}-5 \alpha_{2} & 2 \alpha_{2} & \alpha_{2} \\
\alpha_{2} & 2 \alpha_{2} & -\alpha_{1}-5 \alpha_{2} & \alpha_{0}+3 \alpha_{1}+12 \alpha_{2} & -\alpha_{1}-6 \alpha_{2} & -\alpha_{1}-4 \alpha_{2} \\
-\alpha_{1}-4 \alpha_{2} & -\alpha_{1}-5 \alpha_{2} & 2 \alpha_{2} & -\alpha_{1}-6 \alpha_{2} & \alpha_{0}+3 \alpha_{1}+12 \alpha_{2} & \alpha_{2} \\
0 & 0 & \alpha_{2} & -\alpha_{1}-4 \alpha_{2} & \alpha_{2} & \alpha_{0}+\alpha_{1}+2 \alpha_{2}
\end{array}\right]
$$

根据图网络的邻接矩阵可知非零元素刚好在其每阶的局部位置上。

[GCN-3](https://zhuanlan.zhihu.com/p/120311352)

## GCN的可解释性

## 参考论文

> [GNN 综述](https://zhuanlan.zhihu.com/p/120311352)
>
> 待看
>
> [图神经网络在线研讨会2020丨图表示学习和图神经网络的最新理论进展和应用探索_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1zp4y117bB?spm_id_from=333.999.0.0)
>
> [GraphSAGE：我寻思GCN也没我牛逼 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/74242097)
>
> [一文读懂图卷积GCN - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/89503068)
>
> [图卷积网络(GCN)的谱分析 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/124727955)
>
> [图神经网络中的谱图理论基础 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/368729415)
>
> [(80 条消息) 如何理解 Graph Convolutional Network（GCN）？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/54504471)
>
> [从图(Graph)到图卷积(Graph Convolution)：漫谈图神经网络模型 (一) - SivilTaram - 博客园 (cnblogs.com)](https://www.cnblogs.com/SivilTaram/p/graph_neural_network_1.html) 
