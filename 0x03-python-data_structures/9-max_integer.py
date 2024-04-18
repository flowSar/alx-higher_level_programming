#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    tmp = -1
    for nm in my_list:
        if nm > tmp:
            tmp = nm
    return tmp
