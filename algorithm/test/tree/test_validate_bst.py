#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_validate_bst.py
@time: 2018/5/23 14:45
"""
import unittest

from basic.tree.validate_bst import ValidateBst
from basic.tree.binary_search_tree import BinaryTreeNode as Node, Traversal
from basic.utils.results import Results


class TestBinarySearchTreeBfs(unittest.TestCase):

    def tearDown(self):
        self.bst = None
        self.results = None

    def setUp(self):
        self.bst = ValidateBst()
        self.results = Results()
        self.traversal = Traversal()

    def test_bst(self):
        bst = ValidateBst(Node(5))
        bst.insert(8)
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        self.assertEqual(bst.validate_bst(), True)
        self.traversal.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(self.results.results, [4, 5, 5, 6, 7, 8])
        bst = ValidateBst(Node(5))
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        bst.root.left = left
        bst.root.right = right
        bst.root.left.right = invalid
        self.assertEqual(bst.validate_bst(), False)


if __name__ == '__main__':
    pass
