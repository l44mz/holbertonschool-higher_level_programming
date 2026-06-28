#!/usr/bin/python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to a JSON file named data.json.

    Args:
        csv_filename (str): The path to the input CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except FileNotFoundError:
        return False
