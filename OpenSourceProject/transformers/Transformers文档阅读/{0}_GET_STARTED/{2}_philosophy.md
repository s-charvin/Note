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
data: 2021-12-07 11:07:03
lastmod: 2022-03-27 17:45:50
---

# 理念

🤗 Transformers 的设计有两个目标：

- 尽可能简单快捷地使用：
  
    - 严格限制了面向对象抽象概念的数量，只需要使用每个模型所需的三个标准类：[configuration](https://huggingface.co/docs/transformers/main_classes/configuration)、[models](https://huggingface.co/docs/transformers/main_classes/model)和[tokenizer](https://huggingface.co/docs/transformers/main_classes/tokenizer)。
    - 所有这些类都可以通过通用的 `from_pretrained()` 实例化方法从预先训练的实例以简单统一的方式进行初始化，通过 [Hugging Face Hub](https://huggingface.co/models) 提供的预训练的检查点(checkpoint)或者你自己保存的检查点(checkpoint)，下载 (如果需要), 缓存和加载相关的类实例和关联数据(超参数配置, tokenizers’ 词表, 和模型权重) 
    - 在这三个标准基类之上，该库提供了两个 API: [pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline)用于在给定任务上快速使用模型 (及其关联的 tokenizer 和 configuration) [Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer)/`Keras.fit` 用于快速训练或微调给定模型。
    - 因此, 该库不是一个用来建立神经网络块的模块化工具箱。如果你想基于此库进行扩展，只需使用常规的Python/PyTorch/TensorFlow/Keras模块，并继承此库的基类，以重用模型的功能。
- 提供最先进的模型，其性能尽可能接近原始模型：
  
    - 我们为每个架构都提供了至少一个示例，该示例再现了所述架构的官方作者提供的结果。
    - 代码通常尽可能接近原始代码库，这意味着一些PyTorch 代码不能像*pytorchic* 一样转换为TensorFlow 代码，反之亦然。

其他一些目标：

- 尽可能一致地公开模型的内部结构：
  
    - 使用单个 API 提供对完整隐藏状态和注意力权重的访问权限。
    - Tokenizer 和基本模型的 API 已标准化，可在模型之间轻松切换。
- 结合一些主观选择的有前途的 tools， 用来fine-tuning/investigating 这些模型:
  
    - 添加新的 tokens 到词表中，并嵌入以进行 fine-tuning。
    - mask and prune transformer heads.
- 简单的在PyTorch and TensorFlow 2.0之间进行切换, 允许使用一个框架进行训练，并使用另一个框架进行推理和预测。

## 主要概念

该库对每一个模型都基于三种类进行构建：

- **模型类(Model classes)** 如 [BertModel](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/bert#transformers.BertModel), 含有30多个 PyTorch ([torch.nn.Module](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)) 或 Keras ([tf.keras.Model](https://www.tensorflow.org/api_docs/python/tf/keras/Model)) 模型，能与库中提供的预训练权重一起使用。
- **配置类(Configuration classes)** 如 [BertConfig](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/bert#transformers.BertConfig)，它存储了构建模型所需的所有参数，如果仅仅只是使用预训练模型而不进行任何修改，则无需实例化此类，因为创建模型时会自动实例化配置。
- **Tokenizer classes** such as [BertTokenizer](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/bert#transformers.BertTokenizer)，存储了每个模型的vocabulary，并提供了对送入模型的 token embeddings indices 列表进行encoding/decoding 字符串的方法。

所有这些类都可以从预训练的实例中实例化，并使用两种方法保存在本地：

- `from_pretrained()` 允许从[Model Hub](https://huggingface.co/models)提供的或用户自有的预训练版本实例化一个 model/configuration/tokenizer。
- `save_pretrained()` 允许在本地保存 model/configuration/tokenizer，以便可以使用 `from_pretrained()`重新加载。
