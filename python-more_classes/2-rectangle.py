#!/usr/bin/python3
"""creating a class to define a Rectangle."""


class Rectangle:
    """creating a class to define a Rectangle."""
    pass

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """to return the area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """to return the perimeter of a rectangle."""
        return ((self.__width * 2) + (self.__height * 2))
        if self.__width == 0 and self.__height == 0:
            self.perimeter == 0
