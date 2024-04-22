#!/usr/bin/python3
import json
"""
    this is a base module
    we have her a Base calsss inside the class we have
    __init__ methode that have id argument
"""


class Base:
    """
        this __init__ for initializing Base object she receive one argument
        and asign it to object (is) if id argument(arg)
        isn't None if it's none we increament
        __nb__objects and asign it to id

        Attributes:
        id: id
        Return: None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            this __init__ for initiliaze the object
            Attributes:
                id : id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            this function turn list_dictionaries
            into string with json.dumps()
            and return it if it's not ampty
            Return:
                jsonstring if list_dictionaries  not empty
                and [] if list_dictionaries is empty
        """

        if list_dictionaries is None:
            return "[]"
        length = len(list_dictionaries)
        if length == 0:
            return "[]"
        json_data = json.dumps(list_dictionaries)
        return json_data

    @classmethod
    def save_to_file(cls, list_objs):
        """
            this function save objecsts attributes in json file
            if list_object empt we create file and add write
            [] inside the file that me the file is empty
            Attributes:
                list_objs: list of object, Rectangle or Square
                or both.
        """
        dic_list = []
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as file:
                file.write("[]", file)
        else:
            for obj in list_objs:
                dic_list.append(obj.to_dictionary())
            json_string = cls.to_json_string(dic_list)
            with open(f"{cls.__name__}.json", "w+") as f:
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
            this method is loads string into jsonobject
            like turning strign into json_object that we
            can manipulate
            Attributes:
                json_string: json string
            Return:
                empty list of json_string is None or
                return json object of not None
        """
        if json_string is None:
            return []
        else:
            json_data = json.loads(json_string)
            return json_data

    @classmethod
    def create(cls, **dictionary):
        """
            this function create a dummy object and update its
            attribute and return it.
            Attributes:
                dictionary: dictionary
            Return:
                return dummy object
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2, 2, 6)
            dummy.update(**dictionary)
            return dummy
        if cls.__name__ == "Square":
            dummy = cls(2, 0, 0)
            dummy.update(**dictionary)
            return dummy
        return None

    @classmethod
    def load_from_file(cls):
        """
            this function loads data from json file
            turn it into string with to_json_string
            and then turn it into object by from_json_string
            send it to creat method to update the object arrtibute
            and get a dummy object
            if not data in the file
            Return:
                list pf dummy object ot Null if file empty
        """
        file_name = cls.__name__
        dummy_obj_list = []
        with open(f"{file_name}.json") as file:
            json_data = json.load(file)
        json_data = cls.from_json_string(cls.to_json_string(json_data))
        if len(json_data) == 0:
            return []
        for data in json_data:
            dummy_obj_list.append(cls.create(**data))
        return dummy_obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            this function save object attributes to csv file
            Attributes:
                list_objs: list of object that we save their
                data
        """
        file_name = cls.__name__
        if file_name == "Rectangle":
            for obj in list_objs:
                obj_dic = obj.to_dictionary()
                id = obj_dic['id']
                width = obj_dic['width']
                height = obj_dic['height']
                x = obj_dic['x']
                y = obj_dic['y']
                csv_data = f"{id}, {width}, {height}, {x}, {y}\n"

                with open(f"{file_name}.csv", "a") as file:
                    file.write(csv_data)
        if file_name == "Square":
            for obj in list_objs:
                obj_dic = obj.to_dictionary()
                id = obj_dic['id']
                size = obj_dic['size']
                x = obj_dic['x']
                y = obj_dic['y']
                csv_data = f"{id}, {size}, {x}, {y}\n"

                with open(f"{file_name}.csv", "a") as file:
                    file.write(csv_data)

    @classmethod
    def load_from_file_csv(cls):
        """
            this function loads data from csv file line
            by line and then fill it to a empty dictionary
            and then send it creat() method to get
            dummy object and update the rectangle attributes
            create() will return dummy object we collect those objects
            in a list and return them.
            this function do this for square and Rectangle
        """
        file_name = cls.__name__
        object_list = []
        dic_key_rect = ['id', 'width', 'height', 'x', 'y']
        dic_key_sq = ['id', 'size', 'x', 'y']
        used_list = []
        if file_name == "Rectangle":
            used_list = dic_key_rect
        elif file_name == "Square":
            used_list = dic_key_sq

        with open(f"{file_name}.csv", "r") as file:
            new_dic = {}
            for line in file:
                for key, value in zip(used_list, line.strip().split(',')):
                    new_dic[key] = int(value)
                object_list.append(cls.create(**new_dic))
        return object_list
