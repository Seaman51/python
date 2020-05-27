try:
    with open('text_2.txt', 'r', encoding='utf-8') as f_obj:
        line_count = 0
        for line in f_obj:
            line_count += 1
            print(f'В {line_count}-й строке {len(line.split())} слова')
        print(f'Файл содержит {line_count} строки')
except:
    print('Произошла ошибка ввода-вывода!')
