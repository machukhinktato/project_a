"""Создаем PyQt-приложение c ui-файлом, конвертированном в py-файл"""
# Нужно перейти в папку с ui-файлом и из этой папки запустить команду конвертации
# pyuic5 имя_исходного_ui_файла -o имя_конечного_py_файла
# например,
# pyuic5 server.ui -o server.py

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp
# Импортируем сгенерированный файл server
import server


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Создаем экземпляр класса формы (экземпляр интерфейса) 
        # из файла server
        self.ui = server.Ui_ServerGui()
        # Связываем экземпляр интерфейса с данным окном
        self.ui.setupUi(self)
        # Устанавливаем для кнопки обработчик
        self.ui.btn_quit.clicked.connect(qApp.quit)


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    WIN = Window()
    WIN.show()
    sys.exit(APP.exec_())
