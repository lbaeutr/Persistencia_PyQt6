import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

class SpaceRoom(QMainWindow):
    def __init__(self):
        super(SpaceRoom, self).__init__()
        uic.loadUi("juego.ui", self)

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

    def handle_login(self):
        correo = self.input_correo.text().strip()
        contrasena = self.input_contrasena.text().strip()

        if not correo or not contrasena:
            self.show_error("Por favor, ingrese todos los datos")
            return

        print(f"Login con: {correo}, {contrasena}") #Esto son logs para el cambio de pantalla para versi se hace bien

    def handle_register(self, event): # Este metodo es para cambiar a la pagina de registro
        self.stackedWidget.setCurrentIndex(1)
        print("Cambio de pantalla a registro") #Esto son logs para el cambio de pantalla para versi se hace bien

    def handle_register_action(self): # Este metodo es para registrar un usuario
        correo = self.input_correo_2.text().strip()
        contrasena = self.input_contrasena_2.text().strip()
        confirmar_contrasena = self.input_repeatContra.text().strip()

        if  not correo or not contrasena or not confirmar_contrasena:
            self.show_error("Por favor, ingrese todos los datos")
            return

        if contrasena != confirmar_contrasena:
            self.show_error("Las contraseñas no coinciden")
            return

        # todo: En esta parte tenemos que anadir la logica del registro
        print(f"Registro con:  {correo}, {contrasena}")

    def handle_login_page(self, event): # Este metodo es para volver a la pagina de inicio de sesion
        self.stackedWidget.setCurrentIndex(0)
        print("Cambiando a la pagina de inicio de sesion") #Esto son logs para el cambio de pantalla para versi se hace bien

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