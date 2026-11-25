#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max is the last element of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max is found in an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max is the first element."""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_in_middle(self):
        """Max is in the middle of the list."""
        self.assertEqual(max_integer([1, 2, 99, 4, 5]), 99)

    def test_max_at_end(self):
        """Max is the last element."""
        self.assertEqual(max_integer([5, 4, 3, 100]), 100)

    def test_one_element(self):
        """A list with one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument uses the default empty list and returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Max of negative numbers."""
        self.assertEqual(max_integer([-5, -2, -9, -1]), -1)

    def test_positive_and_negative(self):
        """Max of mixed positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_all_equal(self):
        """All equal elements."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_duplicate_max(self):
        """Max appears several times."""
        self.assertEqual(max_integer([1, 8, 8, 2]), 8)

    def test_zero(self):
        """List of zeros and negatives."""
        self.assertEqual(max_integer([0, -1, -2]), 0)

    def test_floats(self):
        """Max of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_int_and_float(self):
        """Max of mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_big_numbers(self):
        """Max of very big integers."""
        self.assertEqual(max_integer([10 ** 20, 10 ** 10, 5]), 10 ** 20)

    def test_infinity(self):
        """Infinity is the max."""
        self.assertEqual(max_integer([1, float('inf'), 3]), float('inf'))

    def test_tuple(self):
        """A tuple works since it supports len and indexing."""
        self.assertEqual(max_integer((1, 5, 2)), 5)

    def test_string(self):
        """A string returns its greatest character."""
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        """A list of strings returns the greatest string."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_list_of_lists(self):
        """A list of lists compares them in order."""
        self.assertEqual(max_integer([[1, 2], [3], [1, 5]]), [3])

    def test_mixed_types(self):
        """Comparing a string with an integer raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 2])

    def test_none_argument(self):
        """None has no length, so TypeError is raised."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_integer_argument(self):
        """An integer has no length, so TypeError is raised."""
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_list_with_none(self):
        """None inside a list cannot be compared to an integer."""
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_input_not_modified(self):
        """The list is not modified by the function."""
        data = [3, 1, 2]
        max_integer(data)
        self.assertEqual(data, [3, 1, 2])


if __name__ == '__main__':
    unittest.main()
