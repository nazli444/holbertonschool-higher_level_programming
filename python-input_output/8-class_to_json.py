#!/usr/bin/python3
"""Module that returns dictionary description of a class object"""


def class_to_json(obj):
    """Return dictionary representation of an object"""
    return obj.__dict__
