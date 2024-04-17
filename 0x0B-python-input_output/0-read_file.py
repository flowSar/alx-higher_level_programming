#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names read_file.
"""


def read_file(filename=""):
    """
    this function read from a file and pritn to stdout
    Args:
        filename: file name or a path of the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end='')
