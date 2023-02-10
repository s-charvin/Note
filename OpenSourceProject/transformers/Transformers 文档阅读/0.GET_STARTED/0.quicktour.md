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
data: 2021-12-07 11:06:40
lastmod: 2022-03-30 08:37:02
---

# Quick tour

快速浏览 🤗 Transformers 库功能。该库可以下载适用于自然语言理解 （NLU） 和自然语言生成 （NLG）的预训练模型，

## 使用 pipeline 开始执行任务

在给定任务上，可以轻松利用  [pipeline（）](https://huggingface.co/docs/transformers/master/en/main_classes/pipelines#transformers.pipeline) API 使用预训练模型。

🤗 Transformers 提供以下可以直接使用的功能：

**文本**

- Sentiment analysis: 对文本情感正负面进行分类。
- Text generation (in English): 给定输入生成文本。
- Name entity recognition (NER): 在输入句子中，用实际对象（人、日期、地点等）标记每个单词。
- Question answering: 为模型提供一些上下文和问题，从上下文中提取答案。
- Filling masked text: 给定包含屏蔽词的文本（替换为 `[MASK]`），填充空白。
- Summarization: 生成长文本或文档的摘要。
- Translation: 将文本翻译成另一种语言。
- Feature extraction: 返回文本的张量表示。

**图片**：

- Image classificatio：对图像进行分类。
- Image segmentation：对图像中的每个像素进行分类。
- Object detection：检测图像中的对象。

**音频**：

- Audio classification：为给定的音频片段分配标签。
- Automatic speech recognition (ASR)：将音频数据转录为文本。

> 有关 [pipeline（）](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline) 和相关任务的更多详细信息，请参阅[此处](https://huggingface.co/docs/transformers/main_classes/pipelines)的文档。

### Pipeline 使用方法

在以下示例中，你将使用 [pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline) 进行情感分析。

如果尚未安装以下依赖项，请安装以下依赖项：

```shell
pip install torch
```

导入 [pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline) 并指定要完成的任务：

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
```

pipeline会下载并缓存默认的 [预训练模型](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) 和 tokenizer，现在您就可以在目标文本上使用：`classifier` 对其进行情绪分析：

```python
classifier("We are very happy to show you the 🤗 Transformers library.")
# [{'label': 'POSITIVE', 'score': 0.9998}]
```

对于多个句子，将句子列表传递给[pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline)，该pipeline会返回一个对应的字典列表：

```python
results = classifier(["We are very happy to show you the 🤗 Transformers library.", "We hope you don't hate it."])
for result in results:
	print(f"label: {result['label']}, with score: {round(result['score'], 4)}")
# label: POSITIVE, with score: 0.9998
# label: NEGATIVE, with score: 0.5309
```

 [pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline) 还可以循环访问整个数据集。首先需要安装 [🤗 Datasets](https://huggingface.co/docs/datasets/) 库：

```shell
pip install datasets
```

根据要要实现的任务和要使用的模型创建[pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline) 然后将参数设置为将tensor放置在 CUDA 上：`device` `0`

```python
from transformers import pipeline

speech_recognizer = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h", device=0)
```

接下来，加载要循环访问的🤗 Datasets （更多详细信息，请参阅🤗 Datasets [快速入门](https://huggingface.co/docs/datasets/quickstart.html)）。例如，加载 [SUPERB 数据集](https://huggingface.co/datasets/superb)：

```python
import datasets

dataset = datasets.load_dataset("superb", name="asr", split="test")
```

可以传递整个dataset pipeline：

```python
files = dataset["file"]
speech_recognizer(files[:4])
# [{'text': 'HE HOPED THERE WOULD BE STEW FOR DINNER TURNIPS AND CARROTS AND BRUISED POTATOES AND FAT MUTTON PIECES TO BE LADLED OUT IN THICK PEPPERED FLOWER FAT AND SAUCE'},
# {'text': 'STUFFERED INTO YOU HIS BELLY COUNSELLED HIM'},
# {'text': 'AFTER EARLY NIGHTFALL THE YELLOW LAMPS WOULD LIGHT UP HERE AND THERE THE SQUALID QUARTER OF THE BROTHELS'},
# {'text': 'HO BERTIE ANY GOOD IN YOUR MIND'}]
```

对于输入较大的较大数据集（如语音或视觉），将需要传递generator，而不是在内存中加载所有输入。有关详细信息，请参阅[pipeline 文档](https://huggingface.co/docs/transformers/main_classes/pipelines)。

### 在管道中使用其他模型和分词器

[pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline) 可以调用 [Model Hub](https://huggingface.co/models)中的任何模型，从而可以轻松将[pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline) 应用到其他实例。例如，如果想要一个能够处理法语文本的模型，请使用Model Hub上的tags来筛选得到合适的模型。最顶部的筛选结果返回的是针对情绪分析进行微调的多语言[BERT model](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) 。

```python
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
```

使用 [AutoModelForSequenceClassification](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/auto#transformers.AutoModelForSequenceClassification) 和[‘AutoTokenizer’]加载预训练的模型及其关联的tokenizer：

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

然后，可以在[pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline)中指定模型和tokenizer, 并将`classifier`应用于目标文本：

```python
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
classifier("Nous sommes très heureux de vous présenter la bibliothèque 🤗 Transformers.")
# [{'label': '5 stars', 'score': 0.7273}]
```

I如果找不到适用于您的用例的模型，则需要根据数据微调(fine-tune)预训练模型，具体情况可以查看 [fine-tuning 教程](https://huggingface.co/docs/transformers/training) 。最后，在对预训练模型进行后，请考虑在Model Hub与社区上共享它([分享教程](https://huggingface.co/docs/transformers/model_sharing)) ! 🤗

## AutoClass

[AutoModelForSequenceClassification](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/auto#transformers.AutoModelForSequenceClassification) 和 [AutoTokenizer](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/auto#transformers.AutoTokenizer) 类协同工作，为 [pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline)提供支持。 [AutoClass](https://huggingface.co/docs/transformers/model_doc/auto)  是一种快捷方式，可根据预训练模型的名称或路径，自动检索其体系结构。您因此需要选择适合的任务，并将它与[AutoTokenizer](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/auto#transformers.AutoTokenizer)相关联。`AutoClass`

回到示例，看看如何使用`AutoClass`来重现[pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline)的结果。

### AutoTokenizer

tokenizer负责将文本预处理为模型可以理解的格式。首先，tokenizer会将文本拆分为称为*tokens*的单词。有多个规则用于管理tokenization过程,，包括如何拆分单词以及在哪个level (learn more about tokenization [here](https://huggingface.co/docs/transformers/tokenizer_summary))拆分。重要的是，需要使用相同的模型名称实例化tokenizer ，以确保使用的是模型预训练时使用的相同的tokenization规则。

使用[AutoTokenizer](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/auto#transformers.AutoTokenizer)加载tokenize：

```python
from transformers import AutoTokenizer

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

接下来，tokenizer将tokens转换为数字，以便构造tensor作为模型的输入，这称为模型的*vocabulary*。

将文本传递给tokenizer：

```python
encoding = tokenizer("We are very happy to show you the 🤗 Transformers library.")
print(encoding)
# {'input_ids': [101, 11312, 10320, 12495, 19308, 10114, 11391, 10855, 10103, 100, 58263, 13299, 119, 102],
# 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
```

tokenizer将返回一个字典，其中包含：

- [input_ids](https://huggingface.co/docs/transformers/glossary#input-ids): tokens数字表示。
- [atttention_mask](https://huggingface.co/docs/transformers/.glossary#attention-mask): 指示应关注哪些tokens。

像[pipeline()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/pipelines#transformers.pipeline)一样，tokenizer可以接受输入列表，此外，它可以填充和截断文本以返回长度统一的batch：

```python
pt_batch = tokenizer(
...     ["We are very happy to show you the 🤗 Transformers library.", "We hope you don't hate it."],padding=True,truncation=True,max_length=512,return_tensors="pt",)
```

查看 [preprocessing](https://huggingface.co/docs/transformers/preprocessing) 教程，了解有关tokenization的更多详细信息。

### AutoModel

🤗 Transformers 提供了一种简单而统一的方式来加载预训练的实例。这意味着您可以像加载[AutoTokenizer](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/auto#transformers.AutoTokenizer)一样加[AutoModel](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/auto#transformers.AutoModel) ，唯一的区别是需要为当前任务选择适合的[AutoModel](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/auto#transformers.AutoModel) 。本文正在做Text 或sequence分类，因此请加载[AutoModelForSequenceClassification](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/auto#transformers.AutoModelForSequenceClassification)。

```python
from transformers import AutoModelForSequenceClassification

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
pt_model = AutoModelForSequenceClassification.from_pretrained(model_name)
```

> 更多信息参阅 [task summary](https://huggingface.co/docs/transformers/task_summary) ，了解哪一个 [AutoModel](https://huggingface.co/docs/transformers/v4.17.0/en/model_doc/auto#transformers.AutoModel) 适用于哪一个任务。

现在，可以将预处理的输入batch直接传递给模型（注意：使用PyTorch 模型时，需要通过添加`**`来解压缩字典）：

```python
pt_outputs = pt_model(**pt_batch)
```

模型输出的final activations，在`logits` 属性中，因此对`logits`应用 softmax 函数就可以获得分类概率：

```python
from torch import nn

pt_predictions = nn.functional.softmax(pt_outputs.logits, dim=-1)
print(pt_predictions)
# tensor([[0.0021, 0.0018, 0.0115, 0.2121, 0.7725],
        [0.2084, 0.1826, 0.1969, 0.1755, 0.2365]], grad_fn=<SoftmaxBackward0>)
```

> 所有的🤗 Transformers 模型 (PyTorch or TensorFlow) 在最终激活函数（如softmax）之前输出tensors，because最终的激活函数通常与loss融合。

🤗 Transformers 模型是标准的 [`torch.nn.Module`](https://pytorch.org/docs/stable/nn.html#torch.nn.Module) 或[`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model) ，因此您可以在通常的训练中使用它们。但是，为了使事情变得更容易，🤗 Transformers为PyTorch提供了一个[Trainer](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/trainer#transformers.Trainer)类，该类添加了分布式训练(distributed training)，混合精度(mixed precision)等功能。对于TensorFlow，可以使用[Keras](https://keras.io/)的`fit`方法。更多信息可以查阅 [training tutorial](https://huggingface.co/docs/transformers/training) 。

> 🤗 Transformers模型的输出是一个特殊的数据类(dataclasse)，因此它们的属性会在IDE中自动生成。并且模型输出同tuple 或dictionary类似，可以使用整数, 切片或字符串进行索引，在这种情况下为 `None`的属性会被忽略。

### Save a model

微调后的模型和tokenizer，可以使用[PreTrainedModel.save_pretrained()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/model#transformers.PreTrainedModel.save_pretrained)保存：

```python
pt_save_directory = "./pt_save_pretrained"
tokenizer.save_pretrained(pt_save_directory)
pt_model.save_pretrained(pt_save_directory)
```

当您想要再次使用该模型时，可以使用[PreTrainedModel.from_pretrained()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)重新加载：

```python
pt_model = AutoModelForSequenceClassification.from_pretrained("./pt_save_pretrained")
```

🤗 Transformers 还有一个很酷的功能，可以通过给定的参数 `from_pt`或`from_tf`将保存的模型重新加载为PyTorch或TensorFlow模型，并且支持框架转换。

```python
from transformers import AutoModel

tokenizer = AutoTokenizer.from_pretrained(tf_save_directory)
pt_model = AutoModelForSequenceClassification.from_pretrained(tf_save_directory, from_tf=True)
```
