#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for inner_list in matrix:
        print(" ".join("{:d}".format(element) for element in inner_list))
