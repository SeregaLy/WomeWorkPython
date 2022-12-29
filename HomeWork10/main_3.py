# Домашняя работа по десятому семинару
# Задание № 3 Создать метакласс для паттерна Синглтон (см. конец вебинара)

class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(Singleton):
    def write_log(self, path):
        pass


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()
    assert logger1 is logger2

print(f"logger1 is logger1  {logger1 is logger1}")
print(f"logger1 is logger1  {logger2 is logger1}")
