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
data: 2022-05-04 20:04:39
lastmod: 2022-05-26 20:46:23
---

# Qt的文件类型

.py

Python文件。当使用Python语言进行项目开发时，主要使用文件格式是.py文件，其余像.ui、.qrc或.qml文件不是必需的，但是使用其他格式可以简化某些过程，并使用一些新功能。

.ui

用户界面定义文件。当使用Qt Designer时，可以使用所见即所得的UI编辑器，通过Qt组件创建用户界面，该界面使用XML格式保存组件树，最终生成.ui文件。

pyside6-uic工具可以从将.ui文件转换成Python代码，当然也可以使用PySide6.QtUiTools.QUiLoader直接加载.ui文件。

.qrc

资源文件列表。也是基于XML格式的文件。

pyside6-rcc工具可以从将.qrc文件转换成Python代码。

.qml

图形化的QML与Qt Widgets等部件没有什么关联，因此想要使用QML项目，需要在Python文件内部加载.qml文件。.qml文件，可以使用内置在Qt Creator中的QML Designer、Qt Design Studio等工具进行编写，当然，如果编码能力强，也可以自己手动编写。

.pyproject

Python项目列表。要让Qt Creator加载和处理基于Python的项目，需要一个特殊的文件，即.pyproject文件。该文件是一个基于JSON的文件，可以在其中添加任意项目文件。

# Qt项目分发

在开发完应用程序之后，需要创建一个Python可执行文件。

Python应用程序的部署过程称为“freezing”，它会将你的虚拟环境内容分发给其他用户。

由于Python不支持WebAssembly和移动平台，如Android和iOS，您不能直接将应用部署到这些平台上，您需要高级流程才能完成此操作。

对于嵌入式系统，您目前需要为您的目标平台构建Qt for Python，并将安装与您的应用程序一起部署。

一种常见的方法是只提供一个Requirements.txt文件，在该文件中声明您的依赖项。用户需要从那里安装它们才能运行您的应用程序。
例如，假设我有一个具有两个依赖项的项目，模块a和模块b，我在main.py文件中使用这两个依赖项。

您可以注意到，这种方法包括共享您的代码，因此如果您想隐藏应用程序的代码，它将失败。


这是用户分发其应用程序的最常见方法，即使最终用户仍然可以使用代码，检索它也会稍微困难一些。
在我们的Qt for Python部署部分，您可以找到一系列基于最流行工具的教程，这些工具允许Python用户冻结和分发应用程序。

尽管Python本身并不支持编译，但有一些补充工具可以让您实现这一点。您可以查看Nuitka项目以了解更多信息。

# 扩展Qt/C++项目

## 基本区别

### C++ vs Python

- C++和Python均含有代码重用方法，即当前代码文件导入其他代码文件的功能。在C++中，使用`#INCLUDE`指令。等效于Python的是一条`import`语句。
- C++类的构造类会自动调用其基类的构造函数(以预定义的顺序)。Python中，可以利用__init__()方法，以任何顺序显式调用基类构造函数。
- C++使用关键字This隐式引用当前对象。在Python中，需要显式地将当前对象作为类的每个实例方法的第一个参数，通常为`self`。
- 更重要的是，Python要忘记大括号`{}`和分号`；`。
- Python 仅当变量定义需要全局作用域时，才在变量定义之前使用GLOBAL关键字。

# 元对象系统

Qt的元对象系统提供了用于对象间通信的信号和槽机制、运行时类型信息保存和动态属性设置等功能的基础。

`QObject`类为利用元对象系统中所有对象的基类。可以通过在类的私有部分中生声明`Q_OBJECT`宏，启用元对象特性。之后元对象编译器（Moc）(MOC)会为每个`QObject`子类提供实现元对象功能所需的代码。Moc工具将读取C++源文件，如果它找到一个或多个声明`Q_OBJECT`宏的类，它会生成另一个C++源文件，其中包含每个类的元对象代码。

```python
class MyClass(QObject):

    Q_OBJECT
    ...
```

## 信号与信号槽

信号和信号槽是窗口小部件与Python代码进行通信的桥梁，例如，点击是信号，信号槽是按钮被点击后发生的事件，比如关闭窗口、保存文档等。

### 信号

`emit` 会从当前对象发出信号`valueChanged()`，并将新值`value`作为参数，传递进去。

```python
class Counter(QObject):            
	Q_OBJECT
# public
	Counter() { m_value = 0; }
	int value() { return m_value; }
slots: = public()
def setValue(self, value):
    if (value != m_value) {
        m_value = value
        valueChanged.emit(value)
signals:
    def valueChanged(newValue):
    return newValue
# private
	m_value = int()

```

### 信号槽

通过装饰符:`@Slot()` ,可以将将函数标识为信号槽。

`name`参数可以自定义当前信号槽函数的参数名称，默认为正在修饰的函数名。

`result`参数可以定义此槽函数返回的数据类型，可以是C或Python类型。

### 连接

信号与信号槽之间使用connect()方法来连接。

- `connect()`方法返回一个QMetaObject.Connection类型对象。

```python
QObject.connect(a, Object.Signal,b,Object::slot)
Object.event.connect(slot)
```

- `disconse()`方法可以切断连接。

在用Python编写基于QWidget的组件class时，组件的信号由class变量表示，此变量被声明为`QtCore.Signal()`。例如，基于QWidget的按钮可以发出Click()信号：

```python
class Button(QWidget):
	# `Signal`可以接受一个或一组Python类型和C类型的元组：
	# Signal((float,int,str), (QDate,QUrl))
	# 通过name参数可以定义当前信号的参数名称，默认为被幅值的变量名称，如下面的clicked
	# 通过arguments参数可以定义QML应用接收的信号参数名称
    clicked = Signal(Qt.MouseButton)
    ...
    def mousePressEvent(self, event):
        self.clicked.emit(event.button())

```

## 对象属性系统

- 要声明属性，可以在继承自`QObject`的类中使用`Q_PROPERTY()`宏。
	```python
	Class MyClass(QObject):
	    Q_OBJECT
	    # `READ`函数映射为`priority`
	    # WRITE函数映射为setPriority
	    # 自定义了一个Priority类型的priority
	    Q_PROPERTY(Priority priority READ priority WRITE setPriority NOTIFY priorityChanged)
	    ...
	```

- 调用对象属性可以通过已经指定的内置函数操作，也可以通过给定属性名称，使用`.setProperty("name", value)`方法。
	```
	button.setDown(True)
	object.setProperty("down", True)
	```

- 要访问类的属性，已知或者未知的，可以通过遍历`metaObject()` 函数会返回当前类关联的 `meta-object`，然后再通过 `property()`函数获取类中定义的每个属性的元数据。
	```python
	object = ...
	metaobject = object.metaObject()
	count = metaobject.propertyCount()
	for i in range(0, count):
	    metaproperty = metaobject.property(i)
	    name = metaproperty.name()
	    value = object.property(name)
	    ...
	```

## 附加功能

`metaObject()` 函数会返回当前类关联的 `meta-object` 。
  
`className()` 函数会以字符串形式返回当前类的类名。

`inherits()` 函数会通过输入的类名字符串，判断当前类是否是`QObject` 继承树中的一类，字符串所代表的类名应在继承树中。

`tr()` 翻译字符串以实现国际化。

`setProperty()` 和 `property()` 函数可以动态的按name和key设置或获取类属性。

`newInstance()` 函数会基于此类，建立一个新类。

 QML

QML描述文件（定义用户界面）

QML将前端的用户界面及其内部各个组件模块看作是单独的对象，然后通过固定格式，以树的形式搭配各个对象模块。之后通过Python或者C++语言编写后端。

```python
import QtQuick

Rectangle {
    id: main
    width: 200
    height: 200
    color: "green"

    Text {
        text: "Hello World"
        anchors.centerIn: main
    }
}
```
