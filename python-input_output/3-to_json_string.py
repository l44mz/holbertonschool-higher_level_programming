#!/usr/bin/python3
"""Module for converting an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    Args:
        my_obj: The object to serialize to JSON.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
