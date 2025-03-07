class Respuesta:
    id: int
    pregunta_id: int
    texto: str
    correcta: bool


    def __init__(self, id: int, pregunta_id: int, texto: str, correcta: bool):
        self.id = id
        self.pregunta_id = pregunta_id
        self.texto = texto
        self.correcta = correcta