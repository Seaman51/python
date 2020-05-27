my_dict = {}
try:
    with open('text_6.txt', 'r', encoding='utf-8') as f_obj:
        while True:
            line = f_obj.readline().split()
            if not line:
                break
            for el in line[1:]:
                if el == '-':
                    line.remove(el)
                for garbage in ['(пр)', '(л)', '(лаб)']:
                    if el.find(garbage) > 0:
                        line[line.index(el)] = el[:el.find(garbage)]
            my_dict.update({line[0]: sum([int(el) for el in line[1:]])})
        print(my_dict)
except IOError:
    print('Произошла ошибка ввода-вывода!')
