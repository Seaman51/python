number = int(input("Введите целое положительное число: "))
digit_max = 0
digit = 0
while number != 0 and digit != 9:
    digit = number % 10
    number = number // 10
    if digit > digit_max:
        digit_max = digit
print(f"Максимальная цифра в числе: {digit_max}")
