my_items = []
my_item = ()
specifications = {}
analytics = {}
for i in range(3):
    name_item = input(f'Введите название {i + 1} товара ')
    price = float(input(f'Введите цену {i + 1} товара '))
    count = int(input(f'Введите количество {i + 1} товара '))
    unit = input(f'Введите единицы изверения {i + 1} товара ')
    specifications = {"название": name_item, "цена": price, "количество": count, "ед": unit}
    my_item = (i + 1, specifications)
    my_items.append(my_item)
print('Данные "Товары"')
for i in my_items:
    print(i)
# для проверки
# my_items = [
#    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт."}),
#    (2, {"название": "принтер", "цена": 6000, "количество": 2, "ед": "шт."}),
#    (3, {"название": "сканер", "цена": 2000, "количество": 7, "ед": "шт."}),
#    (4, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт."})
# ]
for key in list(my_items[1][1].keys()):
    temp = set()
    for item in my_items:
        temp.add(item[1].get(key))
        analytics[key] = list(temp)
print(f'Словарь: {analytics}')
