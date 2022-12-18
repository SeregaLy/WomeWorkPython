# Домашняя работа по седьмому семинару
# Задание № 5 Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод
# выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen
# (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.
from sys import argv


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки. {self.title} хорошо пишет'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки. {self.title} красиво рисует'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки. {self.title} ярко выделяет текст'


SCRIPT_NAME, user_pen, user_pencil, user_hendle = argv
print(Pen(user_pen).draw())
print(Pencil(user_pencil).draw())
print(Handle(user_hendle).draw())
