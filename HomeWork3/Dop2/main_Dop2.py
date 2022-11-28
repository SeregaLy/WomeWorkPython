# Домашняя работа по третьему семинару
# Задание Дополнительное № 1_2 Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний элемент, второй и
# предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mult_lst(user_lst):
    len_lst = len(user_lst)//2 + 1 if len(user_lst) % 2 != 0 \
        else len(user_lst)//2
    new_lst = [user_lst[i]*user_lst[len(user_lst)-i-1] for i in range(len_lst)]
    print(new_lst)

user_lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(user_lst)