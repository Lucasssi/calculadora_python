import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QMainWindow, QVBoxLayout, QWidget

class MainWindon(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)


        #Configurando o  layout básico
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        #Titulo da janela
        self.setWindowTitle('CALCULADORA')

    def adjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())