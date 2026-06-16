#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the square.
        """
        self.__size = size
