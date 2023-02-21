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
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """to assign an argument to each attribute.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    import json
    def to_dictionary(self):
        """to return the dictionary representation of a square.
        """
        d = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return d
