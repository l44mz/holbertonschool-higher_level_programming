#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.

It validates the matrix structure and divisor, then returns a new
matrix with each element divided and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix: a list of lists of integers or floats.
        div: an integer or float divisor.

    Returns:
        A new matrix with each element divided by div,
        rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not all(
            isinstance(row, list) and len(row) > 0 for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)) or isinstance(elem, bool):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
