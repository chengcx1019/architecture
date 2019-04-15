#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: PyCharm
@file: test_priority_queue.py
@time: 2018/5/14 00:10
"""
import unittest
from basic.array_string.priority_queue import PriorityQueue, PriorityQueueNode


class TestPriorityQueue(unittest.TestCase):

    def tearDown(self):
        self.priority_queue = None

    def setUp(self):
        self.priority_queue = PriorityQueue()

    def test_priority_queue(self):
        self.assertEqual(self.priority_queue.extract_min(), None)
        self.priority_queue.insert(PriorityQueueNode('a', 20))
        self.priority_queue.insert(PriorityQueueNode('b', 5))
        self.priority_queue.insert(PriorityQueueNode('c', 15))
        self.priority_queue.insert(PriorityQueueNode('d', 22))
        self.priority_queue.insert(PriorityQueueNode('e', 40))
        self.priority_queue.insert(PriorityQueueNode('f', 3))
        self.priority_queue.decrease_key('f', 2)
        self.priority_queue.decrease_key('a', 19)
        mins = []
        while self.priority_queue.array:
            mins.append(self.priority_queue.extract_min().key)
        self.assertEqual(mins, [2, 5, 15, 19, 22, 40])


if __name__ == '__main__':
    pass
