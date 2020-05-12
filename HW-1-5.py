receipt = float(input("Введите выручку: "))
costs = float(input("Введите затраты: "))
if receipt > costs:
    print(f"Вы работаете с прибылью! Ваша рентабельность {(receipt - costs) / receipt:.2%}")
    workers = int(input("Введите численность сотрудников: "))
    print(f"Прибыль на одного сотрудника составляет {(receipt - costs) / workers:.2f}")
else:
    print("Вы работаете с убытком!")
