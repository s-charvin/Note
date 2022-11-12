---
title: "Temporal Segment Networks: Towards Good Practices for Deep Action Recognition"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: "笔记"
draft: true
layout: 
data: 2022-08-26 22:01:02
lastmod: 2022-11-12 14:13:37
---

# 重点

- [开源代码](https://github.com/yjxiong/tsn-pytorch)

# 摘要

Deep convolutional networks have achieved great success for visual recognition in still images. However, for action recognition in videos, the advantage over traditional methods is not so evident. This paper aims to discover the principles to design effective ConvNet architectures for action recognition in videos and learn these models given limited training samples. Our first contribution is temporal segment network (TSN), a novel framework for video-based action recognition. which is based on the idea of long-range temporal structure modeling. It combines a sparse temporal sampling strategy and video-level supervision to enable efficient and effective learning using the whole action video. The other contribution is our study on a series of good practices in learning ConvNets on video data with the help of temporal segment network. Our approach obtains the state-the-of-art performance on the datasets of HMDB51 (69.4%) and UCF101 (94.2%). We also visualize the learned ConvNet models, which qualitatively demonstrates the effectiveness of temporal segment network and the proposed good practices. 1

深度卷积网络在静止图像的视觉识别领域取得了巨大成功。然而，对于视频中的动作识别，这些传统方法的优势并不明显。本文旨在研究(discover the principles)如何为视频动作识别设计高效的 ConvNet 架构，并在有限的训练样本下学习这些模型。我们的第一个贡献是 temporal segment network（TSN），一种基于长时间结构建模(long-range temporal structure modeling)的思想, 用于视频动作识别的新框架。它结合了稀疏时间采样(sparse temporal sampling)策略和视频层级监督，以实现使用整个动作视频的高效学习。另一个贡献是我们在 TSN 网络的帮助下, 对视频数据上学习 ConvNets 的一系列优秀的实践研究。我们的方法在 HMDB51（69.4%）和 UCF101（94.2%）的数据集上获得了最先进的性能。同时, 我们还将学习到的 ConvNet 模型进行了可视化，定性地证明了 TSN 网络的有效性和实践结果。

# 结果

# 词汇记录

# 精读

Video-based action recognition has drawn a significant amount of attention from the academic community [1,2,3,4,5,6], owing to its applications in many areas like security and behavior analysis. In action recognition, there are two crucial and complementary aspects: appearances and dynamics. The performance of a recognition system depends, to a large extent, on whether it is able to extract and utilize relevant information therefrom. However, extracting such information is non-trivial due to a number of complexities, such as scale variations, view point changes, and camera motions. Thus it becomes crucial to design effective representations that can deal with these challenges while preserve categorical information of action classes. Recently, Convolutional Networks (ConvNets) [7] have witnessed great success in classifying images of objects, scenes, and complex events [8,9,10,11]. ConvNets have also been introduced to solve the problem of video-based action recognition [12,1,13,14]. Deep ConvNets come with great modeling capacity and are capable of learning discriminative representation from raw visual data with the help of large-scale supervised datasets. However, unlike image classification, end-to-end deep ConvNets remain unable to achieve significant advantage over traditional hand-crafted features for video-based action recognition. 
基于视频的动作识别由于其在安全和行为分析等许多领域的应用，已经引起了学术界的大量关注[1,2,3,4,5,6]。
在动作识别中，有两个至关重要且相辅相成的方面: 外观和动态。
识别系统的性能在很大程度上取决于它是否能够从中提取和利用相关信息。
然而，提取这样的信息并非易事，因为有许多复杂性，如缩放变化，视点变化和相机运动。
因此，在保留动作类的分类信息的同时，设计能够处理这些挑战的有效表示就变得至关重要。
最近，卷积网络(ConvNets)[7]在对物体、场景和复杂事件的图像进行分类方面取得了巨大成功[8,9,10,11]。
ConvNets 也被引入来解决基于视频的动作识别问题[12,1,13,14]。
深度卷积网络具有强大的建模能力，能够在大规模监督数据集的帮助下从原始视觉数据学习判别表示。
然而，与图像分类不同的是，端到端深度卷积网络在基于视频的动作识别方面仍无法取得传统手工特征的显著优势。
In our view, the application of ConvNets in video-based action recognition is impeded by two major obstacles. First, long-range temporal structure plays an important role in understanding the dynamics in action videos [15,16,17,18]. However, mainstream ConvNet frameworks [1,13] usually focus on appearances and short-term motions, thus lacking the capacity to incorporate long-range temporal structure. Recently there are a few attempts [19,4,20] to deal with this problem. These methods mostly rely on dense temporal sampling with a pre-defined sampling interval. This approach would incur excessive computational cost when applied to long video sequences, which limits its application in real-world practice and poses a risk of missing important information for videos longer than the maximal sequence length. Second, in practice, training deep ConvNets requires a large volume of training samples to achieve optimal performance. However, due to the difficulty in data collection and annotation, publicly available action recognition datasets (e.g. UCF101 [21], HMDB51 [22]) remain limited, in both size and diversity. Consequently, very deep ConvNets [9,23], which have attained remarkable success in image classification, are confronted with high risk of over-fitting. 
在我们看来，ConvNets 在基于视频的动作识别中的应用受到两个主要障碍的阻碍。
首先，长程时间结构在理解动作视频中的动态方面起着重要作用[15,16,17,18]。
然而，主流的 ConvNet 框架[1,13]通常关注外观和短期运动，因此缺乏整合长期时间结构的能力。
最近有一些尝试[19,4,20]来处理这个问题。
这些方法大多依赖于具有预先定义的采样间隔的密集时间采样。
当应用于较长的视频序列时，该方法会产生过多的计算成本，这限制了其在现实实践中的应用，并对超过最大序列长度的视频存在丢失重要信息的风险。
第二，在实践中，训练深度 ConvNets 需要大量的训练样本来达到最佳性能。
然而，由于数据收集和注释的困难，公开的动作识别数据集(如 UCF101 [21]， HMDB51[22])在规模和多样性方面仍然有限。
因此，非常深的 ConvNets[9,23]在图像分类中取得了显著的成功，但却面临着很高的过拟合风险。
These challenges motivate us to study two problems: 1) how to design an effective and efficient video-level framework for learning video representation that is able to capture long-range temporal structure; 2) how to learn the ConvNet models given limited training samples. In particular, we build our method on top of the successful two-stream architecture [1] while tackling the problems mentioned above. In terms of temporal structure modeling, a key observation is that consecutive frames are highly redundant. Therefore, dense temporal sampling, which usually results in highly similar sampled frames, is unnecessary. Instead a sparse temporal sampling strategy will be more favorable in this case. Motivated by this observation, we develop a video-level framework, called temporal segment network (TSN). This framework extracts short snippets over a long video sequence with a sparse sampling scheme, where the samples distribute uniformly along the temporal dimension. Thereon, a segmental structure is employed to aggregate information from the sampled snippets. In this sense, temporal segment networks are capable of modeling long-range temporal structure over the whole video. Moreover, this sparse sampling strategy preserves relevant information with dramatically lower cost, thus enabling end-to-end learning over long video sequences under a reasonable budget in both time and computing resources. 
这些挑战促使我们研究两个问题:1)如何设计一个有效且高效的视频级框架来学习视频表示，并能够捕捉到远程时间结构;
2)在有限训练样本下如何学习 ConvNet 模型。
特别是，我们在成功的双流体系结构[1]的基础上构建了我们的方法，同时解决了上面提到的问题。
在时间结构建模方面，一个关键的观察是连续帧是高度冗余的。
因此，没有必要进行密集时间采样，这通常会导致高度相似的采样帧。
相反，在这种情况下，稀疏时间采样策略将更有利。
基于这种观察，我们开发了一个视频级别的框架，称为时间段网络(TSN)。
该框架使用稀疏采样方案从长视频序列中提取短片段，样本沿时间维均匀分布。
在此基础上，采用分段结构从采样片段中聚合信息。
从这个意义上说，时间段网络能够模拟整个视频的长时间结构。
此外，这种稀疏采样策略以极低的成本保存相关信息，从而在合理的时间和计算资源预算下实现长视频序列的端到端学习。
To unleash the full potential of temporal segment network framework, we adopt very deep ConvNet architectures [23,9] introduced recently, and explored a number of good practices to overcome the aforementioned difficulties caused by the limited number of training samples, including 1) cross-modality pre-training; 2) regularization; 3) enhanced data augmentation. Meanwhile, to fully utilize visual content from videos, we empirically study four types of input modalities to two-stream ConvNets, namely a single RGB image, stacked RGB difference, stacked optical flow field, and stacked warped optical flow field. 
为了充分释放时间段网络框架的潜力，我们采用了最近引入的非常深入的 ConvNet 架构[23,9]，并探索了许多好的实践来克服上述训练样本数量有限所带来的困难，包括 1)跨模态预训练;
2)正则化;
3)增强数据增强。
同时，为了充分利用视频中的视觉内容，我们实证研究了单 RGB 图像、叠加 RGB 差分、叠加光流场和叠加扭曲光流场四种双流 ConvNets 的输入模式。
We perform experiments on two challenging action recognition datasets, namely UCF101 [21] and HMDB51 [22], to verify the effectiveness of our method. In experiments, models learned using the temporal segment network significantly outperform the state of the art on these two challenging action recognition datasets. We also visualize the our learned two-stream models trying to provide some insights for future action recognition research.
我们在 UCF101[21]和 HMDB51[22]两个具有挑战性的动作识别数据集上进行了实验，以验证我们方法的有效性。
在实验中，使用时间段网络学习的模型在这两个具有挑战性的动作识别数据集上的表现明显优于现有的技术水平。
我们还将我们所学习的两流模型进行了可视化，试图为未来的动作识别研究提供一些见解。
## 引文
