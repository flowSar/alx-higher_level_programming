#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names load_from_json_file.
"""
import json


def load_from_json_file(filename):
    """
    this function dump a dictioney object to a file
    Args:
        filename: filename or a path of a file.
    """
    # json_data = """
    with open(filename, "r") as f:
        json_data = f.read()

    json_object = json.loads(json_data)
    return json_object
