#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_fibonacci.py
@time: 2018/5/28 14:10
"""
import unittest
from basic.recursion_dynamic.fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    
    def tearDown(self):
        self.fibonacci = None

    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_iterative(self):
        self.assertEqual(self.fibonacci.fibo_iterative(9), 34)

    def test_recursive(self):
        self.assertEqual(self.fibonacci.fibo_recursive(1), 1)
        self.assertEqual(self.fibonacci.fibo_recursive(1), 1)
        self.assertEqual(self.fibonacci.fibo_recursive(9), 34)

    def test_dynamic(self):
        self.assertEqual(self.fibonacci.fibo_dynamic(6), 8)
        self.assertEqual(self.fibonacci.fibo_dynamic(7), 13)
        self.assertEqual(self.fibonacci.fibo_dynamic(8), 21)
        self.assertEqual(self.fibonacci.fibo_dynamic(9), 34)


        
    

if __name__ == '__main__':
    pass