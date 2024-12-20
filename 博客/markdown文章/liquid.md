

# 基础

## 简介

Liquid 代码可分为 **对象（object）**、**标记（tag）** 和 **过滤器（filter）**。

### 对象

**对象** 告诉 Liquid 在页面的哪个位置展示内容。对象和变量名由双花括号标识：`{{` 和 `}}`。

输入

```
{{ page.title }}
```

输出

```
Introduction
```

上述实例中，Liquid 输出 `page.title` 对象的内容，此对象保存的是文本 `Introduction`。

### 标记（tag）

**标记（tag）** 创造了模板的逻辑和控制流。他们由单括号加百分号标识：`{%` 和 `%}`。

标记（tag）并不产生任何可见的文本输出。这意味着你可以用他们为变量赋值、创建条件和循环逻辑，并且不在页面上显示出任何 Liquid 逻辑代码。

输入

```
{% if user %}
  Hello {{ user.name }}!
{% endif %}
```

输出

```
Hello Adam!
```

标记被分为三类：

- [控制流](https://liquid.bootcss.com/tags/control-flow)
- [迭代](https://liquid.bootcss.com/tags/iteration)
- [变量赋值](https://liquid.bootcss.com/tags/variable)

你可以在每一类标记所对应的章节了解更多信息。

### 过滤器

**过滤器** 改变 Liquid 对象的输出。他们被用在输出上，通过一个 `|` 符号分隔。

输入

```
{{ "/my/fancy/url" | append: ".html" }}
```

输出

```
/my/fancy/url.html
```

多个过滤器可以共同作用于同一个输出，并按照从左到右的顺序执行。

输入

```
{{ "adam!" | capitalize | prepend: "Hello " }}
```

输出

```
Hello Adam!
```

## 操作符

Liquid 包含了大量逻辑（logical）和比较操作符（comparison operator）。

### 基本操作符

| `==`  | 相等       |
| ----- | ---------- |
| `!=`  | 不相等     |
| `>`   | 大于       |
| `<`   | 小于       |
| `>=`  | 大于或等于 |
| `<=`  | 小于或等于 |
| `or`  | 逻辑或     |
| `and` | 逻辑与     |

例如：

```
{% if product.title == "Awesome Shoes" %}
  These shoes are awesome!
{% endif %}
```

可以在一个标记（tag）中使用多个操作符：

```
{% if product.type == "Shirt" or product.type == "Shoes" %}
  This is a shirt or a pair of shoes.
{% endif %}
```

### contains（包含）

`contains` 用于检查在一个字符串中是否存在某个子串。

```
{% if product.title contains 'Pack' %}
  This product's title contains the word Pack.
{% endif %}
```

`contains` 还可以用于检查一个字符串数组中是否存在某个字符串。

```
{% if product.tags contains 'Hello' %}
  This product has been tagged with 'Hello'.
{% endif %}
```

`contains` 只能用于搜索字符串。你不能将其用于从一个对象数组中检查是否存在某个对象。

## 真值与假值

编程时，在条件判断中任何返回 `true` 的都被叫做 **真值（truthy）**。任何返回 `false` 的都被叫做 **假值（falsy）**。所有的对象（object）类型都可以被描述为真值（truthy）或假值（falsy）。

- [Truthy](https://liquid.bootcss.com/basics/truthy-and-falsy/#truthy)
- [Falsy](https://liquid.bootcss.com/basics/truthy-and-falsy/#falsy)
- [Summary](https://liquid.bootcss.com/basics/truthy-and-falsy/#summary)

### 真值（Truthy）

除了 `nil` 和 `false` 之外的所有值都是真值。

如下例，字符串 “Tobi” 虽不是布尔类型，但是其在条件判断时被当做真值（truthy）：

```
{% assign tobi = "Tobi" %}

{% if tobi %}
  This condition will always be true.
{% endif %}
```

[字符串（String）](https://liquid.bootcss.com/basics/types/#string)，即便是空字符串，也是真值（truthy）。如下例，如果 `settings.fp_heading` 是个空字符串将会输出空 HTML 标签：

输入

```
{% if settings.fp_heading %}
  <h1>{{ settings.fp_heading }}</h1>
{% endif %}
```

输出

```
<h1></h1>
```

### 假值（Falsy）

在 Liquid 中，[`nil`](https://liquid.bootcss.com/basics/types/#nil) 和 [`false`](https://liquid.bootcss.com/basics/types/#boolean) 是假值。

### 总结

下表总结了在 Liquid 中什么是真值什么是假值。

|              | 真值（truthy） | 假值（falsy） |
| :----------: | :------------: | :-----------: |
|     true     |       •        |               |
|    false     |                |       •       |
|     nil      |                |       •       |
|    string    |       •        |               |
| empty string |       •        |               |
|      0       |       •        |               |
|   integer    |       •        |               |
|    float     |       •        |               |
|    array     |       •        |               |
| empty array  |       •        |               |
|     page     |       •        |               |
|  EmptyDrop   |       •        |               |

## 数据类型

Liquid 对象的类型可以是以下五种：

- [String](https://liquid.bootcss.com/basics/types/#string)
- [Number](https://liquid.bootcss.com/basics/types/#number)
- [Boolean](https://liquid.bootcss.com/basics/types/#boolean)
- [Nil](https://liquid.bootcss.com/basics/types/#nil)
- [Array](https://liquid.bootcss.com/basics/types/#array)

你可以通过 [assign](https://liquid.bootcss.com/tags/variable/#assign) 或 [capture](https://liquid.bootcss.com/tags/variable/#capture) 标记来初始化 Liquid 变量。

### String（字符串）

将变量的值包裹在单引号或双引号之中就声明了一个字符串：

```
{% assign my_string = "Hello World!" %}
```

### Number（数字）

数字类型包括浮点数和整数：

```
{% assign my_int = 25 %}
{% assign my_float = 39.756 %}
```

### Boolean（布尔）

Booleans 类型只能是 `true` 或 `false`。布尔值千万不能加引号，否则就成为字符串了。

```
{% assign foo = true %}
{% assign bar = false %}
```

### Nil（空）

Nil 是一个特殊的空值，当 Liquid 代码没有可输出的结果时将返回 Nil。他并**不是**由 “nil” 这个三个字符组成的字符串。

在 `if` 条件判断和其他 Liquid 标记（tag）判断语句中，Nil [被当做 false](https://liquid.bootcss.com/basics/truthy-and-falsy) 。

下例中，如果 user 不存在（也就是 `user` 返回 `nil`），Liquid 不输出问候语：

```
{% if user %}
  Hello {{ user.name }}!
{% endif %}
```

如果 Liquid 标记（tag）或输出返回的是 `nil`，页面上将不会有任何内容。

输入

```
The current user is {{ user.name }}
```

输出

```
The current user is
```

### Array（数组）

数组能够存储一组任意类型的变量。

#### 访问数组中的项

通过 [迭代标记（iteration tag）](https://liquid.bootcss.com/tags/iteration) 可以访问数组中的所有项。

输入

```
<!-- if site.users = "Tobi", "Laura", "Tetsuro", "Adam" -->
{% for user in site.users %}
  {{ user }}
{% endfor %}
```

输出

```
Tobi Laura Tetsuro Adam
```

#### 访问数组中的特定项

利用方括号 `[` `]` 能够访问数组中的特定项。数组的索引从 0 开始。

输入

```
<!-- if site.users = "Tobi", "Laura", "Tetsuro", "Adam" -->
{{ site.users[0] }}
{{ site.users[1] }}
{{ site.users[3] }}
```

输出

```
Tobi
Laura
Adam
```

#### 初始化数组

你无法只通过 Liquid 语法初始化一个数组。

然而，你可以利用 [split](https://liquid.bootcss.com/filters/split) 过滤器将一个字符串分割为一个子字符串数组。

## Liquid 的各种分支

Liquid 是一门灵活、安全的模版语言，被用于许多不同环境中。Liquid 被创建之初是用在 [Shopify](https://www.shopify.com/) 商店系统中的，后来也被广泛用于 [Jekyll](https://jekyllrb.com/) 网站中。随着时间的推移，Shopify 和 Jekyll 分别为 Liquid 添加了针对各自用途的对象（object）、标记（tag）和过滤器（filter）。目前最流行的 Liquid 版本包括 **Liquid**、**Shopify Liquid** 和 **Jekyll Liquid**。

本站点托管的是最新版本的 **Liquid** 的文档，包括了 beta 和 release candidate 版本中包含的特性，也就是说，是独立于 Shopify 和 Jekyll 之外的 Liquid。如果你是从 Liquid 仓库下载的代码或者安装的的是 [gem](https://rubygems.org/gems/liquid) 包，你所选择的 Liquid 版本对应你能够访问的对象（object）、标记（tag）和过滤器。

### Shopify

Shopify 一直采用的都是最新版本的 Liquid，并且 Shopify 会针对 merchants’ store 为 Liquid 添加大量的对象（object）、标记（tag）和过滤器。这些新增的内容包括代表商店（store）、产品（product）和顾客信息的对象，以及用于展示商店数据和操作产品照片的过滤器。

Shopify 版本的 Liquid 所对应的文档在 [Shopify Help Center](https://help.shopify.com/themes/liquid)。如果你希望尝试 Shopify 版本的 Liquid，你可以[试用 Shopify](https://www.shopify.com/signup) 或者使用类似 [DropPen](http://droppen.org/) 的工具。

### Jekyll

[Jekyll](https://jekyllrb.com/) 是一个静态网站生成器，一个用于将模版和内容合并到一起从而创建网站的命令行工具。ekyll 将 Liquid 作为自身的模版语言，并且添加了许多对象（object）、标记（tag）和过滤器（filter）。这些新增内容包括代表内容页面的对象、用于在页面中引入内容片段的标记（tag），以及用于操作字符串和 URL 的过滤器。

Jekyll 还是 [GitHub Pages](https://pages.github.com/) 的底层引擎。GitHub Pages 是一项网站托管服务，允许你将 Jekyll 网站推送到 GitHub 仓库，最终得到一个发布到公网的站点。本网站就是由 GitHub Pages 托管的。

Jekyll 可能使用的不是最新版本的 Liquid。也就意味着本文档所列出的标记（tag）和过滤器不能在 Jekyll 中使用。通常 Jekyll 项目使用的是稳定版的 Liquid，而不使用 beta 或 release candidate 版本。通过 [Jekyll 的 gem 信息也](https://rubygems.org/gems/jekyll) 可查看 Jekyll 所依赖的所有 gem 包，从而可以了解 Jekyll 所使用的 Liquid 版本。

Jekyll 版本的 Liquid 的文档在 [Templates section of Jekyll’s documentation](http://jekyllrb.com/docs/templates/)。如果你希望尝试 Jekyll 版本的 Liquid，你可以克隆 Jekyll 项目或者安装 Jekyll 的 gem 包，然后在静态网站中测试 Liquid。

## 控制输出的空白符

在 Liquid 模版中，你可以将连字符放在标记（tag）中，例如 `{{-`、`-}}`、`{%-` 和 `-%}`，用于将标记（tag）渲染之后的输出内容的左侧或右侧的空拍符剔除。

通常，即使不输出文本，模版中的任何 Liquid 表达式仍然会在渲染之后输出的 HTML 中包含一个空行：

输入

```
{% assign my_variable = "tomato" %}
{{ my_variable }}
```

请注意渲染之后输出的 “tomato” 字符前面包含了一个空行：

输出

```
tomato
```

通过为 `assign` 标记（tag）添加连字符，可以将渲染之后所输出的空拍符删除：

输入

```
{%- assign my_variable = "tomato" -%}
{{ my_variable }}
```

输出

```
tomato
```

如果你不希望任何标记（tag）被渲染之后所输出的内容有任何空白符，只需在所有标记（tag）两侧全部添加连字符即可，例如 (`{%-` 和 `-%}`)：

输入

```
{% assign username = "John G. Chalmers-Smith" %}
{% if username and username.size > 10 %}
  Wow, {{ username }}, you have a long name!
{% else %}
  Hello there!
{% endif %}
```

不做空白符控制的输出

```
  Wow, John G. Chalmers-Smith, you have a long name!
```

输入

```
{%- assign username = "John G. Chalmers-Smith" -%}
{%- if username and username.size > 10 -%}
  Wow, {{ username }}, you have a long name!
{%- else -%}
  Hello there!
{%- endif -%}
```

带有空白符控制的输出

```
Wow, John G. Chalmers-Smith, you have a long name!
```

# 标记（tag）

## 注释

`comment` 标记让你能够在 Liquid 模板中书写的内容不被输出。任何书写在 `comment` 起始与结束标记之间的内容都不会被输出，如果是 Liquid 代码则不会被执行。

输入

```
Anything you put between {% comment %} and {% endcomment %} tags
is turned into a comment.
```

输出

```
Anything you put between  tags
is turned into a comment.
```

## 控制流

控制流标记（control flow tag）能够根据编程逻辑改变 Liquid 输出的信息。

### if

只有当某个条件为 `true` 时才执行一段代码。

输入

```
{% if product.title == 'Awesome Shoes' %}
  These shoes are awesome!
{% endif %}
```

输出

```
These shoes are awesome!
```

### unless

与 `if` 相对 – 只有当某个条件**不**成立时才执行一段代码。

输入

```
{% unless product.title == 'Awesome Shoes' %}
  These shoes are not awesome.
{% endunless %}
```

输出

```
These shoes are not awesome.
```

和如下实例的执行结果一致：

```
{% if product.title != 'Awesome Shoes' %}
  These shoes are not awesome.
{% endif %}
```

### elsif / else

为 `if` 或 `unless` 添加更多状态判断。

输入

```
<!-- If customer.name = 'anonymous' -->
{% if customer.name == 'kevin' %}
  Hey Kevin!
{% elsif customer.name == 'anonymous' %}
  Hey Anonymous!
{% else %}
  Hi Stranger!
{% endif %}
```

输出

```
Hey Anonymous!
```

### case/when

创建一个开关表达式，用于将一个变量和多个不同值进行比较。`case` 用于初始化一个开关表达式，`when` 用于比较他们的值。

输入

```
{% assign handle = 'cake' %}
{% case handle %}
  {% when 'cake' %}
     This is a cake
  {% when 'cookie' %}
     This is a cookie
  {% else %}
     This is not a cake nor a cookie
{% endcase %}
```

输出

```
This is a cake
```

## 迭代／循环

迭代（或循环）标记（iteration tag）用于重复运行一段代码。

### for

重复运行一段代码。`for` 循环中所能够使用的属性请参考 [forloop (object)](https://docs.shopify.com/themes/liquid/objects/for-loops)。

输入

```
  {% for product in collection.products %}
    {{ product.title }}
  {% endfor %}
```

输出

```
hat shirt pants
```

#### break

循环过程中若干遇到 `break` 标记（tag）即停止循环。

输入

```
{% for i in (1..5) %}
  {% if i == 4 %}
    {% break %}
  {% else %}
    {{ i }}
  {% endif %}
{% endfor %}
```

输出

```
1 2 3
```

#### continue

循环过程中若遇到 `continue` 标记（tag）则跳出当前循环。

输入

```
{% for i in (1..5) %}
  {% if i == 4 %}
    {% continue %}
  {% else %}
    {{ i }}
  {% endif %}
{% endfor %}
```

输出

```
1 2 3   5
```

### for (parameters)

#### limit

限定循环执行的次数。

输入

```
<!-- if array = [1,2,3,4,5,6] -->
{% for item in array limit:2 %}
  {{ item }}
{% endfor %}
```

输出

```
1 2
```

#### offset

从指定索引号开始执行循环。

输入

```
<!-- if array = [1,2,3,4,5,6] -->
{% for item in array offset:2 %}
  {{ item }}
{% endfor %}
```

输出

```
3 4 5 6
```

#### range

定义循环执行的范围。可利用数字或变量来定义此执行范围。

输入

```
{% for i in (3..5) %}
  {{ i }}
{% endfor %}

{% assign num = 4 %}
{% for i in (1..num) %}
  {{ i }}
{% endfor %}
```

输出

```
3 4 5
1 2 3 4
```

#### reversed

反转循环的执行顺序。注意和 `reverse` 过滤器（filter）的拼写是不同的。

输入

```
<!-- if array = [1,2,3,4,5,6] -->
{% for item in array reversed %}
  {{ item }}
{% endfor %}
```

输出

```
6 5 4 3 2 1
```

### cycle

循环一组字符串并按照它们传入的顺序将其输出。每次调用 `cycle` 时，传入的参数中的下一个字符串将被输出。

`cycle` 必须用在 [for](https://liquid.bootcss.com/tags/iteration/#for) 循环中。

输入

```
{% cycle 'one', 'two', 'three' %}
{% cycle 'one', 'two', 'three' %}
{% cycle 'one', 'two', 'three' %}
{% cycle 'one', 'two', 'three' %}
```

输出

```
one
two
three
one
```

`cycle` 的使用场景包括：

- 对表格中的奇数／偶数行输出相应的类（class）
- 在一行中的最后一列输出一个唯一的类（class）

### cycle (parameters)

`cycle` 能够接受一个叫做 `cycle group` 的参数，以便满足你在模版中需要使用多个 `cycle` 代码块的情况。如果没有为 cycle group 命名，那么将会假定带有相同参数的 cycle 调用属于同一个组（group）。

### tablerow

生成一个 HTML 表格。必须用 `` 和 `` 这两个 HTML 标签将其包裹起来。

输入

```
<table>
{% tablerow product in collection.products %}
  {{ product.title }}
{% endtablerow %}
</table>
```

输出

```
<table>
  <tr class="row1">
    <td class="col1">
      Cool Shirt
    </td>
    <td class="col2">
      Alien Poster
    </td>
    <td class="col3">
      Batman Poster
    </td>
    <td class="col4">
      Bullseye Shirt
    </td>
    <td class="col5">
      Another Classic Vinyl
    </td>
    <td class="col6">
      Awesome Jeans
    </td>
  </tr>
</table>
```

### tablerow (parameters)

#### cols

定义表格应当有多少列。

输入

```
{% tablerow product in collection.products cols:2 %}
  {{ product.title }}
{% endtablerow %}
```

输出

```
<table>
  <tr class="row1">
    <td class="col1">
      Cool Shirt
    </td>
    <td class="col2">
      Alien Poster
    </td>
  </tr>
  <tr class="row2">
    <td class="col1">
      Batman Poster
    </td>
    <td class="col2">
      Bullseye Shirt
    </td>
  </tr>
  <tr class="row3">
    <td class="col1">
      Another Classic Vinyl
    </td>
    <td class="col2">
      Awesome Jeans
    </td>
  </tr>
</table>
```

##### limit

在执行到指定的脚标（index）之后退出 tablerow 。

```
{% tablerow product in collection.products cols:2 limit:3 %}
  {{ product.title }}
{% endtablerow %}
```

#### offset

在指定的脚标（index）之后开始执行 tablerow 。

```
{% tablerow product in collection.products cols:2 offset:3 %}
  {{ product.title }}
{% endtablerow %}
```

#### range

定义循环执行的范围。可利用数字和变量来定义执行范围。

```
<!--variable number example-->

{% assign num = 4 %}
<table>
{% tablerow i in (1..num) %}
  {{ i }}
{% endtablerow %}
</table>

<!--literal number example-->

<table>
{% tablerow i in (3..5) %}
  {{ i }}
{% endtablerow %}
</table>
```

## 原始内容

`raw` 标记临时禁止处理其所包围的代码。如果输出的内容与 Liquid 模板语言有冲突时（例如 Mustache、Handlebars 模板语言）可以避免冲突。

输入

```
{% raw %}
  In Handlebars, {{ this }} will be HTML-escaped, but
  {{{ that }}} will not.
{% endraw %}
```

输出

```
In Handlebars, {{ this }} will be HTML-escaped, but {{{ that }}} will not.
```

## 变量

变量标记（variable tag）用于创建新的 Liquid 变量。

### assign

创建一个新变量。

输入

```
{% assign my_variable = false %}
{% if my_variable != true %}
  This statement is valid.
{% endif %}
```

输出

```
  This statement is valid.
```

将变量用 `"` 包裹之后则将其当做字符串对待。

输入

```
{% assign foo = "bar" %}
{{ foo }}
```

输出

```
bar
```

### capture

将 `capture` 开始与结束标记之间的字符串捕获之后赋值给一个变量。通过 `{% capture %}` 创建的变量都是字符串。

输入

```
{% capture my_variable %}I am being captured.{% endcapture %}
{{ my_variable }}
```

输出

```
I am being captured.
```

使用 `capture` 时，你还可以利用 `assign` 创建的其他变量创造一个复杂的字符串。

输入

```
{% assign favorite_food = 'pizza' %}
{% assign age = 35 %}

{% capture about_me %}
I am {{ age }} and my favorite food is {{ favorite_food }}.
{% endcapture %}

{{ about_me }}
```

输出

```
I am 35 and my favourite food is pizza.
```

### increment

创建一个全新的数值变量，并且在后续每次调用时将此变量的值加 1。初始值是 0。

输入

```
{% increment my_counter %}
{% increment my_counter %}
{% increment my_counter %}
```

输出

```
0
1
2
```

通过 `increment` 标记（tag）创建的变量与通过 `assign` 或 `capture` 创建的变量是相互独立的。

在下面的实例中，名为 “var” 的变量是通过 `assign` 创建的。然后将 `increment` 标记（tag）在相同的变量名上应用了几次。注意，`increment` 标记（tag）不会对 `assign` 创建的变量 “var” 及其值产生任何影响。

输入

```
{% assign var = 10 %}
{% increment var %}
{% increment var %}
{% increment var %}
{{ var }}
```

输出

```liquid
0
1
2
10
```

### decrement

创建一个全新的数值变量，并且在后续每次调用时将此变量的值减 1。初始值是 -1。

输入

```
{% decrement variable %}
{% decrement variable %}
{% decrement variable %}
```

输出

```
-1
-2
-3
```

和 [increment](https://liquid.bootcss.com/tags/variable/#increment) 类似，在 `decrement` 之中创建的变量与通过 `assign` 或 `capture` 创建的变量是互相独立的。

#  过滤器（filter）

## abs

返回一个数字的绝对值。

输入

```
{{ -17 | abs }}
```

输出

```
17
```

输入

```
{{ 4 | abs }}
```

输出

```
4
```

如果组成字符串的各个字符全是数字，`abs` 也能够对此字符串求绝对值。

输入

```
{{ "-19.86" | abs }}
```

输出

```
19.86
```

## append

将两个字符串拼接起来并返回拼接之后的值。

输入

```
{{ "/my/fancy/url" | append: ".html" }}
```

输出

```
/my/fancy/url.html
```

`append` 同样能够作用于变量：

输入

```
{% assign filename = "/index.html" %}
{{ "website.com" | append: filename }}
```

输出

```
website.com/index.html
```

## at_least

将数字限制在最小值。

输入

```
{{ 4 | at_least: 5 }}
```

输出

```
5
```

输入

```
{{ 4 | at_least: 3 }}
```

输出

```
4
```

## at_most

将数字限制在最大值。

输入

```
{{ 4 | at_most: 5 }}
```

输出

```
4
```

输入

```
{{ 4 | at_most: 3 }}
```

输出

```
3
```

## capitalize

将字符串首字母转为大写。

输入

```
{{ "title" | capitalize }}
```

输出

```
Title
```

`capitalize` 只把字符串的首字母转为大写，其他字符不受影响：

输入

```
{{ "my great title" | capitalize }}
```

输出

```
My great title
```

## ceil

将一个浮点数向上取整并返回一个最接近的整数。在 ceil 过滤器执行之前 Liquid 会先尝试将输入转换为数字格式。

输入

```
{{ 1.2 | ceil }}
```

输出

```
2
```

输入

```
{{ 2.0 | ceil }}
```

输出

```
2
```

输入

```
{{ 183.357 | ceil }}
```

输出

```
184
```

以下实例所用输入是字符串：

输入

```
{{ "3.5" | ceil }}
```

输出

```
4
```

## compact

删除数组中的所有 `nil` 值。

例如，假定整个网站所有内容页面作为一个数组保存在 `site.pages` 变量中，其中某些页面被设置了 `category` 属性用于指定该页面的内容分类。如果我们利用 `map` 过滤器将所有页面的 `category` 属性保存到一个数组中，就会出现如果某个页面没有 `category` 属性，其在数组中的值就会是 `nil`。

输入

```
{% assign site_categories = site.pages | map: 'category' %}

{% for category in site_categories %}
  {{ category }}
{% endfor %}
```

输出

```
  business
  celebrities

  lifestyle
  sports

  technology
```

在创建 `site_categories` 数组时，通过使用 `compact` 过滤器我们可以删除此数组中的所有 `nil` 值。

输入

```
{% assign site_categories = site.pages | map: 'category' | compact %}

{% for category in site_categories %}
  {{ category }}
{% endfor %}
```

输出

```
  business
  celebrities
  lifestyle
  sports
  technology
```

## concat

串联（连接）多个数组。生成的数组包含输入数组中的所有项。

输入

```
{% assign fruits = "apples, oranges, peaches" | split: ", " %}
{% assign vegetables = "carrots, turnips, potatoes" | split: ", " %}

{% assign everything = fruits | concat: vegetables %}

{% for item in everything %}
- {{ item }}
{% endfor %}
```

输出

```
- apples
- oranges
- peaches
- carrots
- turnips
- potatoes
```

您可以将筛选器串`concat`以联接两个以上数组在一起：

输入

```
{% assign furniture = "chairs, tables, shelves" | split: ", " %}

{% assign everything = fruits | concat: vegetables | concat: furniture %}

{% for item in everything %}
- {{ item }}
{% endfor %}
```

输出

```
- apples
- oranges
- peaches
- carrots
- turnips
- potatoes
- chairs
- tables
- shelves
```

## date

将时间戳（timestamp）转换为另一种日期格式。格式化语法与 [`strftime`](http://strftime.net/) 一致。输入格式与 Ruby 中的 [`Time.parse`](https://ruby-doc.org/stdlib/libdoc/time/rdoc/Time.html#method-c-parse) 一致。

输入

```
{{ article.published_at | date: "%a, %b %d, %y" }}
```

输出

```
Fri, Jul 17, 15
```

输入

```
{{ article.published_at | date: "%Y" }}
```

输出

```
2015
```

`date` 能够作用于包含良好格式化的日期字符串：

输入

```
{{ "March 14, 2016" | date: "%b %d, %y" }}
```

输出

```
Mar 14, 16
```

将 `"now"` (或 `"today"`) 单词传入 `date` 过滤器可以获取当前时间：

输入

```
This page was last updated at {{ "now" | date: "%Y-%m-%d %H:%M" }}.
```

输出

```
This page was last updated at 2020-03-17 17:11.
```

注意，上述实例输出的日期是最后一次生成当前页面的时间，并不是页面呈现给用户的时间。

## default

指定一个默认值，以防预期的值不存在。如果左侧的值为 `nil`、`false` 或空，`default` 将输出此默认值。

如下实例中，`product_price` 并未被定义，因此将输出默认值。

输入

```
{{ product_price | default: 2.99 }}
```

输出

```
2.99
```

如下实例中，`product_price` 已被定义，不再输出默认值。

输入

```
{% assign product_price = 4.99 %}
{{ product_price | default: 2.99 }}
```

输出

```
4.99
```

如下实例中，`product_price` 的值为空，因此将输出默认值。

输入

```
{% assign product_price = "" %}
{{ product_price | default: 2.99 }}
```

输出

```
2.99
```

## divided_by

将两个数相除。

如果除数（divisor）为整数，则将相除之后得到的结果向下取整得到最接近的整数（也就是对应 [floor](https://liquid.bootcss.com/filters/floor) 的功能）。

输入

```
{{ 16 | divided_by: 4 }}
```

输出

```
4
```

输入

```
{{ 5 | divided_by: 3 }}
```

输出

```
1
```

#### 控制舍入

`divided_by` 返回的结果于除数是同一数据类型的，也就是说，如果除数是整数，返回的结果也是整数；如果除数是浮点数（带有小数），返回的结果也是浮点数。

如下实例，除数为整数：

输入

```
{{ 20 | divided_by: 7 }}
```

输出

```
2
```

除数为浮点数：

输入

```
{{ 20 | divided_by: 7.0 }}
```

输出

```
2.857142857142857
```

#### 改变变量的类型

某些情况你需要将除数设置为一个变量，这种情况下你无法简单的给这个变量添加 `.0` 将其转变为浮点数。这时，你可以通过 `times` 过滤器将其转变为浮点数，并通过 `assign` 创建一个新变量来保存转换之后的浮点数。

下例中，除数是一个变量，保存的是一个整数，所以返回值也是一个整数：

输入

```
{% assign my_integer = 7 %}
{{ 20 | divided_by: my_integer }}
```

输出

```
2
```

下面，我们将这个变量[乘以](https://liquid.bootcss.com/filters/times) `1.0` 来得到一个浮点数，然后将此浮点数作为除数进行运算：

输入

```
{% assign my_integer = 7 %}
{% assign my_float = my_integer | times: 1.0 %}
{{ 20 | divided_by: my_float }}
```

输出

```
2.857142857142857
```

## downcase

用于将字符串中的各个字符转换为小写形式。对于已经是小写形式的字符串没有任何影响。

输入

```
{{ "Parker Moore" | downcase }}
```

输出

```
parker moore
```

输入

```
{{ "apple" | downcase }}
```

输出

```
apple
```

## escape

对字符串转义操作就是将字符串中的某些字符替换为转义序列（escape sequence），这样整个字符串就能够用于 URL 了。如果字符串不需要转义则不会对字符串做任何操作。

输入

```
{{ "Have you read 'James & the Giant Peach'?" | escape }}
```

输出

```
Have you read &#39;James &amp; the Giant Peach&#39;?
```

输入

```
{{ "Tetsuro Takara" | escape }}
```

输出

```
Tetsuro Takara
```

## escape_once

转义一个字符串并且不修改已经转义过的实体（entities)。对于无须转义的字符串不做任何修改。

输入

```
{{ "1 < 2 & 3" | escape_once }}
```

输出

```
1 &lt; 2 &amp; 3
```

输入

```
{{ "1 &lt; 2 &amp; 3" | escape_once }}
```

输出

```
1 &lt; 2 &amp; 3
```

## first

返回数组的第一项。

输入

```
{% assign my_array = "apples, oranges, peaches, plums" | split: ", " %}

{{ my_array.first }}
```

输出

```
apples
```

输入

```
{% assign my_array = "zebra, octopus, giraffe, tiger" | split: ", " %}

{{ my_array.first }}
```

输出

```
zebra
```

## floor

将一个浮点数通过舍弃小数部分得到最近的整数。在 floor 过滤器执行之前 Liquid 会先尝试将输入转换为数字格式。

输入

```
{{ 1.2 | floor }}
```

输出

```
1
```

输入

```
{{ 2.0 | floor }}
```

输出

```
2
```

输入

```
{{ 183.357 | floor }}
```

输出

```
183
```

以下实例所用输入是字符串：

输入

```
{{ "3.5" | floor }}
```

输出

```
3
```

## join

将数组中的各个字符串合并为一个字符串，并将 `split` 参数作为字符串之间的分隔符。

输入

```
{% assign beatles = "John, Paul, George, Ringo" | split: ", " %}

{{ beatles | join: " and " }}
```

输出

```
John and Paul and George and Ringo
```

## last

返回数组中的最后一项。

输入

```
{% assign my_array = "apples, oranges, peaches, plums" | split: ", " %}

{{ my_array.last }}
```

输出

```
plums
```

输入

```
{% assign my_array = "zebra, octopus, giraffe, tiger" | split: ", " %}

{{ my_array.last }}
```

输出

```
tiger
```

## lstrip

删除字符串左侧的所有空白符（制表符、空格和换行符）。字符串中间的所有空白符不受影响。

输入

```
{{ "          So much room for activities!          " | lstrip }}
```

输出

```
So much room for activities!        
```

## map

从对象（object）中提取指定名称的属性的值，并用这些值构建一个数组。

以下实例中，假定 `site.pages` 包含了整个网站的元数据信息。利用 `assign` 和 `map` 过滤器创建一个变量，此变量只包含 `site.pages` 对象中 `category` 属性对应的所有值。

输入

```
{% assign all_categories = site.pages | map: "category" %}

{% for item in all_categories %}
{{ item }}
{% endfor %}
```

输出

```
business
celebrities
lifestyle
sports
technology
```

## minus

从一个数中减去另一个数。

输入

```
{{ 4 | minus: 2 }}
```

输出

```
2
```

输入

```
{{ 16 | minus: 4 }}
```

输出

```
12
```

输入

```
{{ 183.357 | minus: 12 }}
```

输出

```
171.357
```

## modulo

返回除法运算的余数。

输入

```
{{ 3 | modulo: 2 }}
```

输出

```
1
```

输入

```
{{ 24 | modulo: 7 }}
```

输出

```
3
```

输入

```
{{ 183.357 | modulo: 12 }}
```

输出

```
3.357
```

## newline_to_br

将所有换行符(`\n`) 替换为 HTML 的 (` `) 标签。

输入

```
{% capture string_with_newlines %}
Hello
there
{% endcapture %}

{{ string_with_newlines | newline_to_br }}
```

输出

```
<br />
Hello<br />
there<br />
```

## plus

两个数相加。

输入

```
{{ 4 | plus: 2 }}
```

输出

```
6
```

输入

```
{{ 16 | plus: 4 }}
```

输出

```
20
```

输入

```
{{ 183.357 | plus: 12 }}
```

输出

```
195.357
```

## prepend

在一个字符串前面附加另一个字符串。

输入

```
{{ "apples, oranges, and bananas" | prepend: "Some fruit: " }}
```

输出

```
Some fruit: apples, oranges, and bananas
```

`prepend` 也能作用于变量：

输入

```
{% assign url = "example.com" %}

{{ "/index.html" | prepend: url }}
```

输出

```
example.com/index.html
```

## remove

从一个字符串中删除所有出现的另一个子字符串。

输入

```
{{ "I strained to see the train through the rain" | remove: "rain" }}
```

输出

```
I sted to see the t through the 
```

## remove_first

从一个字符串中仅仅删除第一次出现的另一个子字符串。

输入

```
{{ "I strained to see the train through the rain" | remove_first: "rain" }}
```

输出

```
I sted to see the train through the rain
```

## replace

将参数中给出的第一个参数全部替换为第二个参数。

输入

```
{{ "Take my protein pills and put my helmet on" | replace: "my", "your" }}
```

输出

```
Take your protein pills and put your helmet on
```

## replace_first

将字符串中出现的第一个参数替换为第二个参数。

输入

```
{% assign my_string = "Take my protein pills and put my helmet on" %}
{{ my_string | replace_first: "my", "your" }}
```

输出

```
Take your protein pills and put my helmet on
```

## reverse

将数组中的所有项的顺序反转。`reverse` 不能操作字符串。

输入

```
{% assign my_array = "apples, oranges, peaches, plums" | split: ", " %}

{{ my_array | reverse | join: ", " }}
```

输出

```
plums, peaches, oranges, apples
```

`reverse` 不能直接应用到字符串上，但是你可以先将字符串分割成字符数组，然后再将数组反转，最后将反转之后的数组合并。

输入

```
{{ "Ground control to Major Tom." | split: "" | reverse | join: "" }}
```

输出

```
.moT rojaM ot lortnoc dnuorG
```

## round

将浮点数舍入到最近的整数，或者，如果传入的参数是一个数值的话，将浮点数舍入到参数指定的小数位。

输入

```
{{ 1.2 | round }}
```

输出

```
1
```

输入

```
{{ 2.7 | round }}
```

输出

```
3
```

输入

```
{{ 183.357 | round: 2 }}
```

输出

```
183.36
```

## rstrip

将字符串右侧的所有空白字符（制表符 - tab、空格符 - space 和 回车符 - newline）删除。

输入

```
{{ "          So much room for activities!          " | rstrip }}
```

输出

```
          So much room for activities!
```

## size

返回字符串中所包含的字符数或者数组中所包含的条目数量。`size` 还支持“点标记”（例如 `{{ my_string.size }}`）。这种用法便于你在标签（tag）中使用 `size` 过滤器，例如条件判断标签（tag）。

输入

```
{{ "Ground control to Major Tom." | size }}
```

输出

```
28
```

输入

```
{% assign my_array = "apples, oranges, peaches, plums" | split: ", " %}

{{ my_array | size }}
```

输出

```
4
```

使用“点标记”：

```
{% if site.pages.size > 10 %}
  This is a big website!
{% endif %}
```

## slice

只传入一个参数时将返回此参数作为下标所对应的单个字符。第二个参数是可选的，用于指定返回的子字符串的长度。

String indices are numbered starting from 0.

输入

```
{{ "Liquid" | slice: 0 }}
```

输出

```
L
```

输入

```
{{ "Liquid" | slice: 2 }}
```

输出

```
q
```

输入

```
{{ "Liquid" | slice: 2, 5 }}
```

输出

```
quid
```

If the first parameter is a negative number, the indices are counted from the end of the string:

输入

```
{{ "Liquid" | slice: -3, 2 }}
```

输出

```
ui
```

## sort

对数组中的所有进行排序。排序后的数组是按照区分大小写的顺序排列的。

输入

```
{% assign my_array = "zebra, octopus, giraffe, Sally Snake" | split: ", " %}

{{ my_array | sort | join: ", " }}
```

输出

```
Sally Snake, giraffe, octopus, zebra
```

## sort_natural

对数组进行排序，并且大小写无关。

输入

```
{% assign my_array = "zebra, octopus, giraffe, Sally Snake" | split: ", " %}

{{ my_array | sort_natural | join: ", " }}
```

输出

```
giraffe, octopus, Sally Snake, zebra
```

## split

根据参数传入的分隔符将字符串分解为数组。`split` 通常被用于将以逗号为分隔符的字符串转换为数组。

输入

```
{% assign beatles = "John, Paul, George, Ringo" | split: ", " %}

{% for member in beatles %}
  {{ member }}
{% endfor %}
```

输出

```
  John

  Paul

  George

  Ringo
```

## strip

删除字符串左右两侧的所有空白符号（包括制表符、空格、换行符）。对于字符串中间的空白符不做任何处理。

Input

```
{{ "          So much room for activities!          " | strip }}
```

Output

```
So much room for activities!
```

## strip_html

从字符串中删除所有 HTML 标签。

输入

```
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```

输出

```
Have you read Ulysses?
```

## strip_newlines

从字符串中删除所有换行字符（newline character）。

输入

```
{% capture string_with_newlines %}
Hello
there
{% endcapture %}

{{ string_with_newlines | strip_newlines }}
```

输出

```
Hellothere
```

## times

将一个数乘以另一个数。

输入

```
{{ 3 | times: 2 }}
```

输出

```
6
```

输入

```
{{ 24 | times: 7 }}
```

输出

```
168
```

输入

```
{{ 183.357 | times: 12 }}
```

输出

```
2200.284
```

## truncate

`truncate` 将字符串截短为指定的字符个数。如果指定的字符数量小于字符串的长度，则会在字符串末尾添加一个省略号(…) 并将此省略号计入字符个数中。

输入

```
{{ "Ground control to Major Tom." | truncate: 20 }}
```

输出

```
Ground control to...
```

#### 自定义省略号

`truncate` 还支持第二个可选参数，用于指定一个字符序列，此字符序列将被添加到截短字符串的后面。默认是省略号(…)，但是你可以按照你的需要传递一个新的。

第二个参数的长度将被计入第一个参数的字符个数中。例如，如果你希望将字符串截短为 10 个字符，并且使用由 3 个字符组成的省略号，这时，你需要将 `truncate` 的第一个参数设置为 **13**，是因为需要计入省略号的 3 个字符。

输入

```
{{ "Ground control to Major Tom." | truncate: 25, ", and so on" }}
```

输出

```
Ground control, and so on
```

#### 无省略号

你可以将字符串按照第一个参数截短为指定长度，并且可以通过传递一个空字符作为第二个参数，从而让截短之后的字符串不显示省略号。

输入

```
{{ "Ground control to Major Tom." | truncate: 20, "" }}
```

输出

```
Ground control to Ma
```

## truncatewords

将字符串截短为指定的单词个数。如果指定的单词数量小于字符串中包含的单词个数，则会在字符串末尾添加一个省略号(…)。

输入

```
{{ "Ground control to Major Tom." | truncatewords: 3 }}
```

输出

```
Ground control to...
```

#### 自定义省略号

`truncatewords` 还支持第二个可选参数，用于指定一个字符序列，此字符序列将被添加到截短字符串的后面。默认是省略号(…)，但是你可以按照你的需要传递一个新的。

输入

```
{{ "Ground control to Major Tom." | truncatewords: 3, "--" }}
```

输出

```
Ground control to--
```

#### 无省略号

如果你不希望在末尾添加省略号，可以将 `truncatewords` 的第二个参数设置为空字符串：

输入

```
{{ "Ground control to Major Tom." | truncatewords: 3, "" }}
```

输出

```
Ground control to
```

## uniq

删除数组中的所有冗余项。

输入

```
{% assign my_array = "ants, bugs, bees, bugs, ants" | split: ", " %}

{{ my_array | uniq | join: ", " }}
```

输出

```
ants, bugs, bees
```

## upcase

将字符串中的每个字符都转换为大写形式。对于已经全是大写的字符串不做任何操作。

输入

```
{{ "Parker Moore" | upcase }}
```

输出

```
PARKER MOORE
```

输入

```
{{ "APPLE" | upcase }}
```

输出

```
APPLE
```

## url_decode

对于作为 URL 进行编码或通过 [`url_encode`](https://liquid.bootcss.com/filters/url_encode) 编码的字符串进行解码。

输入

```
{{ "%27Stop%21%27+said+Fred" | url_decode }}
```

输出

```
'Stop!' said Fred
```

## url_encode

将字符串中非 URL 安全的字符转换为百分号编码（percent-encoded）的字符。

输入

```
{{ "john@liquid.com" | url_encode }}
```

输出

```
john%40liquid.com
```

输入

```
{{ "Tetsuro Takara" | url_encode }}
```

输出

```
Tetsuro+Takara
```