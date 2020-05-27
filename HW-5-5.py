try:
    with open('text_5.txt', 'w', encoding='utf-8') as f_obj:
        f_obj.write(' '.join([str(el) for el in range(25)]))
    with open('text_5.txt', 'r', encoding='utf-8') as f_obj:
        print(f'Сумма чисел в файле равна: {sum([int(el) for el in f_obj.readline().split()])}')
except IOError:
    print('Произошла ошибка ввода-вывода!')
