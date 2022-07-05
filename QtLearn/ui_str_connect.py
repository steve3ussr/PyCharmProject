# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'str_connect.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(649, 399)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 60, 501, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_arg2 = QLabel(self.gridLayoutWidget)
        self.label_arg2.setObjectName(u"label_arg2")

        self.gridLayout.addWidget(self.label_arg2, 1, 0, 1, 1)

        self.label_arg1 = QLabel(self.gridLayoutWidget)
        self.label_arg1.setObjectName(u"label_arg1")

        self.gridLayout.addWidget(self.label_arg1, 0, 0, 1, 1)

        self.lineEdit_arg1 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_arg1.setObjectName(u"lineEdit_arg1")

        self.gridLayout.addWidget(self.lineEdit_arg1, 0, 1, 1, 1)

        self.lineEdit_arg2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_arg2.setObjectName(u"lineEdit_arg2")

        self.gridLayout.addWidget(self.lineEdit_arg2, 1, 1, 1, 1)

        self.button_str_connect = QPushButton(Form)
        self.button_str_connect.setObjectName(u"button_str_connect")
        self.button_str_connect.setGeometry(QRect(200, 280, 201, 71))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_arg2.setText(QCoreApplication.translate("Form", u"arg2", None))
        self.label_arg1.setText(QCoreApplication.translate("Form", u"arg1", None))
        self.button_str_connect.setText(QCoreApplication.translate("Form", u"str + str", None))
    # retranslateUi

