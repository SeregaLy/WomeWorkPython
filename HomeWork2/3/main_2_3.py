# Домашняя работа по второму семинару
# Задание №3 Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить
# к какому времени года относится месяц (зима, весна, лето, осень). Напишите
# решения через list и через dict.

seasonsList = [None, 'Зима', 'Зима', 'Весна', 'Весна', 'Весна',
               'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень',
               'Зима']
seasonsDict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна',
               6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
               10: 'Осень', 11: 'Осень', 12: 'Зима'}
month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if month != 1 and month != 2 and month != 3 and month != 4 and month != 5 \
        and month != 6 and month != 7 and month != 8 and month != 9 \
        and month != 10 and month != 11 and month != 12:
    print("Ввод не соответствует критерию: целое число от 1 до 12 ")
else:
    print(seasonsDict.get(month))
    print(seasonsList[month])
