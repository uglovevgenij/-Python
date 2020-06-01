"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __add__(self, my_other):
        self.test_list1 = []
        self.test_list2 = []
        self.my_other = my_other
        for x, y in zip(self.my_list, self.my_other):
            for a, b in zip(x, y):
                self.test_list1.append(a + b)
            self.test_list2.append(self.test_list1)
            self.test_list1 = []
        self.my_list = self.test_list2
        return self.my_list

    def __str__(self):
        matr = str()
        i = 0
        while i < len(self.my_list):
            matr = matr + '\t'.join(str(j) for j in self.my_list[i]) + '\n' * 2
            i += 1
        return matr


m = Matrix([[1, 2, 3], [2, 3, 4], [5, 6, 7]])
print(m)
my_other = [[3, 4, 5], [6, 7, 8], [9, 0, 7]]
m + my_other
print(m)