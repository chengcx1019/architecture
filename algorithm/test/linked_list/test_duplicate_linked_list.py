#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_duplicate_linked_list.py
@time: 2018/5/28 16:34
"""
import unittest
from basic.linked_list.duplicate_linked_list import DuplicateLinkedList
from basic.linked_list.linked_list import LinkedListNode


class MyTestCase(unittest.TestCase):
    def tearDown(self):
        self.linked_list = None

    def setUp(self):
        self.linked_list = DuplicateLinkedList()

    def test_something(self):
        option = 3
        self.linked_list.insert(2)
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.get_all(), [2, 3])
        self.linked_list.insert(2)
        self.assertEqual(self.linked_list.get_all(), [2, 2, 3])
        if option == 1:
            self.linked_list.remove_dupes()
        elif option == 2:
            self.linked_list.remove_dupes_in_place()
        else:
            self.linked_list.remove_dupes_single_pointer()
        self.assertEqual(self.linked_list.get_all(), [2, 3])
        self.linked_list.insert(2)
        self.linked_list.insert(2)
        self.linked_list.insert(2)
        self.linked_list.insert(3)
        if option == 1:
            self.linked_list.remove_dupes()
        elif option == 2:
            self.linked_list.remove_dupes_in_place()
        else:
            self.linked_list.remove_dupes_single_pointer()
        self.assertEqual(self.linked_list.get_all(), [3, 2])


if __name__ == '__main__':
    unittest.main()
