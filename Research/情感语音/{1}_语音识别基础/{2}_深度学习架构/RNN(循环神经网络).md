---
title: "RNN(循环神经网络)"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-03-19 14:32:52
lastmod: 2022-04-27 21:15:23
---

# RNN 循环神经网络

当在理解一段序列(语音、文本、视频)的意思时，我们通常并不是只去分析当前时间点的数据，而是会将其连接起来，考虑前后数据的关系。相似的，神经网络中的 RNN 便是用来处理具有序列特性的数据，从中挖掘数据中的时序信息以及语义信息。

回顾全连接网络的结构，如下图所示（仅有一层隐藏层）：

![](RNN(循环神经网络).assets/MLP.svg)

输入向量 $x_{t}$ 通过运算得到隐藏层向量 $h_{t}$ （当前输入向量的表征向量），用来表征其特征，然后继续通过运算分析其特征数据，最终得到输出 $o_{t}$ 。

RNN 网络与全连接网络的一个不同点就是，RNN网络在利用隐藏层向量 $h_{t}$  计算输出结果 $o_{t}$ 的同时，将其保留，提供给下一个输入数据作为参考数据，使其能够获得对应语境信息。

![](RNN(循环神经网络).assets/RNN.excalidraw.svg)
![](RNN(循环神经网络).assets/RNN_unit%202.svg)


上图网络左图为抽象的RNN结构，右图为其按照数据输入的时间顺序来看的时间序列展开图，最下面的图为每单位输入对应的 RNN 计算单元结构。

分析可知，在 RNN 网络结构中，每一时刻的隐藏层向量不仅由该时刻的输入向量决定，还由上一时刻的隐藏层向量决定。

当RNN网络在 $t$ 时刻接收到输入 $x_{t}$ 之后，输入数据 $x_{t}$ 和上层隐藏层向量 $h_{t-1}$ 会分别经由共享权重矩阵 $W_{xh}$ 和共享权重矩阵 $W_{hh}$，计算得到当前状态的隐藏层向量 $h_{t}$ ,由 $h_{t}$ 可以计算输出值 $o_{t}$ 或是继续提供给下一个输入数据 $x_{t+1}$ 做计算。对任意时刻的输入 $x_{i}$ ，共享权重矩阵 $W_{hh}$ 可以记住所有时刻隐藏层向量 $h_{t}$ 提供的信息（ $x_{i}$ 的特征表示信息和语境信息）。其中每个单位时间计算公式如下表示：

$$
\begin{aligned}

&o_{t}=SoftMax\left(W_{ho} \cdot h_{t}+b_{o}\right) \\

&h_{t}=Tanh\left(W_{xh} \cdot x_{t}+W_{hh} \cdot h_{t-1} + b_{h}\right)
\end{aligned}
$$

以上介绍为经典的 RNN 结构，可以理解为一个简单的多对多模型，每输入一个数据就能得到一个输出结果，与此同时此结构也带来了一个隐含要求：输入和输出序列要有相同的时间长度。

因此在RNN结构的发展过程中，其结构设计产生了许多变体，使得 RNN 结构不再局限于 N to N的输入输出，如下所示：

## RNN 基本结构

1. 1 to N
	使用每次RNN结构的输出作为隐藏值 $h_{t}$，为下次输入提供历史信息。需要注意的是，如果是分类任务，输出的类别（单个数值）需要提前将类别元数据进行 [embedding](#^f2c635)或 one-hot 编码，转换成等维度的向量数据，才能与后面的权重矩阵做运算。
	结构问题：一步错，步步错，蝴蝶效应明显。
	解决方法：[Scheduled Sampling](#^d4b30e)
	
	![](RNN(循环神经网络).assets/1toN.svg)
2. N to 1
	![](RNN(循环神经网络).assets/Nto1.svg)
3. N to M
	![](RNN(循环神经网络).assets/NtoM.svg)

以上三种结构是其余一些变体的基本思想，通过互相嵌套或添加一些残差结构、注意力机制等，就可以得到一些目前流行的 RNN 模型。

## GRU 门控循环单元

解决问题：梯度消失或爆炸问题

![image-20220206205332409](RNN(循环神经网络).assets/image-20220206205332409.png)

![image-20220206205925169](RNN(循环神经网络).assets/image-20220206205925169.png)

## LSTM 长短期记忆网络

回顾原始 RNN 结构按输入时间的展开图

![](RNN(循环神经网络).assets/RNN_unit_sequence%202.svg)

从数学上来说，对于任何数值，如果循环乘以略大于1的值，它都会变得越来越大,直至无穷。而深度神经网络的本质运算就是矩阵乘法，每一层网络都是通过乘法相互关联的，因此在实际运算中很容易产生梯度消失或梯度爆炸的问题。梯度爆炸解决起来相对容易，因为它们可以直接被截断或压缩。梯度消失正好相反，是导数数值变得非常小，使计算机无法工作，网络也无法学习。

可以看出，随着 RNN 输入序列长度的增加，权重矩阵 $W_{hh}$ 在训练过程中，记录的前期输入数据的特征信息和语境会慢慢变少，而更多的去存放近期输入数据。

那应该怎样解决因为输入序列太长，导致 RNN 出现记忆模糊的问题？想象一下，当学习的东西太多，难以记忆的时候，我们（普通人）会怎么做？个人觉得记笔记是个好方法，什么时候要用到了，直接去翻笔记就好了。而且还不能囫囵吞枣似的全记下来，太费本子（钱）了，得划重点！

第一步，确定要记住什么。

原始的 RNN 网络，整体概括下来只有三种值：输入向量、输出值、隐藏层向量。其中隐藏层向量通常理解为能表征输入向量的特征向量，因此要记忆住的也是这个向量。

第二步，怎么长期记住。

最简单的方法就是来者不拒，每由输入向量 $x_{t}$ 得到一个隐藏层向量 $h_{t}$ ，就用一个存储单位把它存起来。

![](RNN(循环神经网络).assets/RNN_unit_sequence_lstm1%202.svg)

这里引用的存储单位为 $c$ ，加下标的 $c_{t}$ 表示刚记录完 $h_{t}$ 后的状态；将权重矩阵 $W_{xh}$ 和 $W_{hh}$ 合并为了一个。

$$\begin{aligned}
&c_{t}= c_{t-1}+h_{t}\\
&h_{t}=  
\tanh \left(W_{xhh}\left[h_{t-1}, x_{t}\right]+b\right)

\end{aligned}$$

第三步，判断当前的 $h_{t}$ 所表征的信息是否需要被记住。

想知道 $h_{t}$ 表征的信息重不重要，让 RNN 自己给它去算一个权重系数就好了。假设 $\Gamma_{u}$ 为控制是否记住当前 $h_{t}$ 表征信息的权重系数，令 $c_{t}= c_{t-1}+\Gamma_{u}h_{t}$。

然后通过输入数据 $x_{t}$ 和语境表征 $h_{t-1}$ 计算当前 $h_{t}$ 表征信息的重要程度。如果 $\Gamma_{u}=0$ ， $h_{t}$ 表征的信息都不重要，可以完全不记住；当 $\Gamma_{u}=1$  ， $h_{t}$ 表征的信息都很重要，需要完全记住。

![](RNN(循环神经网络).assets/RNN_unit_sequence_lstm2.svg)

$$
\begin{aligned}
&c_{t}= c_{t-1}+\Gamma_{u}h_{t}\\
&h_{t}=  
\tanh \left(W_{xhh}\left[h_{t-1}, x_{t}\right]+b_{h}\right)\\
&\Gamma_{u}=\sigma\left(W_{xhu}\left[h_{t-1}, x_{t}\right]+b_{u}\right)
\end{aligned}
$$

==然后通过输入数据 $x_{t}$ 和 $h_{t-1}$ 的可替代性，将其作为 $\Gamma_{u}$ 。如果 $\Gamma_{u}=0$ ，则 $x_{t}$ 可以被 $h_{t-1}$所替代 ，那就无需再记住 $x_{t}$ 。当 $\Gamma_{u}$ 为 1 时为完全记住。==

第四步，判断过去的信息是否已经out（过时）了。

未来总是不断更替的，总有新事物替代旧事物，因此我们的网络也得与时俱进。同上面第三步的思路，再给 RNN 训练一个类似结构，能通过输入数据 $x_{t}$ 和语境表征 $h_{t-1}$ ，判断长期记忆 $c_{t-1}$ 是否需要被忘记，遗忘系数设为 $\Gamma_{f}$ ， 可得 $c_{t}= \Gamma_{f}c_{t-1}+\Gamma_{u}h_{t}$。如果 $\Gamma_{f}=0$ ，说明 $c_{t-1}$ 已经过时，可以被遗忘了，反之，则不能遗忘。

![](RNN(循环神经网络).assets/RNN_unit_sequence_lstm3.svg)

$$
\begin{aligned}
&c_{t}= \Gamma_{f}c_{t-1}+\Gamma_{u}h_{t}\\
&h_{t}=  
\tanh \left(W_{xhh}\left[h_{t-1}, x_{t}\right]+b_{h}\right)\\
&\Gamma_{u}=\sigma\left(W_{xhu}\left[h_{t-1}, x_{t}\right]+b_{u}\right)\\
&\Gamma_{f}=\sigma\left(W_{xhf}\left[h_{t-1}, x_{t}\right]+b_{f}\right)
\end{aligned}
$$

第五步，使用长期记住的信息

上述二、三、四步所构造的结构，虽然已经使用 $c_{t}$ 将重要的信息记住了，但是整个网络依旧是使用 $h_{t}$ 给输出或下一个输入提供当前输入的特征信息和语境信息。考虑到 $h_{t}$ 记录的信息是不完整的，不如直接使用蕴含长期记忆的 $c_{t}$ 作为参考，从 $c_{t}$ 中选择出当前输入 $x_{t}$ 的特征信息和语境信息。

因此继续构建一个计算权重系数  $\Gamma_{o}$ 的结构，使得 $a_{t}=\Gamma_{o} * \tanh c_{t}$，用 $a_{t}$ 保存由长期记忆 $c_{t}$ 提取的特征信息和语境信息，然后将 $a_{t}$ 替代之前网络结构中的 $h_{t}$ 。

![](RNN(循环神经网络).assets/RNN_unit_sequence_lstm.svg)

$$
\begin{aligned}
&c_{t}= \Gamma_{f}c_{t-1}+\Gamma_{u}h_{t}\\
&h_{t}=  
\tanh \left(W_{xhh}\left[h_{t-1}, x_{t}\right]+b_{h}\right)\\\\
&\Gamma_{u}=\sigma\left(W_{xhu}\left[a_{t-1}, x_{t}\right]+b_{u}\right)\\
&\Gamma_{f}=\sigma\left(W_{xhf}\left[a_{t-1}, x_{t}\right]+b_{f}\right)\\
&\Gamma_{o}=\sigma\left(W_{xhf}\left[a_{t-1}, x_{t}\right]+b_{f}\right)\\
&a_{t}=\Gamma_{o} * \tanh c_{t}
\end{aligned}
$$

==上述二、三、四步所构造的结构，虽然已经使用 $c_{t}$ 将重要的东西记住了，但是 $c_{t}$ 每次记住的信息都是非常完整的吗？
先看一看公式 $c_{t}= \Gamma_{f}c_{t-1}+\Gamma_{u}h_{t}$，可以知道每次 $c_{t}$ 记住的都是 $h_{t}$ 。而 $h_{t}$ 是表征当前输入向量的特征向量，并且它还包含了 $h_{t}$ 所需要的语境信息。
前面几步我们把重要的 $h_{t}$ 都记录了下来，但是 $h_{t}$ 记录的语境信息依旧会随着 RNN 输入序列长度的增加而减少，完整记录的只有当前输入 $x_{t}$ 的特征信息。因此 $c_{t}$ 每次记住的信息是不完整的。
如果把 $h_{t}$ 进行功能分离，使其只提取当前输入 $x_{t}$ 的特征信息，并保存到$c_{t}$ 中。然后再构造。==

LSTM 长短期记忆网络

![image-20220206210535699](RNN(循环神经网络).assets/image-20220206210535699.png)

![image-20220206210602486](RNN(循环神经网络).assets/image-20220206210602486.png)

peephole connection

## BRNN 双向递归神经网络

![image-20220207141423060](RNN(循环神经网络).assets/image-20220207141423060.png)

优点：双向考虑，但是需要输入完整序列，不适用于实时监测。

其余RNN变体

1. 自制第一版

	![](RNN(循环神经网络).assets/image-20220313102511.png)

2. [窥视孔连接](https://zhuanlan.zhihu.com/p/135970560/%5Bftp://ftp.idsia.ch/pub/juergen/TimeCount-IJCNN2000.pdf%5D(ftp://ftp.idsia.ch/pub/juergen/TimeCount-IJCNN2000.pdf))
	
	![](RNN(循环神经网络).assets/image-20220313100506.png)

3. Clockwork RNN

	![](RNN(循环神经网络).assets/image-20220313100953.png)
	
4. SRU

	![](RNN(循环神经网络).assets/image-20220313102554.png)

5. [Q-RNN](https://arxiv.org/abs/1611.01576)
	
	![](RNN(循环神经网络).assets/image-20220313103503.png)

## BPTT 时序反向传播算法

[零基础入门深度学习(5) - 循环神经网络 - 作业部落 Cmd Markdown 编辑阅读器 (zybuluo.com)](https://zybuluo.com/hanbingtao/note/541458)

### 回顾多层感知机的反向传播计算

![](RNN(循环神经网络).assets/image-20220318132037.png)

循环神经网络的时间反向传播（backpropagation through time，BPTT），是循环神经网络中反向传播技术的一个特定应用， 它要求我们将循环神经网络的计算图一次展开一个时间步， 以获得模型变量和参数之间的依赖关系。 然后，基于链式法则，应用反向传播来计算和存储梯度。 由于序列可能相当长，因此依赖关系也可能相当长。 例如，某个1000个字符的序列， 其第一个词元可能会对最后位置的词元产生重大影响。 

### RNN单元前向计算公式（详细）

![](RNN(循环神经网络).assets/image-20220318141126.png)
与上图RNN计算单元类似，变量假设和前向计算公式如下：

$$
\begin{array}{|l|l|l|}

\hline

\text { 神经元 } & \text { 描述 } & \text { 变量索引 } \\

\hline

x_{t} \in R^{l × 1} & \text { 输入向量 } & (i) \\

h_{t-1}\in R^{m × 1} & \text { 前一层隐藏层向量 } & (s) \\

h_{t}\in R^{m × 1} & \text { 当前层隐藏层向量r } & (j) \\

o_{t}\in R^{q × 1} & \text { 输出向量 } & (k) \\

\hat{o}_{t}&\text { 真实输出 }&\\

L & \text { 最终损失值 } & \\

\hline

\hline
\text { 权重矩阵 } & \text { 描述 } & \text { 变量索引 } \\
\hline

W_{xh}\in R^{m × l} & \text { 输入 } \rightarrow \text { 隐向量 } & (i, j) \\

W_{hh}\in R^{m × m} & \text { 前隐向量 } \rightarrow \text { 隐向量 } & (s, j) \\

W_{ho}\in R^{q × m} & \text { 隐向量 } \rightarrow \text { 输出 } & (j, k) \\

\hline

\hline
\text { 函数 } & \text { 描述 } & \text {  } \\
\hline

f() & \text { 激活函数：SoftMax } &  \\

g() & \text { 激活函数：Tanh } &  \\

loss() & \text { 损失函数 } &  \\

\hline

\hline

\text { 维度 } & \text { 描述 } & \text { } \\
\hline

T & \text { 输入序列长度 } &  \\

l& \text { 输入向量特征维度(如词元onehot向量) } &  \\

m& \text { 隐藏层向量维度 } &  \\

q& \text { 输出向量维度(可与输入相等，变为计算onehot类词元的概率) } &  \\

\hline
\end{array}
$$

$$
\begin{aligned}
  

L&=\sum_{t=1}^{T} L_{t}=\sum_{t=1}^{T} \operatorname{loss}\left(o_{t}, \hat{o}_{t}\right)\\

o_{t} &=f\left(W_{ho} h_{t}+b_{o}\right) \\

&=f\left(\left[\begin{array}{c}

\vdots\\

\sum_{j=1}^{m} h_{t}(j) w(k,j)+b_{o}(k) \\

\vdots

\end{array}\right]\right)\\

h_{t} &=g\left(W_{x h} x_{t}+W_{h h} h_{t-1}+b_{h}\right) \\

&=\left[\begin{array}{c}
\vdots \\

g\left(\sum_{i=1}^{l} x_{t}(i) w_{x h}(j, i)+\sum_{s=1}^{m} h_{t-1}(s) w_{h h}(j, s)+b_{h}(j)\right) \\

\vdots
\end{array}\right]

\end{aligned}
$$

通过对公式分析，可知对于总输出 L (最终损失值)，其可训练参数仅有五种（$W_{xh},W_{hh},W_{ho},b_{o},b_{h}$），由梯度下降法可知，网络中的每个权重变化应该相对于成本函数（Loss函数）的梯度成负比例关系，即在参数更新时，需要计算 L 对以上五种参数矩阵(向量)的偏微分：  $\frac{\partial L}{\partial W_{x h}}, \frac{\partial L}{\partial W_{h h}}, \frac{\partial L}{\partial W_{h o}},\frac{\partial L}{\partial b_{o}},\frac{\partial L}{\partial b_{h}}$。

偏微分的求解，可以使用与BP网络相同的链式法则获取，但是需要注意的是，因为函数中存在线性和非线性部分，因此计算过程中也需要将其考虑在内。

先计算非线性函数：

$$
\begin{aligned}
\frac{\partial g(x(i))}{\partial(x(j))}&=\frac{\partial \tanh (x(i))}{\partial(x(j))}=
\left\{\begin{array}{cc}1-\tanh^{2}(x(i))& \ i=j \\0 &i \neq j\end{array}\right\}\\

\frac{\partial g(x)}{\partial(x)}&=
\left[\begin{array}{c}
\frac{\partial g(x(1))}{\partial(x)}\\
\frac{\partial g(x(2))}{\partial(x)}\\
\vdots\\
\frac{\partial g(x(l))}{\partial(x)}
\end{array}\right]
=\left[\begin{array}{cccc}
\frac{\partial g(x(1))}{\partial(x(1))} & \frac{\partial g(x(1))}{\partial(x(2))} & \cdots & \frac{\partial g(x(1))}{\partial(x(l))} \\
\frac{\partial g(x(2))}{\partial(x(1))} & \frac{\partial g(x(2))}{\partial(x(2))} & \cdots & \frac{\partial g(x(2))}{\partial(x(l))} \\
\vdots & \vdots & \ddots & \vdots\\
\frac{\partial g(x(l))}{\partial(x(1))} & \frac{\partial g(x(l))}{\partial(x(2))} & \cdots & \frac{\partial g(x(l))}{\partial(x(l))}
\end{array}\right] \\

&=\left[\begin{array}{cccc}
1-\tanh^{2}(x(1)) & 0 & \cdots & 0 \\
0 & 1-\tanh^{2}(x(2)) & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & 1-\tanh^{2}(x(l))
\end{array}\right]\\

\frac{\partial f(x(i))}{\partial(x(j))}&=\frac{\partial\left(\frac{e^{x(i)}}{\sum_{k=1}^{l} e^{x(k)}}\right)}{\partial(x(j))}=\left\{\begin{array}{l}

f(x(i))(1-f(x(j)) \quad i=j \\

-f(x(i)) f(x(j)) \quad i \neq j

\end{array}\right.\\

\frac{\partial f(x)}{\partial(x)}&=
\left[\begin{array}{cccc}

f(x(1))(1-f(x(1))) & -f(x(1))f(x(2)) & \cdots & -f(x(1))f(x(l)) \\

-f(x(2))f(x(1)) & f(x(2))(1-f(x(2))) & \cdots & -f(x(2))f(x(l)) \\
\vdots & \vdots & \ddots & \vdots\\
-f(x(l))f(x(1)) & -f(x(l))f(x(2)) & \cdots & f(x(l))(1-f(x(l)))
\end{array}\right]\\

\end{aligned}
$$

计算 $\frac{\partial L}{\partial W_{h o}}$

$$
\begin{aligned}

\frac{\partial o_{t}}{\partial W_{ho}}&=\frac{\partial f(\sim)}{\partial \sim}h_{t}\\

\frac{\partial L}{\partial W_{ho}}&
=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial W_{ho}}
=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial o_{t}} \frac{\partial o_{t}}{\partial W_{ho}}\\
&=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial o_{t}} \frac{\partial f(\sim)}{\partial \sim}h_{t}

\end{aligned}
$$

计算 $\frac{\partial L}{\partial W_{h h}}$

$$
\begin{aligned}

\frac{\partial o_{t}}{\partial h_{t}}&=\frac{\partial f(\sim)}{\partial \sim}W_{oh}\\
  

\frac{\partial h_{t}}{\partial W_{h h}}&=\frac{\partial g(\sim)}{\partial \sim} h_{t-1}+\frac{\partial g(\sim)}{\partial \sim} \frac{\partial h_{t-1}}{\partial W_{hh}}W_{hh}\\
&=\sum_{v=1}^{t}\left(\left(\frac{\partial g(\sim)}{\partial(\sim)}\right)^{v} W_{h h}^{v-1} h_{t-v}\right)+\left(\frac{\partial g(\sim)}{\partial(\sim)}\right)^{t} W_{h h}^{t} \frac{\partial h_{0}}{\partial W_{h h}}\\

\frac{\partial L}{\partial W_{h h}}&=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial W_{h h}}=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial o_{t}} \frac{\partial o_{t}}{\partial h_t} \frac{\partial h_{t}}{\partial W_{h h}}

\end{aligned}
$$

计算 $\frac{\partial L}{\partial W_{xh}}$


$$
\begin{aligned}

\frac{\partial o_{t}}{\partial h_{t}}&=\frac{\partial f(\sim)}{\partial \sim}W_{oh}\\

\frac{\partial h_{t}}{\partial W_{x h}}&=\frac{\partial g(\sim)}{\partial \sim} x_{t}\\
\frac{\partial L}{\partial W_{x h}}&=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial W_{x h}}=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial o_{t}} \frac{\partial o_{t}}{\partial h_t} \frac{\partial h_{t}}{\partial W_{x h}}

\end{aligned}$$

计算 $\frac{\partial L}{\partial b_{o}}$
$$
\begin{aligned}

\frac{\partial o_{t}}{\partial b_{o}}&=\frac{\partial f(\sim)}{\partial \sim}\\

\frac{\partial L}{\partial b_{o}}&
=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial b_{o}}
=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial o_{t}} \frac{\partial o_{t}}{\partial b_{o}}\\
&=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial o_{t}} \frac{\partial f(\sim)}{\partial \sim}

\end{aligned}

$$
计算 $\frac{\partial L}{\partial b_{h}}$
$$

\begin{aligned}

\frac{\partial o_{t}}{\partial h_{t}}&=\frac{\partial f(\sim)}{\partial \sim}W_{ho}\\

\frac{\partial h_{t}}{\partial b_{h}}&=\frac{\partial g(\sim)}{\partial \sim}\\
\frac{\partial L}{\partial b_{h}}&=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial b_{h}}=\sum_{t=1}^{T} \frac{\partial L_{t}}{\partial o_{t}} \frac{\partial o_{t}}{\partial h_t} \frac{\partial h_{t}}{\partial b_{h}}

\end{aligned}

$$
假设最终分类任务得到的输出是对每个类别的概率计算，然后通过交叉熵损失函数计算损失值L，即
$$

L=\frac{1}{T} \sum_{t=1}^{T} L_{t}=-\frac{1}{T} \sum_{t=1}^{T} \sum_{k=1}^{q} \hat{o}_{t}(k) \log \left(o_{t}(k)\right)

$$
由此，通过具体实例，就可以简单的把前面列的偏导式子化简了。



> http://ir.hit.edu.cn/~jguo/docs/notes/bptt.pdf
> [PyTorch学习笔记——多分类交叉熵损失函数 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/56638625)
> [(24条消息) 深度学习中矩阵求导公式整理_Kobaayyy的博客-CSDN博客](https://blog.csdn.net/Kobaayyy/article/details/104317646)
> [循环神经网络(RNN)模型与前向反向传播算法 - 刘建平Pinard - 博客园 (cnblogs.com)](https://www.cnblogs.com/pinard/p/6509630.html)
> [LayerNorm_LSTM/ln-wd-vd-lstm.py at master · chenhuaizhen/LayerNorm_LSTM (github.com)](https://github.com/chenhuaizhen/LayerNorm_LSTM/blob/master/ln-wd-vd-lstm.py)

## 举例：Seq2Seq 模型

![](RNN(循环神经网络).assets/RNN_example%201.svg)

Encoder结构：左边紫色 RNN 结构，在输入 $x_{i}, (i \in \{1, \cdots,N\})$ 后，可以获得其隐藏层状态 $h_{i}$ ：用来表征 $x_{i}$ 及其历史信息的编码特征。因此通过此 N to 1结构的编码器 Encoder 可以把所有输入序列 $\{x_{i}\}$ 都编码成一个统一的语义向量 Context (红色)。

Decoder结构：右边蓝色RNN结构，不断地将前一个时刻 $t-1$ 的输出作为后一个时刻 $t$ 的输入，循环解码，直到输出停止符为止。

## 强化 : Attention 注意力机制

Encoder 编码结束后，会得到一个统一的语义向量 $Context$，即由得来最后一个输入数据元的隐藏层状态 $h_{N}$，用来表征原输入序列的所有信息，之后提供给Decoder 解码，得到最终想要的结果。因此 $Context$ 的长度就成了限制模型表征能力的瓶颈（输入序列包含的信息越多，由于 $Context$ 表征能力不足，会导致整个模型的最终训练效果不好）。==（并且 $Context$ 虽然可以表征原输入序列的所有信息，但是随着 RNN 输入序列长度的增加，可能会慢慢遗忘最初输入数据带来的信息。思考和疑问：代替LSTM？）（如果将输入数据的所有隐藏层状态$\{h_{i}\}$保存下来，共同输入给 Decoder ，坏处在哪？）==

![](RNN(循环神经网络).assets/image-20220310180812.png)

Attention机制通过将 Decoder 的原本单一的，由 $h_{N}$ 得来的 $Context$ 输入向量，换成了不同的 $c_{t}$ 来解决这个问题。它通过计算 Decoder   $t$ 时刻状态向量  s(t) 与 Encoder 中所有隐藏层 $\{h_{i}\}$ 的相关性 $a_{t}(i)$ 

$$a_{t}(i)=\frac{\exp \left(\operatorname{score}\left(s_{t}, h_{i}\right)\right)}{\sum_{i=1}^{N} \exp \left(\operatorname{score}\left(s_{t}, h_{j}\right)\right)}$$


这里的 score 可以通过以下三种方式计算：


$$\operatorname{score}\left(s_{t}, h_{i}\right)= \begin{cases}s_{t}^{T} h_{i} & \text { Dot } \\ s_{t}^{T} R h_{i} & \text { General } \\ v_{a}^{T} \tanh \left(R \cdot \operatorname{concat}\left(s_{t}, h_{i}\right)\right) & \text { Concat }\end{cases}$$

其中R是可学习矩阵，最终得到包含最合适的语境信息的语义向量  $c_{t}$ 

$$c_{t}=\sum_{i=1}^{N} a_{t}(i) \cdot h_{i}$$

权重 $a_{t}(i)$ 用来控制每一个隐藏层 $h_{i}$ 提供的信息所占比例。(==权重数据可以用来画图，看看到底注意了什么==)

接下来，将通过权重 $a_{t}(i)$ 生成的 $c_{t}$ 与原始 decoder 隐藏层 $t$ 时刻状态 $s_{t}$ 拼接在一起得到 decoder 最终的隐藏状态向量 $\tilde{h}_{t}$ 和输出 $o_{t}$ 。
$$
\begin{aligned}
&\tilde{h}_{t}=\tanh \left(W_{cs\tilde{h}} \cdot \operatorname{concat}\left(c_{t}, s_{t}\right)+b_{\tilde{h}} \right)=\tanh \left(W_{cs\tilde{h}} \cdot\left[c_{t} ; s_{t}\right]+b_{\tilde{h}}\right)\\
&o_{t}=SoftMax\left(W_{ho} \cdot \tilde{h}_{t}+b_{o}\right) 
\end{aligned}
$$

## 强化 : Scheduled Sampling ^d4b30e

早期 Seq2Seq 模型训练阶段， Decoder 的输入主要只使用目标的真实数据或生成数据(如输出值o、隐藏层向量h)训练。

完全依赖于真实数据会导致生成阶段和训练阶段的输入数据分布产生极大差异，影响模型训练结果。

![](RNN(循环神经网络).assets/RNN_Decoder2.svg)

若在训练阶段，只使用生成数据作为输入，那么当某一时刻的输出发生错误，就可能会导致后面全错。

![](RNN(循环神经网络).assets/RNN_Decoder1%201.svg)

因此为了解决这两种问题，Google 提出了 Scheduled Sampling(计划取样)方法，其具体实现过程如 Seq2Seq 模型图中菱形结构所示。

![](RNN(循环神经网络).assets/image-20220310152522.png)

在 Decoder 的 $t$ 时刻， Scheduled Sampling 以概率$1-ϵ_{t}$  使用 t-1 时刻生成的输出作为输入、概率 $ϵ_{t}$ 使用真实数据作为输入，而 $ϵ_{t}$ 是一个随  $t$  增大而衰减的变量，衰减方式由自己定义。随着 $ϵ_{t}$ 衰减，Decoder 将不断倾向于使用生成的元素作为输入，从而避免训练过程过度依赖于真实数据。同时，因为前期概率 $ϵ_{t}$ 会挺大，大概率将真实数据作为 Decoder 输入，这样即使前面生成错误，其训练目标仍然是最大化真实目标序列的概率，模型会朝着正确的方向进行训练，增加了模型的容错能力。

Embedding ^f2c635

解决问题1：输入序列成分间的关系

每输入序列中一个特征向量，所得到的计算结果都会保留到内存中，当输入下一个特征向量时，会同时考虑内存保留的上一步的计算结果和当前输入，计算得到最后的结果，并继续保留到内存中。

解决问题2：输入序列间的长度差异

[Understanding LSTM Networks -- colah's blog](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
