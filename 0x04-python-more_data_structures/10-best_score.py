#!/usr/bin/python3

def best_score(a_dictionary):
    tmp = 0
    ky = None
    if a_dictionary is None:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > tmp:
            tmp = a_dictionary[key]
            ky = key
    return ky
