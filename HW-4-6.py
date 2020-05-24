from sys import argv
from itertools import count, cycle

try:
    script_name, number_start, number_count = argv
    for el in count(int(number_start)):
        if el > int(number_start) + 10:
            break
        print(el)
    с = 0
    for el in cycle(["A", "B", "C"]):
        if с > abs(int(number_count)):
            break
        print(el)
        с += 1
except ValueError:
    print('Вы задали некорректные параметры!')
