#!/usr/bin/python3
"""Module that loads a JSON object from a file"""

import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
