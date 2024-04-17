#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names save_to_json_file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
        this function dump a dictioney object to a file
        Args:
            my_obj: dictionary object.
            filename: filename or a path of a file.
    """
    with open(filename, "w+") as f:
        json.dump(my_obj, f)
