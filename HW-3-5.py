def list_sum(my_list):
    global my_list_sum
    for el in my_list:
        if el == 'q':
            break
        my_list_sum += float(el)
    return my_list_sum


my_list_sum = 0
while True:
    my_list = input('Введите числа разделенные пробелом, для выхода введите q ').split()
    print(f'Сумма чисел равна {list_sum(my_list)}')
    if my_list.count('q') > 0:
        break
print('Вы закончили выполнение программы')