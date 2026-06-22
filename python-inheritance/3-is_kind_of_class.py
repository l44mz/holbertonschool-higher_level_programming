#!/usr/bin/python3
"""Module that defines a function to check class instance or inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it.

    Args:
        obj: Any Python object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or any class that
        inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
