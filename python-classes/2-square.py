#!/usr/bin/python3
# This function is creating new empty class
"""creating a class square to define square"""


class Square:
    """creating a class tha define a square by private instance attribute."""

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise (Exception("size must be an integer"))
            raise (TypeError)
        else:
            if size < 0:
                raise (Exception("size must be >= 0"))
                raise (ValueError)
