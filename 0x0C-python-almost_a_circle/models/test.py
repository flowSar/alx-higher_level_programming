#!/usr/bin/python3

#class Superclass:

	#def __init__(self):
		#dummy = __import__("subclass_module")
		#dummy = getattr(dummy, "subclass")
		#dummy_instance = dummy()

#class subclass(Superclass):
	
	#def __init__(self, y):
		#self.y = y
	
	#def update(self, x):
		#self.y = x



from rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
