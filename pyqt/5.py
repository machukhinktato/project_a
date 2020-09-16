"""Назначение обработчика для сигнала """

# <Qt_компонент>.<Сигнал>.connect(<Обработчик>[, <Тип_соединения>])

# <Qt_компонент>.<Сигнал>.[<Тип>].connect(<Обработчик>[, <Тип_соединения>])

# например, chck_box.checked.connect(on_checked_chck_box)

import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QCheckBox


def on_checked(param):
    """Функция-обработчик события установки флажка"""
    print(f"Флажок установлен. Функция on_checked приняла параметр {param}")


class MyClass:
    """Класс-обработчик события установки флажка"""
    def __init__(self, y=0):
        self.y = y

    def __call__(self):
        print("Флажок установлен. Метод MyClass.__call__()")
        print("y = ", self.y)

    @staticmethod
    def on_checked():
        print("Флажок установлен. Метод MyClass.on_checked()")


APP = QApplication(sys.argv)
CHCK_BOX = QCheckBox("Установите флажок")

# В качестве обработчика назначается функция (используем lambda)
CHCK_BOX.stateChanged.connect(lambda: on_checked(5))

# В качестве обработчика назначается функция (используем partial)
CHCK_BOX.stateChanged.connect(partial(on_checked, 5))

MC_OBJ = MyClass()
# В качестве обработчика назначается метод объекта
CHCK_BOX.stateChanged.connect(MC_OBJ.on_checked)

# В качестве обработчика назначается класс
CHCK_BOX.stateChanged.connect(MyClass(10))

# В качестве обработчика назначается lambda-функция
CHCK_BOX.stateChanged.connect(lambda: MyClass(5)())

CHCK_BOX.show()
sys.exit(APP.exec_())

# Результат
"""
Флажок установлен. Функция on_checked приняла параметр 5
Флажок установлен. Функция on_checked приняла параметр 5
Флажок установлен. Метод MyClass.on_checked()
Флажок установлен. Метод MyClass.__call__()
y =  10
Флажок установлен. Метод MyClass.__call__()
y =  5
"""
