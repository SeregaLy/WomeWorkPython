# Домашняя работа по одидцатому семинару
# Задание № 2 Каждое из слов «class», «function», «method» записать в байтовом
# типе без преобразования в последовательность кодов (не используя методы
# encode и decode) и определить тип, содержимое и длину соответствующих
# переменных.

import binascii

my_list = [b'class', b'function', b'method']

for s in my_list:
    print(f"Записать в байтовом типе: {binascii.hexlify(s)} тип {type(s)} "
          f"{binascii.hexlify(s)} содержимое {s} длина {len(s)}")
