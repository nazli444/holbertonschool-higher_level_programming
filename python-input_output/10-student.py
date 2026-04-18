#!/usr/bin/python3
"""Student class module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student"""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__
