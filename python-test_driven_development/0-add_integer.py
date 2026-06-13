#!/usr/bin/python3
"""
This module provides a function that adds two integers.

It demonstrates type checking, casting floats to integers,
and raising appropriate exceptions for invalid input types.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats (casted to int).

    Args:
        a: first number, int or float.
        b: second number, int or float, defaults to 98.

    Returns:
        The integer sum of a and b.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
