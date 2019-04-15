#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_sort_stack.py
@time: 2018/5/29 11:48
"""
from random import randint
import unittest

from basic.stack_queue.sort_stack import SortStack


class MyTestCase(unittest.TestCase):
    def tearDown(self):
        self.test_object = None

    def setUp(self):
        self.test_object = SortStack()

    def test_something(self):
        self.test_object.push(1)

        def get_sorted_number(sorted_buffer):
            sorted_nums = []
            while not sorted_buffer.is_empty():
                sorted_nums.append(sorted_buffer.pop())
            return sorted_nums

        self.assertEqual(get_sorted_number(self.test_object.sort()), [1])

        self.test_object.head = None
        numbers = [randint(0, 10) for x in range(10)]
        print(numbers)
        for num in numbers:
            self.test_object.push(num)
        self.assertEqual(get_sorted_number(self.test_object.sort()), sorted(numbers, reverse=True))


if __name__ == '__main__':
    unittest.main()
