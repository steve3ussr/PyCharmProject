from PySide6.QtCore import Slot, QTimer
from ui_merge_tool_demo import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__out_format = None
        self.__set_optional_internal_link()
        self.__set_toolButtons()
        self.__set_timer()  # very important!

        self.test_auto_fill()
        self.ui.pushButton.clicked.connect(self._main_exec)

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

    def __set_toolButtons(self) -> None:
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

        self.__save_file(self.ui.toolButton_merged, self.ui.lineEdit_merged, self.__out_format)

    def __get_file(self, a_button, a_line, a_str) -> None:
        """
        just don't want to see many '.clicked.connect'
        select file, get file path
        """
        a_button.clicked.connect(self.__select_file(a_line, a_str))

    def __save_file(self, a_button, a_line, a_str) -> None:
        """
        just don't want to see many '.clicked.connect'
        select folder, get file path
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

        def select_folder_inner() -> None:
            folder_path = QFileDialog.getSaveFileName(QMainWindow(),
                                                      caption="保存文件",
                                                      dir=".",
                                                      filter=a_str)[0]  # 选择目录，返回选中的路径
            a_line.setText(folder_path)

        return select_folder_inner

    def __set_timer(self):
        """
        set a timer to check and update statuses
        """
        self.__timer = QTimer()
        self.__timer.start(50)
        self.__timer.timeout.connect(self.__JIT_status_update)

    def __JIT_status_update(self):
        """
        Just-In-Time check and update widgets' statuses
        VERY IMPORTANT
        """
        self.__update_out_format()

        if self.__check_input_validity():
            self.__output_status_update_valid()

            if self.__check_output_validity():
                self.ui.pushButton.setEnabled(True)
            else:
                self.ui.pushButton.setEnabled(False)

        else:
            self.__output_status_update_invalid()



    @staticmethod
    def __check_path(path, *format_tuple, existJudge=True) -> bool:
        # TODO: args opt
        """
        exp: __check_path_format('123.exe', 'exe', 'zip', 'rar', existJudge=False)
        check path has:
            1. valid name
            2. expected suffix
            3. file existence check
        """
        if (i := path.rfind('.')) == -1:
            return False
        else:
            temp = os.path.exists(path) if existJudge else True

            # debug
            # if

            return True if (path[i + 1:] in format_tuple) and path[:i] and temp else False

    def __update_out_format(self) -> None:
        """
        update:
            1. self.__out_format(.hex / .s19) according to REQUIRED radioButton
            2. merged file toolButton -> Dialog file filter
            3. merged file path
        """
        current_format = 'hex' if self.ui.radioButton_hex.isChecked() else 's19'
        if current_format != self.__out_format:

            # 1. reconnect toolButton
            self.ui.toolButton_merged.clicked.disconnect()
            temp_str = 'Intel (*.hex)' if current_format == 'hex' else 'Motorola32 (*.s19)'
            self.__save_file(self.ui.toolButton_merged, self.ui.lineEdit_merged, temp_str)

            # 2. replace suffix of path
            current_path = self.ui.lineEdit_merged.text()
            if self.__check_path(current_path, current_format, existJudge=False):
                pass
            elif self.__check_path(current_path, self.__out_format, existJudge=False):
                self.ui.lineEdit_merged.setText(current_path[:-3] + current_format)
            else:
                self.ui.lineEdit_merged.clear()

            # 3. switch internal status
            self.__out_format = current_format

        else:
            pass

    def __check_input_validity(self) -> bool:
        """
        check required(src and tgt; a2l, hex/s19):
            has valid path or not
            Accordingly switch status of OUTPUT, and executable
        """
        src_a2l_path = self.ui.lineEdit_src_a2l.text()
        src_hex_s19_path = self.ui.lineEdit_src_hex_s19.text()
        tgt_a2l_path = self.ui.lineEdit_tgt_a2l.text()
        tgt_hex_s19_path = self.ui.lineEdit_tgt_hex_s19.text()

        if self.__check_path(src_a2l_path, 'a2l') and \
                self.__check_path(src_hex_s19_path, 'hex', 's19') and \
                self.__check_path(tgt_a2l_path, 'a2l') and \
                self.__check_path(tgt_hex_s19_path, 'hex', 's19'):
            pass
        else:
            return False

        if self.ui.checkbox_dcm.isChecked():
            if self.__check_path(self.ui.lineEdit_dcm.text(), 'dcm', existJudge=True):
                return True
            elif self.ui.lineEdit_dcm.text().strip() == '':
                return True
            else:
                return False
        else:
            return True

    def __output_status_update_valid(self):
        """
        update output status if inputs valid
        """
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

        if self.ui.checkBox_merged.isChecked():
            self.ui.lineEdit_merged.setEnabled(True)
            self.ui.toolButton_merged.setEnabled(True)
        else:
            pass

        if self.ui.checkBox_xlsx.isChecked():
            self.ui.lineEdit_xlsx.setEnabled(True)
            self.ui.toolButton_xlsx.setEnabled(True)
        else:
            pass

    def __output_status_update_invalid(self):
        """
        update output status if inputs valid
        """
        self.ui.checkBox_merged.setEnabled(False)
        self.ui.checkBox_xlsx.setEnabled(False)
        self.ui.pushButton.setEnabled(False)
        # self.ui.lineEdit_merged.clear()
        # self.ui.lineEdit_xlsx.clear()
        self.ui.lineEdit_merged.setEnabled(False)
        self.ui.toolButton_merged.setEnabled(False)
        self.ui.lineEdit_xlsx.setEnabled(False)
        self.ui.toolButton_xlsx.setEnabled(False)

    def __check_output_validity(self):
        """
        check all output
        """
        if self.ui.checkBox_merged.isChecked():
            if self.__check_path(self.ui.lineEdit_merged.text(), self.__out_format, existJudge=False):
                pass
            else:
                return False
        else:
            pass

        if self.ui.checkBox_xlsx.isChecked():
            if self.__check_path(self.ui.lineEdit_xlsx.text(), 'xlsx', existJudge=False):
                pass
            else:
                return False
        else:
            pass

        return True

    def test_auto_fill(self):
        self.ui.lineEdit_src_a2l.setText('D:/src.a2l')
        self.ui.lineEdit_src_hex_s19.setText('D:/src.hex')
        self.ui.lineEdit_tgt_a2l.setText('D:/tgt.a2l')
        self.ui.lineEdit_tgt_hex_s19.setText('D:/tgt.s19')

    def _main_exec(self):
        # TODO: execute
        """
        options when clicked main pushButton
        """
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
