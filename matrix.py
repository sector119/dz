from typing import List


class Matrix:
    def __init__(self, matrix=None):
        if matrix is not None:
            self._matrix = matrix
        else:
            self._matrix = []

    def __iter__(self):
        for line in self._matrix:
            yield line

    def append(self, value: List[int]):
        return self._matrix.append(value)

    def find_and_swap(self):
        for row_idx in range(len(self._matrix)):
            max_idx = self._matrix[row_idx].index(max(self._matrix[row_idx]))

            self._matrix[row_idx][max_idx], self._matrix[row_idx][row_idx] = self._matrix[row_idx][row_idx], self._matrix[row_idx][max_idx]


def read_matrix():
    matrix = Matrix()

    with open('matrix.csv', 'r') as f:
        for line in f.readlines():
            items = line.strip().split(',')
            matrix.append([int(item) for item in items])

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    matrix = read_matrix()

    print_matrix(matrix)

    matrix.find_and_swap()

    print_matrix(matrix)


main()
