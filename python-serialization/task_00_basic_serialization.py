#!/usr/bin/python3
"""Module for basic JSON serialization and deserialization."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The output JSON file path. Replaced if it exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): The input JSON file path.

    Returns:
        dict: The deserialized Python dictionary from the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
