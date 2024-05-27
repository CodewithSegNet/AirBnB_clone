#!/usr/bin/env python3

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the json file to path: __file_path"""
        object_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                object_dict = json.load(file)
                for key, value in object_dict.items():
                    cls_name, obj_id = key.split(".")
                    cls = eval(cls_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass



        