#!/usr/bin/python3
"""la puta que lo aprio"""
from models.base_model import BaseModel
import models
from datetime import datetime
import unittest
import os
from time import sleep


class BaseModelTest(unittest.TestCase):
    """la puta que lo aprio"""

    @classmethod
    def setUp(self):
        """la puta que lo aprio"""
        self.ritmobase = BaseModel()

    def tearDown(self):
        """la puta que lo aprio"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_crearunainstancia(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        self.assertEqual(type(ritmobase.id), str)
        self.assertEqual(type(ritmobase.created_at), datetime)
        self.assertEqual(type(ritmobase.updated_at), datetime)

    def test_idiferente(self):
        """la puta que lo aprio"""
        ritmobase1 = BaseModel(69)
        self.assertNotEqual(ritmobase1.id, 69)
        ritmobase1 = BaseModel("holi")
        self.assertNotEqual(ritmobase1.id, "holi")
        ritmobase1 = BaseModel([0, 1, 2])
        self.assertNotEqual(ritmobase1.id, [0, 1, 2])

    def test_cuandosecreopadre(self):
        """la puta que lo aprio"""
        ritmobase2 = BaseModel()
        self.assertEqual(type(ritmobase2.created_at), type(datetime.now()))
        self.assertTrue(hasattr(ritmobase2, "created_at"))

    def test_cuandoseupdeteoyeyeee(self):
        """la puta que lo aprio"""
        ritmobase2 = BaseModel()
        self.assertEqual(type(ritmobase2.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(ritmobase2, "updated_at"))
        actualizado = ritmobase2.updated_at
        self.assertTrue(actualizado == ritmobase2.updated_at)
        ritmobase2.save()
        self.assertFalse(actualizado == ritmobase2.updated_at)

    def test_crearvariasinstancias(self):
        """la puta que lo aprio"""
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
        """la puta que lo aprio"""
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

    def test_metodostring(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        self.assertEqual(type(str(ritmobase)), str)

    def test_metstrclasname(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        self.assertEqual('[BaseModel]' in str(ritmobase), True)

    def test_strid(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        self.assertEqual('id' in str(ritmobase), True)

    def test_strcreatedat(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        self.assertEqual('created_at' in str(ritmobase), True)

    def test_strupdatedat(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        self.assertEqual('updated_at' in str(ritmobase), True)

    def test_quetira(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        resultante = "[{}] ({}) {}".format(
            ritmobase.__class__.__name__,
            ritmobase.id,
            ritmobase.__dict__
        )
        self.assertEqual(resultante, str(ritmobase))

    def test_gaurdalopapa(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        tiempopachu = ritmobase.updated_at
        sleep(10)
        ritmobase.id = 69
        ritmobase.save()
        tiempokiko = ritmobase.updated_at
        self.assertTrue(hasattr(ritmobase, "id"))
        self.assertTrue(ritmobase.id == 69)
        self.assertNotEqual(tiempokiko, tiempopachu)
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertTrue("\"id\": 69" in f.read())

    def test_todict(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        self.assertEqual(type(ritmobase.to_dict()), dict)

    def test_updatedatsave(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        ritmobase.save()
        self.assertEqual(type(ritmobase.updated_at), type(datetime.now()))
        self.assertEqual(type(ritmobase.updated_at), datetime)
        self.assertTrue(hasattr(ritmobase, "updated_at"))

    def test_dicttoatsall(self):
        """la puta que lo aprio"""
        ritmobase = BaseModel()
        pic = ritmobase.to_dict()
        self.assertEqual('__class__' in pic, True)
        self.assertEqual('id' in pic, True)
        self.assertEqual('created_at' in pic, True)
        self.assertEqual('updated_at' in pic, True)

    def test_argumentoteleton(self):
        """la puta que lo aprio"""
        with self.assertRaises(NameError) as a:
            ritmobase = BaseModel(ea)
        self.assertEqual(str(a.exception), "name 'ea' is not defined")

    def test_demasiadosargumentos(self):
        """la puta que lo aprio"""
        with self.assertRaises(TypeError) as a:
            ritmobase = BaseModel()
            ritmobase.save("eae")
        self.assertEqual(str(a.exception), "save() takes 1 positional" +
                                           " argument but 2 were given")

    def test_guardaint(self):
        """la puta que lo aprio"""
        ritmobase1 = BaseModel()
        with self.assertRaises(TypeError) as a:
            ritmobase1.save(69)

        self.assertEqual(str(a.exception), "save() takes 1 positional" +
                                           " argument but 2 were given")

    def test_demasiadosargumentospadre(self):
        """la puta que lo aprio"""
        with self.assertRaises(TypeError) as a:
            ritmobase = BaseModel()
            ritmobase.to_dict("eae")
        self.assertEqual(str(a.exception), "to_dict() takes 1 positional" +
                                           " argument but 2 were given")

if __name__ == "__main__":
    unittest.main()
