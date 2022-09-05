---
title: "Datamerging(数据合并)"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-03-19 14:39:06
lastmod: 2022-03-19 15:19:21
---

# 额外信息添加方式

定义所需添加信息为 $z_{t}$ ，原输入信息为 $x_{t}$
- ADD: 直接将 $z_{t}$ 添加在 $x_{t}$ 上。

$$

x_{t} \leftarrow x_{t}+z_{t}

$$

CONCAT: 将 $z_{t}$ 拼接在隐藏层 $x_{t}$ 后，使用全连接恢复维度（不恢复维度也可以，但是会造成参数量加倍）。

$$

x_{t} \leftarrow W \cdot \operatorname{concat}\left(x_{t}, z_{t}\right)

$$

MLP: 新添加一个对 $z_{t}$ 的感知单元 $z_{t}\leftarrow W \cdot z_{t}+b$ 。

$$
\begin{aligned}

x_{t}=\tanh \left(\left(W_{xx} \cdot x_{t}\right)+\left(W_{zx} \cdot z_{t}\right)+b_{x}\right)

\end{aligned}
$$
