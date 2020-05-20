"""Вариант №1."""


def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    arg_max = max(my_list)
    my_list.remove(arg_max)
    return arg_max + max(my_list)


"""Вариант №2."""


def my_func_1(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    return sum(my_list) - min(my_list)


"""Вариант №3."""


def my_func_2(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()
    return sum(my_list[1:3])


number_1 = float(input('Введите первое число '))
number_2 = float(input('Введите второе число '))
number_3 = float(input('Введите третье число '))
print(f'Вариант №1 Сумма двух наибольших чисел равна {my_func(number_1, number_2, number_3)}')
print(f'Вариант №2 Сумма двух наибольших чисел равна {my_func_1(number_1, number_2, number_3)}')
print(f'Вариант №3 Сумма двух наибольших чисел равна {my_func_2(number_1, number_2, number_3)}')
