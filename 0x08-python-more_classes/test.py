#!/usr/bin/python3

class Person:

    def __init__(self, name = None):
    	self.name = name

    def __str__(self):
        return "hello "+self.name+" !"


u = Person("brahim")
print(u)