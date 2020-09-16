"""Создаем PyQt-приложение c ui-файлом, созданным в Qt-дизайнере"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp
# qApp - это глобальный (доступный из любого места приложения)
# указатель на объект текущего приложения (PyQt)
from PyQt5 import uic


class Window(QMainWindow):
    """Главное окно"""
    def __init__(self):
        super().__init__()
        # Для подключения файла с кодом интерфейса необходимо воспользоваться функцией loadUi()
        # loadUi(<ui-файл>[, <экземпляр_класса>])
        uic.loadUi('server.ui', self)
        # У одного из элементов управления интерфейса (кнопки) имя btn_quit
        # С этой кнопкой мы связываем обработчик события нажатия (clicked)
        # Этот обработчик - закрытие окна (стандартная функция quit)
        self.btn_quit.clicked.connect(qApp.quit)


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    WIN = Window()
    WIN.show()
    sys.exit(APP.exec_())
