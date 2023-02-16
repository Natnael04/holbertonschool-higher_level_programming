#!/usr/bin/python3
"""importing base from base file.
"""
from models.rectangle import Rectangle
"""creating a square of class "Rectangle".
"""


class Square(Rectangle):
    """creating square class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """use class constructor to call the super class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """the overloading str method to return.
        """
        return '[Square] ({}) {}/{} - {}'.format(
            self.id,
            self.x,
            self.y,
            self.height
        )

    @property
    def size(self):
        """getting self width of a square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """setting.
        """
        self.height = value
        self.width = value
