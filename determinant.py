from functools import reduce
from itertools import permutations
from typing import List

SAMPLE_MATRIX_A: List[List[int]] = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
SAMPLE_MATRIX_B: List[List[int]] = [
    [3, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 2, 1],
    [0, 0, 0, 1]
]


def to_permutation_list(matrix_lenght) -> list:
    return list(permutations(range(matrix_lenght)))


def get_sign(matrix_list) -> int:
    count = 0
    for i in range(len(matrix_list)):
        for j in range(i + 1, len(matrix_list)):
            if matrix_list[i] > matrix_list[j]:
                count += 1
    return 1 if (count % 2) == 0 else -1


def calculate_determinant(matrix) -> int:
    ''' Get the determinant of the matrix.

    :param list[list[int]] matrix: Matrix to operate on.
    :return: An integer determinant.

    Note: This only works for square matrices.
    '''

    if len(matrix) != len(matrix[0]):
        raise Exception('Must be square')

    determinant = 0
    matrix_lenght = len(matrix)
    permutation_list = to_permutation_list(matrix_lenght)

    for value in permutation_list:
        signal = get_sign(value)
        product_diagonal_elements = reduce(
            lambda a1, a2: a1 * a2,
            [matrix[i][value[i]] for i in range(matrix_lenght)]
        )
        determinant += signal * product_diagonal_elements

    return determinant


if __name__ == '__main__':
    print(
        f'Determinante da matriz A {SAMPLE_MATRIX_A} = \
        {calculate_determinant(SAMPLE_MATRIX_A)}'
    )
    print(f'Determinante da matriz B {SAMPLE_MATRIX_B} = \
        {calculate_determinant(SAMPLE_MATRIX_B)}'
    )
