---
title: "Terabit Faster-Than-Nyquist PDM 16-QAM WDM Transmission With a Net Spectral Efficiency of 7.96 b/s/Hz"
description: ""
citekey: zhuTerabitFasterThanNyquistPDM2018
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:32:02
lastmod: 2023-04-11 11:28:15
---

> [!info] 论文信息
>1. Title：Terabit Faster-Than-Nyquist PDM 16-QAM WDM Transmission With a Net Spectral Efficiency of 7.96 b/s/Hz
>2. Author：Yixiao Zhu, Mingxuan Jiang, Zeyu Chen, Fan Zhang
>3. Entry：[Zotero link](zotero://select/items/@zhuTerabitFasterThanNyquistPDM2018) [URL link]() [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Zhu et al_2018_Terabit Faster-Than-Nyquist PDM 16-QAM WDM Transmission With a Net Spectral.pdf,E\:\\mypack\\人生规划\\ 3 _进修\\ 2 _升学\\ 4 _硕士学习\\ 4 _研究\\Zotero\\storage\\3K5SBBGX\\Zhu 等。 - 2018 - Terabit Faster-Than-Nyquist PDM 16-QAM WDM Transmi.pdf>)
>4. Other：2018 - Journal of Lightwave Technology     -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 

## 摘要

> [!abstract] In this paper, we experimentally demonstrate a 1.28 Tb/s faster-than-Nyquist (FTN) wavelength division multiplexing (WDM) system with polarization division multiplexed (PDM) 16-ary quadrature amplitude modulation (16-QAM) signal and coherent detection. Note that intersymbol interference (ISI) and intercarrier interference (ICI) are two major problems in FTN-WDM systems. In our experiment, we use a digital brick-wall filter at the transmitter to reduce the signal bandwidth and fit the FTN-WDM channel spacing. In doing so, the ICI can be mostly suppressed when aggregating the WDM channels. The aggressive filtering induced ISI is compensated based on duobinary signal processing at the receiver. Through numerical simulation, we evaluate the robustness of the receiver-side duobinary signal processing against bandwidth truncation ratio of the digital brick-wall filter, the ICI from neighboring channels, and laser phase noise. The FTN WDM transmission is based on five-channel 32 Gbaud PDM 16-QAM signal with 29 GHz channel spacing. The gross data capacity is 1.28 Tb/s (5 × 256 Gb/s). After 80 km standard single-mode fiber transmission, the bit-error rates of the five WDM channels are all below than 7% hard-decision forward error correction threshold of 4.5 × 10-3. The net bit rate is 1.15 Tb/s and the net optical spectral efficiency achieves a record of 7.96 b/s/Hz for PDM 16-QAM format. To our best knowledge, our work is the first report of Terabit FTN-WDM system with high-order modulation of PDM 16-QAM signal.

> 在本文中，我们通过实验展示了一个1.28 Tb/s 的超奈奎斯特 (FTN) 波分复用 (WDM) 系统系统，该系统同时使用了偏振分复用 (PDM) 16 元正交幅度调制 (16-QAM) 信号和相干检测两种技术。请注意，符号间干扰 (ISI) 和载波间干扰 (ICI) 是 FTN-WDM 系统中的两个主要问题。在我们的实验中，我们在发射机处使用数字砖墙滤波器（理想低通滤波器）来**降低信号带宽**并适应 FTN-WDM 信道间隔。这样做，在聚合 WDM 信道时，ICI 可以大部分被抑制。基于接收器处的双二进制信号处理来补偿激进滤波引起的 ISI。通过数值模拟，我们评估了接收端双二进制信号处理对数字砖墙滤波器（理想低通滤波器）的带宽截断率、来自相邻通道的 ICI 和激光相位噪声的鲁棒性。基于 5 通道 32 Gbaud PDM 16-QAM 载波信号，以29 GHz 信道间隔（channel spacing）在 FTN WDM 传输中，其总信息容量为 1.28 Tb/s (5 × 256 Gb/s)。并且在标准单模光纤传输80km 后，5个 WDM 通道的比特出错概率均低于7%的硬判决前向纠错 (HD-FEC) 阈值4.5×10-3。对于 PDM 16-QAM 方法，净比特率为 1.15 Tb/s，净光谱效率 SE 达到了 7.96 b/s/Hz 的新记录。据我们所知，本文工作所提出的是第一个对 PDM 16-QAM 信号进行高阶调制的 Terabit FTN-WDM 系统。

> [!tip]
> 信道间隔是用来防止信道间干扰的，规定的信道间隔有25KHz(宽带)、20KHz、12.5KHz(窄带)等，一般都是按照抗干扰要求来选取的。
> 理想低通滤波器用来抑制载波间干扰 (ICI).
> 双二进制信号处理来补偿符号间干扰 (ISI) .
> **baud** 的意思是 数据通信速度的表示单位。即调制速率，指的是有效数据讯号调制载波的速率，即单位时间内载波调制状态变化的次数。symbol/s

## 预处理

## 概述

## 结果

## 精读

**双二进制的编码原理：**

按照一定的规则将原来的二进制中逻辑信号“1”转换为逻辑信号“+1”和“-1”，使信号的频谱带宽减为原来的一半。调制解调过程分为预编码、编码和解码。

![]({25}_Terabit%20Faster-Than-Nyquist%20PDM%2016-QAM%20WDM%20Transmission%20With%20a%20Net%20Spectral%20Efficiency%20of%207.96%20b_s_Hz@zhuTerabitFasterThanNyquistPDM2018.assets/image-20220519105032.png)

双二进制调制器原理  

双二进制调制采用的方案是使用低于R/2 Hz的带宽传送R bit/s速率的信号。由奈奎斯特抽样准则可知，为了无码间干扰（ISI）地传送R bit/s的信号，传输脉冲所需的最小的带宽是R/2 Hz。这意味着双二进制调制存在码间干扰，实际上这个干扰是在可控制之下引入的，在接收端可以去掉这个干扰，恢复原始信号。  

双二进制编码允许一定的ISI，因此其频域的频谱变窄，信道的畸变效应减小。这也是为什么双二进制调制具有抗色散能力的原因。  

双二进制调制信号的产生方法之一是采用有限脉冲响应（FIR）滤波器和低通滤波器对数据比特进行低通滤波。这两个滤波器也可以合成一个低通滤波器。FIR的输入是两个数（1和-1），可能的输出结果有-1、0和1。因此双二进制信号也是一个三电平信号。这里FIR滤波器输出特性之一是输出信号是相关的，不是所有可能的三个电平构成的结果都会产生。FIR输出结果不可能是{1 –1}或{-1 1}，1和-1之间总要有一个0，但也不会出现{1 0 1}和{-1 0 –1}这种情况，只能输出{1 0 –1}或{-1 0 1}，即在一个0两边的电平是相反的。这也是双二进制调制技术抗色散的原因之一。编码举例如下：  
数字序列： 0 1 1 0 1 0 1 0 0 0 0 1 0 1 0 1 1 1 0 1  
双二进制码： 0 1 1 0-1 0 1 0 0 0 0 1 0-10 1 1 1 0-1

**相位噪声(phase noise)**

单频激光器的输出并不是严格的单色光，还存在相位噪声。这导致激光器输出具有有限的线宽。锁模激光器中的频率部分也同样存在，即辐射的频率梳。   
相位噪声的来源为量子噪声，尤其是增益介质中的自发辐射辐射到谐振腔模式中，还包含与光学损耗有关的量子噪声。另外，技术噪声也会产生影响，例如腔镜的振动或者温度涨落。有时，强度噪声也会与相位噪声通过非线性相互作用（参阅词条线宽增强因子）发生相互耦合。   
相位噪声可能体现为连续频移，或者相位跳变，或者二者的结合。



由于长距离、城域网、数据中心光纤网络的带宽需求不断增加，大容量光数据传输一直是非常需要的。由于可用带宽有限，需要高频谱效率 (SE) 的光传输，这通常通过高级调制方法来实现 [1]。

> 数字通信系统的**链路频谱效率**定义为净比特率（有用信息速率，不包括纠错码）或最大吞吐量除以通信信道或数据链路的带宽（单位：赫兹）。调制效率定义为净比特率（包括纠错码）除以带宽。比较不同通信系统的有效性时，单看他们的传输速率是不够的，还应该看在这样的传输速率下所占信道的宽度。所以真正衡量数字通信系统传输效率的应当是单位频带内的码元传输速率，即 Spectrum Effectiveness=R/B(码元速率/带宽) 单位为 Bd/HZ(波特每赫兹)

基于偏振分复用 (PDM) +16 元正交幅度调制 (16-QAM) 方法的光学系统是实现具有实际光信噪比 (OSNR) 要求的高频谱效率的有希望的候选者之一。

> **光信噪比**的定义是在光有效带宽为 0.1 nm 内光信号功率和噪声功率的比值。光信号的功率一般取峰值，而噪声的功率一般取两相临通路的中间点的功率电平。它能够定量检测信号沿光纤传播途中，被噪声干扰的程度。
> 并且 OSNR 与比特出错概率 (BER) 之间存在直接关系，其中 BER 是衡量传输质量的终极值。OSNR 越高则比特出错概率越低，也即传输错误越少。

例如
1. 22 通道，15.625 Gbaud PDM 16-QAM 信号为 Nyquist shaped，滚降系数 roll-off factor 为 0.01，以 16 GHz 信道间隔传输，得到的净 SE 为 6.25 b/s/Hz [2]。
2. 7 通道，10 Gbaud PDM-16 QAM，以 10.01 GHz 信道间隔，在超过 5890 公里的 Corning SMF-28 超低损耗光纤传输后，得到的净 SE 为 6.60 b/s/Hz [3]。
3. 37.5 Gbaud PDM 16-QAM 信号，以奈奎斯特间隔，即最大允许的抽样间隔：37.5 GHz，在后置补偿（post equalization）的帮助下，得到的净 SE 为 6.66 b/s/Hz  [4]。
4. 16 Gbaud PDM-16 QAM 信号，以 16 GHz 信道间隔在 1200 km 标准单模光纤 (SSMF) 上传输后，得到的比特出错概率 (BER) 低于 7% 的硬判决前向纠错 (HD-FEC) 阈值，实现了高达 7.47 b/s/Hz [5] 的净 SE。



除了前面提到的可以得到高 SE 的 16-QAM 传输实验之外，超奈奎斯特(FTN)可以通过将波分复用 (WDM) 信道设置为小于符号率（符码率、波特率）的间隔，来进一步提高 SE。在 FTN 系统中，载波间干扰 (ICI) 和符号间干扰 (ISI) 是需要解决的两个主要损耗问题。

实现 FTN 传输的一种直接方法是重叠相邻信道，这将会引起 ICI 但并不引入 ISI 问题[6]、[7]。基于联合多进多出(MIMO) 处理，占用 30 GHz 带宽超通道的 2 通道 16 Gbaud 双载波 FTN 16-QAM，在 960 km SSMF 传输中传输后，得到的净 SE 为 7.68 b/s/Hz [ 7]。然而，这种方法需要锁频光源和同时接收重叠通道，这会增加收发器的复杂性。

另一种方法是通过引入可控 ISI 来避免 ICI，例如可以使用发射端双二进制或多二进制编码的方法[8]-[10]，通过类余弦信号频谱编码部分抑制 ICI，再通过 2-tap（或 3-tap）最大似然序列检测（MLSD）[11]消除 ISI。

同时，在发射端使用主动滤波方法（aggressive filtering）也被证明是有效的，其中包括光滤波、电滤波和数字滤波。对于光滤波，以前的大多数工作都集中在正交相移编码 QPSK 方法上，它通常在组合 WDM 通道之前使用波长选择开关 (WSS)，并根据 9-QAM 星座图解调恢复信号 [12]。然而，对于 16-QAM 等高阶调制方法，当信道间隔小于符号率 [7]、[13]、[14] 时，光学滤波方法仍然是一个挑战。

此外，时频打包 (TFP) [15]、[16] 是一种可行的解决方案，它优化了时间和频率间隔以实现最大 SE。通过利用电滤波，在 [15] 中报告了 PDM QPSK 方法得到的净 SE 高达 7.1 b/s/Hz。


在本文中，我们采用数字砖墙滤波器来主要抑制密集通道之间的 ICI，它可以执行精确的频谱编码，其边缘比光学（或电）滤波更陡峭，可以通过接收器处的双二进制信号处理来减轻激进滤波引起的 ISI。我们在 5 通道 WDM 32 Gbaud PDM 16-QAM FTN 系统中验证了该方案。29 GHz 信道间隔的 WDM 信号在 80 km 标准单模光纤 (SSMF) 上传输后，得到的 BER 低于 7% HD-FEC 阈值 4.5×10−3，其总数据速率高达 1.28 Tb/s (256 Gb/s × 5)，每通道 256 Gb/s (32 Gbaud × 2 × 4)。考虑到帧冗余和 7% HD-FEC 开销，WDM 系统得到的净比特率为 1.15 Tb/s，每个通道的净比特率为 230.8 Gb/s。 PDM 16-QAM 信号的净频谱效率达到了 7.96 bit/s/Hz (1.15 Tb/s/5/29 GHz) 的记录。

本文的其余部分安排如下。在第二节中介绍了 FTN 方案的工作原理，数字信号处理 (DSP) 堆栈，以及实验装置。第三部分评估了 DSP 算法的性能并报告了实验结果。最后，在第四节得出结论。

## DSP Stack and Experimental Setup

### A. DSP Stack

DSP 的示意图如图 1（a）和（b）所示。在发送端，比特流首先映射到 16-QAM（信号调制）。之后经过上采样后，使用滚降系数为 0.01（决定频宽和陡峭程度）的根升余弦 (RRC) 滤波器对信号进行数字整形。

在对原始 01 数据进行编码调制后数据仍是为数不多的几个离散状态。例如：BPSK 为 1 和-1 两种状态，QPSK 也是 1 和-1 两种状态（只是比 BPSK 多了两个映射象限），16 QAM 则为±1，±2，±3 这 6 个状态。并且这些存在于时域的波形在时域上反应出来就是一个又一个方波，由傅里叶可知，方波的组成是由近乎无限高的高频分量组成的，而这在通信系统中是物理不可实现的。

升余弦滚降滤波器以具有余弦函数性质的频域响应代替了方形频响，将高频的方波“滚降”到物理可实现的升余弦函数脉冲，即起到了一个低通滤波器的作用，保证了采样时刻无 ISI 影响。

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519192041.png)

然后对信号进行下采样。最后，利用数字砖墙滤波器（低通滤波器）对信号带宽进行压缩，只需将信号的 $10\%$ 最高频率在频域设置为零，从而将每个通道中 32 Gbaud 信号的带宽（信号频谱宽度？）压缩为 $29.09 \mathrm{GHz}(32 \mathrm{GHz} \times 1.01 \times 0.9)$ ，括号内包括 RRC 滤波器的滚降系数。

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519144533.png)

图 1(c) 显示了发送的 Nyquist 16-QAM 信号的帧结构。前导码包括两个 63-symbol synchronization 序列和两个670-symbol 的训练序列。为了获得 Jones 空间中的 $2\times 2$ 信道响应矩阵，训练序列由两对 time-multiplexed patterns（时分复用？）组成，跨越两个极化 $\left[t_{x} \text{ }  t_{y}\right]^ {T}$ in (1), $$ \left(\begin{array}{l} t_{x} \\ t_{y} \end{array}\right)=\left(\begin{array}{ cc} M &0 \\ 0 & M \end{array}\right) $$
这里 $(\cdot)^{T}$ 是转置操作， $'M'$ 表示 255-symbol M-sequence 和 80-symbol 循环前缀。 $'o'$ ; 代表 335-symbol 的零序列。因此， $t_{x}$ 和 $t_{y}$ 都由一个 $'M'$ 表序列和一个 $'o'$ 序列组成，总长度为 670 个符号。

在前导码之后传输的是 50800 个数据符号。需要注意的是，在训练序列和数据符号之间插入了一个 0 符号，以在接收端进行双二进制处理时切断训练序列的影响。对于双二进制处理后的粗略相位估计，导频符号对均匀地位于数据帧中。在每个 256 符号长度的数据块中，有一对两个连续的导频符号。单通道的净比特率计算为 $230.8(=32 \times 4 \times 2 / 1.07 /(63 \times 2+670 \times 2+1$ $+51200) \times 50800) \mathrm{Gb} / \mathrm{s}$ ，同时考虑帧冗余和 $7 \%$  $\mathrm{HD}-\mathrm{FEC}$ 开销。

接收端的 DSP 执行顺序如下。

信号首先被重新采样为每符号 4 个样本 (SPS)。然后补偿色散（CD）。 LO 和信号之间的频率偏移是通过获得 $\left|\mathrm{FFT}\left(r^{4}(t)\right)\right|[17]$ 的最大值来估计的。这里 $\mathrm{FFT}(\cdot)$ 是快速傅里叶变换， $r(t)$ 是下转换（下采样？）后的信号。在匹配滤波和同步之后，执行基于部分响应 $H(t)$ 的 $2×2$ 蝶形结构时域均衡，它表现出更好的带宽限制效应容忍度[12]。传递函数为 $H(t)=1+\delta\left(t-T_{s}\right)$ ，在此期间，符号将等于其自身和紧随其后的符号之和。因此，在此操作之后，星座图从 16-QAM 映射到 49-QAM。在均衡数据之前，使用递归最小二乘 (RLS) 算法从训练序列更新滤波器抽头。

载波相位恢复分两步进行。

1.根据 $(2)$ ，利用均匀分布的导频对实现粗相位跟踪。


$$
\Delta \varphi(k)=\arg \left\{\frac{\text { Pilot }_{R x_{-} e q}(k, 2)}{\text { Pilot }_{T x}(k, 1)+\text { Pilot }_{T x}(k, 2)}\right\}
$$
这里 $\Delta \varphi(k)$ 是第 $k^{\text {th }}$ 符号块中估计的粗略旋转角度（相位？）。 $\arg \{\cdot\}$ 表示角度操作。 Pilot $_{T x}(k, 1)$ 和 Pilot $_{T x}(k, 2)$ 是第 $k^{\text {th }}$ 符号块中的一对传输的导频。 $P i l o t_{R x_{-} e q}(k, 2)$ 是经过接收器中双二进制均衡后导频对的第二个导频。请注意，在双二进制均衡之后，每个数据符号都与其前一个符号相加。为避免未知数据符号的影响，仅采用每对中的第二个导频符号进行相位校正。因此，Pilot ${ }_{R x_{-} e q}(k, 2)$ 除以两个连续的 Pilot $_{T x}(k, 1)$ 和 Pilot $_{T x }(k, 2)$ 就可得到结果。在我们的实验中，每个具有 256 个数据符号的数据块中的一对导频足以进行粗略的相位恢复。

2. 准确的相位恢复基于如图 1(d) [17]、[18] 所示的盲相位搜索 (BPS) 算法。代价函数 $e(\varphi)$ 根据 $(3)$ 计算，其中 Decision $(\cdot)$ 表示按照 49-QAM 星座的硬决策结果， $N$ 是 BPS 阶段的符号块长度， $S_{\mathrm{in}, n}$ 和 $S_{\mathrm{out}, n}$ 分别是输入和输出数据符号。

$$
\begin{gathered}

e(\varphi)=\sum_{n=1}^{N}\left|S_{\mathrm{in}, n} \exp (j \varphi)-\operatorname{Decision}\left(S_{\mathrm{out}, n} \exp (j \varphi)\right)\right|^{2}

\end{gathered}
$$

然后使用 $\mathrm{T}_{\mathrm{s}}$ 间隔的直接决策 RLS 滤波器通过跟踪时变信道响应来改善信号质量，其成本函数由滤波之间的距离构成符号和 49-QAM 星座中最近的点决定。为了消除已知的 ISI，使用基于 Viterbi 解码算法 [8]、[11]  MLSD 方法。最后，通过 $\sim 2 \times 10^{6}$ 位样本的错误计数来计算 BER。

### B. Experimental Setup

图 2 显示了 FTN WDM 传输系统的实验装置。在发射器上，5个间隔为 29 GHz 频率网格的 WDM 通道由 5 个外腔激光器 (ECL) 提供，这些激光器由级联的 2 x 1 保偏光耦合器 (PM- OC）组成。每个激光器的线宽约为 $\sim 100 \mathrm{kHz}$ 。以 92 $\mathrm{GSa} / \mathrm{s}$ 运行的任意波形发生器 (Keysight M8196A) 可生成 32 Gbaud Nyquist 16-QAM FTN 信号，这些信号驱动两个偏置在零点的 IQ 调制器，分别生成奇数和偶数通道。 AWG 和 IQ 调制器的带宽分别为 $32\mathrm{GHz}$ 和 $25\mathrm{GHz}$ 。在去相关的光学延迟之后，奇数和偶数通道通过 $2 × 1$ PM-OC 相互交错。 PDM 使用偏振分束器/组合器 (PBS/PBC) 和可调谐光学延迟线进行仿真。光延迟线的延迟测量为335个符号，与时间复用训练序列模式的周期一致。在发射到 $80 \mathrm{~km}$ SSMF 链路之前，使用掺铒光纤放大器 (EDFA) 用于调整发射功率。不使用在线光学 CD 补偿。

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519154931.png)

在接收端，使用光学带通滤波器（OBPF，Yenista Optics XTM-50）选择所需通道。然后将信号和本地振荡器 (LO) 发送到光混合器中。使用 3-dB 带宽为 $70 \mathrm{GHz}$ 的四个平衡光电二极管 (BPD)  ，将拍频信号转换为电域。最后，电信号由以 80 GSa/s 运行的实时数字存储示波器（Keysight DSA-X 96204 Q）进行采样，以执行离线 DSP。

## Results and Discussions

### A. Simulation Results

我们首先针对背靠背 (BTB) 场景下单通道数字砖墙滤波器（低通滤波器）的不同带宽截断率评估基于双二进制的均衡的鲁棒性。使用商业软件 VPItransmissionMaker 9.1 进行模拟。在我们的仿真中，数模转换器 (DAC) 和模数转换器 (ADC) 具有无限分辨率。 BPD 非常理想，没有暗电流、热噪声和散粒噪声。

如图 3(a) 所示，传输信号的带宽与数字砖墙滤波器（低通滤波器）的带宽截断率成正比。当聚合 FTN WDM 信道时，数字频谱的边缘足够陡峭以实现低 ICI。

图 3(b) 显示了对具有不同带宽截断比的信号使用传统均衡或双二进制均衡的模拟星座。需要注意的是，传统的均衡是指在均衡过程中数据符号被迫向传输的训练序列收敛。相比之下，二元均衡将收敛于具有部分响应 $H(t)$ 的训练序列，如第 II 节所述。在图 3(b) 中，我们可以发现采用常规均衡的星座点在 0.9 的截断率下变得无法区分，而采用双二进制均衡的星座仍然具有良好的收敛性。

此外，在图 3(c) 中，针对不同带宽截断信号测试了 BER-OSNR 关系。在 BER 为 $4.5 \times 10^{-3}(7 \% \mathrm{HD}-\mathrm{FEC}$ Threshold) 时，双二进制均衡（深蓝色曲线）带来 $\sim 1.5 \mathrm{~ dB}$ 与未压缩信号的传统均衡（品红色曲线）相比，OSNR 损失主要来自部分响应操作中的噪声累积。对于带宽截断比大于 0.9 的信号，几乎没有 OSNR 损失。具体来说，未压缩的信号（深蓝色曲线）和截断率为 0.95 的信号（蓝色曲线）几乎相互重叠。此外，截断比为o.9的信号（青色曲线）与未压缩信号相比，OSNR 损失仅为o.2 dB，显示出适合 FTN 传输的压缩比区域。请注意，32-QAM 信号的 BER-OSNR 性能也显示在图 3 (c) 中进行了比较。如果信号带宽被强截断（即截断比 0.83），FTN 16 QAM 信号（深青色曲线）的 BER-OSNR 性能将接近甚至比传统 32-QAM 信号（黑色曲线）更差.

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519155815.png)

我们还模拟了 BTB 场景中 3 通道 WDM 系统中不同 OBPF 带宽所需的 OSNR 与通道间隔的关系。接收端 OBPF 被建模为 4 阶高斯滤波器。图 4(a) 显示了在 BER 为 $4.5 \times 10^{-3}$ 时所需的 OSNR 作为不同 OBPF 带宽的信道间隔的函数。带宽截断率固定为 $0.9$ ，因此信号带宽约为 $29.09\mathrm{GHz}$ 。由于数字砖墙滤波器（低通滤波器）后信号频谱的陡峭边缘，对于 29 Ghz 的信道间隔，只有 0.4 dB 的 OSNR 损失，这主要是因为与相邻通道有轻微重叠。还可以观察到，接收端 OBPF 的带宽对 BER 性能几乎没有影响。具体来说， $35\mathrm{GHz}$ 和 $40\mathrm{GHz}$ 带宽曲线的比较表明，**DSP 中的匹配 RRC 滤波器可以去除大部分光滤波后的残余 ICI**。此外，当信道间隔小于 RRC 滤波器的带宽时，匹配 RRC 滤波器后仍有部分 ICI。通过比较 $30 \mathrm{GHz}$ 与 35 Ghz 带宽这证实了双二进制均衡对 ICI 有一定的抵抗力。上述仿真结果表明，在实际实现中，粗滤光足以用于波长解复用。

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519155908.png)

此外，我们模拟了发射器和接收器处激光器线宽的影响。对 BTB 场景下的单通道操作进行了仿真。如图 4(b) 所示，当 BER 为 $4.5 \times 10^{-3}$ 时，图 4（c）显示了不同相位恢复阶段的星座图。均衡后，由于激光相位噪声的存在，星座点呈螺旋状分布。然后，在基于导频的粗相位恢复之后，星座点变得更加清晰。在 $100 \mathrm{kHz}$ 激光线宽的情况，经过 BPS 算法计算之后，残余相位噪声得到了缓解。然而，对于 $500 \mathrm{kHz}$ 的激光线宽，一些点尚未收敛到 49-QAM 星座。

### B. Experimental BTB Performance

我们首先研究了 BTB 场景下单通道数字砖墙滤波器带宽截断率的影响。 OSNR 值测量为 $36.0 \mathrm{~dB}$ ，带宽截断比为 $1.0$ 作为参考。如图5(a)所示，我们可以发现 $Q^{2}$ -factor 在截断比区间 $[0.9,1.0]$ 处几乎保持不变，并且在截断比小于 0.9 时迅速减小，这与图 3（c）中的模拟结果非常吻合。因此，我们在实验中选择带宽截断率等于 0.9 ，因为这种带宽截断可以很好地解决主动滤波引起的 ISI。其中 $\mathrm{Q}^{2}$ -因子被定义为 BER 的函数。
$$ Q^{2}=20 \log _{10}\left[\sqrt{2} \cdot e r f c^{-1}(2 \cdot B E R)\right] $$

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519155620.png)

图 5(b) 描绘了具有不同带宽截断率的数字滤波后的信号光谱，这些光谱是在 $\mathrm{PD}$ 检测之前测量的。光谱分辨率设置为 $0.01 \mathrm{~nm}$ 。可以观察到，信号带宽与数字砖墙滤波器的带宽截断率成正比。此外，还有一些频谱泄漏，这将成为 FTN WDM 系统中 ICI 的一部分。

然后我们通过在 BTB 场景下以不同的信道间隔打包 WDM 信道来测试 ICI。如图 6(a) 所示，我们测量 $\mathrm{Q}^{2}$ -因子作为从 $29\mathrm{GHz}$ 到 $45\mathrm{GHz}$ 的信道间隔的函数。 OSNR 值测量为 $34.3 \mathrm{~dB}$ 。当信道间隔大于 $34\mathrm{GHz}$ 时， $\mathrm{Q}^{2}$ -因子饱和到 $10.2\mathrm{~dB}$ ，因为在这样的信道间隔下 ICI 可以忽略不计。对于 29  $\mathrm{GHz}$ 的信道间隔，有 0.95  $\mathrm{~dB}$ 的 $\mathrm{Q}^{2}$ 因子损失。图 6(b)为 5 通道 WDM 系统不同通道间距的光谱图。

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519155539.png)

图 7(a) 分别显示了 WDM、具有双二进制和传统均衡的单通道信号在 BTB 场景下的 OSNR 灵敏度曲线。在我们的实验中，通过光衰减器和 EDFA 放大来改变 OSNR。对于 1.o 的带宽截断率，单通道的双二进制均衡（蓝色曲线）在 BER 为 $4.5\times 10^{-3}$ 时，与传统方法相比具有 $\sim 1.9 \mathrm{~dB}$ OSNR 损失均衡（深青色曲线）。这种惩罚可以解释为双二进制均衡中的噪声累积。对于 0.9 的带宽截断率，传统均衡（紫色曲线）无法恢复信号。相比之下，双二进制均衡仅能观察到 $\sim 0.4 \mathrm{~dB}$ 额外的 OSNR 损失，这证实了双二进制均衡处理对激进滤波引起的 ISI 具有鲁棒性。此外，WDM 带来了 $\sim 2.2 \mathrm{~dB}$ OSNR 损失。这种损失主要是由在 FTN 间隔中打包 WDM 信道后的 ICI 引起的。在图 7(a) 中，可以在高 OSNR 区域观察到错误底限，这主要来自 DSO 的噪声。图 7 (b) 给出了在 WDM 场景下两个 X/Y 极化的典型星座图，截断比等于 $0.9$ ，在 BTB 场景下，截断比分别为 o.9 和 $1.0$ 的单通道。 $\mathrm{A}$ 和 $\mathrm{B}$ 的星座之间的差异显示了 ICI 的影响，而 $B$ 和 $C$ 的星座之间的差异则显示了截断诱导 ISI 的影响.

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519155426.png)

### C. Experimental Transmission Performance

 对于使用5通道波分复用系统, 在 $80 \mathrm{~km}$ 标准单模光纤传输实验中，我们首先优化了系统的总发射功率，如图 8(a) 所示。可以得出其最佳总发射功率为 $7.0 \mathrm{dBm}$ ，对应的最佳比特出错率为 $3.5 \times 10^{-3}$ 。
 
 图 8(b) 描绘了在发射功率为 $7.0\mathrm{dBm}$ 的条件下,经过 $80\mathrm{~km}$ 传输后,所有的 5 个信道的比特出错率测量值。可以得到对应的光信噪比测量值为 $30.8 \mathrm{~dB}$ ，所有 5 个信道的平均比特出错率为 $3.2\times 10^{-3}$ ，低于 $7\%$ 硬判决前向纠错阈值 $4.5\times 10^{-3}$ 。其中的插图是第三通道的星座图。第 1 通道和第 5 通道因为仅遭受了一个相邻通道的串扰,所以会有更小的比特出错率。
 
 图 8(c) 是以 $0.01 \mathrm{~nm}$ 分辨率分别显示的发射和接收端光谱。其中深青色曲线和粉红色曲线分别代表经过光学带通滤波器的波分复用和单通道信号。通过对比两条曲线可以发现，经过光学带通滤波器之后，相邻通道仍有一些残余信号，**这些信号的大部分会在经过数字匹配滤波器后被去除，其余的会被双二进制均衡抑制。**

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519155407.png)

### D. Discussions

本文研究了基于 FTN 方案的频域主动滤波器的性能。1. 通过 BTB 实验以评估该方案抑制 ISI 和 ICI 的效果. 2. 通过 $80 \mathrm{~km}$ 的标准单模光纤，验证了其实际传输性能。

对于实际实施，我们的 FTN 方案主要与传统的奈奎斯特脉冲整形相干系统兼容。在发射端，使用 2 倍的上采样就可以避免频谱重叠。 DAC 和 IQ 调制器的带宽要求可以根据带宽截断率来降低。此外，可以在 DAC 的输出端使用低通电子滤波器来抑制频谱泄漏。由于 16-QAM 信号的双二进制操作，在接收器处，均衡器和载波相位恢复阶段都应修改以协调 49-QAM 星座。要消除 ISI，需要基于 MLSD 模块的 2-tap Viterbi 解码算法。

表一总结了迄今为止讨论的三种 FTN 方案之间的比较。需要注意的是，由于 TFP 的恢复需要结合最大后验概率 (MAP) 检测器和低密度奇偶校验 (LDPC) 解码器 [15]，因此无法直接将 TFP 与上述方案进行比较。对于重叠双通道方案，发送端操作与传统的 16-QAM 信号一样简单。然而，由于 ICI 缓解需要相邻信道的信息，因此硬件要求和计算复杂度都是这三种方案中最高的。或者，多二进制整形和数字砖墙滤波器方案在没有 MIMO 均衡的情况下共享相同的接收器操作。在发射机处，多二进制整形生成类似余弦的频谱，以通过延迟和加法运算部分抑制 ICI，而数字砖墙滤波器生成截断的平方频谱以避免 ICI。随着信道间隔的减小，对于多二进制整形方案，类余弦频谱（ICI）的重叠将变得更加严重。

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519155320.png)

## Conclusions

在本文中，通过在发射端使用了低通滤波器来抑制密集型 WDM 信道的载波间干扰，并在 16-QAM FTN WDM 系统的接收端使用双二进制信号处理方法来减轻符号间干扰。

本文在仿真实验中对双二进制信号处理技术，分别验证了其对主动滤波引起符号间干扰、WDM 汇合引起的载波间干扰和激光相位噪声三者的鲁棒性。

本文还通过实验演示了 $1.28 \mathrm{~Tb} / \mathrm{s}$ 5通道 FTN-WDM 系统，该系统使用了32 Gbaud PDM 16-QAM 的载波信号和 $29 \mathrm{GHz}$ 信道间隔。该 FTN-WDM 系统，在标准单模光纤中传输超过 $80 \mathrm{~km}$ 后，信道的比特出错率均低于 $7 \%$ 硬判决前向纠错阈值 $4.5 \times 10^{-3}$ 。

本文同时在 BTB 场景下，分别对低通滤波器产生的 ISI 和来自相邻通道的 ICI 进行了研究。

本文是第一个将 PDM 16-QAM 信号应用于 Terabit FTN-WDM 传输的工作，并且使用此方法得到的净比特率为 $1.15 \mathrm{~Tb} / \mathrm{s}$ ，净光谱效率（SE）为 $7.96 \mathrm{~b} / \mathrm{s} / \mathrm{Hz }$ 。

本文还通过实验证明，通过截断 16-QAM 信号的 $10\%$ 带宽可以实现 FTN-WDM 操作，且 OSNR 损失很小。

## 基础知识

### 通信系统

#### 通信系统分类

1）按照信号特征分为：模拟通信系统、数字通信系统
其中，数字通信的优缺点：

优点：
- 抗噪声、抗干扰性能更好，可实现传输差错控制；
- 易于与现代数字信号处理技术结合；
- 易于用大规模数字集成电路实现，设备简单；
- 易加密，保密性好；

缺点：（待补充）

2）按照复用方式分为：时分复用、频分复用、码分复用通信系统

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519084405.png)

**频分复用**

频分复用（FDM，Frequency Division Multiplexing）就是将用于传输信道的**总带宽划分**成若干个子频带（或称子信道），每一个子信道传输 1 路信号。频分复用要求总频率宽度大于各个子信道频率之和，同时为了保证各子信道中所传输的信号互不干扰，应在各子信道之间设立隔离带，这样就保证了**各路信号互不干扰**（条件之一）。频分复用技术的特点是所有子信道传输的信号以**并行**的方式工作，每一路信号传输时可不考虑传输时延，因而频分复用技术取得了非常广泛的应用。频分复用技术除传统意义上的频分复用（FDM）外，还有一种是正交频分复用（OFDM）。

OFDM（Orthogonal Frequency Division Multiplexing）实际是一种多载波数字调制技术。OFDM 全部载波频率有相等的频率间隔，它们是一个基本振荡频率的整数倍，正交指各个载波的信号频谱是正交的。

1）高速传输带来的新问题：随着数据传输速率的提高，符号周期 T 很小，高速传输时会产生**多径效应**  

2）OFDM 技术要素：  
① **增大符号周期**：发射端串联传输转成并联传输，可以抑制多径效应  
② **多载波调制**  
③ **载波相互正交**

OFDM 系统比 FDM 系统要求的带宽要小得多。由于 OFDM 使用无干扰正交载波技术，单个载波间无需保护频带，这样使得可用频谱的使用效率更高。另外，OFDM 技术可动态分配在子信道中的数据，为获得最大的数据吞吐量，多载波调制器可以智能地分配更多的数据到噪声小的子信道上。目前 OFDM 技术已被广泛应用于广播式的音频和视频领域以及民用通信系统中，主要的应用包括：非对称的数字用户环线（ADSL）、数字视频广播（DVB）、高清晰度电视（HDTV）、无线局域网（WLAN）和第 4 代（4 G）移动通信系统等。

**时分复用**  

时分复用（TDM，Time Division Multiplexing）就是将提供给整个信道传输信息的时间划分成若干时间片（简称时隙），并将这些时隙分配给每一个信号源使用，每一路信号在自己的时隙内独占信道进行数据传输。时分复用技术的特点是时隙事先规划分配好且固定不变，所以有时也叫同步时分复用。其优点是时隙分配固定，便于调节控制，适于数字信息的传输；缺点是当某信号源没有数据传输时，它所对应的信道会出现空闲，而其他繁忙的信道无法占用这个空闲的信道，因此会降低线路的利用率。时分复用技术与频分复用技术一样，有着非常广泛的应用，电话就是其中最经典的例子，此外时分复用技术在广电也同样取得了广泛地应用，如 SDH，ATM，IP 和 HFC 网络中 CM 与 CMTS 的通信都是利用了时分复用的技术。

**波分复用**  

通信是由光来运载信号进行传输的方式。在光通信领域，人们习惯按波长而不是按频率来命名。因此，所谓的波分复用（WDM，Wavelength Division Multiplexing）其本质上也是频分复用而已。WDM 是在 1 根光纤上承载多个波长（信道）系统，将 1 根光纤转换为多条“虚拟”纤，当然每条虚拟纤独立工作在不同波长上，这样极大地提高了光纤的传输容量。由于 WDM 系统技术的经济性与有效性，使之成为当前光纤通信网络扩容的主要手段。波分复用技术作为一种系统概念，通常有 3 种复用方式，即 1 310 nm 和 1 550 nm 波长的波分复用、粗波分复用（CWDM，Coarse Wavelength Division Multiplexing）和密集波分复用（DWDM，Dense Wavelength Division Multiplexing）。

（1）1 310 nm 和 1 550 nm 波长的波分复用  

这种复用技术在 20 世纪 70 年代初时仅用两个波长：1 310 nm 窗口一个波长，1 550 nm 窗口一个波长，利用 WDM 技术实现单纤双窗口传输，这是最初的波分复用的使用情况。  

（2）粗波分复用  

继在骨干网及长途网络中应用后，波分复用技术也开始在城域网中得到使用，主要指的是粗波分复用技术。CWDM 使用 1 200~1 700 nm 的宽窗口，目前主要应用波长在 1 550 nm 的系统中，当然 1 310 nm 波长的波分复用器也在研制之中。粗波分复用（大波长间隔）器相邻信道的间距一般≥20 nm，它的波长数目一般为 4 波或 8 波，最多 16 波。当复用的信道数为 16 或者更少时，由于 CWDM 系统采用的 DFB 激光器不需要冷却，在成本、功耗要求和设备尺寸方面，CWDM 系统比 DWDM 系统更有优势，CWDM 越来越广泛地被业界所接受。CWDM 无需选择成本昂贵的密集波分解复用器和“光放”EDFA，只需采用便宜的多通道激光收发器作为中继，因而成本大大下降。如今，不少厂家已经能够提供具有 2~8 个波长的商用 CWDM 系统，它适合在地理范围不是特别大、数据业务发展不是非常快的城市使用。  

（3）密集波分复用  

密集波分复用技术（DWDM）可以承载 8～160 个波长，而且随着 DWDM 技术的不断发展，其分波波数的上限值仍在不断地增长，间隔一般≤1.6 nm，主要应用于长距离传输系统。在所有的 DWDM 系统中都需要色散补偿技术（克服多波长系统中的非线性失真——四波混频现象）。在 16 波 DWDM 系统中，一般采用常规色散补偿光纤来进行补偿，而在 40 波 DWDM 系统中，必须采用色散斜率补偿光纤补偿。DWDM 能够在同一根光纤中把不同的波长同时进行组合和传输，为了保证有效传输，一根光纤转换为多根虚拟光纤。目前，采用 DWDM 技术，单根光纤可以传输的数据流量高达 400 Gbit/s，随着厂商在每根光纤中加入更多信道，每秒太位的传输速度指日可待。

**码分复用**  


码分复用（CDM，Code Division Multiplexing）是靠不同的编码来区分各路原始信号的一种复用方式，主要和各种多址技术结合产生了各种接入技术，包括无线和有线接入。例如在多址蜂窝系统中是以信道来区分通信对象的，一个信道只容纳 1 个用户进行通话，许多同时通话的用户，互相以信道来区分，这就是多址。移动通信系统是一个多信道同时工作的系统，具有广播和大面积覆盖的特点。在移动通信环境的电波覆盖区内，建立用户之间的无线信道连接，是无线多址接入方式，属于多址接入技术。联通 CDMA（Code Division Multiple Access）就是码分复用的一种方式，称为码分多址，此外还有频分多址（FDMA）、时分多址（TDMA）和同步码分多址（SCDMA）。  

（1）FDMA  

FDMA 频分多址采用调频的多址技术，业务信道在不同的频段分配给不同的用户。FDMA 适合大量连续非突发性数据的接入，单纯采用 FDMA 作为多址接入方式已经很少见。目前中国联通、中国移动所使用的 GSM 移动电话网就是采用 FDMA 和 TDMA 两种方式的结合。  

（2）TDMA 时分多址  

TDMA 时分多址采用了时分的多址技术，将业务信道在不同的时间段分配给不同的用户。TDMA 的优点是频谱利用率高，适合支持多个突发性或低速率数据用户的接入。除中国联通、中国移动所使用的 GSM 移动电话网采用 FDMA 和 TDMA 两种方式的结合外，广电 HFC 网中的 CM 与 CMTS 的通信中也采用了时分多址的接入方式（基于 DOCSIS 1.0 或 1.1 和 Eruo DOCSIS1.0或1.1）。 

（3）CDMA 码分多址  

CDMA 是采用数字技术的分支——扩频通信技术发展起来的一种崭新而成熟的无线通信技术，它是在 FDM 和 TDM 的基础上发展起来的。FDM 的特点是信道不独占，而时间资源共享，每一子信道使用的频带互不重叠；TDM 的特点是独占时隙，而信道资源共享，每一个子信道使用的时隙不重叠；CDMA 的特点是所有子信道在同一时间可以使用整个信道进行数据传输，它在信道与时间资源上均为共享，因此，信道的效率高，系统的容量大。CDMA 的技术原理是基于扩频技术，即将需传送的具有一定信号带宽的信息数据用一个带宽远大于信号带宽的高速伪随机码（PN）进行调制，使原数据信号的带宽被扩展，再经载波调制并发送出去；接收端使用完全相同的伪随机码，与接收的带宽信号作相关处理，把宽带信号换成原信息数据的窄带信号即解扩，以实现信息通信。CDMA 码分多址技术完全适合现代移动通信网所要求的大容量、高质量、综合业务、软切换等，正受到越来越多的运营商和用户的青睐。 

（4）同步码分多址技术  

同步码分多址（SCDMA，Synchrnous Code Division Multiplexing Access）指伪随机码之间是同步正交的，既可以无线接入也可以有线接入，应用较广泛。广电 HFC 网中的 CM 与 CMTS 的通信中就用到该项技术，例如美国泰立洋公司（Terayon）和北京凯视通电缆电视宽带接入，结合 ATDM（高级时分多址）和 SCDMA 上行信道通信（基于 DOCSIS 2.0 或 Eruo DOCSIS2.0）。 

中国第 3 代移动通信系统也采用同步码分多址技术，它意味着代表所有用户的伪随机码在到达基站时是同步的，由于伪随机码之间的同步正交性，可以有效地消除码间干扰，系统容量方面将得到极大的改善，它的系统容量是其他第 3 代移动通信标准的 4～5 倍

3）按照**工作方式**分为：单工、半双工、全双工通信系统

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519084419.png)

（上图中从上往下依次为：单工、半双工、双工）  

全双工：指可以同时（瞬时）进行信号的双向传输（A→B 且 B→A）。指 A→B 的同时 B→A，是瞬时同步的。

半双工：指一个时间内只有一个方向的信号传输（A→B 或 B→A）。

4）按照**传输方式**分为：并行、串行通信系统

#### 通信系统结构

1）**普适性通信系统结构**

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519084545.png)

2）**模拟通信系统结构**

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519084549.png)

相比于普适性通信系统结构，模拟通信系统结构多了对**模拟信号的调制和解调**。

**调制与解调**，是无线通信领域中常见的技术词汇。在发送端把**基带信号**（包含传输信息的有效信号）加载到某个**载波**（通常为高频的正弦或余弦波）的过程称为**调制**，得到的信号称为**已调信号**。**解调**是**调制**的逆过程，就是在接收端通过某种信号处理手段从**已调信号**中得到**基带信号**。

**双边带幅度调制（DSB-AM）与解调**

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519090734.png)

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519090952.png)

1）基带信号的频谱范围通常很低，有时，甚至零频的能量也不可忽略，而发射天线的尺度与电磁波的波长有关，只有发射天线尺度大于等于 1/4 倍的波长时信号才能有效传输，对于十几千赫兹的信号，发射天线都都要十几公里。这在工程上是不切实际的；

2）调制能够实现频谱搬移，将低频信号搬移到高频处，这能够降低发射天线的尺度；

3）低频频带窄，都用低频传输，会造成堵塞，调制能够扩宽传输频带，提高了频率利用率；

4）调制能够将多路基带信号加载到频率不同的载波上，完成信号的频率分配，使多路信号互不干扰地在同一个信道上传输，实现频分复用；

5）调制还可以减弱噪声和降低干扰。

我们知道，可以用振幅、频率和相位来描述一个波，因此，调制的方式也可分为调幅、调频、调相。

**16-QAM（正交幅度调制）**

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519100555.png)

16 QAM 星座图，每个蓝点代表一组 I 和 Q，对应一组 A 和φ，也即对应了一个波形，总共 16 种组合，也就是携带了 4bit 信息。

3）**数字通信系统结构**

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519084556.png)

相比于普适性通信系统结构，数字通信系统结构除了增加了**对数字信号的调制和解调**，还多了**信源与信道的编码与译码**，以及**加密和解密**过程。

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519084608.png)

- 信源编码与译码的目的：提高信息传输的效率，完成模/数转换；其中信源编码的任务是将信息转换成二进制数据，并进行适当的数据压缩。
- 信道编码与译码的目的：增强抗干扰能力，其中信道编码的意义是检错并纠错。
- 加密与解密的目的：保证所传信息的安全；
- 数字调制与解调的目的：形成适合在信道中传输的带通信号。

在数字调制与解调的过程中，主要是基带调制+载波调制与载波解调+均衡判决。
其中载波调制：把基带信号映射为带通信号的过程，这个带通信号以频率 fc 为载波。

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519091244.png)

其中基带信号指幅度在零/低频处不全为零，在高频处为零；带通信号指在以 f = fc 为中心的一个频带内幅度不全为零，其中载波频率 fc>>0。
载波调制的原因：满足天线发射的要求，并且利于频率资源的利用。

#### 通信性能的衡量指标

1）**有效性**  
① 码元（符号）传输速率 RB：单位时间传送码元的数目，单位为波特，简记为 B  
② 信息（比特）传输速率 Rb：单位时间内传递的平均信息量或比特数，单位为比特/秒，简记为 b/s，或 bps  
③ 频带利用率：单位带宽（1 Hz）内的传输速率  
2）**可靠性**

### 信道

通常是指以传输媒质为基础的信号通道，是通信系统的重要组成部分

1）**恒参信道**：信道参数在通信过程中基本不随时间变化的信道。如有线信道和部分无线信道（微波视距中继、卫星链路等）

2）**随参信道**：信道参数随时间变化的信道。如部分无线信道（短波电离层反射、地面波、散射信道、移动通信等）

① **随参信道特性**：  
- 信号的传输幅度衰减随时间而变化  
- 信号的传输时延随时间而变化  
- 信号经过多条路径到达接收端，各路径的引起的幅度衰减和时延均不同，且均随时间而变化，即出现多径传输现象

② **信道的平坦衰落和频率选择性衰落**  
- 频率非选择性衰落（平坦衰落）：信号带宽 < 相干带宽  
- 频率选择性衰落：信号带宽 > 相干带宽  
③ **信道频谱展宽**：多普勒（Doppler）频移

④ **信道的慢衰落和快衰落**  
- 慢衰落：符号周期 < 相干时间  
- 快衰落：符号周期 > 相干时间  
△ **多径衰落信道的四种衰落特性归纳（重点）**：

### 信道的容量

1）**信息的定义**：（香农给出的定义是）不确定性的减小  
2）**熵的定义**：用随机变量 X 来描述信息，设 X 是一个离散随机变量，它可以取 M 个可能值{x 1,x 2,…,xm}，设 X 取 xi 的概率为 p(xi)，则把 X 的平均不确定性（即熵）定义为：
$$

H(X)=-\sum_{i=1}^{M} p\left(x_{i}\right) \log p\left(x_{i}\right)

$$
3）**互信息**：
$$

I(X ; Y)=H(X)-H(X \mid Y)

$$
4）**离散无记忆信道的容量**：
$$

C=\max _{\left\{P_{X}(x)\right\}} I(X ; Y)

$$
5）**带宽有限、平均功率有限的高斯白噪声连续信道的容量**：
$$

C=\mathrm{W} \log _{2}\left(1+\frac{S}{N}\right) \quad \text { bit } / s

$$
其中 S 为信号平均功率，N 为噪声功率，W 为信道带宽。

设噪声单边功率谱密度为 NO，即 $N=N 0 * W$ ，则带宽有限、平均功率有限的高斯白噪声连续信道的容量可以表示为:
$$

C=\mathrm{W} \log _{2}\left(1+\frac{S}{N_{0} \mathrm{~W}}\right) \quad \text { bit } / s

$$
(1) 当信号功率 S 趋于无穷大时，连续信道的容量趋于无穷大；
(2) 当噪声功率 $\mathrm{A}$ 趋于零时，连续信道的容量趋于无穷大;
$$
\frac{S}{N_{0}} \log _{2} e \approx 1.44 \frac{S}{N_{0}}
$$
(3) 当信号带宽 W 趋于无穷大时，连续信道的容量等于
$$
\frac{S}{N_{0}} \log _{2} e \approx 1.44 \frac{S}{N_{0}}
$$

### 奈奎斯特准则

**奈奎斯特第一准则**

发信端发出的信号经过信源编码、信道编码过程后，原始信号转换成了二进制序列，然后根据需要把这些二进制序列按照 $k$ 个比特这样划分成一组（比如说，如果我们以 2 个比特为一组），称为一个**码元**。

在接收端，通过解调之后，就恢复成了低频的连续模拟信号，然后以 $T_{s}$ 的采样时间间隔对这个模拟信号采样，根据采样的值，来判断它是哪一个码元。那么，如果某些抽样时刻 $[t_{i},..]$ 抽样得到的模拟信号的值不幸受到了其他码元的干扰，那么我们就称这叫做产生了 "码间串扰"。

根据奈奎斯特第一准则可知，在理想带限信道, 带宽为 $B$ 的信道上传送码元时，要想实现无码间串扰，码元速率 $R_{s}$ 不能超过 2 倍的带宽。即： $R_{s} \leq 2 B$ ，要达到最高传输速率 (奈奎斯特速率) $2 B$ ，必须使用带宽为 $B$ 的理想低通滤波器进行滤波。

[参考：奈奎斯特第一准则](https://blog.csdn.net/weixin_44586473/article/details/104372110)

**奈奎斯特第二准则**

转换点无失真准则，或无抖动（JitterFree）准则。

转换点无失真。有控制地在某些码元的抽样时刻引入码间干扰，而在其余码元的抽样时刻无码间干扰，就能使频带利用率达到理论上的最大值，同时又可降低对定时精度的要求。通常把满足奈奎斯特第二准则的波形称为部分响应波形。利用部分响应波形进行传送的基带传输系统称为部分响应系统。

**奈奎斯特第三准则**

波形面积无失真准则。

脉冲波形面积保持不变。即如果在一个码元间隔内接收波形的面积正比于发送矩形脉冲的幅度，而其他码元间隔的发送脉冲在此码元间隔内的面积为零，则接收端也能无失真地恢复原始信码。

### 香农定理

- 香农第一定理（可变长无失真信源编码定理)

一段信息的信息量是固定的，这称为这段信息的信息熵（H）。

$$

H(X)=-\sum_{i=1}^{n} p\left(x_{i}\right) \log p\left(x_{i}\right)

$$

无论怎么压缩，信息熵是无失真信源编码的极限值。若编码的平均码长小于信息熵值，必然发生差错（也就是有损）。

香农第一定理指出，对于不同的符号要采用不同编码，经常出现的符号使用短的编码，出现频率低的使用更长的编码。如果做到每个符号的代码长度等于它出现概率的对数，则编码总长度就是信息熵。

- 香农第二定理（有噪信道编码定理）

有噪信道编码定理指出，尽管噪声会干扰通信信道，但还是有可能在信息传输速率小于信道容量的前提下，以任意低的错误概率传送数据信息。

$$

C=B * \log (1+S / N)

$$
$B$ 为信道带宽； $S / N$ 为信噪比，通常用分贝（dB) 表示。从这个公式中，我们也可以得知:
信噪比越大（也就是信号比例越大），容量也越大。
当噪声很大（例如极限情况，无限大），那么信噪比接近 0，C 的结果为 0。也就是说，噪声太大没法传输任何信号。
同时香农指出，传输率永远都不可能超过信道容量 $\mathrm{C}$

例如当你网络频段带宽有 $10 \mathrm{MHz}$ ，假设你离路由器3米时，信噪比 $S / N=63$ ,那么这时候容量 $C$ 为 $10^{*} \log (1+63)=$ 80Mbit/s。但如果你把距离增加到9米，这时候，信噪比 $S / N$ 会减少到 7 ，这时候容量 C 为 $100 * \log (1+7)=30 \mathrm{Mbit} / \mathrm{s}$ 。（以上计算底数为 2 ) 你就会明显感到网速下降了。(所以有时候你觉得你网速慢，并不一定是带宽被偷工减料了，而是噪声太多)

从香农第二定理我们可以看到，两个增加信道容量的路径为：增加带宽、增加信噪比

- 香农第三定理（保失真度准则下的有失真信源编码定理）

总能找到一种有效的编码方法，让信息的传输率接近信道容量时而不出错。

香农同时也在这个定理指出，试图以超越信道容量 C 的传输率来传输信息，那么无论如何编码，都必定出错。

### 光通信

光数据传输从最简单、最经济的数字编码方案开始：归零 (RZ) 和非归零 (NRZ) 开关键控 (OOK)。在理想的情况下，信号是一系列的 “1”（通电）和 “0”（断电）。当传输速率达到 40 Gb/s 时，这一概念就面临了极限。在这个速率以上的话，频谱加宽的信道开始与相邻信道重叠，导致调制信息产生串扰和质量下降。于是业界转为寻求更复杂的调制方案，如正交相移键控 (QPSK)，以减少 OOK 方案中出现的色散减损。

#### 光的偏振

光的干涉和衍射现象说明了光具有**波动性**。振动方向对于传播方向的不对称性叫做偏振，它是横波区别于纵波的一个最明显的标志，

横波的振动方向和波的传播方向垂直。假如使得横波穿过一个栅栏，波的传播就会受到栅栏的限制。如果栅栏缝隙的方向与振动方向一致，波能顺利通过栅栏。如果缝隙方向与振动方向垂直，波就被阻挡而不能继续向前传播。

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519095506.png)

而纵波的振动沿着波的传播方向，栅栏或类似的障碍无论在哪一个方向，都不会阻止波的传播。因此只有横波才有偏振现象，光的偏振和光学各向异性晶体中的双折射现象也进一步证实了光的横波性。

##### 偏振复用

偏振复用就是将激光器发出的光通过偏振分束器分裂成两束，这两束光可以分别进行调制，由于偏振方向垂直，不会发生干涉。

但是由于光在光纤中传输时，偏振方向可能发生改变，导致偏振方向不再严格垂直，产生偏振损耗。在激光器到光调制器之间的光路上，必须使用保偏光纤，保证光的偏振度，避免对非偏振的部分进行调制。在光纤中远距离传输时，必然会产生一定的偏振损耗。

##### 相干检测

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519103134.png)

由于乘以一个本振光的原因，接收信号与本振光相乘之后得到的信号中，带有幅度、频率、相位信息，因此无论何种调制方式，在这种通信系统中都可以使用。**这与直接检测只能检测幅度信息，是有天壤之别的。** 而且本振光的大功率，也大大提高了接收机的灵敏度。

#### 载波干扰

子载波间的干扰就是子载波间的正交性被破坏了。

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519104450.png)

在要发送的符号间加入了保护间隔避免了多径效应引起的符号间干扰，且这里假设多经时延等于保护间隔的长度。

我们知道，符号是要调制子载波后得到已调信号，之后再发送出去的，（这里同样省略了射频调制的过程），本身符号 s 1 与符号 s 3 对应的调制子载波是相互正交的，见下图：

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519104517.png)

二者子载波间相乘在积分为 0；

但符号 s 1 调制频率为 f 0 的子载波后经过第一径发送出去，符号 s 3 调制频率为 2 f 0 的子载波后经过第二径发送出去，二者的子载波间的关系如下：

![]({25}_Terabit%20 Faster-Than-Nyquist%20 PDM%2016-QAM%20 WDM%20 Transmission%20 With%20 a%20 Net%20 Spectral%20 Efficiency%20 of%207.96%20 b_s_Hz@zhuTerabitFasterThanNyquistPDM 2018.assets/image-20220519104540.png)

易知，二者相乘后积分不在为零，这就是说二者之间不满足正交性了。

这就是为了解决多径效应引起的码间干扰而添加保护间隔后破坏了子载波间的正交性，也就是引起了子载波间的干扰。



### 引文

## 摘录
