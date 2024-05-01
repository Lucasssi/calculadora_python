import sys
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindon
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display



if __name__ == '__main__':

    #snake_case
    #PascalCase
    #camelCase


    # cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindon()

    # Definir o ícone
    icon = QIcon(str(WINDOW_ICON_PATH)) 
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display  = Display()
    window.addToVLayout(display)

    
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

