---
title: "Padding(填充)"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-03-19 14:37:39
lastmod: 2022-03-19 15:19:27
---

# Padding(填充)

## TensorFlow.Padding 模式： `SAME`

给定输入尺寸 $(m=5,n=5)$ ，移动步长 $s=2$ 后，Filter=(3×3)，可以通过公式  $ceil\left(\frac{n-f+1}{s}\right)$，计算出 Filter 最多右移 2 步，顶点才不会超出边界，同理通过公式  $ceil\left(\frac{m-f+1}{s}\right)$，计算出 Filter 最多下移 2 步。

对于最后一次窗口超出图像边界的部分可以通过公式 $pad_{m(or\ n)}= ceil\left(\frac{m(or\ n)-f+1}{s}\right)×s+f-1-m(or\ n)$ ，得到两个维度总共需要填充的元素维度 $pad_{m(or\ n)}$ 均为 1（即左右共需要填充1维向量，上下也共需要填充1维向量）。
最后计算图的上下左右分别需要填充多少维度向量。

```c
pad_top = floor(pad_m / 2) // =0 // 注意此处向下取整
pad_bottom = pad_m - pad_top // =1
pad_left = floor(pad_n / 2) // =0  // 注意此处向下取整
pad_right = pad_n - pad_left // =1
```

Padding后的数据维度$(ceil(\frac{m }{s}),ceil(\frac{n}{s}))$。
