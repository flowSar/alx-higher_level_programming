#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    p_num = 0
    try:
        for i in range(x):
            print(f"{my_list[i]}", end='')
            p_num += 1
        print("")
        return p_num
    except Exception as e:
        print("")
        return p_num
