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
        if id is not None:

            self.width = width
            self.height = height
            self.x = x
            self.y = y
            self.id = id
        else:
            Rectangle.__nb_objects += 1
            self.id = Rectangle.__nb_objects
    """getting self width of the Rectangle."""

    def getwidth(self):
        return self.width

    def setwidth(self, value):
        self.width = value

    def getheight(self):
        return self.height

    def setheight(self, value):
        self.height = value

    def getx(self):
        return self.x

    def setx(self, value):
        self.x = value

    def gety(self):
        return self.y

    def sety(self, value):
        self.y = value
