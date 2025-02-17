import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication

class SpaceRoom(QMainWindow):
    def __init__(self):
        super(SpaceRoom, self).__init__()
        uic.loadUi("juego.ui", self)

        #! Nombre de la aplicación en la ventana
        self.setWindowTitle("Space Room")

        #! Agregar datos de prueba
        self.label_frase_profesor.setText("El profesor dice: Piensa bien antes de responder.")
        self.label_acertijo.setText("¿Qué tiene un ojo pero no puede ver?")
        self.label_respuesta.setText("Respuesta: ???")
        self.btn_pist.setText("Mostrar pista")

        #! Conectar el botón a una función
        self.btn_pist.clicked.connect(self.mostrar_pista)

    def mostrar_pista(self):
        self.label_respuesta.setText("Pista: Se usa para coser.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = SpaceRoom()
    dia.show()
    sys.exit(app.exec())