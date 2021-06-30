#!/usr/bin/python3
"""
        import modules of class StateTest
"""
import unittest
from models.state import State
import models
from datetime import datetime
import os


class StateTest(unittest.TestCase):
        """test cases for class object State"""

        @classmethod
        def setUp(self):
            """test instance"""
            self.t = Review()

        def test_Init(self):
                """test instance"""
                self.assertIsInstance(self.t, State)

        def test_unique_id(self):
                """ test if it generate unique id"""
                State1 = State()
                State2 = State()
                self.assertNotEqual(State1, State2)

        def test_doc(self):
                """ test if class has docstring"""
                self.assertIsNotNone(models.state.__doc__)
                self.assertIsNotNone(State.__doc__)

if __name__ == "__main__":
    unittest.main()
