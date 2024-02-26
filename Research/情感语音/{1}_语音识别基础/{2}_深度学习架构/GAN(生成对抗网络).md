---
title: "GAN(生成对抗网络)"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-03-19 14:34:55
lastmod: 2023-11-14 11:55:14
date: 2022-03-19 14:34:55
---

# GAN：生成式对抗网络（Generrative Adversarial Network）

[GAN-Zoo](https://github.com/hindupuravinash/the-gan-zoo
)

相同的输入有不同的输出。

Generator

 Discriminator

给定初始输入向量后，GAN 网络训练大致分为两步，第一步是固定 G 的参数，给 D 输入训练 data 和 G 生成的数据，训练 D，使其能分辨出输入是 G 的还是 data 的，最终的参数更新以最大化 D 的分辨能力为目的，即使得输入训练数据得到的 D(y)，越大越好，输入 D 生成的数据得到的 D(y)，越小越好。也就是说识别到的数据差异越大越好。

![](GAN(生成对抗网络).assets/image-20220304011854.png)



![](GAN(生成对抗网络).assets/image-20220304011913.png)



第二部是固定D的参数，给G输入随机数据，训练G，使得其能够生成类似data的数据，使得D无法准确识别来源，最终的参数更新以最小化G和训练data的数据差异为目的，即可相当于最小化D输入data和生成数据得到的结果，使得无论是输入训练数据还是G生成的数据，其输出预测为0.5。  

![image-20220204212546446](GAN(生成对抗网络).assets/image-20220204212546446.png)

![](GAN(生成对抗网络).assets/image-20220304012012.png)

WGan思想：

JS Diversion 

Wasserstein distance

SNGan

Cycle Gan 单一风格转换

StarGan 多风格转换
