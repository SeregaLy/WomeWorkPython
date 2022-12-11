# Домашняя работа по пятому семинару
# Задание № 1 Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# свидетельствует пустая строка.

file_creation = open('file_1.txt', 'r+')
line = input('Введите текст первой строки \n')
while line:
    file_creation.writelines(line)
    line = input('Введите текст следующей строки, либо закончите ввод введя '
                 'пустую строку \n')
    if not line:
        break

print_file_1 = file_creation.readlines()
print(f"Файл file_1.txt содержит текст: {print_file_1}")
file_creation.close()