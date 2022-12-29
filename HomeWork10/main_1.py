# Домашняя работа по десятому семинару
# Задание № 1 Создать дескриптор для атрибутов классов, которые вы создали
# ранее в ДЗ

class CorrectValues:

    def __set__(self, instance, value):
        if type(value) != int and type(value) != float:
            raise TypeError(f'Значение переменной {self.my_attr} не является числом')
        elif value == 0:
            raise ValueError(f'Значение переменной {self.my_attr} равен нулю,'
                             f'а значит результат заведомо обнулится')
        elif value < 0:
            raise ValueError(f'Значение переменной {self.my_attr}  менее нуля,'
                             f' а значит результат будет некоректен')
        else:
            instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    _length = CorrectValues()
    _width = CorrectValues()
    _thickness = CorrectValues()
    _weight = CorrectValues()

    def __init__(self, _length, _width, _thickness, _weight):
        self._length = _length
        self._width = _width
        self._thickness = _thickness
        self._weight = _weight

    def mass(self):
        return self._length * self._width * self._thickness * self._weight

    def square(self):
        return self._length * self._width


road_1 = Road(20, 66, 25, 5)
print(f"Вес участка дорожного полотна {road_1.mass()} кг")
print(f"Площадь участка дорожного полотна {road_1.square()} м2")
road_2 = Road(20, "7000", 25, 5)
print(f"Вес участка дорожного полотна {road_2.mass()} кг")
print(f"Площадь участка дорожного полотна {road_2.square()} м2")
