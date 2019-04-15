#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_uber_interview.py
@time: 2018/5/22 01:04
"""
import unittest
from BadRomance.practice.uber_interview import validate

class TestUberInterview(unittest.TestCase):

    def tearDown(self):
        pass
    def setUp(self):
        pass

    def test1(self):
        rules = ["A NW B","A N B"]
        self.assertEqual(validate(rules), True)

    def test2(self):
        rules = ["A N B","C SE B","C N A","B S C"]
        self.assertEqual(validate(rules), False)

    def test3(self):
        rules = ["A N B","C N B"]
        self.assertEqual(validate(rules), True)

    def test4(self):
        rules = ["A WN B","C ES B", "C ES A"]
        self.assertEqual(validate(rules), True)

    def test_final(self):
        rules = ['A N B', 'B N C', 'C N A']
        self.assertEqual(validate(rules), False)

if __name__ == '__main__':
    pass