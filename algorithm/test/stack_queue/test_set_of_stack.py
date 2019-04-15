#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_set_of_stack.py
@time: 2018/5/26 21:44
"""

import unittest

from basic.stack_queue.stack import Stack
from basic.linked_list.linked_list import LinkedListNode
from basic.stack_queue.set_of_stack import StackWithCapacity, SetOfStack


class TestSetOfStack(unittest.TestCase):

    def tearDown(self):
        self.stack = None

    def setUp(self):
        self.stack = SetOfStack(stack_capacity=2)

    def test_stack(self):
        self.assertEqual(self.stack.pop(), None)
        self.stack.push(5)
        # print(self.stack.last_stack.head.data)
        self.assertEqual(self.stack.last_stack.head.data, 5)
        self.stack.push(3)
        self.assertEqual(self.stack.last_stack.head.data, 3)
        self.stack.push('a')

        self.assertEqual(self.stack.pop(), 'a')

        self.assertEqual(self.stack.pop(), 3)
        print(self.stack.last_stack.head.data)
        print(self.stack.stacks.__len__())
        self.assertEqual(self.stack.last_stack.head.data, 5)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.pop(), None)
        # stack = StackWithCapacity(None, 2)
        # stacks =  []
        # stacks.append(stack)
        # stack.push(5)
        # self.assertEqual(stack.head.data, 5)
        # self.assertEqual(stacks[0].head.data, 5)




if __name__ == '__main__':
    pass