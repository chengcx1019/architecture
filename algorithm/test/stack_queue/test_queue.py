#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_queue.py
@time: 2018/5/28 23:44
"""
import unittest
from basic.stack_queue.queue import Queue


class MyTestCase(unittest.TestCase):
    def tearDown(self):
        self.queue = None

    def setUp(self):
        self.queue = Queue()

    def test_something(self):
        # print('Test: Dequeue an empty queue')
        self.assertEqual(self.queue.dequeue(), None)
        # print('Test: Enqueue to an empty queue')
        self.queue.enqueue(1)

        # print('Test: Dequeue a queue with one element')
        self.assertEqual(self.queue.dequeue(), 1)
        #  print('Test: Enqueue to a non-empty queue')
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        # print('Test: Dequeue a queue with more than one element')
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)


if __name__ == '__main__':
    unittest.main()
