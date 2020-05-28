"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    speed = None
    color = None
    name = None
    is_police = None #вставить булевое значение

    def go(self):
        print('Автомобиль стартовал.')

    def stop(self):
        print('Автомобиль остановлен.')

    def turn(self, l='L', r='R'):
        if l == 'L':
            print('Поворот налево!')
        elif r == 'R':
            print('Поворот направо!')

    def show_speed(self):
        print('Скорость автомобиля: {} км/ч.'.format(self.speed))

# Ниже был добавлен еще один метод не из условий задачи, отвечающий за постоянный запрос
    # действий от водителя для управления автомобилем.
    def car_action(self):
        print('Автомобиль: {}''\n'
              'Цвет: {}'.format(self.name, self.color))
        if self.is_police == True:
            print('Служебный полицейский автомобиль.')
        while True:
            x = input('G - запуск, Q - выход.''\n'
                      'Введите действие: ')  # переменная, обозначающая действия
            if x == 'G':
                self.go()
                self.speed = int(input('Укажите скорость: '))
                self.show_speed()
                while True:
                    x = input('S - стоп, L - влево, R - вправо, SPEED - скорость. ''\n'
                              'Введите действие: ')  # переменная, обозначающая действия
                    if x == 'S':
                        self.stop()
                        break
                    elif x == 'SPEED':
                        try:
                            self.speed = int(input('Укажите скорость: '))
                            self.show_speed()
                        except:
                            print('Не верная команда!')
                    elif x == 'L':
                        self.turn('L')
                    elif x == 'R':
                        self.turn('R')
                    else:
                        print('Не верная команда!')
            elif x == 'Q':
                print('Вы вышли из автомобиля.')
                break
            else:
                print('Не верная команда!')


class TownCar(Car):
    def show_speed(self):
        print('Скорость автомобиля: {} км/ч.'.format(self.speed))
        if self.speed >= 60:
            print('Скорость превышена!')

    def action(self):
        self.name = 'TownCar'
        self.color = 'Green'
        self.car_action()

class SportCar(Car):
    def action(self):
        self.name = 'SportCar'
        self.color = 'Red'
        self.car_action()

class WorkCar(Car):
    def show_speed(self):
        print('Скорость автомобиля: {} км/ч.'.format(self.speed))
        if self.speed >= 40:
            print('Скорость превышена!')
    def action(self):
        self.name = 'WorkCar'
        self.color = 'Yellow'
        self.car_action()

class PoliceCar(Car):
    def action(self):
        self.name = 'PoliceCar'
        self.color = 'Black'
        self.is_police = True
        self.car_action()

qwe = input('Выбор автомобиля.''\n'
      'TownCar - t, WorkCar - w, SportCar - s, PoliceCar - p: ')
if qwe == 't':
    t = TownCar()
    t.action()
elif qwe == 's':
    t = SportCar()
    t.action()
elif qwe == 'w':
    t = WorkCar()
    t.action()
elif qwe == 'p':
    p = PoliceCar()
    p.action()