# Изучаю бинарный поиск при помощи рекурсии

my_list = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]


def binaryserch(list, my_x, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if my_x == list[mid]:
            return mid
        elif my_x < list[mid]:
            return binaryserch(list, my_x, start, mid - 1)
        else:
            return binaryserch(list, my_x, mid + 1, stop)

my_x = 20
x = binaryserch(my_list, my_x, 0, len(my_list))

if x == False:
    print(f"Item {my_x} not found!")
else:
    print(f"Item {my_x} found at index {x}")