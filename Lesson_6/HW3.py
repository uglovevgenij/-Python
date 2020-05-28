"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""
class Worker:
    name = None
    surname = None
    position = None
    _income = {"wage": None, "bonus": None}

class Position(Worker):
    def get_full_name(self):
        self.name = input('Имя сотрудника: ')
        self.surname = input('Фамилия сотрудника: ')
        self.position = input('Должность: ')
        print('Имя: {}'
              '\n' 'Фамилия: {}'
              '\n' 'Должность: {}'.format(self.name, self.surname, self.position))

    def get_total_income(self):
        self._income.update({"wage": int(input('Оклад: ')), "bonus": int(input('Премия: '))})
        print('Итого выплата: {}'.format(sum(self._income.values())))


p = Position()
p.get_full_name()
p.get_total_income()