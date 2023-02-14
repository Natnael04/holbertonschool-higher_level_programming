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
        
            self.width = width
            self.height = height
            self.x = x
            self.y = y
            if id is not None:
              self.id = id
            else:
              Rectangle.__nb_objects += 1
              self.id = Rectangle.__nb_objects

    def getwidth(self):
        """
        getting self width of the Rectangle.
        """
        return self.width

    def setwidth(self, value):
        """
        setting self width of the Rectangle.
        """
        self._width = value

    def getheight(self):
        """
        getting self height of the Rectangle.
        """
        return self.height

    def setheight(self, value):
        """
        setting self height of the Rectangle.
        """
        self._height = value

    def getx(self):
        """
        getting self x of the Rectangle.
        """
        return self.x

    def setx(self, value):
        """
        setting self x of the Rectangle.
        """
        self._x = value

    def gety(self):
        """
        getting self y of the Rectangle.
        """
        return self.y

    def sety(self, value):
        """
        setting self y of the Rectangle.
        """
        self._y = value
