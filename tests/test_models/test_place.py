#!/usr/bin/python3
"""
        import modules of class PlaceTest
"""
import unittest
from datetime import datetime
import os
import models
Place = models.place.Place
BaseModel = models.base_model.BaseModel


class PlaceTest(unittest.TestCase):
    """test cases for class object Place"""

    @classmethod
    def setUp(self):
        """test instance"""
        self.t = Place()

    def tearDown(self):
        """test instance"""
        pass

    def test_Init(self):
        """test instance"""
        self.assertIsInstance(self.t, BaseModel)

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
