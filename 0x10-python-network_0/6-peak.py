#!/usr/bin/python3
"""peak"""


def find_peak(list_of_integers):
    """find peak in a list by using linear search"""
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 0:
        return None
    lng = len(list_of_integers) - 2
    i = 0
    peak = 0
    while (i <= lng):
        if i > 0:
            if list_of_integers[i] > list_of_integers[i+1]:
                if list_of_integers[i] > list_of_integers[i-1]:
                    peak = list_of_integers[i]
        i += 1
    return peak
