#! /usr/bin/python3


def divisible_by_2(my_list=[]):

    list_len = len(my_list)
    new_list = [None for _ in range(list_len)]

    for i in range(list_len):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
