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
data: 2022-04-17 14:17:35
lastmod: 2022-06-07 12:24:47
---

# 重点：

- 论文原文件
- 使用Speech2Vec和Word2Vec来学习语音和文本的嵌入空间。
- 语音和文本嵌入空间的无监督跨模态对齐

![]({14}_Unsupervised%20Cross-Modal%20Alignment%20of%20Speech%20and%20Text%20Embedding%20Spaces@chungUnsupervisedCrossModalAlignment2018.assets/image-20220304010515.png)

![]({14}_Unsupervised%20Cross-Modal%20Alignment%20of%20Speech%20and%20Text%20Embedding%20Spaces@chungUnsupervisedCrossModalAlignment2018.assets/image-20220304010527.png)

# 摘要

Recent research has shown that word embedding spaces learned from text corpora of different languages can be aligned without any parallel data supervision. Inspired by the success in unsupervised cross-lingual word embeddings, in this paper we target learning a cross-modal alignment between the embedding spaces of speech and text learned from corpora of their respective modalities in an unsupervised fashion. The proposed framework learns the individual speech and text embedding spaces, and attempts to align the two spaces via adversarial training, followed by a refinement procedure. We show how our framework could be used to perform spoken word classification and translation, and the experimental results on these two tasks demonstrate that the performance of our unsupervised alignment approach is comparable to its supervised counterpart. Our framework is especially useful for developing automatic speech recognition (ASR) and speechto-text translation systems for low- or zero-resource languages, which have little parallel audio-text data for training modern supervised ASR and speech-to-text translation models, but account for the majority of the languages spoken across the world.

最近的研究表明，从不同语言的文本语料库学习的单词嵌入空间可以在没有任何并行数据监督的情况下进行对齐。受无监督跨语言单词嵌入的成功启发，本文的目标是在语音和文本的嵌入空间之间进行跨模式对齐，这些空间是以非监督方式从各自的语料库中学习的。该框架学习单个语音和文本嵌入空间，并尝试通过对抗性训练对这两个空间进行对齐，然后进行精化过程。我们展示了我们的框架如何用于口语分类和翻译，在这两个任务上的实验结果表明，我们的无监督对齐方法的性能与它的有监督对齐方法相当。我们的框架对于开发低资源或零资源语言的自动语音识别(ASR)和语音到文本翻译系统特别有用，这些语言几乎没有并行的音频-文本数据来训练现代有监督的ASR和语音到文本翻译模型，但占世界上大多数语言的使用。

# 词汇记录

# 结果

# 精读

一些研究表明，即使是使用不同的语言得到的Word embedding  spaces会有着类似的结构，可以在无任何双语监督的情况下实现跨语言对齐。因此可以想到，是否可以尝试引申到声音与文本的语义嵌入矩阵之间的相似结构，实现跨语音和文本的嵌入空间对齐？

与可以容易地将内容分割成单词的文本不同，语音本质上是连续的，使得每个单词的语音边界难以定位。如果语音语料库中的所有语音都通过强制对齐来获得与单词对应的完美音频段，会使得从语音学习 embedding  spaces 的过程并非真正的无监督。主流的解决方法有 un-supervised term discovery（在语音集合中找到类似单词或短语的模式）、full-coverage approaches（整个语音输入被分割成类似单词的单位，有BES-GMM、ES KMeans、SylSeg。

受此启发，在本文的目标就是在无监督的方式下，将从不同形式语料库中学习到的Speech embedding  spaces和 Text embedding  spaces 实现 cross-modal alignment。这种 Unsupervised cross-modal alignment 对于缺乏语音和文本并行语料库，低资源甚至零资源的automatic speech recognition 和 speech-to-text 翻译系统开发有用。

本文所提出的框架，首先使用 k 均值算法将它们聚类为k个聚类，大致对应于k个不同的单词类型。然后分别使用了Speech2Vec 和 Word2Vec 在独立的语料库中训练语音和文本的 embedding  spaces 。因为 Speech2Vec 和 Word2Vec 共享相同的训练方法，两者有望表现出相似的结构。

在 Word2Vec 模型中，特定单词的嵌入是确定性的，同一单词将仅由一个 embedding  vector 表示。相反，对于 Speech2Vec ，由于说话者信道和其他上下文差异等，相同底层单词的每个语音实例将由不同的 embedding  vector 表示。因此，在学习到上述两个 embedding  spaces 之后，可以对属于同一群集的embedding  vector 进行平均（可能是相同底层单词的实例，也可能是语义上相似的不同单词的实例），以实现一对一的表示。 $S={s_{1}，s_{2}，…，s_{m}}⊆ R^{d1}$和$T={t_{1}，t_{2}，…，t_{n}}⊆ R^{d2}$ 为m个语音单词和n个文本单词对应的两个 embedding  space；$W$ 为其线性映射矩阵，即 $WS=T$ ；

接下来尝试通过 Adversarial training 来学习从Speech embedding  spaces到 Text embedding  spaces的线性映射，然后进行细化。![]({14}_Unsupervised%20Cross-Modal%20Alignment%20of%20Speech%20and%20Text%20Embedding%20Spaces@chungUnsupervisedCrossModalAlignment2018.assets/image-20220304012822.jpeg)

映射矩阵 $W$ 看作是 generator() （输入speech embedding  spaces生成 Text embedding  spaces），后面的 discriminator 用来分辨其获得的随机输入数据，究竟来自generator()还是 原Text embedding  spaces，通过损失函数不断后向调整参数，使得映射矩阵W能够产生与原Text embedding  spaces更相似的数据，即每次鉴别的结果都大致为0.5。

使用 Adversarial training 所得的 $W$ 作为初始映射矩阵，选择 $S$和 $T$ 中出现最频繁的单词构造一个输入数据集，运用==跨域相似性局部缩放==方法进一步细化$W$。
