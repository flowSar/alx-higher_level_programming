#!/usr/bin/python3


class Person:
    
    __number = 0
    
    def __init__(self, id=None):
        
        if id is None:
            Person.__number += 1
            self.id = Person.__number
        else:
            self.id = id
    
        
    def update(self, id):
        self.id = id
    
    def __str__(self):
        return f"{self.id}"
    
    @classmethod
    def create(cls):
        dummy = cls()
        return dummy

p = Person()
p2 = Person()
p3 = Person()
p4 = Person()
print(p4)
dummy = Person.create()
print(dummy)
print(p3.id)
p5 = Person()
print(p5.id)
