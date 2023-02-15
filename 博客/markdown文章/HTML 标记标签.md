本文标题:HTML 标记标签

文章作者:大傻瓜

标签：

HTML
学习

发布时间:2019-01-23, 16:47:00

最后更新:2019-01-23, 16:47:00

## 总结html标签,以便随时查看

> 有智者立长志，无志者长立志。



## 基础

### HTML 定义文档类型

```
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

```
<h1>This is a h1</h1>
<h2>This is a h2</h2>
<h3>This is a h3</h3>
<h4>This is a h4</h4>
<h5>This is a h5</h5>
<h6>This is a h6</h6>
```



# This is a h1





## This is a h2





### This is a h3





#### This is a h4





##### This is a h5



###### This is a h6

### HTML 段落

```
<p>This is a paragraph.</p>
```

This is a paragraph.

### HTML 换行

```
<br />
```

换
行

### HTML 水平线

```
<hr />
```

------

### HTML 注释

```
<!--这是一段注释。注释不会在浏览器中显示。-->
```

## 格式

### HTML 缩写标签

```
<abbr title="People's Republic of China">PRC</abbr>
```

PRC

### HTML 文档作者或拥有者的联系信息。

```
<address>
Written by <a href="https://charvin.cn/">大傻瓜</a>.<br> 
Visit me In China<br>
And web:charvin.cn
</address>
```


Written by [大傻瓜](https://charvin.cn/).

Visit me In China

And web:charvin.cn

### HTML 粗体文本

```
<b>这是粗体文本</b>
```

**这是粗体文本**

### HTML 斜体文本

```
<i> 斜体文本 </i>
```

*斜体文本*

### HTML 大号文本

```
<big> 我是最大的 </big>
```

我是最大的

### HTML 小号文本

```
<small>小号文本</small>
```

小号文本

### HTML 打字机文本

```
<tt> 打字机文本 </tt>
打字机文本
```

### HTML 5定义文本的文本方向，使其脱离其周围文本的方向设置

```
<li>这个我真的 <bdi>没</bdi>咋看懂</li>
```

这个我真的 没咋看懂

### HTML 文字方向

```
<bdo dir="rtl">
我到底是正的反的
</bdo>
```


我到底是正的反的

### HTML 长的引用

```
<blockquote>长的引用,</blockquote>
```

> 长的引用,自动前后+换行,左右+外边距

### HTML 短的引用

```
<q>短的引用,自动+"",不自动换行</q>
```

短的引用,自动+””,不自动换行

### HTML 删除线

```
<del>删除线</del>
```

~~删除线~~

### HTML 被插入文本

```
<ins>插入线</ins>
```

插入线

### HTML 5有记号的文本

```
<mark> 有记号的文本</mark>
```

有记号的文本

### HTML 5规定范围内的度量

```
<meter value="3" min="0" max="10"></meter>
<meter value="0.6">60%</meter>
```



### HTML 预格式文本

```
<pre>
保留空格       和
换行符,使用ASCII 实体 符号
</pre>
保留空格       和
换行符,使用ASCII 实体 符号
```

### HTML 5任何类型的任务的进度条

```
<progress value="22" max="100"></progress>
```



### HTML 上标文本

```
<sup>上标</sup>
```

上标

### HTML 下标文本

```
<sub>下标</sub>
```

下标

### HTML 5日期/时间(截至2008主流浏览器均不支持)

```
<time datetime="2019-01-24">文档创建日</time>
```

文档创建日

### HTML 5可能的换行符

```
<p>要求改变窗口在<wbr>这里<wbr>换行</p>
```

要求改变窗口在这里换行

### HTML 计算机代码文本

```
<code>自动变为等宽字体</code>
自动变为等宽字体
```

### HTML 普通引用

```
<cite>普通引用,自动倾斜,不自带换行<cite>
```

普通引用,自动倾斜,不自带换行

### HTML 强调

```
<em>强调</em>
```

*强调*

### HTML 语气更强的强调

```
<strong>语气更强的强调</strong>
```

**语气更强的强调**

### HTML 定义一个定义项目

```
<dfn>定义项目</dfn>
```

定义项目

### HTML 样本文本

```
<samp>样本文本</samp>
```

样本文本

### HTML 键盘文本

```
<kbd>键盘文本</kbd>
```

键盘文本

### HTML 变量

```
<var>变量</var>
```

变量

## 表单

### HTML 定义供用户输入的 HTML 表单

```
<form action="/demo/demo_form.asp">
</form> 
<p>表单数据会被发送到名为 demo_form.asp 的页面。</p>
```

### HTML 输入控件

```
user name:<br>
<input type="text" name="user name" value="user name">
password:<br>
<input type="text" name="password" value="password">
<input type="submit" value="Submit">
```

user name:


password:





### HTML input 元素的标注

```
<form>
<label for="标注id">标注</label>
<input type="radio" name="标注" id="标注id" />
</form>
```


标注




\### HTML 5 input的下拉列表

```
<input id="number" list="listid" />
<datalist id="listid">
  <option value="0">
  <option value="1">
</datalist>
```








\### HTML 多行的文本输入控件

```
<textarea rows="3" cols="20">
你可以在这里输入任何数量的文本
</textarea>
```







\### HTML 按钮

```
<button type="button">我是一个不限制内容的按钮</button>
```



我是一个不限制内容的按钮

\### HTML 选择列表（下拉列表）

```
<select>
</select>
```







\### HTML 选择列表中的选项

```
<select>
  <option value ="0">0</option>
  <option value ="1">1</option>
  <option value ="a">a</option>
  <option value ="b">b</option>
</select>
```







\### HTML 选择列表中相关选项的组合

```
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







\### HTML 围绕表单中元素的边框

```
<fieldset>
</fieldset>
```



\### HTML fieldset 元素的标题

```
<fieldset>
  <legend>边框标题</legend>
</fieldset>
```






边框标题



如果表单周围没有边框,听说是浏览器的问题。



\### HTML 5 规定用于表单的密钥

```
<form action="/example/html5/demo_form.asp" method="get">
用户名：<input type="text" name="usr_name" />
加密：<keygen name="security" />
<input type="submit" />
</form>
```






用户名：
加密：



### HTML 5输出的一些类型

```
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

```
<frameset cols="25%,50%,25%">
</frameset>
```

### HTML 架集的窗口或框架

```
<frameset cols="50%,50%">
<frame src="https://charvin.cn/2019/01/23/Markdown%20For%20Typora/">
  <frame src="https://charvin.cn/2019/01/22/hello-world/">
</frameset>
```

### HTML 针对不支持框架的用户的替代内容

```
<frameset cols = "25%, 25%,*">
  <noframes>
  <body>您的浏览器无法处理框架！</body>
  </noframes>
</frameset>
```

### HTML 内联框架

```
<iframe src="https://charvin.cn/2019/01/23/Markdown%20For%20Typora/>
</iframe >
<iframe src="https://charvin.cn/2019/01/22/hello-world/>
</iframe >
```

## 图像

### HTML 图像

```
<img src="https://charvin.cn/img/avatar.png" width="104" height="142" />
```

[![undefined](https://charvin.cn/img/avatar.png)](https://charvin.cn/img/avatar.png)

### HTML 图像映射

```
<img src="https://charvin.cn/img/avatar.png" width="104" height="142" usemap="#clickarea"/>
<map name="clickarea" id="clickarea">
</map>
```

### HTML 定义图像映射内部的区域。

```
<img src="https://charvin.cn/img/avatar.png"
border="0"
usemap="#clickarea"
alt="clickarea  g"/>
<map name="clickarea" id="clickarea">
  <area shape="circle" coords="82,38,16" href ="https://charvin.cn/" alt="charvin" />
</map>
```

### HTML 5使用图形容器绘制图形

```
<canvas id="myCanvas">your browser does not support the canvas tag </canvas>
<script type="text/javascript">
var myCanvas=document.getElementById('myCanvas');
var ctx=myCanvas.getContext('2d');
ctx.fillStyle='#FF0000';
ctx.fillRect(0,0,80,100);
```



### HTML 5定义媒介内容（图像、图表、照片、代码等等）的分组，以及它们的标题

```
<figure>
  <p>my img</p>
  <img src="https://charvin.cn/img/avatar.png" />
</figure>
```



my img


[![undefined](https://charvin.cn/img/avatar.png)](https://charvin.cn/img/avatar.png)

### HTML 5定义 figure 元素的标题

```
<figure>
<figcaption>my img</figcaption>
  <img src="https://charvin.cn/img/avatar.png" />
</figure>
```


my img
[![undefined](https://charvin.cn/img/avatar.png)](https://charvin.cn/img/avatar.png)

## 音频/视频

### HTML 5声音内容

```
<audio src="https://charvin.cn/music/maliang-For%20the%20rest%20of%20the%20life.mp3" controls="controls">
</audio>
```

### HTML 5视频

```
<video src="https://charvin.cn/videos/小哥哥为什么都不追小姐姐了.mp4" controls="controls">
</video>
```

### HTML 5定义媒介源

```
<audio controls>
<source src="https://charvin.cn/videos/小哥哥为什么都不追小姐姐了.mp4" type="audio/mp4">
<source src="https://charvin.cn/musics/maliang-For%20the%20rest%20of%20the%20life.mp3" type="audio/mpeg">
 Your browser does not support the audio element.
</audio>
```

### HTML 5定义用在媒体播放器中的文本轨道(字幕)

```
<video width="320" height="240" controls="controls">
  <source src="forrest_gump.mp4" type="video/mp4" />
  <track kind="subtitles" src="subs_chi.srt" srclang="zh" label="Chinese">
</video>
```

## 链接

### HTML 定义超链接

```
<a href="https://charvin.cn/">This is my blog</a>
```

[This is my blog](https://charvin.cn/)

### HTML 定义文档与外部资源的关系

```
<link rel="stylesheet" type="text/css" href="theme.css" />
```

### HTML 定义导航链接

```
<nav>
<a href="https://charvin.cn/">Home</a>
<a href="https://charvin.cn/archives/">blog</a>
</nav>
```


[Home](https://charvin.cn/)
[blog](https://charvin.cn/archives/)

## 列表

### HTML 定义列表的项目

```
<li>项目</li>
```

项目

### HTML 无序列表

```
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```

- Coffee
- Tea
- Milk

### HTML 有序列表

```
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```

1. Coffee
2. Tea
3. Milk

### HTML 自定义列表中的项目

```
<dt>项目</dt>
```

### HTML 自定义列表中项目的描述

```
<dd>项目描述</dd>
```

### HTML 自定义列表

```
<dl>
   <dt>计算机</dt>
   <dd>用来计算的仪器 ... ...</dd>
   <dt>显示器</dt>
   <dd>以视觉方式显示信息的装置 ... ...</dd>
</dl>
```

- 计算机

  用来计算的仪器 … …

- 显示器

  以视觉方式显示信息的装置 … …

## 表格

### HTML 表格标题

```
<caption>标题</caption>
```

### HTML 表格中的表头单元格

```
<th>表头单元格</th>
```

### HTML 表格中的行

```
<tr></tr>
```

### HTML 表格中的单元

```
<td>单元</td>
```

### HTML 表格中的表头内容

```
<thead></thead>
```

### HTML 表格中的主体内容

```
<tbody></tbody>
```

### HTML 表格中的表注内容（脚注）

```
<tfoot></tfoot>
```

### HTML 表格中一个或多个列的属性值

```
<col />
```

### HTML 表格中供格式化的列组

```
<colgroup></colgroup>
```

### HTML 定义表格

```
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

























|  Month   | Savings |
| :------: | :-----: |
| January  |  $100   |
| February |   $80   |
|   Sum    |  $180   |

## 样式/分区

### HTML 定义文档的样式信息

```

```

### HTML 定义文档中的分区

```
<p>分区外没颜色.</p>
<div style="color:#00FF00">
<p>分区内有颜色(因为div自定义了专属style).</p>
</div>
```

分区外没颜色.





分区内有颜色(因为div自定义了专属style).





\### HTML 组合行内元素

```
<p><span>span内的文本</span>和外面没什么不一样,除非自定义了span的style</p>
```





span内的文本和外面没什么不一样,除非自定义了span的style

### HTML 5section 或 page 的页眉

```
<header>
</header>
```

### HTML 5section 或 page 的页脚

```
<footer>
</footer>
```

### HTML 5定义 section(文档中的分段)

```
<section></section>
```

### HTML 5定义文章

```
<article>
</article>
```

### HTML 5定义页面内容之外的内容

```
<aside></aside>
```

## 元信息

### HTML 定义关于 HTML 文档的元信息

```
<meta name="???"
content="???" http-equiv="???" scheme="???">
```

### HTML 定义页面中所有链接的默认地址或默认目标

```
<base target="_blank" href="https://charvin.cn/" />
```

## 编程

### HTML 插入 JavaScript

```
<script type="text/javascript">
</script>
```

### HTML 定义在脚本未被执行时的替代内容（文本）

```
<noscript>Sorry, your browser does not support JavaScript!</noscript>
```

### HTML 为外部应用程序（非 HTML）定义容器

```
<embed src="helloworld.swf" />
```

### HTML 定义嵌入的对象

```
<object classid="clsid:???" id="Slider1" 
width="100" height="50">
<param name="BorderStyle" value="1" />
</object>
```

### HTML 定义对象的参数

```
<param name="BorderStyle" value="1" />
```