 #!/usr/bin/python3
""" test_rectangle """

import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):

    def checking_docstring(self):
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(width.__doc__)
        self.assertIsNotNone(height.__doc__)
        self.assertIsNotNone(x.__doc__)
        self.assertIsNotNone(y.__doc__)
        self.assertIsNotNone(area.__doc__)
        self.assertIsNotNone(display.__doc__)
        self.assertIsNotNone(__str__.__doc__)
        self.assertIsNotNone(update.__doc__)
        self.assertIsNotNone(to_dictionary.__doc__)

    def test_style_rect(self):
        """ Tests for pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects == 0
        cls.rec1 = Rectangle(10, 2)
        cls.rec3 = Rectangle(2, 4, 2, 2, 12)

    def test_ids(self):
        self.assertEqual(self.rec1.id, 2)
        self.assertEqual(self.rec3.id, 12)
        self.rec3.id = "b"
        self.assertEqual(self.rec3.id, "b")

    def test_attr_errors(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError, msg="height must be an integer"):
            rec11 = Rectangle(10, "2")
        with self.assertRaises(ValueError, msg="height must be  > 0"):
            rec11 = Rectangle(-2, 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            rec11 = Rectangle({1: 2}, 2)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            rec21 = Rectangle(10, 2)
            rec21.width = -10
        with self.assertRaises(TypeError, msg="x must be an integer"):
            rec31 = Rectangle(10, 2)
            rec31.x = {}
        with self.assertRaises(ValueError, msg="y must be >=0"):
            rec41 = Rectangle(10, 2, 3, -1)

    def test_area(self):
        self.assertEqual(self.rec1.area(), 20)
        self.assertEqual(self.rec3.area(), 8)

    def test_display(self):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.rec1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "##########\n##########\n")
        sys.stdout = mystdout = StringIO()
        self.rec3.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n  ##\n  ##\n")
        sys.stdout = old_stdout

    def test_str(self):
        self.assertEqual(self.rec1.__str__(), "[Rectangle] (2) 0/0 - 10/2")
        self.assertEqual(self.rec3.__str__(), "[Rectangle] (b) 2/2 - 2/4")

    def test_update(self):
        self.rec1.update(89)
        self.assertEqual(self.rec1.__str__(), "[Rectangle] (89) 0/0 - 10/2")
        self.rec1.update(89, 2)
        self.assertEqual(self.rec1.__str__(), "[Rectangle] (89) 0/0 - 2/2")
        self.rec1.update(89, 2, 3)
        self.assertEqual(self.rec1.__str__(), "[Rectangle] (89) 0/0 - 2/3")
        self.rec1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.rec1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        with self.assertRaises(ValueError, msg="x must be >=0"):
            self.rec1.update(y=1, width=2, x=-3, id=89)

    def test_dictionary(self):
        rec1_dictionary = self.rec1.to_dictionary()
        self.assertDictEqual(rec1_dictionary, {
            'x': 0, 'y': 0, 'width': 10, 'height': 2, 'id': 2})
        rec3_dictionary = self.rec3.to_dictionary()
        self.assertDictEqual(rec3_dictionary, {
            'x': 2, 'y': 2, 'width': 2, 'height': 4, 'id': 12})

    def test_to_json(self):
        dict = self.rec1.to_dictionary()
        self.assertIsInstance(Base.to_json_string(dict), str)


if __name__ == '__main__':
    unittest.main()
