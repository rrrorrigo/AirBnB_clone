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
        Storage = FileStorage()
        self.assertTrue(type(Storage) == FileStorage)
        self.assertTrue(isinstance(Storage, FileStorage))
    
    def test_privastor(self):
        Storage = FileStorage()
        with self.assertRaises(AttributeError) as a:
            print(Storage.__objects)
        self.assertEqual(str(e.exception),
                         "'FileStorage' object has no" +
                         " attribute '_TestFileStorageClass_objects'")



