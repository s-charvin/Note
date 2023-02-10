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
data: 2022-05-26 19:55:38
lastmod: 2022-05-26 19:55:45
---

# QML设计

QML是一种声明性语言。在QML中，用户界面被指定为具有属性的对象树。

一个PySide6/QML应用程序至少由两个不同的文件组成：

1. QML描述文件，定义用户界面，如`view.qml`

```css
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

2. 后端处理文件，加载QML文件，如`main.py`

```python
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView

if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    view = QQuickView()
    
    view.setSource("view.qml")
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.show()
    
    sys.exit(app.exec())
```

## 基本使用流程

定义QML文件

```css
import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

import io.qt.textproperties 1.0

ApplicationWindow {
    id: page
    width: 800
    height: 400
    visible: true
    Material.theme: Material.Dark
    Material.accent: Material.Red

    Bridge {
        id: bridge
    }

    GridLayout {
        id: grid
        columns: 2
        rows: 3

        ColumnLayout {
            spacing: 2
            Layout.columnSpan: 1
            Layout.preferredWidth: 400

            Text {
                id: leftlabel
                Layout.alignment: Qt.AlignHCenter
                color: "white"
                font.pointSize: 16
                text: "Qt for Python"
                Layout.preferredHeight: 100
                Material.accent: Material.Green
            }

            RadioButton {
                id: italic
                Layout.alignment: Qt.AlignLeft
                text: "Italic"
                onToggled: {
                    leftlabel.font.italic = bridge.getItalic(italic.text)
                    leftlabel.font.bold = bridge.getBold(italic.text)
                    leftlabel.font.underline = bridge.getUnderline(italic.text)

                }
            }
            RadioButton {
                id: bold
                Layout.alignment: Qt.AlignLeft
                text: "Bold"
                onToggled: {
                    leftlabel.font.italic = bridge.getItalic(bold.text)
                    leftlabel.font.bold = bridge.getBold(bold.text)
                    leftlabel.font.underline = bridge.getUnderline(bold.text)
                }
            }
            RadioButton {
                id: underline
                Layout.alignment: Qt.AlignLeft
                text: "Underline"
                onToggled: {
                    leftlabel.font.italic = bridge.getItalic(underline.text)
                    leftlabel.font.bold = bridge.getBold(underline.text)
                    leftlabel.font.underline = bridge.getUnderline(underline.text)
                }
            }
            RadioButton {
                id: noneradio
                Layout.alignment: Qt.AlignLeft
                text: "None"
                checked: true
                onToggled: {
                    leftlabel.font.italic = bridge.getItalic(noneradio.text)
                    leftlabel.font.bold = bridge.getBold(noneradio.text)
                    leftlabel.font.underline = bridge.getUnderline(noneradio.text)
                }
            }
        }

        ColumnLayout {
            id: rightcolumn
            spacing: 2
            Layout.columnSpan: 1
            Layout.preferredWidth: 400
            Layout.preferredHeight: 400
            Layout.fillWidth: true

            RowLayout {
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter


                Button {
                    id: red
                    text: "Red"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        leftlabel.color = bridge.getColor(red.text)
                    }
                }
                Button {
                    id: green
                    text: "Green"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        leftlabel.color = bridge.getColor(green.text)
                    }
                }
                Button {
                    id: blue
                    text: "Blue"
                    highlighted: true
                    Material.accent: Material.Blue
                    onClicked: {
                        leftlabel.color = bridge.getColor(blue.text)
                    }
                }
                Button {
                    id: nonebutton
                    text: "None"
                    highlighted: true
                    Material.accent: Material.BlueGrey
                    onClicked: {
                        leftlabel.color = bridge.getColor(nonebutton.text)
                    }
                }
            }
            RowLayout {
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
                Text {
                    id: rightlabel
                    color: "white"
                    Layout.alignment: Qt.AlignLeft
                    text: "Font size"
                    Material.accent: Material.White
                }
                Slider {
                    width: rightcolumn.width*0.6
                    Layout.alignment: Qt.AlignRight
                    id: slider
                    value: 0.5
                    onValueChanged: {
                        leftlabel.font.pointSize = bridge.getSize(value)
                    }
                }
            }
        }
    }
}


```

```python
import sys
from pathlib import Path

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle

import style_rc

# To be used on the @QmlElement decorator

# (QML_IMPORT_MINOR_VERSION is optional)

QML_IMPORT_NAME = "io.qt.textproperties"

QML_IMPORT_MAJOR_VERSION = 1

# 利用QmlElement修饰器定义一个Bridge类
# 其中包含在QML中注册的元素的所有后端逻辑。
# 之后在ApplicationWindow加载的界面文件中，
# 声明一个与Bridge类同名的组件，并给定一个id。
# 通过该id可以使用该注册元素和连接其后端逻辑函数。
@QmlElement
class Bridge(QObject):

    @Slot(str, result=str)
    def getColor(self, s):

        if s.lower() == "red":
            return "#ef9a9a"
        elif s.lower() == "green":
            return "#a5d6a7"
        elif s.lower() == "blue":
            return "#90caf9"
        else:
            return "white"

    @Slot(float, result=int)
    def getSize(self, s):
        size = int(s * 34)
        if size <= 0:
            return 1
        else:
            return size

    @Slot(str, result=bool)
    def getItalic(self, s):
        if s.lower() == "italic":
            return True
        else:
            return False

    @Slot(str, result=bool)
    def getBold(self, s):
        if s.lower() == "bold":
            return True
        else:
            return False

    @Slot(str, result=bool)
    def getUnderline(self, s):
        if s.lower() == "underline":
            return True
        else:
            return False


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()
  
    # Get the path of the current directory, and then add the name of the QML file, to load it.

    qml_file = Path(__file__).parent / 'view.qml'
    engine.load(qml_file)

    if not engine.rootObjects():

        sys.exit(-1)

    sys.exit(app.exec())
```

注意，注册要归功于QmlElement修饰器，它下面使用对Bridge类的引用以及变量QML_IMPORT_NAME和QML_IMPORT_MAJOR_VERSION。

现在，返回到QML文件并将信号连接到Bridge类中定义的插槽：

在ApplicationWindow中，我们声明一个与Python类同名的组件，并提供id：。该id将帮助您获得对从Python注册的元素的引用。

斜体、粗体和下划线属性是相互排斥的，这意味着任何时候只能有一个处于活动状态。为了实现这一点，每次我们选择这些选项之一时，我们通过QML元素属性检查三个属性，如您在上面的代码片段中所看到的。三个参数中只有一个将返回True，而其他两个将返回False，这就是我们如何确保只有一个应用于文本的方法。

每个槽验证所选选项是否包含与属性相关联的文本：

返回True或False允许您激活和停用QML UI元素的属性。
也可以返回非布尔值的其他值，如负责返回字体大小的槽：

现在，要更改应用程序的外观，您有两个选择：

使用命令行：执行添加选项-style的python文件：

使用qtQuickContros2.conf文件：然后将其添加到您的.qrc文件中：
生成运行的RC文件，即pyside 6-rcc style le.qrc&gt;style_rc.py，最后从main.py脚本导入它。

@QmlElement
