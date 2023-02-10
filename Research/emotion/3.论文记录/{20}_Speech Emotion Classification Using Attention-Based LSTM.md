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
data: 2022-04-29 14:51:45
lastmod: 2022-05-03 14:22:48
---

# 重点

- 提出了一种基于注意力的长短期记忆(LSTM)递归神经网络的帧级语音特征的语音识别方法
	- 修改传统 LSTM 的遗忘门来降低计算复杂度
	- 使用注意力机制, 分别提取时间和特征方面的关联特征信息，在特征层面上，区分时间维度中的情感差异以及特征维度中的情感表征能力

# 摘要

Automatic speech emotion recognition **has been a research hotspot in the field** of human–computer interaction **over the past decade.** However, due to the lack of research on the inherent temporal relationship of the speech waveform, the current recognition accuracy needs improvement. To make full use of the difference of emotional saturation between time frames, a novel method is proposed for speech recognition using frame-level speech features combined with attention-based long short-term memory (LSTM) recurrent neural networks. Frame-level speech features were extracted from waveform to replace traditional statistical features, which could preserve the timing relations in the original speech through the sequence of frames. To distinguish emotional saturation in different frames, two improvement strategies are proposed for LSTM based on the attention mechanism: first, the algorithm reduces the computational complexity by modifying the forgetting gate of traditional LSTM without sacrificing performance and second, in the final output of the LSTM, an attention mechanism is applied to both the time and the feature dimension to obtain the information related to the task, rather than using the output from the last iteration of the traditional algorithm. Extensive experiments on the CASIA, eNTERFACE, and GEMEP emotion corpora demonstrate that the performance of the proposed approach is able to outperform the state-of-the-art algorithms reported to date.

语音情感自动识别是近十年来人机交互领域的研究热点。然而，由于缺乏对语音波形内在时间关系(the inherent temporal relationship)的研究，目前的识别准确率还有待提高。为了充分利用时间帧之间情感饱和度的差异，提出了一种结合基于注意力的长短期记忆(LSTM)递归神经网络的帧级语音特征的语音识别方法。从波形中提取帧级语音特征来代替传统的统计特征，通过帧序列来保留原始语音中的时间关系。为了区分不同帧中的情感饱和，提出了两种基于注意力机制的LSTM改进策略：第一，在不牺牲性能的情况下，通过修改传统LSTM的遗忘门来降低计算复杂度；第二，在LSTM的最终输出中，将注意力机制应用到时间和特征维度上，以获取与任务相关的信息，而不是使用传统算法最后一次迭代的输出。在CASIA、eNTERFACE和 GEMEP 情感语料库上的大量实验表明，所提出的方法的性能能够超过迄今报道的最先进的算法。

# 结果

# 词汇记录

# 精读

情感识别在人机交互中具有重要的实用价值[1]-[4]，并具有广泛的应用前景。为了实现基于语音的情感分类，人们在机器学习算法上投入了大量的研究工作，如支持向量机[5]-[7]、贝叶斯分类器[8]、[9]和 K 最近邻分类法[10]、[11]。近年来，深度学习也被广泛应用于自动语音情感识别。但大多数传统的机器学习算法和深度学习网络(如自动编码器和卷积神经网络)都只能接受固定维度的数据作为输入，这对于具有可变语音长度的发音级情感识别来说似乎是矛盾的。为了解决这个问题，首先，最流行的方法[15]-[18]从短时语音帧中提取与情感相关的特征(本文称为帧级特征)，然后将静态统计函数(例如，均值、方差、最大值或线性回归系数)应用于帧级特征，并将结果拼接成固定维度的向量来表示完整的语音波形。虽然这些固定维度的特征满足了模型输入的要求，但经过统计分析处理的语音特征丢失了原始语音中的时间信息。解决这一矛盾的另一种方法是设计一种可以接受可变长度特征的模型。

近年来，为了增强LSTM在特定任务中处理数据的能力，人们对LSTM的内部结构提出了许多改进建议。Schmidhuber[19]提出了一种通过使用历史细胞状态作为输入信息的窥视孔连接，以增强学习历史信息的能力。
姚[20]通过引入深度门来连接各层之间的存储单元，从而控制存储单元之间的数据流。

此外，在许多LSTM应用[14]、[21]-[23]中，LSTM最后一次的输出通常被选为下一个模型的输入(因为其他模型只能接受固定尺寸的输入)。然而，在语音情感识别任务中，语音在最后大多是无声的，几乎没有任何情感信息。因此，情绪信息会在最后一刻被削弱。如何在任何时刻(而不是在最后一刻)有效地使用LSTM输出是提高语音情感识别性能的关键。针对上述问题，提出了一种改进的LSTM模型用于语音情感识别任务。首先，该模型使用帧级别的语音特征作为输入。特征的维度随着实际语音长度的变化而变化，而原始语音中的时间信息被帧之间的序列保留。因此，它更适合于具有处理可变长度序列的能力的LSTM的输入。其次，为了使LSTM的存储单元能够有效地利用历史状态中的关键信息，提出了一种替代传统LSTM中遗忘门的关注门。这一改进不仅降低了LSTM的计算复杂度，而且优化了情感识别性能。此外，语音的不同时间段的情感饱和度不同(沉默的片段包含的情感信息较少)，各种语音特征区分情感的能力也不同[24]。因此，利用权重系数区分差异是可行的，可以充分利用情感信息，提高情感识别性能。因此，针对语音情感识别的特殊性，本文提出了一种基于注意力机制的LSTM输出加权方法，并成功应用于图像处理领域[25]-[27]。该加权操作不仅作用于时间维度，还作用于特征维度。最后，在CASIA、eNTERFACE和GEMEP语料库上验证了该模型的性能。

从理论上讲，LSTM网络的最后时刻应该获得较大的权重。因此，本研究以上一次的输出为参照，通过使用注意机制来确保其能够获得较大的权重。此外，考虑到语音特征之间区分能力的差异，还将注意力机制应用于LSTM输出的特征维度。本文研究侧重于细胞内部的计算，并使用自我注意算法对LSTM的遗忘门进行了改进[43]。因此，遗忘门的计算不同于以前的LSTM。由于自我注意算法仅与历史单元状态本身相关，而与当前输入和历史隐藏无关。

基于OpenSMILE ComParE的帧级别的语音特征(即没有统计函数的特征)。直接用于情感分类，如下表所示。基本原因是：(1)统计函数的定长特征计算丢失了原始语音中的大量信息，如时间信息。(2)Hinton[45]认为深度学习具有自动学习特征变化的能力，可以从潜在的语音特征中学习与任务相关的深层特征。因此，帧级别特征看起来更适合作为在此建议的深度学习网络的输入。

| Features | Description |
| :--- | :--- |
| voiceProb | Voicing probability（发音概率） |
| HNR | Log harmonics-to-noise ratio（对数谐波均方根能量(Harmonic ERMS)与声门噪声均方根能量(NoiseERMS)之比） |
| F0 | Pitch frequency（基音频率） |
| F0raw | Raw F0 candidate without threshold in unvoiced segments（在无声段中无阈值的原生F0）|
| F0env | F0 envelope（F0 包络） |
| jitterLocal | The Average Absolute Difference between consecutive periods(连续周期之间的平均绝对差值) |
| jitterDDP | The Average Absolute Difference between consecutive differences between consecutive periods(连续周期间连续差的平均绝对差值) |
| shimmerLocal | The Average Absolute Difference between the interpolated peak amplitudes of consecutive periods(连续周期内插峰值幅度的平均绝对差) |
| harmonicERMS | Harmonic component RMS[Root Mean Square] energy（谐波分量均方根能量） |
| noiseERMS | Noise component RMS[Root Mean Square] energy（噪声分量均方根能量） |
| pcm_loudness_sma | Loudness（响度） |
| pcm_loudness_sma_de | Delta regression of loudness（响度的前向差分回归） |
| mfcc_sma[0]-[14] | Mel-Frequency Cepstral Coefficients（梅尔倒谱系数） |
| mfcc_sma_de[0]-[14] | Delta regression of mfcc（梅尔倒谱系数的前向差分回归） |
| pcm_Mag[0]-[25] | Mel Spectral（MEL 谱） |
| logMelFreqBand[0]-[7] | log Mel frequency bands（对数MEL频带） |
| lpcCoeff[0]-[7] | Linear predictive coding coefficients（线性预测编码系数） |
| lspFreq[0]-[7] | Line spectral pair frequency（线谱对频率） |
| pcm_zcr | Zero-crossing rate（过零率） |

谐波与噪声比(HNR)：：

$$
\mathrm{HNR}=10 \log _{10}\left\{\sum_{n=1}^{N} g^{2}(n) / \sum_{n=1}^{N} n^{2}(n)\right\}
$$

然而，HNR模糊了不同情绪类别之间的差异，因为在比例上存在分歧。相反，谐音ERMS和噪声ERMS特征可以保留情感类别之间的差异。同时，分别提取声门谐波能量（glottal harmonic energy）和声门噪声能量（glottal noise energy）作为反映声门关闭状态的情感特征。

为了可视化这三种特征对分类的影响，从CASIA[47]、eNTERFACE[48]和GEMEP语料库[49]中获取了一些样本(X轴)，然后计算这些样本的三个特征在一段时间内的平均值。如下图所示，在eNTERFACE语料库上，情绪之间的区别在谐波ERMS和噪声ERMS等值线上明显，而在HNR(谐波ERMS和噪声ERMS的比率)等值线中由于除法运算而严重降低。同样，在CASIA语料库上，HNR维度上的情绪差异小于和谐ERMS和NoiseERMS维度上的差异。此外，愤怒情绪在这些语料库上处于较高水平(这也是上述语料库的共性)，因此相对更容易与其他情绪区分开来。在CASIA语料库上，中性情绪在三个特征轮廓中处于最低水平，因此也相对容易区分。在eNTERFACE语料库上，处于最低水平的悲伤情绪在理论上具有较强的区分性，而厌恶、恐惧和惊讶情绪相互重叠，可能很难区分。在GEMEP语料库上，所有情感的轮廓相互重叠，其中一个可能的原因是一些情感描述带有非语义的短文本AAA。因此，GEMEP的情感区分度低于其他两个语料库，这表明在GEMEP上的平均识别率最低。总而言之，不同的特征在不同的数据库中具有不同的区分情绪的能力。

![]({20}_Speech%20Emotion%20Classification%20Using%20Attention-Based%20LSTM.assets/image-20220429171451.png)

注意机制首次应用于图像处理领域[25]-[27]，取得了很好的效果。其核心思想是，人脑对整个画面的关注是不平衡的，并存在一定的权重区分。受这一现象的启发，本文将自我注意机制引入到LSTM的遗忘门计算中，在保证模型性能的前提下减少了模型运算量。同时，情感识别中使用的帧级语音特征不仅包括时间信息，还包括特征级信息。这些不同的特征可能对最终分类性能具有不同程度的影响。为此，还将特征级别信息乘以关注度加权系数，以提高模型的最终性能。

LSTM信元的遗忘门用于确定在前一时刻的信元状态中应该丢弃哪些信息，并直接参与更新信元状态。

整体网络架构如下图所示

![]({20}_Speech%20Emotion%20Classification%20Using%20Attention-Based%20LSTM.assets/image-20220429175757.png)

为了展示所建议方法的性能，我们选择了三个不同的流行数据库来避免基于单一语料库评估的观察。实验使用了CASIA[47]、eNTERFACE[48]和GEMEP语料库[49]。

CASIA是中科院自动化所引进的情感语料库，包含6类情感(即愤怒、恐惧、高兴、中性、悲伤和惊讶)。语料库包含来自4名说话人(2名男性和2名女性)的7200个语音样本，其中随机选择1000个样本作为测试集。

eNTERFACE是一个英语音频和视频情感语料库，记录了来自14个国家的43名说话者，并根据以下6种情绪对样本进行分类：愤怒、厌恶、恐惧、高兴、悲伤和惊讶。

在这项工作中只使用了来自该语料库的音频数据。获得了1260个有效语音样本用于情感识别研究，其中260个样本作为测试集。GEMEP是一个法语内容语料库，拥有18个语音情感类别和1260个话语样本。在我们的实验中，我们选择了12种情绪(娱乐(Amu)、焦虑(Inq)、绝望(Des)、愤怒(Coll)、喜悦(Joi)、恐慌恐惧(Peu)、兴趣(Int)、激怒(Irr)、快乐(Pla)、骄傲(Fie)、解脱(Sou)、悲伤(Tri)；注：缩写来自法语)，如[8]、[52]。这是属于所选类别的10个说话人的1080个样本，其中随机选择200个样本作为测试集。根据作者目前的知识，基于语音的识别准确率在CASIA[53]、[54]上低于90%，在eNTERFACE[8]、[44]上低于80%，在GEMEP[8]、[55]上低于50%。提出的模型包括基于时间维度注意力加权的LSTM模型(LSTM-T)、基于特征维度注意力加权的LSTM(LSTMF)、基于改进注意力机制遗忘门的LSTM-AT(LSTM-AT)、基于时间和特征维度注意力加权的LSTM(LSTM-TF)及其改进的遗忘门LSTM-AT(LSTM-TF-AT)，相关参数的设置如表II所示。输入的维度为[128，TimeStep，93]，其中128是批次大小，TimeStep是帧的数量，93是从语音中提取的特征的数量。为了比较时间复杂度，这些参数在所有没有筛选的语料库上都是相同的。只有学习率根据训练集上收敛的稳定性进行调整。CASIA的初始学习率为0.0001，eNTERFACE和GEMEP的初始学习率均为0.001。输出的维度由语料库中情绪的数量决定(CASIA和ENTERFACE有6个类别，而GEMEP有12个类别)。由于对LSTM的输出矩阵执行两次注意力加权运算，并且结果以[outputT，outputF]的形式连接作为后续全连接层的输入，因此全连接层的信元数加倍。表II中的全连接层参数[256,128]对应于基于传统LSTM的网络，而[512,128]是基于时间和特征维度的注意力机制的LSTM网络的参数设置。其他参数保持不变，以保证实验结果的有效性。

为了验证基于注意力机制的改进型遗忘门在保证系统性能的前提下能够有效地减少训练时间，本文对两组实验进行了对比实验。一个实验是在LSTM-AT和传统的LSTM模型之间，另一个实验是在LSTM-TF模型和LSTM-TF-AT之间。如图5所示，它描述了在相应语料库上相同训练步骤下的训练时间。这四个模型分别在CASIA、ENTERFACE和GEMEP上训练，CASIA为1200个历元，ENTERFACE为1000个历元，GEMEP为1500个历元。换句话说，这些模型在相同的数据库上执行相同的迭代。从图中可以看出，相同训练步数的每个模型的训练时间是不同的。与未修改的LSTM模型相比，基于关注门的LSTM模型的时间开销更小。比较这些语料库的训练时间，CASIA需要更多的时间，LSTM-AT与LSTM(3.5h)、LSTM-Tf-At与LSTM-Tf(1h)的训练时间差异大于eNTERFACE(0.8h和0.9h)和GEMEP(0.7h)。这表明训练时间越长，基于注意门的LSTM的优势越显著。在计算复杂性方面，GRU的训练时间少于提出的基于注意力的遗忘门(Lstmat)，如图5所示。然而，LSTM-AT在拥有比eNTERFACE和GEMEP更多样本的CASIA语料库上取得了比GRU更好的性能。虽然GRU具有较低的计算复杂度，但在大数据集上表现不佳。布里茨[56]推翻了类似的结论。在他的工作中，LSTM细胞的表现一直好于GRU细胞。因此，LSTM-AT在不牺牲性能的情况下降低了计算复杂度。在更新细胞状态方面，陶[40]将注意力机制应用于LSTM的细胞状态更新，关注细胞之间的信息。但本研究关注的是细胞内部，并对LSTM的遗忘门进行了改造。因此，遗忘门的计算不同于以前的LSTM和[40]中的计算。在所有提到的语料库上，LSTM-AT的性能与TAO相似。然而，后者需要更多的时间来训练，因为需要计算更多的先前的小区状态，如图5所示。在本研究中，LSTM-AT侧重于小区状态的内部计算，并综合考虑了计算复杂度和性能。为了定量分析基于关注门的LSTM模型的识别性能，分析了每个模型的最佳识别性能，如表三、表四和表五所示。基于关注门的LSTM减少了模型内部的矩阵运算，并且不会对所有数据库的UAR产生负面影响，事实上，有时甚至可以观察到性能的提高。与传统LSTM相比，LSTM-AT在CASIA、eNTERFACE和GEMEP语料库上的UAR分别提高了约0.6%、5.7%和2.5%，在CASIA、eNTERFACE和GEMEP语料库上的UAR分别提高了约0.8%、2.7%和3%。综上所述，LSTM-TF-at通过在时间和特征维度中引入注意机制，增强了与情绪相关的信息，显著提高了UAR，如表VI所示，该表描述了LSTM和改进后的P值之间的左尾T检验。然而，在CASIA语料库上，由于基线较高，0.052的P值对LSTM-AT的改善并不显著。此外，设计了基于注意力机制的遗忘门，在保证性能的前提下，降低了模型的计算复杂度，加快了模型的收敛速度，缩短了训练时间。将LSTM-Tf和LSTM-At结合起来，由于LSTM-Tf-At得到的P值较小，其意义更加明显。因此，该模型在情感分类中具有明显的优势。

由于本文使用的特征集是在OpenSMILE比较特征集[16]的基础上进行修改的，所以还对原始特征集和修改后的两个特征集进行了比较。然而，由于函数应用于LLD后的最终OpenSMILE比较特征集是一维特征向量，内部数据不具有时序关系，不适合作为提出的用于分类情感识别的LSTM模型的输入。因此，将OpenSMILE比较函数特征集与传统的机器学习算法支持向量机相结合，作为比较基线。结果见表七、表八和表九，分别对应于CASIA、eNTERFACE和GEMEP数据库。如表所示，该方法在CASIA、eNTERFACE和GEMEP上的UAR分别提高了5.4%、33.8%和17.0%。尤其是在CASIA和eNTERFACE上，每类情绪的回忆次数都有所增加，这表明了LSTM-TF-AT具有框架级特征的优势。

本文提出了一种改进的基于注意力的LSTM情感分类方法。在遗忘门和LSTM的输出中都引入了注意机制。改进后的门只与历史单元状态有关，与当前输入无关，降低了计算复杂度。实验表明，新的关注门也能提高识别率。此外，由于LSTM-TFat模型考虑了不同时间段的情感饱和度，并将注意力机制应用到LSTM输出的时间和特征维中，使得LSTM-TFat模型具有更好的性能，特别是在大数据集上。在小数据集上，LSTM-TF-AT和Mirsamadi的模型具有相似的UAR，但后者在算法复杂度上具有优势。此外，与经典的支持向量机分类器相比，在CASIA和eNTERFACE语料库上，LSTM-TF-AT对每类情感的召回率都有所提高。下一步的工作包括以下几个方面。首先，虽然该方法在分类任务上是有效的，但它对连续情感的分类有很大的意义。因此，有必要研究改进的LSTM用于连续情感识别。其次，该算法考虑了不同特征对情感的区分能力。因此，在我们未来的研究中，它将被用于特征过滤。此外，随着我们的研究，这种基于注意力的LSTM有望在更多的应用中进行。

## 引文

- 邓[12]使用了带有自动编码器的半监督学习和少量的情感标签数据来进行SER。
- Neumann[13]和Wöllmer[14]分别将卷积神经网络和LSTM应用于SER。Wöllmer[14]首次将LSTM应用于连续情感识别，为每句话提取了4843个特征作为LSTM的输入。在他的进一步工作[15]中，静态特征被用作双向LSTM(BLSTM)的输入，以预测口语的情感表达。
- Schmidhuber[19]针对递归神经网络(RNN)提出了长短期记忆(LSTM)结构。该方法为处理诸如语音的可变长度的时间序列提供了可行性。
- 在特征方面，由于全局统计忽略了语音的时间结构，语音中的时间信息没有得到充分利用[31]。为了增强特征，文[32]将时间窗口逐帧引入递归层，并进行了情感分类实验，取得了较好的效果。
- 在早期的工作中，SER[31]、[33]-[36]直接使用了帧级特征，通过帧之间的序列来保存时间信息。众所周知，LSTM擅长处理序列数据，因此帧级别的特征比统计特征更适合于它的输入。
- 除了LSTM的输入外，还需要改进常规LSTM的输出。在LSTM[21][23]的大多数应用中，选择LSTM中最后时刻的输出作为下一个模型的输入(因为其他模型只接受具有固定维度的输入，而LSTM的输出的维度与其实数维度不一致的输入相同)。这可能会导致在其他历史时刻对LSTM输出信息的不完全使用；具体地说，由于长期依赖的时间跨度不是无限的[37]，[38]，在最后时刻LSTM的累积信息是有损失的。
- 在情感分类任务中，Keren[32]在LSTM的输出中引入了卷积神经网络的汇集操作。
- Mirsamadi[39]提出了一种用于计算具有注意力参数向量的帧的权重的注意力机制。由于LSTM的存储容量，在上一次的输出中积累的信息最丰富。因此，最后一次的输出通常被认为是LSTM的最终输出(在本研究和[39]中，这种方法都可以识别情绪)。
- 注意机制不仅可以用来优化LSTM的输出，而且还可以用来更新存储单元。一些研究已经调查了如何更新存储单元。陶[40]将注意力机制应用于LSTM的细胞状态更新，该机制关注细胞之间的信息，并更多地考虑先前的细胞状态。
- 在计算方面，Bradbury[41]提出了用于神经序列建模的准递归神经网络，它允许输出依赖于序列中元素的整体顺序，并且在训练和测试时间比传统的LSTM具有更快的速度。
- Cho[42]提出了门控递归单元(GRU)，它将输入门和遗忘门组合成一个更新门，并将单元状态和隐层状态混合在一起，从而简化了LSTM的计算。
- Greff[22]引入了一种耦合的LSTM，它只使用一个门来控制历史小区状态和候选小区状态对当前小区状态的影响，从而简化了候选小区状态权重的计算。
- Schuller等人提出的ComParE openSMILE特征。在语音情感识别中应用最为广泛[12]，[44]，其中一个[17]基于低级描述符(LLD，例如零交叉率、均方根帧能量、基音频率和Mel频率倒谱系数1-12)的提取，添加它们的增量，并应用统计函数，具有6373个特征的维度。
- 如[7]，证实了语音的harmonic information信息可以用于区分CASIA和EMODB数据库中的情感类别。
- 研究[46]还表明，声门波（glottis waves）包含某些情绪信息。
- 在Hochreiter[19]提出的原始LSTM算法中，单元状态的更新算法与前一时刻的隐含层输出和当前时刻的输入有关。此外，他们增加了窥视孔连接，并将前一时刻的细胞状态作为参数来更新当前状态。
