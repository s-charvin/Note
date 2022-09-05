---
title: "DomainAdversarial(领域对抗)"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-03-19 14:46:08
lastmod: 2022-03-19 16:24:54
---
![](DomainAdversarial(领域对抗).assets/image-20220304012251.jpeg)


映射矩阵 $W$ 看作是 generator() （输入speech embedding  spaces生成 Text embedding  spaces），后面的 discriminator 用来分辨其获得的随机输入数据，究竟来自generator()还是 原Text embedding  spaces，通过损失函数不断后向调整参数，使得映射矩阵W能够产生与原Text embedding  spaces更相似的数据，即每次鉴别的结果都大致为0.5。
