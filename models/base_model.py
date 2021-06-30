#!/usr/bin/python3
""" Creation of class base_model"""

from uuid import uuid4
from datetime import datetime
import models

timeform = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """ Class BaseModel that defines all common
    attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ Initialization of class base model"""
        if kwargs:
            for key, value, in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if (hasattr(self, "created_at") and type(self.created_at) is str):
                a = datetime.strptime(kwargs["created_at"], timeform)
                self.created_at = a
            if (hasattr(self, "updated_at") and type(self.updated_at) is str):
                a = datetime.strptime(kwargs["updated_at"], timeform)
                self.updated_at = a
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """ String representation of class BaseModel"""
        __name = type(self).__name__
        return "[{}] ({}) {}".format(__name, self.id, self.__dict__)

    def save(self):
        """ Save the object into .json file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return an dictionary representation of object"""
        rdict = dict(self.__dict__)
        rdict["__class__"] = type(self).__name__
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        return rdict
