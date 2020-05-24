source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Исходный список: {source_list}')
print(f'Результат: {[el for el in source_list if source_list.count(el) == 1]}')
