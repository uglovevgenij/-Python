"""Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    title = None
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    title = 'Ручка'
    def draw(self):
        print('{} пишет.'.format(self.title))

class Pencil(Stationery):
    title = 'Карандаш'
    def draw(self):
        print('{} рисует.'.format(self.title))

class Handle(Stationery):
    title = 'Маркер'
    def draw(self):
        print('{} штрихует.'.format(self.title))



pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
