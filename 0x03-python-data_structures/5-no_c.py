#!/usr/bin/python3

def no_c(my_string):
    new = ""
    for el in my_string:
        if el != 'c' and el != 'C':
            new += el
    return new
