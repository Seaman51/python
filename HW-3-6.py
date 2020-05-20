def my_word_up(my_word):
    return str(chr(ord(my_word[0]) - 32)) + my_word[1:]


flag = 1
while flag == 1:
    my_line = input('Введите строку из слов записанных маленькими латинскими буквами разделенных пробелами ').split()
    for i, my_word in enumerate(my_line):
        for el in my_word:
            flag = 0
            if ord(el) < 97 or ord(el) > 122:
                flag = 1
                break
        if flag == 1:
            break
        else:
            my_line[i] = my_word_up(my_word)
print(f"Результирующая строка {' '.join(my_line)}")
