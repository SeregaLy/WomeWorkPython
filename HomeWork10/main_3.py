# Домашняя работа по десятому семинару
# Задание № 3 Создать метакласс для паттерна Синглтон (см. конец вебинара)

class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            return cls._instance
        return cls._instance


class Logger(metaclass=Singleton):
    def __init__(self, text):
        self.text = text


logger1 = Logger('елка')
logger2 = Logger('Привет')
print(logger1)
print(logger2)
print('Получили ссулку на одну область памяти')
print(f"logger1 is logger1  {logger1 is logger1}")
print(f"logger1 is logger1  {logger2 is logger1}")
