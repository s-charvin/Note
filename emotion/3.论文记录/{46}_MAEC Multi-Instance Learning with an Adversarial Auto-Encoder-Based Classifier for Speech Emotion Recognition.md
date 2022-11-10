---
title: "MAEC: Multi-Instance Learning with an Adversarial Auto-Encoder-Based Classifier for Speech Emotion Recognition"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: "笔记"
draft: true
layout: 
data: 2022-05-16 17:57:55
lastmod: 2022-11-10 10:29:12
---

# 重点

- 开源代码

# 摘要

In this paper, we propose an adversarial auto-encoder-based classifier, which can regularize the distribution of latent representation to smooth the boundaries among categories. Moreover, we adopt multi-instance learning by dividing speech into a bag of segments to capture the most salient moments for presenting an emotion. The proposed model was trained on the IEMOCAP dataset and evaluated on the in-corpus validation set (IEMOCAP) and the cross-corpus validation set (MELD). The experiment results show that our model outperforms the baseline on in-corpus validation and increases the scores on cross-corpus validation with regularization.

在本文中，我们提出了一种基于对抗性自动编码器的分类器，该分类器可以正则化潜在表示的分布，以平滑类别之间的边界。此外，我们采用多实例学习，将语音分成一组片段，以捕捉表达情感的最显著时刻。所提出的模型在 IEMOCAP 数据集上进行训练，并在语料库内验证集（IEMOCAP）和跨语料库验证集（MELD）上进行评估。实验结果表明，我们的模型在语料库内验证方面优于基线，并通过正则化提高了跨语料库验证的分数。

# 结果

# 词汇记录

# 精读

情绪是一种重要的内在状态，它影响人类的目的表达、意图理解和决策[1]。为了提供有效的服务，一些公司采用语音情感识别技术来跟踪客户的感受[2]。人机交互领域的其他研究人员开发了情感检测系统，以改善用户体验[3]。近几十年来，特征工程[4，5]和深度学习模型[6，7]的发展极大地改善了语音情感识别。由于语音样本具有时间序列特性，许多研究都采用了门控递归单元（GRU）[8]、长短记忆网络（LSTMs）[9]或卷积神经网络（CNN）和 LSTMs 的组合[10]来感知时间序列信息。除了考虑语音中包含的特征序列之外，还提出了可以分析对话中的上下文信息的新模型。Yeh 等人[8]提出了一种交互感知网络，以考虑对话中的上下文。Jiao 等人[11]通过考虑上下文，构建了用于话语级情感识别的分层门控重复单元。上述研究在上下文信息的帮助下显著提高了语音情感识别的性能。为了捕捉最有助于标签分配的情感框架，研究人员采用了注意机制[12]，并借用了多实例学习的思想来识别和关注语音话语中最显著的部分[13]。此外，由于语音中的情感因素因性别和人而异，Latif 等人[14]提出了一种多任务学习框架，以提高语音情感识别的性能。尽管在语音情感识别领域取得了进展，但很少有研究探索数据正则化的好处。众所周知，言语情感表达因说话人而异，这种偏见可能会给同一类别下的样本形成聚类或具有不规则边界（非高斯分布）的聚类带来困难。这种情况可能会使模型容易在域内数据集上过度拟合，对模式分布的局部不规则性敏感，并且跨域实现的得分也会降低[15，16，17]。为了通过正则化潜在表示的分布来平滑边界，并赋予模型专注于最显著的语音片段的能力，在本研究中，我们提出了一种基于多实例学习的对抗性自动编码器分类器。我们提出的模型中的鉴别器可以将潜在表示映射到高维高斯分布。我们还采用了性别和情感分类的多任务学习策略。所提出的模型在 IEMOCAP[18]数据集上进行训练，并在语料库内（IEMOCAP）和跨语料库验证集（MELD[19]）上进行评估。我们的论文结构如下。我们在第 2 节描述了我们提出的方法的细节。第 3 节描述了实验设置和结果。第 4 节介绍了讨论，第 5 节简要总结了我们的工作。

我们使用 openSMILE 工具包[5]基于 Emobase 2010 Config 提取了低级声学特征，包括 Mel 频率倒谱系数（MFCC）、F0、过零率及其在每个帧中的统计数据。对于每个音频样本，预处理方法产生一个 45 维的低级声学特征。然后，我们使用具有固定宽度（50ms）和步幅（10ms）的窗口将特征分成若干段，以便将每个样本转换为一组实例（如等式 1 所示）x[i] = [s1, s2, .., sn]。

![]({46}_MAEC%20Multi-Instance%20Learning%20with%20an%20Adversarial%20Auto-Encoder-Based%20Classifier%20for%20Speech%20Emotion%20Recognition.assets/image-20221110092854.png)

图 1 显示了模型的架构。总体结构类似于对抗式自动编码器（AAE），但我们提出的模型只有一个 encoder、一个 discriminator，并用分类器代替 decoder。所提出的模型的输入是用户的前一回合 (the interlocutor’s turn)、对话者的回合 (the user’s current utterance)和用户的当前话语 ( the user’s previous turn )。

编码器的功能是将子样本的前一回合、对话者的回合和当前话语的信息压缩为潜在表征 Z。

首先，我们构建了一个具有[卷积捷径](https://www.cnblogs.com/linzzz98/articles/13454369.html))的空洞卷积块，以处理片段级特征。其中空洞卷积块有两个普通卷积层，和一个空洞卷积层，而卷积捷径仅由普通卷积层组成。然后我们使用全连接层作为过滤信息的 Bottleneck（降低维度，减少参数量）。请注意，空洞卷积块和 Bottleneck 都是逐片段处理特征，并根据原始顺序将其连接为时间序列。

$$
\begin{aligned}
&h_i=\text { DilatedConv }\left(x_i\right) \\
&H=\left[h_1, h_2, \ldots, h_n\right] \\
&b t_i=\text { Bottleneck }\left(h_i\right) \\
&B T=\left[b t_1, b t_2, \ldots, b t_n\right]
\end{aligned}
$$

然后，通过注意力机制得到 HF。其中 Key 部分来自于双向 GRU 处理 H 的输出。Query 部分来自于 Bottleneck 的输出 BT。Value 部分通过对 Key 进行全局池化得到。

$$
\begin{aligned}
&\text { Key }=\operatorname{BiGRU}(H) \\
&A=\text { Attention }(\text { Key, BT }) \\
&K Q=\text { GlobalPooling }(A) \\
&V=G \text { lobalPooling }(\text { Key) } \\
&H F=\text { Multiply }(K Q, V)
\end{aligned}
$$

通过将用户的前一回合、对话者的回合和用户的当前话语放入前述模型中运算。可以得到（分别为 HFpre、HFInt 和 HFcur）三个隐藏层特征，最后融合它们以获得最终的潜在表征 Z。

$$
\begin{aligned}
&P I=\operatorname{Softmax}\left(\operatorname{Multiply}\left(H F_{\text {pre }}, H F_{\text {Int }}\right)\right) \\
&Z=\operatorname{Concatenate}\left(\operatorname{Multiply}\left(HF_{\text {cur }}, PI\right), HF_{cur}\right)
\end{aligned}
$$

在获得潜在表征 Z 之后，我们提出的模型有两个最终阶段：带鉴别器（discriminator）的正则化阶段（D）和分类阶段。我们构造了一个有两个全连接层的 discriminator，其功能是区分 $\mathcal{E}$  N（μ，σ）高斯分布（实）和潜在表征 Z（假）。高斯分布的维数与潜在表征 Z 相同。目的是通过学习对更接近真实样本的样本进行编码来愚弄鉴别器。

$$
L_D=\max \left(\mathbb{E}_{\mathcal{E}}[\log D(\mathcal{E})]+\mathbb{E}_Z[\log (1-D(Z))]\right)
$$

在分类阶段，我们借鉴了多任务学习的思想，构建了一个具有两个分支的分类器：性别分类和情感分类。每个分支由一个致密层组成。等式 7 表示分类器的损失函数，Cg 表示性别分类，Ce 表示情感分类。

$$
L_C=\min \left(\mathbb{E}_Z\left[\log C_g(Z)\right]+\mathbb{E}_Z\left[\log \left(C_e(Z)\right)\right]\right)
$$

在训练过程中，编码器和鉴别器首先运行，然后是分类阶段。请注意，编码器在正则化和分类阶段都进行了训练。在这个训练序列中，潜在表示阶段不仅受到正则化阶段的影响，还受到监督分类阶段的影响。等式 8 表示损失函数。

$$
\begin{aligned}
L_{E n c}=& \min \left(\mathbb{E}_X[\log (1-D(\operatorname{Enc}(X)))]\right.\\
&+\mathbb{E}_X\left[\log \left(C_g(\operatorname{Enc}(X))\right)\right] \\
&\left.+\mathbb{E}_X\left[\log \left(C_e(\operatorname{Enc}(X))\right)\right]\right)
\end{aligned}
$$

## 引文
