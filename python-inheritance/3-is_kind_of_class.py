#!/usr/bin/python3
"""Module that checks if an object is an instance of a class or inherited"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is instance of a_class or inherited from it"""
    return isinstance(obj, a_class)
