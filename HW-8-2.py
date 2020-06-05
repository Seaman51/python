class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    in_data = list(map(float, input('Введите делимое и делитель через пробел - ').split()))
    if in_data[1] == 0:
        raise OwnError('На ноль делить нельзя!')
except ValueError:
    print('Можно вводить только числа!')
except OwnError as err:
    print(err)
else:
    print(f'Частное от деления {in_data[0]} на {in_data[1]} равно {round(in_data[0] / in_data[1], 2)}')
