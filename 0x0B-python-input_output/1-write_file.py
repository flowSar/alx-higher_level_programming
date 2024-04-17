#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names write_file.
"""


def write_file(filename="", text=""):
    """
    this function write to textfile and return number of char
    Args:
        filename: file name or a path of a file.
        text: text that will write to file.
    """
    read_number = 0
    with open(filename, "w", encoding="utf-8") as f:
        read_number = f.write(text)

    return read_number
