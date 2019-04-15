#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_min_heap.py
@time: 2018/5/18 18:36
"""
import unittest

from basic.tree.min_heap import MinHeap
from basic.utils.results import Results

class TestMinHeap(unittest.TestCase):

    def tearDown(self):
        self.heap = None


    def setUp(self):
        self.heap = MinHeap()

    def test_bst(self):
        self.assertEqual(self.heap.extra_min(), None)
        self.assertEqual(self.heap.peek_min(), None)
        self.heap.insert(20)
        self.assertEqual(self.heap.array[0], 20)
        self.heap.insert(5)
        self.assertEqual(self.heap.array[0], 5)
        self.assertEqual(self.heap.array[1], 20)
        self.heap.insert(15)
        self.assertEqual(self.heap.array[0], 5)
        self.assertEqual(self.heap.array[1], 20)
        self.assertEqual(self.heap.array[2], 15)
        self.heap.insert(22)
        self.assertEqual(self.heap.array[0], 5)
        self.assertEqual(self.heap.array[1], 20)
        self.assertEqual(self.heap.array[2], 15)
        self.assertEqual(self.heap.array[3], 22)
        self.heap.insert(40)
        self.assertEqual(self.heap.array[0], 5)
        self.assertEqual(self.heap.array[1], 20)
        self.assertEqual(self.heap.array[2], 15)
        self.assertEqual(self.heap.array[3], 22)
        self.assertEqual(self.heap.array[4], 40)
        self.heap.insert(3)
        self.assertEqual(self.heap.array[0], 3)
        self.assertEqual(self.heap.array[1], 20)
        self.assertEqual(self.heap.array[2], 5)
        self.assertEqual(self.heap.array[3], 22)
        self.assertEqual(self.heap.array[4], 40)
        self.assertEqual(self.heap.array[5], 15)
        mins = []
        while self.heap:
            mins.append(self.heap.extra_min())
        self.assertEqual(mins, [3, 5, 15, 20, 22, 40])



if __name__ == '__main__':
    pass