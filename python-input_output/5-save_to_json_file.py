#!/usr/bin/python3
"""Module for saving an object to a file as a JSON string."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to serialize and save.
        filename (str): The path to the file to write.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
