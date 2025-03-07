import datetime


class Puntuacion:
    id: int 
    jugador_id: str
    puntuacion: int
    fecha: datetime

    def __init__(self, id: int, jugador_id: str, puntuacion: int, fecha: datetime):
        self.id = id
        self.jugador_id = jugador_id
        self.puntuacion = puntuacion
        self.fecha = fecha
