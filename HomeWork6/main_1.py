# Домашняя работа по пятому семинару
# Задание № 1 Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры
# времени, оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы
# сделали и чего удалось добиться

from timeit import timeit

USER_X = 5
USER_Y = 4


def num_pow(x, y):
    '''
    функция выполняет возведение числа x в степень y
    :param x: основание
    :param y:степень
    :return: основание х возведеное в степень у
    '''
    return x ** y


def new_num_pow(x, y):
    '''
        функция выполняет возведение числа x в степень y
        :param x: основание
        :param y:степень
        :return: основание х возведеное в степень у
        '''
    return pow(x, y)


print(f" Скорость выполнения самодельной функции :"
      f"{timeit('num_pow(USER_X,USER_Y)', globals=globals())}")
print(f"Cкорость выполнения функции pow() находящейся в функции :"
      f"{timeit('new_num_pow(USER_X,USER_Y)', globals=globals())}")
print(f"Cкорость выполнения функции pow() :"
      f"{timeit('{pow(USER_X, USER_Y)}', globals=globals())}")
'''
функция pow() имеет удобную короткую запись, но медленнее **

'''
