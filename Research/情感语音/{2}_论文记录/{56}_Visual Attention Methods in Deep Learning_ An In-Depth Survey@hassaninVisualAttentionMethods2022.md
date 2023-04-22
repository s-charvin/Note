---
title: "Visual Attention Methods in Deep Learning: An In-Depth Survey"
description: ""
citekey: hassaninVisualAttentionMethods2022
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-04-21 15:50:40
lastmod: 2023-04-22 19:13:41
---

> [!info] 论文信息
>1. Title：Visual Attention Methods in Deep Learning: An In-Depth Survey
>2. Author：Mohammed Hassanin, Saeed Anwar, Ibrahim Radwan, Fahad S. Khan, Ajmal Mian
>3. Entry：[Zotero link](zotero://select/items/@hassaninVisualAttentionMethods2022) [URL link](http://arxiv.org/abs/2204.07756) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Hassanin et al_2022_Visual Attention Methods in Deep Learning.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\TNLRSNH4\\2204.html>)
>4. Other：2022 - arxiv:2204.07756     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- :fas_question:   
- :obs_pdf_file:   
- :obs_graph_glyph:   
- :obs_wand_glyph:   

## 摘要

> [!abstract] Inspired by the human cognitive system, attention is a mechanism that imitates the human cognitive awareness about specific information, amplifying critical details to focus more on the essential aspects of data. Deep learning has employed attention to boost performance for many applications. Interestingly, the same attention design can suit processing different data modalities and can easily be incorporated into large networks. Furthermore, multiple complementary attention mechanisms can be incorporated in one network. Hence, attention techniques have become extremely attractive. However, the literature lacks a comprehensive survey specific to attention techniques to guide researchers in employing attention in their deep models. Note that, besides being demanding in terms of training data and computational resources, transformers only cover a single category in self-attention out of the many categories available. We fill this gap and provide an in-depth survey of 50 attention techniques categorizing them by their most prominent features. We initiate our discussion by introducing the fundamental concepts behind the success of attention mechanism. Next, we furnish some essentials such as the strengths and limitations of each attention category, describe their fundamental building blocks, basic formulations with primary usage, and applications specifically for computer vision. We also discuss the challenges and open questions related to attention mechanism in general. Finally, we recommend possible future research directions for deep attention.

> 受人类认知系统的启发，注意力机制是一种模仿人类对特定信息的认知意识的机制，放大关键细节以更加关注数据的本质方面。深度学习利用注意力机制提高了许多应用程序的性能。有趣的是，相同的注意力机制设计可以适合处理不同的数据模式，并且可以很容易地融入大型网络。此外，多个互补的注意力机制可以合并到一个网络中。因此，研究注意力机制变得极具吸引力。然而，迄今为止很少有针对注意力技术进行全面调查的文献，来指导研究人员在他们的深度学习模型中使用注意力方法。请注意，除了在训练数据和计算资源方面的要求外，transformers 仅涵盖许多可用类别中的自我注意类别。我们填补了这一空白，并对 50 种注意力技术进行了深入调查，并按其最突出的特征对其进行了分类。我们通过介绍注意力机制成功背后的基本概念来开始我们的讨论。接下来，我们提供了一些基本要素，例如每个注意力类别的优势和局限性，描述了它们的基本构建块、具有主要用途的基本公式以及专门用于计算机视觉的应用程序。我们还讨论了与一般注意力机制相关的挑战和未解决的问题。最后，我们推荐了深度关注的未来可能的研究方向。

## 预处理

## 概述

## 结果

## 精读

Attention 与人类认知系统有着天然的联系。根据认知科学，人类视神经接收大量数据，超出其处理能力。因此，人脑会对输入进行权衡，只关注必要的信息。随着机器学习（更具体地说是深度学习）的最新发展，以及处理大量和多输入数据流的能力不断增强，研究人员在许多领域采用了类似的概念，并制定了各种注意力机制，以提高深度神经网络模型的性能机器翻译[1]、[2]、视觉识别[3]、生成模型[4]、多代理强化学习[5]等。在过去的十年中，深度学习取得了突飞猛进的发展，产生了许多能够学习数据中复杂关系的深度神经网络架构。通常，神经网络提供隐式注意以从数据中提取有意义的信息。隐式注意力是指网络在训练过程中自动学习对输入数据的关注和权重分配，而无需显式定义注意力权重。

首次引入深度学习中的显式注意力机制是为了解决为机器翻译问题设计的编码器-解码器架构中的遗忘问题 [6]。通常, 深度学习网络会通过编码器部分专注于生成最具代表性的输入表征向量，再通过解码器部分将表征向量映射为输出结果。而, 双向递归神经网络 (RNN) [6] 被用于从输入序列数据中提取考虑了上下文信息的输入表征向量, 然后根据表征向量以及先前的隐藏状态向量解码输出来, 来解决深度学习网络的遗忘问题。上下文表征向量是通过对中间表征向量进行加权计算得来的，这里通常会采样显式注意力的方法。此外，长短期记忆 (LSTM) [7] 也被用于生成上下文表征向量和输出。两种方法都考虑了编码器的所有隐藏状态来计算上下文表征向量。然而，[8] 引入了另一个想法，让注意力机制只关注部分输入序列的隐藏状态，以生成整个输入序列的上下文表征向量权重。与以前的注意力方法相比，这在计算上更加高效，并且可以在全局和局部注意力之间实现权衡。


Vaswani 等人取得了在基于注意力机制的深度学习架构中取得了突破 [2], 其提出的 Transformer 模型结构均是基于自注意力机制构建的。在此结构中, 其输入序列首先被并行编码为多种表示形式，称为 Key、Query,和 Value, 有助于更有效地捕捉输入序列的元素之间的重要性。自此以后，许多研究人员针对特定应用扩展了基本的 Transformer 架构。

为了关注图像中的重要部分并抑制不必要的信息，基于注意力的学习的进步已经进入多种计算机视觉任务，或者对每个图像像素使用不同的注意力图，将其与图像的表示进行比较其他像素 [3]、[4]、[9] 或生成注意力图以提取整个图像的全局表示 [10]、[11]。然而，注意力机制的设计高度依赖于手头的问题。为了强制选择与输入中的关键信息相对应的隐藏状态，注意力技术已被用作基于视觉的任务中的插件单元，以减轻梯度消失的风险。总而言之，计算注意力分数，并确定性或随机地选择隐藏状态。

在过去几年中，注意力一直是重要研究工作的中心，图像注意力在许多不同的机器学习和视觉应用中蓬勃发展，例如分类 [12]、检测 [13]、图像字幕 [14]、3D 分析 [15] 等。尽管深度学习中使用的注意力技术表现令人印象深刻，但没有文献调查全面回顾视觉中的所有注意力机制，特别是基于深度学习的注意力机制，以根据其基本底层架构对其进行分类并突出其优势和弱点。最近，研究人员调查了特定于应用程序的注意力技术，重点是基于 NLP 的 [16]、基于转换器的 [17]、[18] 和基于图形的方法 [19]。然而，还没有一项全面的研究能够对所有为视觉输入开发的基于深度学习的注意力技术的广泛而多样的范围进行整理。

在本文中，我们回顾了特定于视觉的注意力技术。 我们的调查涵盖了许多基本构建块（操作和功能）和完整的架构，旨在学习合适的表示，同时使模型注意输入图像或视频中的相关和重要信息。 我们的调查对计算机视觉文献中提出的注意力机制进行了广泛的分类，包括软注意力、硬注意力、多模态、算术、类注意力和逻辑注意力。 我们注意到一些方法属于多个类别； 但是，我们将每个方法分配给与该类别的其他方法具有显性关联的类别。 遵循这样的分类有助于追踪常见的注意力机制特征，并提供可能有助于设计新颖注意力技术的见解。 图 2 显示了注意力机制的分类。

我们强调，由于图 1 中概述的大量论文发表，因此有必要在视觉上进行调查。从图 1 中可以明显看出，去年发表的文章数量与往年相比显着增加，并且 我们预计未来几年会出现类似的趋势。 此外，我们的调查列出了具有重要意义的文章，以帮助计算机视觉和机器学习社区在其模型中采用最合适的注意力机制并避免重复注意力方法。 它还确定了研究差距，提供了当前的研究背景，提出了合理的研究方向和未来的重点领域。

由于 Transformer 已被用于许多视觉应用；一些调查 [17]、[18] 总结了计算机视觉中 Transformer 的最新趋势。虽然 Transformer 提供高精度，但这是以非常高的计算复杂性为代价的，这阻碍了它们在移动和嵌入式系统应用中的可行性。此外，基于 Transformer 的模型比 CNN 需要更多的训练数据，并且缺乏有效的硬件设计和通用性。根据我们的调查，Transformer 只涵盖了 50 个不同注意力类别中的一个类别。另一个显着差异是我们的调查侧重于注意力类型，而不是基于 Transformer 的调查 [17]、[18] 中涵盖的应用程序。

### 引文

## 摘录
