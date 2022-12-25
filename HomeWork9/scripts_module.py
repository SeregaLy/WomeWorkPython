from sys import argv
from itertools import count


def salary(arg_1, arg_2, arg_3):
    try:
        time = int(arg_1)
        salary = int(arg_2)
        bonus = int(arg_3)
        result = time * salary + bonus
        return result
    except ValueError:
        print('один из аргументов имеет не числовой формат')


def sum_two_max(arg_1, arg_2, arg_3):
    my_list = sorted([float(arg_1), float(arg_2), float(arg_3)], reverse=True)
    return my_list[0] + my_list[1]


def title_func(arg):
    return arg.title()


def gen_num(arg1, arg2):
    result_list = []
    for el in count(arg1):
        if el > arg2:
            break
        result_list.append(el)
    return result_list
