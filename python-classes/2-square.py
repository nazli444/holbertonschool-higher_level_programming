#!/usr/bin/python3
"""Module that defines a square based on 1-square.py"""


class Square:
    """Class that defines a square"""
    def __init__(self, size = 0):
         """Initialize square with size validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=")
    self._size = size
