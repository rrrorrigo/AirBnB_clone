#!/usr/bin/python3
"""
        import modules of class PlaceTest
"""
import unittest
from models.place import Place
from models import place
import models
import inspect
Place = place.Place


class PlaceTest(unittest.TestCase):
        """test cases for class object Place"""
        @classmethod
        def setUp(cls):
                """test instance"""
                cls.place_f = inspect.getmembers(Place, inspect.isfunction)

        def tearDown(self):
                """test instance"""
                pass

        def test_Init(self):
                """test instance"""
                t = Place()
                self.assertIsInstance(t, Place)

        def test_unique_id(self):
                """ test if it generate unique id"""
                Place1 = Place()
                Place2 = Place()
                self.assertNotEqual(Place1, Place2)

        def test_doc(self):
                """ test if class has docstring"""
                self.assertIsNotNone(models.place.__doc__)
                self.assertIsNotNone(Place.__doc__)

if __name__ == "__main__":
    unittest.main()
