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

    def get__width(self):
        """
        getting self width of the Rectangle.
        """
        return self.__width

    def set__width(self, value):
        """
        setting self width of the Rectangle.
        """
        self.__width = value

    def getheight(self):
        """
        getting self height of the Rectangle.
        """
        return self.__height

    def set__height(self, value):
        """
        setting self height of the Rectangle.
        """
        self.__height = value

    def get__x(self):
        """
        getting self x of the Rectangle.
        """
        return self.__x

    def set__x(self, value):
        """
        setting self x of the Rectangle.
        """
        self.__x = value

    def get__y(self):
        """
        getting self y of the Rectangle.
        """
        return self.__y

    def set__y(self, value):
        """
        setting self y of the Rectangle.
        """
        self.__y = value
