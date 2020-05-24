from sys import argv

try:
    script_name, hour, rate, bonus = argv
    print(f'Заработная плата составляет: {float(hour) * float(rate) + float(bonus)}')
except ValueError:
    print('Вы задали некорректные параметры!')
