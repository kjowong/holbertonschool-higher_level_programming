#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for array in matrix:
        array = list(map(lambda element: element**2, array))
        new_matrix.append(array)
    return new_matrix
