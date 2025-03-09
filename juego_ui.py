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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTextBrowser, QTextEdit, QWidget)

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
"    background: #a29bfe;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #716db2;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"	font-size: 11px;\n"
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
        self.groupBox_register.setGeometry(QRect(380, 255, 431, 341))
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
"    background: #a29bfe;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #716db2;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"	font-size: 11px;\n"
"}")
        self.login_enlace = QLabel(self.groupBox_register)
        self.login_enlace.setObjectName(u"login_enlace")
        self.login_enlace.setGeometry(QRect(120, 290, 211, 20))
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
        self.logo_5 = QLabel(self.register_2)
        self.logo_5.setObjectName(u"logo_5")
        self.logo_5.setGeometry(QRect(498, 55, 181, 181))
        self.logo_5.setPixmap(QPixmap(u"resources/images/background/Logo.png"))
        self.logo_5.setScaledContents(True)
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
        self.boton_volver_admin_4 = QPushButton(self.gestion)
        self.boton_volver_admin_4.setObjectName(u"boton_volver_admin_4")
        self.boton_volver_admin_4.setGeometry(QRect(20, 10, 75, 31))
        self.boton_volver_admin_4.setStyleSheet(u"QPushButton {\n"
"    background: #a29bfe;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    border: 1px solid #716db2;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.stackedWidget.addWidget(self.gestion)
        self.ActualizarScreen = QWidget()
        self.ActualizarScreen.setObjectName(u"ActualizarScreen")
        self.groupBox_login_4 = QGroupBox(self.ActualizarScreen)
        self.groupBox_login_4.setObjectName(u"groupBox_login_4")
        self.groupBox_login_4.setGeometry(QRect(390, 20, 431, 611))
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
        self.buttonActualizar.setGeometry(QRect(170, 550, 75, 31))
        self.buttonActualizar.setFont(font1)
        self.buttonActualizar.setStyleSheet(u"QPushButton {\n"
"    background: #74b9ff;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #578bbf;\n"
"    color: black;\n"
"	font-weight: bold;\n"
"	font-size: 11px;\n"
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
        self.IdLabel_4.setGeometry(QRect(60, 30, 121, 16))
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
        self.respuestaLabel_5 = QLabel(self.groupBox_login_4)
        self.respuestaLabel_5.setObjectName(u"respuestaLabel_5")
        self.respuestaLabel_5.setGeometry(QRect(60, 450, 111, 16))
        self.respuestaLabel_5.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.combo_respuestas_3 = QComboBox(self.groupBox_login_4)
        self.combo_respuestas_3.addItem("")
        self.combo_respuestas_3.addItem("")
        self.combo_respuestas_3.addItem("")
        self.combo_respuestas_3.setObjectName(u"combo_respuestas_3")
        self.combo_respuestas_3.setGeometry(QRect(50, 480, 81, 31))
        self.combo_respuestas_3.setStyleSheet(u"QComboBox {\n"
"    background: white;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"")
        self.boton_volver_admin = QPushButton(self.ActualizarScreen)
        self.boton_volver_admin.setObjectName(u"boton_volver_admin")
        self.boton_volver_admin.setGeometry(QRect(20, 10, 75, 31))
        self.boton_volver_admin.setStyleSheet(u"QPushButton {\n"
"    background: #a29bfe;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    border: 1px solid #716db2;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.stackedWidget.addWidget(self.ActualizarScreen)
        self.Juego = QWidget()
        self.Juego.setObjectName(u"Juego")
        self.Juego.setStyleSheet(u"QWidget {\n"
"    background: transparent;\n"
"}")
        self.pregunta = QLabel(self.Juego)
        self.pregunta.setObjectName(u"pregunta")
        self.pregunta.setGeometry(QRect(280, 30, 811, 111))
        font3 = QFont()
        font3.setPointSize(20)
        self.pregunta.setFont(font3)
        self.pregunta.setStyleSheet(u"QLabel {\n"
"    background: white;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"")
        self.foto = QLabel(self.Juego)
        self.foto.setObjectName(u"foto")
        self.foto.setGeometry(QRect(150, 30, 111, 111))
        self.foto.setStyleSheet(u"QLabel {\n"
"    background: white;\n"
"}")
        self.foto.setPixmap(QPixmap(u"resources/images/background/Imagen de WhatsApp 2025-03-05 a las 17.53.39_336876c6.jpg"))
        self.foto.setScaledContents(True)
        self.enviar = QPushButton(self.Juego)
        self.enviar.setObjectName(u"enviar")
        self.enviar.setGeometry(QRect(850, 550, 75, 31))
        self.enviar.setStyleSheet(u"QPushButton {\n"
"    background: #74b9ff;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #578bbf;\n"
"    color: black;\n"
"	font-weight: bold;\n"
"	font-size: 11px;\n"
"}")
        self.combo_respuestas = QComboBox(self.Juego)
        self.combo_respuestas.setObjectName(u"combo_respuestas")
        self.combo_respuestas.setEnabled(True)
        self.combo_respuestas.setGeometry(QRect(490, 520, 321, 91))
        self.combo_respuestas.setFont(font3)
        self.combo_respuestas.setStyleSheet(u"QComboBox {\n"
"    background: white;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"    image: none;\n"
"    width: 0px;\n"
"}\n"
"")
        self.boton_volver = QPushButton(self.Juego)
        self.boton_volver.setObjectName(u"boton_volver")
        self.boton_volver.setGeometry(QRect(20, 10, 75, 31))
        self.boton_volver.setStyleSheet(u"QPushButton {\n"
"    background: #a29bfe;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    border: 1px solid #716db2;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
        self.respuestaLabel_2 = QLabel(self.Juego)
        self.respuestaLabel_2.setObjectName(u"respuestaLabel_2")
        self.respuestaLabel_2.setGeometry(QRect(500, 490, 111, 16))
        self.respuestaLabel_2.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"	font-weight: bold;\n"
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
        self.buttonVolver.setFont(font1)
        self.buttonVolver.setMouseTracking(True)
        self.buttonVolver.setStyleSheet(u"QPushButton {\n"
"    background: #a29bfe;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #716db2;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"	font-size: 11px;\n"
"}")
        self.listarBrowser = QTextBrowser(self.groupBox_login_5)
        self.listarBrowser.setObjectName(u"listarBrowser")
        self.listarBrowser.setGeometry(QRect(10, 10, 831, 551))
        self.listarBrowser.setStyleSheet(u"QTextBrowser {\n"
"    background: white;\n"
"}")
        self.stackedWidget.addWidget(self.ListarScreen)
        self.CrearScreen = QWidget()
        self.CrearScreen.setObjectName(u"CrearScreen")
        self.groupBox_login_2 = QGroupBox(self.CrearScreen)
        self.groupBox_login_2.setObjectName(u"groupBox_login_2")
        self.groupBox_login_2.setGeometry(QRect(390, 40, 431, 551))
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
        self.buttonEnviar.setGeometry(QRect(160, 490, 75, 31))
        self.buttonEnviar.setStyleSheet(u"QPushButton {\n"
"    background: #74b9ff;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #578bbf;\n"
"    color: black;\n"
"	font-weight: bold;\n"
"	font-size: 11px;\n"
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
        self.respuestaLabel_4 = QLabel(self.groupBox_login_2)
        self.respuestaLabel_4.setObjectName(u"respuestaLabel_4")
        self.respuestaLabel_4.setGeometry(QRect(50, 410, 111, 16))
        self.respuestaLabel_4.setStyleSheet(u"QLabel {\n"
"    color: black;\n"
"}")
        self.comboNivel = QComboBox(self.groupBox_login_2)
        self.comboNivel.addItem("")
        self.comboNivel.addItem("")
        self.comboNivel.addItem("")
        self.comboNivel.setObjectName(u"comboNivel")
        self.comboNivel.setGeometry(QRect(50, 440, 81, 31))
        self.comboNivel.setStyleSheet(u"QComboBox {\n"
"    background: white;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"")
        self.boton_volver_admin_2 = QPushButton(self.CrearScreen)
        self.boton_volver_admin_2.setObjectName(u"boton_volver_admin_2")
        self.boton_volver_admin_2.setGeometry(QRect(20, 10, 75, 31))
        self.boton_volver_admin_2.setStyleSheet(u"QPushButton {\n"
"    background: #a29bfe;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    border: 1px solid #716db2;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}")
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
"	font-weight: bold;\n"
"	font-size: 9pt;\n"
"}")
        self.boton_volver_admin_3 = QPushButton(self.EliminarScreen)
        self.boton_volver_admin_3.setObjectName(u"boton_volver_admin_3")
        self.boton_volver_admin_3.setGeometry(QRect(20, 10, 75, 31))
        self.boton_volver_admin_3.setStyleSheet(u"QPushButton {\n"
"    background: #a29bfe;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    border: 1px solid #716db2;\n"
"    color: black;\n"
"    font-weight: bold;\n"
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

        self.stackedWidget.setCurrentIndex(4)


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
        self.logo_5.setText("")
        self.crearPregunta.setText(QCoreApplication.translate("MainWindow", u"Crear Pregunta", None))
        self.eliminarPregunta.setText(QCoreApplication.translate("MainWindow", u"Eliminar Pregunta", None))
        self.actualizarPregunta.setText(QCoreApplication.translate("MainWindow", u"Actualizar Pregunta", None))
        self.listarPreguntas.setText(QCoreApplication.translate("MainWindow", u"Listar Preguntas", None))
        self.logo.setText("")
        self.boton_volver_admin_4.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.groupBox_login_4.setTitle("")
        self.pregunta_label_2.setText(QCoreApplication.translate("MainWindow", u"Pregunta", None))
        self.respuestaLabel_3.setText(QCoreApplication.translate("MainWindow", u"Respuesta", None))
        self.buttonActualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.IdLabel_4.setText(QCoreApplication.translate("MainWindow", u"Id de la pregunta", None))
        self.respuestaLabel_5.setText(QCoreApplication.translate("MainWindow", u"Dificultad", None))
        self.combo_respuestas_3.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.combo_respuestas_3.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.combo_respuestas_3.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))

        self.boton_volver_admin.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.pregunta.setText(QCoreApplication.translate("MainWindow", u"Pregunta", None))
        self.foto.setText("")
        self.enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.boton_volver.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.respuestaLabel_2.setText(QCoreApplication.translate("MainWindow", u"Elige opci\u00f3n:", None))
        self.groupBox_login_5.setTitle("")
        self.buttonVolver.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.groupBox_login_2.setTitle("")
        self.preguinta_label.setText(QCoreApplication.translate("MainWindow", u"Pregunta", None))
        self.respuestaLabel.setText(QCoreApplication.translate("MainWindow", u"Respuesta", None))
        self.buttonEnviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.respuestaLabel_4.setText(QCoreApplication.translate("MainWindow", u"Dificultad", None))
        self.comboNivel.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboNivel.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboNivel.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))

        self.boton_volver_admin_2.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.groupBox_login_3.setTitle("")
        self.idLabel.setText(QCoreApplication.translate("MainWindow", u"Id de la pregunta", None))
        self.buttonEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.boton_volver_admin_3.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
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

