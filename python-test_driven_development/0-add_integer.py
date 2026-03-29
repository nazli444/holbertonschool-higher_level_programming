#!/usr/bin/python3
"""
Module 0-add_integer
Contains a function that adds two integers.
"""
def add_integer(a, b=98):
    """
    Adds two integers a and b.
    Casts floats to integers.
    Raises TypeError if a or b are not integers or floats.
    Returns the integer sum of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
