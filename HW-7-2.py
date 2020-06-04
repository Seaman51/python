from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def my_title(self):
        print(f'My title - {self.title}')


class Coat(Clothes):
    def __init__(self, size, title='Пальто'):
        super().__init__(title)
        self.size = size
        self.consumption = self.size / 6.5 + 0.5

    def my_title(self):
        print(f'My title - {self.title}')

    @property
    def fabric_consumption(self):
        print(f'Расход ткани на {self.title} {self.size} размера равен {round(self.consumption, 2)}')


class Suit(Clothes):
    def __init__(self, growth, title='Костюм'):
        super().__init__(title)
        self.growth = growth
        self.consumption = 2 * self.growth + 0.3

    def my_title(self):
        print(f'My title - {self.title}')

    def fabric_consumption(self):
        print(f'Расход ткани на {self.title} {self.growth} размера равен {round(self.consumption, 2)}')


obj1 = Coat(50)
obj1.my_title()
obj1.fabric_consumption

obj2 = Suit(52)
obj2.my_title()
obj2.fabric_consumption()

obj3 = Suit(60)
obj3.my_title()
obj3.fabric_consumption()

print(f'Общий расход составил: {round(obj1.consumption + obj2.consumption + obj3.consumption, 2)}')
