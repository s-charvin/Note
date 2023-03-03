---
title: "Multi-Task Learning as Multi-Objective Optimization"
description: ""
citekey: senerMultiTaskLearningMultiObjective2019
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
---

> [!info] 论文信息
>1. Title：Multi-Task Learning as Multi-Objective Optimization
>2. Author：Ozan Sener, Vladlen Koltun
>3. Entry：[Zotero link](zotero://select/items/@senerMultiTaskLearningMultiObjective2019) [URL link](http://arxiv.org/abs/1810.04650) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Sener_Koltun_2019_Multi-Task Learning as Multi-Objective Optimization.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\5MFPXGFP\\1810.html>)
>4. Other：2019 - arxiv:1810.04650 [cs, stat]  arXiv   -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***


## ⭐ 重点

- 

## 摘要

> [!abstract] In multi-task learning, multiple tasks are solved jointly, sharing inductive bias between them. Multi-task learning is inherently a multi-objective problem because different tasks may conflict, necessitating a trade-off. A common compromise is to optimize a proxy objective that minimizes a weighted linear combination of per-task losses. However, this workaround is only valid when the tasks do not compete, which is rarely the case. In this paper, we explicitly cast multi-task learning as multi-objective optimization, with the overall objective of finding a Pareto optimal solution. To this end, we use algorithms developed in the gradient-based multi-objective optimization literature. These algorithms are not directly applicable to large-scale learning problems since they scale poorly with the dimensionality of the gradients and the number of tasks. We therefore propose an upper bound for the multi-objective loss and show that it can be optimized efficiently. We further prove that optimizing this upper bound yields a Pareto optimal solution under realistic assumptions. We apply our method to a variety of multi-task deep learning problems including digit classification, scene understanding (joint semantic segmentation, instance segmentation, and depth estimation), and multi-label classification. Our method produces higher-performing models than recent multi-task learning formulations or per-task training.

> 

## 预处理

## 概述

## 结果

## 精读

### 引文

## 摘录
