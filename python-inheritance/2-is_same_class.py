#!/usr/bin/python3
"""Module that defines a function to check exact class instance membership."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, False otherwise.

    Args:
        obj: Any Python object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
