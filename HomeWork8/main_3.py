# Домашняя работа по восьмому семинару
# Задание № 3 Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на нуль. Проверьте его работу на данных, вводимых пользователем. При
# вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class Zero(Exception):

    def __init__(self, text):
        self.text = text


def test(a, b):
    try:
        if b == 0:
            raise Zero('Cannot divide by zero')
    except Zero as err:
        print(err)
    else:
        print(f'All right: {a} / {b} = {int(a) / int(b)}')


test(5, 2)
test(5, 0)
