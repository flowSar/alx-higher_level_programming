#!/usr/bin/python3

from .rectangle import Rectangle
from .rectangle import check_for_exception


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str is a mgic method for printing object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        check_for_exception(size, "width")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):

        args_length = len(args)
        if args_length >= 1:
            if args_length >= 1:
                self.id = args[0]
            if args_length >= 2:
                self.size = args[1]
            if args_length >= 3:
                self.x = args[2]
            if args_length >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    check_for_exception(value, "width")
                    self.size = value
                elif key == "x":
                    check_for_exception(value, key)
                    self.x = value
                elif key == "y":
                    check_for_exception(value, key)
                    self.y = value

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
