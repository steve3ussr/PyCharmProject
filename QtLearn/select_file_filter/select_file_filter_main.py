import sys
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog
from PySide6.QtCore import Slot


@Slot()
def open_explorer(self):
    file_path = QFileDialog.getOpenFileName(QMainWindow(),
                                            caption="选择文件",
                                            dir=".",
                                            filter="Python Files .py(*.py);;Markdown doc (*.md; *.markdown)")[0]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    button = QPushButton('click me')
    button.clicked.connect(open_explorer)
    button.show()
    sys.exit(app.exec())
