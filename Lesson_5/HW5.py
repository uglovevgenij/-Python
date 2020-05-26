"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
#создаем функцию reduce
from functools import reduce
def my_func(prev_el, el):
    return int(prev_el) + int(el)

#Вводим значения строкой в нофый файл
my_f2 = open("HW5.txt", "w")
a = ' '.join(input('Введите числа через пробел: ').split())
my_f2.write(a)
my_f2.close()

#Выводим сумму чисел через reduce
with open('HW5.txt') as file:
    for line in file:
        a = line.split(' ')
        print('Сумма чисел:', reduce(my_func, a))
