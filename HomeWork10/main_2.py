# Домашняя работа по десятому семинару
# Задание № 2 Создать дескриптор для атрибутов классов, которые вы создали
# # ранее в ДЗ

class CorrectValues:

    def __set__(self, instance, value):
        if type(value) != int and type(value) != float:
            raise TypeError(
                f'Значение переменной {self.my_attr} не является числом')

        elif value < 0:
            raise ValueError(f'Значение переменной {self.my_attr}  менее нуля,'
                             f' а значит результат будет некоректен')
        else:
            instance.__dict__[self.my_attr] = value


class Worker:
    _wage = CorrectValues()
    _bonus = CorrectValues()

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


user_one = Position("Вася", "Веселый", "Могильщик", 40000, 666)
print(f"Сотрудник {user_one.get_full_name()}")
print(f"Имеет должность {user_one.position}")
print(f"Текущая зарплата {user_one.get_full_name()} на должности "
      f"{user_one.position} составляет {user_one.get_total_income()}")
user_two = Position("Петя", "Грустный", "Могильщик", 10000, "666")
print(f"Сотрудник {user_two.get_full_name()}")
print(f"Имеет должность {user_two.position}")
print(f"Текущая зарплата {user_two.get_full_name()} на должности "
      f"{user_two.position} составляет {user_two.get_total_income()}")
