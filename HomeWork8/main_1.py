# Домашняя работа по восьмому семинару
# Задание № 1 Реализовать класс Matrix (матрица). Обеспечить перегрузку
# конструктора класса (метод init()), который должен принимать данные (список
# списков) для формирования матрицы.
# [[], [], []]
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.output = ''
        self.matrix_out = []
        self.temporary = []
        self.lines_storage = []

    def __str__(self):
        for line in self.matrix:
            self.output += str(line) + '\n'
        return self.output + '\n'

    def __add__(self, other):
        for line in range(0, len(self.matrix)):
            self.lines_storage = []
            for el in range(0, len(self.matrix[line])):
                self.temporary = self.matrix[line][el] + other.matrix[line][el]
                self.lines_storage.append(self.temporary)
            self.matrix_out.append(self.lines_storage)
        return Matrix(self.matrix_out)


first_mat = [
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, 8]
]

second_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, ]
]

one = Matrix(first_mat)
print(one)

two = Matrix(second_matrix)
print(two)

sum_of_matri = one + two
print(sum_of_matri)
