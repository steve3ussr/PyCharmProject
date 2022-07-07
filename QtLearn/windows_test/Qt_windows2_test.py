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
