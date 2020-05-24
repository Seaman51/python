def fact(n):
    factorial = 1
    for el in range(n):
        factorial = factorial * (el + 1)
        yield el, factorial


n = 4

for el in fact(n):
    print(f'Результат: {(el[0] + 1)}! = {el[1]}')
print(type(fact(n)))

line = str(n) + '! = '
for el in fact(n):
    line = line + str(el[0] + 1) + ' * '
    factorial = el[1]
print(f'{line[:-2]} = {factorial}')
