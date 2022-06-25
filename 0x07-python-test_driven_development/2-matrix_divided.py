#!/usr/bin/python
"""
    Divides all elements of a matrix with a given divisor.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix
        Args:
            matrix (list): matrix of int/float lists
            div (int): divisor for matrix item
        Return:
            returns new list with result
    """
    if not isinstance(div, (int, float)) or div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
        # new_list = []
        # res = list(map(lambda item: round(item / div, 2), row))
        # new_list.append(res)

    # return new_list
    return [list(map(lambda item: round(item / div, 2), row)) for row in matrix]
