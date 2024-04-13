#!/usr/bin/python3

def text_indentation(text):
    """function print a text as lines witch each line end with '.' or '':'"""
    found = 0
    space = 0

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        if letter == ' ':
            space +=1
        if letter != ' ':
            space = 0
        if found == 1:
            found = 0
            space += 1
            if space <=1:
                print(letter, end='')
            continue
        if space <=1:
            print(letter, end='')
        if letter == '.' or letter == ':' or letter == '?':
            found += 1
            print("\n")
