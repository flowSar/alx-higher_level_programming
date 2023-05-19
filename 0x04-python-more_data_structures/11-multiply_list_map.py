#!/usr/bin/python3

def square(number, mlist):
    return number * mlist
def multiply_list_map(my_list=[], number=0):
    return list(map(square, [number for _ in my_list], my_list))
