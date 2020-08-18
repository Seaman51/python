class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list, el = [], None
while el != 'stop':
    try:
        in_data = list(input('Введите число или числа через пробел, для выхода наберите stop - ').split())
        for el in in_data:
            if el == 'stop':
                break
            elif el.isdigit() == False:
                raise OwnError('Можно вводить только числа!')
            else:
                my_list.append(el)
    except OwnError as err:
        print(err)
print(f'Список корректно введенных значений: {my_list}')
