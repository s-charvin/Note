本文标题:Markdown For Typora

文章作者:大傻瓜

标签：
Markdown
Typora
学习

发布时间:2019-01-23, 02:10:00

最后更新:2019-01-23, 02:10:00



## 常用Typora_Markdown语法. 以备写文章所需.

> 每天收获小进步，积累起来就是大进步；



# 标题:

# 这是一级标题

```
# 这是一级标题
```

## 这是二级标题

```
## 这是二级标题
```

### 这是三级标题

```
### 这是三级标题
```

#### 这是四级标题

```
#### 这是四级标题
```

##### 这是五级标题

```
##### 这是五级标题
```

###### 这是六级标题

```
###### 这是六级标题
```

# 引用文字

> 这是一个有一个段落的块引用。
>
> 这是第二段
>
> ```
> > 这是一个有一个段落的块引用。
> >
> >这是第二段
> ```

# 链接引用

```
[链接引用]: https://www.charvin.cn/
```

# 列表

## 无序列表

- 红色

- 绿色

- 蓝色

  ```
  *   红色
  *   绿色
  *   蓝色
  ```

## 有序列表

1. 红色

2. 绿色

3. 蓝色

   ```
   1.  红色
   2. 	绿色
   3.	蓝色
   ```

# 任务列表

-  这是一 个未完成任务列表项

-  

  完成

  ```
  -  这是一个未完成任务列表项
  - [x] 完成
  ```

# 数学公式块



V1×V2=∣∣ijk ∂X∂u∂Y∂u0 ∂X∂v∂Y∂v0 ∣∣V1×V2=|ijk ∂X∂u∂Y∂u0 ∂X∂v∂Y∂v0 |





```
$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} 
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
\end{vmatrix}
$$
```



# 表格

| Left-Aligned                                                 | Center Aligned  | Right Aligned |
| :----------------------------------------------------------- | :-------------: | ------------: |
| *倾斜*                                                       | some wordy text |         $1600 |
| **加粗**                                                     |    centered     |           $12 |
| [超链接](https://s-charvin.github.io/2019/01/23/Markdown For Typora/) |    are neat     |            $1 |

最左侧的冒号表示左对齐的列; 最右侧的冒号表示右对齐的列; 两侧的冒号表示中心对齐的列。

```
| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| *倾斜* | some wordy text | $1600 |
| **加粗**  | centered        |   $12 |
| [超链接]() | are neat        |    $1 |
```

# 水平线

------

------

```
***
---
```

# URL网址

[i@typora.io](mailto:i@typora.io)

```
<i@typora.io>
```

# 超链接

This is an [example](https://www.charvin.cn/2019/01/23/Markdown For Typora/) reference-style link.

```
This is an [example](https://www.charvin.cn/2019/01/23/Markdown%20For%20Typora/) reference-style link.
```

# 图片

[![替代文字](https://www.charvin.cn/img/avatar.png)](https://www.charvin.cn/img/avatar.png)

```
![替代文字](https://www.charvin.cn/img/avatar.png "可选标题")
```



# 强调（斜体） 粗体 删除线 下划线

**强调**
*斜体*
~~删除线~~
下划线

```
**强调**
*斜体*
~~删除线~~
<u>下划线</u>
```

# 短代码

```
printf()
`printf()`
```



# 代码块

```
function test() {
  console.log("notice the blank line before this function?");
}
```

# 下标 上标 高亮

H~2~O, X~long\ text~
X^2^
==highlight==

```
H~2~O, X~long\ text~
X^2^
==highlight==
```

# HTML

```

```

# 视频



<iframe frameborder="0" width="400" height="400" src="https://v.qq.com/txp/iframe/player.html?vid=d0840lp92pj" allowfullscreen="true" style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-weight: 400; font-style: normal; font-family: &quot;Lucida Grande&quot;, Verdana, &quot;Helvetica Neue&quot;, Arial, &quot;Microsoft YaHei&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif; font-size: 16px; vertical-align: baseline; color: rgb(51, 51, 51); font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgba(255, 255, 255, 0.45); text-decoration-style: initial; text-decoration-color: initial;"></iframe>



```
<video id="video" controls="" preload="none" >
	<source id="123" src="https://www.charvin.cn//video/20190220_140403.mp4" type="video/mp4">
	您的浏览器不支持 video 标签。
</video>
<iframe 
    id="Example2"
    title="Example2"
    width="400"
    height="300"
    frameborder="0"
    scrolling="no"
    marginheight="0"
    marginwidth="0"
    src="https://v.qq.com/txp/iframe/player.html?vid=d0840lp92pj" allowFullScreen="true">
</iframe>
```

# 音频



<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width="330" height="86" src="https://music.163.com/outchain/player?type=2&amp;id=572035587&amp;auto=0&amp;height=66" style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-weight: 400; font-style: normal; font-family: &quot;Lucida Grande&quot;, Verdana, &quot;Helvetica Neue&quot;, Arial, &quot;Microsoft YaHei&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif; font-size: 16px; vertical-align: baseline; color: rgb(51, 51, 51); font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgba(255, 255, 255, 0.45); text-decoration-style: initial; text-decoration-color: initial;"></iframe>



```
<audio controls="controls">
  <source src="https://www.charvin.cn/music/往后余生-马良.mp3" type="audio/mp3">
您的浏览器不支持 audio 标签。
</audio>
<iframe 
        frameborder="no" 
        border="0" 
        marginwidth="0" 
        marginheight="0" 
        width=330 
        height=86 
        src="//music.163.com/outchain/player?type=2&id=572035587&auto=1&height=66">
</iframe>
```

# 脚注

```
[^脚注]: 脚注介绍
```