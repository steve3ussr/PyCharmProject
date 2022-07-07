# Ref

 [PySide6官方教程 循序渐进学好Qt for Python_两只程序猿的博客-CSDN博客_pyside6](https://blog.csdn.net/baidu_36499789/article/details/113835688)

[【Qt for Python官方教程】使用QUiLoader和pyside6-uic导入ui文件_两只程序猿的博客-CSDN博客_pyside6 uic](https://blog.csdn.net/baidu_36499789/article/details/119486355)

[Python 图形界面框架 PySide6 使用及避坑指南_java编程艺术的博客-CSDN博客_pyside6](https://blog.csdn.net/penriver/article/details/122686212?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-122686212-blog-119486355.pc_relevant_multi_platform_whitelistv2&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-122686212-blog-119486355.pc_relevant_multi_platform_whitelistv2&utm_relevant_index=1)

[【Qt for Python官方教程】改变Qt Widgets程序的样式_两只程序猿的博客-CSDN博客_python qtwidgets](https://blog.csdn.net/baidu_36499789/article/details/119712023)

https://zhuanlan.zhihu.com/p/445661017

# TODO

- [x] 多个窗口

- [x] 创建widget并调用

- [ ] 自定义信号发射

- [ ] `exec()`, `show()`

# 安装

Qt是一个公司的.

PySide 是这个公司的官方版, 开源; 

PyQt 是第三方做的, 商用要收费. 

## 配置

可以在Pycharm 里配置外部工具. 

配置 UIC, RCC 和 QtDesigner，程序在python/script

|            | 实参                                               | 工作目录               |
| ---------- | ------------------------------------------------ |:------------------ |
| UIC        | `$FileName$ -o $FileNameWithoutExtension$.py`    | `$FileDir$`        |
| RCC        | `$FileName$ -o $FileNameWithoutExtension$_rc.py` | `$FileDir$`        |
| QtDesigner |                                                  | `$ProjectFileDir$` |

# 基础知识

1. Qt 是用C++设计和编写的C++框架, 有的时候Qt指Qt框架, 有的时候指Qt项目. 

2. 一个框架包含许多组件, 和模块;
   
   1. 比如`QtCore`是一个含有许多模块的基本组件;
   
   2. 这些模块含有许多可以直接使用的类; 
   
   3. 这样就可以创建没有GUI的应用程序; 
   
   4. **或者**: 使用`QtWidgets` 模块中的类创建GUI, 比如按钮, 标签, 框, 等等. 

# Hello, World!

```python
import sys
from PySide6.QtWidgets import QApplication, QLabel


app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.show()
app.exec()
```

1. `QApplication`: 创建一个实例, 其实不用传递参数 (`inst = QApplication([])`) , 但是也可以传; 

2. `sys.argv` : 一个 list , 储存命令行的参数; 

3. `Qlabel()`: 一个可以显示文本和图像的容器。文本可以是简单文本，也可以是富文本; 

4. 创建标签后要调用 `show()` 函数才能显示; 

5. `app.exec()`: 进入主循环，开始执行代码 (上一步的 show 到这里才有用) ; 

# Signal & Slot

>  这是 Qt 的特色, 用来让你的图形组件与其他图形组件或 Python 代码交流。
> 
> - 信号: 对象发生变化时, 就发射一个信号; 
> 
> - 信号应该连接到槽上 / 信号上; 一个信号对多个槽, 多个信号也可对应一个槽;  
> 
> - 发射信号后, 槽会立即执行, 就像普通函数调用; 
> 
> - 信号和槽: 不同对象之间的通讯; 
> 
> [pyqt, signal, slot]([信号与槽的详解_耐耐~的博客-CSDN博客_信号和槽](https://blog.csdn.net/f156207495/article/details/77387079))

```python
import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


@Slot()
def say_hello():
    print("Button clicked, Hello!")


app = QApplication(sys.argv)
button = QPushButton('DO NOT PRESS F')

button.clicked.connect(say_hello)
button.show()
app.exec()
```

> PyCharm 经年 bug: 无法正确检测 connect 方法

1. 定义了一个按钮; 

2. 按钮自带 `clicked` 信号, 把这个信号和一个槽连接起来; 

3. 槽这里是自定义的函数, 输出到 python 控制台; 

4. `@Slot()` 将一个函数变成一个槽; 

# A Dialog with Input

```python
import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog
)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # 创建组件
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        # 创建布局并添加组件
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # 应用布局
        self.setLayout(layout)
        # 连接greetings槽和按钮单击信号
        self.button.clicked.connect(self.greetings)

    # 向用户打招呼
    def greetings(self):
        print(f"Hello {self.edit.text()}")

if __name__ == '__main__':
    # 创建Qt应用程序
    app = QApplication(sys.argv)
    # 创建并显示Form
    form = Form()
    form.show()
    # 运行Qt主循环
    sys.exit(app.exec())
```

1. 可以任意创建 PySide6 中组件的子类: 在这里创建了一个`QDialog` 的子类; 

2. 调用父类组件的初始化方法

3. `setWindowTitle()`用于创建窗口的标题; 

两个组件:

1. `QLineEdit`: 这是一个允许用户输入和编辑单行纯文本的单行文本输入框. 

2. `QPushBotton`: 用于点击后输出; 

布局: 

1. `QVBoxLayout`: 用于对组件垂直布局; 

2. 并且在布局中加入两个组件; 

3. 别忘了`setLayout()` !

输出: 

1. 定义一个 print 函数; 

2. 将其与 clicked 相连接; 

3. 通过 `QLineEdit.text()` 获取文本;

运行: 

1. 据说这个sys.exit()其实没什么作用，他其实就是用来反映程序终止的状态的，在它有父进程的情况下最好有这个sys.exit()通过她的返回值可以判断子进程的状态。而在没有子进程的程序中，其实sys.exit(app.exec_())和app.exec_()效果是一样的。

# Qt Designer simp case

创建一个 MainWindow，插入各种组件，在右上角可以修改各种对象名。

左上角窗体，可以预览

保存成`.ui`后，可以被python使用，使用方式（对于这个MainWindow类型的 ui ）：

1. 用`PyUIC`转成py后导入，其中的类的attr中有我们之前定义的对象名，在主程序里写slot就行

2. 通过文件的形式动态读取`.ui`文件：

```python
from PySide6.QtUiTools import QUiLoader


ui_file = QFile("mainwindow.ui")
ui_file.open(QFile.ReadOnly)

loader = QUiLoader()
window = loader.load(ui_file)
window.show()
```

# Main & Slave Window

```python
from ui_window2 import Ui_Dialog
from ui_str_connect import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    # str_signal = Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_print.clicked.connect(self.res_print)

    def res_print(self):
        res = self.ui.lineEdit_1.text() + self.ui.lineEdit_2.text()
        slave_window = SlaveWindow()
        slave_window.ui.textBrowser.setText(res)
        slave_window.ui.pushButton.clicked.connect(self.close_main)
        slave_window.exec()

    @Slot()
    def close_main(self):
        self.close()


class SlaveWindow(QDialog):
    # str_signal = Signal(str, str)

    def __init__(self):
        super(SlaveWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close_all)

    @Slot()
    def close_all(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
```

在这个例子中: 

1. slave 由 主窗口信号触发, 才生成; 

2. 主窗口点击 -> 从窗口初始化; 

3. 从窗口点击 -> 主从窗口关闭. 

# 打开文件

```python

 @Slot()
 def open_explorer(self):
     file_path = QFileDialog.getOpenFileName(QMainWindow(), "选择文件夹")[0]  # 选择目录，返回选中的路径
     print(type(file_path))
     self.ui.textEdit.setText(file_path)

```

