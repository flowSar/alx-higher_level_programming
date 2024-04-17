#!/usr/bin/python3
"""
    his module contains a class Student that represent
    student information and methods to handle student data.
"""


class Student:
    """
    student with first name, last name, and age attributes.
    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """ Initializes a new Student object. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            function return a student attribute as a dictionary

            Return: return a dictionary containing the student's
                first name, last name, and age.
        """
        students = {"first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age}
        return students
