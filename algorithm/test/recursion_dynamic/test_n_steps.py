#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_n_steps.py
@time: 2018/5/29 00:03
"""
import unittest
from basic.recursion_dynamic.n_steps import NSteps


class TestNSteps(unittest.TestCase):
    def tearDown(self):
        self.test_object = None

    def setUp(self):
        self.test_object = NSteps()

    def test_something(self):
        # self.assertRaises(self.test_object.n_steps(None), TypeError)
        self.assertEqual(self.test_object.n_steps(0), 1)
        self.assertEqual(self.test_object.n_steps(1), 1)
        self.assertEqual(self.test_object.n_steps(2), 2)
        self.assertEqual(self.test_object.n_steps(3), 4)
        self.assertEqual(self.test_object.n_steps(4), 7)
        self.assertEqual(self.test_object.n_steps(10), 274)


if __name__ == '__main__':
    unittest.main()
