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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float('inf') or a == float('-inf') or a != a:
        raise OverflowError("cannot convert float infinity to integer")
    if b == float('inf') or b == float('-inf') or b != b:
        raise OverflowError("cannot convert float infinity to integer")
    return int(a) + int(b)
