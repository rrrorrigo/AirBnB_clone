#!/usr/bin/python3
"""
        import modules of class CityTest
"""
import unittest
from datetime import datetime
import os
import models
from models.city import City
from models.base_model import BaseModel


class CityTest(unittest.TestCase):
    """test cases for class object City"""

    @classmethod
    def setUp(self):
        """test instance"""
        self.t = City()

    def tearDown(self):
        """test instance"""
        pass

    def test_Init(self):
        """test instance"""
        self.assertIsInstance(self.t, BaseModel)

    def test_unique_id(self):
        """ test if it generate unique id"""
        City1 = City()
        City2 = City()
        self.assertNotEqual(City1, City2)

    def test_doc(self):
        """ test if class has docstring"""
        self.assertIsNotNone(models.city.__doc__)
        self.assertIsNotNone(City.__doc__)

if __name__ == "__main__":
    unittest.main()
