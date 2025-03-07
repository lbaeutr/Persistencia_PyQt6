import datetime


class Jugador:
    id: int
    nombre: str
    creacion: datetime


    def __init__(self, id: int, nombre: str, creacion: datetime):
        self.id = id
        self.nombre = nombre
        self.creacion = creacion