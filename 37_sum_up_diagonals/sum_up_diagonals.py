def sum_diagonal(matrix, direction):
    if direction == 'lr':
        sum = 0
        for col, row in enumerate(matrix):
            sum = sum + row[col]

    elif direction == 'rl':
        sum = 0
        idx = len(matrix) - 1
        for col, row in enumerate(matrix):
            sum = sum + row[idx]
            idx = idx - 1

    return sum


def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    return sum_diagonal(matrix, 'lr') + sum_diagonal(matrix, 'rl')



# Given a matrix [square list of lists], return sum of diagonals.

# Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

m1 = [
    [1,   2],
    [30, 40],
]

print(sum_up_diagonals(m1))
# 73

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(sum_up_diagonals(m2))
# 30