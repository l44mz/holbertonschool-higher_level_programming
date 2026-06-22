#!/usr/bin/python3
"""Module that defines a function to check indirect class inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited from a_class.

    The object must be an instance of a subclass of a_class, not a_class
    itself. Direct or indirect inheritance both return True.

    Args:
        obj: Any Python object to check.
        a_class: The class to compare against.

    Returns:
        True if obj's class inherited from a_class but is not exactly
        a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
