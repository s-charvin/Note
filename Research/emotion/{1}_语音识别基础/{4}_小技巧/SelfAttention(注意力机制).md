---
title: "SelfAttention(注意力机制)"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-03-19 14:43:52
lastmod: 2022-03-19 16:26:35
---

# *Self Attention

![image-20220208095202208](SelfAttention(注意力机制).assets/image-20220208095202208.png)

![](SelfAttention(注意力机制).assets/image-20220304012049.png)





![](SelfAttention(注意力机制).assets/image-20220304012101.png)





![](SelfAttention(注意力机制).assets/image-20220304012111.png)


$$
\begin{array}{l}

I^{[n*d_{k}]} =\left[a_{1}, a_{2}, a_{3}, \ldots \cdot, a_{n}\right]^{\top}\\

Q^{[n*d_{k}]} = I \cdot W_{q}  =\left[q_{1}, q_{2}, q_{3}, \ldots \ldots, q_{n}\right]^{\top}\\

K^{[n*d_{k}]} =I \cdot W_{k}  =\left[k_{1}, k_{2}, k_{3}, \cdots \cdot \ldots, k_{n}\right]^{\top}\\

V^{[n*d_{v}]} =I \cdot W_{v}  = \left[v_{1}, v_{2}, v_{3}, \cdots \cdot \ldots, v_{n}\right]^{\top}\\

A^{[n*n]}=Q K^{\top} \\

\quad =\left[\begin{array}{ccc}

q_{1} k_{1}^{\top}, & q_{1} k_{2}^{\top}, & q_{1} k_{3}^{\top}, & \ldots \ldots, & q_{1} k_{n}^{\top} \\

q_{2} k_{1}^{\top}, & q_{2} k_{2}^{\top}, & q_{2} k_{3}^{\top}, & \ldots \ldots, & q_{2} k_{n}^{\top} \\

\vdots & \vdots & \vdots & & \vdots \\
\vdots & \vdots & \vdots & & \vdots \\

q_{n} k_{1}^{\top}, & q_{n} k_{2}^{\top}, & q_{n} k_{3}^{\top}, & \ldots \ldots, & q_{n} k_{n}^{\top}

\end{array}\right]\\

\quad =\left[\begin{array}{ccc}

\alpha_{1,1}, & \alpha_{1,2}, & \alpha_{1,3}, & \ldots \ldots, & \alpha_{1,n} \\
\alpha_{2,1}, & \alpha_{2,2}, & \alpha_{2,3}, & \ldots \ldots, & \alpha_{2,n} \\
\vdots & \vdots & \vdots & & \vdots \\
\vdots & \vdots & \vdots & & \vdots \\
\alpha_{n,1}, & \alpha_{n,2}, & \alpha_{n,3}, & \ldots \ldots, & \alpha_{n,n}
\end{array}\right] \\
\quad =\left[A_{1}, A_{2}, A_{3}, \cdots \cdot \ldots, A_{n}\right]^{\top}\\

O^{[n*d_{v}]} = A \cdot V =\left[\begin{array}{c}

v_{1}\alpha_{1,1}+v_{2}\alpha_{1,2}+\ldots \ldots+v_{n}\alpha_{1,n}\\

v_{1}\alpha_{2,1}+v_{2}\alpha_{2,2}+\ldots \ldots+v_{n}\alpha_{2,n}\\

\vdots \\

v_{1}\alpha_{n,1}+v_{2}\alpha_{n,2}+\ldots \ldots+v_{n}\alpha_{n,n}\\

\end{array}\right]^{T}\\

\end{array}
$$


> 将输入序列构成一个矩阵 **I** ，每一个col为原始的单数据序列。
>
> 初始化三个矩阵**W**^q/k/v^，使用 **W** 对 **I** 进行矩阵点积运算得到三个矩阵 **Q**（所有数据序列的query向量（搜索特征）所构成的矩阵）、**K**（所有数据序列的key向量所构成的矩阵）、**V**（计算得到所有数据序列的value向量（权重）所构成的矩阵）
>
> > Query，Key，Value的概念取自于信息检索系统。例：当你在某电商平台搜索某件商品（年轻女士冬季穿的红色薄款羽绒服）时，你在搜索引擎上输入的内容便是Query，然后搜索引擎根据Query为你匹配Key（例如商品的种类，颜色，描述等），然后根据Query和Key的相似度得到匹配的内容（Value)。
>
> 由矩阵**Q**和**K**计算出相关向量矩阵**A**（得到每一个输入向量与其他输入向量互相间的相关系数，越大代表越相似），其中**Ai**为每一个输入向量对应的搜索向量**qi**与其余所有输入向量的key向量（含自身）**ki **运算得到的相关系数构成的向量。
>
> **V**与相关向量矩阵**A’**相乘，**A‘**在softmax层中，已经被转为了一种大小在$[0-1]$的权重系数，因此此运算相当于将从输入向量得到的value向量矩阵 **V** 中的每个向量进行加权求和，最终得到新的嵌入向量矩阵。

Multi-head self-attention

Multi-Head Attention 就是使用多个Self-attention操作，得到多个**O**，然后将**O**拼接得到一个更大维度的嵌入向量，然后通过一个全连接层得到嵌入向量矩阵。

Positional Encoding

解决随着网络层数的增多，训练集loss逐渐下降，然后趋于饱和，但是当再增加网络深度的时候，训练集loss反而会增大的问题。

Truncated Self-attention

cross Attention

Attention内部的q来自于自身，kv来自于其他地方。

Guided Attention

限定Attention的方向（如，由左向右的语音辨识和合成）
