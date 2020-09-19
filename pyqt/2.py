"""Создаем PyQt-приложение вручную"""

import sys
# QtWidgets — содержит классы для классических приложений на основе виджетов,
# модуль выделен из модуля QtGui в версии PyQt5
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class CatalogMainWindow(QMainWindow):
    """
    QMainWindow - класс, содержит в себе обобщенные
    средства для создания на их основе главных окон приложения

    QAction - класс, предоставляет абстрактное действие пользовательского интерфейса,
    которое может быть вставлено в виджеты

    QApplication - класс, управляет главным потоком и основными настройками приложения с GUI
    """

    def __init__(self):
        super().__init__()

        # Создаем меню
        self.menu_bar = self.menuBar()

        # Наполняем меню
        self.gma_menu = self.menu_bar.addMenu('Учет движения товаров')
        self.ro_open_btn = QAction(self)
        self.ro_open_btn.setText('Приходный ордер')
        self.wo_open_btn = QAction(self)
        self.wo_open_btn.setText('Расходный ордер')
        self.gma_menu.addAction(self.ro_open_btn)
        self.gma_menu.addAction(self.wo_open_btn)


# Отобразить главное окно
if __name__ == "__main__":

    '''
    Каждое приложение PyQt5 должно создать объект QApplication. 
    Параметр sys.argv это список аргументов командной строки. 
    Скрипты на Пайтон могут быть запущены из консоли, 
    и с помощью аргументов мы можем контролировать запуск приложения.
    '''

    APP = QApplication(sys.argv)

    CMW = CatalogMainWindow()
    CMW.setWindowTitle('Складской учет')
    CMW.setFixedSize(700, 300)
    CMW.show()

    '''
    В конце мы запускаем основной цикл приложения.
    Отсюда начинается обработка событий. 
    Приложение получает события от оконной системы и распределяет их по виджетам. 
    Когда цикл заканчивается, и если мы вызовем метод exit(), 
    то наше окно (главный виджет) будет уничтожено. 
    Метод sys.exit() гарантирует чистый выход. 
    Окружение будет проинформировано о том, как приложение завершилось.
    Вы удивлены почему метод exec_() записан с подчеркиваение? 
    Это сделано потому, что exec – ключевое слово в пайтон.
    '''

    sys.exit(APP.exec_())
