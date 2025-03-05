# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'juego.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

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
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(0, 10, 1191, 671))
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"    background: transparent;\n"
"}")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.groupBox_login = QGroupBox(self.login)
        self.groupBox_login.setObjectName(u"groupBox_login")
        self.groupBox_login.setGeometry(QRect(380, 210, 431, 281))
        font = QFont()
        font.setPointSize(26)
        self.groupBox_login.setFont(font)
        self.groupBox_login.setStyleSheet(u"QGroupBox {\n"
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
        self.correo_label = QLabel(self.groupBox_login)
        self.correo_label.setObjectName(u"correo_label")
        self.correo_label.setGeometry(QRect(50, 40, 181, 16))
        font1 = QFont()
        font1.setBold(True)
        self.correo_label.setFont(font1)
        self.contrasena_label = QLabel(self.groupBox_login)
        self.contrasena_label.setObjectName(u"contrasena_label")
        self.contrasena_label.setGeometry(QRect(50, 110, 111, 16))
        self.input_correo = QLineEdit(self.groupBox_login)
        self.input_correo.setObjectName(u"input_correo")
        self.input_correo.setGeometry(QRect(50, 70, 331, 31))
        self.input_contrasena = QLineEdit(self.groupBox_login)
        self.input_contrasena.setObjectName(u"input_contrasena")
        self.input_contrasena.setGeometry(QRect(50, 140, 331, 31))
        self.button_login = QPushButton(self.groupBox_login)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(170, 190, 75, 31))
        self.registro_enlace = QLabel(self.groupBox_login)
        self.registro_enlace.setObjectName(u"registro_enlace")
        self.registro_enlace.setGeometry(QRect(80, 230, 271, 20))
        self.registro_enlace.setStyleSheet(u"QLabel {\n"
"    color: blue;\n"
"    text-decoration: underline;\n"
"    cursor: pointer;\n"
"}")
        self.stackedWidget.addWidget(self.login)
        self.register_2 = QWidget()
        self.register_2.setObjectName(u"register_2")
        self.register_2.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.groupBox_register = QGroupBox(self.register_2)
        self.groupBox_register.setObjectName(u"groupBox_register")
        self.groupBox_register.setGeometry(QRect(380, 170, 431, 341))
        font2 = QFont()
        font2.setPointSize(1)
        self.groupBox_register.setFont(font2)
        self.groupBox_register.setStyleSheet(u"QGroupBox {\n"
"    background-color: rgba(255, 255, 255, 0.2); \n"
"    border: 2px solid white;  \n"
"    border-radius: 10px;  \n"
"    padding: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white; \n"
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
        self.correo_label_2 = QLabel(self.groupBox_register)
        self.correo_label_2.setObjectName(u"correo_label_2")
        self.correo_label_2.setGeometry(QRect(50, 40, 181, 16))
        self.correo_label_2.setFont(font1)
        self.contrasena_label_2 = QLabel(self.groupBox_register)
        self.contrasena_label_2.setObjectName(u"contrasena_label_2")
        self.contrasena_label_2.setGeometry(QRect(50, 110, 111, 16))
        self.input_correo_2 = QLineEdit(self.groupBox_register)
        self.input_correo_2.setObjectName(u"input_correo_2")
        self.input_correo_2.setGeometry(QRect(50, 70, 331, 31))
        self.input_contrasena_2 = QLineEdit(self.groupBox_register)
        self.input_contrasena_2.setObjectName(u"input_contrasena_2")
        self.input_contrasena_2.setGeometry(QRect(50, 140, 331, 31))
        self.button_register = QPushButton(self.groupBox_register)
        self.button_register.setObjectName(u"button_register")
        self.button_register.setGeometry(QRect(170, 250, 75, 31))
        self.login_enlace = QLabel(self.groupBox_register)
        self.login_enlace.setObjectName(u"login_enlace")
        self.login_enlace.setGeometry(QRect(110, 290, 211, 20))
        self.login_enlace.setStyleSheet(u"QLabel {\n"
"    color: blue;\n"
"    text-decoration: underline;\n"
"    cursor: pointer;\n"
"}")
        self.contrasena_label_3 = QLabel(self.groupBox_register)
        self.contrasena_label_3.setObjectName(u"contrasena_label_3")
        self.contrasena_label_3.setGeometry(QRect(50, 180, 161, 16))
        self.input_repeatContra = QLineEdit(self.groupBox_register)
        self.input_repeatContra.setObjectName(u"input_repeatContra")
        self.input_repeatContra.setGeometry(QRect(50, 210, 331, 31))
        self.stackedWidget.addWidget(self.register_2)
        self.Juego = QWidget()
        self.Juego.setObjectName(u"Juego")
        self.Juego.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.label = QLabel(self.Juego)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 30, 811, 111))
        self.label.setStyleSheet(u"QLabel {\n"
"    background: white;\n"
"}")
        self.label_2 = QLabel(self.Juego)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 70, 101, 111))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background: white;\n"
"}")
        self.lineEdit = QLineEdit(self.Juego)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 590, 721, 51))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background: white;\n"
"}")
        self.pushButton = QPushButton(self.Juego)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1030, 600, 75, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"}")
        self.stackedWidget.addWidget(self.Juego)
        self.principalUsuario = QWidget()
        self.principalUsuario.setObjectName(u"principalUsuario")
        self.principalUsuario.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.buttonFacil = QPushButton(self.principalUsuario)
        self.buttonFacil.setObjectName(u"buttonFacil")
        self.buttonFacil.setGeometry(QRect(520, 200, 151, 41))
        self.buttonNormal = QPushButton(self.principalUsuario)
        self.buttonNormal.setObjectName(u"buttonNormal")
        self.buttonNormal.setGeometry(QRect(520, 260, 151, 41))
        self.buttonDificil = QPushButton(self.principalUsuario)
        self.buttonDificil.setObjectName(u"buttonDificil")
        self.buttonDificil.setGeometry(QRect(520, 320, 151, 41))
        self.stackedWidget.addWidget(self.principalUsuario)
        self.principalAdmin = QWidget()
        self.principalAdmin.setObjectName(u"principalAdmin")
        self.principalAdmin.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.buttonFacilAdmin = QPushButton(self.principalAdmin)
        self.buttonFacilAdmin.setObjectName(u"buttonFacilAdmin")
        self.buttonFacilAdmin.setGeometry(QRect(520, 200, 151, 41))
        self.buttonNormalAdmin = QPushButton(self.principalAdmin)
        self.buttonNormalAdmin.setObjectName(u"buttonNormalAdmin")
        self.buttonNormalAdmin.setGeometry(QRect(520, 260, 151, 41))
        self.buttonDificilAdmin = QPushButton(self.principalAdmin)
        self.buttonDificilAdmin.setObjectName(u"buttonDificilAdmin")
        self.buttonDificilAdmin.setGeometry(QRect(520, 320, 151, 41))
        self.buttonGestion = QPushButton(self.principalAdmin)
        self.buttonGestion.setObjectName(u"buttonGestion")
        self.buttonGestion.setGeometry(QRect(520, 380, 151, 41))
        self.stackedWidget.addWidget(self.principalAdmin)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_background.setText("")
        self.groupBox_login.setTitle("")
        self.correo_label.setText(QCoreApplication.translate("MainWindow", u"Correo Electronico", None))
        self.contrasena_label.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.button_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.registro_enlace.setText(QCoreApplication.translate("MainWindow", u"\u00bfNo tienes una cuenta? Reg\u00edstrate aqu\u00ed", None))
        self.groupBox_register.setTitle("")
        self.correo_label_2.setText(QCoreApplication.translate("MainWindow", u"Correo Electronico", None))
        self.contrasena_label_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.button_register.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.login_enlace.setText(QCoreApplication.translate("MainWindow", u"\u00bfYa tienes cuenta? Inicia sesion", None))
        self.contrasena_label_3.setText(QCoreApplication.translate("MainWindow", u"Repite contrase\u00f1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pregunta", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Foto", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Respuesta", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.buttonFacil.setText(QCoreApplication.translate("MainWindow", u"F\u00e1cil", None))
        self.buttonNormal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.buttonDificil.setText(QCoreApplication.translate("MainWindow", u"Dif\u00edcil", None))
        self.buttonFacilAdmin.setText(QCoreApplication.translate("MainWindow", u"F\u00e1cil", None))
        self.buttonNormalAdmin.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.buttonDificilAdmin.setText(QCoreApplication.translate("MainWindow", u"Dif\u00edcil", None))
        self.buttonGestion.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n", None))
    # retranslateUi

