from PySide6.QtCore import Slot
from ui_radio_button import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys


# demo 目标:
# 一按按钮, 就在控制台print当前选择的是哪个radio


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(self.status_check)
        self.file_path = None

    @Slot()
    def status_check(self):
        if self.ui.radio_button_md.isChecked():
            # print('MDMDMDMDMDMDMD')
            filter_str = 'Markdown doc (*md; *markdown)'
            self.file_path = QFileDialog.getOpenFileName(QMainWindow(),
                                                         caption="选择文件",
                                                         dir=".",
                                                         filter=filter_str)[0]
        elif self.ui.radio_button_py.isChecked():
            # print('pypypypypypypypypy')
            filter_str = 'Python File (*py)'
            self.file_path = QFileDialog.getOpenFileName(QMainWindow(),
                                                         caption="选择文件",
                                                         dir=".",
                                                         filter=filter_str)[0]
        else:
            raise TypeError('NON py md')
        print(f'selected file path: {self.file_path}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
