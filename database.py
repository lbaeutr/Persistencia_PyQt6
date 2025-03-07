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