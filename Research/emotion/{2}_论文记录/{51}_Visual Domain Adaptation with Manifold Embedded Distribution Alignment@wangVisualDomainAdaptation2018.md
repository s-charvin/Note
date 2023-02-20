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
lastmod: 2023-02-20 21:09:39
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

在线媒体和内容共享应用程序的快速增长刺激了对图像和其他多媒体数据的自动识别和分析的巨大需求 [8, 20]。不幸的是，获取足够的标记数据来训练机器学习模型通常既昂贵又耗时。因此，通常有必要利用一些现有领域中丰富的标记样本来促进新目标领域的学习。域适应 [27, 36] 是解决此类跨域学习问题的一种很有前途的方法。由于源域和目标域的分布不同，成功适应的关键是减少分布差异。为此，现有工作可归纳为两大类：(a) Instance-reweighting [9, 39] (寻找一种对输入样本或者输入样本特征进行加权的方法)，根据某种加权技术重用源域中的样本； (b) feature matching，它通过利用子空间几何结构 [13、15、30] 或分布对齐来执行子空间学习以减少域之间的边缘或条件分布差异 [23、40]。我们的重点是特征匹配方法。现有方法存在两个重大挑战，即退化的特征转换和未评估的分布对齐。退化特征变换意味着子空间学习和分布对齐都只能减少而不能消除分布散度[1]。具体来说，子空间学习 [13、15、30] 进行子空间变换以获得更好的特征表示。然而，由于子空间学习仅利用子空间或流形结构，但未能执行特征对齐，因此子空间变换后并未消除特征发散 [22]。另一方面，分布对齐 [23, 26, 37] 通常会减少原始特征空间中的分布距离，而原始特征空间中的特征通常会扭曲 [3]，这使得很难减少域之间的差异。因此，利用子空间学习和分布对齐的优势进一步促进领域适应至关重要。
未评估的分布对齐意味着现有工作 [19, 23, 33, 40] 仅试图将边际分布和条件分布对齐并具有相同的权重。但他们未能评估这两种分布的相对重要性。例如，当两个域非常不同时（图 1(a) → 1(b)），对齐边缘分布更为重要。当边际分布很接近时（图 1(a) → 1(c)），应给予条件分布更大的权重。然而，没有一种比对方法可以定量地说明这两个分布的重要性。

据我们所知，之前还没有一起解决这两个挑战的工作。在本文中，我们提出了一种新的流形嵌入分布对齐 (MEDA) 方法来解决退化特征转换和未评估分布对齐的挑战。 MEDA 在具有结构风险最小化的 Grassmann 流形中学习域不变分类器，同时通过考虑边际分布和条件分布的不同重要性来执行动态分布对齐。我们还提供了一个可行的解决方案来定量评估分布的重要性。据我们所知，MEDA 是第一个试图揭示边际分布和条件分布在领域适应中的相对重要性的尝试。


这项工作做出了以下贡献：1）我们提出了域适应的 MEDA 方法。 MEDA 能够解决退化特征转换和未评估分布对齐的挑战。 2) 我们首次对边缘分布和条件分布在领域适应中的相对重要性进行了定量评估。 这在未来的迁移学习研究中非常有用。 3）对 7 个真实世界图像数据集的大量实验表明，与几种最先进的传统深度方法相比，MEDA 在平均分类准确率方面实现了 3.5% 的显着提高。




给定一个含有标签的源域 $\mathcal{D}_s=\left\{\mathbf{x}_{s_i}, y_{s_i}\right\}_{i=1}^n$ 和一个无标签的目标域 $\mathcal{D}_t=\left\{\mathrm{x}_{t_j}\right\}_{j=n+1}^{n+m}$ , 假设特征空间 $\mathcal{X}_s=\mathcal{X}_t$ , 标签空间 $\boldsymbol{y}_s=\boldsymbol{y}_t$ , but marginal probability $P_s\left(\mathrm{x}_s\right) \neq P_t\left(\mathrm{x}_t\right)$ with conditional probability $Q_s\left(y_s \mid \mathbf{x}_s\right) \neq Q_t\left(y_t \mid \mathbf{x}_t\right)$ . The goal of domain adaptation is to learn a classifier $f: \mathbf{x}_t \mapsto \mathrm{y}_t$ to predict the labels $\mathrm{y}_t \in \boldsymbol{y}_t$ for the target domain $\mathcal{D}_t$ using labeled source domain $\mathcal{D}_s$ . According to the structural risk minimization (SRM) [35], $f=$ $\arg \min _{f \in \mathcal{H}_K} \ell(f(\mathbf{x}), \mathbf{y})+R(f)$ , where the first term indicates the loss on data samples, the second term denotes the regularization term, and $\mathcal{H}_K$ is the Hilbert space induced by kernel function $K(\cdot, \cdot)$ . Since there is no labels on $\mathcal{D}_t$ , we can only perform SRM on $\mathcal{D}_s$ . Moreover, due to the different distributions between $\mathcal{D}_s$ and $\mathcal{D}_t$ , it is necessary to add other constraints to maximize the distribution consistency while learning $f$ .

### 引文

## 摘录
