#!/usr/bin/python3
"""
    module square fontinue squre class and it
    methode that handle ths class
"""
from models.rectangle import Rectangle
from models.rectangle import check_for_exception


class Square(Rectangle):
    """ Square class is subclass of Recltange has many opveridded
    function like update for updating attribute and size setter
    and getter and to_dictionay to pack all object attribute
    in a dictionary
    """
    def __init__(self, size, x=0, y=0, id=None):
        """this function of initilalize object instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str is a mgic method for printing object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        check_for_exception(size, "width")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ this function update object instance attribute with new attribute
            Attributes: args : this is tuple of attribute
                        kwargs: attribute packed in dictionary
            Return: None
        """
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
        """
        this function return all obkect instance attribute in a dictionary
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
