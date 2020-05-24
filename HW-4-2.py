source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список: {source_list}')
"""Вариант №1."""
print(
    f'Вариант №1 {[el for el in source_list if source_list.index(el) > 0 and source_list[source_list.index(el)] > source_list[source_list.index(el) - 1]]}')
"""Вариант №2."""
print(f'Вариант №2 {[el for i, el in enumerate(source_list) if i > 0 and source_list[i] > source_list[i - 1]]}')
