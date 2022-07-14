from PySide6.QtCore import Slot, QTimer
from ui_widget_disabled import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
import time


# 需求:
# 初始 radio 不可用
# 每次点击根据 text 状态确定是否可用


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolButton.clicked.connect(self.select_file)
        # self.ui.radioButton.clicked.connect(self.status_preCheck)
        self.timer = QTimer()
        self.timer.start(50)
        self.timer.timeout.connect(self.JIT_status_update)

    @Slot()
    def JIT_status_update(self):
        self.ui.lineEdit_2.setText(self.ui.lineEdit.text())
        if self.ui.lineEdit.text():
            self.ui.radioButton.setEnabled(True)
        else:
            self.ui.radioButton.setEnabled(False)
            self.ui.radioButton.setChecked(False)

    @Slot()
    def select_file(self):
        file_path = QFileDialog.getOpenFileName(QMainWindow(),
                                                caption="给我选!",
                                                dir='.',
                                                filter='Python File (*.py)')
        print(file_path)
        self.ui.lineEdit.setText(file_path[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
