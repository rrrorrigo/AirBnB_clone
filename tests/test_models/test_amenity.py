#!/usr/bin/python3
"""
        import modules of class AmenityTest
"""
import unittest
from models.amenity import Amenity
from models import amenity
import models
import inspect
Amenity = amenity.Amenity

class AmenityTest(unittest.TestCase):
        """test cases for class object Amenity"""
        @classmethod
        def setUp(cls):
                """test instance"""
                cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

        def tearDown(self):
                """test instance"""
                pass

        def test_Init(self):
                """test instance"""
                self.assertIsInstance(self.t, Amenity)
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
