# Домашняя работа по второму семинару
# Задание №2 Для списка реализовать обмен значений соседних элементов, т.е.
# значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При
# нечетном количестве элементов последний сохранить на своем месте. Для
# заполнения списка элементов необходимо использовать функцию input().

countList = int(input("Введите количество элементов списка: "))
newList = []
i, index = 0, 0
while i < countList:
    newList.append(input(f"Введите значение элемента списка {i + 1}: "))
    i += 1

for elem in range(int(len(newList) / 2)):
    newList[index], newList[index + 1] = newList[index + 1], newList[index]
    index += 2
print(f"{newList}")
