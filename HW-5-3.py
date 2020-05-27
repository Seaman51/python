try:
    with open('text_3.txt', 'r', encoding='utf-8') as f_obj:
        fond = 0
        while True:
            user = f_obj.readline().split()
            if not user:
                break
            fond += float(user[1])
            if float(user[1]) < 20000:
                print(f'{user[0]} имеет оклад {user[1]}, что меньше 20 тыс.')
        f_obj.seek(0)
        print(f'Средняя величина дохода сотрудников составляет {fond / len(f_obj.readlines())}')
except:
    print('Произошла ошибка ввода-вывода!')
