import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout, QLineEdit


class Adialog(QDialog):
    def __init__(self, parent=None):
        super(Adialog, self).__init__(parent)
        self.button = QPushButton('goto love')
        self.edit_zone = QLineEdit('the lucky one')
        self.setWindowTitle('loving U')

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.edit_zone)
        self.setLayout(layout)
        self.button.clicked.connect(self.loveing)

    @Slot()
    def loveing(self):
        print(f'Go and love yourself, {self.edit_zone.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a_dialog = Adialog()
    a_dialog.show()
    sys.exit(app.exec())
    # app.exec()


