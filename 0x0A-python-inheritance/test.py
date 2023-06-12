#!/usr/bin/python3

class Employee:

    full_name = None
    def __init__(self, f_name, l_name, phone):
	    self.l_name = l_name
	    self.f_name = f_name


    def full_user_name(self):
        self.full_name = self.f_name+" "+self.l_name
        return self.full_name

    def is_same_class(self, obj, a_class):
        return isinstance(obj, a_class)


if __name__ == '__main__':

	em_1 = Employee("brahim", "sarouri", "0650704968")
	em_1.full_user_name()
	print(em_1.full_name)

	print(em_1.is_same_class(em_1, Employee))