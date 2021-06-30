#!/usr/bin/python3
"""
        import modules of class AmenityTest
"""
import unittest
from models.amenity import Amenity
import models
from datetime import datetime
import os
import pep8
import inspect


class TestAmenityDocs(unittest.TestCase):
    """test cases for class object Amenity"""
    @classmethod
    def setUpClass(cls):
        """test cases for class object Amenity"""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_amenity_module_docstring(self):
        """test cases for class object Amenity"""
        self.assertIsNot(Amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """test cases for class object Amenity"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """test cases for class object Amenity"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


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
                self.assertIsNotNone(models.amenity.__doc__)
                self.assertIsNotNone(Amenity.__doc__)

if __name__ == "__main__":
    unittest.main()
