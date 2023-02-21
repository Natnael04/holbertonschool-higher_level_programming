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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to return to json format representation.
        """
        to_json_string = json.dumps(list_dictionaries)
        if list_dictionaries is None:
            return ("[]")
        else:
            return to_json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    def from_json_string(json_string):
        """to return the list of the json string.
        """
        if json_string is None and json_string == "[]":
            return []
        else:
            return json.loads(json_string)
