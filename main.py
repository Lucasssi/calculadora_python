import sys
from PySide6.QtWidgets import QApplication, QLabel
from info import Info
from main_window import MainWindon
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from styles import setupTheme
from buttons import Buttuon, ButtonsGrid



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
    window.addWidgetToVLayout(info)

    # Display
    display  = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonGrid)



    button  = Buttuon('Texto do botão')
    window.addWidgetToVLayout(button)

    
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

