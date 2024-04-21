#!/usr/bin/python3
import json
"""
    this is a base module
    we have her a Base calsss inside the class we have
    __init__ methode that have id argument
"""


class Base:
    """
        this __init__ for initializing Base object she receive one argument
        and asign it to object (is) if id argument(arg)
        isn't None if it's none we increament
        __nb__objects and asign it to id

        Attributes:
        id: id
        Return: None
    """
    # class attribue
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        length = len(list_dictionaries)
        if list_dictionaries is None or length == 0:
            return "[]"
        json_data = json.dumps(list_dictionaries)
        return json_data

    @classmethod
    def save_to_file(cls, list_objs):
        dic_list = []
        if list_objs is None:
            data = json.loads("[]")
            with open(f"{cls.__name__}.json", "w") as file:
                json.dump(data, file)
        else:
            for obj in list_objs:
                dic_list.append(obj.to_dictionary())
            json_string = cls.to_json_string(dic_list)
            data = json.loads(json_string)
            with open(f"{cls.__name__}.json", "w") as f:
                json.dump(data, f)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            json_data = json.loads(json_string)
            return json_data
    
    @classmethod
    def create(cls, **dictionary):
        pass
