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
        self.size = size

    def __str__(self):
        """the overloading str method to return.
        """
        return '[Square] ({}) {}/{} - {}'.format(
            self.id,
            self.x,
            self.y,
            self.size
        )
