#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_stack.py
@time: 2018/5/26 21:06
"""

import unittest

from basic.stack_queue.stack import Stack
from basic.linked_list.linked_list import LinkedListNode

class TestStack(unittest.TestCase):
    
    def tearDown(self):
        pass

    def setUp(self):
        self.stack = Stack()

    def test_stack(self):
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack.peek(), None)
        # top = LinkedListNode(5)
        # self.stack = Stack(top)
        # self.assertEqual(self.stack.peek(), 5)
        # self.assertEqual(self.stack.pop(), 5)
        # self.assertEqual(self.stack.peek(), None)
        self.stack.push(1)
        self.assertEqual(self.stack.head.data, 1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)


        
    

if __name__ == '__main__':
    pass