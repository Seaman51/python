class Matrix:
    def __init__(self, my_m):
        self.my_m = my_m

    def __str__(self):
        return ('\n').join([str((' ')).join(map(str, el)) for el in self.my_m]) + '\n'

    def __add__(self, other):
        my_m = []

        def matrix_append(obj1, obj2):
            print(f'Размерность матриц не совпадает')
            for ii in range(len(obj1) - len(obj2)):
                obj2.append([0])
            return obj2

        def line_append(obj1, obj2):
            print('Размерность элементов матрицы не совпадает')
            for ii in range(len(obj1) - len(obj2)):
                obj2.append(0)
            return obj2

        if len(self.my_m) > len(other.my_m):
            matrix_append(self.my_m, other.my_m)
        if len(self.my_m) < len(other.my_m):
            matrix_append(other.my_m, self.my_m)

        for i in range(len(self.my_m)):

            if len(self.my_m[i]) > len(other.my_m[i]):
                line_append(self.my_m[i], other.my_m[i])
            if len(self.my_m[i]) < len(other.my_m[i]):
                line_append(other.my_m[i], self.my_m[i])

            my_m.append(list(map(lambda x, y: x + y, self.my_m[i], other.my_m[i])))

        return Matrix(my_m)


matrix_1 = Matrix([[11, 15, 18], [13, 14, 15], [15, 16, 15]])
matrix_2 = Matrix([[17], [19, 10, 15], [11, 12, 15]])
matrix_3 = Matrix([[12, 19, 17], [14, 15]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
print(matrix_3)
print(matrix_1 + matrix_3)
print(matrix_1 + matrix_2 + matrix_3)
