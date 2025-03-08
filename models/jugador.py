import datetime


class Jugador:
    id: int
    nombre: str
    creacion: datetime
    rol: str


    def __init__(self, id: int, nombre: str, creacion: datetime, rol: str):
        self.id = id
        self.nombre = nombre
        self.creacion = creacion
        self.rol = rol