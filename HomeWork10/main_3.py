# Домашняя работа по десятому семинару
# Задание № 3 Создать метакласс для паттерна Синглтон (см. конец вебинара)
# Мы сделаем возможным создание только одного экземпляра класса Singleton.
# Если экземпляр существует, мы всегда будем использовать уже существующий
# объект.

class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            return cls._instance
        return cls._instance


class LoggerY(metaclass=Singleton):
    def __init__(self, text):
        self.text = text + 'LoggerY'


class LoggerX(metaclass=Singleton):
    def __init__(self, text):
        self.text = text + 'LoggerY'


logger1 = LoggerY('елка')
logger2 = LoggerY('Привет')
print(logger1)
print(logger2)
print(f'logger1 == logger1  {logger1 is logger1}')
print(f'logger1 == logger2  {logger2 is logger1}')
print('Получили ссылку на одну область памяти т.е. можно создать только один '
      'экземпляр класса')
logger3 = LoggerX('Привет')
print(logger2)
print(logger3)
print(f'logger2 == logger3  {logger2 is logger3}')
print('При создании обьекта содержание которого одинаковое и классы имеют один'
      ' общий метакласс , а ссылка на область памяти другая')

#Годный пример Я еще не готов сделать т.к. в моих детских програмулинах все
# обьекты единичные
