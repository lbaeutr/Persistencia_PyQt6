import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import pyrebase
import sqlite3
from datetime import datetime

# Configuración de Pyrebase
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

        #* Titulo ventana principal
        self.setWindowTitle("Programa")

        #* Establecer la página inicial (índice 0, inicio de sesión)
        self.stackedWidget.setCurrentIndex(0)

        #* Inicializar el rol del usuario
        self.rol = None

        #* Boton de inicio de sesión
        self.button_login.clicked.connect(self.handle_login)
        #* Conectar el enlace de registro
        self.registro_enlace.mousePressEvent = self.handle_register
        #* Boton de registro
        self.button_register.clicked.connect(self.handle_register_action)
        #* Conectar el enlace de inicio de sesión en la página de registro
        self.login_enlace.mousePressEvent = self.handle_login_page

        #! USER -> Conectar los botones de dificultad a la función handle_difficulty
        self.buttonFacil.clicked.connect(lambda: self.handle_difficulty(1))  # ID del nivel fácil
        self.buttonNormal.clicked.connect(lambda: self.handle_difficulty(2))  # ID del nivel medio
        self.buttonDificil.clicked.connect(lambda: self.handle_difficulty(3))  # ID del nivel difícil

        #! ADMIN -> Conectar los botones de dificultad y gestión para el administrador
        self.buttonFacilAdmin.clicked.connect(lambda: self.handle_difficulty(1))  # ID del nivel fácil
        self.buttonNormalAdmin.clicked.connect(lambda: self.handle_difficulty(2))  # ID del nivel medio
        self.buttonDificilAdmin.clicked.connect(lambda: self.handle_difficulty(3))  # ID del nivel difícil
        #self.buttonGestion.clicked.connect(self.handle_gestion)
        self.buttonGestion.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        #! Conectar a la base de datos
        self.conn = sqlite3.connect('quiz.db')
        self.cursor = self.conn.cursor()

        #* Botones de pantalla Juego
        self.enviar.clicked.connect(self.mostrar_siguiente_pregunta)

        #! Pantalla de gestión
        #* Boton de listar preguntas
        self.listarPreguntas.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        #* Boton regreso pantalla de gestión de preguntas
        self.buttonVolver.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        #* Boton para crear pregunta
        self.crearPregunta.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        #* Boton para enviar pregunta
        self.buttonEnviar.clicked.connect(self.crear_pregunta)
        #* Boton para accion de eliminar pregunta
        self.eliminarPregunta.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        
        #* Boton para eliminar pregunta --> ACCION ELIMINAR
        self.buttonEliminar.clicked.connect(self.eliminar_pregunta)


        #* Boton para actualizar pregunta
        self.actualizarPregunta.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        #* Boton para Accion de actualizar
        self.buttonActualizar.clicked.connect(self.actualizar_pregunta)

#* ############################# Registro y Login #############################

    def handle_login(self):
        correo = self.input_correo.text().strip()
        contrasena = self.input_contrasena.text().strip()

        if not correo or not contrasena:
            self.show_error("Por favor, ingrese todos los datos")
            return
        
        # Logica para iniciar sesión
        try:
            user = auth.sign_in_with_email_and_password(correo, contrasena)
            print(f"Login exitoso con: {correo}") # Esto debemos mostrar una pantalla de exito

            # Obtener el rol del usuario desde la base de datos local
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

        print(f"Login con: {correo}, {contrasena}") # Esto son logs para el cambio de pantalla para ver si se hace bien

    def handle_register(self, event): # Este metodo es para cambiar a la pagina de registro
        self.stackedWidget.setCurrentIndex(1)
        print("Cambio de pantalla a registro") # Esto son logs para el cambio de pantalla para ver si se hace bien

    def handle_login_page(self, event): # Este metodo es para volver a la pagina de inicio de sesion
        self.stackedWidget.setCurrentIndex(0)
        print("Cambiando a la pagina de inicio de sesion") # Esto son logs para el cambio de pantalla para ver si se hace bien

    
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

        # En esta parte tenemos que anadir la logica del registro
        try:
            # Registrar el usuario en Firebase
            user = auth.create_user_with_email_and_password(correo, contrasena)
            print(f"Registro exitoso con: {correo}") # Esto debemos mostrar una pantalla de exito

            # Crear un registro en la base de datos local
            creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute("INSERT INTO Jugador (nombre, creacion, rol) VALUES (?, ?, ?)", (nombre, creacion, rol))
            self.conn.commit()

            self.stackedWidget.setCurrentIndex(0)
        except Exception as e:
            self.show_error(f"Error al registrar el usuario: {str(e)}")
        print(f"Registro con:  {correo}, {contrasena}")

#* ############################# Juego #############################

    def handle_difficulty(self, nivel): 
        self.nivel_seleccionado = nivel
        self.stackedWidget.setCurrentIndex(4)  # Indice de la pantalla de juego
        print(f"Cambiando a la pantalla de juego con nivel: {nivel}")  # Esto son logs
        self.iniciar_quiz()  # Iniciar el juego 

    def iniciar_quiz(self):
        # Obtener el nivel seleccionado
        nivel_id = self.nivel_seleccionado

        # Obtener las preguntas del nivel seleccionado
        self.preguntas = self.obtener_preguntas_por_nivel(nivel_id)
        self.indice_pregunta_actual = 0

        # Mostrar la primera pregunta
        self.mostrar_pregunta_actual()

    def reiniciar_quiz(self):
        self.stackedWidget.setCurrentIndex(1)  # Volver al menú de selección de dificultad

    def obtener_preguntas_por_nivel(self, nivel_id):
        # Obtener las preguntas y respuestas del nivel seleccionado
        self.cursor.execute('''
        SELECT Pregunta.id, Pregunta.texto, Respuesta.id, Respuesta.texto, Respuesta.correcta
        FROM Pregunta
        JOIN Respuesta ON Pregunta.id = Respuesta.pregunta_id
        WHERE Pregunta.nivel_id = ?
        ''', (nivel_id,))
        resultados = self.cursor.fetchall()

        # Organizar las preguntas y respuestas en una lista de diccionarios
        preguntas = []
        for row in resultados:
            pregunta_id, pregunta_texto, respuesta_id, respuesta_texto, correcta = row
            pregunta = next((p for p in preguntas if p['id'] == pregunta_id), None)
            if not pregunta:
                pregunta = {'id': pregunta_id, 'texto': pregunta_texto, 'respuestas': []}
                preguntas.append(pregunta)
            pregunta['respuestas'].append({'id': respuesta_id, 'texto': respuesta_texto, 'correcta': correcta})

        return preguntas

    def mostrar_pregunta_actual(self):
        if self.indice_pregunta_actual < len(self.preguntas):
            pregunta_actual = self.preguntas[self.indice_pregunta_actual]

            # Mostrar la pregunta
            self.pregunta.setText(pregunta_actual['texto'])

            # Agregar las respuestas al comboBox
            self.combo_respuestas.clear()
            for respuesta in pregunta_actual['respuestas']:
                self.combo_respuestas.addItem(respuesta['texto'])
        else:
            # No hay más preguntas
            self.pregunta.setText("¡Has completado el quiz!")
            self.combo_respuestas.clear()
            # Volver al menu de selección de dificultad
            if self.rol == "user":
                self.stackedWidget.setCurrentIndex(8)  # Menu de administrador
            else:
                self.stackedWidget.setCurrentIndex(9)  # menu de usuario

    def mostrar_siguiente_pregunta(self):
        self.indice_pregunta_actual += 1
        self.mostrar_pregunta_actual()

#* ############################# Control Errores #############################

    def show_error(self, message): # Este metodo es para mostrar un mensaje de error en la pantalla
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()

#* ############################# CRUD #############################

    def mostrar_listar_preguntas(self):
        #todo falta un boton para volver a la pantalla de gestion

        #self.stackedWidget.setCurrentIndex(5)  
        print("Cambiando a la pantalla de listar preguntas")  # Esto son logs para el cambio de pantalla para ver si se hace bien


    def crear_pregunta(self):
        #inputPregunta_2 = self.inputPregunta_2.text()
        #inputRespuesta_2 = self.inputRespuesta_2.text()



        #todo logica de programacion crear pregunta
        

        self.stackedWidget.setCurrentIndex(2)  

    def eliminar_pregunta(self):
        #* input para el id
        inputId_2 = self.inputId_2.text()
        print(inputId_2) # log para comprobacion
        

        #todo logica de programacion para eliminar pregunta
        

        self.stackedWidget.setCurrentIndex(2)

    def actualizar_pregunta(self):  
        inputId = self.inputId.text()
        inputPregunta = self.inputPregunta.toPlainText()
        inputRespuesta = self.inputRespuesta_3.text()

        print(inputId) # log para comprobacion
        print(inputPregunta)
        print(inputRespuesta)

        #todo logica de programacion para actualizar pregunta

        self.stackedWidget.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = SpaceRoom()
    dia.show()
    sys.exit(app.exec())