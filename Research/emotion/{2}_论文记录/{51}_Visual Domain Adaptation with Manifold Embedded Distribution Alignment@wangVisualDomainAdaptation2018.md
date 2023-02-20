---
title: "Visual Domain Adaptation with Manifold Embedded Distribution Alignment"
description: ""
citekey: wangVisualDomainAdaptation2018
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-20 20:46:38
lastmod: 2023-02-20 20:58:12
---

> [!info] 论文信息
>1. Title：Visual Domain Adaptation with Manifold Embedded Distribution Alignment
>2. Author：Jindong Wang, Wenjie Feng, Yiqiang Chen, Han Yu, Meiyu Huang, Philip S. Yu
>3. Entry：[Zotero link](zotero://select/items/@wangVisualDomainAdaptation2018) [URL link](http://arxiv.org/abs/1807.07258) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Wang et al_2018_Visual Domain Adaptation with Manifold Embedded Distribution Alignment.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\HLK8ATMF\\1807.html>)
>4. Other：2018 - arxiv:1807.07258 [cs]  arXiv   -   

>- :luc_github: 论文实现：[https://github.com/wenchieh/MEDA](https://github.com/wenchieh/MEDA)
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 

## 摘要

> [!abstract] Visual domain adaptation aims to learn robust classifiers for the target domain by leveraging knowledge from a source domain. Existing methods either attempt to align the cross-domain distributions, or perform manifold subspace learning. However, there are two significant challenges: (1) degenerated feature transformation, which means that distribution alignment is often performed in the original feature space, where feature distortions are hard to overcome. On the other hand, subspace learning is not sufficient to reduce the distribution divergence. (2) unevaluated distribution alignment, which means that existing distribution alignment methods only align the marginal and conditional distributions with equal importance, while they fail to evaluate the different importance of these two distributions in real applications. In this paper, we propose a Manifold Embedded Distribution Alignment (MEDA) approach to address these challenges. MEDA learns a domain-invariant classifier in Grassmann manifold with structural risk minimization, while performing dynamic distribution alignment to quantitatively account for the relative importance of marginal and conditional distributions. To the best of our knowledge, MEDA is the first attempt to perform dynamic distribution alignment for manifold domain adaptation. Extensive experiments demonstrate that MEDA shows significant improvements in classification accuracy compared to state-of-the-art traditional and deep methods.

> 视觉域适应领域旨在通过利用源域的知识来学习目标域的稳健分类器。现有方法要么试图跨域分布对齐，要么执行流形子空间学习。然而，这样存在两个重大挑战：（1）退化特征变换，这意味着分布对齐通常在原始特征空间中进行，特征失真难以克服。另一方面，子空间学习不足以减少分布散度。 (2)未评估的分布对齐，即现有的分布对齐方法仅对齐具有同等重要性的边际分布和条件分布，而未能评估这两种分布在实际应用中的不同重要性。在本文中，我们提出了一种流形嵌入式分布对齐 (MEDA) 方法来应对这些挑战。 MEDA 在具有结构风险最小化的 Grassmann 流形中学习域不变分类器，同时执行动态分布对齐以定量说明边际分布和条件分布的相对重要性。据我们所知，MEDA 是第一个为流形域自适应执行动态分布对齐的尝试。大量实验表明，与最先进的传统方法和深度方法相比，MEDA 在分类准确性方面有显着提高。

## 预处理

## 概述

## 结果

## 精读

### 引文

## 摘录
