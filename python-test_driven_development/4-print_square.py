#!/usr/bin/python3
"""
This module provides a function that prints a square using '#'.

It validates that size is a non-negative integer before printing
the square pattern row by row.
"""


def print_square(size):
    """
    Print a square of '#' characters with side length size.

    Args:
        size: an integer representing the side length of the square.

    Returns:
        None
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
