# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_file_test.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(716, 533)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 430, 691, 61))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 701, 211))
        self.gridLayout_required = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_required.setObjectName(u"gridLayout_required")
        self.gridLayout_required.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_required.setHorizontalSpacing(15)
        self.gridLayout_required.setVerticalSpacing(6)
        self.gridLayout_required.setContentsMargins(0, 0, 0, 0)
        self.toolButton_tgt_a2l = QToolButton(self.gridLayoutWidget)
        self.toolButton_tgt_a2l.setObjectName(u"toolButton_tgt_a2l")

        self.gridLayout_required.addWidget(self.toolButton_tgt_a2l, 3, 2, 1, 1)

        self.lineEdit_tgt_a2l = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_tgt_a2l.setObjectName(u"lineEdit_tgt_a2l")

        self.gridLayout_required.addWidget(self.lineEdit_tgt_a2l, 3, 1, 1, 1)

        self.lineEdit_src_hex_s19 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_src_hex_s19.setObjectName(u"lineEdit_src_hex_s19")

        self.gridLayout_required.addWidget(self.lineEdit_src_hex_s19, 2, 1, 1, 1)

        self.label_tgt_hex_s19 = QLabel(self.gridLayoutWidget)
        self.label_tgt_hex_s19.setObjectName(u"label_tgt_hex_s19")

        self.gridLayout_required.addWidget(self.label_tgt_hex_s19, 4, 0, 1, 1)

        self.label_res_format = QLabel(self.gridLayoutWidget)
        self.label_res_format.setObjectName(u"label_res_format")

        self.gridLayout_required.addWidget(self.label_res_format, 6, 0, 1, 1)

        self.label_src_a2l = QLabel(self.gridLayoutWidget)
        self.label_src_a2l.setObjectName(u"label_src_a2l")

        self.gridLayout_required.addWidget(self.label_src_a2l, 1, 0, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_required.addWidget(self.line_3, 5, 2, 1, 1)

        self.label_tgt_a2l = QLabel(self.gridLayoutWidget)
        self.label_tgt_a2l.setObjectName(u"label_tgt_a2l")

        self.gridLayout_required.addWidget(self.label_tgt_a2l, 3, 0, 1, 1)

        self.lineEdit_tgt_hex_s19 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_tgt_hex_s19.setObjectName(u"lineEdit_tgt_hex_s19")

        self.gridLayout_required.addWidget(self.lineEdit_tgt_hex_s19, 4, 1, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_required.addWidget(self.line_2, 5, 0, 1, 1)

        self.toolButton_src_a2l = QToolButton(self.gridLayoutWidget)
        self.toolButton_src_a2l.setObjectName(u"toolButton_src_a2l")

        self.gridLayout_required.addWidget(self.toolButton_src_a2l, 1, 2, 1, 1)

        self.toolButton_src_hex_s19 = QToolButton(self.gridLayoutWidget)
        self.toolButton_src_hex_s19.setObjectName(u"toolButton_src_hex_s19")

        self.gridLayout_required.addWidget(self.toolButton_src_hex_s19, 2, 2, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_required.addWidget(self.line, 5, 1, 1, 1)

        self.label_src_hex_s19 = QLabel(self.gridLayoutWidget)
        self.label_src_hex_s19.setObjectName(u"label_src_hex_s19")
        self.label_src_hex_s19.setEnabled(True)

        self.gridLayout_required.addWidget(self.label_src_hex_s19, 2, 0, 1, 1)

        self.lineEdit_src_a2l = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_src_a2l.setObjectName(u"lineEdit_src_a2l")

        self.gridLayout_required.addWidget(self.lineEdit_src_a2l, 1, 1, 1, 1)

        self.toolButton_tgt_hex_s19 = QToolButton(self.gridLayoutWidget)
        self.toolButton_tgt_hex_s19.setObjectName(u"toolButton_tgt_hex_s19")

        self.gridLayout_required.addWidget(self.toolButton_tgt_hex_s19, 4, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.label_6.setTextFormat(Qt.RichText)

        self.gridLayout_required.addWidget(self.label_6, 0, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_hex = QRadioButton(self.gridLayoutWidget)
        self.radioButton_hex.setObjectName(u"radioButton_hex")
        self.radioButton_hex.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_hex.setAutoFillBackground(True)
        self.radioButton_hex.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_hex)

        self.radioButton_s19 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_s19.setObjectName(u"radioButton_s19")

        self.horizontalLayout.addWidget(self.radioButton_s19)

        self.horizontalSpacer = QSpacerItem(31, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_required.addLayout(self.horizontalLayout, 6, 1, 1, 1)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(0, 240, 741, 16))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 260, 701, 151))
        self.gridLayout_optional = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_optional.setObjectName(u"gridLayout_optional")
        self.gridLayout_optional.setHorizontalSpacing(15)
        self.gridLayout_optional.setContentsMargins(0, 0, 0, 0)
        self.checkbox_dcm = QCheckBox(self.gridLayoutWidget_2)
        self.checkbox_dcm.setObjectName(u"checkbox_dcm")

        self.gridLayout_optional.addWidget(self.checkbox_dcm, 1, 0, 1, 1)

        self.checkBox_merged = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_merged.setObjectName(u"checkBox_merged")

        self.gridLayout_optional.addWidget(self.checkBox_merged, 3, 0, 1, 1)

        self.checkBox_xlsx = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_xlsx.setObjectName(u"checkBox_xlsx")

        self.gridLayout_optional.addWidget(self.checkBox_xlsx, 2, 0, 1, 1)

        self.lineEdit_merged = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_merged.setObjectName(u"lineEdit_merged")
        self.lineEdit_merged.setEnabled(False)

        self.gridLayout_optional.addWidget(self.lineEdit_merged, 3, 1, 1, 1)

        self.toolButton_dcm = QToolButton(self.gridLayoutWidget_2)
        self.toolButton_dcm.setObjectName(u"toolButton_dcm")
        self.toolButton_dcm.setEnabled(False)

        self.gridLayout_optional.addWidget(self.toolButton_dcm, 1, 2, 1, 1)

        self.lineEdit_dcm = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_dcm.setObjectName(u"lineEdit_dcm")
        self.lineEdit_dcm.setEnabled(False)

        self.gridLayout_optional.addWidget(self.lineEdit_dcm, 1, 1, 1, 1)

        self.lineEdit_xlsx = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_xlsx.setObjectName(u"lineEdit_xlsx")
        self.lineEdit_xlsx.setEnabled(False)

        self.gridLayout_optional.addWidget(self.lineEdit_xlsx, 2, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setTextFormat(Qt.RichText)

        self.gridLayout_optional.addWidget(self.label_7, 0, 0, 1, 1)

        self.toolButton_xlsx = QToolButton(self.gridLayoutWidget_2)
        self.toolButton_xlsx.setObjectName(u"toolButton_xlsx")
        self.toolButton_xlsx.setEnabled(False)

        self.gridLayout_optional.addWidget(self.toolButton_xlsx, 2, 2, 1, 1)

        self.toolButton_merged = QToolButton(self.gridLayoutWidget_2)
        self.toolButton_merged.setObjectName(u"toolButton_merged")
        self.toolButton_merged.setEnabled(False)

        self.gridLayout_optional.addWidget(self.toolButton_merged, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 716, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.checkbox_dcm.clicked["bool"].connect(self.lineEdit_dcm.setEnabled)
        self.checkbox_dcm.clicked["bool"].connect(self.toolButton_dcm.setEnabled)
        self.checkBox_xlsx.clicked["bool"].connect(self.lineEdit_xlsx.setEnabled)
        self.checkBox_xlsx.clicked["bool"].connect(self.toolButton_xlsx.setEnabled)
        self.checkBox_merged.clicked["bool"].connect(self.lineEdit_merged.setEnabled)
        self.checkBox_merged.clicked["bool"].connect(self.toolButton_merged.setEnabled)
        self.checkbox_dcm.clicked["bool"].connect(self.lineEdit_dcm.clear)
        self.checkBox_xlsx.clicked["bool"].connect(self.lineEdit_xlsx.clear)
        self.checkBox_merged.clicked["bool"].connect(self.lineEdit_merged.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"calibration merge tool@steve.zhao", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"CLICK ME!", None))
        self.toolButton_tgt_a2l.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_tgt_hex_s19.setText(QCoreApplication.translate("MainWindow", u"target hex / s19", None))
        self.label_res_format.setText(QCoreApplication.translate("MainWindow", u"result format", None))
        self.label_src_a2l.setText(QCoreApplication.translate("MainWindow", u"source a2l", None))
        self.label_tgt_a2l.setText(QCoreApplication.translate("MainWindow", u"target a2l", None))
        self.toolButton_src_a2l.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_src_hex_s19.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_src_hex_s19.setText(QCoreApplication.translate("MainWindow", u"source hex / s19", None))
        self.toolButton_tgt_hex_s19.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"REQUIRED: ", None))
        self.radioButton_hex.setText(QCoreApplication.translate("MainWindow", u".hex", None))
        self.radioButton_s19.setText(QCoreApplication.translate("MainWindow", u".s19", None))
        self.checkbox_dcm.setText(QCoreApplication.translate("MainWindow", u".dcm", None))
        self.checkBox_merged.setText(QCoreApplication.translate("MainWindow", u"specify merged file", None))
        self.checkBox_xlsx.setText(QCoreApplication.translate("MainWindow", u"specify .xlsx", None))
        self.toolButton_dcm.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"*OPTIONAL: ", None))
        self.toolButton_xlsx.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_merged.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

