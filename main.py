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


        #! USER -> Conectar los botones de dificultad a la función handle_difficulty
        self.buttonFacil.clicked.connect(self.handle_difficulty)
        self.buttonNormal.clicked.connect(self.handle_difficulty)
        self.buttonDificil.clicked.connect(self.handle_difficulty)

        #! ADMIN -> Conectar los botones de dificultad y gestión para el administrador
        self.buttonFacilAdmin.clicked.connect(self.handle_difficulty)
        self.buttonNormalAdmin.clicked.connect(self.handle_difficulty)
        self.buttonDificilAdmin.clicked.connect(self.handle_difficulty)
        self.buttonGestion.clicked.connect(self.handle_gestion)

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


    def handle_gestion(self):
        # Cambiar al índice de la pantalla de gestión
        self.stackedWidget.setCurrentIndex(2)  # Asegúrate de que el índice 2 sea el de la pantalla de gestión
        print("Cambiando a la pantalla de gestión") # Esto son logs para el cambio de pantalla para ver si se hace bien


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





    def iniciar_quiz(self):
        # Obtener el nivel seleccionado
        nivel_id = self.combo_niveles.currentData()

        # Obtener las preguntas del nivel seleccionado
        self.preguntas = self.obtener_preguntas_por_nivel(nivel_id)
        self.indice_pregunta_actual = 0

        # Mostrar la primera pregunta
        self.mostrar_pregunta_actual()

        # Cambiar a la pantalla del quiz
        self.stackedWidget.setCurrentIndex(2)  # Suponiendo que el índice 2 es la pantalla del quiz

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
            self.label_pregunta.setText(pregunta_actual['texto'])

            # Limpiar el comboBox de respuestas
            self.combo_respuestas.clear()

            # Agregar las respuestas al comboBox
            for respuesta in pregunta_actual['respuestas']:
                self.combo_respuestas.addItem(respuesta['texto'])
        else:
            # No hay más preguntas
            self.label_pregunta.setText("¡Has completado el quiz!")
            self.combo_respuestas.clear()
            self.button_responder.setEnabled(False)  # Deshabilitar el botón de responder
    

    def get_pregunta_actual(self):
        if self.indice_pregunta_actual < len(self.preguntas):
            return self.preguntas[self.indice_pregunta_actual]
        return None


    def responder_pregunta(self):
        respuesta_seleccionada = self.combo_respuestas.currentText()
        pregunta_actual = self.get_pregunta_actual()

        # Verificar si la respuesta es correcta
        self.cursor.execute('''
        SELECT correcta FROM Respuesta WHERE pregunta_id = ? AND texto = ?
        ''', (pregunta_actual.id, respuesta_seleccionada))
        resultado = self.cursor.fetchone()

        if resultado and resultado[0]:
            self.actualizar_puntuacion()
            self.mostrar_siguiente_pregunta()
        else:
            self.show_error("Respuesta incorrecta")


    def actualizar_puntuacion(self):
        try:
            jugador_id = self.get_jugador_actual().id
            fecha = datetime.now()
            self.cursor.execute('''
            INSERT INTO Puntuacion (jugador_id, puntuacion, fecha) VALUES (?, ?, ?)
            ''', (jugador_id, 1, fecha))
            self.conn.commit()
        except sqlite3.Error as e:
            self.show_error(f"Error al actualizar la puntuación: {e}")


    def get_jugador_actual(self):
        # Aquí debemos obtener el ID del jugador actual (por ejemplo, desde Firebase)
        # Esto es un ejemplo, tenemos q adaptarlo 
        return {"id": 1}  # Reemplazar p


    def cargar_niveles(self):
        # Obtener los niveles de dificultad desde la base de datos
        self.cursor.execute('SELECT id, nombre FROM Nivel')
        niveles = self.cursor.fetchall()

        # Limpiar el ComboBox
        self.combo_niveles.clear()

        # Agregar los niveles al ComboBox
        for nivel in niveles:
            self.combo_niveles.addItem(nivel[1], nivel[0])  # nombre, id   


    def mostrar_siguiente_pregunta(self):
        self.indice_pregunta_actual += 1
        self.mostrar_pregunta_actual()


   
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


    