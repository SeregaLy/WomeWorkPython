# Домашняя работа по третьему семинару
# Задание № 3 Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    if arg3 <= arg1 <= arg2 or arg3 <= arg2 <= arg1:
        return arg1 + arg2
    elif arg2 <= arg1 <= arg3 or arg2 <= arg3 <= arg1:
        return arg1 + arg3
    else:
        return arg2 + arg3


one_num = int(input("Введите первый аргумент "))
two_num = int(input("Введите второй аргумент "))
tree_num = int(input("Введите третий аргумент "))
print(f'Сумма наибольших аргументов = {my_func(one_num, two_num, tree_num)}')
