import sqlite3
from datetime import datetime

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Jugador (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    creacion DATETIME NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Puntuacion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jugador_id INTEGER NOT NULL,
    puntuacion INTEGER NOT NULL,
    fecha DATETIME NOT NULL,
    FOREIGN KEY (jugador_id) REFERENCES Jugador (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Nivel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Pregunta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL,
    nivel_id INTEGER NOT NULL,
    FOREIGN KEY (nivel_id) REFERENCES Nivel (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Respuesta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pregunta_id INTEGER NOT NULL,
    texto TEXT NOT NULL,
    correcta BOOLEAN NOT NULL,
    FOREIGN KEY (pregunta_id) REFERENCES Pregunta (id)
)
''')

conn.commit()

# Inserción de datos: Niveles, Preguntas y Respuestas

# 1. Insertar niveles
niveles = [("Fácil",), ("Medio",), ("Difícil",)]
cursor.executemany("INSERT INTO Nivel (nombre) VALUES (?)", niveles)
conn.commit()

# Obtener los IDs de los niveles insertados y crear un diccionario para usarlos
cursor.execute("SELECT id, nombre FROM Nivel")
niveles_dict = {nombre: id for id, nombre in cursor.fetchall()}

# 2. Definir preguntas y respuestas
# Cada tupla contiene: (texto de la pregunta, texto de la respuesta, nivel)
preguntas_respuestas = [
    # Sistemas de Gestión Empresarial (Nivel Fácil)
    ("¿Qué sigla representa la planificación de recursos empresariales?", "ERP", "Fácil"),
    ("¿Qué sistema gestiona clientes y ventas?", "CRM", "Fácil"),
    ("¿Qué sigla describe la cadena de suministro?", "SCM", "Fácil"),
    ("¿Qué módulo de un ERP se encarga de la contabilidad?", "Finanzas", "Fácil"),
    ("¿Qué sistema optimiza el control de almacenes?", "WMS", "Fácil"),
    ("¿Qué sigla identifica la planificación de producción?", "MRP", "Fácil"),
    ("¿Qué módulo administra las adquisiciones?", "Compras", "Fácil"),
    ("¿Qué sistema gestiona el capital humano?", "HRMS", "Fácil"),
    ("¿Qué sigla se asocia con la automatización de procesos?", "BPM", "Fácil"),
    ("¿Qué sistema facilita la gestión de proyectos?", "PPM", "Fácil"),

    # PyQT6 (Nivel Medio)
    ("¿Qué lenguaje se utiliza en PyQt6?", "Python", "Medio"),
    ("¿Qué widget crea ventanas principales?", "QMainWindow", "Medio"),
    ("¿Qué clase se usa para botones?", "QPushButton", "Medio"),
    ("¿Qué objeto representa la aplicación?", "QApplication", "Medio"),
    ("¿Qué widget permite ingresar texto?", "QLineEdit", "Medio"),
    ("¿Qué módulo contiene los widgets básicos?", "QtWidgets", "Medio"),
    ("¿Qué layout organiza de forma vertical?", "QVBoxLayout", "Medio"),
    ("¿Qué widget muestra tablas?", "QTableWidget", "Medio"),
    ("¿Qué componente gestiona eventos?", "Signals", "Medio"),
    ("¿Qué herramienta diseña interfaces gráficas?", "QtDesigner", "Medio"),

    # C# (Nivel Difícil)
    ("¿Qué palabra clave define una interfaz?", "interface", "Difícil"),
    ("¿Qué tipo de dato inmutable se usa para cadenas?", "string", "Difícil"),
    ("¿Qué símbolo se emplea para la herencia?", ":", "Difícil"),
    ("¿Qué colección evita elementos duplicados?", "HashSet", "Difícil"),
    ("¿Qué estructura funciona como una pila?", "Stack", "Difícil"),
    ("¿Cómo se conoce al recolector de basura?", "GC", "Difícil"),
    ("¿Qué palabra clave define un delegado?", "delegate", "Difícil"),
    ("¿Qué clase crea hilos en C#?", "Thread", "Difícil"),
    ("¿Qué espacio de nombres agrupa tareas asíncronas?", "Tasks", "Difícil"),
    ("¿Qué tipo de variable almacena direcciones de memoria?", "pointer", "Difícil")
]

# 3. Insertar preguntas y respuestas
for texto_pregunta, texto_respuesta, nivel in preguntas_respuestas:
    nivel_id = niveles_dict[nivel]
    cursor.execute("INSERT INTO Pregunta (texto, nivel_id) VALUES (?, ?)", (texto_pregunta, nivel_id))
    pregunta_id = cursor.lastrowid
    # Se inserta la respuesta como correcta (True)
    cursor.execute("INSERT INTO Respuesta (pregunta_id, texto, correcta) VALUES (?, ?, ?)",
                   (pregunta_id, texto_respuesta, True))

conn.commit()
conn.close()

print("Preguntas y respuestas insertadas correctamente.")