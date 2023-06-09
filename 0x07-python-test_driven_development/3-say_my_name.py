#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """ function that print full name"""
    if type(first_name) is int:
        raise TypeError("first_name must be a string")
    elif type(last_name) is int:
    	raise TypeError("last_name must be a string")
    else:
    	print("My name is {:s} {:s}".format(first_name, last_name))
