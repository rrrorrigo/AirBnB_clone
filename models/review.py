#!/usr/bin/python
""" Creation of class user"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Init method of class State"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Init method of class State"""
        super().__init__(*args, **kwargs)
