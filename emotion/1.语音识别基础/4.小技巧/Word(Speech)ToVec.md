---
title: "Word(Speech)ToVec"
author: "石昌文"
tags: [""]
description: ""
categories: [""]
keywords:  [""]
type: ""
draft: true
layout: 
data: 2022-03-19 14:47:46
lastmod: 2022-03-22 17:16:38
---

# *Word2Vec and Spech2Vec

> 在一句话中，其中的每个单词与上下文间会有相关性，对于具有相似结构的上下文中的出现的单词往往会有相似的含义。因此，利用这种相关性训练的神经网络所得到的向量矩阵，其中必然就会含有单词的一些语义信息。Word2vec 就是 word embedding 的一种方式，给其预先定义好的 One-Hot Vector 作为输入，然后通过神经网络进行训练，得到网络权重就是所需要的Word embedding  spaces，在这个Word embedding  spaces中，相似的单词在几何距离上会非常接近。
>
> 与文本相比，语音是另一种语言形式。原始的声音表示方法，大都是提取其声学特征，即一个声音听起来的方式，而未考虑一段声音中所蕴含的语义。Speech2Vec就是一种能够将从音频段表示为包含基础语义信息的固定维vectors。它受Word2vec的启发，借鉴了其训练方法，输入可变长度的acoustic features序列，然后通过循环神经网络（RNN）进行训练。
>
> 两者的训练方法一般分为两种：CBOW（多对一）和 Skip-Gram（一对多）。
>
> 

![](Word(Speech)ToVec.assets/image-20220304012312.jpeg)



![](Word(Speech)ToVec.assets/image-20220304012325.png)



 Word Embedding

用向量表示 word。One-hot向量，构建简单，但是不蕴含word间的关系，并且当word词汇量太多时，向量维度会非常高；使用word class对word进行分类，只能蕴含一部分word之间的关系，但是关系不全。



 语言模型

N-gram语言模型

Bigram语言模型

RNN-LM语言模型
