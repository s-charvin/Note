---
title: "StarGAN: Unified Generative Adversarial Networks for Multi-domain Image-to-Image Translation"
description: ""
citekey: choiStarGANUnifiedGenerative2018
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:35:31
lastmod: 2023-04-11 13:03:48
---

> [!info] 论文信息
>1. Title：StarGAN: Unified Generative Adversarial Networks for Multi-domain Image-to-Image Translation
>2. Author：Yunjey Choi, Minje Choi, Munyoung Kim, Jung-Woo Ha, Sunghun Kim, Jaegul Choo
>3. Entry：[Zotero link](zotero://select/items/@choiStarGANUnifiedGenerative2018) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Choi et al_2018_StarGAN.pdf>)
>4. Other：2018 - 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 

## 摘要

> [!abstract] Recent studies have shown remarkable success in image-to-image translation for two domains. However, existing approaches have limited scalability and robustness in handling more than two domains, since different models should be built independently for every pair of image domains. To address this limitation, we propose StarGAN, a novel and scalable approach that can perform image-to-image translations for multiple domains using only a single model. Such a unified model architecture of StarGAN allows simultaneous training of multiple datasets with different domains within a single network. This leads to StarGAN's superior quality of translated images compared to existing models as well as the novel capability of flexibly translating an input image to any desired target domain. We empirically demonstrate the effectiveness of our approach on a facial attribute transfer and a facial expression synthesis tasks.

> 最近的研究表明，在两个领域的图像到图像转换方面取得了显着的成功。然而，现有方法在处理两个以上的域时具有有限的可扩展性和鲁棒性，因为应该为每对图像域独立构建不同的模型。为了解决这个限制，我们提出了 StarGAN，这是一种新颖且可扩展的方法，可以仅使用单个模型为多个域执行图像到图像的转换。 StarGAN 的这种统一模型架构允许在单个网络中同时训练具有不同域的多个数据集。与现有模型相比，这导致 StarGAN 具有卓越的翻译图像质量，以及将输入图像灵活翻译到任何所需目标域的新颖能力。我们凭经验证明了我们的方法在面部属性转移和面部表情合成任务上的有效性。

## 预处理

## 概述

## 结果

## 精读

图像到图像转换的任务是将给定图像的特定方面更改为另一个方面，例如，将人的面部表情从微笑变为皱眉（见图 1）。在引入生成对抗网络 (GAN) 后，这项任务经历了显着的改进，其结果包括改变头发颜色 [9]、从边缘图重建照片 [7] 以及改变风景图像的季节 [33]。给定来自两个不同域的训练数据，这些模型学习将图像从一个域转换到另一个域。我们将术语属性表示为图像中固有的有意义的特征，例如头发颜色、性别或年龄，将属性值表示为属性的特定值，例如，黑色/金色/棕色表示头发颜色或男性/女性表示性别。我们进一步将域表示为一组共享相同属性值的图像。例如，女性的图像可以代表一个领域，而男性的图像可以代表另一个领域。

几个图像数据集带有许多标记属性。 例如，CelebA[19] 数据集包含 40 个与头发颜色、性别和年龄等面部属性相关的标签，而 RaFD [13] 数据集包含 8 个面部表情标签，如“快乐”、“愤怒”和“ 伤心'。 这些设置使我们能够执行更有趣的任务，即多域图像到图像的转换，我们根据来自多个域的属性更改图像。 图 1 中的前五列显示了如何根据“金发”、“性别”、“老年”和“苍白皮肤”这四个域中的任何一个来翻译 CelebA 图像。 我们可以进一步扩展到训练来自不同数据集的多个域，例如联合训练 CelebA 和 RaFD 图像，以使用通过在 RaFD 上训练学习到的特征来改变 CelebA 图像的面部表情，如图 1 最右边的列。

然而，现有模型在此类多域图像翻译任务中既低效又无效。 它们的低效率是因为为了学习 k 个域之间的所有映射，必须训练 k(k-1) 个生成器。 图 2 (a) 说明了如何必须训练十二个不同的生成器网络才能在四个不同的域之间转换图像。 同时，即使存在可以从人脸形状等所有域的图像中学习到的全局特征，但每个生成器都不能充分利用整个训练数据，只能从 k 个域中的两个域中学习。 未能充分利用训练数据可能会限制生成图像的质量。 此外，它们无法联合训练来自不同数据集的域，因为每个数据集都被部分标记，我们将在 3.2 节中进一步讨论。

作为此类问题的解决方案，我们提出了 StarGAN，这是一种新颖且可扩展的方法，能够学习多个域之间的映射。 如图 2 (b) 所示，我们的模型接收多个域的训练数据，并仅使用单个生成器学习所有可用域之间的映射。 这个想法很简单。 我们的生成器不是学习固定的翻译（例如，黑色到金色的头发），而是将图像和域信息作为输入，并学习将图像灵活地翻译到相应的域。 我们使用标签（例如，二进制或单热向量）来表示域信息。 在训练过程中，我们随机生成一个目标域标签并训练模型灵活地将输入图像转换为目标域。 通过这样做，我们可以控制域标签并在测试阶段将图像转换为任何所需的域。

我们还介绍了一种简单但有效的方法，通过向域标签添加掩码向量，可以在不同数据集的域之间进行联合训练。 我们提出的方法确保模型可以忽略未知标签并专注于特定数据集提供的标签。 通过这种方式，我们的模型可以很好地执行任务，例如使用从 RaFD 学习的特征来合成 CelebA 图像的面部表情，如图 1 最右边的列所示。据我们所知，我们的工作是第一个 成功地跨不同数据集执行多域图像翻译。

总的来说，我们的贡献如下：

我们提出了 StarGAN，这是一种新颖的生成对抗网络，它只使用一个生成器和一个鉴别器来学习多个域之间的映射，从所有域的图像中进行有效训练。

我们展示了如何通过使用使 StarGAN 能够控制所有可用域标签的掩码向量方法成功地学习多个数据集之间的多域图像转换。

我们使用 StarGAN 提供了面部属性转移和面部表情合成任务的定性和定量结果，显示了其优于基线模型的优势。

相关工作

生成对抗网络。 生成对抗网络 (GAN) [3] 在图像生成 [6, 24, 32, 8]、图像翻译 [7, 9, 33]、超分辨率成像 [14]、 和人脸图像合成[10,16,26,31]。 典型的 GAN 模型由两个模块组成：鉴别器和生成器。 鉴别器学习区分真假样本，而生成器学习生成与真实样本无法区分的假样本。 我们的方法还利用对抗性损失使生成的图像尽可能逼真。

条件 GAN。 基于 GAN 的条件图像生成也得到了积极的研究。 先前的研究已经为鉴别器和生成器提供了类信息，以便生成以类为条件的样本[20,21,22]。 最近的其他方法侧重于生成与给定文本描述高度相关的特定图像 [25, 30]。 条件图像生成的思想也已成功应用于域迁移 [9, 28]、超分辨率成像 [14] 和照片编辑 [2, 27]。 在本文中，我们提出了一个可扩展的 GAN 框架，该框架可以通过提供条件域信息，灵活地将图像转换到各种目标域。

Image-to-Image Translation.

最近的工作在图像到图像的翻译方面取得了令人瞩目的成果 [7, 9, 17, 33]。例如，pix2pix [7] 使用 cGANs[20] 以监督方式学习此任务。它结合了对抗性损失和 L1 损失，因此需要成对的数据样本。为了缓解获取数据对的问题，已经提出了不成对的图像到图像转换框架[9,17,33]。 UNIT [17] 将变分自动编码器 (VAE) [12] 与 CoGAN [18] 相结合，这是一个 GAN 框架，其中两个生成器共享权重以学习跨域中图像的联合分布。 CycleGAN [33] 和 DiscoGAN [9] 通过利用循环一致性损失来保留输入和翻译图像之间的关键属性。然而，所有这些框架一次只能学习两个不同领域之间的关系。他们的方法在处理多个域时的可扩展性有限，因为应该为每对域训练不同的模型。与上述方法不同，我们的框架可以仅使用单个模型来学习多个域之间的关系。

Star Generative Adversarial Networks

我们首先描述了我们提出的 StarGAN，这是一个在单个数据集中解决多域图像到图像转换的框架。 然后，我们讨论 StarGAN 如何合并包含不同标签集的多个数据集，以使用这些标签中的任何一个灵活地执行图像翻译。

我们的目标是训练一个生成器 G 来学习多个域之间的映射。 为了实现这一点，我们训练 G 将输入图像 x 转换为以目标域标签 c 为条件的输出图像 y，G(x, c) → y。 我们随机生成目标域标签 c，以便 G 学习灵活地翻译输入图像。 我们还引入了一个辅助分类器[22]，它允许单个鉴别器控制多个域。 也就是说，我们的鉴别器在源和域标签上产生概率分布，D : x → {Dsrc(x), Dcls(x)}。 图 3 说明了我们提出的方法的训练过程。

Adversarial Loss

为了使生成的图像与真实图像无法区分，我们采用了对抗性损失

其中 G 以输入图像 x 和目标域标签 c 为条件生成图像 G(x, c)，而 D 试图区分真实图像和假图像。 在本文中，我们将术语 Dsrc(x) 称为 D 给定的源上的概率分布。生成器 G 试图最小化这个目标，而鉴别器 D 试图最大化它。

Domain Classification Loss.

对于给定的输入图像 x 和目标域标签 c，我们的目标是将 x 转换为输出图像 y，将其正确分类到目标域 c。 为了达到这个条件，我们在 D 之上添加了一个辅助分类器，并在优化 D 和 G 时施加域分类损失。也就是说，我们将目标分解为两个项：用于优化 D 的真实图像的域分类损失， 以及用于优化 G 的假图像的域分类损失。详细地说，前者定义为

其中术语 Dcls(c 0 |x) 表示由 D 计算的域标签上的概率分布。通过最小化这个目标，D 学习将真实图像 x 分类到其对应的原始域 c 0 。 我们假设输入图像和域标签对 (x, c0 ) 由训练数据给出。 另一方面，假图像域分类的损失函数定义为

换句话说，G 试图最小化这个目标以生成可以分类为目标域 c 的图像

Reconstruction Loss

通过最小化对抗性和分类损失，G 被训练以生成逼真的图像并分类到其正确的目标域。 然而，最小化损失（方程（1）和（3））并不能保证翻译后的图像在只改变输入的域相关部分的同时保留其输入图像的内容。 为了缓解这个问题，我们将循环一致性损失 [9, 33] 应用于生成器，定义为

其中 G 将翻译后的图像 G(x, c) 和原始域标签 c 0 作为输入，并尝试重建原始图像 x。 我们采用 L1 范数作为我们的重建损失。 请注意，我们使用单个生成器两次，首先将原始图像转换为目标域中的图像，然后从转换后的图像重建原始图像。

Full Objective

最后，优化 G 和 D 的目标函数分别写为

其中 λcls 和 λrec 是超参数，与对抗性损失相比，它们分别控制域分类和重建损失的相对重要性。 我们在所有实验中使用 λcls = 1 和 λrec = 10。

Training with Multiple Datasets

StarGAN 的一个重要优势是它同时合并了多个包含不同类型标签的数据集，因此 StarGAN 可以在测试阶段控制所有标签。 然而，从多个数据集学习时的一个问题是每个数据集只知道部分标签信息。 在 CelebA [19] 和 RaFD [13] 的情况下，虽然前者包含诸如头发颜色和性别等属性的标签，但它没有任何诸如“快乐”和“愤怒”等面部表情的标签，反之亦然 对于后者。 这是有问题的，因为当从转换后的图像 G(x, c) 重建输入图像 x 时，需要关于标签向量 c 0 的完整信息（参见方程（4））。

Mask Vector

为了缓解这个问题，我们引入了一个掩码向量 m，它允许 StarGAN 忽略未指定的标签并专注于特定数据集提供的明确已知的标签。 在 StarGAN 中，我们使用 n 维 one-hot 向量来表示 m，其中 n 是数据集的数量。 另外，我们将标签的统一版本定义为向量

其中 [·] 表示连接，ci 表示第 i 个数据集标签的向量。 已知标签 ci 的向量可以表示为二进制属性的二进制向量或分类属性的 one-hot 向量。 对于剩余的 n-1 个未知标签，我们只需分配零值。 在我们的实验中，我们使用了 CelebA 和 RaFD 数据集，其中 n 为 2。

培训策略。

在使用多个数据集训练 StarGAN 时，我们使用等式中定义的域标签 c~。 (7) 作为生成器的输入。通过这样做，生成器学会忽略未指定的标签，它们是零向量，并专注于明确给定的标签。生成器的结构与使用单个数据集的训练完全相同，除了输入标签 c~ 的维度。另一方面，我们扩展了鉴别器的辅助分类器，以生成所有数据集标签上的概率分布。然后，我们在多任务学习设置中训练模型，其中判别器尝试仅最小化与已知标签相关的分类错误。例如，在 CelebA 中使用图像进行训练时，鉴别器仅最小化与 CelebA 属性相关的标签的分类错误，而不是与 RaFD 相关的面部表情。在这些设置下，通过在 CelebA 和 RaFD 之间交替，鉴别器学习两个数据集的所有鉴别特征，生成器学习控制两个数据集中的所有标签。

Improved GAN Training.

为了稳定训练过程并生成更高质量的图像，我们替换了 Eq。 (1) 使用带有梯度惩罚的 Wasserstein GAN 目标 [1, 4] 定义为

其中 x^ 沿一对真实图像和生成图像之间的直线均匀采样。 我们对所有实验使用 λgp = 10。

StarGAN 改编自 CycleGAN [33]，其生成网络由两个用于下采样的步长为 2 的卷积层、六个残差块 [5] 和两个用于上采样的步长为 2 的转置卷积层组成。我们对生成器使用实例归一化[29]，但对鉴别器没有归一化。我们将 PatchGANs [7, 15, 33] 用于鉴别器网络，该网络对本地图像补丁是真实的还是虚假的进行分类。有关网络架构的更多详细信息，请参见附录（第 7.2 节）。

### 引文

## 摘录
