#!/usr/bin/python3
"""
In this module has one class which is a subclass of a list.
"""


class MyList(list):

    def print_sorted(self):
        """ Sort list and print it """
        new_List = [x for x in self]
        length = len(new_List)
        for i in range(length):
            for j in range(length):
                if new_List[i] < new_List[j]:
                    tmp = new_List[i]
                    new_List[i] = new_List[j]
                    new_List[j] = tmp

        print(new_List)
