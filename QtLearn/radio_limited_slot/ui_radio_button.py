# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'radio_button.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(357, 289)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 80, 211, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radio_button_py = QRadioButton(self.horizontalLayoutWidget)
        self.radio_button_py.setObjectName(u"radio_button_py")
        self.radio_button_py.setChecked(True)

        self.horizontalLayout.addWidget(self.radio_button_py)

        self.radio_button_md = QRadioButton(self.horizontalLayoutWidget)
        self.radio_button_md.setObjectName(u"radio_button_md")

        self.horizontalLayout.addWidget(self.radio_button_md)

        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(100, 160, 171, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 357, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radio_button_py.setText(QCoreApplication.translate("MainWindow", u".py", None))
        self.radio_button_md.setText(QCoreApplication.translate("MainWindow", u".md", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"click me", None))
    # retranslateUi

