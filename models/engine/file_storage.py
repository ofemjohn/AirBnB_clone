#!/usr/bin/python3
"""
class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances:
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the
        JSON file (path: __file_path)
        """
        new_dict = {}
        with open(type(self).__file_path, "w", encoding="utf-8") as f:
            for key, value in type(self).__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)


    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(type(self).__file_path, "r") as f:
                data_file = json.load(f)
            for key, value in data_file.items():
                type(self).__objects[key] = eval(key.split(".")[0])(**value)
                """
                'key' holds a value of the form 'BaseModel.1234455'.
                That is NameOfModule.ID.
                key.split('.') would separate the name from id thus
                producing a tupule of the form ('BaseModel', '1234455')
                using '.' as delimiter
                key.split('.')[0] would take the first element
                of the tupule which is = 'BaseModel'
                Thus your would have a representation of the form:
                BaseModel(**value)
                eval() simply evaluates the above string
                representation to produce
                an instance of an object which is
                then stored into the dictionary __objects
                """
        except FileNotFoundError:
            pass
