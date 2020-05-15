user = input('Введите строку из нескольких слов, разделённых пробелами ')
slova = user.split()
for i in range(len(slova)):
    print(f'{i + 1} {slova[i][:10]}')
