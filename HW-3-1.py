"""Вариант №1."""


def division_1(dividend, divider):
    if divider == 0:
        return 'Вариант №1 На ноль делить нельзя'
    else:
        return f'Вариант №1 Частное от деления {dividend} на {divider} равно {dividend / divider}'


"""Вариант №2."""


def division_2(dividend, divider):
    try:
        dividend / divider
    except ZeroDivisionError:
        return 'Вариант №2 На ноль делить нельзя'
    return f'Вариант №2 Частное от деления {dividend} на {divider} равно {dividend / divider}'


number_1 = float(input('Введите делимое '))
number_2 = float(input('Введите делитель '))
print(division_1(number_1, number_2))
print(division_2(number_1, number_2))
