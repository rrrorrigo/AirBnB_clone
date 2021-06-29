#!/usr/bin/python3
"""la puta que lo aprio"""
from models.engine.file_storage import FileStorage
import models
import unittest
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import path
import os
from datetime import datetime


class fileestoraesoepapa(unittest.TestCase):
    """la puta que lo aprio"""

    @classmethod
    def setUp(self):
        """la puta que lo aprio"""
        pass

    def tearDown(self):
        """la puta que lo aprio"""
        if os.path.exists("file.json"):
            os.rename("file.json", "eae")

    def test_creation(self):
        """la puta que lo aprio"""
        Storage = FileStorage()
        self.assertTrue(type(Storage) == FileStorage)
        self.assertTrue(isinstance(Storage, FileStorage))
    
    def test_privastor(self):
        """la puta que lo aprio"""
        Storage = FileStorage()
        with self.assertRaises(AttributeError) as a:
            print(Storage.__objects)
        self.assertEqual(str(a.exception),
                         "'FileStorage' object has no" +
                         " attribute '_fileestoraesoepapa__objects'")

    def test_atr(self):
        """la puta que lo aprio"""
        Storage = FileStorage()
        Storage.reload()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

if __name__ == "__main__":
    unittest.main()
