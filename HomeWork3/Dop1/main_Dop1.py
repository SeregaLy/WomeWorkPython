# Домашняя работа по третьему семинару
# Задание Дополнительное № 1_1 Задайте список из нескольких чисел. Напишите
# программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_num_index(user_lst):
    """
    :param lst: пользовательский список
    :return: возвращает сообщение в консоль с суммой элементов списка, стоящих
    на нечётных позициях.
    """
    sum_num = 0
    for i in range(0, len(user_lst)):
        if i % 2 != 0:
            sum_num += user_lst[i]
    print(f"Сумма элементов списка на нечётных позициях ровна: {sum_num}")


user_lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_num_index(user_lst)
