#!/usr/bin/python3
"""Module for appending a string to a UTF8 text file."""


def append_write(filename="", text=""):
    """Append a string to a text file and return the number of chars added.

    Args:
        filename (str): The path to the file to append to.
        text (str): The string content to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
