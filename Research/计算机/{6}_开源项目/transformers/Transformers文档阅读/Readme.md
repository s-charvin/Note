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
data: 2021-12-07 10:05:49
lastmod: 2022-03-27 14:12:21
---

# 🤗 Transformers

‎适用于 Jax、Pytorch 和 TensorFlow‎最先进的机器学习‎‎框架

🤗 Transformers（以前称为*pytorch-transformers*和*pytorch-pretrained-bert）*提供了数千个预训练模型，用于在文本、视觉和音频等不同模态上执行任务。

这些模型可以应用于：

- 📝 Text, 用于 100 多种语言的文本分类、信息提取、问答、摘要、翻译、文本生成等任务。
- 🖼️ Images, 用于图像分类、对象检测和分割等任务。
- 🗣️ Audio, 用于语音识别和音频分类等任务。

Transformer模型还可以在**多种组合的模态**上执行任务，例如 tableQA，光学字符识别，扫描文档信息提取，视频分类和 VQA。

🤗 Transformers 提供了 API，用于在给定文本上快速下载和使用这些预训练模型，并在您自己的数据集上微调它们，然后在我们的[模型中心](https://huggingface.co/models)上与社区共享它们。同时，每个架构的python模块都是完全独立的，可以进行修改以实现快速的研究实验。

🤗 Transformers 可以在三个最流行的深度学习库[Jax、PyTorch](https://pytorch.org/)和[TensorFlow](https://www.tensorflow.org/)之间无缝衔接。在加载你的模型应用到其他模型前，使用库中的模型训练你的模型变得非常简单。

这是我们 [Transformers ](https://github.com/huggingface/transformers)的文档。您还可以关注我们的[在线课程](https://huggingface.co/course)，该课程教授了如何使用此库，以及Hugging Face和Hub开发的其他库。T

## 如果您正在寻找 Hugging Face 团队的自定义支持

[![HuggingFace Expert Acceleration Program](Readme.assets/support-16388476576101.png)](https://huggingface.co/support)

## 特点

1. 轻松使用最新的模型:
	- 在自然语言理解和生成、计算机视觉和音频任务方面效果显著。
	- 教育工作者和从业人员的进入门槛低。
	- 很少有面向用户的抽象，只有三个类需要学习。
	- 只有一个统一的 API，用于使用所有预训练的模型。
2. 更低的计算成本，更低的碳足迹：
	- 研究人员可以共享经过训练的模型，而不是总是重新训练。
	- 从业人员可以减少计算时间和生产成本。
	- 数十种架构，包含 20，000 多个预训练模型，其中一些模型支持 100 多种语言。
3. 为模型运行周期的每个部分选择正确的框架:
	- 在 3 行代码中训练最先进的模型。
	- 随意在 TF2.0/PyTorch/JAX 框架之间切换单个模型。
	- 简单而正确的选择训练、评估和生成框架。
4. 根据您的需求轻松自定义模型或示例：
	- 我们为每种架构提供示例，以重现其原始作者发布的结果。
	- 模型内部尽可能一致地公开。
	- 模型文件可以独立于库使用，以便进行快速试验。

[所有的 checkpoints 模型文件](https://huggingface.co/models) 都可以从 huggingface.co [模型中心](https://huggingface.co/) 中无缝集成。模型中心的模型都是由 [用户](https://huggingface.co/users) 和 [组织](https://huggingface.co/organizations)上传的。

## 内容

本文档分为五个部分：

- **GET STARTED** 包含快速浏览、安装说明以及有关我们的原理（philosophy）和术语表（glossary.）的一些有用信息。
- **USING 🤗 TRANSFORMERS** 包含有关如何使用该库的一般教程。
- **ADVANCED GUIDES** 包含更高级的指南，这些指南更专注于某个脚本或库的某一部分。
- **RESEARCH** 不怎么教给你怎么使用库，更多地侧重于 transformers 模型的一般研究的教程。
- **API** 包含每个公共类和函数的文档，这些类和函数按以下顺序分组：
	- **MAIN CLASSES** 主要类，公开库的重要 API。
	- **MODELS** 与库中每个模型实现相关的类和函数
	- **INTERNAL HELPERS** 用于我们在内部使用的类和函数。

该库目前包含以下模型在Jax、PyTorch 和 Tensorflow中的实现、预训练模型权重、脚本使用和转换程序。

### 受支持的模型

1. **[ALBERT](https://huggingface.co/docs/transformers/model_doc/albert)** 

	[ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/abs/1909.11942)

2. **[BART](https://huggingface.co/docs/transformers/model_doc/bart)**

	[BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/pdf/1910.13461.pdf) 

3. **[BARThez](https://huggingface.co/docs/transformers/model_doc/barthez)** 

	[BARThez: a Skilled Pretrained French Sequence-to-Sequence Model](https://arxiv.org/abs/2010.12321)

4. **[BARTpho](https://huggingface.co/docs/transformers/model_doc/bartpho)**  

	[BARTpho: Pre-trained Sequence-to-Sequence Models for Vietnamese](https://arxiv.org/abs/2109.09701) 

5. **[BEiT](https://huggingface.co/docs/transformers/model_doc/beit)**

	[BEiT: BERT Pre-Training of Image Transformers](https://arxiv.org/abs/2106.08254)

6. **[BERT](https://huggingface.co/docs/transformers/model_doc/bert)** 

	[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)

7. **[BERTweet](https://huggingface.co/docs/transformers/model_doc/bertweet)** 

	[BERTweet: A pre-trained language model for English Tweets](https://aclanthology.org/2020.emnlp-demos.2/)

8. **[BERT For Sequence Generation](https://huggingface.co/docs/transformers/model_doc/bertgeneration)**

	[Leveraging Pre-trained Checkpoints for Sequence Generation Tasks](https://arxiv.org/abs/1907.12461)

9. **[BigBird-RoBERTa](https://huggingface.co/docs/transformers/model_doc/bigbird)**

	[Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062)

10. **[BigBird-Pegasus](https://huggingface.co/docs/transformers/model_doc/bigbird_pegasus)** 

	[Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062)

11. **[Blenderbot](https://huggingface.co/docs/transformers/model_doc/blenderbot)**

	[Recipes for building an open-domain chatbot](https://arxiv.org/abs/2004.13637)

12. **[BlenderbotSmall](https://huggingface.co/docs/transformers/model_doc/blenderbot_small)**

	[Recipes for building an open-domain chatbot](https://arxiv.org/abs/2004.13637)

13. **[BORT](https://huggingface.co/docs/transformers/model_doc/bort)**

	[Optimal Subarchitecture Extraction For BERT](https://arxiv.org/abs/2010.10499)

14. **[ByT5](https://huggingface.co/docs/transformers/model_doc/byt5)**

	[ByT5: Towards a token-free future with pre-trained byte-to-byte models](https://arxiv.org/abs/2105.13626)

15. **[CamemBERT](https://huggingface.co/docs/transformers/model_doc/camembert)**

	[CamemBERT: a Tasty French Language Model](https://arxiv.org/abs/1911.03894)

16. **[CANINE](https://huggingface.co/docs/transformers/model_doc/canine)**

	[CANINE: Pre-training an Efficient Tokenization-Free Encoder for Language Representation](https://arxiv.org/abs/2103.06874)

17. **[CLIP](https://huggingface.co/docs/transformers/model_doc/clip)**

	[Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)

18. **[ConvBERT](https://huggingface.co/docs/transformers/model_doc/convbert)**

	[ConvBERT: Improving BERT with Span-based Dynamic Convolution](https://arxiv.org/abs/2008.02496)

19. **[CPM](https://huggingface.co/docs/transformers/model_doc/cpm)**

	[CPM: A Large-scale Generative Chinese Pre-trained Language Model](https://arxiv.org/abs/2012.00413)

20. **[CTRL](https://huggingface.co/docs/transformers/model_doc/ctrl)**

	[CTRL: A Conditional Transformer Language Model for Controllable Generation](https://arxiv.org/abs/1909.05858)

21. **[DeBERTa](https://huggingface.co/docs/transformers/model_doc/deberta)**

	[DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654) 

22. **[DeBERTa-v2](https://huggingface.co/docs/transformers/model_doc/deberta_v2)**

	[DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654) 

23. **[DeiT](https://huggingface.co/docs/transformers/model_doc/deit)**

	[Training data-efficient image transformers & distillation through attention](https://arxiv.org/abs/2012.12877)

24. **[DETR](https://huggingface.co/docs/transformers/model_doc/detr)**

	[End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872)

25. **[DialoGPT](https://huggingface.co/docs/transformers/model_doc/dialogpt)**

	[DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation](https://arxiv.org/abs/1911.00536)

26. **[DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert)**

	[DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108)The same method has been applied to compress GPT2 into [DistilGPT2](https://github.com/huggingface/transformers/tree/master/examples/distillation), RoBERTa into [DistilRoBERTa](https://github.com/huggingface/transformers/tree/master/examples/distillation), Multilingual BERT into [DistilmBERT](https://github.com/huggingface/transformers/tree/master/examples/distillation) and a German version of DistilBERT.

27. **[DPR](https://huggingface.co/docs/transformers/model_doc/dpr)**

	[Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906)

28. **[EncoderDecoder](https://huggingface.co/docs/transformers/model_doc/encoderdecoder)**

	[Leveraging Pre-trained Checkpoints for Sequence Generation Tasks](https://arxiv.org/abs/1907.12461)

29. **[ELECTRA](https://huggingface.co/docs/transformers/model_doc/electra)**

	[ELECTRA: Pre-training text encoders as discriminators rather than generators](https://arxiv.org/abs/2003.10555)

30. **[FlauBERT](https://huggingface.co/docs/transformers/model_doc/flaubert)**

	[FlauBERT: Unsupervised Language Model Pre-training for French](https://arxiv.org/abs/1912.05372)

31. **[FNet](https://huggingface.co/docs/transformers/model_doc/fnet)**

	[FNet: Mixing Tokens with Fourier Transforms](https://arxiv.org/abs/2105.03824) 

32. **[Funnel Transformer](https://huggingface.co/docs/transformers/model_doc/funnel)**

	[Funnel-Transformer: Filtering out Sequential Redundancy for Efficient Language Processing](https://arxiv.org/abs/2006.03236)

33. **[GPT](https://huggingface.co/docs/transformers/model_doc/gpt)**

	[Improving Language Understanding by Generative Pre-Training](https://blog.openai.com/language-unsupervised/)

34. **[GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2) **

	[Language Models are Unsupervised Multitask Learners](https://blog.openai.com/better-language-models/)

35. **[GPT-J](https://huggingface.co/docs/transformers/model_doc/gptj)** 

	[kingoflolz/mesh-transformer-jax](https://github.com/kingoflolz/mesh-transformer-jax/)

36. **[GPT Neo](https://huggingface.co/docs/transformers/model_doc/gpt_neo)**

	[EleutherAI/gpt-neo](https://github.com/EleutherAI/gpt-neo)**[Hubert](https://huggingface.co/docs/transformers/model_doc/hubert)** 

	[HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units](https://arxiv.org/abs/2106.07447)

38. **[I-BERT](https://huggingface.co/docs/transformers/model_doc/ibert)** 

	[I-BERT: Integer-only BERT Quantization](https://arxiv.org/abs/2101.01321)

39. **[ImageGPT](https://huggingface.co/docs/transformers/model_doc/imagegpt)** 

	[Generative Pretraining from Pixels](https://openai.com/blog/image-gpt/)

40. **[LayoutLM](https://huggingface.co/docs/transformers/model_doc/layoutlm)** 

	[LayoutLM: Pre-training of Text and Layout for Document Image Understanding](https://arxiv.org/abs/1912.13318)

41. **[LayoutLMv2](https://huggingface.co/docs/transformers/model_doc/layoutlmv2)** 

	[LayoutLMv2: Multi-modal Pre-training for Visually-Rich Document Understanding](https://arxiv.org/abs/2012.14740)

42. **[LayoutXLM](https://huggingface.co/docs/transformers/model_doc/layoutlmv2)** 

	[LayoutXLM: Multimodal Pre-training for Multilingual Visually-rich Document Understanding](https://arxiv.org/abs/2104.08836)

43. **[LED](https://huggingface.co/docs/transformers/model_doc/led)** 

	[Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150) 

44. **[Longformer](https://huggingface.co/docs/transformers/model_doc/longformer)** 

	[Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150) 

45. **[LUKE](https://huggingface.co/docs/transformers/model_doc/luke)** 

	[LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention](https://arxiv.org/abs/2010.01057) 

46. **[LXMERT](https://huggingface.co/docs/transformers/model_doc/lxmert)** 

	[LXMERT: Learning Cross-Modality Encoder Representations from Transformers for Open-Domain Question Answering](https://arxiv.org/abs/1908.07490)

47. **[M2M100](https://huggingface.co/docs/transformers/model_doc/m2m_100)** 

	[Beyond English-Centric Multilingual Machine Translation](https://arxiv.org/abs/2010.11125)

48. **[MarianMT](https://huggingface.co/docs/transformers/model_doc/marian)** 

	Machine translation models trained using [OPUS](http://opus.nlpl.eu/) data by Jörg Tiedemann. The [Marian Framework](https://marian-nmt.github.io/) is being developed by the Microsoft Translator Team.

49. **[MBart](https://huggingface.co/docs/transformers/model_doc/mbart)** 

	[Multilingual Denoising Pre-training for Neural Machine Translation](https://arxiv.org/abs/2001.08210)

50. **[MBart-50](https://huggingface.co/docs/transformers/model_doc/mbart)** 

	[Multilingual Translation with Extensible Multilingual Pretraining and Finetuning](https://arxiv.org/abs/2008.00401)

51. **[Megatron-BERT](https://huggingface.co/docs/transformers/model_doc/megatron_bert)** 

	[Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053)

52. **[Megatron-GPT2](https://huggingface.co/docs/transformers/model_doc/megatron_gpt2)** 

	[Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053)

53. **[MPNet](https://huggingface.co/docs/transformers/model_doc/mpnet)** 

	[MPNet: Masked and Permuted Pre-training for Language Understanding](https://arxiv.org/abs/2004.09297)

54. **[MT5](https://huggingface.co/docs/transformers/model_doc/mt5)** 

	[mT5: A massively multilingual pre-trained text-to-text transformer](https://arxiv.org/abs/2010.11934)

55. **[Pegasus](https://huggingface.co/docs/transformers/model_doc/pegasus)** 

	[PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization](https://arxiv.org/abs/1912.08777)

56. **[PhoBERT](https://huggingface.co/docs/transformers/model_doc/phobert)** 

	[PhoBERT: Pre-trained language models for Vietnamese](https://www.aclweb.org/anthology/2020.findings-emnlp.92/)

57. **[ProphetNet](https://huggingface.co/docs/transformers/model_doc/prophetnet)** 

	[ProphetNet: Predicting Future N-gram for Sequence-to-Sequence Pre-training](https://arxiv.org/abs/2001.04063)

58. **[QDQBert](https://huggingface.co/docs/transformers/model_doc/qdqbert)** 

	[Integer Quantization for Deep Learning Inference: Principles and Empirical Evaluation](https://arxiv.org/abs/2004.09602)

59. **[Reformer](https://huggingface.co/docs/transformers/model_doc/reformer)** 

	[Reformer: The Efficient Transformer](https://arxiv.org/abs/2001.04451)

60. **[RemBERT](https://huggingface.co/docs/transformers/model_doc/rembert)**

	[Rethinking embedding coupling in pre-trained language models](https://arxiv.org/pdf/2010.12821.pdf)

61. **[RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta)** 

	(https://arxiv.org/abs/1907.11692)

62. **[RoFormer](https://huggingface.co/docs/transformers/model_doc/roformer)** 

	(https://arxiv.org/pdf/2104.09864v1.pdf)

63. **[SegFormer](https://huggingface.co/docs/transformers/model_doc/segformer)** 

	[SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers](https://arxiv.org/abs/2105.15203)

64. **[SEW](https://huggingface.co/docs/transformers/model_doc/sew)** 

	[Performance-Efficiency Trade-offs in Unsupervised Pre-training for Speech Recognition](https://arxiv.org/abs/2109.06870)

65. **[SEW-D](https://huggingface.co/docs/transformers/model_doc/sew_d)** 

	[Performance-Efficiency Trade-offs in Unsupervised Pre-training for Speech Recognition](https://arxiv.org/abs/2109.06870)

66. **[SpeechToTextTransformer](https://huggingface.co/docs/transformers/model_doc/speech_to_text)** 

	[fairseq S2T: Fast Speech-to-Text Modeling with fairseq](https://arxiv.org/abs/2010.05171)

67. **[SpeechToTextTransformer2](https://huggingface.co/docs/transformers/model_doc/speech_to_text_2)** 

	[Large-Scale Self- and Semi-Supervised Learning for Speech Translation](https://arxiv.org/abs/2104.06678)

68. **[Splinter](https://huggingface.co/docs/transformers/model_doc/splinter)** 

	[Few-Shot Question Answering by Pretraining Span Selection](https://arxiv.org/abs/2101.00438)

69. **[SqueezeBert](https://huggingface.co/docs/transformers/model_doc/squeezebert)** 

	[SqueezeBERT: What can computer vision teach NLP about efficient neural networks?](https://arxiv.org/abs/2006.11316)

70. **[T5](https://huggingface.co/docs/transformers/model_doc/t5)** 

	[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)

71. **[T5v1.1](https://huggingface.co/docs/transformers/model_doc/t5v1.1)** 

	[google-research/text-to-text-transfer-transformer](https://github.com/google-research/text-to-text-transfer-transformer/blob/main/released_checkpoints.md#t511)

72. **[TAPAS](https://huggingface.co/docs/transformers/model_doc/tapas)** 

	[TAPAS: Weakly Supervised Table Parsing via Pre-training](https://arxiv.org/abs/2004.02349)

73. **[Transformer-XL](https://huggingface.co/docs/transformers/model_doc/transformerxl)** 

	[Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/abs/1901.02860)

74. **[TrOCR](https://huggingface.co/docs/transformers/model_doc/trocr)** 

	[TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models](https://arxiv.org/abs/2109.10282)

75. **[UniSpeech](https://huggingface.co/docs/transformers/model_doc/unispeech)** 

	[UniSpeech: Unified Speech Representation Learning with Labeled and Unlabeled Data](https://arxiv.org/abs/2101.07597)

76. **[UniSpeechSat](https://huggingface.co/docs/transformers/model_doc/unispeech_sat)** 

	[UNISPEECH-SAT: UNIVERSAL SPEECH REPRESENTATION LEARNING WITH SPEAKER AWARE PRE-TRAINING](https://arxiv.org/abs/2110.05752)

77. **[Vision Transformer (ViT)](https://huggingface.co/docs/transformers/model_doc/vit)** 

	[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)

78. **[VisualBERT](https://huggingface.co/docs/transformers/model_doc/visual_bert)** 

	[VisualBERT: A Simple and Performant Baseline for Vision and Language](https://arxiv.org/pdf/1908.03557)

79. **[Wav2Vec2](https://huggingface.co/docs/transformers/model_doc/wav2vec2)** 

	[wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477) 

80. **[XLM](https://huggingface.co/docs/transformers/model_doc/xlm)** 

	[Cross-lingual Language Model Pretraining](https://arxiv.org/abs/1901.07291)

81. **[XLM-ProphetNet](https://huggingface.co/docs/transformers/model_doc/xlmprophetnet)** 

	[ProphetNet: Predicting Future N-gram for Sequence-to-Sequence Pre-training](https://arxiv.org/abs/2001.04063)

82. **[XLM-RoBERTa](https://huggingface.co/docs/transformers/model_doc/xlmroberta)** 

	[Unsupervised Cross-lingual Representation Learning at Scale](https://arxiv.org/abs/1911.02116)

83. **[XLNet](https://huggingface.co/docs/transformers/model_doc/xlnet)** 

	[XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237)

84. **[XLSR-Wav2Vec2](https://huggingface.co/docs/transformers/model_doc/xlsr_wav2vec2)** 

	[Unsupervised Cross-Lingual Representation Learning For Speech Recognition](https://arxiv.org/abs/2006.13979)

### 支持的框架

下表表示库中对每个模型的当前支持，无论它们是否具有Python tokenizer（"slow"）。由🤗 Tokenizers库支持的“fast” tokenizer(无论是否支持 Jax（通过 Flax），PyTorch 和/或TensorFlow)

| Model                       | Tokenizer slow | Tokenizer fast | PyTorch support | TensorFlow support | Flax Support |
| --------------------------- | -------------- | -------------- | --------------- | ------------------ | ------------ |
| ALBERT                      | ✅              | ✅              | ✅               | ✅                  | ✅            |
| BART                        | ✅              | ✅              | ✅               | ✅                  | ✅            |
| BEiT                        | ❌              | ❌              | ✅               | ❌                  | ✅            |
| BERT                        | ✅              | ✅              | ✅               | ✅                  | ✅            |
| Bert Generation             | ✅              | ❌              | ✅               | ❌                  | ❌            |
| BigBird                     | ✅              | ✅              | ✅               | ❌                  | ✅            |
| BigBirdPegasus              | ❌              | ❌              | ✅               | ❌                  | ❌            |
| Blenderbot                  | ✅              | ✅              | ✅               | ✅                  | ✅            |
| BlenderbotSmall             | ✅              | ✅              | ✅               | ✅                  | ✅            |
| CamemBERT                   | ✅              | ✅              | ✅               | ✅                  | ❌            |
| Canine                      | ✅              | ❌              | ✅               | ❌                  | ❌            |
| CLIP                        | ✅              | ✅              | ✅               | ❌                  | ✅            |
| ConvBERT                    | ✅              | ✅              | ✅               | ✅                  | ❌            |
| CTRL                        | ✅              | ❌              | ✅               | ✅                  | ❌            |
| DeBERTa                     | ✅              | ✅              | ✅               | ✅                  | ❌            |
| DeBERTa-v2                  | ✅              | ❌              | ✅               | ✅                  | ❌            |
| DeiT                        | ❌              | ❌              | ✅               | ❌                  | ❌            |
| DETR                        | ❌              | ❌              | ✅               | ❌                  | ❌            |
| DistilBERT                  | ✅              | ✅              | ✅               | ✅                  | ✅            |
| DPR                         | ✅              | ✅              | ✅               | ✅                  | ❌            |
| ELECTRA                     | ✅              | ✅              | ✅               | ✅                  | ✅            |
| Encoder decoder             | ❌              | ❌              | ✅               | ✅                  | ✅            |
| FairSeq Machine-Translation | ✅              | ❌              | ✅               | ❌                  | ❌            |
| FlauBERT                    | ✅              | ❌              | ✅               | ✅                  | ❌            |
| FNet                        | ✅              | ✅              | ✅               | ❌                  | ❌            |
| Funnel Transformer          | ✅              | ✅              | ✅               | ✅                  | ❌            |
| GPT Neo                     | ❌              | ❌              | ✅               | ❌                  | ✅            |
| GPT-J                       | ❌              | ❌              | ✅               | ❌                  | ✅            |
| Hubert                      | ❌              | ❌              | ✅               | ✅                  | ❌            |
| I-BERT                      | ❌              | ❌              | ✅               | ❌                  | ❌            |
| ImageGPT                    | ❌              | ❌              | ✅               | ❌                  | ❌            |
| LayoutLM                    | ✅              | ✅              | ✅               | ✅                  | ❌            |
| LayoutLMv2                  | ✅              | ✅              | ✅               | ❌                  | ❌            |
| LED                         | ✅              | ✅              | ✅               | ✅                  | ❌            |
| Longformer                  | ✅              | ✅              | ✅               | ✅                  | ❌            |
| LUKE                        | ✅              | ❌              | ✅               | ❌                  | ❌            |
| LXMERT                      | ✅              | ✅              | ✅               | ✅                  | ❌            |
| M2M100                      | ✅              | ❌              | ✅               | ❌                  | ❌            |
| Marian                      | ✅              | ❌              | ✅               | ✅                  | ✅            |
| mBART                       | ✅              | ✅              | ✅               | ✅                  | ✅            |
| MegatronBert                | ❌              | ❌              | ✅               | ❌                  | ❌            |
| MobileBERT                  | ✅              | ✅              | ✅               | ✅                  | ❌            |
| MPNet                       | ✅              | ✅              | ✅               | ✅                  | ❌            |
| mT5                         | ✅              | ✅              | ✅               | ✅                  | ✅            |
| OpenAI GPT                  | ✅              | ✅              | ✅               | ✅                  | ❌            |
| OpenAI GPT-2                | ✅              | ✅              | ✅               | ✅                  | ✅            |
| Pegasus                     | ✅              | ✅              | ✅               | ✅                  | ✅            |
| ProphetNet                  | ✅              | ❌              | ✅               | ❌                  | ❌            |
| QDQBert                     | ❌              | ❌              | ✅               | ❌                  | ❌            |
| RAG                         | ✅              | ❌              | ✅               | ✅                  | ❌            |
| Reformer                    | ✅              | ✅              | ✅               | ❌                  | ❌            |
| RemBERT                     | ✅              | ✅              | ✅               | ✅                  | ❌            |
| RetriBERT                   | ✅              | ✅              | ✅               | ❌                  | ❌            |
| RoBERTa                     | ✅              | ✅              | ✅               | ✅                  | ✅            |
| RoFormer                    | ✅              | ✅              | ✅               | ✅                  | ❌            |
| SegFormer                   | ❌              | ❌              | ✅               | ❌                  | ❌            |
| SEW                         | ❌              | ❌              | ✅               | ❌                  | ❌            |
| SEW-D                       | ❌              | ❌              | ✅               | ❌                  | ❌            |
| Speech Encoder decoder      | ❌              | ❌              | ✅               | ❌                  | ❌            |
| Speech2Text                 | ✅              | ❌              | ✅               | ❌                  | ❌            |
| Speech2Text2                | ✅              | ❌              | ❌               | ❌                  | ❌            |
| Splinter                    | ✅              | ✅              | ✅               | ❌                  | ❌            |
| SqueezeBERT                 | ✅              | ✅              | ✅               | ❌                  | ❌            |
| T5                          | ✅              | ✅              | ✅               | ✅                  | ✅            |
| TAPAS                       | ✅              | ❌              | ✅               | ✅                  | ❌            |
| Transformer-XL              | ✅              | ❌              | ✅               | ✅                  | ❌            |
| TrOCR                       | ❌              | ❌              | ✅               | ❌                  | ❌            |
| UniSpeech                   | ❌              | ❌              | ✅               | ❌                  | ❌            |
| UniSpeechSat                | ❌              | ❌              | ✅               | ❌                  | ❌            |
| Vision Encoder decoder      | ❌              | ❌              | ✅               | ❌                  | ✅            |
| VisionTextDualEncoder       | ❌              | ❌              | ✅               | ❌                  | ✅            |
| VisualBert                  | ❌              | ❌              | ✅               | ❌                  | ❌            |
| ViT                         | ❌              | ❌              | ✅               | ✅                  | ✅            |
| Wav2Vec2                    | ✅              | ❌              | ✅               | ✅                  | ✅            |
| XLM                         | ✅              | ❌              | ✅               | ✅                  | ❌            |
| XLM-RoBERTa                 | ✅              | ✅              | ✅               | ✅                  | ❌            |
| XLMProphetNet               | ✅              | ❌              | ✅               | ❌                  | ❌            |
| XLNet                       | ✅              | ✅              | ✅               | ✅                  | ❌            |
