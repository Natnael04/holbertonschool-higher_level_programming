#!/usr/bin/python3
"""creating an empty class"""


class BaseGeometry:
    """to create empty class."""
    pass
    """to raise Exception with message."""

    def area(self):
        """to raise an exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """to validate the value is integer"""
        if type(value) != int:
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("name must be greater than 0")
