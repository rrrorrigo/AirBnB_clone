#!/usr/bin/python3


from models.base_model import BaseModel
import models
from datetime import datetime
import unittest
import os
from time import sleep

class BaseModelTest(unittest.TestCase):

    def test_setealo(self):
        self.ritmobase = BaseModel()

    def test_romeplo(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_crearunainstancia(self):
        ritmobase = BaseModel()
        self.assertEqual(type(ritmobase.id), str)
        self.assertEqual(type(ritmobase.created_at), datetime)
        self.assertEqual(type(ritmobase.updated_at), datetime)

    def test_idiferente(self):
        ritmobase1 = BaseModel(69)
        self.assertNotEqual(ritmobase1.id, 69)
        ritmobase1 = BaseModel("holi")
        self.assertNotEqual(ritmobase1.id, "holi")
        ritmobase1 = BaseModel([0, 1, 2])
        self.assertNotEqual(ritmobase1.id, [0, 1, 2])

    def test_cuandosecreopadre(self):
        ritmobase2 = BaseModel()
        self.assertEqual(type(ritmobase2.created_at), type(datetime.now()))
        self.assertTrue(hasattr(ritmobase2, "created_at"))

    def test_cuandoseupdeteoyeyeee(self):
        ritmobase2 = BaseModel()
        self.assertEqual(type(ritmobase2.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(ritmobase2, "updated_at"))
        actualizado =  ritmobase2.updated_at
        self.assertTrue(actualizado == ritmobase2.updated_at)
        ritmobase2.save()
        self.assertFalse(actualizado == ritmobase2.updated_at)

    def test_crearvariasinstancias(self):
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

    def test_agregaleatributoskiko(self):
        ritmobase = BaseModel()
        ritmobase.name = "Pachu"
        ritmobase.my_number = 69
        pictionario = ritmobase.to_dict()
        self.assertEqual('name' in pictionario, True)
        self.assertEqual('my_number' in pictionario, True)
        ritmobase1 = BaseModel()
        pictionario2 = ritmobase1.to_dict()
        self.assertEqual('name' in pictionario2, False)
        self.assertEqual('my_number' in pictionario2, False)

if __name__ == "__main__":
    unittest.main()