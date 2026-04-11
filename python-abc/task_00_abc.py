#!/usr/bin/env python3
"""Module that defines abstract Animal class and its subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal"""

    def sound(self):
        """Returns Dog sound"""
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal"""

    def sound(self):
        """Returns Cat sound"""
        return "Meow"
