#!/usr/bin/python3

def uniq_add(my_list=[]):
    dic = {}
    res = 0
    for el in my_list:
        dic[el] = el

    for key in dic:
        res+= dic.get(key)
    return res
