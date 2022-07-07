from QtLearn.windows_test.ui_str_connect import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_print.clicked.connect(self.str_combine)

    @Slot()
    def str_combine(self):
        print(f'{self.ui.lineEdit_1.text() + self.ui.lineEdit_2.text()}')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
