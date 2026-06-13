#!/usr/bin/python3
"""
This module provides a function that prints text with indentation.

It adds two new lines after each occurrence of '.', '?' or ':',
stripping leading and trailing spaces from each line.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after '.', '?' and ':'.

    Args:
        text: the string to print.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    lines = result.split("\n")
    output = "\n".join(line.strip() for line in lines)
    print(output, end="")
