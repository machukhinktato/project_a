"""
Простейшее приложение на Kivy
"""
# Традиционный подход к созданию Kivy-приложений


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class MyInterface(GridLayout):
    """
    Элементы управления можно предварительно указать в общем классе-интерфейсе.
    Тогда метод build будет возвращать не экземпляр класса Label, а экземпляр класса-интерфейса.
    При этом используется сеточный компоновщик виджетов GridLayout
    """
    def __init__(self, **kwargs):
        super(MyInterface, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Тестовое приложение'))


class MyApp(App):
    def build(self):
        return MyInterface()


if __name__ == '__main__':
    MyApp().run()
