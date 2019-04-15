#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_one_for_all.py
@time: 2018/9/5 09:58
"""
import unittest

from basic.linked_list.linked_list import ComplexLinkedListNode
from practice.sword2offer.one_for_all_4_19_28 import CloneComplexLinkedList


class MyTestCase(unittest.TestCase):
    def tearDown(self):
        self.test_object = None

    def setUp(self):
        self.test_object = None

    def test_cloen_complex_linkedlist(self):
        head = ComplexLinkedListNode('a')
        node2 = ComplexLinkedListNode('b')
        node3 = ComplexLinkedListNode('c')
        node4 = ComplexLinkedListNode('d')
        node5 = ComplexLinkedListNode('e')
        head.next = node2
        head.sibling = node3
        node2.next = node3
        node2.sibling = node5
        node3.next = node4
        node4.next = node5
        node4.sibling = node2
        ccll = CloneComplexLinkedList()
        clone_head = ccll.clone_complex_linkedlist(head)
        node = clone_head
        while node:
            if node.sibling is not None:
                if node.data == 'a':
                    self.assertEqual(node.sibling.data, 'c')
                elif node.data == 'b':
                    self.assertEqual(node.sibling.data, 'e')
                elif node.data == 'd':
                    self.assertEqual(node.sibling.data, 'b')
            node = node.next


if __name__ == '__main__':
    unittest.main()
