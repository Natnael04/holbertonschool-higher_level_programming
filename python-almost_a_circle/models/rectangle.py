#!/usr/bin/python3
from models.base import Base
"""creating  a rectangle class"""


class Rectangle(Base):
    pass
    """declaring private instance attribute"""
    __nb_objects = 0
    """define private instance attribute"""

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
    """define private instance attribute with getter"""

    def getwidth(self):
        return self.width
    """define private instance attribute with getter"""

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

    def getid(self):
        return self.id

    def setid(self, value):
        self.id = value
