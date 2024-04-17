#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names load_from_json_file.
"""
import json


def class_to_json(obj):
    """"
        THIS FUNCTION RETURN THE ATTRIBUTE OF THE OBJ IN DICTIONAY TYPE
            ARGS:
                OBJ: OBJECT
            RETURN: RETURN A DICTIONAY
    """
    my_dic = {}
    for key, value in obj.__dict__.items():
        my_dic[key] = value
    return my_dic
