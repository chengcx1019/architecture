#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_compress_string.py
@time: 2018/5/28 21:09
"""
import unittest
from basic.array_string.compress_string import CompressString


class MyTestCase(unittest.TestCase):
    def tearDown(self):
        self.test_object = None

    def setUp(self):
        self.test_object = CompressString()

    def test_something(self):
        self.assertEqual(self.test_object.compress(None), None)
        self.assertEqual(self.test_object.compress(''), '')
        self.assertEqual(self.test_object.compress('AAABCCDDDDE'), 'A3BC2D4E')
        self.assertEqual(self.test_object.compress('BAAACCDDDD'), 'BA3C2D4')
        self.assertEqual(self.test_object.compress('AABBCC'), 'AABBCC')
        self.assertEqual(self.test_object.compress('AAABAACCDDDD'), 'A3BA2C2D4')


if __name__ == '__main__':
    unittest.main()
