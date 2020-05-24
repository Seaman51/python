from functools import reduce

print(reduce(lambda arg_1, arg_2: arg_1 * arg_2, [el for el in range(100, 1001) if el % 2 == 0]))
