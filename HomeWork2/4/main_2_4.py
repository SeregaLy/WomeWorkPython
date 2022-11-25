# Домашняя работа по второму семинару
# Задание №4 Пользователь вводит строку из нескольких слов, разделённых
# пробелами. Вывести каждое слово с новой строки. Строки необходимо
# пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

MAXLEN = 10
userString = input("Введите строку из нескольких слов, разделённых пробелами:")
wordInString = []
for index in range(userString.count(' ') + 1):
    wordInString = userString.split()
    if len(str(wordInString)) <= MAXLEN:
        print(f" {index + 1} {wordInString[index]}")
    else:
        print(f" {index + 1} {wordInString[index][0:MAXLEN]}")
