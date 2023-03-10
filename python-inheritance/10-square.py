#!/usr/bin/python3
"""creating an empty class"""


class BaseGeometry:
    """to create empty class"""
    pass
    """to raise Exception with message"""

    def area(self):
        """to raise an exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """to validate the value is integer """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """to write a class rectangle that inherits.
    """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """ print(rectangle())"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def __repr__(self):
        """ str(rectangle())"""
        return '{}'.format(self)
    
class Square(Rectangle):
    """inheriting square class from rectangle"""
    def __init__(self, size):
        """instantiaion"""
        super().__init__(size, size)