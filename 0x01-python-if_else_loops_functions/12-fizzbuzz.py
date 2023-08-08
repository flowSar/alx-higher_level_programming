#!/usr/bin/python3
def fizzbuzz():
    text = ""
    for i in range(1, 100):
        if i % 3 == 0:
            text += "Fizz "
        elif i % 5 == 0:
            text += "Buzz "
        elif i % 5 == 0 and i % 3 == 0:
            text +="FizzBuzz "
        else:
            text += str(i)+" "
    print(text+"$", end='')
fizzbuzz()