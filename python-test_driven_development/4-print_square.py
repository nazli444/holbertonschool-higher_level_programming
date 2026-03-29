#!/usr/bin/python3
"""
Module that prints a square with the character #
"""


def print_square(size):
    """
    Prints a square of size 'size' using the character #
    """

    # Type check
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Value check
    if size < 0:
        raise ValueError("size must be >= 0")

    # If size is 0, print nothing
    if size == 0:
        return

    # Print the square
    for _ in range(size):
        print("#" * size)
