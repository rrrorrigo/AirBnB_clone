#!/usr/bin/python3
"""
        import modules of class AmenityTest
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import models
from datetime import datetime
import os
import pep8
import inspect


class AmenityTest(unittest.TestCase):
        """test cases for class object Amenity"""
        def test_is_subclass(self):
            """Test that Amenity is a subclass of BaseModel"""
            amenity = Amenity()
            self.assertIsInstance(amenity, BaseModel)
            self.assertTrue(hasattr(amenity, "id"))
            self.assertTrue(hasattr(amenity, "created_at"))
            self.assertTrue(hasattr(amenity, "updated_at"))

        def test_unique_id(self):
                """ test if it generate unique id"""
                Amenity1 = Amenity()
                Amenity2 = Amenity()
                self.assertNotEqual(Amenity1, Amenity2)

        def test_doc(self):
                """ test if class has docstring"""
                self.assertIsNotNone(models.amenity.__doc__)
                self.assertIsNotNone(Amenity.__doc__)

if __name__ == "__main__":
    unittest.main()
