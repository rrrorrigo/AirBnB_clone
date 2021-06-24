#!/usr/bin/python3
""" Creation of class base_model"""

from uuid import uuid4
from datetime import datetime
import models

timeform = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
	def __init__(self, *args, **kwargs):
		if kwargs:
			for key, value, in kwargs.tems():
				if key != "__class__":
					setattr(self, key, value)
			if hasattr(self, "created_at") and type(self.created_at) is str:
				self.created_at = datetime.strptime(kwargs["created_at"], timeform)
			if hasattr(self, "updated_at") and type(self.update_at) is str:
				self.update_at = datetime.strptime(kwargs["updated_at"], timeform)
		else:
			self.id = str(uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			models.storage.new(self)
			models.storage.save()

	def __str__(self):
		return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

	def save(self):
		self.updated_at = datetime.now()
		models.storage.save()

	def to_dict(self):
		rdict = dict(self.__dict__)
		rdict["__class__"] = type(self).__name__
		rdict["created_at"] = self.created_at.isoformat()
		rdict["updated_at"] = self.updated_at.isoformat()
		return rdict
