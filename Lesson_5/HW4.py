"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в
новый текстовый файл.

"""
my_f = open("HW4.txt", "r")
my_f2 = open("HW4_1.txt", "w", encoding='utf-8') #создаем новый текстовый файл
my_f2.close()

for line in my_f:
    a = line.split(' ')
    b = int(a[2])
    if b == 1:
        a.insert(0, 'Один')
        a.pop(1)
        with open('HW4_1.txt', 'a', encoding='utf-8') as file:
            a = ' '.join(a)
            file.write(a)  #сохраняем переименованную строку в новый файл
    if b == 2:
        a.insert(0, 'Два')
        a.pop(1)
        with open('HW4_1.txt', 'a', encoding='utf-8') as file:
            a = ' '.join(a)
            file.write(a)
    if b == 3:
        a.insert(0, 'Три')
        a.pop(1)
        with open('HW4_1.txt', 'a', encoding='utf-8') as file:
            a = ' '.join(a)
            file.write(a)
    if b == 4:
        a.insert(0, 'Четыре')
        a.pop(1)
        with open('HW4_1.txt', 'a', encoding='utf-8') as file:
            a = ' '.join(a)
            file.write(a)

my_f.close()

#