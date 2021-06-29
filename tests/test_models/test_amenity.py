#!/usr/bin/python3
"""
        import modules of class AmenityTest
"""
import unittest
from models.amenity import Amenity
import models
from datetime import datetime
import os


class AmenityTest(unittest.TestCase):
        """test cases for class object Amenity"""
        def test_Init(self):
                """test instance"""
                t = Amenity()
                self.assertIsInstance(t, Amenity)

        def test_unique_id(self):
                """ test if it generate unique id"""
                Amenity1 = Amenity()
                Amenity2 = Amenity()
                self.assertNotEqual(Amenity1, Amenity2)

        def test_doc(self):
                """ test if class has docstring"""
        for f in self.amenity_f:
            self.assertIsNot(f[1].__doc__, None,
                             "{:s} method needs a docstring".format(f[0]))
            self.assertTrue(len(f[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(f[0]))

if __name__ == "__main__":
    unittest.main()
