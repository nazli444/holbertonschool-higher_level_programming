#!/usr/bin/python3
"""Module that defines a square based on 1-square.py"""


class Square:
    """Defines a square with validated private size attribute."""

    def __init__(self, size=0):
        """Initialize square with optional size (with validation)."""
        self.size = size
    def size(self):
        """Retrieve the size."""
        return self.__size
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
