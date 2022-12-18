# Домашняя работа по седьмому семинару
# Задание № 3 Реализовать базовый класс Worker (работник), в котором
# определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать
# класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на
# реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
from sys import argv


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        '''
        вывод имя + фамилия
        :return:
        '''
        return self.name + " " + self.surname

    def get_total_income(self):
        '''
        сумма оклад + премия
        :return:
        '''
        return self._income.get('wage') + self._income.get('bonus')


SCRIPT_NAME, name_, surname_, position_, wage_, bonus_ = argv
user_one = Position(name_, surname_, position_, wage_, bonus_)
print(f"Сотрудник {user_one.get_full_name()}")
print(f"Имеет должность {user_one.position}")
print(f"Текущая зарплата {user_one.get_full_name()} на должности "
      f"{user_one.position} составляет {user_one.get_total_income()}")
