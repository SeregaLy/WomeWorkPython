class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            return cls._instance
        return cls._instance


class PresidentCar(metaclass=Singleton):
    def __init__(self,  name):
        self.text = name

    def __str__(self):
        return str(self.name)

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


Pytin = PresidentCar('Танк')
print(Pytin)
Pytin = list(map(str, Pytin))
Medvedev = PresidentCar('Оранжевая Калина')
print(Medvedev)