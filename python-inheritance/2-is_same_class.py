#!/usr/bin/python3
"""to check the object an instance of specified class"""


def is_same_class(obj, a_class):
    """to check the object an instance of specified class"""
    return type(obj) is a_class


is_same_class(1, int)
is_same_class(1, object)
