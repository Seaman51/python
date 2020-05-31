class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки маркером')


obj1 = Stationery()
obj1.draw()
obj2 = Pen()
obj2.draw()
obj3 = Pencil()
obj3.draw()
obj4 = Handle()
obj4.draw()
