#!/usr/bin/python
""" Creation of class user"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Creation of class City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization of class City"""
        super().__init__(*args, **kwargs)
