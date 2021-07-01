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
        """ test cases for help command"""
        m1 = "\nDocumented commands (type help <topic>):\n"
        m2 = "========================================\n"
        m3 = "EOF  all  count  create  destroy  help  quit  show  update\n\n"
        hmsg = m1 + m2 + m3
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help randomname")
            self.assertEqual(f.getvalue(), "*** No help on randomname\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(), " exit of command interpreter\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue(), " exit of command interpreter\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(f.getvalue(), hmsg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue(), " exit of command interpreter\n")
