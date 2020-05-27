try:
    with open('text_1.txt', 'w', encoding="utf-8") as f_obj:
        while True:
            my_string = input("Введите данные, для выхода оставте пустую строку: ")
            if not my_string:
                break
            f_obj.write(my_string + '\n')
except IOError:
    print('Произошла ошибка ввода-вывода!')
