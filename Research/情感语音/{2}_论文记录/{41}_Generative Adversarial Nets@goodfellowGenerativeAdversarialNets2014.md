---
title: "Generative Adversarial Nets"
description: ""
citekey: goodfellowGenerativeAdversarialNets2014
author: "石昌文"
tags: [""]
categories: "PaperNote"
keywords:  [""]
draft: true
layout: "blog"
date: 2023-02-15 14:35:10
lastmod: 2023-04-11 13:02:49
---

> [!info] 论文信息
>1. Title：Generative Adversarial Nets
>2. Author：Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio
>3. Entry：[Zotero link](zotero://select/items/@goodfellowGenerativeAdversarialNets2014) [URL link](https://papers.nips.cc/paper/2014/hash/5ca3e9b122f61f8f06494c97b1afccf3-Abstract.html) [PDF link](<file:///C\:\\Users\\19115\\OneDrive - stu.suda.edu.cn\\Zotero\\Goodfellow et al_2014_Generative Adversarial Nets.pdf>)
>4. Other：2014 - Advances in Neural Information Processing Systems  Curran Associates, Inc.   -   

>- :luc_github: 论文实现：
>- :luc_external_link: 论文解读：[深度学习：生成式对抗网络，让机器在博弈中实现“自我成长” - 前沿洞察 - 恒生研究院 (hundsun.com)](https://rdc.hundsun.com/portal/article/920.html)
>- :luc_linkedin: 相关笔记：***

## ⭐ 重点

- 

## 摘要

> [!abstract] We propose a new framework for estimating generative models via adversarial nets, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G. The training procedure for G is to maximize the probability of D making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions G and D, a unique solution exists, with G recovering the training data distribution and D equal to 1/2 everywhere. In the case where G and D are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples. Experiments demonstrate the potential of the framework through qualitative and quantitatively evaluation of the generated samples.

> 本文提出了一个通过对抗过程评估（ estimating）生成式模型的新框架。在此框架中，通过同时训练两个模型：一个用来捕获数据分布的生成模型 G，以及一个估计样本是否来自训练数据概率的判别模型 D（注意： G 的训练过程是最大化 D 出错的概率）。该框架类似于（corresponds to）一个最小最大化的博弈过程（two-player game）。对于任意的生成函数 G 和判别函数 D 的解空间，存在唯一解，即生成模型 G 能够恢复（模拟）训练数据分布，而判别模型 D 的输出恒等于$1/2$。如果 G 和 D 都定义为多层感知机，则整个系统可以通过反向传播算法进行训练。在此框架中，无论是在训练阶段，或是样本生成阶段，不需要任何马尔可夫链或滚动展开的近似推理网络（approximate inference net）。本文的实验部分，通过对 G 生成的样本数据，进行了定性和定量评估，证明了框架的潜力。

## 预处理

## 概述

## 结果

## 精读

引言

深度学习的前景是（人们寄希望于利用深度学习）发现表达能力丰富的，拥有层次化结构的模型[2]，并通过这些模型来表达人工智能应用中遇到的各种数据的概率分布，如图像数据、包含语音的波形数据和自然语言语料库中的符号。到目前为止，深度学习中最引人注目的成功领域(应用最广泛的领域)包括判别模型（discriminative models），该类模型通常是将那些高维、丰富的感官输入（sensory input）映射到类别标签上[14，20]。深度学习应用的成功主要是基于反向传播算法和随机神经元抑制算法（Dropout Algorithm），并且这两种算法都使用了具有特别良好的梯度表现的分段线性单元[17，8，9]。相反的，深度生成类模型（generative models）的影响力较小，原因有二：第一是很难近似极大似然估计和其他相关策略中出现的许多棘手的概率计算，第二是因为很难在生成类模型中充分利用利用分段线性单位的好处。我们提出了一种新的生成类模型估计方法来避开这些困难。


在本文所提出的对抗网络框架中，包含两个模型：生成类模型；以及确定样本是来自模型生成分布还是来自真实数据分布的判别模型。生成类模型可以被想象为类似于一群造假者，试图制造假币并在不被发现的情况下使用，而识别类模型则类似于警察，试图检测假币。这个游戏中双方的竞争会驱使双方改进他们的方法，直到仿冒品与正品无法辨别。

该训练框架可以为多种模型和优化算法产生特定的训练算法。本文探讨了一种特例：通过多层感知器向生成类模型传递随机噪声，让其产生样本数据；同时识别类模型也是一个多层感知器（multilayer perceptron）。我们将这种特殊情况称为对抗网络（adversarial nets.）。在这个例子中，我们可以只使用非常成熟的反向传播算法和随机神经元抑制算法来训练这两个模型[16]，并且生成模型生成样本数据的过程只使用前向传播来训练。整个模型训练过程不需要依赖于近似推论（approximate inference）或马尔可夫链（Markov chains）。

相关工作

直到最近，大多数生成类模型工作都聚焦在已经给定概率分布函数参数说明的模型上。然后通过最大化对数似然概率来训练该模型。在这类模型中，最成功的是深度玻尔兹曼机（Boltzmann machine）[25]。这类模型通常具有难以处理（非常棘手）的似然函数，因此需要大量的似然梯度估计。这些困难推动了“generative machines 生成式机器”模型的发展。生成式机器，不显示地表示可能性（概率分布），但能够从我们期望的分布中生成样本数据。生成式随机网络[4]就是生成式机器的一种，它可以用精确的反向传播来训练，而不像用Boltzmann机器训练那样需要大量近似估算。本文的工作通过不再使用生成随机网络中的马尔科夫链，进一步扩展了生成机的概念。

在本文的工作中，梯度的反向传播是通过生成式过程实现的，其中梯度计算公式如下：

$$
\lim _{\sigma \rightarrow 0} \nabla_{\boldsymbol{x}} \mathbb{E}_{\epsilon \sim \mathcal{N}}\left(0, \sigma^{2} \boldsymbol{I}\right) f(\boldsymbol{x}+\epsilon)=\nabla_{\boldsymbol{x}} f(\boldsymbol{x})
$$

在进行本文研究工作时，我们并不知道 Kingma、Wling[18]和Rezende等人[23]已经研究出了更加通用的随机反向传播规则，该规则使得模型能够在有限方差范围内，使用高斯分布来进行梯度的反向传播，并向后传播到协方差参数和平均值。
同时，这些反向传播规则使得模型能够学到生成器的条件方差，而在我们的研究中则把条件方差当做了超参数。在Kingma和Welling[18]，以及Rezende et al[23]的研究中，他们还使用随机反向传播规则来训练可变自编码器(VAEs)。和生成式对抗网络类似，VAE把一个可微的生成网络和另外一个神经网络打包成网络组。不过和GAN不同的是，VAE中的第二个神经网络是一个识别模型，用于执行一些近似推理任务。GAN需要在可视单元可导（GAN需要通过可见单元进行区分），因此不能用于对离散数据建模；而VAE需要隐藏层单元可导（进行区分），因此模型中不能包含有离散值的隐含变量。其他类似VAE的方法也有很多，详见[12,22]，不过这些方法跟本文所研究的方法关联不大，因此不再深入讨论。


在之前的工作中，也有采用了使用判别准则来训练生成模型的方法 [29, 13]。但是这些研究中使用的标准，深度生成类模型通常难以处理（套用）。甚至这些方法，即使使用深度模型也很难近似，因为它们涉及的概率比率不能使用可变近似值的方法来近似。噪声对比估计 (NCE) [13] 方法是通过学习到能够使模型可用于从固定噪声分布中区分数据的权重参数，来训练生成模型。如果使用先前训练的模型作为噪声分布数据源，有助于训练提高模型的性能。这种方式可以视为是一种非正式的竞争机制，其思想和对抗式网络使用的正式竞争类似。 NCE 方法的关键限制是它的“判别器”是由噪声分布和模型分布的概率密度之比定义的，因此需要能够通过对这两种概率密度进行评估和反向传播。

还有一些研究使用了一般意义上的神经网络对抗概念。最相关的（最具代表性的）研究就是可测性最小化模型(predictability minimization)[26]。在可测性最小化模型中，第一个神经网络的每一个隐藏层神经元经训练之后，使其与第二个神经网络的输出保持不同，而第二个神经网络的目标就是在给定所有其他隐藏层神经元的值的情况下，预测该隐藏单元的值。本文的工作在三个重要方面不同于可预测性最小化：
1）在本文的工作中，网络之间的竞争是唯一的训练标准，并且其本身就足以支持训练整个网络。可测性最小化模型只是一个正则化器，它会对神经网络的隐藏层单元施加某种约束，从而使的隐藏层单元在满足其他任务的同时，又保持统计上的独立性；这不是主要的培训标准。 
2）竞争本质不同。在可测性最小化模型中，，两个网络的输出要进行博弈，其中一个网络的目标是两个网络的输出相似，而另外一个网络的目标则是使得两个网络的输出不同。网络的输出值均是标量值。在生成式对抗模型中(GAN)，一个网络用于生成高维向量，并将其作为第二个网络的待输入项，然后选定一个输入送入第二个网络，而此时第二个网络对于所输入的数据并不知情
3）学习过程不同。可测性最小化模型是一个优化问题，其目标是将目标函数优化到最小值点。 GAN 基于最大最小的博弈问题而不是优化问题。在其训练过程中存在一个值函数，一个网络寻求最大化这个值函数，而另一个网络寻求最小化这个值函数。整个博弈过程会在一个鞍点处终止，该鞍点对于其中一个网络而言是最小值点，而对于另一个网络的而言是最大值点。

生成式对抗网络有时候也会和“对抗样本（adversarial examples）”这个概念混淆[28]。对抗样本是通过直接在分类网络的输入上使用基于梯度的优化（故意添加细微的干扰）来找到的样本数据，即其目的是找到与输入样本数据相似，却被错误分类的样本数据。这与本文提出的工作不同，因为对抗样本不是一种训练生成式模型的机制。相反，对抗样本主要是一种分析工具，用于探索神经网络本身的一种奇特的行为方式：即使两张图像之间的差异对于人类观察者来说是察觉不到的，但是神经网络通常会自信地以高置信度对两张图像进行不同的分类。这种对抗性样本的存在确实表明生成对抗式网络的训练可能效率低下，因为这表明可以使现代判别模型，能够在不模拟任何人类可感知的类别属性情况下，就能高置信度地识别一个类。

对抗网络

当生成式模型都是多层感知机时，对抗式建模框架最容易应用。为了让生成器学到关于输入数据 $x$ 上的分布 $p_{g}$，我们对输入噪声变量定义了一个先验值 $p_{\boldsymbol{z}}(\boldsymbol{z})$ ，然后将其映射到数据空间 $G\left(\boldsymbol{z} ; \theta_{g}\right)$中，其中 $G$ 是一个可微函数，代表以 $\theta_{g}$ 为参数的多层感知机。我们还定义了第二个多层感知机 $D\left(x;\theta_{d}\right)$，用来输出单个标量值。 $D(x)$ 表示 $x$ 来自真实样本数据而不是生成数据分布 $p_{g}$ 的概率。最终训练判别器 $D$ 以最大化判别来自 $G$ 的训练示例和真实数据样本的概率。同时训练生成器 $G$ 以最小化 $\log (1-D(G(z)))$。换句话说，$D$ 和 $G$ 训练过程就是一个使用下面的价值函数 $V(G, D)$ 的最大最小化博弈游戏。

$$
\min _{G} \max _{D} V(D, G)=\mathbb{E}_{\boldsymbol{x} \sim p_{\text {data }}(\boldsymbol{x})}[\log D(\boldsymbol{x})]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}(\boldsymbol{z})}[\log (1-D(G(\boldsymbol{z})))]
$$


在下一部分中，我们将介绍对抗网络的理论分析，基本上表明这个博弈训练准则能够让生成模型 $G$ 恢复出样本数据分布（即生成模型G学习到了输入样本数据的分布函数，从G中恢复的数据能够做到以假乱真的效果），并且判别器 $D$ 也能够有足够的判别能力（如不对 D 做任何参数限制）。有关该方法的不太正式、更具教学性的解释，请参见图 1。
在实际实践中，我们必须以迭代式的数值方法来实现博弈过程。在训练周期的内循环中优化判别模型 $D$ ，其计算成本令人望而却步，并且在有限的数据集上会导致模型过拟合。相反，另一种替代方案是轮流的优化判别模型$D$和生成式模型$G$。具体来说就是每对判别器模型D进行k步优化之后，然后开始对生成模型G进行单步优化，并一直轮流交替下去直至收敛。这种方案的好处在于只需生成式模型 $G$ 变化足够缓慢，判别模型 $D$ 就会一直保持在其最优解位置。该过程在算法 $1$ 中正式提出。

在实践中，上述价值函数提供的梯度信息并不足以令生成模型 $G$ 很好地学习。在学习的早期，生成模型 $G$ 性能很差时，判别模型 $D$ 可以以高置信度拒绝生成样本，因为它们与训练数据有明显的不同。在这种情况下，$\log (1-D(G(z)))$ 饱和。与其训练生成模型 $G$ 来最小化 $\log (1-D(G(z)))$，反倒不如训练生成模型 $G$ 来最大化 $\log D(G(\boldsymbol{z}))$。这一目标函数的改变不会对 $G$ 和 $D$ 的训练结果产生影响，但在学习早期能够提供了更丰富的梯度信息。


理论

生成模型 $G$ 隐含地定义了一个概率分布 $p_{g}$ ，在 $z \sim p_{z}$ 的条件下，该分布就是生成器输出的样本 $G(z)$ 的分布。因此，如果给定足够的容量和训练时间，我们希望能够使用算法 1 获得一个可以收敛到 $p_{\text {data }}$ 的估计器。本部分的结果，是在非参数设置中完成的，例如我们通过研究概率密度函数空间中的收敛性来表示具有无限容量的模型。

我们将在 $4.1$ 中展示这个 minimax 博弈，将对于 $p_{g}=p_{\text {data }}$ 有一个全局最优值。然后我们将在第 4.2 节中展示算法 1 优化了 Eq 1 ，从而获得了预期的结果。


全局最优值

给定任意生成器 $G$ ，我们首先考虑如何得到最佳判别器 $D$。

问题一：对于某一个固定的生成器 $G$，最优判别器 $D$ 可以表示为 $$ D_{G}^{*}(\boldsymbol{x})=\frac{p_{\text {data }}(\boldsymbol{x })}{p_{\text {数据}}(\boldsymbol{x})+p_{g}(\boldsymbol{x})} $$


证明：对于给定的任意生成器 $G$，判别器 $\mathrm{D}$ 的训练标准是最大化函数 $V(G, D)$ 
$$

\begin{aligned}

V(G, D) &=\int_{\boldsymbol{x}} p_{\text {data }}(\boldsymbol{x}) \log (D(\boldsymbol{x})) d x+\int_{z} p_{\boldsymbol{z}}(\boldsymbol{z}) \log (1-D(g(\boldsymbol{z}))) d z \\

&=\int_{\boldsymbol{x}} p_{\text {data }}(\boldsymbol{x}) \log (D(\boldsymbol{x}))+p_{g}(\boldsymbol{x}) \log (1-D(\boldsymbol{x})) d x

\end{aligned}

$$ 
对于任意 $(a, b) \in \mathbb{R}^{2} \backslash\{0,0\}$，函数$y \rightarrow a \log (y)+b \log (1-y)$ 在点 $\frac{a}{a+b}$ 处达到值域在 $[0,1]$ 的最大值。判别器不需要在$\operatorname{Supp}\left(p_{\text {data }}\right)\cup\operatorname{Supp}\left(p_{g}\right)$之外定义。

注意判别模型 $D$ 的训练目标可以理解为最大化条件概率$P(Y=y \mid x)$ 的对数似然估计，其中 $Y$ 表示输入 $x$ 是否来源于$p_{\text {data }}$ （即 $y=1$ ）或来自 $p_{g}$ （即 $y=0$ ）。则前文方程中的最小最大化算法现在可以重新表述为： 

$$

\begin{aligned}

C(G) &=\max _{D} V(G, D) \\

&=\mathbb{E}_{\boldsymbol{x} \sim p_{\text {data }}}\left[\log D_{G}^{*}(\boldsymbol{x})\right]+\mathbb{E}_{\boldsymbol{z} \sim p_{\boldsymbol{z}}}\left[\log \left(1-D_{G}^{*}(G(\boldsymbol{z}))\right)\right] \\

&=\mathbb{E}_{\boldsymbol{x} \sim p_{\text {data }}}\left[\log D_{G}^{*}(\boldsymbol{x})\right]+\mathbb{E}_{\boldsymbol{x} \sim p_{g}}\left[\log \left(1-D_{G}^{*}(\boldsymbol{x})\right)\right] \\

&=\mathbb{E}_{\boldsymbol{x} \sim p_{\text {data }}}\left[\log \frac{p_{\text {data }}(\boldsymbol{x})}{P_{\text {data }}(\boldsymbol{x})+p_{g}(\boldsymbol{x})}\right]+\mathbb{E}_{\boldsymbol{x} \sim p_{g}}\left[\log \frac{p_{g}(\boldsymbol{x})}{p_{\text {data }}(\boldsymbol{x})+p_{g}(\boldsymbol{x})}\right]

\end{aligned}

$$

定理一：当且仅当 $p_{g}=p_{\text {data }}$ 时，达到训练准则 $C(G)$ 的全局最小值。此时，$C(G)$ 的值为 $-\log 4$。

证明：当 $p_{g}=p_{\text {data }}，D_{G}^{*}(x)=\frac{1}{2}$。因此 $C(G)=\log \frac{1}{2}+\log \frac{1 }{2}=-\log 4$。这就是 $C(G)$ 的最小值，并且仅在 $p_{g}=p_{\text {data }}$ 可以达到。

$$
\mathbb{E}_{\boldsymbol{x} \sim p_{\text {data }}}[-\log 2]+\mathbb{E}_{\boldsymbol{x} \sim p_{g}}[-\log 2]=-\log 4
$$

如果 $C(G)=V\left(D_{G}^{*}, G\right)$ 时，可以得到

$$

C(G)=-\log (4)+K L\left(p_{\text {data }} \| \frac{p_{\text {data }}+p_{g}}{2}\right)+K L\left(p_{g} \| \frac{p_{\text {data }}+p_{g}}{2}\right)

$$

其中 KL 是 Kullback-Leibler 散度。同时如果将其表示为模型真实数据分布和数据生成过程之间的 Jensen Shannon 散度，可以得到： 

$$

C(G)=-\log (4)+2 \cdot J S D\left(p_{\text {data }} \| p_{g}\right)

$$

因为两个分布之间的 Jensen-Shannon 散度总是非负的，并且当两个分布相等时为零，所以我们已经证明 $C^{*}=-\log (4)$ 是$C(G)$ 的全局最小值，且唯一的解决方案是 $p_{g}=p_{\text {data }}$，即生成模型完美地复制了真实数据分布。

算法的收敛性

问题二：如果 $G$ 和 $D$ 有足够的能力；在算法的每一步，给定 $G$ 的情况下，判别器都能达到其最优值； $p_{g}$ 会一直更新以改进标准 $$ \mathbb{E}_{\boldsymbol{x} \sim p_{\text {data}}}\left[\log D_{G}^{*}(\boldsymbol{x})\right]+ \mathbb{E}_{\boldsymbol{x} \sim p_{g}}\left[\log \left(1-D_{G}^{*}(\boldsymbol{x})\right)\right] $$那么 $p_{g}$ 就会收敛到 $p_{\text {data }}$ 


证明：如上文所述准则中所做的那样，将 $V(G, D)=U\left(p_{g}, D\right)$ 视为 $p_{g}$ 的函数。注意 $U\left(p_{g}, D\right)$ 是 $p_{g}$ 的凸函数。凸函数的上确界的次导数为函数最大值点的导数。换句话说，如果 $f(x)=$ $\sup _{\alpha \in \mathcal{A}} f_{\alpha}(x)$ ，并且对于任意 $\alpha$， $f_{\alpha}(x)$ 为 $x$ 的凸函数。那么当 $\beta=\operatorname{arg~sup}_{\alpha \in \mathcal{A }} f_{\alpha}(x)$ 时， $\partial f_{\beta}(x) \in \partial f$ 。这相当于在给定 $G$ 的情况下，为了获得最优 $D$ ，所需要计算的 $p_{g}$ 的梯度下降更新值。 $\sup _{D} U\left(p_{g}, D\right)$ 在 $p_{g}$ 中是凸的，具有唯一的全局最优值，因此 $p_{g }$ 的更新步长足够小的情况下，$p_{g}$ 可以收敛到 $p_{x}$。


实际上，对抗网络只能通过函数 $G\left(z ; \theta_{g}\right)$ 表示有限的 $p_{g}$ 分族，因此我们只能优化 $\theta_{g}$ 而不是 $p_{g}$ 本身，所以以上证明并不适用。然而，多层感知器在实践中的出色表现表明，尽管缺乏理论保证，它仍是一个设计合理的模型。


我们在一系列的数据集上训练了对抗网络，包括 MNIST [21]、Toronto Face Database (TFD) [27] 和 CIFAR-10 [19]。生成器网络 G 使用了修正的线性激活函数 [17, 8] 和 sigmoid 激活函数，而判别器网络仅使用了 maxout [9] 激活函数。同时训练判别器网络时， 我们还使用了Dropout [16] 技巧。虽然我们的理论框架允许在生成器的中间层使用 dropout 和其他噪声，但在实际训练中我们仅使用了噪声作为生成器网络最底层的输入信号。

我们通过对 $G$ 生成的样本数据使用 Gaussian Parzen 窗口估计，报告了生成样本分布相对于 $p_{g}$ 的对数似然率， 同时将其作为估计测试集数据的概率估计值。Gaussians的 $\sigma$ 参数是通过对验证集的交叉验证获得的。这种估计似然率的方法具有较高的方差，并且在高维空间中表现不佳，但它是我们所知的最佳方法。在一些研究中，通过采样来获取似然率值，直接推动了对如何评估此类模型的进一步研究。在图中，我们展示了一些经过训练的生成器网络所生成的样本数据。虽然我们没有声称这些样本比现有方法生成的样本更好，但我们相信这些样本至少与文献中更好的生成模型具有竞争力，并突出了对抗框架的潜力。

Advantages and disadvantages

相对于以前的建模框架，这个新框架具有优点和缺点。缺点主要是  $p_{g}(x)$  没有明确的表示，并且在训练期间 D 必须与 G 很好地协调（ G 在不更新 D 的情况下不能训练太多，以避免“Helvetica scenario”现象。即 G 会为了具有足够的多样性来建模  $p_{data}$，将很多输入的初始 z 信号，都塌缩为到同一个 x 处）。就像玻尔兹曼机器的负链必须在学习步骤之间保持最新一样。优点是永远不需要马尔可夫链，只使用反向传播来获得梯度，学习过程中不需要推理，模型中可以包含各种各样的函数。表 2 总结了生成对抗网络与其他生成建模方法的比较。上述优势主要是计算上的。对抗模型也可能从生成器网络中获得一些统计优势，而不是直接使用数据示例更新，而只是使用流经鉴别器的梯度。这意味着输入的组件不会直接复制到生成器的参数中。对抗网络的另一个优点是它们可以表示非常尖锐甚至退化的分布，而基于马尔可夫链的方法要求分布有些模糊，以便链能够在模式之间混合。

相对之前的建模框架来说, 本文所提出的新框架既有优点又有劣势。最主要的劣势有二: 其一是该框架没有给出一个明确的ú $($ غ्ष $)$ 的表达; 其二是 $D$ 和 $G$ 的训练要达到宽泛意义的同步（所谓宽泛意义上的同步是指: G 网络不能训练的太快, 要低于 $D$ 网络的训练节奏, 即要在训练多步 $D$ 的情况下, 才训练一步 $G$ 。如果不能满足 $G$ 和 D 之间的宽泛同步, 那么训练过程就会陷入 Helvetica Scenario 情形, 即模型 $G$ 会把很多输入 曼机的负链机制相似, 即在玻尔兹曼中负链必须在每一步的学习更新中, 都时刻保持最新状态。对抗网络的主要优势有三：其一在于其放弃了对马 尔科夫链的依赖; 其二是网络仅需要进行梯度的后向传播, 在学习期间不再需要推理; 其三是模型支持更加多样性的函数。表二中总结了生成对抗 网络与其他生成模型方法的对比。



图 1：图中，判别分布（$D$，蓝色，虚线）是输入数据是否归属于真实数据分布（黑色，虚线）$p_{x}$ 的概率分布。同时，它也被用来训练生成对抗网络，从而得到更拟合的生成数据分布 $p_{g}$ (G)（绿色，实线）。最下面的水平轴是从中采样 $z$ 的域，在这种情况下是均匀的。上面的水平线是 $x$ 域的一部分。向上的箭头显示了映射 $x=G(z)$ 如何将非均匀分布 $p_{g}$ 施加到转换后的样本上。 $G$ 在高密度区域收缩，在 $p_{g}$ 的低密度区域膨胀。 (a) 考虑一个接近收敛的对抗对：$p_{g}$ 类似于 $p_{\text {data }}$，$D$ 是一个部分准确的分类器。 (b) 在算法的内部循环中，$D$ 被训练来区分样本和数据，收敛到 $D^{*}(\boldsymbol{x})=$ $\frac{p_{\text {data }} (\boldsymbol{x})}{p_{\text {数据}}(\boldsymbol{x})+p_{g}(\boldsymbol{x})}$。 (c) 更新到 $G$ 后，$D$ 的梯度引导 $G(\boldsymbol{z})$ 流向更有可能被分类为数据的区域。 (d) 经过几个步骤的训练，如果 $G$ 和 $D$ 有足够的容量，它们将达到一个点，因为 $p_{g}=p_{\text {data }}$，它们都无法提高。判别器无法区分这两个分布，即 $D(x)=\frac{1}{2}$。

### 引文

## 摘录
