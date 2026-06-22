#!/usr/bin/python3
"""Module that provides a function to look up object attributes and methods."""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: Any Python object to inspect.

    Returns:
        A list of strings representing the names of the object's
        attributes and methods.
    """
    return dir(obj)
