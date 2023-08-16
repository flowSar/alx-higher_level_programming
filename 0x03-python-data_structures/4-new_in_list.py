#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_ls = [None for _ in range(length)]
    i = 0
    for el in my_list:
        new_ls[i] = el
        i+=1
    new_ls[idx] = element
    return new_ls
