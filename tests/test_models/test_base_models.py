#!/usr/bin/python3


from models.base_model import BaseModel
import models
from datetime import datetime
import unittest
import os
from time import sleep

class testeomodeloclase(unittest.TestCase):

    def setealo(self):
        self.ritmobase = BaseModel()

    def romeplo(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def crearunainstancia(self):
        ritmobase = BaseModel()
        self.assertEqual(type(ritmobase.id), str)
        self.assertEqual(type(ritmobase.created_at), datetime)
        self.assertEqual(type(ritmobase.updated_at), datetime)


if __name__ == "__main__":
    unittest.main()