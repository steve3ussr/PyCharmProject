from PySide6.QtCore import Slot
from ui_load_file_test import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setter_file(self.ui.toolButton_src_a2l, self.ui.lineEdit_src_a2l, '*.a2l')
        self.setter_file(self.ui.toolButton_src_hex_s19, self.ui.lineEdit_src_hex_s19, ('*.hex', '*.s19'))
        self.setter_file(self.ui.toolButton_tgt_a2l, self.ui.lineEdit_tgt_a2l, '*.a2l')
        self.setter_file(self.ui.toolButton_tgt_hex_s19, self.ui.lineEdit_tgt_hex_s19, '*.hex; *.s19')

        self.setter_file(self.ui.toolButton_dcm, self.ui.lineEdit_dcm, '*.dcm')
        self.setter_folder(self.ui.toolButton_xlsx, self.ui.lineEdit_xlsx, '*.xlsx')
        self.setter_folder(self.ui.toolButton_merged, self.ui.lineEdit_merged, '*.xlsx')


    """def res_format(self):
        if self.ui.radioButton_hex.isChecked():
            return '*.hex'
        elif self.ui.radioButton_s19.isChecked():
            return '*.s19'
        else:
            raise"""

    def setter_file(self, a_button, a_line, a_str):
        a_button.clicked.connect(self.select_file(a_line, a_str))

    @Slot()
    def select_file(self, a_line, a_str):
        def select_file_inner():
            file_path = QFileDialog.getOpenFileName(QMainWindow(),
                                                    caption="选择文件",
                                                    dir=".",
                                                    filter=a_str)[0]  # 选择目录，返回选中的路径
            a_line.setText(file_path)
        return select_file_inner

    def setter_folder(self, a_button, a_line, a_str):
        a_button.clicked.connect(self.select_folder(a_line, a_str))

    @Slot()
    def select_folder(self, a_line, a_str):
        def select_folder_inner():
            folder_path = QFileDialog.getSaveFileName(QMainWindow(),
                                                      caption="保存文件",
                                                      dir=".",
                                                      filter=a_str)[0]  # 选择目录，返回选中的路径
            a_line.setText(folder_path)
        return select_folder_inner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
