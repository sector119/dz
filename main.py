from typing import Generator, Optional, List


class Matrix:
    def __init__(self, matrix: Optional[list] = None):
        if matrix is not None:
            self._matrix = matrix
        else:
            self._matrix = []

    def __iter__(self) -> Generator:
        for line in self._matrix:
            yield line

    def append(self, value: List[int]):
        return self._matrix.append(value)

    # def find_specials(self) -> Generator:
    #     for col_idx in range(len(self._matrix[0])):
    #         for row_idx in range(len(self._matrix)):
    #             special = self._matrix[row_idx][col_idx]
    #
    #             if special > sum([self._matrix[i][col_idx] for i in range(len(self._matrix))]) - special:
    #                 yield col_idx, special

    def find_specials(self) -> Generator:
        sum_list = [sum(i) for i in zip(*self._matrix)]

        for col_idx in range(len(self._matrix[0])):
            for row_idx in range(len(self._matrix)):
                special = self._matrix[row_idx][col_idx]

                if special > sum_list[col_idx] - special:
                    yield col_idx, special
                    break


def read_matrix() -> Matrix:
    matrix = Matrix()

    with open('data.txt', 'r') as f:
        for line in f.readlines():
            items = line.strip().split(', ')

            matrix.append([int(item) for item in items])

    return matrix


def main():
    matrix = read_matrix()

    for row in matrix:
        print(row)

    for col, special in matrix.find_specials():
        print(f'col {col} has special item {special}')


main()
