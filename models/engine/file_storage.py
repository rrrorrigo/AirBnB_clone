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

props = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

class FileStorage:
	__file_path = "file.json"
	__objects = {}

	def all(self):
		return self.__objects

	def new(self, obj):
		if obj is not None:
			key = obj.__class__.__name__ + "." + obj.id
			self.__objects[key] = obj

	def save(self):
		json_objects = {}
		for key in self.__objects:
			json_objects[key] = self.__objects[key].to_dict()

	def reload(self):
		try:
			with open(self.__file_path, 'r') as f:
				js = json.load(f)
			for key in js:
				self.__objects[key] = props[js[key]["__class__"]](**js[key])
		except Exception as e:
			pass
