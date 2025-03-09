import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import pyrebase
import sqlite3
import random
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
        self.enviar.clicked.connect(self.enviar_respuesta)
        self.boton_volver.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(8))

        #! Pantalla de gestión

        # Botón de listar preguntas
        self.listarPreguntas.clicked.connect(self.listar_preguntas)


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

        #* Botones para volver como admin
        self.boton_volver_admin.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.boton_volver_admin_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.boton_volver_admin_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))
        self.boton_volver_admin_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(9))

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
        self.stackedWidget.setCurrentIndex(8)  # Volver al menú de selección de dificultad

        

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

        # Obtener respuestas incorrectas aleatorias de otras preguntas
        self.cursor.execute('''
        SELECT Respuesta.texto
        FROM Respuesta
        JOIN Pregunta ON Respuesta.pregunta_id = Pregunta.id
        WHERE Pregunta.nivel_id = ? AND Respuesta.correcta = 0
        ''', (nivel_id,))
        respuestas_incorrectas = [row[0] for row in self.cursor.fetchall()]

        # Si no hay respuestas incorrectas, forzar algunas respuestas como incorrectas
        if not respuestas_incorrectas:
            self.cursor.execute('''
            SELECT Respuesta.texto
            FROM Respuesta
            JOIN Pregunta ON Respuesta.pregunta_id = Pregunta.id
            WHERE Pregunta.nivel_id = ?
            ''', (nivel_id,))
            todas_las_respuestas = [row[0] for row in self.cursor.fetchall()]
            respuestas_incorrectas = todas_las_respuestas  # Usar todas las respuestas como incorrectas

        # Mezclar las respuestas incorrectas para obtener opciones aleatorias
        import random
        random.shuffle(respuestas_incorrectas)

        # Añadir respuestas incorrectas aleatorias a cada pregunta
        for pregunta in preguntas:
            respuestas_correctas = [r for r in pregunta['respuestas'] if r['correcta'] == 1]
            respuestas_incorrectas_pregunta = respuestas_incorrectas[:3]  # Tomar 3 respuestas incorrectas aleatorias
            pregunta['respuestas'] = respuestas_correctas + [{'texto': r, 'correcta': 0} for r in respuestas_incorrectas_pregunta]
            random.shuffle(pregunta['respuestas'])  # Mezclar las respuestas para que no siempre esté primero la correcta

        return preguntas

    def mostrar_pregunta_actual(self):
        if self.indice_pregunta_actual < len(self.preguntas):
            pregunta_actual = self.preguntas[self.indice_pregunta_actual]

            # Mostrar la pregunta
            self.pregunta.setText(pregunta_actual['texto'])

            # Verificar la estructura de las respuestas (para depuración)
            print("Pregunta actual:", pregunta_actual)

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
                self.stackedWidget.setCurrentIndex(9)  # Menu de administrador
            else:
                self.stackedWidget.setCurrentIndex(8)  # menu de usuario

    def enviar_respuesta(self):

        if self.indice_pregunta_actual < len(self.preguntas):
            pregunta_actual = self.preguntas[self.indice_pregunta_actual]
            respuesta_seleccionada = self.combo_respuestas.currentText()

            # Verificar si la respuesta seleccionada es correcta
            respuesta_correcta = next((r for r in pregunta_actual['respuestas'] if r['correcta'] == 1), None)
            if respuesta_correcta and respuesta_seleccionada == respuesta_correcta['texto']:
                # Mostrar un mensaje de "Correcto"
                QMessageBox.information(
                    self,  # Ventana padre
                    "Correcto",  # Título del mensaje
                    "¡Respuesta correcta!",  # Mensaje
                    QMessageBox.StandardButton.Ok  # Botón "Aceptar"
                )
            else:
                self.show_error(f"Respuesta incorrecta. La respuesta correcta era: {respuesta_correcta['texto']}")

            # Pasar a la siguiente pregunta
            self.indice_pregunta_actual += 1
            self.mostrar_pregunta_actual()  # Mostrar la siguiente pregunta
        else:
            # Si no hay más preguntas, mostrar un mensaje de finalización
            self.show_error("¡Has completado el quiz!")
            # Volver al menú de selección de dificultad
            if self.rol == "user":
                self.stackedWidget.setCurrentIndex(8)  # Menú de usuario
            else:
                self.stackedWidget.setCurrentIndex(9)  # Menú de administrador

#* ############################# Control Errores #############################

    def show_error(self, message): # Este metodo es para mostrar un mensaje de error en la pantalla
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()

#* ############################# CRUD #############################

    def listar_preguntas(self):
        try:
            self.cursor.execute('''
                SELECT Pregunta.id, Pregunta.texto, Pregunta.nivel_id, Respuesta.texto
                FROM Pregunta
                JOIN Respuesta ON Pregunta.id = Respuesta.pregunta_id
                ORDER BY Pregunta.id
            ''')
            resultados = self.cursor.fetchall()

            print("Resultados de la consulta:", resultados)  # 🔍 Depuración

            if not resultados:
                self.listarBrowser.setPlainText("No hay preguntas registradas.")
            else:
                texto = ""
                pregunta_actual = None
                for row in resultados:
                    pregunta_id, texto_pregunta, nivel, texto_respuesta = row
                    if pregunta_actual != pregunta_id:
                        texto += f"\nID: {pregunta_id} | Nivel: {nivel}\nPregunta: {texto_pregunta}\nRespuestas:\n"
                        pregunta_actual = pregunta_id
                    texto += f"  - {texto_respuesta}\n"

                print("Texto generado:", texto)  # 🔍 Depuración
                self.listarBrowser.setPlainText(texto)

            self.stackedWidget.setCurrentIndex(5)  # Cambiar a la pantalla correcta

        except Exception as e:
            print("Error al listar preguntas:", e)  # 🔍 Depuración
            self.listarBrowser.setPlainText(f"Error al listar preguntas: {str(e)}")
            self.stackedWidget.setCurrentIndex(5)

    def crear_pregunta(self):
        # Obtener el texto de la pregunta (QTextEdit)
        texto_pregunta = self.inputPregunta_2.toPlainText().strip()
        
        # Obtener el nivel seleccionado (QComboBox)
        nivel_id = self.comboNivel.currentIndex() + 1  # Asumiendo que el comboBox tiene los niveles 1, 2, 3
        
        # Obtener la respuesta correcta (QLineEdit)
        respuesta_correcta = self.inputRespuesta.text().strip()

        # Validar que todos los campos estén completos
        if not texto_pregunta or not respuesta_correcta:
            self.show_error("Por favor, complete todos los campos")
            return

        try:
            # Insertar la pregunta en la base de datos
            self.cursor.execute("INSERT INTO Pregunta (texto, nivel_id) VALUES (?, ?)", (texto_pregunta, nivel_id))
            pregunta_id = self.cursor.lastrowid  # Obtener el ID de la pregunta recién insertada

            # Insertar la respuesta correcta en la base de datos
            self.cursor.execute(
                "INSERT INTO Respuesta (texto, correcta, pregunta_id) VALUES (?, ?, ?)",
                (respuesta_correcta, 1, pregunta_id)  # correcta = 1 (verdadero)
            )

            # Guardar los cambios en la base de datos
            self.conn.commit()
            
            # Mostrar un mensaje de éxito
            QMessageBox.information(self, "Éxito", "Pregunta creada exitosamente")
            
            # Limpiar los campos
            self.limpiar_campos()
            
            # Volver a la pantalla de gestión
            self.stackedWidget.setCurrentIndex(2)
        except Exception as e:
            print(f"Error: {str(e)}")  # Depuración
            QMessageBox.critical(self, "Error", f"Error al crear la pregunta: {str(e)}")

    def limpiar_campos(self):
        # Limpiar campos en el crear pregunta
        self.inputPregunta_2.clear()        
        self.inputRespuesta.clear()        
        self.comboNivel.setCurrentIndex(0)        
        if hasattr(self, 'comboCorrecta'):
            self.comboCorrecta.setCurrentIndex(0)

        # Limpiar campos en el modificar pregunta
        self.inputPregunta.clear()
        self.inputRespuesta_3.clear()
        self.inputId.clear()
        if hasattr(self, 'comboNivel'):
            self.comboNivel.setCurrentIndex(0)
        

    def eliminar_pregunta(self):
        pregunta_id = self.inputId_2.text().strip()

        if not pregunta_id:
            self.show_error("Por favor, ingrese el ID de la pregunta")
            return

        try:
            # Eliminar las respuestas asociadas a la pregunta
            self.cursor.execute("DELETE FROM Respuesta WHERE pregunta_id = ?", (pregunta_id,))
            # Eliminar la pregunta
            self.cursor.execute("DELETE FROM Pregunta WHERE id = ?", (pregunta_id,))
            self.conn.commit()
            self.show_error("Pregunta eliminada exitosamente")
            self.stackedWidget.setCurrentIndex(2)  # Volver a la pantalla de gestión
        except Exception as e:
            self.show_error(f"Error al eliminar la pregunta: {str(e)}")

    def actualizar_pregunta(self):  
        pregunta_id = self.inputId.text().strip()
        texto_pregunta = self.inputPregunta.toPlainText().strip()
        texto_respuesta = self.inputRespuesta_3.text().strip()

        if not pregunta_id or not texto_pregunta or not texto_respuesta:
            self.show_error("Por favor, complete todos los campos")
            return

        try:
            # Actualizar la pregunta
            self.cursor.execute("UPDATE Pregunta SET texto = ? WHERE id = ?", (texto_pregunta, pregunta_id))
            # Actualizar la respuesta (asumiendo que solo se actualiza una respuesta)
            self.cursor.execute("UPDATE Respuesta SET texto = ? WHERE pregunta_id = ?", (texto_respuesta, pregunta_id))
            self.conn.commit()
            QMessageBox.information(self, "Éxito", "Pregunta actualizada exitosamente")
            self.limpiar_campos()
            self.stackedWidget.setCurrentIndex(2)  # Volver a la pantalla de gestión
        except Exception as e:
            self.show_error(f"Error al actualizar la pregunta: {str(e)}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = SpaceRoom()
    dia.show()
    sys.exit(app.exec())