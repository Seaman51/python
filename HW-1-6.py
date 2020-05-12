a = float(input("Введите параметр a: "))
b = float(input("Введите параметр b: "))
day = 1
while True:
    print(f"{day}-й день: {a:.2f}")
    if a >= b:
        break
    else:
        a *= 1.1
        day += 1
