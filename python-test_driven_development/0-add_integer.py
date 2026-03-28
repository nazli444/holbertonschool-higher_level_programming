#!/usr/bin/python3
def add_integer(a, b=98):
    """Module for adding two integers.
        add a and b two integers
        a and b must be integer and float
        we should cast b integer
        Raises TypeError if a or b are not integers or floats."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
