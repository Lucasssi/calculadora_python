import sys
from PySide6.QtWidgets import QApplication, QLabel
from info import Info
from main_window import MainWindon
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from styles import setupTheme



if __name__ == '__main__':

    #snake_case
    #PascalCase
    #camelCase


    # cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindon()

    # Definir o ícone
    icon = QIcon(str(WINDOW_ICON_PATH)) 
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display  = Display()
    window.addToVLayout(display)

    
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

