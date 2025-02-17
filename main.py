import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *



class pantalla(QMainWindow):
    def __init__(self):
        super(pantalla, self).__init__()
        uic.loadUi("juego.ui", self)
               #! Nombre de la aplicación en la ventana 
        self.setWindowTitle("space_room")

    









if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = pantalla()
    dia.show()
    sys.exit(app.exec())