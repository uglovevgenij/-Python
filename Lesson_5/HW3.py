"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""

my_f = open("HW3.txt", "r")

all_money = 0  # сумма дохода отстающих сотрудников
num = 0  # количество отстающих сотрудников
print('Сотрудники с заработком ниже 20 т.:')
for line in my_f:
    a = line.split(' ')
    b = float(a[1])
    if b <= 20000:
        all_money += b
        num += 1
        print(a[0]) #выводим фамилию сотрудника

mid_money = all_money / num  #их средний доход

print('Средний заработок отстающего сотрудника: {}'.format(mid_money))

my_f.close()


#Приведен пример подсчета средней величины дохода сотрудников, которые зарабатывают менее 20 тыс.