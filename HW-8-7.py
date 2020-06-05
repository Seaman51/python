class My_complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}{("+" if self.y >= 0 else "")}{self.y}j)'

    def __add__(self, other):
        return My_complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return My_complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)


a = My_complex(8, 2)
b = My_complex(2, -3)
c = My_complex(-3, 1)
a1 = complex(8, 2)
b1 = complex(2, -3)
c1 = complex(-3, 1)
print(f"Сумма равна {a + b + c}")
print(f'Проверка {a1 + b1 + c1}')
print(f"Произведение равно {a * b * c}")
print(f'Проверка {a1 * b1 * c1}')
