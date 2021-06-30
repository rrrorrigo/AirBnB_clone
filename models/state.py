#!/usr/bin/python
""" Creation of class user"""

from models.base_model import BaseModel


class State(BaseModel):
    """ creation of class State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init method of class State"""
        super().__init__(*args, **kwargs)
