#!/usr/bin/python3
"""
student with first name, last name, and age attributes.
Attributes:
    first_name (: The first name of the student.
    last_name: The last name of the student.
    age : The age of the student.
"""


class Student:
    """
    student with first name, last name, and age attributes.
    Attributes:
        first_name : The first name of the student.
        last_name : The last name of the student.
        age : The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """ Initializes a new Student object. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            function return a student attribute as a
            dictionary basd on given key
            Return: return a student infor based on giving key
                first name or last name or and age.
        """
        students = {"first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age}
        std = {}
        if attrs is not None:
            for key in attrs:
                if key in students:
                    std[key] = students[key]
            return std
        return students

    def reload_from_json(self, json):
        if len(json) > 1:
            self.__init__(json["first_name"], json["last_name"], json["age"])
