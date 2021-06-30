#!/usr/bin/python3
"""
        import modules of class PlaceTest
"""
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class ConsoleTest(unittest.TestCase):
        """ test cases for console"""
        def test_helpcommand(self):
                with patch('sys.stdout', new=StringIO()) as f:
                        HBNBCommand().onecmd("show randomname")
                        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")