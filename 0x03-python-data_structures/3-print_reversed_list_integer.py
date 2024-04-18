#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return []
    lng = len(my_list) - 1
    idx = lng
    for el in my_list:
        print("{:d}".format(my_list[idx]))
        idx -= 1
