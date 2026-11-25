#!/usr/bin/python3
"""Unittests for models/square.py."""
import io
import os
import unittest
import unittest.mock
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Tests for Square instantiation."""

    def test_is_base(self):
        """Square inherits from Base."""
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        """Square inherits from Rectangle."""
        self.assertIsInstance(Square(10), Rectangle)

    def test_no_args(self):
        """No argument raises TypeError."""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Ids increment."""
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        """Two arguments."""
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        """Three arguments."""
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        """Four arguments set id."""
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        """Five arguments raise TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        """__size is private."""
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        """Size getter."""
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        """Size setter changes width and height."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)
        self.assertEqual(8, s.width)
        self.assertEqual(8, s.height)

    def test_x_y_getters(self):
        """x and y getters."""
        s = Square(10, 2, 3)
        self.assertEqual(2, s.x)
        self.assertEqual(3, s.y)

    def test_default_x_y(self):
        """x and y default to 0."""
        s = Square(10)
        self.assertEqual(0, s.x)
        self.assertEqual(0, s.y)


class TestSquareSize(unittest.TestCase):
    """Tests for size validation."""

    def test_none(self):
        """None size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str(self):
        """String size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float(self):
        """Float size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_list(self):
        """List size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2])

    def test_negative(self):
        """Negative size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_zero(self):
        """Zero size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_setter_type(self):
        """Setter checks type."""
        s = Square(2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_setter_value(self):
        """Setter checks value."""
        s = Square(2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0


class TestSquareXY(unittest.TestCase):
    """Tests for x and y validation."""

    def test_x_str(self):
        """String x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_x_float(self):
        """Float x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_x_negative(self):
        """Negative x."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)

    def test_y_str(self):
        """String y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, "invalid")

    def test_y_float(self):
        """Float y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_y_negative(self):
        """Negative y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)

    def test_size_before_x(self):
        """Size is checked before x."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid", "invalid")

    def test_x_before_y(self):
        """x is checked before y."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid", "invalid")


class TestSquareArea(unittest.TestCase):
    """Tests for area."""

    def test_small(self):
        """Small area."""
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_large(self):
        """Large area."""
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_changed(self):
        """Area after change."""
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())

    def test_one_arg(self):
        """Argument raises TypeError."""
        with self.assertRaises(TypeError):
            Square(2, 10, 1, 1).area(1)


class TestSquareDisplay(unittest.TestCase):
    """Tests for display and __str__."""

    @staticmethod
    def capture(sq, method):
        """Capture stdout of display or print."""
        out = io.StringIO()
        with unittest.mock.patch("sys.stdout", out):
            if method == "print":
                print(sq)
            else:
                sq.display()
        return out.getvalue()

    def test_str_print(self):
        """Print a square."""
        s = Square(4, 2, 1, 12)
        self.assertEqual("[Square] (12) 2/1 - 4\n", self.capture(s, "print"))

    def test_str_default(self):
        """__str__ with default x, y."""
        self.assertEqual("[Square] (1) 0/0 - 4", str(Square(4, id=1)))

    def test_str_changed(self):
        """__str__ after changes."""
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_one_arg(self):
        """__str__ with argument raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4).__str__(1)

    def test_display_size(self):
        """Display without x, y."""
        s = Square(2, 0, 0, 9)
        self.assertEqual("##\n##\n", self.capture(s, "display"))

    def test_display_x(self):
        """Display with x."""
        s = Square(3, 1, 0, 18)
        self.assertEqual(" ###\n ###\n ###\n", self.capture(s, "display"))

    def test_display_y(self):
        """Display with y."""
        s = Square(2, 0, 1, 9)
        self.assertEqual("\n##\n##\n", self.capture(s, "display"))

    def test_display_x_y(self):
        """Display with x and y."""
        s = Square(2, 3, 2, 1)
        self.assertEqual("\n\n   ##\n   ##\n", self.capture(s, "display"))

    def test_display_one_arg(self):
        """Display with argument raises TypeError."""
        with self.assertRaises(TypeError):
            Square(3, 4, 5, 2).display(1)


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for update with *args."""

    def test_zero(self):
        """No args changes nothing."""
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_one(self):
        """Update id."""
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_two(self):
        """Update id, size."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_three(self):
        """Update id, size, x."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_four(self):
        """Update all."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_twice(self):
        """Update twice."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(s))

    def test_size_sets_width_height(self):
        """Updated size sets width and height."""
        s = Square(10, 10, 10, 10)
        s.update(1, 7)
        self.assertEqual(7, s.width)
        self.assertEqual(7, s.height)

    def test_invalid_size(self):
        """Invalid size in args."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_zero_size(self):
        """Zero size in args."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_negative_x(self):
        """Negative x in args."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_invalid_y(self):
        """Invalid y in args."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for update with **kwargs."""

    def test_one(self):
        """Update id."""
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_two(self):
        """Update size and id."""
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_all(self):
        """Update all."""
        s = Square(10, 10, 10, 10)
        s.update(id=89, y=1, x=12, size=7)
        self.assertEqual("[Square] (89) 12/1 - 7", str(s))

    def test_args_and_kwargs(self):
        """Args take priority over kwargs."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_invalid_size(self):
        """Invalid size in kwargs."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_negative_x(self):
        """Negative x in kwargs."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_wrong_keys(self):
        """Unknown keys are ignored."""
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))


class TestSquareToDictionary(unittest.TestCase):
    """Tests for to_dictionary."""

    def test_output(self):
        """Dictionary content."""
        s = Square(10, 2, 1, 1)
        d = {"id": 1, "x": 2, "size": 10, "y": 1}
        self.assertDictEqual(d, s.to_dictionary())

    def test_type(self):
        """Returns a dict."""
        self.assertEqual(dict, type(Square(10, 2, 1, 1).to_dictionary()))

    def test_no_object_changes(self):
        """Update from dictionary."""
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)
        self.assertEqual(str(s1), str(s2))

    def test_arg(self):
        """Argument raises TypeError."""
        with self.assertRaises(TypeError):
            Square(10, 10, 10, 10).to_dictionary(1)


class TestSquareSaveToFile(unittest.TestCase):
    """Tests for Square.save_to_file."""

    def tearDown(self):
        """Delete created file."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_empty_list(self):
        """Square.save_to_file([]) writes '[]'."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_none(self):
        """Square.save_to_file(None) writes '[]'."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_one_square(self):
        """Square.save_to_file with one square."""
        Square.save_to_file([Square(1, 2, 3, 4)])
        with open("Square.json", "r") as f:
            data = Square.from_json_string(f.read())
        self.assertEqual([{"id": 4, "size": 1, "x": 2, "y": 3}], data)


if __name__ == "__main__":
    unittest.main()
