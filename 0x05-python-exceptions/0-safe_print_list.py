#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    length = 0
    try:
        for i in range(x):
            length+=1
            print(f"{my_list[i]}", end='')
        print("");
        return length
    except IndexError as e:
        print("");
        return length - 1
