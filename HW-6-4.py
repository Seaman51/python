class Car:
    def __init__(self, name, color, is_police=False, speed=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(
            f'\n{"Полицейская" if self.is_police == True else "Обычная"} машнина {self.name} {self.color} скорость {self.speed} км/ч')

    def go(self, speed):
        self.speed = int(speed)
        print(f'{"Полицейская" if self.is_police == True else "Обычная"} машнина {self.name} {self.color} поехала')

    def stop(self):
        self.speed = int(0)
        print(f'{"Полицейская" if self.is_police == True else "Обычная"} машнина {self.name} {self.color} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(
            f'{"Полицейская" if self.is_police == True else "Обычная"} машнина {self.name} {self.color} повернула {self.direction}')

    def show_speed(self):
        print(
            f'{"Полицейская" if self.is_police == True else "Обычная"} машнина {self.name} {self.color} текущая скорость автомобиля {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        print(
            f'{"Полицейская" if self.is_police == True else "Обычная"} машнина {self.name} {self.color} текущая скорость автомобиля в городе {self.speed} км/ч')
        if float(self.speed) > 60:
            print(f'Вы превышаете разрешенную в городе скорость!')


class WorkCar(Car):

    def show_speed(self):
        print(
            f'{"Полицейская" if self.is_police == True else "Обычная"} машнина {self.name} {self.color} текущая скорость рабочего автомобиля {self.speed} км/ч')
        if float(self.speed) > 40:
            print(f'Вы превышаете разрешенную в городе скорость!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


auto1 = TownCar('Mazda', 'синяя')
auto1.go(70)
auto1.show_speed()
auto1.turn('налево')
auto1.stop()
auto1.show_speed()

auto2 = WorkCar('Mercedes', 'красная')
auto2.go(50)
auto2.show_speed()
auto2.turn('направо')
auto2.stop()
auto2.show_speed()

auto3 = SportCar('Porsche', 'черная')
auto3.go(100)
auto3.show_speed()
auto3.turn('налево')
auto3.stop()
auto3.show_speed()

auto4 = PoliceCar('Ford', 'белая', True)
auto4.go(80)
auto4.show_speed()
auto4.turn('направо')
auto4.stop()
auto4.show_speed()
