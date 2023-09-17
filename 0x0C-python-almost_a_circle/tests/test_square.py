#!/usr/bin/python3
"""Defining unittests for square.py
                  
                Testsquare_instantiation - Line 24
                Testsquare_size -
                Testsquare_x - 
                Testsquare_y - 
                Testsquare_order_of_init - 
                Testsquare_area - 
                Testsqaure_str_display -
                Testsquare_updating_args - 
                Test_square_updating_kwargs - 
                Testsquare_to_dict - Line 

"""

import csv
import io
import sys
import unittest
from models.base import Base
from models.square import Square

class Testsquare_instantiation(unittest.TestCase):
    """test instantiation of the square class"""

    def test_sq_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_is_square(self):
        self.assertIsInstance(Square(10), Square)

    def test_one_arg(self):
            sqr1 = Square(12)
            sqr2 = Square(10)
            self.assertEqual(sqr1.id, sqr2.id - 1)

    def test_two_args(self):
        sqr1 = Square(10, 4)
        sqr2 = Square(4, 10)
        self.assertEqual(sqr1.id, sqr2.id - 1)

    def test_three_args(self):
        sqr1 = Square(2, 4, 8)
        sqr2 = Square(4, 2, 2)
        self.assertEqual(sqr1.id, sqr2.id - 1)

    def test_four_args(self):
        self.assertEqual(8, Square(2, 4, 8, 8).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(2, 4, 6, 6, 1)