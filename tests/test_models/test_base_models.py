#!/usr/bin/python3


from models.base_model import BaseModel
import models
from datetime import datetime
import unittest
import os
from time import sleep

class BaseModelTest(unittest.TestCase):

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

    def cuandosecreopadre(self):
        ritmobase2 = BaseModel()
        self.assertEqual(type(ritmobase2.created_at), type(datetime.now()))
        self.assertTrue(hasattr(ritmobase2, "created_at"))

    def cuandoseupdeteoyeyeee(self):
        ritmobase2 = BaseModel()
        self.assertEqual(type(ritmobase2.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(ritmobase2, "updated_at"))
        actualizado =  ritmobase2.updated_at
        self.assertTrue(actualizado == ritmobase2.updated_at)
        ritmobase2.save()
        self.assertFalse(actualizado == ritmobase2.updated_at)

    def crearvariasinstancias(self):
        ritmobase = BaseModel()
        self.assertEqual(type(ritmobase.id), str)
        self.assertEqual(type(ritmobase.created_at), datetime)
        self.assertEqual(type(ritmobase.updated_at), datetime)
        ritmobase1 = BaseModel()
        self.assertEqual(type(ritmobase1.id), str)
        self.assertEqual(type(ritmobase1.created_at), datetime)
        self.assertEqual(type(ritmobase1.updated_at), datetime)
        ritmobase2 = BaseModel()
        self.assertEqual(type(ritmobase2.id), str)
        self.assertEqual(type(ritmobase2.created_at), datetime)
        self.assertEqual(type(ritmobase2.updated_at), datetime)
        self.assertNotEqual(ritmobase.id, ritmobase1.id, ritmobase2.id)

if __name__ == "__main__":
    unittest.main()