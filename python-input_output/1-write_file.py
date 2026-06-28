#!/usr/bin/python3
"""Module for writing a string to a UTF8 text file."""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The path to the file to write.
        text (str): The string content to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
