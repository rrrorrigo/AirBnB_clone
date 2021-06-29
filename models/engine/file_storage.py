#!/usr/bin/python3
""" Creation of class FileStorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

props = {"BaseModel": BaseModel, "User": User, "State": State,
         "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage:
    """ Creation of class FileStorage that handles .json files"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ method that return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ method that sets in __objects the obj with key <objName>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                js = json.load(f)
            for key in js:
                self.__objects[key] = props[js[key]["__class__"]](**js[key])
        except:
            pass
