#!/usr/bin/python3


"""
A class that serialize instances to a JSON file and
deserialize JSON file to instances
"""
# Import
import json
from models.base_model import BaseModel
import models
import models.base_model


class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        " a public instance method that returns the dict obj "
        return self.__objects

    def new(self, obj):
        " a instance method that returns sets in obj with key "

        # construct the key using the class name and id of the object
        key = f'{obj.__class__.__name__}.{obj.id}'

        # store the object in the __objects dict with the constructed key
        self.__objects[key] = obj

    def save(self):
        " serialize the __objects to the JSON file "
        # # Convert __objects to a dictionary of dictionaries
        object_dict = {key: obj.to_dict()
                       for key, obj in self.__objects.items()}

        # save in a file
        with open(self.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        ' deserialize the JSON file to __objects '
        try:
            with open(self.__file_path, 'r') as file:
                object_dict = json.load(file)
                for key, value in object_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = getattr(models.base_model, class_name)
                    value['id'] = obj_id
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
