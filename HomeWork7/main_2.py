# Домашняя работа по седьмому семинару
# Задание № 2 Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width бутов должны
# передаваться при создании экземпляра класса. Атр(ширина). Значения данных
# атриибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длинаширинамасса асфальта для
# покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины
# полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, _length, _width, _thickness, _weight):
        self._length = _length
        self._width = _width
        self._thickness = _thickness
        self._weight = _weight

    def mass(self):
        return self._length * self._width * self._thickness * self._weight

    def square(self):
        return self._length * self._width

road_1 = Road(20, 5000, 25, 5)
print(f"Вес участка дорожного полотна {road_1.mass()} кг")
print(f"Площадь участка дорожного полотна {road_1.square()} м2")