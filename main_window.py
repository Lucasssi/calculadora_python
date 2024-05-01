import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QMainWindow, QVBoxLayout, QWidget, QLineEdit, QTextEdit
from PySide6.QtGui import QIcon

class MainWindon(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)


        #Configurando o  layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        #Titulo da janela
        self.setWindowTitle('CALCULADORA')


    def adjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
