import json

my_dict_1 = {}
my_dict_2 = {}
try:
    with open('text_7.txt', 'r', encoding='utf-8') as f_obj:
        while True:
            line = f_obj.readline().split()
            if not line:
                break
            my_dict_1.update({line[0]: float(line[2]) - float(line[3])})
    my_dict_2.update({'average_profit': sum([int(el) for el in my_dict_1.values() if el > 0]) / len(
        [int(el) for el in my_dict_1.values() if el > 0])})
    with open('text_71.json', 'w', encoding='utf-8') as f_obj:
        json.dump([my_dict_1, my_dict_2], f_obj, ensure_ascii=False, indent=4)
except IOError:
    print('Произошла ошибка ввода-вывода!')
