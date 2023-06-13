#!/usr/bin/python3
"""
This is module-level documentation
In this module has one class names MyList.
"""
class MyList(list):
    """MyList is a subclass of list"""
    def print_sorted(self):
        """this function printed sorted list"""
        my_list = [elm for elm in self]
        my_list.sort()
        print(my_list)
