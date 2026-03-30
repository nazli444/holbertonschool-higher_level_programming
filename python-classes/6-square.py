#!/usr/bin/python3
"""Module that defines a square based on 5-square."""


class Square:
    """Defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with optional size and position."""
        self.size = size          # setter çağırılır
        self.position = position  # setter çağırılır

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' respecting position."""
        if self.__size == 0:
            print()
            return

        # print vertical offset
        for _ in range(self.__position[1]):
            print()
        # print each line of the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
