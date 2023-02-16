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
data: 2022-04-20 12:09:35
lastmod: 2022-04-21 16:49:17
---

# 重点

- [开源代码](https://github.com/pytorch/fairseq/blob/main/fairseq/models/wav2vec/wav2vec2.py)

# 摘要

We show for the first time that learning powerful representations from speech audio alone followed by fine-tuning on transcribed speech can outperform the best semi-supervised methods while being conceptually simpler. wav2vec 2.0 masks the speech input in the latent space and solves a contrastive task defined over a quantization of the latent representations which are jointly learned. Experiments using all labeled data of Librispeech achieve 1.8/3.3 WER on the clean/other test sets. When lowering the amount of labeled data to one hour, wav2vec 2.0 outperforms the previous state of the art on the 100 hour subset while using 100 times less labeled data. Using just ten minutes of labeled data and pre-training on 53k hours of unlabeled data still achieves 4.8/8.2 WER. This demonstrates the feasibility of speech recognition with limited amounts of labeled data.

我们首次提出了一个概念上更简单，性能上优于最好的半监督方法的Wave2vec 2.0模型(仅从语音音频学习强大的表征，然后对转录(目标)的语音进行微调(fine-tuning))。Wave2vec 2.0屏蔽(masks)了潜在空间中的语音输入，并解决了通过联合学习(jointly learned)的潜在表征量化上的对比任务。使用Librispeech的所有标记数据训练，在clean/other测试数据集上获得了1.8/3.3的字错率(WER)。当将使用的标记数据量降低到1小时时，Wave2vec 2.0性能优于以前在100小时子集上的的技术水平，而且使用的标记数据也减少了100倍。当仅仅使用10分钟的标记数据，再使用53k小时的未标记数据进行预训练，仍然可以达到4.8/8.2字错率(WER)。这证明了使用有限数量的标记数据进行语音识别的可行性。

# 结果

# 词汇记录

# 精读

神经网络(Neural networks)的出现和普及得益于大量的带标签的训练数据。然而，在许多情况下，有标签的数据比无标签的数据更难获得。 例如：当前的语音识别系统需要数千小时的转录语音才能达到想要的性能，这在全球近7,000种语言的绝大多数语言中是无法获得的[31]。而且仅仅从有标签的示例数据中学习并不类似于人类的语言学习过程，通常婴儿都是通过倾听周围的成年人说话，从中学习语言（学习良好的言语认知和表达的过程）。

在机器学习中，自我监督学习已经成为一种通用方法，用于从未标记的样本中学习一般数据表示，并使用已标记的数据微调模型。这在自然语言处理方面特别成功[43，45，9]，是计算机视觉的一个热门研究领域[20，2，36，19，6]。

在本文中，提出了一个从原始音频数据中自监督学习音频表征的模型框架。本文的方法通过多层卷积神经网络（multi-layer convolutional neural network）对语音音频进行编码（encode），然后掩蔽得到的潜在语音表征[26，56]，类似于掩蔽语言建模（masked language modeling）[9]。之后再将语音表征馈送到 Transformer 网络中以构建情景表征（考虑上下文的表征），并且通过对比任务（对比学习思想）来训练模型，其中真正的潜在语音表征要与干扰区分开来[54，49，48，28](§2)。

作为训练的一部分，我们通过 Gumbel Softmax[24，5]学习离散的语音单元（speech units）[53，32，7，18]来表示对比任务(图1)中的潜在语音表征，我们发现这些表征比非量化目标更有效。在对未标记的语音进行预训练之后，该模型通过使用Connectionist Temporal Classification(CTC)损失，在有标记数据上进行微调，以用于下行语音识别任务(§3)

以前的工作是先学习数据的量化表征，然后使用自注意力模型（self-attention）获取情景表征[5，4]，而本文的方法端到端地解决了这两个问题。人们已经探索了用 Transformer 网络来掩蔽语音输入的部分[4，26]，但以前的工作要么依赖于两步管道（two-step pipeline），要么通过重建输入的Fbank特征来训练他们的模型。还有其他相关工作，包括自动编码（auto-encoding）输入数据[52，11]或直接预测未来时间步长[8]来学习表征。

我们的结果表明，与前一步[4]中学习的固定单元相比，联合学习（jointly learning）具有情景表征的离散语音单元获得了更好的结果。同时，我们还论证了低资源语音识别的可行性：当只使用10分钟的标记数据时，我们的方法在Librispeech的clean/other测试集上达到了4.8/8.2的单词错误率。我们在Timit音素识别（phoneme recognition）以及Librispeech的100小时 clean 子集上得到了目前最先进的结果。此外，当我们将已标记数据的数量减少到仅仅一个小时，使用相同数量的未标记数据时，尽管只有少了100倍的已标记数据，但我们仍然优于[42]的 self-training 方法。当我们使用来自Librispeech的所有960小时的标记数据时，我们的模型可以达到1.8/3.3WER(§4，§5)。

我们的模型首先通过多层卷积特征编码器（multi-layer convolutional feature encoder，$f：X→Z$ ），以原始音频 $X$ 为输入，输出潜在语音表征 $[z_{1}, \ldots, z_{T}]$ ，$T$ 为时间步长。然后将输出的潜在语音表征馈送到 Transformer $g：Z →C$ 中 ，从整个语音表征序列[9，5，4]捕获信息，以构建情景表征  $[c_{1}, \ldots, c_{T}]$ 。再使用量化模型（quantization module，Z →Q）将特征编码器（ feature encoder）输出的潜在语音表征离散为 $qt$，以表示自监督训练的目标(§3.2)。与VQ-Wav2vec[5]相比，本文的模型在连续的语音表征上构建情景表征，并且通过自注意力模型，端到端地捕获整个潜在表征序列上的依赖关系。

![]({18}_Wav2vec%202.0_%20A%20Framework%20for%20Self-Supervised%20Learning%20of%20Speech%20Representations@baevskiWav2vecFrameworkSelfSupervised2020.assets/image-20220421145614.png)

Feature encoder。该encoder由几个块（block）组成，该块包含时间卷积层（temporal convolution），归一化层（layer normalization）[1]和GELU激活函数[21]。输入编码器的原始波形会被归一化为零均值和单位方差的数据。encoder的总步长（total stride）决定了输入到 Transformer 的时间步长T的数值(§4.2)。

Contextualized representations with Transformers。经过Feature encoder 卷积后的GELU的输出，经过归一化层（layer normalization），被馈送到遵循 Transformer 结构[55，9，33]的情景网络模型，作为输入。同时，本文使用类似于[37，4，57]的卷积层作为相对位置嵌入（relative positional embedding），而不是编码绝对位置信息的固定位置嵌入。

Quantization module。对于自监督训练，我们通过乘积量化[25]（product quantization）将特征编码器的输出离散为一组有限的语音表示。该工作在第一步先学习离散单元（discrete units），然后再学习情景表征[5]。乘积量化相当于从多个码本（codebooks）中选择量化表征，并将它们连接在一起。给定具有V个词目的G个码本或d个码组（$e \in \mathbb{R}^{V \times d / G}$），我们从每个码本中选择一个条目，并将结果向量 $[e_{1}, \ldots, e_{G}]$ 连接起来，并应用线性变换（$\mathbb{R}^{d} \mapsto \mathbb{R}^{f}$）以获得$q \in \mathbb{R}^{f}$

Gumbel Softmax 允许以完全可区分的方式，选择离散的码本条目[16、24、35]。我们使用直通估计器（straight-through estimator）[26]和设置 $G$ hard Gumbel Softmax 运算[24]。特征编码器输出 $Z$ 被映射到 $l \in \mathbb{R}^{G \times V}$ logits(不在0-1范围内的值)，并获得组 $g$ 第 $v$ 个码本条目的概率

$$

p_{g, v}=\frac{\exp \left(l_{g, v}+n_{v}\right) / \tau}{\sum_{k=1}^{V} \exp \left(l_{g, k}+n_{k}\right) / \tau}

$$
其中 $τ$ 是非负温度系数，$n=-\log (-\log (u))$ 并且 $u$ 是来自 $\mathcal{U}(0,1)$ 的均匀样本。在前向传递期间，通过 $i=\operatorname{argmax}_{j} p_{g, j}$ 来选择码字 $i$，并且在后向传递中，使用Gumbel Softmax输出的真实梯度回溯。

为了预训练模型，我们在潜在特征编码器空间中屏蔽（mask）了一定比例的时间步长(§3.1)，类似于BERT[9]中的屏蔽语言建模（masked language modeling）。训练目标要求在每个屏蔽时间步长的一组干扰项中识别正确的量化潜在音频表征(§3.2)，并根据标记的数据对最终模型进行微调(§3.3)。

在将特征编码器的输出馈送到情景网络之前，首先屏蔽一部分输出或时间步，并使用在所有屏蔽时间步之间共享的训练特征向量替换它们；量化模块的输入不使用屏蔽（mask）。为了屏蔽编码器输出的潜在语音表征，通过随机采样得到的一定比例p作为起始索引（要求不替换所有时间步长），然后屏蔽来自每个采样索引的后续M个连续时间步长；中间跨度可能有重叠。


在预训练过程中，我们通过解决对比任务 $\mathcal{L}_{m}$ 来学习语音音频的表征，该任务要求在一组干扰项中识别被屏蔽时间步长的真实量化潜在语音表征。并且使用了码本分集损失（diversity loss）$\mathcal{L}_{d}$ 增强了这一点，以鼓励模型同等地使用每个码本条目。

$$
\mathcal{L}=\mathcal{L}_{m}+\alpha \mathcal{L}_{d}
$$

Contrastive Loss： $\mathcal{L}_{m}$ 

给定以屏蔽时间步 $t$ 为中心的情景网络输出 $c_{t}$，该模型需要在包括 $q_{t}$ 和其他 $K$ 个干扰项[23，54]的K+1个量化表征候选表 $\tilde{\mathbf{q}} \in \mathbf{Q}_{t}$ 的集合中识别真正的量化潜在语音表征 $q_{t}$。其中干扰项从相同 utterance 的其他屏蔽时间步中均匀地采样得到。损失的定义为

$$
\mathcal{L}_{m}=-\log \frac{\exp \left(\operatorname{sim}\left(\mathbf{c}_{\ell}, \mathbf{q}_{\iota}\right) / \kappa\right)}{\sum_{\tilde{\mathbf{q}} \sim \mathbf{Q}_{\iota}} \exp \left(\operatorname{sim}\left(\mathbf{c}_{t}, \tilde{\mathbf{q}}\right) / \kappa\right)}
$$

其中首先计算了情景表征和量化的潜在语音表征之间的余弦相似性 $\operatorname{sim}(\mathbf{a}, \mathbf{b})=\mathbf{a}^{T} \mathbf{b} /\|\mathbf{a}\|\|\mathbf{b}\|$[19，6]。

Diversity Loss：$\mathcal{L}_{d}$

对比任务学习依赖于表征正反例的码本和被设计来增加码本量化表征使用[10]的分集损失 $\mathcal{L}_{d}$。我们通过最大化每个 batch 中每个码本 $\bar{p}_{g}$ 的所有码本条目的 softmax 平均分布 $l$ 的熵（entropy），来鼓励平等地使用每个码本G中的V个条目；其中softmax分布不包含 gumbel 噪声和温度系数

$$
\mathcal{L}_{d}=\frac{1}{G V} \sum_{g=1}^{G}-H\left(\bar{p}_{g}\right)=\frac{1}{G V} \sum_{g=1}^{G} \sum_{v=1}^{V} \bar{p}_{g, v} \log \bar{p}_{g, v}
$$

通过在最后（情景网络后）的一个随机初始化的线性映射，来表征表征C类任务词汇，为语音识别微调预先训练的模型[4]。对于Librispeech，我们有29个作为目标字符的 token，外加一个单词边界 token。训练过程中，通过最小化CTC损失来优化模型[14]，并且我们还在训练期间通过对时间步和通道（channels）进行屏蔽，来应用修改版本的specAugment[41]。specAugment操作延迟了过拟合并显著提高了最终错误率，特别是在具有很少标记样本的Libri-light子集上。

## 引文
