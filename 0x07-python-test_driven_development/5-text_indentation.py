#!/usr/bin/python3

def text_indentation(text):
    """function print a text as lines witch each line end with '.' or '':'"""
    found = 0
    for letter in text:
        if found == 1:
            found = 0
            continue
        print(letter, end='')
        if letter == '.' or letter == ':':
            found += 1
            print("\n")
