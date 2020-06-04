class Cell:
    def __init__(self, count_cells):
        self.count_cells = count_cells
        print(f'Клетка имеет {self.count_cells} ячеек')

    def __add__(self, other):
        return self.count_cells + other.count_cells

    def __sub__(self, other):
        return (
            self.count_cells - other.count_cells if self.count_cells >= other.count_cells else 'Операция некорректна')

    def __mul__(self, other):
        return self.count_cells * other.count_cells

    def __truediv__(self, other):
        return (
            self.count_cells // other.count_cells if self.count_cells / other.count_cells > 1 else 'Операция некорректна')

    def make_order(self, number):
        self.number = number
        return print(('').join([('*\n' if i % self.number == 0 else '*') for i in range(1, self.count_cells + 1)]))


obj1 = Cell(35)
obj1.make_order(8)
obj2 = Cell(24)
obj2.make_order(5)
print(f'Сумма = {obj1 + obj2}')
print(f'Разность = {obj1 - obj2}')
print(f'Произведение = {obj1 * obj2}')
print(f'Деление = {obj1 / obj2}')
