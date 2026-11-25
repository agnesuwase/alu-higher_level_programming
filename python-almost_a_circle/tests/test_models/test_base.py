#!/usr/bin/python3
"""Unittests for models/base.py."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Tests for Base instantiation and ids."""

    def test_no_arg(self):
        """Ids without argument increment by one."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_three_bases(self):
        """Three bases get consecutive ids."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 2)

    def test_none_id(self):
        """None id behaves like no id."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        """Given id is used."""
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_increment(self):
        """Given id does not change the counter."""
        b1 = Base()
        Base(98)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 1)

    def test_id_public(self):
        """Id can be changed."""
        b = Base(5)
        b.id = 15
        self.assertEqual(b.id, 15)

    def test_nb_objects_private(self):
        """__nb_objects is private."""
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects)

    def test_negative_id(self):
        """Negative id is stored as is."""
        self.assertEqual(Base(-5).id, -5)

    def test_string_id(self):
        """String id is stored as is."""
        self.assertEqual(Base("hello").id, "hello")

    def test_float_id(self):
        """Float id is stored as is."""
        self.assertEqual(Base(5.5).id, 5.5)

    def test_list_id(self):
        """List id is stored as is."""
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_two_args(self):
        """Two arguments raise TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_type(self):
        """Returns a string."""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_rectangle_one_dict(self):
        """One rectangle dictionary."""
        r = Rectangle(10, 7, 2, 8, 6)
        s = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(json.loads(s), [r.to_dictionary()])

    def test_rectangle_two_dicts(self):
        """Two rectangle dictionaries."""
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(json.loads(Base.to_json_string(dicts)), dicts)

    def test_square_one_dict(self):
        """One square dictionary."""
        s = Square(10, 2, 3, 4)
        js = Base.to_json_string([s.to_dictionary()])
        self.assertEqual(json.loads(js), [s.to_dictionary()])

    def test_square_two_dicts(self):
        """Two square dictionaries."""
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertEqual(json.loads(Base.to_json_string(dicts)), dicts)

    def test_empty_list(self):
        """Empty list gives '[]'."""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none(self):
        """None gives '[]'."""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_args(self):
        """No argument raises TypeError."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_than_one_arg(self):
        """Two arguments raise TypeError."""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseFromJsonString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_type(self):
        """Returns a list."""
        s = '[{"id": 89, "width": 10, "height": 4}]'
        self.assertEqual(list, type(Base.from_json_string(s)))

    def test_one_rectangle(self):
        """One rectangle dictionary."""
        data = [{"id": 89, "width": 10, "height": 4, "x": 7, "y": 8}]
        s = Base.to_json_string(data)
        self.assertEqual(data, Base.from_json_string(s))

    def test_two_rectangles(self):
        """Two rectangle dictionaries."""
        data = [{"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
                {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3}]
        s = Base.to_json_string(data)
        self.assertEqual(data, Base.from_json_string(s))

    def test_one_square(self):
        """One square dictionary."""
        data = [{"id": 89, "size": 10, "x": 7, "y": 8}]
        s = Base.to_json_string(data)
        self.assertEqual(data, Base.from_json_string(s))

    def test_empty_string(self):
        """Empty string gives []."""
        self.assertEqual([], Base.from_json_string(""))

    def test_empty_list_string(self):
        """'[]' gives []."""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_none(self):
        """None gives []."""
        self.assertEqual([], Base.from_json_string(None))

    def test_no_args(self):
        """No argument raises TypeError."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_more_than_one_arg(self):
        """Two arguments raise TypeError."""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBaseSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file."""

    def tearDown(self):
        """Delete created files."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_one_rectangle(self):
        """Save one rectangle."""
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [r.to_dictionary()])

    def test_two_rectangles(self):
        """Save two rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(json.loads(f.read()),
                             [r1.to_dictionary(), r2.to_dictionary()])

    def test_one_square(self):
        """Save one square."""
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [s.to_dictionary()])

    def test_two_squares(self):
        """Save two squares."""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertEqual(json.loads(f.read()),
                             [s1.to_dictionary(), s2.to_dictionary()])

    def test_overwrite(self):
        """Saving again overwrites the file."""
        Square.save_to_file([Square(9, 2, 39, 2)])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [s.to_dictionary()])

    def test_none_rectangle(self):
        """None saves '[]'."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_none_square(self):
        """None saves '[]'."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_empty_list(self):
        """Empty list saves '[]'."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_no_args(self):
        """No argument raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_more_than_one_arg(self):
        """Two arguments raise TypeError."""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBaseCreate(unittest.TestCase):
    """Tests for Base.create."""

    def test_rectangle_original(self):
        """Created rectangle has same values."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_rectangle_is_not(self):
        """Created rectangle is a new object."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_rectangle_type(self):
        """Created object is a Rectangle."""
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        self.assertIsInstance(r, Rectangle)

    def test_square_original(self):
        """Created square has same values."""
        s1 = Square(3, 5, 1, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_square_is_not(self):
        """Created square is a new object."""
        s1 = Square(3, 5, 1, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_square_type(self):
        """Created object is a Square."""
        s = Square.create(**{"id": 89, "size": 4})
        self.assertIsInstance(s, Square)


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file."""

    def tearDown(self):
        """Delete created files."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_rectangles(self):
        """Load two rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(loaded[0]))
        self.assertEqual(str(r2), str(loaded[1]))

    def test_rectangle_types(self):
        """Loaded objects are Rectangles."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        self.assertTrue(all(type(o) is Rectangle
                            for o in Rectangle.load_from_file()))

    def test_squares(self):
        """Load two squares."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(str(s1), str(loaded[0]))
        self.assertEqual(str(s2), str(loaded[1]))

    def test_square_types(self):
        """Loaded objects are Squares."""
        Square.save_to_file([Square(5, 1, 3, 3)])
        self.assertTrue(all(type(o) is Square
                            for o in Square.load_from_file()))

    def test_file_does_not_exist(self):
        """Missing file gives []."""
        self.assertEqual([], Rectangle.load_from_file())
        self.assertEqual([], Square.load_from_file())

    def test_more_than_one_arg(self):
        """An argument raises TypeError."""
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
