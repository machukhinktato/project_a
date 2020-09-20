"""
Простейшее приложение на Kivy
"""
# Декларативный подход к созданию Kivy-приложений

import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

"""
При этом используется язык KV, который позволяет декларативно 
создавать дерево виджетов и связывать их свойства друг с другом.
"""

"""
Преимущества подхода:
●	Быстрое создание прототипов и возможность оперативно
изменять пользовательский интерфейс;
●	Можно реализовать отделение логики работы приложения 
от его графической части (интерфейса пользователя).
"""


class AppInterface(Widget):
    pass


class KivyApp(App):
    def build(self):
        self.root = Builder.load_file('kivy_app.kv')
        return AppInterface()


if __name__ == '__main__':
   KivyApp().run()
