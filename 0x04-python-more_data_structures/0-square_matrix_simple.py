#!/usr/bin/python3

# def square(num):
#     return num ** 2


# def square_matrix_simple(matrix=[]):
#     """Square of matrix"""
#     square_matrix = []
#     for row in matrix:
#         square_list = map(square, row)
#         square_matrix.append(list(square_list))
#     return square_matrix

def square_matrix_simple(matrix=[]):
    """Square of matrix"""
    square_matrix = []
    for row in matrix:
        square_list = list(map(lambda num: num ** 2, row))
        square_matrix.append(square_list)
    return square_matrix
