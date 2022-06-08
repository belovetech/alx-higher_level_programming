#!/usr/bin/python3

def square(num):
    return num ** 2


def square_matrix_simple(matrix=[]):
    """Square of matrix"""
    square_matrix = []
    for row in matrix:
        col = map(square, row)
        square_matrix.append(list(col))
    return square_matrix
