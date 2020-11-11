matrix = [[1, 2, 3, 4, -5], [2, 5, 5, 5, 5], [1, 5, 1, 4, 4], [4, 5, 4, 4, 4], [1, 5, -1, 4, 1]]

for r in matrix:
    print(r)

for i, row in enumerate(matrix):
    if row == [r[i] for r in matrix]:
        # print(f'row {i} == col {i}')
        print('row ' + str(i) + ' == col ' + str(i))

    # if len([e for e in row if e < 0]):
    if len(list(filter(lambda e: e < 0, row))):
        # print(f'row {i} has negative element and sum: {sum(row)}')
        print('row ' + str(i) + ' has negative element and sum: ' + str(sum(row)))
