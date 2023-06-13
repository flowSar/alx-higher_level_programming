#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names from_json_string.
"""
import json


def from_json_string(my_str):
    """
    this function return the JSON representation of an object.
    using loads to convert string to dictionary object
        my_str: string dict.
    """
    dic_object = json.loads(my_str)
    return json.dumps(dic_object)
