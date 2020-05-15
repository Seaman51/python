count = int(input('Введите количество элементов '))
start_list = []
finish_list = []
for i in range(count):
    start_list.append(int(input(f'Введите {i + 1} элемент ')))
print(f'Исходный список {start_list}')
for i in range(0, count, 2):
    finish_list.extend(reversed(start_list[i:i + 2]))
print(f'Итоговый список {finish_list}')
