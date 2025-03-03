# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'juego.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMinimumSize(QSize(1200, 700))
        MainWindow.setMaximumSize(QSize(1200, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1200, 700))
        self.centralwidget.setMaximumSize(QSize(1200, 700))
        self.label_background = QLabel(self.centralwidget)
        self.label_background.setObjectName(u"label_background")
        self.label_background.setGeometry(QRect(0, 0, 1200, 700))
        self.label_background.setMinimumSize(QSize(1200, 700))
        self.label_background.setMaximumSize(QSize(1200, 700))
        self.label_background.setPixmap(QPixmap(u"resources/images/background/backgroundLogin.png"))
        self.label_background.setScaledContents(True)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(390, 220, 431, 251))
        font = QFont()
        font.setPointSize(26)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: rgba(255, 255, 255, 0.2); \n"
"    border: 2px solid white;  \n"
"    border-radius: 10px;  \n"
"    padding: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white; \n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgba(255, 255, 255, 0.8);\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4CAF50; \n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"")
        self.correo_label = QLabel(self.groupBox)
        self.correo_label.setObjectName(u"correo_label")
        self.correo_label.setGeometry(QRect(50, 40, 181, 16))
        font1 = QFont()
        font1.setBold(True)
        self.correo_label.setFont(font1)
        self.contrasena_label = QLabel(self.groupBox)
        self.contrasena_label.setObjectName(u"contrasena_label")
        self.contrasena_label.setGeometry(QRect(50, 110, 111, 16))
        self.input_correo = QLineEdit(self.groupBox)
        self.input_correo.setObjectName(u"input_correo")
        self.input_correo.setGeometry(QRect(50, 70, 331, 31))
        self.input_contrasena = QLineEdit(self.groupBox)
        self.input_contrasena.setObjectName(u"input_contrasena")
        self.input_contrasena.setGeometry(QRect(50, 140, 331, 31))
        self.button_login = QPushButton(self.groupBox)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(170, 190, 75, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_background.setText("")
        self.groupBox.setTitle("")
        self.correo_label.setText(QCoreApplication.translate("MainWindow", u"Correo Electronico", None))
        self.contrasena_label.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.button_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

