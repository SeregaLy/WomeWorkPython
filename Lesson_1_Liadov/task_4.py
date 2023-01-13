# Домашняя работа по одидцатому семинару
# Задание № 4 Преобразовать слова «разработка», «администрирование»,
# «protocol», «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).

import chardet

my_list = ['разработка', 'администрирование', 'protocol', 'standard']
my_list_bytes = []

for s in my_list:
    s = s.encode('utf-8', errors='namereplace')
    my_list_bytes.append(s)
    print(s)

for s in my_list_bytes:
    print(s.decode(chardet.detect(s)['encoding']))
