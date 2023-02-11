---
title: ""
description: ""
author: "石昌文"
tags: [""]
categories: ""
keywords:  [""]
draft: true
layout: 
createdata: 2023-02-11 19:33:31
updatedata: 2023-02-11 19:35:42
---

## 总结 html 标签, 以便随时查看

> 有智者立长志，无志者长立志。

## 基础

### HTML 定义文档类型

```html
<!DOCTYPE html>
<html>

<head>
<title>文档的标题</title>
</head>

<body>
文档的内容......
</body>

</html>
```

### HTML 标题

```html
<h1>This is a h1</h1>
<h2>This is a h2</h2>
<h3>This is a h3</h3>
<h4>This is a h4</h4>
<h5>This is a h5</h5>
<h6>This is a h6</h6>
```

### HTML 段落

```html
<p>This is a paragraph.</p>
```

### HTML 换行

```html
<br />
```

### HTML 水平线

```html
<hr />
```

### HTML 注释

```html
<!--这是一段注释。注释不会在浏览器中显示。-->
```

## 格式

### HTML 缩写标签

```html
<abbr title="People's Republic of China">PRC</abbr>
```

### HTML 文档作者或拥有者的联系信息。

```html
<address>
Written by <a href="https://charvin.cn/">大傻瓜</a>.<br> 
Visit me In China<br>
And web:charvin.cn
</address>
```

### HTML 粗体文本

```html
<b>这是粗体文本</b>
```

### HTML 斜体文本

```html
<i> 斜体文本 </i>
```

### HTML 大号文本

```html
<big> 我是最大的 </big>
```

### HTML 小号文本

```html
<small>小号文本</small>
```

### HTML 打字机文本

```html
<tt> 打字机文本 </tt>
```

### HTML 5 定义文本的文本方向，使其脱离其周围文本的方向设置

```html
<li>这个我真的 <bdi>没</bdi>咋看懂</li>
```

### HTML 文字方向

```html
<bdo dir="rtl">
我到底是正的反的
</bdo>
```

### HTML 长的引用

```html
<blockquote>长的引用,</blockquote>
```

> 长的引用, 自动前后+换行, 左右+外边距

### HTML 短的引用

```html
<q>短的引用,自动+"",不自动换行</q>
```

### HTML 删除线

```html
<del>删除线</del>
```

### HTML 被插入文本

```html
<ins>插入线</ins>
```

### HTML 5 有记号的文本

```html
<mark> 有记号的文本</mark>
```

### HTML 5 规定范围内的度量

```html
<meter value="3" min="0" max="10"></meter>
<meter value="0.6">60%</meter>
```

### HTML 预格式文本

```html
<pre>
保留空格       和
换行符,使用ASCII 实体 符号
</pre>
保留空格       和
换行符,使用ASCII 实体 符号
```

### HTML 5 任何类型的任务的进度条

```html
<progress value="22" max="100"></progress>
```

### HTML 上标文本

```html
<sup>上标</sup>
```

### HTML 下标文本

```html
<sub>下标</sub>
```

### HTML 5 日期/时间(截至 2008 主流浏览器均不支持)

```html
<time datetime="2019-01-24">文档创建日</time>
```

### HTML 5 可能的换行符

```html
<p>要求改变窗口在<wbr>这里<wbr>换行</p>
```

### HTML 计算机代码文本

```html
<code>自动变为等宽字体</code>
自动变为等宽字体
```

### HTML 普通引用

```html
<cite>普通引用,自动倾斜,不自带换行<cite>
```

### HTML 强调

```html
<em>强调</em>
```

### HTML 语气更强的强调

```html
<strong>语气更强的强调</strong>
```

### HTML 定义一个定义项目

```html
<dfn>定义项目</dfn>
```

### HTML 样本文本

```html
<samp>样本文本</samp>
```

### HTML 键盘文本

```html
<kbd>键盘文本</kbd>
```

### HTML 变量

```html
<var>变量</var>
```

## 表单

### HTML 定义供用户输入的 HTML 表单

```html
<form action="/demo/demo_form.asp">
</form> 
<p>表单数据会被发送到名为 demo_form.asp 的页面。</p>
```

### HTML 输入控件

```html
user name:<br>
<input type="text" name="user name" value="user name">
password:<br>
<input type="text" name="password" value="password">
<input type="submit" value="Submit">
```

### HTML input 元素的标注

```html
<form>
<label for="标注id">标注</label>
<input type="radio" name="标注" id="标注id" />
</form>
```

### HTML 5 input 的下拉列表

```html
<input id="number" list="listid" />
<datalist id="listid">
  <option value="0">
  <option value="1">
</datalist>
```

### HTML 多行的文本输入控件

```html
<textarea rows="3" cols="20">
你可以在这里输入任何数量的文本
</textarea>
```

### HTML 按钮

```html
<button type="button">我是一个不限制内容的按钮</button>
```

### HTML 选择列表（下拉列表）

```html
<select>
</select>
```

### HTML 选择列表中的选项

```html
<select>
  <option value ="0">0</option>
  <option value ="1">1</option>
  <option value ="a">a</option>
  <option value ="b">b</option>
</select>
```

### HTML 选择列表中相关选项的组合

```html
<select>
  <optgroup label="	number">
    <option value ="0">0</option>
    <option value ="1">1</option>
  </optgroup>
  <optgroup label="alphabet">
    <option value ="a">a</option>
    <option value ="b">b</option>
  </optgroup>
</select>
```

### HTML 围绕表单中元素的边框

```html
<fieldset>
</fieldset>
```

### HTML fieldset 元素的标题

```html
<fieldset>
  <legend>边框标题</legend>
</fieldset>
```

### HTML 5 规定用于表单的密钥

```html
<form action="/example/html5/demo_form.asp" method="get">
用户名：<input type="text" name="usr_name" />
加密：<keygen name="security" />
<input type="submit" />
</form>
```

### HTML 5 输出的一些类型

```html
<form oninput="x.value=parseInt(a.value)">
0
<input type="range" id="a" value="50" min="1" max="100">
100
=
<output name="x" for="a"></output>
</form>
```

## 框架

### HTML 框架集

```html
<frameset cols="25%,50%,25%">
</frameset>
```

### HTML 架集的窗口或框架

```html
<frameset cols="50%,50%">
<frame src="https://charvin.cn/2019/01/23/Markdown%20For%20Typora/">
  <frame src="https://charvin.cn/2019/01/22/hello-world/">
</frameset>
```

### HTML 针对不支持框架的用户的替代内容

```html
<frameset cols = "25%, 25%,*">
  <noframes>
  <body>您的浏览器无法处理框架！</body>
  </noframes>
</frameset>
```

### HTML 内联框架

```html
<iframe src="https://charvin.cn/2019/01/23/Markdown%20For%20Typora/>
</iframe >
<iframe src="https://charvin.cn/2019/01/22/hello-world/>
</iframe >
```

## 图像

### HTML 图像

```html
<img src="https://charvin.cn/img/avatar.png" width="104" height="142" />
```

### HTML 图像映射

```html
<img src="https://charvin.cn/img/avatar.png" width="104" height="142" usemap="#clickarea"/>
<map name="clickarea" id="clickarea">
</map>
```

### HTML 定义图像映射内部的区域。

```html
<img src="https://charvin.cn/img/avatar.png"
border="0"
usemap="#clickarea"
alt="clickarea  g"/>
<map name="clickarea" id="clickarea">
  <area shape="circle" coords="82,38,16" href ="https://charvin.cn/" alt="charvin" />
</map>
```

### HTML 5 使用图形容器绘制图形

```html
<canvas id="myCanvas">your browser does not support the canvas tag </canvas>
<script type="text/javascript">
var myCanvas=document.getElementById('myCanvas');
var ctx=myCanvas.getContext('2d');
ctx.fillStyle='#FF0000';
ctx.fillRect(0,0,80,100);
```

### HTML 5 定义媒介内容（图像、图表、照片、代码等等）的分组，以及它们的标题

```html
<figure>
  <p>my img</p>
  <img src="https://charvin.cn/img/avatar.png" />
</figure>
```

### HTML 5 定义 figure 元素的标题

```html
<figure>
<figcaption>my img</figcaption>
  <img src="https://charvin.cn/img/avatar.png" />
</figure>
```

## 音频/视频

### HTML 5 声音内容

```html
<audio src="https://charvin.cn/music/maliang-For%20the%20rest%20of%20the%20life.mp3" controls="controls">
</audio>
```

### HTML 5 视频

```html
<video src="https://charvin.cn/videos/小哥哥为什么都不追小姐姐了.mp4" controls="controls">
</video>
```

### HTML 5 定义媒介源

```html
<audio controls>
<source src="https://charvin.cn/videos/小哥哥为什么都不追小姐姐了.mp4" type="audio/mp4">
<source src="https://charvin.cn/musics/maliang-For%20the%20rest%20of%20the%20life.mp3" type="audio/mpeg">
 Your browser does not support the audio element.
</audio>
```

### HTML 5 定义用在媒体播放器中的文本轨道(字幕)

```html
<video width="320" height="240" controls="controls">
  <source src="forrest_gump.mp4" type="video/mp4" />
  <track kind="subtitles" src="subs_chi.srt" srclang="zh" label="Chinese">
</video>
```

## 链接

### HTML 定义超链接

```html
<a href="https://charvin.cn/">This is my blog</a>
```

### HTML 定义文档与外部资源的关系

```html
<link rel="stylesheet" type="text/css" href="theme.css" />
```

### HTML 定义导航链接

```html
<nav>
<a href="https://charvin.cn/">Home</a>
<a href="https://charvin.cn/archives/">blog</a>
</nav>
```

## 列表

### HTML 定义列表的项目

```html
<li>项目</li>
```

### HTML 无序列表

```html
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```

### HTML 有序列表

```html
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```

### HTML 自定义列表中的项目

```html
<dt>项目</dt>
```

### HTML 自定义列表中项目的描述

```html
<dd>项目描述</dd>
```

### HTML 自定义列表

```html
<dl>
   <dt>计算机</dt>
   <dd>用来计算的仪器 ... ...</dd>
   <dt>显示器</dt>
   <dd>以视觉方式显示信息的装置 ... ...</dd>
</dl>
```

## 表格

### HTML 表格标题

```html
<caption>标题</caption>
```

### HTML 表格中的表头单元格

```html
<th>表头单元格</th>
```

### HTML 表格中的行

```html
<tr></tr>
```

### HTML 表格中的单元

```html
<td>单元</td>
```

### HTML 表格中的表头内容

```html
<thead></thead>
```

### HTML 表格中的主体内容

```html
<tbody></tbody>
```

### HTML 表格中的表注内容（脚注）

```html
<tfoot></tfoot>
```

### HTML 表格中一个或多个列的属性值

```html
<col />
```

### HTML 表格中供格式化的列组

```html
<colgroup></colgroup>
```

### HTML 定义表格

```html
<table border="1">
  <thead>
    <tr>
      <th>Month</th>
      <th>Savings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>January</td>
      <td>$100</td>
    </tr>
    <tr>
      <td>February</td>
      <td>$80</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Sum</td>
      <td>$180</td>
    </tr>
  </tfoot>
</table>
```

## 样式/分区

### HTML 定义文档的样式信息

```html

```

### HTML 定义文档中的分区

```html
<p>分区外没颜色.</p>
<div style="color:#00FF00">
<p>分区内有颜色(因为div自定义了专属style).</p>
</div>
```

### HTML 组合行内元素

```html
<p><span>span内的文本</span>和外面没什么不一样,除非自定义了span的style</p>
```

### HTML 5section 或 page 的页眉

```html
<header>
</header>
```

### HTML 5section 或 page 的页脚

```html
<footer>
</footer>
```

### HTML 5 定义 section(文档中的分段)

```html
<section></section>
```

### HTML 5 定义文章

```html
<article>
</article>
```

### HTML 5 定义页面内容之外的内容

```html
<aside></aside>
```

## 元信息

### HTML 定义关于 HTML 文档的元信息

```html
<meta name="???"
content="???" http-equiv="???" scheme="???">
```

### HTML 定义页面中所有链接的默认地址或默认目标

```html
<base target="_blank" href="https://charvin.cn/" />
```

## 编程

### HTML 插入 JavaScript

```html
<script type="text/javascript">
</script>
```

### HTML 定义在脚本未被执行时的替代内容（文本）

```html
<noscript>Sorry, your browser does not support JavaScript!</noscript>
```

### HTML 为外部应用程序（非 HTML）定义容器

```html
<embed src="helloworld.swf" />
```

### HTML 定义嵌入的对象

```html
<object classid="clsid:???" id="Slider1" 
width="100" height="50">
<param name="BorderStyle" value="1" />
</object>
```

### HTML 定义对象的参数

```html
<param name="BorderStyle" value="1" />
```
