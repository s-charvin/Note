---
title: ""
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-04-22 13:30:00
lastmod: 2022-04-22 13:30:33
---

# Position Embedding 解析

原始的Attention结构，即使输入词序顺序被打乱（意味着使用相同矩阵 $I$ 经 $W$ 得到的 $K$，$V$ 均按行打乱顺序），最终得到 Attention 结果值是不会变化的。

但是如果引入一个位置向量，将词向量与位置向量结合，这样Attention最终的结果就会因为词向量在的不同位置，而产生变化。
