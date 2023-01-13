# Програмка для ограничения обьема и колличества файлов

import shutil
import os
import sys

# PurgeLog.py mylog.txt 10 5
if (len(sys.argv) < 4):
    print("Missing arguments! Usage is script.py 10 5")
    exit(1)
file_name = sys.argv[1]  # первый аргумент вызова имя файла
limitsize = int(sys.argv[2])  # второй аргумент вызова обьем файла
logsnumber = int(sys.argv[
                     3])  # третий аргумент вызова максимальное количество создаваемых файлов

if (os.path.isfile(file_name) == True):
    logfile_size = os.stat(file_name).st_size  # запрашиваем размер файла
    logfile_size = logfile_size / 1024  # переводим размер в килобайты

    if (logfile_size >= limitsize):
        if (logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):
                src = file_name + "_" + str(currentFileNum - 1)
                dst = file_name + "_" + str(currentFileNum)
                if (os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print(f"Copied: {src} to {dst}")

            shutil.copyfile(file_name, file_name + "_1")  #
            print(f" {file_name} to {file_name} + '_1'")  #
        myfile = open(file_name, "w")  # обнуляем файл
        myfile.close()  # закрываем файл
