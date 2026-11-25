#!/usr/bin/python3
"""Unittests for models/rectangle.py."""
import io
import unittest
import unittest.mock
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for Rectangle instantiation."""

    def test_is_base(self):
        """Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """No argument raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """One argument raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Ids increment with two arguments."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Three arguments."""
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Four arguments."""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """Five arguments sets id."""
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """Six arguments raise TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """__width is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """__height is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """__x is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """__y is private."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_getters(self):
        """Getters return values."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)
        self.assertEqual(7, r.height)
        self.assertEqual(7, r.x)
        self.assertEqual(5, r.y)

    def test_setters(self):
        """Setters change values."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        r.height = 11
        r.x = 12
        r.y = 13
        self.assertEqual((10, 11, 12, 13), (r.width, r.height, r.x, r.y))

    def test_default_x_y(self):
        """x and y default to 0."""
        r = Rectangle(5, 7)
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)


class TestRectangleWidth(unittest.TestCase):
    """Tests for width validation."""

    def test_none(self):
        """None width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str(self):
        """String width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float(self):
        """Float width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_list(self):
        """List width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2], 2)

    def test_dict(self):
        """Dict width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1}, 2)

    def test_bool(self):
        """Bool width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_setter_type(self):
        """Setter checks type."""
        r = Rectangle(1, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "1"

    def test_negative(self):
        """Negative width."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero(self):
        """Zero width."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_setter_value(self):
        """Setter checks value."""
        r = Rectangle(1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -5


class TestRectangleHeight(unittest.TestCase):
    """Tests for height validation."""

    def test_none(self):
        """None height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str(self):
        """String height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float(self):
        """Float height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_tuple(self):
        """Tuple height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2))

    def test_negative(self):
        """Negative height."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero(self):
        """Zero height."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangleX(unittest.TestCase):
    """Tests for x validation."""

    def test_none(self):
        """None x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str(self):
        """String x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float(self):
        """Float x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_negative(self):
        """Negative x."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

    def test_zero(self):
        """Zero x is valid."""
        self.assertEqual(0, Rectangle(5, 3, 0, 0).x)


class TestRectangleY(unittest.TestCase):
    """Tests for y validation."""

    def test_none(self):
        """None y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str(self):
        """String y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float(self):
        """Float y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_negative(self):
        """Negative y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)

    def test_zero(self):
        """Zero y is valid."""
        self.assertEqual(0, Rectangle(5, 3, 0, 0).y)


class TestRectangleOrder(unittest.TestCase):
    """Tests for the order of validation."""

    def test_width_before_height(self):
        """Width is checked first."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", "invalid")

    def test_height_before_x(self):
        """Height is checked before x."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid", "invalid")

    def test_x_before_y(self):
        """x is checked before y."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", "invalid")


class TestRectangleArea(unittest.TestCase):
    """Tests for area."""

    def test_small(self):
        """Small area."""
        self.assertEqual(20, Rectangle(10, 2, 0, 0, 0).area())

    def test_large(self):
        """Large area."""
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_changed(self):
        """Area after change."""
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_one_arg(self):
        """Argument raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(2, 10).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for display and __str__."""

    @staticmethod
    def capture(rect, method):
        """Capture stdout of display or print."""
        out = io.StringIO()
        with unittest.mock.patch("sys.stdout", out):
            if method == "print":
                print(rect)
            else:
                rect.display()
        return out.getvalue()

    def test_str_print(self):
        """Print a rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6\n",
                         self.capture(r, "print"))

    def test_str_width_height(self):
        """__str__ with default x, y."""
        r = Rectangle(4, 6, id=1)
        self.assertEqual("[Rectangle] (1) 0/0 - 4/6", str(r))

    def test_str_changed(self):
        """__str__ after changes."""
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_one_arg(self):
        """__str__ with argument raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5).__str__(1)

    def test_display_width_height(self):
        """Display without x, y."""
        r = Rectangle(2, 3, 0, 0, 0)
        self.assertEqual("##\n##\n##\n", self.capture(r, "display"))

    def test_display_x(self):
        """Display with x."""
        r = Rectangle(3, 2, 1, 0, 1)
        self.assertEqual(" ###\n ###\n", self.capture(r, "display"))

    def test_display_y(self):
        """Display with y."""
        r = Rectangle(4, 5, 0, 1, 0)
        expected = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(expected, self.capture(r, "display"))

    def test_display_x_y(self):
        """Display with x and y."""
        r = Rectangle(2, 4, 3, 2, 0)
        expected = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(expected, self.capture(r, "display"))

    def test_display_one_arg(self):
        """Display with argument raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(5, 1, 2, 4, 7).display(1)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for update with *args."""

    def test_zero(self):
        """No args changes nothing."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_one(self):
        """Update id."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_two(self):
        """Update id, width."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_three(self):
        """Update id, width, height."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_four(self):
        """Update id, width, height, x."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_five(self):
        """Update all."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_twice(self):
        """Update twice."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        r.update(6, 5, 4, 3, 2)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_invalid_width(self):
        """Invalid width in args."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_zero_width(self):
        """Zero width in args."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_invalid_height(self):
        """Invalid height in args."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid")

    def test_negative_x(self):
        """Negative x in args."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_invalid_y(self):
        """Invalid y in args."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 1, 2, 3, "invalid")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for update with **kwargs."""

    def test_one(self):
        """Update id."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_two(self):
        """Update width and id."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_all(self):
        """Update all."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_args_and_kwargs(self):
        """Args take priority over kwargs."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_invalid_width(self):
        """Invalid width in kwargs."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_negative_y(self):
        """Negative y in kwargs."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_wrong_keys(self):
        """Unknown keys are ignored."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for to_dictionary."""

    def test_output(self):
        """Dictionary content."""
        r = Rectangle(10, 2, 1, 9, 5)
        d = {"x": 1, "y": 9, "id": 5, "height": 2, "width": 10}
        self.assertDictEqual(d, r.to_dictionary())

    def test_type(self):
        """Returns a dict."""
        self.assertEqual(dict, type(Rectangle(10, 2, 1, 9, 5).to_dictionary()))

    def test_no_object_changes(self):
        """Update from dictionary."""
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)
        self.assertEqual(str(r1), str(r2))

    def test_arg(self):
        """Argument raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 4, 1, 2).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
