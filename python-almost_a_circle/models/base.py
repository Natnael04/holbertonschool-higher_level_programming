#!/usr/bin/python3
"""write the first class"""


import json


class Base:
    """declaring private class attribute"""
    __nb_objects = 0
    """define private class attribute"""

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """to return to json format representation.
        """
        json_string = json.dumps(list_dictionaries)
        if list_dictionaries is None:
            return ("[]")
        else:
            return json_string
