from PySide6.QtCore import Slot, QTimer
from ui_merge_tool_demo import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__out_format = 'hex'
        self.__set_optional_internal_link()
        self.__set_toolButtons()
        self.__set_timer()

        self.test_auto_fill()
        self.ui.pushButton.clicked.connect(self.__main_exec)

    def __set_optional_internal_link(self) -> None:
        """
        for dcm, merged file and xlsx: 
            link checkBox with (lineEdit and toolButton)
        """
        self.ui.checkbox_dcm.clicked['bool'].connect(self.ui.lineEdit_dcm.setEnabled)
        self.ui.checkbox_dcm.clicked['bool'].connect(self.ui.toolButton_dcm.setEnabled)
        self.ui.checkBox_merged.clicked['bool'].connect(self.ui.lineEdit_merged.setEnabled)
        self.ui.checkBox_merged.clicked['bool'].connect(self.ui.toolButton_merged.setEnabled)
        self.ui.checkBox_xlsx.clicked['bool'].connect(self.ui.lineEdit_xlsx.setEnabled)
        self.ui.checkBox_xlsx.clicked['bool'].connect(self.ui.toolButton_xlsx.setEnabled)

    def __set_toolButtons(self):
        """
        set Slots for all toolButtons
        """
        self.__get_file(self.ui.toolButton_src_a2l, self.ui.lineEdit_src_a2l, 'ECU ASAM-2MC (*.a2l)')
        self.__get_file(self.ui.toolButton_src_hex_s19,
                        self.ui.lineEdit_src_hex_s19,
                        'Intel (*.hex);;Motorola32 (*.s19)')

        self.__get_file(self.ui.toolButton_tgt_a2l, self.ui.lineEdit_tgt_a2l, 'ECU ASAM-2MC (*.a2l)')
        self.__get_file(self.ui.toolButton_tgt_hex_s19,
                        self.ui.lineEdit_tgt_hex_s19,
                        'Intel (*.hex);;Motorola32 (*.s19)')

        self.__get_file(self.ui.toolButton_dcm, self.ui.lineEdit_dcm, 'DCM File (*.dcm)')
        self.__save_file(self.ui.toolButton_xlsx, self.ui.lineEdit_xlsx, 'Excel File (*.xlsx)')

        temp_str = 'Intel (*.hex)' if self.__out_format == 'hex' else 'Motorola32 (*.s19)'
        self.__save_file(self.ui.toolButton_merged, self.ui.lineEdit_merged, temp_str)

    def __set_timer(self):
        """
        set a timer to check and update statuses
        """
        self.timer = QTimer()
        self.timer.start(50)
        self.timer.timeout.connect(self.__JIT_status_update)

    def __get_file(self, a_button, a_line, a_str) -> None:
        """
        just don't want to see many '.clicked.connect'
        """
        a_button.clicked.connect(self.__select_file(a_line, a_str))

    def __save_file(self, a_button, a_line, a_str) -> None:
        """
        just don't want to see many '.clicked.connect'
        """
        a_button.clicked.connect(self.__select_folder(a_line, a_str))

    @Slot()
    def __select_file(self, a_line, a_str):
        """
        Slot without decorator will execute(open Dialog) when initializing
        """
        def __select_file_inner() -> None:
            file_path = QFileDialog.getOpenFileName(QMainWindow(),
                                                    caption="选择文件",
                                                    dir=".",
                                                    filter=a_str)
            a_line.setText(file_path[0])

        return __select_file_inner

    @Slot()
    def __select_folder(self, a_line, a_str):
        """
        Slot without decorator will execute(open Dialog) when initializing
        """
        def select_folder_inner():
            folder_path = QFileDialog.getSaveFileName(QMainWindow(),
                                                      caption="保存文件",
                                                      dir=".",
                                                      filter=a_str)[0]  # 选择目录，返回选中的路径
            a_line.setText(folder_path)

        return select_folder_inner

    def __update_out_format(self) -> None:
        """
        update self.out_format(.hex / .s19) according to REQUIRED radioButton
        """
        if self.ui.radioButton_hex.isChecked():
            self.__out_format = 'hex'
        else:
            self.__out_format = 's19'

    def __check_required(self) -> bool:
        """
        check required(src and tgt; a2l, hex/s19):
            has valid path or not
        """
        src_a2l_path = self.ui.lineEdit_src_a2l.text()
        src_hex_s19_path = self.ui.lineEdit_src_hex_s19.text()
        tgt_a2l_path = self.ui.lineEdit_tgt_a2l.text()
        tgt_hex_s19_path = self.ui.lineEdit_tgt_hex_s19.text()

        if self.__check_path_format(src_a2l_path, 'a2l') and \
                self.__check_path_format(src_hex_s19_path, 'hex', 's19') and \
                self.__check_path_format(tgt_a2l_path, 'a2l') and \
                self.__check_path_format(tgt_hex_s19_path, 'hex', 's19'):
            return True
        else:
            return False

    @staticmethod
    def __check_path_format(path, *format_tuple) -> bool:
        """
        exp: __check_path_format('123.exe', 'exe', 'zip', 'rar')
        check path has:
            1. valid name
            2. expected suffix
        """
        if (i := path.rfind('.')) == -1:
            return False
        else:
            return True if path[i + 1:] in format_tuple and path[:i] else False

    @Slot()
    def __JIT_status_update(self):
        """
        Just-In-Time check and update widgets' status 
        """
        self.__update_out_format()
        self.__required_valid() if self.__check_required() else self.__required_invalid()

    def __required_valid(self):
        self.ui.checkBox_merged.setEnabled(True)
        self.ui.checkBox_xlsx.setEnabled(True)
        self.ui.pushButton.setEnabled(True)

        if self.ui.checkBox_merged.isChecked():
            pass
        else:
            tgt_hex_s19 = self.ui.lineEdit_tgt_hex_s19.text()
            merged_path = tgt_hex_s19[:tgt_hex_s19.rfind('.')] + '_MERGED.' + self.__out_format
            self.ui.lineEdit_merged.setText(merged_path)

        if self.ui.checkBox_xlsx.isChecked():
            pass
        else:
            tgt_hex_s19 = self.ui.lineEdit_tgt_hex_s19.text()
            xlsx_path = tgt_hex_s19[:tgt_hex_s19.rfind('.')] + '_MERGE_REPORT.xlsx'
            self.ui.lineEdit_xlsx.setText(xlsx_path)

    def __required_invalid(self):
        """
        options if required inputs invalid
        """
        self.ui.checkBox_merged.setEnabled(False)
        self.ui.checkBox_xlsx.setEnabled(False)
        self.ui.pushButton.setEnabled(False)
        self.ui.lineEdit_merged.clear()
        self.ui.lineEdit_xlsx.clear()

    def test_auto_fill(self):
        self.ui.lineEdit_src_a2l.setText('src.a2l')
        self.ui.lineEdit_src_hex_s19.setText('src.hex')
        self.ui.lineEdit_tgt_a2l.setText('tgt.a2l')
        self.ui.lineEdit_tgt_hex_s19.setText('tgt.s19')

    def __main_exec(self):
        # TODO: if all valid, execute
        """
        options when clicked main pushButton
        """
        pass

    def __check_optional(self):
        # TODO: do it
        """
        check all optional
        """
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
