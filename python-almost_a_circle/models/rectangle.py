#!/usr/bin/python3
"""importing base from base file."""
from models.base import Base
"""creating  a rectangle of base."""


class Rectangle(Base):
    pass
    """declaring private class attribute."""
    __nb_objects = 0
    """define private class attribute."""

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
    """define private instance attribute with getter."""

    def getwidth(self):
        return self.width
    """define private instance attribute with setter."""

    def setwidth(self, value):
        self.width = value
    """define private instance attribute with getter."""

    def getheight(self):
        return self.height
    """define private instance attribute with setter."""

    def setheight(self, value):
        self.height = value
    """define private instance attribute with getter."""

    def getx(self):
        return self.x
    """define private instance attribute with setter."""

    def setx(self, value):
        self.x = value
    """define private instance attribute with getter."""

    def gety(self):
        return self.y
    """define private instance attribute with setter."""

    def sety(self, value):
        self.y = value
    """define private instance attribute with getter."""

    def getid(self):
        return self.id
    """define private instance attribute with setter."""

    def setid(self, value):
        self.id = value
