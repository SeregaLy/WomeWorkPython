# Домашняя работа по семинару 1

bal = 10
print(bal)
bals = input("Задание 1. Веедите число: ")
print(f"Вы ввели {bals}")

SEKONDTOH = 360
SEKONDTOMIN = 60
secondTime = int(input("Задание 2. Введите время в секундах: "))
hTime = secondTime // SEKONDTOH
mTime = (secondTime - hTime * SEKONDTOH) // SEKONDTOMIN
sTime = secondTime % SEKONDTOMIN
print(f"{hTime} : {mTime} : {sTime}")

magicNumber = input("Задание 3. Введите целое положительное число: ")
doubleMagicNumber = magicNumber + magicNumber
tripleMagicNumber = magicNumber + magicNumber + magicNumber
sumMagicNumber = int(magicNumber) + int(doubleMagicNumber) + int(tripleMagicNumber)
print(f"Считаем {magicNumber} + {doubleMagicNumber} + {tripleMagicNumber} = {sumMagicNumber}")

MAXNUM = 9
DEC = 10
userNumber = int(input("Задание 4. Введите целое положительное число: "))
maxNumber = userNumber % DEC
while userNumber >= 1:
    userNumber = userNumber // DEC
    if userNumber % DEC > maxNumber:
        maxNumber = userNumber % DEC
    elif userNumber % DEC == MAXNUM:
        maxNumber = MAXNUM
        break
print(f"Максимальное цифра в числе {maxNumber}")

revenueUser = int(input("Задание 5. Введите выручку предприятия: "))
lesionUser = int(input("Введите значение убытка предприятия: "))
if lesionUser > revenueUser:
    print("Предприятие убыточно")
elif lesionUser == revenueUser:
    print("У предприятия отсутствует прибыль")
else:
    cleanRevenue = revenueUser - lesionUser
    print(f"чиcтая прибыль предприятия {cleanRevenue}")
    numberEmployees = int(input("Укажите колличество сотрудников: "))
    revenueEmployees = cleanRevenue / numberEmployees
    print(f"Чистая прибыль предприятия в пересчете на одного сотрудника: {revenueEmployees}")

PROGRESS = 1.1
startDistance = int(input("Pадание 6. Введите дистанцию спортсмена в первый день: "))
finishDistance = int(input("Введите цель спортсмена: "))
countDay = 1
while startDistance <= finishDistance:
    startDistance *= PROGRESS
    if startDistance * PROGRESS >= finishDistance:
        countDay += 1
        break
    else:
        countDay += 1
print(f"Цель спортсмена будет достигнута на {countDay}")
