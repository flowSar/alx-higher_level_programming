#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    this module continue a Rectangle class  with constractor method
    and he's a subclass on BaseGeometry class
"""

class Rectangle(BaseGeometry):

    """
        Rectangle is a subclass of BaseGeometry
        Attribute:
            __width: width of Rectange
            __height: height of Rectangle

    """
    __width = 0
    __height = 0

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))