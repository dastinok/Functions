# Транспонирование матрицы
# В линейной алгебре транспонирование матрицы-это оператор, который переворачивает матрицу по ее диагонали;
# то есть он переключает индексы строк и столбцов матрицы A, создавая другую матрицу, часто обозначаемую AT
# (среди других обозначений).
matrix = [[3,10,9],
            [34,3,0],
            [38,8,1],
            [56,78,90]]

print('Начальная матрица')
for m in matrix:
    print(m)


matrix_change = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]


def get_trans(matrix_a: list[list], matrix_trans: list[list]) -> list:
    for i in range(len(matrix_a)):
        for b in range(len(matrix_a[0])):
            matrix_trans[b][i] = matrix_a[i][b]
    return matrix_trans

print('Транспортирование матрицы')
transport = get_trans(matrix,matrix_change)
for i in transport:
    print(i)

