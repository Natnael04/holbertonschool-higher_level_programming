#!/usr/bin/python3
"""define the instance of a class"""


def inherits_from(obj, a_class):
    """to return the instance of a class that inherited"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
