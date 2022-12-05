# Домашняя работа по третьему семинару
# Задание № 1 Реализовать функцию, принимающую два числа (позиционные
# аргументы) и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def input_num(str_num, param_zero=999999):
    while True:
        get_number = input("Введите целое положительное число: ")
        if get_number.isdigit():
            return get_number


def oper(dividend, divisor):
    try:
        res_num = dividend / divisor
    except ZeroDivisionError:
        return "Вы еще не готовы к делению на ноль"
    return "Результат деления {dividend} ан {divisor} равен {oper}"


dividend = int(input_num("Введите делимое: "))
divisor = int(input_num("Введите делитель", 0))

print(oper(dividend, divisor))
