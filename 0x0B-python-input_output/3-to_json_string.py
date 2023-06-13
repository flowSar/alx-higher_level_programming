#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names to_json_string.
"""


import json
def to_json_string(my_obj):
    """
    this function eturns the JSON representation of an object.
        my_obj: object.
    """
    return json.dumps(my_obj)

