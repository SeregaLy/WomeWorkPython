# Домашняя работа по седьмому семинару
# Задание № 4 Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
# SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и
# WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните
# доступ к атрибутам, выведите результат. Выполните вызов методов и также
# покажите результат.

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} начал движение'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name}  повернул налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed > 40:
            return f'Автомобиль {self.name} превышает разрешенную скорость, ' \
                   f'{self.speed} км/ч при разрешенной 40 км/ч'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed}км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed > 60:
            return f'Автомобиль {self.name} превышает разрешенную скорость, ' \
                   f'{self.speed} км/ч при разрешенной 60 км/ч'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed}км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} патрульный антомобиль экипажа ДПС'
        else:
            return f'{self.name} гражданский автомобиль'


audi = SportCar(100, 'Синий', 'Audi', False)
oka = TownCar(30, 'Желтый', 'Oka', False)
lada = WorkCar(70, 'Баклажан', 'Lada', True)
ford = PoliceCar(110, 'Белый', 'Ford', True)
print(lada.turn_left())
print(f'{lada.name} цвета {lada.color}')
print(f'{audi.name} полицейский автомобиль? {audi.is_police}')
print(f'{lada.name}  полицейский автомобиль?? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())

