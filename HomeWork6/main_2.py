# Домашняя работа по пятому семинару
# Задание № 2 Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры
# времени, оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы
# сделали и чего удалось добиться
from timeit import timeit

a1, a2, a3 = 5, 6, 9


def my_func(arg1, arg2, arg3):
    '''
    Работа функции через витвления быстрее, но написание программы для более
    чем 3 аргументов займет гораздо больше времени
    :param arg1:
    :param arg2:
    :param arg3:
    :return:
    '''
    if arg3 <= arg1 <= arg2 or arg3 <= arg2 <= arg1:
        return arg1 + arg2
    elif arg2 <= arg1 <= arg3 or arg2 <= arg3 <= arg1:
        return arg1 + arg3
    else:
        return arg2 + arg3


def new_my_func(ar1, ar2, ar3):
    '''
    Работа функции через цикл имеет неоспоримое преимущество в неограниченности
    колличетсва аргументов на входе, но скорость выполнения становится больше

    :param ar1:
    :param ar2:
    :param ar3:
    :return:
    '''
    lst = [ar1, ar2, ar3]
    i = 0
    res = 0
    while i != 2:
        max_val = max(lst)
        res += max_val
        lst.remove(max_val)
        i += 1
    return res


print(f" Скорость выполнения функции через витвления :"
      f"{timeit('my_func(a1, a2, a3)', globals=globals())}")
print(f" Скорость выполнения функции через цикл :"
      f"{timeit('new_my_func(a1, a2, a3)', globals=globals())}")
