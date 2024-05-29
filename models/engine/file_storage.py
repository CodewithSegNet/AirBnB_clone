#!/usr/bin/env python3

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.reviews import Review



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
                    class_name = value['__class__']
                    del value['__class__']
                    cls = globals().get(class_name)
                    if cls:
                        instance = cls(**value)
                        self.__objects[key] = instance
                    else:
                        print(f"Error: Class '{class_name}' not found. Skipping object creation.")
        except FileNotFoundError:
            pass



        