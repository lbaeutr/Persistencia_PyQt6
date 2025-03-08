import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import pyrebase
import sqlite3
from datetime import datetime



#! Configuración de Pyrebase
config = {
    "apiKey": "AIzaSyBhn8Aabjpo3u2DkTsyYzjIvmRztP2t-jo",
    "authDomain": "partyfunamigos.firebaseapp.com",
    "databaseURL": "https://partyfunamigos-default-rtdb.firebaseio.com",
    "projectId": "partyfunamigos",
    "storageBucket": "partyfunamigos.firebasestorage.app",
    "messagingSenderId": "353114155020",
    "appId": "1:353114155020:web:17b507b32667922b682629",
    "measurementId": "G-WXJ46P4RPZ"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

class SpaceRoom(QMainWindow):
    def __init__(self):
        super(SpaceRoom, self).__init__()
        uic.loadUi("juego.ui", self)

        #! Titulo ventana principal
        self.setWindowTitle("Programa")

        #! Establecer la página inicial ( índice 0 ,inicio de sesión)
        self.stackedWidget.setCurrentIndex(0)

        #! Boton de inicio de sesión
        self.button_login.clicked.connect(self.handle_login)
        #! Conectar el enlace de registro
        self.registro_enlace.mousePressEvent = self.handle_register
        #!  Boton de registro
        self.button_register.clicked.connect(self.handle_register_action)
        #! Conectar el enlace de inicio de sesión en la página de registro
        self.login_enlace.mousePressEvent = self.handle_login_page


        #! Conectar los botones de dificultad a la función handle_difficulty
        self.buttonFacil.clicked.connect(self.handle_difficulty)
        self.buttonNormal.clicked.connect(self.handle_difficulty)
        self.buttonDificil.clicked.connect(self.handle_difficulty)

        #! Conectar a la base de datos
        self.conn = sqlite3.connect('quiz.db')
        self.cursor = self.conn.cursor()


    def handle_login(self):
        correo = self.input_correo.text().strip()
        contrasena = self.input_contrasena.text().strip()

        if not correo or not contrasena:
            self.show_error("Por favor, ingrese todos los datos")
            return
        
        #* Logica para iniciar sesión
        try:
            user = auth.sign_in_with_email_and_password(correo, contrasena)
            print(f"Login exitoso con: {correo}") # todo : esto debemos mostrar una pantalla de exito

            #! Obtener el rol del usuario desde la base de datos local
            self.cursor.execute("SELECT rol FROM Jugador WHERE nombre = ?", (correo,))
            result = self.cursor.fetchone()

            if result:
                rol = result[0]
                if rol == "admin":
                    self.stackedWidget.setCurrentIndex(9)  # Índice de la pantalla de administrador
                else:
                    self.stackedWidget.setCurrentIndex(8)  # Índice de la pantalla de usuario
            else:
                self.show_error("Usuario no encontrado en la base de datos local")

        except:
            self.show_error("Correo o contraseña incorrectos")

        print(f"Login con: {correo}, {contrasena}") #Esto son logs para el cambio de pantalla para versi se hace bien

    def handle_register(self, event): # Este metodo es para cambiar a la pagina de registro
        self.stackedWidget.setCurrentIndex(1)
        print("Cambio de pantalla a registro") #Esto son logs para el cambio de pantalla para versi se hace bien


    def handle_login_page(self, event): # Este metodo es para volver a la pagina de inicio de sesion
        self.stackedWidget.setCurrentIndex(0)
        print("Cambiando a la pagina de inicio de sesion") #Esto son logs para el cambio de pantalla para versi se hace bien


    def handle_difficulty(self):
        self.stackedWidget.setCurrentIndex(3)  # Indice de la pantalla de juego
        print("Cambiando a la pantalla de juego") # Esto son logs 

    def handle_register_action(self): # Este metodo es para registrar un usuario
        correo = self.input_correo_2.text().strip()
        contrasena = self.input_contrasena_2.text().strip()
        confirmar_contrasena = self.input_repeatContra.text().strip()
        nombre = self.input_correo_2.text().strip()
        rol = "user"  

        if not correo or not contrasena or not confirmar_contrasena or not nombre:
            self.show_error("Por favor, ingrese todos los datos")
            return

        if contrasena != confirmar_contrasena:
            self.show_error("Las contraseñas no coinciden")
            return

        # todo: En esta parte tenemos que anadir la logica del registro
        try:
            # Registrar el usuario en Firebase
            user = auth.create_user_with_email_and_password(correo, contrasena)
            print(f"Registro exitoso con: {correo}") # todo : esto debemos mostrar una pantalla de exito

            # Crear un registro en la base de datos local
            creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute("INSERT INTO Jugador (nombre, creacion, rol) VALUES (?, ?, ?)", (nombre, creacion, rol))
            self.conn.commit()

            self.stackedWidget.setCurrentIndex(0)
        except Exception as e:
            self.show_error(f"Error al registrar el usuario: {str(e)}")
        print(f"Registro con:  {correo}, {contrasena}")


    def show_error(self, message): # Este metodo es para mostrar un mensaje de error en la pantalla
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = SpaceRoom()
    dia.show()
    sys.exit(app.exec())


    