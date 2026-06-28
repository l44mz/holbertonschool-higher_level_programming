#!/usr/bin/python3
"""Module for reading a text file and printing it to stdout."""


def read_file(filename=""):
    """Read a UTF8 text file and print its contents to stdout.

    Args:
        filename (str): The path to the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
