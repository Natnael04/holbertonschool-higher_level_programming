#!/usr/bin/python3
"""importing base from base file.
"""
from models.base import Base

"""creating a rectangle of class "Base".
"""


class Rectangle(Base):
    """creating rectangle class.
    """
    __nb_objects = 0
    """define private class attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if id is not None:
            self.id = id
        else:
            Rectangle.__nb_objects += 1
            self.id = Rectangle.__nb_objects
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")

    @property
    def width(self):
        """
        getting self width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting self width of the Rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0 ")
        self.__width = value

    @property
    def height(self):
        """
        getting self height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting self height of the Rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0 ")
        self.__height = value

    @property
    def x(self):
        """
        getting self x of the Rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setting self x of the Rectangle.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0 ")
        self.__x = value

    @property
    def y(self):
        """
        getting self y of the Rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setting self y of the Rectangle.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0 ")
        self.__y = value
