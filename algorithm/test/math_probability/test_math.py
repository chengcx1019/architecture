#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_math.py
@time: 2018/5/29 06:48
"""
import unittest
from basic.math_probability.math import Math


class MyTestCase(unittest.TestCase):
    def tearDown(self):
        self.test_object = None

    def setUp(self):
        self.test_object = Math()

    def test_something(self):
        self.assertRaises(TypeError, self.test_object.check_prime, None)
        self.assertRaises(TypeError, self.test_object.check_prime, 98.6)
        self.assertEqual(self.test_object.check_prime(0), False)
        self.assertEqual(self.test_object.check_prime_optimized(1), False)
        self.assertEqual(self.test_object.check_prime(4), False)
        self.assertEqual(self.test_object.check_prime_optimized(4), False)
        self.assertEqual(self.test_object.check_prime(97), True)
        self.assertEqual(self.test_object.check_prime_optimized(97), True)


if __name__ == '__main__':
    unittest.main()
