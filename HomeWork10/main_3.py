# Домашняя работа по десятому семинару
# Задание № 3 Создать метакласс для паттерна Синглтон (см. конец вебинара)

class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            return cls._instance
        return cls._instance


class LoggerY(metaclass=Singleton):
    def __init__(self, text):
        self.text = text
class LoggerX(metaclass=Singleton):
    def __init__(self, text):
        self.text = text

logger1 = LoggerY('елка')
logger2 = LoggerY('Привет')
logger3 = LoggerX('Привет')
print(logger1)
print(logger2)
print('Получили ссылку на одну область памяти')
print(logger3)
print('содержание одинаковое, а вот ссылка на область памяти другая')
print(f'logger1 is logger1  {logger1 is logger1}')
print(f'logger1 is logger2  {logger2 is logger1}')
print(f'logger2 is logger3  {logger2 is logger3}')

