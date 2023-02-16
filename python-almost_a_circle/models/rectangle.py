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
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

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
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
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
            raise ValueError("x must be >= 0")
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
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """to return the value of area of the rectangle instance.
        """
        return (self.height * self.width)

    def display(self):
        """to prints in stdout the Rectangle instance with the character.
        """
        for j in range(0, self.height):
            for j in range(0, self.width):
                print('#', end="")
            print("")

    def __str__(self):
        """to overide the str method to return.
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def display(self):
        """to prints in stdout the Rectangle instance with the character.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """to assign an argument to each attribute.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """to return the dictionary representation of a rectangle.
        """
        d = {'x': self.x, 'y': self.y, 'id': self.id,
             'height': self.height, 'width': self.width, }
        return d
