#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names append_write.
"""
def append_write(filename="", text=""):
    """
    this function append a text to file.
    Args:
        filename: path of a file.
        text: text that will write to file.
    """
    read_number = 0
    with open(filename, "a") as f:
    	read_number = f.write(text)

    return read_number
