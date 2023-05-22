#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    nfound = 1
    for od_key in a_dictionary:
        if key == od_key:
            a_dictionary[od_key] = value
            nfound = 0
        else:
            a_dictionary[od_key] = a_dictionary[od_key]

    if nfound == 1:
        a_dictionary[key] = value
    return a_dictionary
