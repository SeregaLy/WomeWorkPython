# Сортировка пузырьком

oldlist = [10, 75, 43, 15, 25, -4, 27]


def bublesort(mylist, ):
    last_item = len(mylist) - 1
    for z in range(0, last_item):
        for x in range(0, last_item - z):
            if mylist[x] > mylist[x - 1]:
                mylist[x], mylist[x + 1] = mylist[x + 1], mylist[x]
    return mylist


print(f"Old list: {oldlist}")
newlist = bublesort(oldlist).copy()
print(f"New list: {newlist}")
