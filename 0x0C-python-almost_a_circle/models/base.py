#!/usr/bin/python3

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
