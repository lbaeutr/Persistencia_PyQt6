class Pregunta:
    id: int
    texto: str
    nivel_id: int


    def __init__(self, id: int, texto: str, nivel_id: int):
        self.id = id
        self.texto = texto
        self.nivel_id = nivel_id