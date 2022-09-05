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
data: 2022-04-07 19:01:10
lastmod: 2022-04-08 18:02:32
---

#  def __init__(self, mode: str, input_size: int, hidden_size: int,

变量初始化

```python
 self.mode = mode
 self.input_size = input_size
 self.hidden_size = hidden_size
 self.num_layers = num_layers
 self.bias = bias
 self.batch_first = batch_first
 self.dropout = float(dropout)
 self.bidirectional = bidirectional
 num_directions = 2 if bidirectional else 1
```

判断dropout值是不是数字类型，且其值在0-1之间。然后因为dropout是在所有循环层之后添加的，所以非零的dropout需要num_layers>1。

```python
 if not isinstance(dropout, numbers.Number) or not 0 <= dropout <= 1 or \
 	   isinstance(dropout, bool):
    raise ValueError("dropout should be a number in range [0, 1] "
 					"representing the probability of an element being "
 					"zeroed")
 if dropout > 0 and num_layers == 1:
    warnings.warn("dropout option adds dropout after all but last "
 				 "recurrent layer, so non-zero dropout expects "
 				 "num_layers greater than 1, but got dropout={} and "
 				 "num_layers={}".format(dropout, num_layers))
                          
```

 选择RNNbase 的模式

```python
 if mode == 'LSTM':
    gate_size = 4 * hidden_size
 elif mode == 'GRU':
    gate_size = 3 * hidden_size
 elif mode == 'RNN_TANH':
    gate_size = hidden_size
 elif mode == 'RNN_RELU':
    gate_size = hidden_size
 else:
    raise ValueError("Unrecognized RNN mode: " + mode)
```

每一次，当我们创建新的RNNbase实例时，它都会为每一层，每一方向构造新的w_ih、w_hh、b_ih、b_hh参数张量，并将其注册为专属于当前层当前方向的类属性值，最后初始化参数。

 但上述操作无法保证新的参数张量在GPU内存上是连续的，性能可能会因为碎片化存储而下降。因此，在构造函数的末尾调用flatten_parameters()函数，将所有参数张量聚合到GPU内存的连续空间中。

```python
 self._flat_weights_names = []
 self._all_weights = []
 for layer in range(num_layers):
    for direction in range(num_directions):
 	   layer_input_size = input_size if layer == 0 else hidden_size * num_directions

 	   w_ih = Parameter(torch.Tensor(gate_size, layer_input_size))
 	   w_hh = Parameter(torch.Tensor(gate_size, hidden_size))
 	   b_ih = Parameter(torch.Tensor(gate_size))
 	   # Second bias vector included for CuDNN compatibility. Only one
 	   # bias vector is needed in standard definition.
 	   b_hh = Parameter(torch.Tensor(gate_size))
 	   layer_params = (w_ih, w_hh, b_ih, b_hh)

 	   suffix = '_reverse' if direction == 1 else ''
 	   param_names = ['weight_ih_l{}{}', 'weight_hh_l{}{}']
 	   if bias:
 		   param_names += ['bias_ih_l{}{}', 'bias_hh_l{}{}']
 	   param_names = [x.format(layer, suffix) for x in param_names]

 	   for name, param in zip(param_names, layer_params):
 		   setattr(self, name, param)
 	   self._flat_weights_names.extend(param_names)
 	   self._all_weights.append(param_names)

 self._flat_weights = [(lambda wn: getattr(self, wn) if hasattr(
    self, wn) else None)(wn) for wn in self._flat_weights_names]
 self.flatten_parameters()
 self.reset_parameters()
```

#  def forward(self, input: Tensor, hx: Optional[Tensor] = None) -> Tuple[Tensor, Tensor]:

获取batch格式及其大小，一种是tensor型矩阵，一种是经过PackedSequence处理的格式。

```python
 is_packed = isinstance(input, PackedSequence)
 if is_packed:
    input, batch_sizes, sorted_indices, unsorted_indices = input
    max_batch_size = batch_sizes[0]
    max_batch_size = int(max_batch_size)
 else:
    batch_sizes = None
    max_batch_size = input.size(
 	   0) if self.batch_first else input.size(1)
    sorted_indices = None
    unsorted_indices = None

```

获取隐藏层向量hx，x代表第几层循环层。每batch的隐藏层向都应该与输入序列相匹配。其中使用的permute_hidden()函数，在输入为PackedSequence格式时，对hx进沿着sorted_indices进行张量索引，否则使用原hx。

```python

 if hx is None:
    num_directions = 2 if self.bidirectional else 1
    hx = torch.zeros(self.num_layers * num_directions,
 					max_batch_size, self.hidden_size,
 					dtype=input.dtype, device=input.device)
 else:
    # Each batch of the hidden state should match the input sequence that
    # the user believes he/she is passing in.
    hx = self.permute_hidden(hx, sorted_indices)
```

检查输入数据维度，当输入格式为PackedSequence格式时，输入维度应为2，否则为3；检查隐藏层向量维度，是否为`(self.num_layers * num_directions,mini_batch_size, self.hidden_size)`；定义RNN底层计算函数，`RNN_TANH` 或 `RNN_RELU`。

```python
 self.check_forward_args(input, hx, batch_sizes)
 _impl = _rnn_impls[self.mode]
```

使用底层C++代码，计算获取输出，同时将输出更新成与输入相同的格式。

```python
 if batch_sizes is None:
    result = _impl(input, hx, self._flat_weights, self.bias, self.num_layers,
 				  self.dropout, self.training, self.bidirectional, self.batch_first)
 else:
    result = _impl(input, batch_sizes, hx, self._flat_weights, self.bias,
 				  self.num_layers, self.dropout, self.training, self.bidirectional)
 output = result[0]
 hidden = result[1]

 if is_packed:
    output = PackedSequence(
 	   output, batch_sizes, sorted_indices, unsorted_indices)
 return output, self.permute_hidden(hidden, unsorted_indices)

```

# C++底层重点代码实现

## apply_layer_stack

此函数首先使用`TORCH_CHECK`检查了循环层数是否一致，然后使用`layer`对输入数据进行运算得到`layer_output`，并将其中的`.outputs`作为下一时刻`layer`的input，然后复制`layer_output`中的最后一个隐藏层向量`final_hidden`的值，添加到`final_hiddens`的最后面。同时如果有`dropout`则会调用dropout函数。

```c++
template<typename io_type, typename hidden_type, typename weight_type>
LayerOutput<io_type, std::vector<hidden_type>>
apply_layer_stack(const Layer<io_type, hidden_type, weight_type>& layer, const io_type& input,
                  const std::vector<hidden_type>& hiddens, const std::vector<weight_type>& weights,
                  int64_t num_layers, double dropout_p, bool train) {
  TORCH_CHECK(num_layers == (int64_t)hiddens.size(), "Expected more hidden states in stacked_rnn");
  TORCH_CHECK(num_layers == (int64_t)weights.size(), "Expected more weights in stacked_rnn");

  auto layer_input = input;
  auto hidden_it = hiddens.begin();
  auto weight_it = weights.begin();
  std::vector<hidden_type> final_hiddens;
  for (const auto l : c10::irange(num_layers)) {
    auto layer_output = layer(layer_input, *(hidden_it++), *(weight_it++));
    final_hiddens.push_back(layer_output.final_hidden);
    layer_input = layer_output.outputs;

    if (dropout_p != 0 && train && l < num_layers - 1) {
      layer_input = dropout(layer_input, dropout_p);
    }
  }

  return {layer_input, final_hiddens};
}
```

## rnn

### _rnn_impl

根据hidden_type指定使用相应的`rnn_relu_cell`、`rnn_tanh_cell`、`lstm_cell`、`gru_cell`作为`layer`输入`apply_layer_stack`到进行运算。

```c++
template<typename CellType, template<typename,typename> class LayerT, template<typename,typename> class BidirLayerT, typename cell_params, typename io_type>
LayerOutput<io_type, std::vector<typename CellType::hidden_type>> _rnn_impl(
      const io_type& input,
      const std::vector<cell_params>& params,
      const std::vector<typename CellType::hidden_type>& hiddens,
      int64_t num_layers, double dropout_p, bool train, bool bidirectional) {
  using hidden_type = typename CellType::hidden_type;
  CellType cell;
  if (bidirectional) {
    using BidirLayer = BidirLayerT<hidden_type, cell_params>;
    auto bidir_result = apply_layer_stack(BidirLayer{cell}, input, pair_vec(hiddens), pair_vec(params), num_layers, dropout_p, train);
    return {bidir_result.outputs, unpair_vec(std::move(bidir_result.final_hidden))};
  } else {
    return apply_layer_stack(LayerT<hidden_type,cell_params>{cell}, input, hiddens, params, num_layers, dropout_p, train);
  }
}
```

### _rnn_impl_with_concat

```c++

template<typename CellType, template<typename,typename> class LayerT, template<typename,typename> class BidirLayerT, typename cell_params, typename io_type>
std::tuple<io_type, Tensor> _rnn_impl_with_concat(
      const io_type& input,
      const std::vector<cell_params>& params,
      const std::vector<typename CellType::hidden_type>& hiddens,
      int64_t num_layers, double dropout_p, bool train, bool bidirectional) {
  auto result = _rnn_impl<CellType, LayerT, BidirLayerT>(input, params, hiddens, num_layers, dropout_p, train, bidirectional);
  return std::make_tuple(std::move(result.outputs), at::stack(result.final_hidden, 0));
}
```

## lstm

### _lstm_impl

以`_rnn_impl` 为基，调整`hiddens`，输入进行运算。

```c++
template<template<typename,typename> class LayerT, template<typename,typename> class BidirLayerT, typename cell_params, typename io_type>
std::tuple<io_type, Tensor, Tensor> _lstm_impl(
      const io_type& input,
      const std::vector<cell_params>& params, const Tensor& hx, const Tensor& cx,
      int64_t num_layers, double dropout_p, bool train, bool bidirectional) {
  // It's much more useful for us to work on lists of pairs of hx and cx for each layer, so we need
  // to transpose a pair of those tensors.
  auto layer_hx = hx.unbind(0);
  auto layer_cx = cx.unbind(0);
  int64_t total_layers = layer_hx.size();
  std::vector<typename LSTMCell<cell_params>::hidden_type> hiddens;
  hiddens.reserve(total_layers);
  for (const auto i : c10::irange(total_layers)) {
    hiddens.emplace_back(std::move(layer_hx[i]), std::move(layer_cx[i]));
  }

  auto result = _rnn_impl<LSTMCell<cell_params>, LayerT, BidirLayerT>(input, params, hiddens, num_layers, dropout_p, train, bidirectional);

  // Now, we need to reverse the transposed we performed above.
  std::vector<Tensor> hy, cy;
  hy.reserve(total_layers); cy.reserve(total_layers);
  for (auto & hidden : result.final_hidden) {
    hy.push_back(std::move(std::get<0>(hidden)));
    cy.push_back(std::move(std::get<1>(hidden)));
  }

  return std::make_tuple(std::move(result.outputs), at::stack(hy, 0), at::stack(cy, 0));
}

} // anonymous namespace
```

### lstm

```c++
std::tuple<Tensor, Tensor, Tensor> lstm(
      const Tensor& _input, TensorList hx,
      TensorList _params, bool has_biases,
      int64_t num_layers, double dropout_p, bool train, bool bidirectional, bool batch_first) {
  TORCH_CHECK(hx.size() == 2, "lstm expects two hidden states");
  if (at::cudnn_is_acceptable(_input)) {
    Tensor output, hy, cy;
    lstm_cudnn_stub(_input.device().type(), output, hy, cy, _input, hx, _params, has_biases,
            num_layers, dropout_p, train, bidirectional, batch_first);
    return std::make_tuple(std::move(output), std::move(hy), std::move(cy));
  }
  // if cells are of different size, that means projections are used
  bool has_projections = (hx[0].size(2) != hx[1].size(2));
  if (use_miopen(_input, dropout_p)) {
    if (!has_projections) {
      Tensor output, hy, cy;
      lstm_miopen_stub(_input.device().type(), output, hy, cy, _input, hx, _params, has_biases,
                num_layers, dropout_p, train, bidirectional, batch_first);
      return std::make_tuple(std::move(output), std::move(hy), std::move(cy));
    } else {
      TORCH_WARN_ONCE(
          "LSTM with projections is not supported with MIOpen. Using default implementation.");
    }
  }

  check_attributes(_input, _params, hx);
  auto input = batch_first ? _input.transpose(0, 1) : _input;
  auto params = gather_params(_params, has_biases, has_projections);
  auto results = _lstm_impl<FullLayer, FullBidirectionalLayer>(
      input, params, hx[0], hx[1], num_layers, dropout_p, train, bidirectional);
  if (batch_first) {
    std::get<0>(results) = std::get<0>(results).transpose(0, 1);
  }
  return results;
}
```

## gru

```c++

```

## Cell

### rnn_relu_cell 和 rnn_tanh_cell

```C++
Tensor rnn_tanh_cell(
    const Tensor& input, const Tensor& hx,
    const Tensor& w_ih, const Tensor& w_hh, const c10::optional<Tensor>& b_ih_opt, const c10::optional<Tensor>& b_hh_opt) {
  // See [Note: hacky wrapper removal for optional tensor]
  c10::MaybeOwned<Tensor> b_ih_maybe_owned = at::borrow_from_optional_tensor(b_ih_opt);
  const Tensor& b_ih = *b_ih_maybe_owned;
  const Tensor& b_hh = c10::value_or_else(b_hh_opt, [] {return Tensor();});

  static at::Tensor undefined;
  check_rnn_cell_forward_input(input, w_ih.size(1));
  check_rnn_cell_forward_hidden(input, hx, w_hh.size(1), 0);
  return SimpleCell<tanh_f, CellParams>{}(input, hx, CellParams{w_ih, w_hh, b_ih, b_hh, undefined});
}

Tensor rnn_relu_cell(
    const Tensor& input, const Tensor& hx,
    const Tensor& w_ih, const Tensor& w_hh, const c10::optional<Tensor>& b_ih_opt, const c10::optional<Tensor>& b_hh_opt) {
  // See [Note: hacky wrapper removal for optional tensor]
  c10::MaybeOwned<Tensor> b_ih_maybe_owned = at::borrow_from_optional_tensor(b_ih_opt);
  const Tensor& b_ih = *b_ih_maybe_owned;
  const Tensor& b_hh = c10::value_or_else(b_hh_opt, [] {return Tensor();});

  static at::Tensor undefined;
  check_rnn_cell_forward_input(input, w_ih.size(1));
  check_rnn_cell_forward_hidden(input, hx, w_hh.size(1), 0);
  return SimpleCell<relu_f, CellParams>{}(input, hx, CellParams{w_ih, w_hh, b_ih, b_hh, undefined});
}

```

#### SimpleCell

```c++
template<typename nonlinearity, typename cell_params>
struct SimpleCell : Cell<Tensor, cell_params> {
  using hidden_type = Tensor;
  Tensor operator()(
      const Tensor& input,
      const Tensor& hidden,
      const cell_params& params,
      bool pre_compute_input = false) const override {
    return nonlinearity{}(
      params.linear_hh(hidden).add_(
        pre_compute_input ? input : params.linear_ih(input)
        )
        );
  }
};
```

### gru_cell

```C++
Tensor gru_cell(
    const Tensor& input, const Tensor& hx,
    const Tensor& w_ih, const Tensor& w_hh, const c10::optional<Tensor>& b_ih_opt, const c10::optional<Tensor>& b_hh_opt) {
  // See [Note: hacky wrapper removal for optional tensor]
  c10::MaybeOwned<Tensor> b_ih_maybe_owned = at::borrow_from_optional_tensor(b_ih_opt);
  const Tensor& b_ih = *b_ih_maybe_owned;
  const Tensor& b_hh = c10::value_or_else(b_hh_opt, [] {return Tensor();});

  check_rnn_cell_forward_input(input, w_ih.size(1));
  check_rnn_cell_forward_hidden(input, hx, w_hh.size(1), 0);
  static at::Tensor undefined;
  return GRUCell<CellParams>{}(input, hx, CellParams{w_ih, w_hh, b_ih, b_hh, undefined});
}
```

#### GRUCell

```c++
template <typename cell_params>
struct GRUCell : Cell<Tensor, cell_params> {
  using hidden_type = Tensor;

  hidden_type operator()(
      const Tensor& input,
      const hidden_type& hidden,
      const cell_params& params,
      bool pre_compute_input = false) const override {
    if (input.is_cuda()) {
      TORCH_CHECK(!pre_compute_input);
      auto igates = params.matmul_ih(input);
      auto hgates = params.matmul_hh(hidden);
      auto result = at::_thnn_fused_gru_cell(
          igates, hgates, hidden, params.b_ih(), params.b_hh());
      // Slice off the workspace argument (it's needed only for AD).
      return std::move(std::get<0>(result));
    }
    const auto chunked_igates = pre_compute_input
        ? input.unsafe_chunk(3, 1)
        : params.linear_ih(input).unsafe_chunk(3, 1);
    auto chunked_hgates = params.linear_hh(hidden).unsafe_chunk(3, 1);
    const auto reset_gate =
        chunked_hgates[0].add_(chunked_igates[0]).sigmoid_();
    const auto input_gate =
        chunked_hgates[1].add_(chunked_igates[1]).sigmoid_();
    const auto new_gate =
        chunked_igates[2].add(chunked_hgates[2].mul_(reset_gate)).tanh_();
    return (hidden - new_gate).mul_(input_gate).add_(new_gate);
  }
};
```

### lstm_cell

```c++
std::tuple<Tensor, Tensor> lstm_cell(
    const Tensor& input, TensorList hx,
    const Tensor& w_ih, const Tensor& w_hh, const c10::optional<Tensor>& b_ih_opt, const c10::optional<Tensor>& b_hh_opt) {
  // See [Note: hacky wrapper removal for optional tensor]
  c10::MaybeOwned<Tensor> b_ih_maybe_owned = at::borrow_from_optional_tensor(b_ih_opt);
  const Tensor& b_ih = *b_ih_maybe_owned;
  const Tensor& b_hh = c10::value_or_else(b_hh_opt, [] {return Tensor();});

  TORCH_CHECK(hx.size() == 2, "lstm_cell expects two hidden states");
  check_rnn_cell_forward_input(input, w_ih.size(1));
  auto hidden_size = w_hh.size(1);
  check_rnn_cell_forward_hidden(input, hx[0], hidden_size, 0);
  check_rnn_cell_forward_hidden(input, hx[1], hidden_size, 0);
  static at::Tensor undefined;
  return LSTMCell<CellParams>{}(input, std::make_tuple(hx[0], hx[1]), CellParams{w_ih, w_hh, b_ih, b_hh, undefined});
}
```

#### LSTMCell

```c++
template <typename cell_params>
struct LSTMCell : Cell<std::tuple<Tensor, Tensor>, cell_params> {
  using hidden_type = std::tuple<Tensor, Tensor>;

  hidden_type operator()(
      const Tensor& input,
      const hidden_type& hidden,
      const cell_params& params,
      bool pre_compute_input = false) const override {
    const auto& hx = std::get<0>(hidden);
    const auto& cx = std::get<1>(hidden);

    if (input.is_cuda()) {
      TORCH_CHECK(!pre_compute_input);
      auto igates = params.matmul_ih(input);
      auto hgates = params.matmul_hh(hx);
      auto result = at::_thnn_fused_lstm_cell(
          igates, hgates, cx, params.b_ih(), params.b_hh());
      // applying projections if w_hr is defined
      auto hy = params.matmul_hr(std::get<0>(result));
      // Slice off the workspace argument (it's needed only for AD).
      return std::make_tuple(std::move(hy), std::move(std::get<1>(result)));
    }

    const auto gates = params.linear_hh(hx).add_(
        pre_compute_input ? input : params.linear_ih(input));
    auto chunked_gates = gates.unsafe_chunk(4, 1);
    auto ingate = chunked_gates[0].sigmoid_();
    auto forgetgate = chunked_gates[1].sigmoid_();
    auto cellgate = chunked_gates[2].tanh_();
    auto outgate = chunked_gates[3].sigmoid_();
    auto cy = (forgetgate * cx).add_(ingate * cellgate);
    auto hy = outgate * cy.tanh();
    hy = params.matmul_hr(hy);
    return std::make_tuple(std::move(hy), std::move(cy));
  }

};
```
