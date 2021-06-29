#!/usr/bin/python
""" Creation of class user"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ creation of class Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization fo class Amenity"""
        super().__init__(*args, **kwargs)
