#!/usr/bin/python3
class Square:
    """Class that defines a square"""
    def __init__(self, size = 0):
         """Initialize square with size validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=")
    self._size = size
