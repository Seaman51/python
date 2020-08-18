class Storage:
    def __init__(self, title):
        self.title = title
        self.item = {}


class Office_equipment:
    def __init__(self, brand, series, color, type):
        self.type = type
        self.brand = brand
        self.series = series
        self.color = color

    def get_info(self):
        return f'{self.type.title()} {self.brand} {self.series} {"цветной" if self.color == True else "черно-белый"}'


class Printer(Office_equipment):
    def __init__(self, brand, series, color, net, type='принтер'):
        super().__init__(brand, series, color, type)
        self.net = net

    def get_info(self):
        return f'{self.type.title()} {self.brand} {self.series} {"цветной" if self.color == True else "черно-белый"} {"сетевой" if self.net == True else "локальный"}'


class Scanner(Office_equipment):
    def __init__(self, brand, series, color, format, type='сканер'):
        super().__init__(brand, series, color, type)
        self.format = format

    def get_info(self):
        return f'{self.type.title()} {self.brand} {self.series} {"цветной" if self.color == True else "черно-белый"} {"формат А3" if self.format == True else "формат А4"}'


class Xerox(Office_equipment):
    def __init__(self, brand, series, color, technology, type='ксерокс'):
        super().__init__(brand, series, color, type)
        self.technology = technology

    def get_info(self):
        return f'{self.type.title()} {self.brand} {self.series} {"цветной" if self.color == True else "черно-белый"} {"цифровой" if self.technology == True else "аналоговый"}'


obj1 = Printer('HP', 'LaserJet', False, False)
print(obj1.get_info())
obj2 = Scanner('Mustek', '1200', True, False)
print(obj2.get_info())
obj3 = Xerox('Xerox', '5500', True, False)
print(obj3.get_info())
