# Функция фебоначи, помогает продуть систему охлаждения ноутбука

def febo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return febo(x - 1) + febo(x - 2)


print(febo(45))
