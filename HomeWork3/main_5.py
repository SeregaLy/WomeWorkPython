# Задание № 5 Программа запрашивает у пользователя строку чисел, разделенных
# пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь
# может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма
# вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
# вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

def sum_num():
    result = 0
    flag = False
    while flag == False:
        number = input('Введите числа через пробел, для выхода из программы '
                       'введите - q: ').split()
        sum_num = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                flag = True
                break
            else:
                sum_num += int(number[el])
        result += sum_num
        print(f'Сумма введеных цифр ровна: {result}')
    print(f'Программа окончена. Сумма введеных цифр ровна: {result}')


sum_num()