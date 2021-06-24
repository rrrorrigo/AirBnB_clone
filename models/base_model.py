#!/usr/bin/python3
""" Creation of class base_model"""
from uuid import uuid4
from datetime import datetime

class BaseModel():
	def __init__(self):
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()
	
	def __str__(self):
		return "[{}] ({}) {}".format(__name__, self.id, self.__dict__)

	def save(self):
		self.updated_at = datetime.now()

	def to_dict(self):
		rdict = dict(self.__dict__)
		rdict["__class__"] = type(self).__name__
		rdict["created_at"] = self.created_at.isoformat()
		rdict["updated_at"] = self.updated_at.isoformat()
		return rdict