#!/usr/bin/python3
"""
        import modules of class StateTest
"""
import unittest
from datetime import datetime
import os
import models
State = models.state.State
BaseModel = models.base_model.BaseModel


class StateTest(unittest.TestCase):
    """test cases for class object State"""

    @classmethod
    def setUp(self):
        """test instance"""
        self.t = State()

    def tearDown(self):
        """test instance"""
        pass

    def test_Init(self):
        """test instance"""
        self.assertIsInstance(self.t, BaseModel)

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
