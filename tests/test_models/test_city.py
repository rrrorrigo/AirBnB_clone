#!/usr/bin/python3
"""
        import modules of class CityTest
"""
import unittest
from models.city import City
import models
from datetime import datetime
import os


class CityTest(unittest.TestCase):
        """test cases for class object City"""
        def test_Init(self):
                """test instance"""
                t = City()
                self.assertIsInstance(t, City)

        def test_unique_id(self):
                """ test if it generate unique id"""
                City1 = City()
                City2 = City()
                self.assertNotEqual(City1, City2)

        def test_doc(self):
                """ test if class has docstring"""
                self.assertIsNotNone(models.city.__doc__)
                self.assertIsNotNone(City.__doc__)