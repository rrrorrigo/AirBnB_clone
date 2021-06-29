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

    def idiferente(self):
        ritmobase1 = BaseModel(69)
        self.assertNotEqual(ritmobase1.id, 69)
        ritmobase1 = BaseModel("holi")
        self.assertNotEqual(ritmobase1.id, "holi")
        ritmobase1 = BaseModel([0, 1, 2])
        self.assertNotEqual(ritmobase1.id, [0, 1, 2])


if __name__ == "__main__":
    unittest.main()