---
title: "Learning Transferable Visual Models From Natural Language Supervision"
description: ""
citekey: radfordLearningTransferableVisual2021a
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:35:52
lastmod: 2023-04-11 13:05:25
---

> [!info] 论文信息
>1. Title：Learning Transferable Visual Models From Natural Language Supervision
>2. Author：Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever
>3. Entry：[Zotero link](zotero://select/items/@radfordLearningTransferableVisual2021a) [URL link](http://arxiv.org/abs/2103.00020) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Radford et al_2021_Learning Transferable Visual Models From Natural Language Supervision5.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\ZEPSNSXC\\2103.html>)
>4. Other：2021 - arxiv:2103.00020 [cs]  arXiv   -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 

## 摘要

> [!abstract] State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision. We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training. For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on. We release our code and pre-trained model weights at https://github.com/OpenAI/CLIP.

> 当前最先进的计算机视觉模型通常都被训练用于预测一组预先定义好的固定的对象类别。由于此类模型通常需要额外的标注数据，才能被用于预测其他视觉 “ 概念 ”，因此这种严格的监督训练方式限制了模型的泛化性和实用性。而本文认为如果能直接从有关图像的描述文本中学习表征是一种很有潜力的替代方案，因为这样能够获取更多的监督源。本文证明了通过指定的预训练任务（预测哪个文本描述对应当前图像），可以在从互联网上收集的 4 亿个图像、文本对的数据集上，从头开始学习到 SOTA 的图像表征。并在预训练完成之后，使用自然语言（文本）匹配要学习的视觉概念（或描述新的概念），从而使模型能够零样本迁移（zero-shot transfer）到下游任务。我们通过在 30 多个不同类型下游任务（OCR、视频动作识别、地理定位和许多类型的细粒度对象分类等任务）中的现有计算机视觉数据集上进行了基准测试，测试了此方法的性能表现，展示了该模型极为强大的迁移能力，其下游任务性能超过了或接近于一些全监督的基线任务，而无需任何额外的数据训练。例如，我们在 ImageNet 零样本准确率（zero-shot accuracy）能够达到全监督训练的 ResNet-50 的水准，而无需使用它所训练的 128 万个训练示例中的任何一个。我们在 [https://github.com/OpenAI/CLIP](https://github.com/OpenAI/CLIP) 上发布我们的代码和预训练模型权重。

## 预处理

## 概述

## 结果

## 精读

引言

在过去几年中，直接从原始描述文本中学习的预训练方法彻底改变了 NLP。 “text-to-text”作为标准化输入输出接口，使与任务无关的架构能够零样本（zero-shot）迁移到下游任务数据集。甚至像 GPT-3 这样的模型，几乎不需要指定训练数据集的数据，就可以应用在许多定制模型任务中，并有非常优秀的表现。

这些结果表明，在网络大规模（web-scale）的文本数据集中，现代预训练方法中的聚合监督超过了高质量的人工标注的 NLP 数据集。然而，在计算机视觉等其他领域，在 ImageNet 等基于人工标注的数据集上训练预训练模型仍然是标准做法。这不禁让人想问，前述的扩展预训练方法（直接从描述文本中学习）能否在计算机视觉领域取得类似的突破？

乔林等人。 （2016 年）证明，在 image captions （用单词描述图像中的视觉内容的任务）任务中经过预训练的 CNN 模型学习到的表征与以 ImageNet 训练得到的效果接近。
**李等人。 (2017)** 然后将这种方法扩展到预测短语 n-gram 以及单个单词，并展示了他们的系统零样本（zero-shot）迁移到其他图像分类数据集的能力。

VirTex (Desai &amp; Johnson, 2020)、ICLMM (Bulent Sariyildiz et al, 2020) 和 ConVIRT (Zhang et al, 2020) 使用最新的网路结构和预训练方法，证明了基于 transformer 的模型结构，可以在语言建模、掩码语言建模和对比目标等任务中，从文本中学习图像表征。

然而，上述模型的性能仍然低于当前计算机视觉领域的 SOTA 模型，例如 Big Transfer (Kolesnikov et al, 2019) 和弱监督 ResNeXt (Mahajan et al, 2018)。一个关键的区别就是规模。Kolesnikov 和 Mahajan 在数百万到数十亿张图像上训练了 accelerator years（单个加速设备需要训练一年时间），然而 VirTex（自回归预测方式）、ICLMM（完形填空的方式） 和 ConVIRT 仅在 1 到 20 万张图像上训练了 celerator days。我们的贡献之一就是缩小了这一差距，并研究了大规模自然语言监督训练的图像模型的表现。我们提出了一个从头开始训练的 ConVIRT 的简化版本，我们称之为 CLIP，用于对比语言图像预训练（Contrastive LanguageImage Pre-training），这是一种从自然语言监督中学习的有效且可扩展的方法。我们发现 CLIP 在预训练期间学会了执行一系列更广泛的任务，包括 OCR、地理定位、动作识别，并且在计算效率更高的同时优于最好的公开可用的 ImageNet 模型。我们还发现，Zero-shot CLIP 模型比同等精度的监督 ImageNet 模型更稳健。

方法

我们工作的核心目的是要从文本描述（自然语言）的监督信号中学习视觉表征。在下面的小节中，我们将详细介绍我们的具体方法。

Creating a Sufficiently Large Dataset

目前本文工作主要使用了三个数据集，MS-COCO (Lin et al, 2014)、Visual Genome (Krishna et al, 2017) 和 YFCC100M (Thomee et al, 2016)。虽然 MS-COCO 和 Visual Genome 是高质量的人工标注数据集，但以现代标准看待，它们其实都很小，每个大约 有100,000 张训练照片。相比之下，其他计算机视觉系统接受了多达 35 亿张 Instagram 照片的训练（Mahajan 等人，2018 年）。其中 YFCC100M 拥有 1 亿张照片，但每张图像的元数据都很稀疏且质量参差不齐。甚至许多图像使用的自动生成的文件名，如 20160716_113957.JPG 作为“标题”或包含相机曝光设置的“描述文本”。在经过过滤，仅保留带有文本描述标题或英文描述的图像后，数据集缩小了6 倍，仅包含 1500 万张照片。这与 ImageNet 的大小大致相同。

文本语言监督的一个主要动机来源就是因为互联网上含有大量这种形式的公开数据。为了测试这一点，我们构建了一个新的数据集，其中包含从各种公开资源中收集的 4 亿对（图像、文本对）。同时为了尝试覆盖尽可能广泛的视觉概念，我们预先设定了500,000个词语作为queries（wiki中至少出现100次的词语/词组？），然后利用其中的每个 词 query 来爬取对应的图像-文本对，并且每个 query 对应的图像-文本对包含多达 20,000 个查询结果。最终得到的数据集的总数与用于训练 GPT-2 的 WebText 数据集相似。我们将此数据集称为 Web Image Text 的 WIT。

Selecting an Efficient Pre-Training Method

我们最初的方法，类似于 VirTex 网络，从头开始联合训练 CNN结构处理图像和 transformer 结构处理文本，来预测出图像的完整描述文本。但是，当我们想要进行方法迁移时遇到了困难。在图 2 中，可以看到我们使用的一个 6300 万参数的 Transformer 语言模型（两倍于 ResNet50 图像编码器的计算量）去训练学习识别 ImageNet 类别的速度比 Joulin（2016） 等人的方法（预测相同的词袋编码文本）慢了三倍。 

最近在 **对比表征学习（contrastive representation learning）（Tian et al, 2019）** 方面的工作发现，对比目标方法可以胜过等效的直接预测目标方法。通过这一发现，我们探索训练了一个系统来解决可能更容易的替代任务（proxy task），即仅预测整个文本描述与哪个图像配对，而不是预测完整文本描述。以同一个预测词袋编码文本模型作为基线，我们将模型预测目标换成了的对比任务目标，并观察到零样本迁移（zero-shot transfer）到 ImageNet 任务的效率进一步提高了 4 倍。

给定一个有 $N$ 个图像-文本对的 batch，CLIP 网络被训练来预测每 batch 中实际发生的$N\times N$ 个可能的图像-文本对中的哪一个。为此，CLIP 通过联合训练图像编码器和文本编码器来学习多模态嵌入空间，以最大限度地提高批次中 N 个真实图像-文本对的图像嵌入和文本嵌入的余弦相似度，同时最小化$N^{2}-N$ 个不正确的图像-文本对嵌入的余弦相似度。我们在这些相似性分数上优化了对称交叉熵损失。在图 3 中，我们展示 CLIP 架构实现的核心伪代码。这种批量构建技术和目标最初是作为多类 $N$-pair loss Sohn (2016) 引入的，最近被 Zhang 等人用于医学成像领域的对比（文本、图像）表征学习。 （2020 年）。


给定一批 N（图像，文本）对，训练 CLIP 以预测批次中 N × N 可能的（图像，文本）对中的哪一个实际发生。为此，CLIP 通过联合训练图像编码器和文本编码器来学习多模态嵌入空间，以最大化批次中 N 个实数对的图像和文本嵌入的余弦相似度，同时最小化嵌入的余弦相似度。 N 2 - N 个不正确的配对。我们在这些相似性分数上优化了对称交叉熵损失。在图 3 中，我们包含了 CLIP 实现核心的伪代码。这种 batch 内构建的技术和目标最初被引入到了 multi-class N-pair loss (2016) 的，并且最近被 Zhang 等人用于医学成像领域的对比（文本、图像）表征学习。 （2020 年）。

由于过拟合不是主要问题，与 Zhang （2020 年）等人相比，训练 CLIP 的细节被简化了。 我们从头开始训练 CLIP，而不是使用预训练的权重进行初始化。我们移除了表征和对比嵌入空间之间的非线性投影。我们仅使用线性投影将每个编码器的表征映射到多模态嵌入空间。（注：在单模态训练中，似乎可以通过非线性投影提升准确率，但是多模态就没什么大用）

我们还删除了文本转换函数 $t_{u}$，它从文本中统一采样单个句子，因为 CLIP 预训练数据集中的许多图像-文本对只是一个句子。我们还简化了图像变换函数$t_{v}$。，仅使用调整大小图像的随机方形裁剪作为训练期间使用的唯一数据增强方法。最后在训练期间，将控制 softmax 的 logits 范围的温度参数 $\tau$ 直接优化为log-parameterized multiplicative scalar，以避免变成超参数。

Choosing and Scaling a Model

我们为图像编码器考虑了两种不同的架构。首先，我们使用 ResNet50 (He et al, 2016a) 作为图像编码器的基础架构，因为它的广泛采用和经过验证的性能。我们使用 He 等人的 ResNetD 改进对原始版本进行了一些修改。 (2019) 和 Zhang (2019) 的抗锯齿 rect-2 模糊池。我们还用注意力池机制替换了全局平均池层。注意力池实现为单层“transformer-style”的多头 QKV 注意力，其中 query 以图像的全局平均池表征为条件。对于第二种架构，我们尝试了最近推出的 Vision Transformer (ViT) (Dosovitskiy et al, 2020)。我们密切关注他们的实现，只进行了微小的修改，即在transformer之前向组合的patch和位置嵌入添加了额外的 layer normalization，并使用稍微不同的初始化方案。

文本编码器是一个 Transformer (Vaswani et al, 2017)，具体架构修改基于 Radford et al （2019）。这里的基本尺寸使用的是具有 8 个注意力头的 12 层 512 维模型。Transformer 对文本的小写字节使用  BPE 编码表征 (Sennrich et al, 2015)。文本序列使用 [SOS] 和 [EOS] 标记括起来，并且在Transformer的最高层，使用 [EOS] 标记处的token用作文本的特征表征，然后将该文本表征经过 layer normalized，线性投影到多模态嵌入空间。 其中，在文本编码器中使用的Masked self-attention，用来保留添加语言建模作为辅助目标的能力，尽管对此的探索留作未来的工作。

虽然以前的计算机视觉研究通常通过单独增加宽度（Mahajan 等人，2018）或深度（He 等人，2016a）来缩放模型，但对于 ResNet 图像编码器，我们采用了 Tan &amp; Le (2019) 的方法它发现在所有宽度、深度和分辨率上分配额外的计算优于仅将其分配到一个维度。我们使用一个简单的变体，该变体平均分配额外的计算来增加模型的宽度、深度和分辨率。对于文本编码器，我们只缩放模型的宽度，使其与计算的 ResNet 宽度增加成正比，根本不缩放深度，因为我们发现 CLIP 的性能对文本编码器不太敏感。

Pre-training

我们训练了一系列 5 个 ResNets 和 3 个 Vision Transformer。对于 ResNet，我们训练了一个 ResNet50、一个 ResNet101，然后是另外 3 个遵循 EfficientNet 风格的模型缩放并使用大约   $\mathrm{4x}$、 $\mathrm{16x}$ 和 $\mathrm{64x}$ 的 ResNet50 进行计算。它们分别表征为 RN50x4、RN50x16 和 RN50x64。对于 Vision Transformers，我们训练了 ViT-B/32、ViT-B/16 和 ViT-L/14。最大的 ResNet 模型 RN50x64 在 592 个 V100的 GPU 上训练了 18 天，而最大的 Vision Transformer 在 256 个 V100 的GPU 上训练了 12 天。对于 ViT-L/14，我们还以更高的 336 像素分辨率预训练一个额外的 epoch，以提高类似于 FixRes 的性能（Touvron 等人，2019 年）。我们将此模型表征为 ViT-L/14@336px。下文中提到的CLIP，都是以效果最好的ViT-L/14@336px为基准。

Using CLIP

CLIP 经过预训练，可以预测图像和文本片段是否在 WIT 中配对。为了将 CLIP 应用于下游任务，我们重用此功能并研究 CLIP 在标准计算机视觉数据集上的 zero-shot 迁移性能。类似于 Radford 等人（2019）的工作，我们将其作为衡量系统任务学习能力（而不是其表征学习能力）的一种方式。对于每个数据集，我们使用数据集中所有类的名称作为潜在文本对的集合，并根据 CLIP 预测最可能的（图像、文本对）。我们还尝试为 CLIP 提供文本提示，以帮助指定任务以及集成多个这些模板以提高性能。然而，由于绝大多数无监督和自我监督的计算机视觉研究都集中在表征学习上，我们还使用通用的 linear probe protocol 对 CLIP 进行了研究。

分析

Initial Comparison to Visual N-Grams

据我们所知，Visual N-Grams (Li et al, 2017) 首先以上述方式研究了零样本迁移到现有图像分类数据集。这也是我们知道的唯一一项使用与任务无关的预训练模型研究零样本迁移到标准图像分类数据集的工作。在表 1 中，我们将 Visual N-Grams 与 CLIP 进行了比较。即使没有使用 128 万个人工标记的训练示例，最好的 CLIP 模型将 ImageNet 上的准确率从概念证明的 11.5% 提高到了 76.2%，并且与原始 ResNet50 的性能相匹配。此外，CLIP 模型的 top-5 准确率明显更高，该模型的 top-5 准确率达到 95%，与 Inception-V4 相匹配（Szegedy 等人，2016）。这种在零样本设置中匹配强大的、完全监督的基线性能的能力表明，CLIP 是朝着灵活实用的零样本计算机视觉分类器迈出的重要一步。这种比较不是直接的，因为 CLIP 和 Visual N-Grams 之间的许多差异没有得到控制。作为更仔细的比较，我们在与 Visual N-Grams 训练相同的 YFCC100M 数据集上训练了一个 CLIP ResNet50，发现它与 Visual N-Grams 在使用 V100 GPU 训练一天得到的 ImageNet 性能相匹配。该基线模型也是从头开始训练的，而不是像在 Visual N-Grams 中那样从预训练的 ImageNet 权重初始化。

Zero-Shot Performance

在计算机视觉中，零样本学习通常是指在图像分类中泛化到看不见的对象类别的研究（Lampert et al, 2009）。相反，我们的工作是在更广泛的意义上使用该方法，研究对看不见的数据集的泛化。正如 Larochelle （2008 年）等人的零数据学习论文所期望的那样，我们将其作为执行看不见的任务的代理 。虽然无监督学习领域的许多研究都集中在机器学习系统的表征学习能力上，但我们鼓励研究零样本迁移作为衡量机器学习系统任务学习能力的一种方式。在这种观点下，我们使用数据集来评估特定分布上任务的性能。然而，研究界创建了许多流行的计算机视觉数据集，主要作为基准来指导通用图像分类方法的开发，而不是衡量特定任务的性能。据我们所知，Visual N-Grams (Li et al, 2017) 首先以上述方式研究了零样本迁移到现有图像分类数据集。


为了进行更全面的分析，我们实施了一个更大的评估方案，具体详见补充材料。总体而言，我们将 Visual N-Grams 中报告的 3 个数据集扩展到 30 多个数据集，并与 50 多个现有的计算机视觉系统进行比较，以结合背景说明结果。刚开始，我们观察了 CLIP 的零样本分类器与现成基线模型的表现比较：在标准 ResNet50 的特征上拟合一个完全监督的、正则化的逻辑回归分类器。在图 4 中，我们展示了跨 27 个数据集的比较。

Zero-shot CLIP 在 27 个数据集中的 16 个数据集上略微优于该基线模型。数据集 zero-shot CLIP 改进最多的是 STL10，该数据集旨在通过仅包含有限数量的标记示例来增强无监督学习。Zero-shot CLIP，不使用任何训练示例，在这个数据集上达到了 99.3%，这似乎是一个新的 SOTA。在细粒度分类任务中，我们观察到性能的广泛分布。在其中两个数据集上，Stanford Cars 和 Food101，zeroshot CLIP 在 ResNet50 特征上的逻辑回归性能超过 20%，而在 Flowers102 和 FGVCAircraft 上，zeroshot CLIP 的性能低于 10%。我们怀疑这些差异主要是由于 WIT 和 ImageNet 之间的每个任务监督量不同。在 ImageNet、CIFAR10 和 PascalVOC2007 等“通用”对象分类数据集上，性能相对相似，Zero-shot CLIP 略有优势。在测量视频中动作识别的两个数据集上，Zero-shot CLIP 的性能明显优于 ResNet50。在 Kinetics700 上，CLIP 比 ResNet50 高 14.5%。 Zero-shot CLIP 在 UCF101 上的性能也比 ResNet50 的特征高出 7.7%。我们推测这是因为与 ImageNet 中以名词为中心的对象监督相比，自然语言为涉及动词的视觉概念提供了更广泛的监督，。

我们发现 Zero-shot CLIP CLIP 在卫星图像分类（EuroSAT 和 RESISC45）、淋巴结肿瘤检测（PatchCamelyon）、合成场景中的对象计数（CLEVRCounts）、自动驾驶相关任务，例如德国交通标志识别（GTSRB）、识别最近汽车的距离（KITTI Distance）等几个专门的、复杂或抽象的任务上的能力相当薄弱。这些结果突出了 Zero-shot CLIP 在更复杂任务上的能力差。相比之下，非专家人员可以稳定地完成其中一些任务，例如计数、卫星图像分类和交通标志识别，这表明本架构还有很大的改进空间。然而，我们需要提醒的是，对于学习者之前没有经验的困难任务（例如几乎所有人类的淋巴结肿瘤分类），采用零样本迁移（相对于小样本迁移）方法尚不清楚是否有意义。

尽管在将零样本迁移与完全监督模型的表现进行比较时，会突出 CLIP 的任务学习能力，但是与少样本（few-shot）方法进行比较是更直接的比较，因为零样本是少样本方法的极限。在图 5 中，我们可视化了 Zero-shot CLIP 与少样本逻辑回归方法在许多图像模型的特征上的比较，包括最好的公开可用的 ImageNet 模型、自我监督学习方法和 CLIP 本身。虽然人们可能期望Zero-shot的表现不如 one-shot，但我们发现 Zero-shot CLIP 与 4-shot 逻辑回归在相同特征空间上的性能相匹配。这可能是由于零样本和少样本方法之间的关键区别。首先，CLIP 的零样本分类器是通过自然语言生成的，它允许直接指定(“communicated”)的视觉概念。相比之下，“normal” 的监督学习必须从训练样本中间接推断出概念。无上下文的基于示例的学习的缺点是许多不同的假设可以与数据一致，尤其是在一次性的情况下。单个图像通常包含许多不同的视觉概念。尽管有能力的学习者能够利用视觉线索和启发式方法，例如假设所展示的概念是图像中的主要对象，但并不能保证。


在将 Zero-shot CLIP 与其他模型特征的少样本逻辑回归方法进行比较时，Zero-shot CLIP 大致匹配我们评估任务中性能最佳的 16-shot 分类器的性能，该评估任务使用 BiT-M ResNet152x2 的特征在 ImageNet-21K 上训练。我们确信在 JFT-300M 上训练的 BiT-L 模型会表现得更好，但这些模型尚未公开发布。 BiT-M ResNet152x2 在 16-shot 设置中表现最佳有点令人惊讶，因为正如第 3.3 节中分析的那样，Noisy Student EfficientNet-L2 在完全监督的设置中在 27 个数据集上的平均性能优于它近 5%。

Representation Learning

虽然我们专注于通过零样本迁移研究 CLIP 的任务学习能力，但更常见的是研究模型的表征学习能力。我们使用 linear probe evaluation protocol，因为它需要最少的超参数调整并且具有标准化的评估程序。有关评估的更多详细信息，请参阅补充材料。


图 6 总结了我们的发现。为了尽量减少可能引起确认或报告偏差问题的选择效应，我们首先研究了 Kornblith（2019） 等人的 12 个数据集评估任务的性能 。使用 CLIP 训练的模型在计算上的扩展性非常好，我们最大的模型在总体得分和计算效率方面都略胜于现有的最佳模型（Noisy Student EfficientNet-L2）。我们还发现 CLIP vision transformers的计算效率比 CLIP ResNets 高约 3 倍，这可以在我们的计算预算范围内实现更高的整体性能。这些结果复制了 Dosovitskiy（2020） 等人的研究结果。 报告说，在足够大的数据集上训练时，vision transformer的计算效率比卷积网络更高。我们最好的整体模型 ViT-L/14@336px 比这个评估任务中最好的现有模型平均高出 2.6%。

CLIP 模型学习的任务集比以前在从随机初始化端到端训练的单个计算机视觉模型中展示的要广泛。这些任务包括地理定位、光学字符识别、面部情绪识别和动作识别。这些任务都没有在 Kornblith （2019）等人的评估任务中测量 。这可以被认为是Kornbrith等人（2019）对与 ImageNet 重叠任务的研究中的一种选择偏见。为了解决这个问题，我们还测量了更广泛的 27 个数据集评估任务的性能。该评估任务在附录 A 中有详细说明，包括代表上述任务的数据集、德国交通标志识别基准（Stallkamp 等人，2011 年），以及改编自 VTAB 的其他几个数据集（Zhai 等人，2019 年）。在这个更广泛的评估任务中，CLIP 的优势更加明显。所有 CLIP 模型，无论规模如何，在计算效率方面都优于所有评估系统。与以前的系统相比，最佳模型的平均得分提高了 2.6% 至 5%。

Robustness to Natural Distribution Shift

2015 年，一种深度学习模型在 ImageNet 测试集上超过了人类的表现（He et al, 2015）。然而，在随后几年的研究中一再发现，这些模型仍然会犯许多简单的错误（Dodge &amp; Karam，2017；Geirhos 等，2018；Alcorn 等，2019），并且经常发现这些系统在新测试基准中的性能远低于人类精度和 ImageNet 性能（Recht 等人，2019；Barbu 等人，2019）。 Taori 等人 (2020) 最近的一项综合研究，旨在对 ImageNet 模型进行量化和理解 。 他们研究了 ImageNet 模型在评估自然分布变化时的性能变化情况。他们通过 7 个分配转移来衡量其性能，最终发现，分配转移的准确性可预见地随着 ImageNet 精度增加而增加，并且可以很好地建模为 logit 转换精度的线性函数。 利用这一发现，Taori 等人 (2020)提出鲁棒性分析应该区分有效鲁棒性和相对鲁棒性。有效鲁棒性衡量的是在分布偏移下的精度改进，其结果高于已记录的分布内和分布外精度之间的关系所预测的结果。相对鲁棒性反映了分布外准精度的任何改进。 他们认为，鲁棒性技术应旨在提高有效的鲁棒性和相对鲁棒性。

然而，几乎所有在Taori  (2020)等人研究的模型都是在ImageNet数据集上训练或微调的。训练或适应ImageNet数据集分布是观察到的鲁棒性差距的原因吗?直观地说，zero-shot 模型不应该能够利用仅适用于特定分布上存在的虚假相关性或模式，因为它没有针对该分布进行训练。因此，zero-shot模型可能具有更高的有效鲁棒性。
在图7中，我们比较了零射击CLIP与现有ImageNet模型在自然分布偏移情况下的性能。
所有的zero-shot CLIP模型都大幅提高了有效鲁棒性，并将ImageNet精度与分布偏移下精度之间的差距缩小了75%。这些结果表明，最近向大规模任务和数据集不可知的预训练的转变，结合向zero-shot 迁移评估的重新定向任务(如Yogatama和Linzen所主张的)，促进了更稳健系统的开发，并提供了对真实模型性能更准确的评估。

数据重叠分析

在非常大的互联网数据集上进行预训练的一个问题是与下游评估数据集的无意重叠问题。我们进行了重复数据删除分析，并对此在补充材料中提供了完整细节分析。在研究的 35 个数据集中，有 9 个数据集根本没有检测到重叠。重叠的中位数为 2.2%，平均重叠率为 3.2%。由于这种少量的重叠，在只有 7 个数据集高于此阈值的情况下，整体准确度的变化很少超过 0.1%。其中，只有 2 个在 Bonferroni 校正后具有统计学意义。在 Birdsnap 上检测到的最大改进仅为 0.6%。这与之前大规模预训练工作中类似重复分析的结果相呼应。马哈詹等人。 (2018) 和 Kolesnikov 等人。 (2019) 检测到他们模型的相似重叠率，并且还观察到了整体性能的微小变化。

影响

CLIP 允许人们设计自己的分类器，并不需要特定任务的训练数据，那么这些类的设计方式将会严重影响模型性能和模型偏差。例如，我们发现，当给定一组标签时，包括一些 Fairface 种族标签 (K̈ arkk̈ ainen &amp; Joo, 2019) 和少数不好的标签，如“criminal”和“animal”，该模型倾向于将 0 至 20 岁人的图像归类到不好的类别中，比例达32.3%。但是，当我们将类“child”添加到可能的类列表中时，这种行为会下降到 8.7%。我们还发现，归类为“criminal”和“non-human”类别的人在性别和种族方面存在差异，这凸显了即使是精心设计的类，也可能产生不同的影响。

此外，由于 CLIP 不需要特定于任务的训练数据，它可以更轻松地解锁某些特定的小众任务。其中一些任务可能会增加隐私或监控相关风险，我们通过使用 CelebA 数据集（Liu 等人，2018）测试 CLIP 在名人识别方面的表现来探索这些风险。CLIP 在 100 个候选选择中对 “in the wild”名人图像进行分类中准确率为 59.2%，在从 1000 个可能选择中准确率为 43.3%。尽管通过与任务无关的预训练能够实现这些样的结果，是令人惊讶的，但这种性能与广泛可用的生产级模型相比并不具有竞争力。我们在补充材料中探讨了对 CLIP 提出的挑战，并希望这项工作能够激发未来对此类模型的能力、缺点和偏差的表征的研究。

限制

Zero-shot CLIP 的性能通常仅与 ResNet-50 特征上的线性分类器的监督基线相媲美。该基线现在远低于整体 SOTA。仍然需要大量工作来提高 CLIP 的任务学习和迁移能力。我们估计，Zero-shot CLIP 需要大约 1000 倍的计算量才能在我们的评估任务中达到整体 SOTA 性能。使用当前的硬件进行训练是不可行的。有必要进一步研究提高 CLIP 的计算和数据效率。

尽管我们一直在强调零样本迁移，但我们却是通过反复观察验证集的性能以指导开发。这对于真正的零样本迁移是不现实的。在半监督学习领域也提出了类似的担忧（Oliver 等人，2018 年）。另一个潜在问题是我们对评估数据集的选择。虽然我们报告了 （Kornblith 2019）等人的结果。 的 12 个数据集评估套件作为一个标准化集合，我们的主要分析使用了 27 个数据集的一些随意的集合，这些数据集无疑与 CLIP 的功能相适应。旨在评估广泛的零样本传输能力的新任务基准将有助于解决这个问题。

虽然我们将Kornbrith等人（2019）的12个数据集评估任务的结果作为标准化集合进行报告，但我们的主要分析是使用的27个数据集的随机集合，不可否认，这些数据集与CLIP的功能共同适应。一个旨在评估广泛的零样本迁移能力的新任务基准，将有助于解决这一问题。


我们强调通过文本描述学习图像分类器是一个灵活方法架构，但这也有其自身的局限性。许多复杂的任务可能很难仅通过文本来指定。不可否认，实际的训练示例很有用，但 CLIP 并没有直接针对小样本性能进行优化。我们回退到在 CLIP 的特征之上拟合线性分类器。这会导致在从零样本过渡到少样本时，性能会出现反直觉的下降。

相关工作


从自然语言监督中学习执行计算机视觉任务的想法并不新鲜。相反，我们的主要贡献是大规模研究其行为。 20 多年前 Mori 等人。 (1999) 通过训练模型来预测与图像配对的文本中的名词和形容词，探索了改进基于内容的图像检索。夸托尼等人。 （2007 年）证明可以通过流形学习在训练用于预测图像说明中的单词的分类器的权重空间中学习更多数据有效的图像表征。 Srivastava &amp; Salakhutdinov (2012) 通过在低级图像和文本标签特征之上训练多模态深度玻尔兹曼机来探索深度表征学习。引言中描述了最近启发 CLIP 的工作。

Fergus 等人在网络监督学习中通常研究从互联网图像集合中学习。 (2005) 展示了通过将图像搜索引擎结果视为监督来训练有竞争力的计算机视觉分类器的能力。在这一系列工作中，Learn Everything about Anything: Webly-Supervised Visual Concept Learning (Divvala et al, 2014) 与 CLIP 有着明显相似的抱负和目标。

零样本计算机视觉的发展（Larochelle 等人，2008 年；Lampert 等人，2009 年）对于 CLIP 至关重要。索切尔等人。 （2013a）证明，连接图像和语言表征可以零样本迁移到 CIFAR10 和 Frome 等人的未见类。 （2013 年）改进并将这一发现扩展到 ImageNet。从自然语言生成分类器的想法至少可以追溯到 Elhoseiny 等人。 (2013) 和 Lei Ba 等人探索了一种类似于 CLIP 的零样本分类器的形式。 （2015 年）。

自然语言监督也被探索用于图像分类以外的任务，包括视频理解（Ramanathan 等人，2013；Miech 等人，2019）、强化学习（Hermann 等人，2017），以及最近的一系列学习工作视觉和语言的联合模型（Lu et al, 2019; Tan &amp; Bansal, 2019; Chen et al, 2019; Li et al, 2020b; Yu et al, 2020），用于复杂的联合任务，这些任务超出了这里研究的范围，包括视觉问答。

总结


我们研究了是否有可能将 NLP 中与任务无关的网络规模预训练的成功迁移到另一个领域。我们发现采用这个公式会导致计算机视觉领域出现类似的行为，并讨论这一研究方向的社会影响。为了优化他们的训练目标，CLIP 模型学习在预训练期间执行各种各样的任务。然后可以通过自然语言提示利用此任务学习，以实现对许多现有数据集的零样本迁移。在足够的规模下，这种方法的性能可以与特定任务的监督模型相媲美，尽管仍有很大的改进空间。


我们要感谢参与创建 CLIP 训练数据的数百万人。我们还要感谢 Susan Zhang 在 OpenAI 期间在图像条件语言模型方面所做的工作，感谢 Ishaan Gulrajani 发现伪代码中的错误，以及 Irene Solaiman、Miles Brundage 和 Gillian Hadfield 对更广泛影响部分的深思熟虑的反馈的论文。我们还感谢 OpenAI 的加速和超级计算团队在该项目使用的软件和硬件基础设施方面所做的关键工作。最后，我们还要感谢整个项目中使用的许多软件包的开发者，包括但不限于 Numpy (Harris et al, 2020)、SciPy (Virtanen et al, 2020)、ftfy (Speer , 2019)、TensorFlow (Abadi et al, 2016)、PyTorch (Paszke et al, 2019)、pandas (pandas development team, 2020) 和 scikit-learn (Pedregosa et al, 2011)。

### 引文

## 摘录
