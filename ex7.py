import random

x, y = 10, 10
f, t = 0, 100


def pprint_matrix(matrix):
    for row in matrix:
        for col in row:
            print(f'{str(col):>5}', end='')
        print()


matrix = []

for _ in range(y):
    matrix.append([random.randint(f, t) for _ in range(x)])

pprint_matrix(matrix)

matrix2 = []

for i in range(0, x):
    matrix2.append(
        [
            j not in (0, y - 1)
                and (matrix[i][j - 1] + matrix[i][j + 1]) / 2
                or matrix[i][j]
            for j in range(0, y)
        ]
    )

pprint_matrix(matrix2)
