#!/usr/bin/python
""" Creation of class user"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Creation of class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization of class user"""
        super().__init__(*args, **kwargs)
