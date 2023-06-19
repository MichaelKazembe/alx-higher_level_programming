#!/usr/bin/python3

""" test_square Unittest """

import unittest
from io import StringIO
import sys
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def checking(self):
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(size.__doc__)
        self.assertIsNotNone(update.__doc__)
        self.assertIsNotNone(to_dictionary.__doc__)

    def test_style_square(self):
        """ Tests for pep8 """
        style = pep8.StyleGuide(quiet=True)
        pp = style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(pp.total_errors, 0, "fix pep8")
        pp = style.check_files(['models/square.py'])
        self.assertEqual(pp.total_errors, 0, "fix pep8")

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects == 0
        cls.sq1 = Square(2, 2)
        cls.sq2 = Square(size=4, x=2, y=3)

    def test_id(self):
        self.assertTrue(self.sq1.id, 1)
        self.assertTrue(self.sq2.id, 2)

    def test_area(self):
        self.assertTrue(self.sq1.area(), 4)
        self.assertTrue(self.sq2.area(), 16)

    def test_attr_square(self):
        with self.assertRaises(TypeError):
            Square('A')
        with self.assertRaises(ValueError):
            Square(-4)
        with self.assertRaises(ValueError):
            Square(size=1, x=-1)
        with self.assertRaises(TypeError):
            Square(size=1, y='A')

    def test_str(self):
        self.assertNotEqual(str(self.sq1), '[Square] (2) 2/0 - 2')
        self.assertEqual(str(self.sq2), '[Square] (4) 2/3 - 4')

    def test_update(self):
        temp = Square(5)
        temp.update(10)
        self.assertEqual(str(temp), '[Square] (10) 0/0 - 5')
        temp.update(1, 2)
        self.assertEqual(str(temp), '[Square] (1) 0/0 - 2')
        temp.update(1, 2, 3)
        self.assertEqual(str(temp), '[Square] (1) 3/0 - 2')

    def test_display(self):
        Base._Base__nb_objects = 0
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        rec1 = Square(4)
        rec1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "####\n####\n####\n####\n")
        sys.stdout = mystdout = StringIO()
        rec1 = Rectangle(2, 2, 2, 2)
        rec1.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n")
        sys.stdout = old_stdout

    def test_dictionary(self):
        Base._Base__nb_objects = 0
        rec1 = Square(2, 2, 2, 2)
        rec1_dictionary = rec1.to_dictionary()
        self.assertDictEqual(rec1_dictionary, {
            'x': 2, 'y': 2, 'size': 2, 'id': 2})
        rec1 = Rectangle(1, 1)
        rec1_dictionary = rec1.to_dictionary()
        self.assertDictEqual(rec1_dictionary, {
            'x': 0, 'y': 0, 'width': 1, 'height': 1, 'id': 1})

if __name__ == '__main__':
    unittest.main()
