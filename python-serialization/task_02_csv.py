#!/usr/bin/python3
"""Module that converts CSV to JSON"""

import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV file to JSON file"""
    try:
        data = []

        with open(filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile)

        return True

    except FileNotFoundError:
        return False
