#!/usr/bin/python3
#test_rectangle.py
"""Defining unittests for rectangle.py

Unittest classes:
                 Testrectangle_instantiation - Line 25
                 Testrectangle_width - Line 114
                 Testrectangle_height - Line 187
                 Testrectangle_x - Line 259
                 Testrectangle_y - Line 330
                 Testrectangle_order_of_init - Line 397
                 Testrectangle_area - Line 421
                 Testrecatangle_str_display - Line 444
                 Testrectangle_updating_args -
                 Test_rectangle_updating_kwargs -
                 Testrectangle_to_dict -

"""

import csv
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class Testrectangle_instantiation(unittest.TestCase):
    """Testing instantiation of the rectangle class"""

    def test_rect_is_base(self):
        self.assertIsInstance(Rectangle(10, 4), Base)

    def testing_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def testing_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def testing_two_args(self):
        rec1 = Rectangle(10, 4)
        rec2 = Rectangle(4, 10)
        self.assertEqual(rec1.id, rec2.id - 1)

    def testing_three_args(self):
        rec1 = Rectangle(2, 4, 8)
        rec2 = Rectangle(4, 2, 2)
        self.assertEqual(rec1.id, rec2.id - 1)

    def testing_four_args(self):
        rec1 = Rectangle(2, 4, 8, 4)
        rec2 = Rectangle(4, 2, 2, 1)
        self.assertEqual(rec1.id, rec2.id - 1)

    def testing_five_args(self):
        self.assertEqual(7, Rectangle(15, 3, 0, 0, 7).id)

    def testing_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 6, 6, 1, 3)

    def testing_width_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5, 0, 0, 1).__width)

    def testing_height_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5, 0, 0, 1).__height)

    def testing_x_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5, 0, 0, 1).__x)

    def testing_y_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5, 0, 0, 1).__y)

    def width_getter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        self.assertEqual(4, rect.width)

    def width_setter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        rect.width = 12
        self.assertEqual(12, rect.width)

    def height_getter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        self.assertEqual(4, rect.height)

    def height_setter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        rect.height = 12
        self.assertEqual(12, rect.height)

    def x_getter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        self.assertEqual(4, rect.x)

    def x_setter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        rect.x = 12
        self.assertEqual(12, rect.x)

    def y_getter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        self.assertEqual(4, rect.y)

    def y_setter_test(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        rect.y = 12
        self.assertEqual(12, rect.y)


class Testrectangle_width(unittest.TestCase):
    """Testing instantiation of the rectangle's width attribute"""

    def testing_None_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 3)

    def testing_str_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("habibi", 3)

    def testing_float_as_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(7.7, 2)

    def testing_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(4), 3)

    def testing_dict_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"h":7, "b":6}, 3)

    def testing_set_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({4,5, 6}, 3)

    def testing_list_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 3, 4], 3)

    def testing_range_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(6), 3)

    def testing_tuple_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((2, 6, 3), 2)

    def testing_frozen_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 3, 4, 1}), 3)

    def testing_bytes_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 3)

    def testing_bytearrays_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'habibi'), 3)

    def testing_memoryview_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'habibi'), 3)

    def testing_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 3)

    def testing_nan_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def testing_neg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)

    def testing_zero_as_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)


class Testrectangle_height(unittest.TestCase):
    """Testing the height attribute of the class Rectangle"""

    def testing_None_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, None)

    def testing_str_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "habibi")

    def testing_float_as_width(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(2, 7.7)

    def testing_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, complex(4))

    def testing_dict_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {"h":7, "b":6})

    def testing_set_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {4,5, 6})

    def testing_list_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, [2, 3, 4])

    def testing_range_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, range(6))

    def testing_tuple_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (2, 6, 3))

    def testing_frozen_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, frozenset({1, 3, 4, 1}))

    def testing_bytes_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, b'Python',)

    def testing_bytearrays_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, bytearray(b'habibi'))

    def testing_memoryview_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, memoryview(b'habibi'))

    def testing_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('inf'))

    def testing_nan_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('nan'))

    def testing_neg_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -3)

    def testing_zero_as_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)


class Testrectangle_x(unittest.TestCase):
    """Testing the x attribute for the class rectangle"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

class Testrectangle_y(unittest.TestCase):
    """Testing y attribute of the class rectangle"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)
   
class Testrectangle_order_of_init(unittest.TestCase):
    """Testing order of attribute initalization"""

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 4, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 4, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class Testrectangle_area(unittest.TestCase):
    """Testing area attribute of the class rectangle"""
    
    def testing_small_area(self):
        rect = Rectangle(10, 2, 1, 1, 1)
        self.assertEqual(20, rect.area())

    def testing_large_area(self):
        rect = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, rect.area())

    def test_area_changed_attr(self):
        rect = Rectangle(2, 10, 1, 1, 2)
        rect.width = 7
        rect.height = 3
        self.assertEqual(21, rect.area())

    def testing_area_one_arg(self):
        rect = Rectangle(2, 5, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect.area(1)

class Testrecatangle_str_display(unittest.TestCase):
    """Unittests for str method and display method"""
    










