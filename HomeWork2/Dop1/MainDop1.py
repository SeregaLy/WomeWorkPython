# Домашняя работа по второму семинару
# Дополнительное задание №1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

DEC = 10
userNumber = input("Введите вещественное число: ")
x = userNumber.split(".")
chelaPart = int(x[0])
fractionalPart = int(x[1])
numbersSuma = 0
while chelaPart > 0:
    digit = chelaPart % DEC
    numbersSuma += digit
    chelaPart //= DEC
while fractionalPart > 0:
    digit = fractionalPart % DEC
    numbersSuma += digit
    fractionalPart //= DEC
print(f"Сумма чисел входящих в состав введеного числа ровна: {numbersSuma}")
