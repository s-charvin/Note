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
data: 2021-12-07 11:06:55
lastmod: 2022-03-29 13:41:05
---

# 安装

安装🤗Transformers，并设置cache,以及将🤗Transformers配置为脱机运行。

官方测试环境: Python3.6+、PyTorch 1.1.0+、TensorFlow 2.0+和Flax

- [PyTorch](https://pytorch.org/get-started/locally/) 安装教程.
- [TensorFlow 2.0](https://www.tensorflow.org/install/pip) 安装教程.
- [Flax](https://flax.readthedocs.io/en/latest/) 安装教程.

## 使用 conda 安装

使用conda安装 `huggingface`:

```shell
conda install -c huggingface transformers
```

## 使用 pip 进行安装

使用以下命令安装 🤗 Transformers：

```shell
pip install transformers
```

对于仅支持CPU的系统，您可以仅使用一行命令方便地安装🤗Transformers 和深度学习库。例如，使用以下命令安装🤗Transformers和PyTorch：

```shell
pip install transformers[torch]
```

安装🤗  Transformers 和 TensorFlow 2.0：

```shell
pip install transformers[tf-cpu]
```

安装🤗 Transformers and Flax：

```shell
pip install transformers[flax]
```

最后，通过运行以下命令检查是否正确安装了🤗Transformers，它将下载一个预先训练好的模型：

```shell
python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"
```

然后打印出`label`和`score`：

```shell
[{'label': 'POSITIVE', 'score': 0.9998704791069031}]
```

## 从源文件安装

使用以下命令从源文件安装 🤗 Transformers：

```shell
pip install git+https://github.com/huggingface/transformers
```

此命令安装的是最新开发的 `master` 版本而不是 `stable` 版本。 `master` 版本对于了解最新进展非常有用。 

通过运行以下命令检查是否正确安装了🤗Transformers：

```shell
python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('I love you'))"
```

## Editable 安装

如果需要执行以下操作，则使用 Editable 安装：

- 使用源码的 `master` 版本。
- 为 🤗 Transformers 做出贡献，并测试代码中的更改。

使用以下命令克隆存储库并安装 🤗 Transformers：

```shell
git clone https://github.com/huggingface/transformers.git
cd transformers
pip install -e .
```

此命令将链接当前克隆的存储库文件夹和Python库路径。现在，除了常规Python库路径之外，Python还将查看当前克隆的文件夹。例如，如果您的Python包通常安装在 `~/anaconda3/envs/main/lib/python3.7/site-packages/`, Python还将搜索当前克隆的文件夹：`~/transformers/`.

如果您想继续使用库，则必须保留`Transformers`文件夹。

现在，可以使用以下命令轻松地将克隆库更新到最新版本的🤗Transformers：

```shell
cd ~/transformers/
git pull
```

## 缓冲设置

目前如果下载预先训练好的模型，模型将缓存在以下位置：`~/.cache/huggingFaces/Transers/`，此位置由shell 环境变量中的 TRANSFORMERS_CACHE 
 决定。在Windows上，默认目录为`C:\Users\username\.cache\huggingface\transformers`。可以按优先级顺序更改如下所示的shell 环境变量，以指定不同的缓存目录：

1. Shell environment variable (default): `TRANSFORMERS_CACHE`.
2. Shell environment variable: `HF_HOME` + `transformers/`.
3. Shell environment variable: `XDG_CACHE_HOME` + `/huggingface/transformers`.

如果使用过该库的早期版本并设置过相应的环境变量，则除非指定了 Shell 环境变量 `TRANSFORMERS_CACHE`，🤗 Transformers 将使用 shell 环境变量`PYTORCH_TRANSFORMERS_CACHE` 或 `PYTORCH_PRETRAINED_BERT_CACHE` 。

## 离线模式

 只需使用本地文件，🤗Transformers 就可以在离线环境中运行。设置环境变量`TRANSFORMERS_OFFLINE=1=1`以启用此行为。

通过设置环境变量 `HF_DATASETS_OFFLINE=1`，可以将 [🤗 Datasets](https://huggingface.co/docs/datasets/) 添加到离线训练工作流程中。

例如，通常会使用以下命令在有网络情况下运行实例程序：

```
python examples/pytorch/translation/run_translation.py --model_name_or_path t5-small --dataset_name wmt16 --dataset_config ro-en ...
```

但是也可以使用以下命令在离线情况下中运行相同的程序：

```
HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python examples/pytorch/translation/run_translation.py --model_name_or_path t5-small --dataset_name wmt16 --dataset_config ro-en ...
```

### 获取要脱机使用的 models 和tokenizers 

另一个离线使用 🤗 Transformers 的一个方法是提前下载好文件，然后在需要脱机使用它们时指向它们的本地路径。有如下三种实现途径:

- 点击↓图标，在[Model Hub](https://huggingface.co/models)的用户界面下载文件。

![download-icon](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/download-icon.png)

- 使用 [PreTrainedModel.from_pretrained()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) 和 [PreTrainedModel.save_pretrained()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/model#transformers.PreTrainedModel.save_pretrained) 工作流程:

  1. 使用[PreTrainedModel.from_pretrained()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained)提前下载好文件：
		```python
		from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
		tokenizer = AutoTokenizer.from_pretrained("bigscience/T0_3B")
		model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/T0_3B")
		```

  2. 使用 [PreTrainedModel.save_pretrained()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/model#transformers.PreTrainedModel.save_pretrained)保存文件到指定目录
		```python
		tokenizer.save_pretrained("./your/path/bigscience_t0")
		model.save_pretrained("./your/path/bigscience_t0")
		```

  3. 当处于离线状态时，使用[PreTrainedModel.from_pretrained()](https://huggingface.co/docs/transformers/v4.17.0/en/main_classes/model#transformers.PreTrainedModel.from_pretrained) 从指定目录加载文件：
		```python
		tokenizer = AutoTokenizer.from_pretrained("./your/path/bigscience_t0")
		model = AutoModel.from_pretrained("./your/path/bigscience_t0")
		```

- 使用[huggingface_hub](https://github.com/huggingface/huggingface_hub/tree/main/src/huggingface_hub)库以编程方式下载文件：

	1. 安装 `huggingface_hub` 库 ：

		```python
		python -m pip install huggingface_hub
		```

	2. 使用 [`hf_hub_download`](https://huggingface.co/docs/hub/adding-a-library#download-files-from-the-hub) 下载文件到指定路径。例如，以下命令将`config.json`文件从[T0](https://huggingface.co/bigscience/T0_3B)模型下载到您所需的路径：

		```python
		from huggingface_hub import hf_hub_download	
		hf_hub_download(repo_id="bigscience/T0_3B", filename="config.json", cache_dir="./your/path/bigscience_t0")
		```

	3. 下载文件并在本地缓存后，指定要加载和使用的本地路径：

		```python
		from transformers import AutoConfig
		
		config = AutoConfig.from_pretrained("./your/path/bigscience_t0/config.json")
		```

有关下载存储在中心上的文件的更多信息，可以参阅[如何从中心下载文件](https://huggingface.co/docs/hub/how-to-downstream)。
