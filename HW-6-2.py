class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Длина дороги {self._length} м при ширине {self._width} м')

    def weight(self, weight_base=25, thickness=5):
        self.weight_base = weight_base
        self.thickness = thickness
        self.wight = self._length  * self._width * weight_base * thickness / 1000
        print(
            f'Масса асфальтового полотна при плотности {self.weight_base} кг/м2 и толщине покрытия {self.thickness} см равна {self.wight} т')


my_road = Road(5000, 20)
my_road.weight()
my_road.weight(20, 4)
