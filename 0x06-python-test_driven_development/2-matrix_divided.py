#!/usr/bin/python3
""" Function that divides all elements in a matrix"""


def matrix_divided(matrix, div):
    """ Divides all elements in a matrix """
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            result = list(map(lambda x: round(x / div, 2), row))
            new_matrix.append(result)
    return new_matrix
