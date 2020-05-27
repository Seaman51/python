translate = {'One': 'Один ', 'Two': 'Два ', 'Three': 'Три ', 'Four': 'Четыре '}
try:
    with open('text_4.txt', 'r', encoding='utf-8') as load_obj:
        with open('text_4_1.txt', 'w', encoding='utf-8') as save_obj:
            while True:
                line = load_obj.readline().split()
                if not line:
                    break
                save_obj.write(''.join(translate.get(line[0])) + ' '.join(line[1:]) + '\n')
except IOError:
    print('Произошла ошибка ввода-вывода!')
