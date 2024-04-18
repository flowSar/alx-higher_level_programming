#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    p_num = 0
    try:
        for i in range(x):
            p_num += 1
            print(f"{my_list[i]}", end='')
        print("")
        return p_num
    except Exception as e:
        return p_num
