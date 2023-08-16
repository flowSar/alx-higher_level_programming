#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    found = 1
    for ky in a_dictionary:
        if ky == key:
            found = 0
    if found == 0:
        del a_dictionary[key]
    return a_dictionary
