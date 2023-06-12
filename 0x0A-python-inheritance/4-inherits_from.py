#!/usr/bin/python3

def inherits_from(obj, a_class):
    """function return true if obj is instance of class that inherited"""
    if a_class == bool:
    	return False
    return isinstance(obj, a_class)
