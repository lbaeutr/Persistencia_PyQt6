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
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTextEdit, QWidget)

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
        self.label_background.setPixmap(QPixmap(u"resources/images/background/Wave.png"))
        self.label_background.setScaledContents(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(0, 10, 1191, 671))
        self.stackedWidget.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.groupBox_login = QGroupBox(self.login)
        self.groupBox_login.setObjectName(u"groupBox_login")
        self.groupBox_login.setGeometry(QRect(380, 310, 431, 281))
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
        self.correo_label.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.contrasena_label = QLabel(self.groupBox_login)
        self.contrasena_label.setObjectName(u"contrasena_label")
        self.contrasena_label.setGeometry(QRect(50, 110, 111, 16))
        self.contrasena_label.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.input_correo = QLineEdit(self.groupBox_login)
        self.input_correo.setObjectName(u"input_correo")
        self.input_correo.setGeometry(QRect(50, 70, 331, 31))
        self.input_contrasena = QLineEdit(self.groupBox_login)
        self.input_contrasena.setObjectName(u"input_contrasena")
        self.input_contrasena.setGeometry(QRect(50, 140, 331, 31))
        self.button_login = QPushButton(self.groupBox_login)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(170, 190, 75, 31))
        self.button_login.setStyleSheet(u"QPushButton {\n"
"    background: #7CFC00;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #6BBE00;\n"
"    color: black;\n"
"}")
        self.registro_enlace = QLabel(self.groupBox_login)
        self.registro_enlace.setObjectName(u"registro_enlace")
        self.registro_enlace.setGeometry(QRect(80, 230, 271, 20))
        self.registro_enlace.setStyleSheet(u"QLabel {\n"
"    color: blue;\n"
"    text-decoration: underline;\n"
"    cursor: pointer;\n"
"}")
        self.logo_4 = QLabel(self.login)
        self.logo_4.setObjectName(u"logo_4")
        self.logo_4.setGeometry(QRect(498, 100, 181, 181))
        self.logo_4.setPixmap(QPixmap(u"resources/images/background/Logo.png"))
        self.logo_4.setScaledContents(True)
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
        self.correo_label_2.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.contrasena_label_2 = QLabel(self.groupBox_register)
        self.contrasena_label_2.setObjectName(u"contrasena_label_2")
        self.contrasena_label_2.setGeometry(QRect(50, 110, 111, 16))
        self.contrasena_label_2.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.input_correo_2 = QLineEdit(self.groupBox_register)
        self.input_correo_2.setObjectName(u"input_correo_2")
        self.input_correo_2.setGeometry(QRect(50, 70, 331, 31))
        self.input_contrasena_2 = QLineEdit(self.groupBox_register)
        self.input_contrasena_2.setObjectName(u"input_contrasena_2")
        self.input_contrasena_2.setGeometry(QRect(50, 140, 331, 31))
        self.button_register = QPushButton(self.groupBox_register)
        self.button_register.setObjectName(u"button_register")
        self.button_register.setGeometry(QRect(170, 250, 75, 31))
        self.button_register.setStyleSheet(u"QPushButton {\n"
"    background: #7CFC00;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #6BBE00;\n"
"    color: black;\n"
"}")
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
        self.contrasena_label_3.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.input_repeatContra = QLineEdit(self.groupBox_register)
        self.input_repeatContra.setObjectName(u"input_repeatContra")
        self.input_repeatContra.setGeometry(QRect(50, 210, 331, 31))
        self.stackedWidget.addWidget(self.register_2)
        self.gestion = QWidget()
        self.gestion.setObjectName(u"gestion")
        self.gestion.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.crearPregunta = QPushButton(self.gestion)
        self.crearPregunta.setObjectName(u"crearPregunta")
        self.crearPregunta.setGeometry(QRect(500, 320, 181, 31))
        self.crearPregunta.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.eliminarPregunta = QPushButton(self.gestion)
        self.eliminarPregunta.setObjectName(u"eliminarPregunta")
        self.eliminarPregunta.setGeometry(QRect(500, 370, 181, 31))
        self.eliminarPregunta.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.actualizarPregunta = QPushButton(self.gestion)
        self.actualizarPregunta.setObjectName(u"actualizarPregunta")
        self.actualizarPregunta.setGeometry(QRect(500, 420, 181, 31))
        self.actualizarPregunta.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.listarPreguntas = QPushButton(self.gestion)
        self.listarPreguntas.setObjectName(u"listarPreguntas")
        self.listarPreguntas.setGeometry(QRect(500, 470, 181, 31))
        self.listarPreguntas.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.logo = QLabel(self.gestion)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(498, 100, 181, 181))
        self.logo.setPixmap(QPixmap(u"resources/images/background/Logo.png"))
        self.logo.setScaledContents(True)
        self.stackedWidget.addWidget(self.gestion)
        self.ActualizarScreen = QWidget()
        self.ActualizarScreen.setObjectName(u"ActualizarScreen")
        self.groupBox_login_4 = QGroupBox(self.ActualizarScreen)
        self.groupBox_login_4.setObjectName(u"groupBox_login_4")
        self.groupBox_login_4.setGeometry(QRect(390, 60, 431, 501))
        self.groupBox_login_4.setFont(font)
        self.groupBox_login_4.setStyleSheet(u"QGroupBox {\n"
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
        self.pregunta_label_2 = QLabel(self.groupBox_login_4)
        self.pregunta_label_2.setObjectName(u"pregunta_label_2")
        self.pregunta_label_2.setGeometry(QRect(60, 120, 181, 16))
        self.pregunta_label_2.setFont(font1)
        self.pregunta_label_2.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.respuestaLabel_3 = QLabel(self.groupBox_login_4)
        self.respuestaLabel_3.setObjectName(u"respuestaLabel_3")
        self.respuestaLabel_3.setGeometry(QRect(60, 360, 111, 16))
        self.respuestaLabel_3.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.inputRespuesta_3 = QLineEdit(self.groupBox_login_4)
        self.inputRespuesta_3.setObjectName(u"inputRespuesta_3")
        self.inputRespuesta_3.setGeometry(QRect(50, 390, 331, 31))
        self.inputRespuesta_3.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background: white;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.buttonActualizar = QPushButton(self.groupBox_login_4)
        self.buttonActualizar.setObjectName(u"buttonActualizar")
        self.buttonActualizar.setGeometry(QRect(170, 450, 75, 31))
        self.buttonActualizar.setStyleSheet(u"QPushButton {\n"
"    background: #7CFC00;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #6BBE00;\n"
"    color: black;\n"
"}")
        self.inputPregunta = QTextEdit(self.groupBox_login_4)
        self.inputPregunta.setObjectName(u"inputPregunta")
        self.inputPregunta.setGeometry(QRect(50, 150, 331, 181))
        self.inputPregunta.setStyleSheet(u"QTextEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background: white;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.IdLabel_4 = QLabel(self.groupBox_login_4)
        self.IdLabel_4.setObjectName(u"IdLabel_4")
        self.IdLabel_4.setGeometry(QRect(60, 30, 111, 16))
        self.IdLabel_4.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.inputId = QLineEdit(self.groupBox_login_4)
        self.inputId.setObjectName(u"inputId")
        self.inputId.setGeometry(QRect(50, 60, 331, 31))
        self.inputId.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background: white;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.ActualizarScreen)
        self.Juego = QWidget()
        self.Juego.setObjectName(u"Juego")
        self.Juego.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.pregunta = QLabel(self.Juego)
        self.pregunta.setObjectName(u"pregunta")
        self.pregunta.setGeometry(QRect(280, 30, 811, 111))
        self.pregunta.setStyleSheet(u"QLabel {\n"
"    background: white;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"")
        self.foto = QLabel(self.Juego)
        self.foto.setObjectName(u"foto")
        self.foto.setGeometry(QRect(150, 100, 111, 111))
        self.foto.setStyleSheet(u"QLabel {\n"
"    background: white;\n"
"}")
        self.foto.setPixmap(QPixmap(u"resources/images/background/Imagen de WhatsApp 2025-03-05 a las 17.53.39_336876c6.jpg"))
        self.foto.setScaledContents(True)
        self.respuesta = QLineEdit(self.Juego)
        self.respuesta.setObjectName(u"respuesta")
        self.respuesta.setGeometry(QRect(280, 590, 721, 51))
        self.respuesta.setStyleSheet(u"QLineEdit {\n"
"    background: white;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"")
        self.enviar = QPushButton(self.Juego)
        self.enviar.setObjectName(u"enviar")
        self.enviar.setGeometry(QRect(1030, 600, 75, 31))
        self.enviar.setStyleSheet(u"QPushButton {\n"
"    background: #7CFC00;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    border: 1px solid #6BBE00;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.stackedWidget.addWidget(self.Juego)
        self.ListarScreen = QWidget()
        self.ListarScreen.setObjectName(u"ListarScreen")
        self.groupBox_login_5 = QGroupBox(self.ListarScreen)
        self.groupBox_login_5.setObjectName(u"groupBox_login_5")
        self.groupBox_login_5.setGeometry(QRect(190, 30, 851, 631))
        self.groupBox_login_5.setFont(font)
        self.groupBox_login_5.setStyleSheet(u"QGroupBox {\n"
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
        self.buttonVolver = QPushButton(self.groupBox_login_5)
        self.buttonVolver.setObjectName(u"buttonVolver")
        self.buttonVolver.setGeometry(QRect(390, 580, 75, 31))
        self.buttonVolver.setStyleSheet(u"QPushButton {\n"
"    background: #7CFC00;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #6BBE00;\n"
"    color: black;\n"
"}")
        self.listarLabel = QLabel(self.groupBox_login_5)
        self.listarLabel.setObjectName(u"listarLabel")
        self.listarLabel.setGeometry(QRect(50, 30, 751, 531))
        self.listarLabel.setStyleSheet(u"QLabel {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background: white;\n"
"    font-size: 14px;\n"
"}")
        self.stackedWidget.addWidget(self.ListarScreen)
        self.CrearScreen = QWidget()
        self.CrearScreen.setObjectName(u"CrearScreen")
        self.groupBox_login_2 = QGroupBox(self.CrearScreen)
        self.groupBox_login_2.setObjectName(u"groupBox_login_2")
        self.groupBox_login_2.setGeometry(QRect(390, 100, 431, 481))
        self.groupBox_login_2.setFont(font)
        self.groupBox_login_2.setStyleSheet(u"QGroupBox {\n"
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
        self.preguinta_label = QLabel(self.groupBox_login_2)
        self.preguinta_label.setObjectName(u"preguinta_label")
        self.preguinta_label.setGeometry(QRect(50, 40, 181, 16))
        self.preguinta_label.setFont(font1)
        self.preguinta_label.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.respuestaLabel = QLabel(self.groupBox_login_2)
        self.respuestaLabel.setObjectName(u"respuestaLabel")
        self.respuestaLabel.setGeometry(QRect(50, 310, 111, 16))
        self.respuestaLabel.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.inputRespuesta = QLineEdit(self.groupBox_login_2)
        self.inputRespuesta.setObjectName(u"inputRespuesta")
        self.inputRespuesta.setGeometry(QRect(50, 340, 331, 31))
        self.inputRespuesta.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background: white;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.buttonEnviar = QPushButton(self.groupBox_login_2)
        self.buttonEnviar.setObjectName(u"buttonEnviar")
        self.buttonEnviar.setGeometry(QRect(180, 410, 75, 31))
        self.buttonEnviar.setStyleSheet(u"QPushButton {\n"
"    background: #7CFC00;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #6BBE00;\n"
"    color: black;\n"
"}")
        self.inputPregunta_2 = QTextEdit(self.groupBox_login_2)
        self.inputPregunta_2.setObjectName(u"inputPregunta_2")
        self.inputPregunta_2.setGeometry(QRect(50, 80, 331, 181))
        self.inputPregunta_2.setStyleSheet(u"QTextEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background: white;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.CrearScreen)
        self.EliminarScreen = QWidget()
        self.EliminarScreen.setObjectName(u"EliminarScreen")
        self.groupBox_login_3 = QGroupBox(self.EliminarScreen)
        self.groupBox_login_3.setObjectName(u"groupBox_login_3")
        self.groupBox_login_3.setGeometry(QRect(390, 100, 390, 151))
        self.groupBox_login_3.setFont(font)
        self.groupBox_login_3.setStyleSheet(u"QGroupBox {\n"
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
        self.idLabel = QLabel(self.groupBox_login_3)
        self.idLabel.setObjectName(u"idLabel")
        self.idLabel.setGeometry(QRect(40, 20, 111, 16))
        self.idLabel.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.inputId_2 = QLineEdit(self.groupBox_login_3)
        self.inputId_2.setObjectName(u"inputId_2")
        self.inputId_2.setGeometry(QRect(40, 50, 331, 31))
        self.inputId_2.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background: white;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.buttonEliminar = QPushButton(self.groupBox_login_3)
        self.buttonEliminar.setObjectName(u"buttonEliminar")
        self.buttonEliminar.setGeometry(QRect(160, 100, 75, 31))
        self.buttonEliminar.setStyleSheet(u"QPushButton {\n"
"    background: #CD5C5C;\n"
"    border-radius: 10px;\n"
"    color: black;\n"
"}")
        self.stackedWidget.addWidget(self.EliminarScreen)
        self.principalUsuario = QWidget()
        self.principalUsuario.setObjectName(u"principalUsuario")
        self.principalUsuario.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.buttonFacil = QPushButton(self.principalUsuario)
        self.buttonFacil.setObjectName(u"buttonFacil")
        self.buttonFacil.setGeometry(QRect(500, 320, 181, 31))
        self.buttonFacil.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.buttonNormal = QPushButton(self.principalUsuario)
        self.buttonNormal.setObjectName(u"buttonNormal")
        self.buttonNormal.setGeometry(QRect(500, 370, 181, 31))
        self.buttonNormal.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.buttonDificil = QPushButton(self.principalUsuario)
        self.buttonDificil.setObjectName(u"buttonDificil")
        self.buttonDificil.setGeometry(QRect(500, 420, 181, 31))
        self.buttonDificil.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.logo_3 = QLabel(self.principalUsuario)
        self.logo_3.setObjectName(u"logo_3")
        self.logo_3.setGeometry(QRect(498, 100, 181, 181))
        self.logo_3.setPixmap(QPixmap(u"resources/images/background/Logo.png"))
        self.logo_3.setScaledContents(True)
        self.stackedWidget.addWidget(self.principalUsuario)
        self.principalAdmin = QWidget()
        self.principalAdmin.setObjectName(u"principalAdmin")
        self.principalAdmin.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.buttonFacilAdmin = QPushButton(self.principalAdmin)
        self.buttonFacilAdmin.setObjectName(u"buttonFacilAdmin")
        self.buttonFacilAdmin.setGeometry(QRect(500, 320, 181, 31))
        self.buttonFacilAdmin.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.buttonNormalAdmin = QPushButton(self.principalAdmin)
        self.buttonNormalAdmin.setObjectName(u"buttonNormalAdmin")
        self.buttonNormalAdmin.setGeometry(QRect(500, 370, 181, 31))
        self.buttonNormalAdmin.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.buttonDificilAdmin = QPushButton(self.principalAdmin)
        self.buttonDificilAdmin.setObjectName(u"buttonDificilAdmin")
        self.buttonDificilAdmin.setGeometry(QRect(500, 420, 181, 31))
        self.buttonDificilAdmin.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.buttonGestion = QPushButton(self.principalAdmin)
        self.buttonGestion.setObjectName(u"buttonGestion")
        self.buttonGestion.setGeometry(QRect(500, 470, 181, 31))
        self.buttonGestion.setStyleSheet(u"QPushButton {\n"
"    background: white;\n"
"    border-radius: 10px;\n"
"    border: 1px;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.logo_2 = QLabel(self.principalAdmin)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(498, 100, 181, 181))
        self.logo_2.setPixmap(QPixmap(u"resources/images/background/Logo.png"))
        self.logo_2.setScaledContents(True)
        self.stackedWidget.addWidget(self.principalAdmin)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


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
        self.logo_4.setText("")
        self.groupBox_register.setTitle("")
        self.correo_label_2.setText(QCoreApplication.translate("MainWindow", u"Correo Electronico", None))
        self.contrasena_label_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.button_register.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.login_enlace.setText(QCoreApplication.translate("MainWindow", u"\u00bfYa tienes cuenta? Inicia sesion", None))
        self.contrasena_label_3.setText(QCoreApplication.translate("MainWindow", u"Repite contrase\u00f1a", None))
        self.crearPregunta.setText(QCoreApplication.translate("MainWindow", u"Crear Pregunta", None))
        self.eliminarPregunta.setText(QCoreApplication.translate("MainWindow", u"Eliminar Pregunta", None))
        self.actualizarPregunta.setText(QCoreApplication.translate("MainWindow", u"Actualizar Pregunta", None))
        self.listarPreguntas.setText(QCoreApplication.translate("MainWindow", u"Listar Preguntas", None))
        self.logo.setText("")
        self.groupBox_login_4.setTitle("")
        self.pregunta_label_2.setText(QCoreApplication.translate("MainWindow", u"Pregunta", None))
        self.respuestaLabel_3.setText(QCoreApplication.translate("MainWindow", u"Respuesta", None))
        self.buttonActualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.IdLabel_4.setText(QCoreApplication.translate("MainWindow", u"Id de la pregunta", None))
        self.pregunta.setText(QCoreApplication.translate("MainWindow", u"Pregunta", None))
        self.foto.setText("")
        self.respuesta.setText(QCoreApplication.translate("MainWindow", u"Respuesta", None))
        self.enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.groupBox_login_5.setTitle("")
        self.buttonVolver.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.listarLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_login_2.setTitle("")
        self.preguinta_label.setText(QCoreApplication.translate("MainWindow", u"Pregunta", None))
        self.respuestaLabel.setText(QCoreApplication.translate("MainWindow", u"Respuesta", None))
        self.buttonEnviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.groupBox_login_3.setTitle("")
        self.idLabel.setText(QCoreApplication.translate("MainWindow", u"Id de la pregunta", None))
        self.buttonEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.buttonFacil.setText(QCoreApplication.translate("MainWindow", u"F\u00e1cil", None))
        self.buttonNormal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.buttonDificil.setText(QCoreApplication.translate("MainWindow", u"Dif\u00edcil", None))
        self.logo_3.setText("")
        self.buttonFacilAdmin.setText(QCoreApplication.translate("MainWindow", u"F\u00e1cil", None))
        self.buttonNormalAdmin.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.buttonDificilAdmin.setText(QCoreApplication.translate("MainWindow", u"Dif\u00edcil", None))
        self.buttonGestion.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n", None))
        self.logo_2.setText("")
    # retranslateUi

