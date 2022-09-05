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
data: 2022-04-15 22:25:28
lastmod: 2022-04-15 23:11:19
---

# Tutorial

## DataPipes 获取数据流

假设我们要通过以下步骤从CSV文件加载数据：

- 目录中的所有 CSV 文件

- 加载 CSV 文件

- 解析 CSV 文件并生成行

一些内置的 [DataPipes](https://pytorch.org/data/beta/torchdata.datapipes.iter.html) 可以完成上述操作。

- `FileLister` - [列出目录中的文件](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.FileLister.html)
    
- `Filter` - [根据给定函数筛选DataPipe中的元素](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Filter.html)
    
- `FileOpener` - [使用文件路径并返回打开的文件数据流](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.FileOpener.html)
    
- `CSVParser` - [使用文件流，解析 CSV 内容，并一次返回一个解析的行](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.CSVParser.html)
    

 `CSVParser` 源代码示例：

```
@functional_datapipe("parse_csv")
class CSVParserIterDataPipe(IterDataPipe):
    def __init__(self, dp, **fmtparams) -> None:
        self.dp = dp
        self.fmtparams = fmtparams

    def __iter__(self) -> Iterator[Union[Str_Or_Bytes, Tuple[str, Str_Or_Bytes]]]:
        for path, file in self.source_datapipe:
            stream = self._helper.skip_lines(file)
            stream = self._helper.strip_newline(stream)
            stream = self._helper.decode(stream)
            yield from self._helper.return_path(stream, path=path)  # Returns 1 line at a time as List[str or bytes]
```

通过函数或类调用DataPipes：

```python
import torchdata.datapipes as dp

FOLDER = 'path/2/csv/folder' # 文件夹地址
datapipe = dp.iter.FileLister([FOLDER]).filter(filter_fn=lambda filename: filename.endswith('.csv')) # 获取所有的csv文件
datapipe = dp.iter.FileOpener(datapipe, mode='rt') # 获取datapipe内的文件数据流
datapipe = datapipe.parse_csv(delimiter=',') # 解析csv文件

for d in datapipe: # 可以通过迭代看一看获取的每一个csv文件的数
     pass
```

You can find the full list of built-in [IterDataPipes here](https://pytorch.org/data/beta/torchdata.datapipes.iter.html) and [MapDataPipes here](https://pytorch.org/data/beta/torchdata.datapipes.map.html).

### [Iterable-style DataPipes](https://pytorch.org/data/beta/torchdata.datapipes.iter.html)

An iterable-style dataset is an instance of a subclass of IterableDataset that implements the `__iter__()` protocol, and represents an iterable over data samples. This type of datasets is particularly suitable for cases where random reads are expensive or even improbable, and where the batch size depends on the fetched data.

For example, such a dataset, when called `iter(iterdatapipe)`, could return a stream of data reading from a database, a remote server, or even logs generated in real time.

This is an updated version of `IterableDataset` in `torch`.

#### CLASS torchdata.datapipes.iter.IterDataPipe(*args, **kwds)

Iterable-style DataPipe.

All DataPipes that represent an iterable of data samples should subclass this. This style of DataPipes is particularly useful when data come from a stream, or when the number of samples is too large to fit them all in memory.

All subclasses should overwrite `__iter__()`, which would return an iterator of samples in this DataPipe.

IterDataPipe is lazily initialized and its elements are computed only when `next()` is called on its iterator.

These DataPipes can be invoked in two ways, using the class constructor or applying their functional form onto an existing IterDataPipe (recommended, available to most but not all DataPipes). You can chain multiple IterDataPipe together to form a pipeline that will perform multiple operations in succession.

> When a subclass is used with `DataLoader`, each item in the DataPipe will be yielded from the `DataLoader` iterator. When `num_workers > 0`, each worker process will have a different copy of the DataPipe object, so it is often desired to configure each copy independently to avoid having duplicate data returned from the workers. `get_worker_info()`, when called in a worker process, returns information about the worker. It can be used in either the dataset’s `__iter__()` method or the `DataLoader` ‘s `worker_init_fn` option to modify each copy’s behavior.

```python

>>> from torchdata.datapipes.iter import IterableWrapper, Mapper
>>> dp = IterableWrapper(range(10))
>>> map_dp_1 = Mapper(dp, lambda x: x + 1)  # Using class constructor
>>> map_dp_2 = dp.map(lambda x: x + 1)  # Using functional form (recommended)
>>> list(map_dp_1)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(map_dp_2)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> filter_dp = map_dp_1.filter(lambda x: x % 2 == 0)
>>> list(filter_dp)
[2, 4, 6, 8, 10]
```

We have different types of Iterable DataPipes:

1. Archive - open and decompress archive files of different formats.
2. Augmenting - augment your samples (e.g. adding index, or cycle through indefinitely).
3. Combinatorial - perform combinatorial operations (e.g. sampling, shuffling).
4. Combining/Splitting - interact with multiple DataPipes by combining them or splitting one to many.
5. Grouping - group samples within a DataPipe
6. IO - interacting with the file systems or remote server (e.g. downloading, opening, saving files, and listing the files in directories).
7. Mapping - apply the a given function to each element in the DataPipe.
8. Others - perform miscellaneous set of operations.
9. Selecting - select specific samples within a DataPipe.
10. Text - parse, read, and transform text files and data

##### Archive DataPipes

These DataPipes help opening and decompressing archive files of different formats.

| [`Decompressor`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Decompressor.html#torchdata.datapipes.iter.Decompressor) | Takes tuples of path and compressed stream of data, and returns tuples of path and decompressed stream of data (functional name: `decompress`). |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`RarArchiveLoader`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.RarArchiveLoader.html#torchdata.datapipes.iter.RarArchiveLoader) | Decompresses rar binary streams from input Iterable Datapipes which contains tuples of path name and rar binary stream, and yields a tuple of path name and extracted binary stream (functional name: `load_from_rar`). |
| [`TarArchiveLoader`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.TarArchiveLoader.html#torchdata.datapipes.iter.TarArchiveLoader) | Opens/decompresses tar binary streams from an Iterable DataPipe which contains tuples of path name and tar binary stream, and yields a tuple of path name and extracted binary stream (functional name: `load_from_tar`). |
| [`XzFileLoader`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.XzFileLoader.html#torchdata.datapipes.iter.XzFileLoader) | Decompresses xz (lzma) binary streams from an Iterable DataPipe which contains tuples of path name and xy binary streams, and yields a tuple of path name and extracted binary stream (functional name: `load_from_xz`). |
| [`ZipArchiveLoader`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.ZipArchiveLoader.html#torchdata.datapipes.iter.ZipArchiveLoader) | Opens/decompresses zip binary streams from an Iterable DataPipe which contains a tuple of path name and zip binary stream, and yields a tuple of path name and extracted binary stream (functional name: `load_from_zip`). |

##### Augmenting DataPipes

These DataPipes help to augment your samples.

| [`Cycler`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Cycler.html#torchdata.datapipes.iter.Cycler) | Cycles the specified input in perpetuity by default, or for the specified number of times (functional name: `cycle`). |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`Enumerator`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Enumerator.html#torchdata.datapipes.iter.Enumerator) | Adds an index to an existing DataPipe through enumeration, with the index starting from 0 by default (functional name: `enumerate`). |
| [`IndexAdder`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.IndexAdder.html#torchdata.datapipes.iter.IndexAdder) | Adds an index to an existing Iterable DataPipe with (functional name: `add_index`). |

##### Combinatorial DataPipes

These DataPipes help to perform combinatorial operations.

| [`Sampler`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Sampler.html#torchdata.datapipes.iter.Sampler) | Generates sample elements using the provided `Sampler` (defaults to `SequentialSampler`). |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`Shuffler`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Shuffler.html#torchdata.datapipes.iter.Shuffler) | Shuffles the input DataPipe with a buffer (functional name: `shuffle`). |

##### Combining/Spliting DataPipes

These tend to involve multiple DataPipes, combining them or splitting one to many.

| [`Concater`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Concater.html#torchdata.datapipes.iter.Concater) | Concatenates multiple Iterable DataPipes (functional name: `concat`). |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`Demultiplexer`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Demultiplexer.html#torchdata.datapipes.iter.Demultiplexer) | Splits the input DataPipe into multiple child DataPipes, using the given classification function (functional name: `demux`). |
| [`Forker`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Forker.html#torchdata.datapipes.iter.Forker) | Creates multiple instances of the same Iterable DataPipe (functional name: `fork`). |
| [`IterKeyZipper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.IterKeyZipper.html#torchdata.datapipes.iter.IterKeyZipper) | Zips two IterDataPipes together based on the matching key (functional name: `zip_with_iter`). |
| [`MapKeyZipper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.MapKeyZipper.html#torchdata.datapipes.iter.MapKeyZipper) | Joins the items from the source IterDataPipe with items from a MapDataPipe (functional name: `zip_with_map`). |
| [`Multiplexer`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Multiplexer.html#torchdata.datapipes.iter.Multiplexer) | Yields one element at a time from each of the input Iterable DataPipes (functional name: `mux`). |
| [`SampleMultiplexer`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.SampleMultiplexer.html#torchdata.datapipes.iter.SampleMultiplexer) | Takes a Dict of (IterDataPipe, Weight), and yields items by sampling from these DataPipes with respect to their weights. |
| [`UnZipper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.UnZipper.html#torchdata.datapipes.iter.UnZipper) | Takes in a DataPipe of Sequences, unpacks each Sequence, and return the elements in separate DataPipes based on their position in the Sequence. |
| [`Zipper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Zipper.html#torchdata.datapipes.iter.Zipper) | Aggregates elements into a tuple from each of the input DataPipes (functional name: `zip`). |

##### Grouping DataPipes

These DataPipes have you group samples within a DataPipe.

| [`Batcher`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Batcher.html#torchdata.datapipes.iter.Batcher) | Creates mini-batches of data (functional name: `batch`).     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`BucketBatcher`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.BucketBatcher.html#torchdata.datapipes.iter.BucketBatcher) | Creates mini-batches of data from sorted bucket (functional name: `bucketbatch`). |
| [`Collator`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Collator.html#torchdata.datapipes.iter.Collator) | Collates samples from DataPipe to Tensor(s) by a custom collate function (functional name: `collate`). |
| [`Grouper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Grouper.html#torchdata.datapipes.iter.Grouper) | Groups data from input IterDataPipe by keys which are generated from `group_key_fn`, and yields a `DataChunk` with batch size up to `group_size` if defined (functional name: `groupby`). |
| [`UnBatcher`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.UnBatcher.html#torchdata.datapipes.iter.UnBatcher) | Undoes batching of data (functional name: `unbatch`).        |

##### IO DataPipes

These DataPipes help interacting with the file systems or remote server (e.g. downloading, opening, saving files, and listing the files in directories).

| [`FSSpecFileLister`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.FSSpecFileLister.html#torchdata.datapipes.iter.FSSpecFileLister) | Lists the contents of the directory at the provided `root` pathname or URL, and yields the full pathname or URL for each file within the directory. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`FSSpecFileOpener`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.FSSpecFileOpener.html#torchdata.datapipes.iter.FSSpecFileOpener) | Opens files from input datapipe which contains fsspec paths and yields a tuple of pathname and opened file stream (functional name: `open_file_by_fsspec`). |
| [`FSSpecSaver`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.FSSpecSaver.html#torchdata.datapipes.iter.FSSpecSaver) | Takes in a DataPipe of tuples of metadata and data, saves the data to the target path (generated by the filepath_fn and metadata), and yields the resulting fsspec path (functional name: `save_by_fsspec`). |
| [`FileLister`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.FileLister.html#torchdata.datapipes.iter.FileLister) | Given path(s) to the root directory, yields file pathname(s) (path + filename) of files within the root directory. |
| [`FileOpener`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.FileOpener.html#torchdata.datapipes.iter.FileOpener) | Given pathnames, opens files and yield pathname and file stream in a tuple. |
| [`GDriveReader`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.GDriveReader.html#torchdata.datapipes.iter.GDriveReader) | Takes URLs pointing at GDrive files, and yields tuples of file name and IO stream. |
| [`HttpReader`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.HttpReader.html#torchdata.datapipes.iter.HttpReader) | Takes file URLs (HTTP URLs pointing to files), and yields tuples of file URL and IO stream. |
| [`IoPathFileLister`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.IoPathFileLister.html#torchdata.datapipes.iter.IoPathFileLister) | Lists the contents of the directory at the provided `root` pathname or URL, and yields the full pathname or URL for each file within the directory. |
| [`IoPathFileOpener`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.IoPathFileOpener.html#torchdata.datapipes.iter.IoPathFileOpener) | Opens files from input datapipe which contains pathnames or URLs, and yields a tuple of pathname and opened file stream (functional name: `open_file_by_iopath`). |
| [`IoPathSaver`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.IoPathSaver.html#torchdata.datapipes.iter.IoPathSaver) | Takes in a DataPipe of tuples of metadata and data, saves the data to the target path which is generated by the `filepath_fn` and metadata, and yields the resulting path in iopath format (functional name: `save_by_iopath`). |
| [`OnlineReader`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.OnlineReader.html#torchdata.datapipes.iter.OnlineReader) | Takes file URLs (can be HTTP URLs pointing to files or URLs to GDrive files), and yields tuples of file URL and IO stream. |
| [`ParquetDataFrameLoader`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.ParquetDataFrameLoader.html#torchdata.datapipes.iter.ParquetDataFrameLoader) | Takes in paths to Parquet files and return a TorchArrow DataFrame for each row group within a Parquet file (functional name: `load_parquet_as_df`). |
| [`Saver`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Saver.html#torchdata.datapipes.iter.Saver) | Takes in a DataPipe of tuples of metadata and data, saves the data to the target path generated by the `filepath_fn` and metadata, and yields file path on local file system (functional name: `save_to_disk`). |

##### Mapping DataPipes

These DataPipes apply the a given function to each element in the DataPipe.

| [`FlatMapper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.FlatMapper.html#torchdata.datapipes.iter.FlatMapper) | Applies a function over each item from the source DataPipe, then flattens the outputs to a single, unnested IterDataPipe (functional name: `flatmap`). |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`Mapper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Mapper.html#torchdata.datapipes.iter.Mapper) | Applies a function over each item from the source DataPipe (functional name: `map`). |

##### Other DataPipes

A miscellaneous set of DataPipes with different functionalities.

| [`DataFrameMaker`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.DataFrameMaker.html#torchdata.datapipes.iter.DataFrameMaker) | Takes rows of data, batches a number of them together and creates TorchArrow DataFrames (functional name: `dataframe`). |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`EndOnDiskCacheHolder`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.EndOnDiskCacheHolder.html#torchdata.datapipes.iter.EndOnDiskCacheHolder) | Indicates when the result of prior DataPipe will be saved local files specified by `filepath_fn` (functional name: `end_caching`). |
| [`HashChecker`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.HashChecker.html#torchdata.datapipes.iter.HashChecker) | Computes and checks the hash of each file, from an input DataPipe of tuples of file name and data/stream (functional name: `check_hash`). |
| [`InMemoryCacheHolder`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.InMemoryCacheHolder.html#torchdata.datapipes.iter.InMemoryCacheHolder) | Stores elements from the source DataPipe in memory, up to a size limit if specified (functional name: `in_memory_cache`). |
| [`IterableWrapper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.IterableWrapper.html#torchdata.datapipes.iter.IterableWrapper) | Wraps an iterable object to create an IterDataPipe.          |
| [`OnDiskCacheHolder`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.OnDiskCacheHolder.html#torchdata.datapipes.iter.OnDiskCacheHolder) | Caches the outputs of multiple DataPipe operations to local files, which are typically performance bottleneck such download, decompress, and etc (functional name: `on_disk_cache`). |
| [`ShardingFilter`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.ShardingFilter.html#torchdata.datapipes.iter.ShardingFilter) | Wrapper that allows DataPipe to be sharded (functional name: `sharding_filter`). |

##### Selecting DataPipes

These DataPipes helps you select specific samples within a DataPipe.

| [`Filter`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Filter.html#torchdata.datapipes.iter.Filter) | Filters out elements from the source datapipe according to input `filter_fn` (functional name: `filter`). |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`Header`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Header.html#torchdata.datapipes.iter.Header) | Yields elements from the source DataPipe from the start, up to the specfied limit (functional name: `header`). |

##### Text DataPipes

These DataPipes help you parse, read, and transform text files and data.

| [`CSVDictParser`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.CSVDictParser.html#torchdata.datapipes.iter.CSVDictParser) | Accepts a DataPipe consists of tuples of file name and CSV data stream, reads and returns the contents within the CSV files one row at a time (functional name: `parse_csv_as_dict`). |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`CSVParser`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.CSVParser.html#torchdata.datapipes.iter.CSVParser) | Accepts a DataPipe consists of tuples of file name and CSV data stream, reads and returns the contents within the CSV files one row at a time (functional name: `parse_csv`). |
| [`JsonParser`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.JsonParser.html#torchdata.datapipes.iter.JsonParser) | Reads from JSON data streams and yields a tuple of file name and JSON data (functional name: `parse_json_files`). |
| [`LineReader`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.LineReader.html#torchdata.datapipes.iter.LineReader) | Accepts a DataPipe consisting of tuples of file name and string data stream, and for each line in the stream, yields a tuple of file name and the line (functional name: `readlines`). |
| [`ParagraphAggregator`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.ParagraphAggregator.html#torchdata.datapipes.iter.ParagraphAggregator) | Aggregates lines of text from the same file into a single paragraph (functional name: `lines_to_paragraphs`). |
| [`RoutedDecoder`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.RoutedDecoder.html#torchdata.datapipes.iter.RoutedDecoder) | Decodes binary streams from input DataPipe, yields pathname and decoded data in a tuple (functional name: `routed_decode`). |
| [`Rows2Columnar`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.Rows2Columnar.html#torchdata.datapipes.iter.Rows2Columnar) | Accepts an input DataPipe with batches of data, and processes one batch at a time and yields a Dict for each batch, with `column_names` as keys and lists of corresponding values from each row as values (functional name: `rows2columnar`). |
| [`StreamReader`](https://pytorch.org/data/beta/generated/torchdata.datapipes.iter.StreamReader.html#torchdata.datapipes.iter.StreamReader) | Given IO streams and their label names, yields bytes with label name in a tuple. |

### [Map-style DataPipes](https://pytorch.org/data/beta/torchdata.datapipes.map.html)

A Map-style DataPipe is one that implements the `__getitem__()` and `__len__()` protocols, and represents a map from (possibly non-integral) indices/keys to data samples.

For example, when accessed with `mapdatapipe[idx]`, could read the `idx`-th image and its corresponding label from a folder on the disk.

#### `CLASS torchdata.datapipes.map.MapDataPipe(*args, **kwds)`

Map-style DataPipe.

All datasets that represent a map from keys to data samples should subclass this. Subclasses should overwrite `__getitem__()`, supporting fetching a data sample for a given, unique key. Subclasses can also optionally overwrite `__len__()`, which is expected to return the size of the dataset by many `Sampler` implementations and the default options of `DataLoader`.

These DataPipes can be invoked in two ways, using the class constructor or applying their functional form onto an existing MapDataPipe (recommend, available to most but not all DataPipes).

> `DataLoader` by default constructs an index sampler that yields integral indices. To make it work with a map-style DataPipe with non-integral indices/keys, a custom sampler must be provided.

```python
>>> from torchdata.datapipes.map import SequenceWrapper, Mapper
>>> dp = SequenceWrapper(range(10))
>>> map_dp_1 = dp.map(lambda x: x + 1)  # Using functional form (recommended)
>>> list(map_dp_1)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> map_dp_2 = Mapper(dp, lambda x: x + 1)  # Using class constructor
>>> list(map_dp_2)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> batch_dp = map_dp_1.batch(batch_size=2)
>>> list(batch_dp)
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
```

Here is the list of available Map-style DataPipes:

| [`Batcher`](https://pytorch.org/data/beta/generated/torchdata.datapipes.map.Batcher.html#torchdata.datapipes.map.Batcher) | Create mini-batches of data (functional name: `batch`).      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`Concater`](https://pytorch.org/data/beta/generated/torchdata.datapipes.map.Concater.html#torchdata.datapipes.map.Concater) | Concatenate multiple Map DataPipes (functional name: `concat`). |
| [`IterToMapConverter`](https://pytorch.org/data/beta/generated/torchdata.datapipes.map.IterToMapConverter.html#torchdata.datapipes.map.IterToMapConverter) | Lazily load data from `IterDataPipe` to construct a `MapDataPipe` with the key-value pair generated by `key_value_fn` (functional name: `to_map_datapipe`). |
| [`Mapper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.map.Mapper.html#torchdata.datapipes.map.Mapper) | Apply the input function over each item from the source DataPipe (functional name: `map`). |
| [`SequenceWrapper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.map.SequenceWrapper.html#torchdata.datapipes.map.SequenceWrapper) | Wraps a sequence object into a MapDataPipe.                  |
| [`Shuffler`](https://pytorch.org/data/beta/generated/torchdata.datapipes.map.Shuffler.html#torchdata.datapipes.map.Shuffler) | Shuffle the input DataPipe via its indices (functional name: `shuffle`). |
| [`Zipper`](https://pytorch.org/data/beta/generated/torchdata.datapipes.map.Zipper.html#torchdata.datapipes.map.Zipper) | Aggregates elements into a tuple from each of the input DataPipes (functional name: `zip`). |

## DataLoader 加载数据

通过 DataPipe 使用 `DataLoader`。[首先使用`dataset=datapipe`作为`DataLoader`的输入参数](https://pytorch.org/docs/stable/data.html#single-and-multi-process-data-loading)。

随机生成一些数据

```python
import csv
import random

def generate_csv(file_label, num_rows: int = 5000, num_features: int = 20) -> None:
    fieldnames = ['label'] + [f'c{i}' for i in range(num_features)] #['label', 'c0', 'c1', ..., 'c19']
    writer = csv.DictWriter(open(f"sample_data{file_label}.csv", "w"), fieldnames=fieldnames) # 建立或打开sample_data{file_label}.csv文件
    writer.writerow({col: col for col in fieldnames})  # 写入头数据
    for i in range(num_rows):遍历所有行，每一行都
        row_data = {col: random.random() for col in fieldnames} # 生成每一列的对应特征数据
        row_data['label'] = random.randint(0, 9) # 生成第一列的对应标签
        writer.writerow(row_data) # 写入行数据

>>> ['label', 'c0', 'c1', ..., 'c19']
>>> ['0', '0.5', '0.4', ..., '0.4']
>>> .
>>> .
>>> .
>>> ['9', '0.9', '54', ..., '45']
```

构建 DataPipes 读取和解析CSV文件

```python
import numpy as np
import torchdata.datapipes as dp

def build_datapipes(root_dir="."):
    datapipe = dp.iter.FileLister(root_dir)
    datapipe = datapipe.filter(filter_fn=lambda filename: "sample_data" in filename and filename.endswith(".csv"))
    datapipe = dp.iter.FileOpener(datapipe, mode='rt')
    datapipe = datapipe.parse_csv(delimiter=",", skip_lines=1) # 解析csv数据，并跳过第一行头信息
    datapipe = datapipe.map(lambda row: {"label": np.array(row[0], np.int32),
                                         "data": np.array(row[1:], dtype=np.float64)})
    return datapipe
```

Lastly, we will put everything together in `'__main__'` and pass the DataPipe into the DataLoader.

```python
from torch.utils.data import DataLoader

if __name__ == '__main__':
    num_files_to_generate = 3
    for i in range(num_files_to_generate):
        generate_csv(file_label=i)
    datapipe = build_datapipes()
    dl = DataLoader(dataset=datapipe, batch_size=50, shuffle=True)
    first = next(iter(dl))
    labels, features = first['label'], first['data']
    print(f"Labels batch shape: {labels.size()}")
    print(f"Feature batch shape: {features.size()}")
```

The following statements will be printed to show the shapes of a single batch of labels and features.

```
Labels batch shape: 50
Feature batch shape: torch.Size([50, 20])
```

You can find more DataPipe implementation examples for various research domains [on this page](https://pytorch.org/data/beta/torchexamples.html).

## Implementing a Custom DataPipe

Currently, we already have a large number of built-in DataPipes and we expect them to cover most necessary data processing operations. If none of them supports your need, you can create your own custom DataPipe.

As a guiding example, let us implement an `IterDataPipe` that applies a callable to the input iterator. For `MapDataPipe`, take a look at the [map](https://github.com/pytorch/pytorch/tree/master/torch/utils/data/datapipes/map) folder for examples, and follow the steps below for the `__getitem__` method instead of the `__iter__` method.

### Naming

The naming convention for `DataPipe` is “Operation”-er, followed by `IterDataPipe` or `MapDataPipe`, as each DataPipe is essentially a container to apply an operation to data yielded from a source `DataPipe`. For succinctness, we alias to just “Operation-er” in **init** files. For our `IterDataPipe` example, we’ll name the module `MapperIterDataPipe` and alias it as `iter.Mapper` under `torchdata.datapipes`.

### Constructor

DataSets are now generally constructed as stacks of `DataPipes`, so each `DataPipe` typically takes a source `DataPipe` as its first argument. Here is a simplified version of Mapper as an example:

```python
from torchdata.datapipes.iter import IterDataPipe

class MapperIterDataPipe(IterDataPipe):
    def __init__(self, source_dp: IterDataPipe, fn) -> None:
        super().__init__()
        self.source_dp = source_dp
        self.fn = fn
```

Note:

- Avoid loading data from the source DataPipe in `__init__` function, in order to support lazy data loading and save memory.
- If `IterDataPipe` instance holds data in memory, please be ware of the in-place modification of data. When second iterator is created from the instance, the data may have already changed. Please take `IterableWrapper` [class](https://github.com/pytorch/pytorch/blob/master/torch/utils/data/datapipes/iter/utils.py) as reference to `deepcopy` data for each iterator.
- Avoid variables names that are taken by the functional names of existing DataPipes. For instance, `.filter` is is functional name that can be used to invoke `FilterIterDataPipe`. Having a variable named `filter` inside another `IterDataPipe` can lead to confusion.

### Iterator

For `IterDataPipes`, an `__iter__` function is needed to consume data from the source `IterDataPipe` then apply the operation over the data before `yield`.

```python
class MapperIterDataPipe(IterDataPipe):
    # ... See __init__() defined above

    def __iter__(self):
        for d in self.dp:
            yield self.fn(d)
```

### Length

In many cases, as in our `MapperIterDataPipe` example, the `__len__` method of a DataPipe returns the length of the source DataPipe.

```python
class MapperIterDataPipe(IterDataPipe):
    # ... See __iter__() defined above

    def __len__(self):
        return len(self.dp)
```

However, note that `__len__` is optional for `IterDataPipe` and often inadvisable. For `CSVParserIterDataPipe` in the using DataPipes section below, `__len__` is not implemented because the number of rows in each file is unknown before loading it. In some special cases, `__len__` can be made to either return an integer or raise an Error depending on the input. In those cases, the Error must be a `TypeError` to support Python’s build-in functions like `list(dp)`.

### Registering DataPipes with the functional API

Each DataPipe can be registered to support functional invocation using the decorator `functional_datapipe`.

```python
@functional_datapipe("map")
class MapperIterDataPipe(IterDataPipe):
   # ...
```

The stack of DataPipes can then be constructed using their functional forms (recommended) or class constructors:

```python
import torchdata.datapipes as dp

# Using functional form (recommended)
datapipes1 = dp.iter.FileOpener(['a.file', 'b.file']).map(fn=decoder).shuffle().batch(2)
# Using class constructors
datapipes2 = dp.iter.FileOpener(['a.file', 'b.file'])
datapipes2 = dp.iter.Mapper(datapipes2, fn=decoder)
datapipes2 = dp.iter.Shuffler(datapipes2)
datapipes2 = dp.iter.Batcher(datapipes2, 2)
```

In the above example, `datapipes1` and `datapipes2` represent the exact same stack of `IterDataPipe`s. We recommend using the functional form of DataPipes.
