#!/usr/bin/python3
"""Module that defines MyList class inheriting from list."""


class MyList(list):
    """Custom list class that can print itself sorted."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
